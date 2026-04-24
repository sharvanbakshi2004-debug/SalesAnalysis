import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Data Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("data/sales_data.csv")

df = load_data()

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.month

st.sidebar.header("Filters")

region = st.sidebar.multiselect("Region", df['Region'].unique(), default=df['Region'].unique())
category = st.sidebar.multiselect("Category", df['Category'].unique(), default=df['Category'].unique())

filtered_df = df[(df['Region'].isin(region)) & (df['Category'].isin(category))]

# KPIs
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", filtered_df['Sales'].sum())
col2.metric("Total Profit", filtered_df['Profit'].sum())
col3.metric("Total Orders", filtered_df.shape[0])

# Monthly Sales
st.subheader("Monthly Sales")
monthly = filtered_df.groupby('Month')['Sales'].sum()
st.line_chart(monthly)

# Category
st.subheader("Sales by Category")
cat = filtered_df.groupby('Category')['Sales'].sum()
st.bar_chart(cat)

# Region
st.subheader("Profit by Region")
reg = filtered_df.groupby('Region')['Profit'].sum()
st.bar_chart(reg)