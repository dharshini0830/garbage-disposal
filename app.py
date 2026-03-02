import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("your_file.csv")
df['Date'] = pd.to_datetime(df['Date'])

st.title("School Waste Dashboard")

# Line chart
st.subheader("Daily Waste Trends")
daily = df.groupby('Date')[['Recyclable', 'Organic', 'Inorganic']].sum()
st.line_chart(daily)

# Pie chart
st.subheader("Total Waste Composition")
total = df[['Recyclable', 'Organic', 'Inorganic']].sum()
st.pyplot(total.plot.pie(autopct='%1.1f%%', figsize=(5, 5)).figure)
