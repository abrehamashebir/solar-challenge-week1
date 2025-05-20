import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

import os, sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
# Set the page configuration
from utils import load_data, get_summary_table
st.set_page_config(page_title="Solar Potential Dashboard", page_icon=":guardsman:", layout="wide")
st.title("☀️ Solar Potential Comparison Dashboard")

# app/main.py
# --- Sidebar Controls ---
country_options = ['Benin', 'Sierra Leone', 'Togo']
selected_countries = st.sidebar.multiselect("Select countries to compare", country_options, default=country_options)
selected_metric = st.sidebar.selectbox("Select solar metric", ['GHI', 'DNI', 'DHI'])

# --- Load and Filter Data ---
df = load_data()
df_filtered = df[df['Country'].isin(selected_countries)]

# --- Boxplot ---
st.subheader(f"{selected_metric} Distribution by Country")
fig, ax = plt.subplots()
sns.boxplot(data=df_filtered, x='Country', y=selected_metric, palette='Set2', ax=ax)
st.pyplot(fig)

# --- Summary Table ---
st.subheader("📊 Summary Statistics")
summary = get_summary_table(df_filtered)
st.dataframe(summary)

# --- Top Regions ---
st.subheader(f"🌍 Top Regions by Average {selected_metric}")
top_regions = (
    df_filtered.groupby(['Country'])[selected_metric]
    .mean()
    .reset_index()
    .sort_values(by=selected_metric, ascending=False)
    .head(10)
)
st.table(top_regions)