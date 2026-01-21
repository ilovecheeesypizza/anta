%%writefile README.md
# Insider Stock News Intelligence Platform

A Streamlit app that generates insider-style stock intelligence using Grok Cloud.

## Features
- Paste news headlines (one per line)
- Grok generates:
  - Big picture summary
  - Bull signals
  - Bear/risk signals
  - What to watch next
  - Insider score (0-100)

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
