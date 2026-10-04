# JARVIS: Local Linux Terminal Assistant

This project turns your Linux terminal into a lightweight personal AI assistant.

It is designed to be:
- local-first and inexpensive
- safe by default
- useful for day-to-day terminal tasks
- able to use a local Ollama model for free
- able to fall back to a cheap cloud model if you add an API key

Quick start:

1. Install Python dependencies:
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

2. Install Ollama and pull a model:
   curl -fsSL https://ollama.com/install.sh | sh
   ollama pull llama3.1:8b

3. Copy environment settings:
   cp .env.example .env

4. Start the assistant:
   python jarvis.py

Available commands inside the assistant:
- !help
- !ls [path]
- !read [path]
- !write [path] [content]
- !run <shell command>
- !sys
- !clear
- exit

Safety:
- Shell commands are only run after explicit confirmation in the terminal.
- This keeps the assistant useful without turning it into a risky autonomous system.
- It is intended for your personal Linux machine, not for broad unattended automation.

Minimal cost profile:
- $0 with Ollama-only mode
- low cost if you enable a cheap fallback model like Anthropic Haiku for complex reasoning

