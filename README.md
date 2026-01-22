<div align="center">
  <img src="logo.png" alt="sandbox-transformers" width="512"/>

  **🤗 Sandbox for experimenting with Hugging Face Transformers and PyTorch**

</div>

## Overview

An experimental sandbox for working with Hugging Face Transformers and PyTorch. Contains standalone scripts demonstrating various transformer pipeline tasks with optional Gradio UI wrappers.

## Features

- **Sentiment analysis** - Text sentiment classification
- **Object detection** - Detect objects in images
- **Image classification** - ViT-based image classification
- **Text generation** - GPT-2 text generation
- **Gradio UI** - Web interfaces for interactive demos

## Quick Start

```bash
# Clone and setup
git clone https://github.com/tsilva/sandbox-transformers.git
cd sandbox-transformers

# Create environment
conda env create -f environment.yml
conda activate sandbox-transformers

# Run a script
python sentiment-analysis.py

# Launch Gradio UI
python gradio-pipeline-ui.py
```

## Scripts

| Script | Description |
|--------|-------------|
| `sentiment-analysis.py` | Text sentiment classification |
| `object-detection.py` | Object detection in images |
| `gradio-pipeline-ui.py` | ViT image classification UI |
| `gradio-pipeline-ui-2.py` | GPT-2 text generation UI |

## Requirements

- Python 3.x
- Conda
- CUDA (optional, for GPU acceleration)
- Hugging Face account (for some models)

## License

MIT
