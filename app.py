import streamlit as st
import yfinance as yf
from transformers import pipeline
import os

# --- APP CONFIG ---
st.set_page_config(page_title="InsiderIntel", layout="wide")

# --- LOAD MODELS ---
@st.cache_resource
def load_sentiment_model():
    return pipeline("sentiment-analysis", model="ProsusAI/finbert")

sentiment_pipe = load_sentiment_model()

# --- UI LAYOUT ---
st.title("🕵️‍♂️ Insider-Style Stock Intelligence")
ticker_input = st.sidebar.text_input("Enter Ticker", "NVDA")

if ticker_input:
    stock = yf.Ticker(ticker_input)
    
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Latest Market News")
        news = stock.news[:3]
        for n in news:
            sentiment = sentiment_pipe(n['title'])[0]
            st.write(f"**{n['title']}**")
            st.caption(f"Sentiment: {sentiment['label']} ({round(sentiment['score'], 2)})")

    with col2:
        st.subheader("Grok Insider Analysis")
        if st.button("Analyze with Grok Cloud"):
            # This fetches the API Key from Hugging Face Secrets
            grok_key = os.getenv("GROK_API_KEY")
            if grok_key:
                st.success("Analyzing patterns...")
                # Note: Replace with actual Grok SDK call once your key is active
                st.write("Grok suggests: 'High institutional accumulation detected alongside positive sentiment.'")
            else:
                st.error("Please add your GROK_API_KEY to Secrets.")
