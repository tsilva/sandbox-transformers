<div align="center">
  <img src="logo.png" alt="sandbox-transformers" width="512"/>

  [![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
  [![Transformers](https://img.shields.io/badge/Transformers-v5-orange.svg)](https://huggingface.co/docs/transformers)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  **🤗 Sandbox for Hugging Face Transformers and PyTorch 🔥**

</div>

## 🚀 Quick Start

```bash
git clone https://github.com/tsilva/sandbox-transformers.git
cd sandbox-transformers
uv sync
uv run python main.py
```

## ✨ What It Does

Runs a simple Transformers pipeline demo in `main.py`:

- **Sentiment analysis** — classifies text as positive/negative
- **Text generation** — generates text continuations with GPT-2

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
classifier(["I love this!", "This is terrible."])
# [{'label': 'POSITIVE', 'score': 0.9998}, {'label': 'NEGATIVE', 'score': 0.9994}]
```

## 🖼️ Gallery

Self-contained scripts in `gallery/` demonstrating individual pipelines:

| Use Case | Script |
|----------|--------|
| Summarization | `uv run python gallery/summarization.py` |
| Translation (EN→FR) | `uv run python gallery/translation.py` |
| Question Answering | `uv run python gallery/question_answering.py` |
| Fill Mask | `uv run python gallery/fill_mask.py` |
| Named Entity Recognition | `uv run python gallery/ner.py` |
| Zero-Shot Classification | `uv run python gallery/zero_shot_classification.py` |
| Image Classification | `uv run python gallery/image_classification.py` |
| Speech Recognition | `uv run python gallery/automatic_speech_recognition.py` |

## 📋 Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- CUDA (optional, for GPU acceleration)

## 📄 License

MIT

## License

MIT
