# Local Q&A AI Agent

A privacy‑preserving AI agent that can read your personal notes, PDFs, and documents, and answer questions about them with **citations**.  
Runs entirely on your own machine — no cloud uploads, no API costs, and no risk of exposing sensitive information.

---

## Features
- Semantic search across your own documents (e.g., *“What is LangChain used for?”*).
- Cited answers so you know exactly which file and section the response came from.
- Local execution — nothing leaves your computer.
- Free to use — no API keys, no subscription fees.
- Works on macOS, Windows, and Linux.

---

## Requirements
- [Ollama](https://ollama.ai) installed on your machine.
- A supported model (e.g., Qwen family).  
  - Large models benefit from more RAM (e.g., 32 GB on MacBook Pro).  
  - Smaller Qwen models can run on lower‑memory machines.

---

## Getting Started

1. **Install Ollama**  
   Follow instructions from [Ollama’s website](https://ollama.ai).

2. **Clone this repository**  
   ```bash
   git clone https://github.com/yourusername/local-qa-agent.git
   cd local-qa-agent
