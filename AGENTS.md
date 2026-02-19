# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an experimental sandbox for working with Hugging Face Transformers and PyTorch. The repository contains a simple quick start script demonstrating transformer pipelines (sentiment analysis, text generation).

## Environment Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

**Initial setup:**
```bash
uv sync
```

**Run scripts:**
```bash
uv run python main.py
```

## Environment Configuration

- `.env.example` shows the required environment variables (primarily `HF_TOKEN` for Hugging Face authentication)
- Copy to `.env` and populate with actual values when needed

## Architecture

This is a flat, script-based repository without complex module structure:

- **`main.py`**: Quick start script demonstrating Hugging Face pipelines (sentiment analysis, text generation)
- **`gallery/`**: Self-contained scripts each demonstrating a single pipeline use case (summarization, translation, QA, fill-mask, NER, zero-shot classification, image classification, speech recognition)

All scripts use the high-level `pipeline()` API from Hugging Face Transformers.

## Important Notes

- **README.md must be kept up to date** with any significant project changes
- This is an experimental/learning repository, not a production codebase
- Models are downloaded automatically on first run from Hugging Face Hub
