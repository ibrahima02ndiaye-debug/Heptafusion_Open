import torch
import numpy as np
from transformers import AutoModelForCausalLM
from tqdm import tqdm
import os

def weighted_average(tensors, weights):
    """
    Computes the weighted average of a list of tensors.
    """
    assert len(tensors) == len(weights)
    total_weight = sum(weights)
    res = tensors[0] * (weights[0] / total_weight)
    for i in range(1, len(tensors)):
        res += tensors[i] * (weights[i] / total_weight)
    return res

def slerp(t1, t2, lerp, dot_threshold=0.9995):
    """
    Spherical Linear Interpolation between two tensors.
    """
    # Normalize the vectors to get the dot product of the angle between them
    t1_norm = t1 / (torch.norm(t1) + 1e-10)
    t2_norm = t2 / (torch.norm(t2) + 1e-10)

    dot = torch.sum(t1_norm * t2_norm)

    # If the inputs are too close, use linear interpolation
    if torch.abs(dot) > dot_threshold:
        return (1 - lerp) * t1 + lerp * t2

    # Calculate initial angle between v0 and v1
    theta_0 = torch.acos(dot)
    theta = theta_0 * lerp

    t3 = t2 - t1 * dot
    t3 = t3 / (torch.norm(t3) + 1e-10)

    return torch.cos(theta) * t1 + torch.sin(theta) * t3

def dare_linear(tensors, weights, density=0.9):
    """
    DARE (Drop And REscale) Linear merging.
    Note: merging should be done in FP16/BF16/FP32.
    """
    # Use the first tensor (base model) as anchor
    base_tensor = tensors[0]

    total_delta = torch.zeros_like(base_tensor)

    for i in range(1, len(tensors)):
        delta = tensors[i] - base_tensor

        # Masking (Drop)
        mask = torch.bernoulli(torch.full_like(delta, density))
        delta = delta * mask

        # Rescale
        delta = delta / density

        total_delta += delta * weights[i]

    return base_tensor + total_delta

def merge_models(base_model_path, model_paths, method="weighted_average", weights=None, lerp=0.5, output_path="./fused-model"):
    """
    Loads models and merges their state dicts.
    Merging is performed in FP16 to ensure mathematical correctness.
    """
    print(f"Loading base model: {base_model_path}")
    # Load in float16 for merging precision
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_path,
        torch_dtype=torch.float16,
        device_map="cpu" # Merging usually done on CPU to avoid VRAM issues if multiple models are loaded
    )
    base_state_dict = base_model.state_dict()

    model_state_dicts = []
    for path in model_paths:
        print(f"Loading model to merge: {path}")
        model = AutoModelForCausalLM.from_pretrained(
            path,
            torch_dtype=torch.float16,
            device_map="cpu"
        )
        model_state_dicts.append(model.state_dict())

    new_state_dict = {}
    keys = base_state_dict.keys()

    if weights is None:
        weights = [1.0] * (len(model_paths) + 1)

    for key in tqdm(keys, desc="Merging weights"):
        tensors = [base_state_dict[key]] + [sd[key] for sd in model_state_dicts]

        if method == "weighted_average":
            new_state_dict[key] = weighted_average(tensors, weights)
        elif method == "slerp" and len(tensors) == 2:
            new_state_dict[key] = slerp(tensors[0], tensors[1], lerp)
        elif method == "dare_linear":
            new_state_dict[key] = dare_linear(tensors, weights)
        else:
            # Fallback to base model if method not supported or incompatible
            new_state_dict[key] = base_state_dict[key]

    base_model.load_state_dict(new_state_dict)
    print(f"Saving merged model to {output_path}")
    base_model.save_pretrained(output_path)
