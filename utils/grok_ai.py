%%writefile utils/grok_ai.py
import requests

def grok_stock_intelligence(grok_api_key, stock, headlines_text):
    url = "https://api.x.ai/v1/chat/completions"

    prompt = f"""
You are an Insider-style Stock News Intelligence Analyst.

Stock: {stock}

News Headlines:
{headlines_text}

Give output in this format:

1) Big Picture Summary (3 lines)
2) Bull Signals (3 points)
3) Bear/Risk Signals (3 points)
4) What Investors Should Watch Next (3 points)
5) Insider Score (0-100) + one-line reason

Keep it short, sharp, and actionable.
"""

    headers = {
        "Authorization": f"Bearer {grok_api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "grok-beta",
        "messages": [
            {"role": "system", "content": "You give stock market intelligence clearly."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        return f"ERROR: Grok API failed ({response.status_code}) - {response.text}"

    return response.json()["choices"][0]["message"]["content"]
