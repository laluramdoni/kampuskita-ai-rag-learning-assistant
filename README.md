# ✿ KampusKita AI — Cute, grounded academic assistant

A portfolio-ready, **locally runnable web application** adapted from a published academic chatbot study. A calm pastel user interface meets document-grounded question answering, optional local LLM generation, and a small learning design lab.

> **Research distinction:** The publication studied a Telegram interface with BGE embeddings, VectorStoreIndex and Zephyr-7B-beta. **This is a new web adaptation**, not the original Telegram code and not an official campus product.

## Quick start

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows:    .venv\Scripts\activate
python -m pip install -r requirements.txt
python run.py
```

Visit **http://127.0.0.1:8000**. Without a local model, the app still supports **extractive document demo mode**; it labels this clearly as non-generative.

To enable actual local AI generation:

```bash
# Install Ollama first from https://ollama.com/download
ollama pull llama3.2:3b
# Run Ollama if it is not already running
ollama serve
```

To enable Ollama semantic embeddings as an optional retrieval method:

```bash
ollama pull nomic-embed-text
# macOS/Linux: export USE_OLLAMA_EMBEDDINGS=1
# Windows CMD: set USE_OLLAMA_EMBEDDINGS=1
python run.py
```

> Set environment variables **before** starting Python. See **README_PANDUAN.txt** for detailed instructions in Indonesian.

## Features

- 🩷 Responsive pastel user interface with self-designed CSS mascot
- 🧠 Ollama-powered document Q&A with displayed source excerpts
- 📄 Upload PDFs, TXT and MD; no third-party cloud storage
- 🔎 TF-IDF document retrieval and optional Ollama embeddings
- ✿ Offline non-generative document demo, clearly labeled
- 📚 Three-question learning activity based on the research paper
- ◇ Honest research-to-product comparison

## Technology

Python, FastAPI, Uvicorn, pypdf, scikit-learn, NumPy, Ollama REST API, vanilla HTML/CSS/JavaScript.

## Where the paper is used

The original research paper is included under `data/source_paper.pdf` and imported automatically into the searchable library. The app also includes a concise, source-grounded research brief. Any extra sample learning data is **explicitly marked as simulated**.

## Limitations

This project is for **localhost demo use**. It has no authentication, public-facing document isolation, rate limiting, malware screening, or hardened AI safety layer. Do not deploy publicly unchanged or upload confidential personal records. The paper's reported 100% similarity on two sample questions does not imply generalized accuracy.

Created by **Lalu Ramdoni Hidayat** for educational technology.
