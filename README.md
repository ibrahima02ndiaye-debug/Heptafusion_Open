# Ibra-OS: Multi-Agent AI System for Ibra Services Inc.

Ibra-OS is an advanced, multi-agent ecosystem designed to modernize and automate the operations of a mechanical garage (Ibra Services Inc.) in Trois-Rivières. It leverages cutting-edge AI architectures, including Vision-Language Models (VLM), World Models (JEPA), and multi-agent orchestration.

## Core Components

- **Vision Agent**: Uses Qwen2-VL for diagnostic imaging and part identification.
- **Web Agent**: Searches for parts pricing and availability (e.g., via DuckDuckGo Search).
- **Docs Agent**: RAG (Retrieval-Augmented Generation) over technical manuals and PDFs stored on Google Drive.
- **Memory Agent**: Persistent storage of client history and vehicle data using SQLite.
- **Perception Agent (JEPA)**: Implements Joint Embedding Predictive Architecture for physical world understanding and robotic guidance.
- **Vocal/Secretary Agent**: Provides a natural language interface (STT/TTS) for hands-free operation in the garage.
- **Orchestrator**: Coordinates tasks between specialized agents to solve complex business queries.

## Technologies

- **Models**: Qwen2-VL, Gemma, GLM-4, I-JEPA.
- **Frameworks**: Transformers, Accelerate, BitsAndBytes, Mergekit, LiteLLM, MCP (Model Context Protocol).
- **Storage**: SQLite, Google Drive integration.
- **Interface**: Faster-Whisper (STT), Piper (TTS).

## Project Goal
To transform a traditional garage into a high-tech, AI-driven service center with automated diagnostics, client management, and robotic assistance.
