import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Hotel Staff Dashboard", layout="wide")

st.title("📊 Real-time Hotel Staff Dashboard")

# Sample guest requests
sample_data = [
    {"Guest": "John", "Request": "Need 2 towels", "Status": "Pending"},
    {"Guest": "Sara", "Request": "Room Cleaning", "Status": "In Progress"},
    {"Guest": "Liam", "Request": "Order breakfast", "Status": "Completed"},
]

df = pd.DataFrame(sample_data)
st.dataframe(df, use_container_width=True)

# Sentiment Analysis Mockup
st.subheader("📈 Guest Sentiment Summary")
sentiment_data = {
    "Positive": random.randint(50, 70),
    "Neutral": random.randint(20, 30),
    "Negative": random.randint(5, 10),
}
st.bar_chart(sentiment_data)