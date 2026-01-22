# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an experimental sandbox for working with Hugging Face Transformers and PyTorch. The repository contains standalone Python scripts demonstrating various transformer pipeline tasks (sentiment analysis, object detection, image classification, text generation) with optional Gradio UI wrappers.

## Environment Setup

This project uses Conda for dependency management. The environment is named `sandbox-transformers` and includes PyTorch with CUDA 11.8 support.

**Initial setup:**
```bash
conda env create -f environment.yml
source activate-env.sh  # or: conda activate sandbox-transformers
```

**Update environment after modifying environment.yml:**
```bash
conda env update -f environment.yml --prune
```

**Launch Jupyter:**
```bash
jupyter notebook
# or
jupyter lab
```

## Environment Configuration

- `.env.example` shows the required environment variables (primarily `HF_TOKEN` for Hugging Face authentication)
- Copy to `.env` and populate with actual values when needed
- The project uses `python-dotenv` for loading environment variables

## Architecture

This is a flat, script-based repository without complex module structure:

- **Pipeline scripts**: Simple standalone demonstrations of Hugging Face pipelines (`sentiment-analysis.py`, `object-detection.py`)
- **Gradio UI scripts**: Web interfaces for transformer pipelines (`gradio-pipeline-ui.py`, `gradio-pipeline-ui-2.py`)
  - `gradio-pipeline-ui.py`: Image classification with ViT (Vision Transformer)
  - `gradio-pipeline-ui-2.py`: Text generation with GPT-2

All scripts use the high-level `pipeline()` API from Hugging Face Transformers, which abstracts away model loading, preprocessing, and postprocessing.

## Running Scripts

Scripts can be executed directly with Python:
```bash
python sentiment-analysis.py
python object-detection.py
python gradio-pipeline-ui.py  # Launches web UI
python gradio-pipeline-ui-2.py  # Launches web UI
```

Note: Gradio scripts will start a local web server and provide a URL to access the interface.

## Important Notes

- **README.md must be kept up to date** with any significant project changes
- This is an experimental/learning repository, not a production codebase
- Models are downloaded automatically on first run from Hugging Face Hub
- The repository uses PyTorch with CUDA support for GPU acceleration when available
