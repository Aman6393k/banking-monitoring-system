import streamlit as st
st.set_page_config(page_title="Banking Dashboard", layout="wide")

import pandas as pd
import psycopg2
import plotly.express as px

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="transactions",
    user="admin",
    password="admin"
)

# Load data
df = pd.read_sql("SELECT * FROM transactions", conn)

# Sidebar filters
st.sidebar.header("Filters")
locations = st.sidebar.multiselect("Select Location(s)", options=df["location"].unique(), default=df["location"].unique())

filtered_df = df[df["location"].isin(locations)]

# Title
st.title("💳 Banking Transaction Monitoring Dashboard")

# KPIs
col1, col2 = st.columns(2)
col1.metric("Total Transactions", len(filtered_df))
col2.metric("Total Fraudulent", int(filtered_df["is_fraud"].sum()))

# Fraud by location
fraud_by_location = (
    filtered_df.groupby("location")["is_fraud"]
    .sum()
    .reset_index()
    .sort_values(by="is_fraud", ascending=False)
)

fig = px.bar(fraud_by_location, x="location", y="is_fraud", title="Fraudulent Transactions by Location")
st.plotly_chart(fig, use_container_width=True)

# Show raw data
with st.expander("View Data Table"):
    st.dataframe(filtered_df)
import streamlit as st

import pandas as pd
import psycopg2
import plotly.express as px

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="transactions",
    user="admin",
    password="admin"
)

# Fetch data
df = pd.read_sql("SELECT * FROM transactions", conn)

# Sidebar filter
st.sidebar.header("Filter")
if 'location' in df.columns:
    selected_location = st.sidebar.selectbox("Select Location", df['location'].unique())
    df = df[df['location'] == selected_location]

# Dashboard header
st.title("💳 Banking Transaction Monitoring Dashboard")

# Metrics
col1, col2 = st.columns(2)
col1.metric("Total Transactions", len(df))
if 'is_fraud' in df.columns:
    col2.metric("Fraudulent Transactions", int(df['is_fraud'].sum()))
else:
    col2.warning("⚠️ 'is_fraud' column missing")

# Chart
if 'is_fraud' in df.columns:
    fig = px.histogram(df, x="amount", color="is_fraud", barmode="group",
                       title="Transaction Amounts by Fraud Status")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No fraud data to visualize")

conn.close()
import streamlit as st
import pandas as pd
import psycopg2
import altair as alt

# Database connection (update with your credentials)
conn = psycopg2.connect(
    host='localhost',
    port='5432',
    dbname='transactions',
    user='admin',
    password='admin'
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM transactions")
data = cursor.fetchall()
columns = ['transaction_id', 'timestamp', 'amount', 'sender_account', 'receiver_account', 'location', 'is_fraud']
df = pd.DataFrame(data, columns=columns)

# Convert timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Title
st.title("\U0001F4B3 Banking Transaction Monitoring Dashboard")

# Summary metrics
st.metric("Total Transactions", len(df))
st.metric("Total Fraudulent", df['is_fraud'].sum())
st.metric("Fraud %", f"{(df['is_fraud'].mean()*100):.2f}%")

# Filter: Location
locations = df['location'].unique().tolist()
selected_location = st.selectbox("Filter by Location", ["All"] + locations)
if selected_location != "All":
    df = df[df['location'] == selected_location]

# Filter: Amount Range
min_amt, max_amt = int(df['amount'].min()), int(df['amount'].max())
amount_range = st.slider("Select Amount Range", min_amt, max_amt, (min_amt, max_amt))
df = df[(df['amount'] >= amount_range[0]) & (df['amount'] <= amount_range[1])]

# Filter: Date Range
date_range = st.date_input("Select Date Range", [df['timestamp'].min(), df['timestamp'].max()])
if len(date_range) == 2:
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    df = df[(df['timestamp'] >= start_date) & (df['timestamp'] <= end_date)]

# Visualization: Fraud vs Non-Fraud
st.subheader("Fraud vs Non-Fraud Transactions")
fraud_chart = alt.Chart(df).mark_bar().encode(
    x='is_fraud:N',
    y='count()',
    color='is_fraud:N'
).properties(
    width=400,
    height=300
)
st.altair_chart(fraud_chart)

# Visualization: Transactions by Location
st.subheader("Transactions by Location")
loc_chart = alt.Chart(df).mark_bar().encode(
    x='location:N',
    y='count()',
    color='is_fraud:N'
).properties(
    width=600,
    height=400
)
st.altair_chart(loc_chart)

# Download data
st.download_button(
    label="Download Filtered Data as CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name='filtered_transactions.csv',
    mime='text/csv'
)

# Show filtered data table
st.subheader("Filtered Transactions")
st.dataframe(df)
import streamlit as st
import pandas as pd
import psycopg2


st.title("💳 Banking Transaction Monitoring Dashboard")

conn = psycopg2.connect(
    host="localhost",
    database="transactions",
    user="admin",
    password="admin"
)
df = pd.read_sql("SELECT * FROM transactions", conn)

st.metric("Total Transactions", len(df))
st.metric("Total Fraudulent", df['is_fraud'].sum())
st.dataframe(df.sort_values(by="timestamp", ascending=False).head(10))

