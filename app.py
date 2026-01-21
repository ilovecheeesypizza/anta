%%writefile app.py
import streamlit as st
from utils.grok_ai import grok_stock_intelligence

st.set_page_config(page_title="Insider Stock Intel", layout="wide")

st.title("📈 Insider-Style Stock News Intelligence Platform")
st.write("Paste headlines → Get insider intelligence using Grok Cloud ✅")

grok_api_key = st.text_input("Enter Grok API Key", type="password")
hf_token = st.text_input("Enter HuggingFace Token (optional, only storing)", type="password")

stock = st.text_input("Stock Name / Ticker (Example: TSLA, INFY, AAPL)")

headlines = st.text_area(
    "Paste News Headlines (one per line)",
    height=220,
    placeholder="Example:\nTesla shares rise after delivery numbers...\nApple faces regulatory pressure...\nInfosys wins major contract..."
)

if st.button("Generate Insider Intelligence"):
    if not grok_api_key:
        st.error("Please enter Grok API key")
    elif not stock:
        st.error("Please enter stock name/ticker")
    elif not headlines.strip():
        st.error("Please paste some headlines")
    else:
        with st.spinner("Analyzing like an insider..."):
            result = grok_stock_intelligence(
                grok_api_key=grok_api_key,
                stock=stock,
                headlines_text=headlines
            )

        st.subheader("✅ Insider Intelligence Report")
        st.write(result)

        st.subheader("🔐 HuggingFace Token Note")
        st.info("HF token is accepted but not used for models (as you requested).")
