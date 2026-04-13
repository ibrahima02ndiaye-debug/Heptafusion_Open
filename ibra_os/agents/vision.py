import torch
from PIL import Image
import requests

try:
    from transformers import AutoProcessor, AutoModelForVision2Seq
except ImportError:
    AutoProcessor = None
    AutoModelForVision2Seq = None

class VisionAgent:
    def __init__(self, model_id="Qwen/Qwen2-VL-7B-Instruct"):
        self.model_id = model_id
        self.processor = None
        self.model = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def load_model(self):
        if AutoProcessor is None:
            print("Transformers not installed. Skipping model load.")
            return
        print(f"Loading {self.model_id}...")
        self.processor = AutoProcessor.from_pretrained(self.model_id)
        # Using a simplified load for demonstration; in production, use quantization_config
        self.model = AutoModelForVision2Seq.from_pretrained(
            self.model_id,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map="auto" if self.device == "cuda" else None
        )

    def analyze_image(self, image_path, query="Décris cette image."):
        if self.model is None:
            return f"[Mock] Analysis of {image_path}: A mechanical part that needs replacement."

        image = Image.open(image_path if not image_path.startswith('http') else requests.get(image_path, stream=True).raw)
        msgs = [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": query}]}]
        text = self.processor.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
        inputs = self.processor(text=[text], images=[image], return_tensors="pt").to(self.device)
        out = self.model.generate(**inputs, max_new_tokens=150)
        return self.processor.batch_decode(out, skip_special_tokens=True)[0].split("assistant")[-1]
