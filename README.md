<div align="center">
  <img src="logo.png" alt="sandbox-transformers" width="256"/>

  # sandbox-transformers

  [![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
  [![PyTorch](https://img.shields.io/badge/PyTorch-CUDA%2011.8-ee4c2c.svg)](https://pytorch.org/)
  [![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow.svg)](https://huggingface.co/docs/transformers)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  **Hands-on experimentation sandbox for transformer models using PyTorch and Hugging Face**

  [Hugging Face Docs](https://huggingface.co/docs/transformers) · [PyTorch Docs](https://pytorch.org/docs/stable/index.html)
</div>

## Overview

A learning playground for experimenting with state-of-the-art transformer models. Includes standalone scripts demonstrating various Hugging Face pipelines and Gradio-powered web interfaces for interactive exploration.

## Features

- **Sentiment Analysis** - Classify text sentiment using pre-trained models
- **Object Detection** - Detect objects in images with bounding boxes
- **Image Classification** - Classify images using Vision Transformer (ViT)
- **Text Generation** - Generate text continuations with GPT-2
- **Gradio UIs** - Interactive web interfaces for real-time experimentation

## Quick Start

```bash
# Clone and setup
git clone https://github.com/tsilva/sandbox-transformers.git
cd sandbox-transformers
conda env create -f environment.yml
conda activate sandbox-transformers

# Run a demo
python sentiment-analysis.py
```

## Installation

### Prerequisites

- [Conda](https://docs.conda.io/en/latest/miniconda.html) package manager
- NVIDIA GPU with CUDA support (optional, for acceleration)

### Environment Setup

```bash
# Create the conda environment
conda env create -f environment.yml

# Activate the environment
conda activate sandbox-transformers

# Or use the helper script
source activate-env.sh
```

### Update Environment

After modifying `environment.yml`:

```bash
conda env update -f environment.yml --prune
```

### Hugging Face Token (Optional)

For gated models, copy `.env.example` to `.env` and add your token:

```bash
cp .env.example .env
# Edit .env and add your HF_TOKEN
```

## Usage

### Pipeline Scripts

Run standalone demonstrations of Hugging Face pipelines:

```bash
# Sentiment analysis
python sentiment-analysis.py
# Output: [{'label': 'POSITIVE', 'score': 0.9998}]

# Object detection
python object-detection.py
# Output: Detected objects with bounding boxes
```

### Gradio Web Interfaces

Launch interactive web UIs:

```bash
# Image classification with Vision Transformer
python gradio-pipeline-ui.py

# Text generation with GPT-2
python gradio-pipeline-ui-2.py
```

Open the provided URL in your browser to interact with the models.

### Jupyter Notebooks

```bash
jupyter notebook
# or
jupyter lab
```

## Tech Stack

| Component | Purpose |
|-----------|---------|
| PyTorch | Deep learning framework with CUDA support |
| Transformers | Hugging Face's transformer model library |
| Gradio | Web UI for ML model demos |
| Pillow | Image processing |
| NumPy | Numerical computing |
| Jupyter | Interactive development |

## Project Structure

```
sandbox-transformers/
├── sentiment-analysis.py      # Text sentiment classification
├── object-detection.py        # Image object detection
├── gradio-pipeline-ui.py      # ViT image classification UI
├── gradio-pipeline-ui-2.py    # GPT-2 text generation UI
├── environment.yml            # Conda dependencies
├── .env.example               # Environment variables template
└── activate-env.sh            # Environment activation helper
```

## Contributing

This is an experimental/learning repository. Feel free to fork and experiment!

## License

MIT
