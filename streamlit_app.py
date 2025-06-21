import streamlit as st

# ✅ Configure page layout at the top!
st.set_page_config(
    page_title="Banking Fraud Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from sqlalchemy import create_engine, text

# ✅ Update with your actual DB password
engine = create_engine('postgresql://postgres:yourpassword@localhost:5432/banking')

# === Load Data ===
@st.cache_data(ttl=10)
def load_data():
    query = "SELECT * FROM transactions ORDER BY timestamp DESC"
    return pd.read_sql(query, engine)

transactions = load_data()

# === Stats ===
total_transactions = len(transactions)
total_frauds = transactions['is_fraud'].sum()

col1, col2 = st.columns(2)
col1.metric("Total Transactions", f"{total_transactions}")
col2.metric("Frauds Detected", f"{total_frauds}")

st.markdown("---")

# === Charts ===
st.subheader("📊 Transaction Type Distribution")
if not transactions.empty:
    type_chart = alt.Chart(transactions).mark_bar().encode(
        x='transaction_type',
        y='count()',
        color='transaction_type'
    ).properties(width=600)
    st.altair_chart(type_chart)

st.subheader("📈 Transaction Volume Over Time")
if not transactions.empty:
    line_chart_data = transactions.copy()
    line_chart_data['timestamp'] = pd.to_datetime(line_chart_data['timestamp'])
    line_chart_data = line_chart_data.groupby(
        pd.Grouper(key='timestamp', freq='1min')
    ).size().reset_index(name='transactions')

    st.line_chart(line_chart_data.rename(columns={'timestamp': 'index'}).set_index('index'))

st.markdown("---")

# === Tables ===
st.subheader("📋 All Transactions")
st.dataframe(transactions, use_container_width=True)

st.subheader("🚨 Flagged Fraud Transactions")
frauds = transactions[transactions['is_fraud'] == True]
st.dataframe(frauds, use_container_width=True)

