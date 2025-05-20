import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

import os, sys
current_path = os.getcwd()
parent_dir = os.path.dirname(current_path)
sys.path.insert(0, parent_dir)
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

# --- Barplot ---
st.subheader(f"{selected_metric} Distribution by Country")
fig, ax = plt.subplots()
sns.barplot(data=df_filtered, x='Country', y='GHI', palette='Set2', ax=ax)
st.pyplot(fig)

# --- histplot ---
st.subheader(f"{selected_metric} Distribution by Country")
fig, ax = plt.subplots()
sns.histplot(df['GHI'], kde=True, bins=30, ax=ax, color='blue')
ax.set_title(f"Distribution of {selected_metric} by Country")
ax.set_xlabel(selected_metric)
ax.set_ylabel("Frequency")
# Show the plot in Streamlit
st.pyplot(fig)

# --- scatterplot ---
# selected_metric should come from a widget like st.selectbox
selected_metric = st.selectbox("Select metric(X)", ["GHI", "DNI", "DHI"])
selected_metric1 = st.selectbox("Select metric (Y)", ["GHI", "DNI", "DHI"])
st.subheader(f"{selected_metric} Distribution by Country")

fig, ax = plt.subplots()
sns.scatterplot(x=selected_metric, y=selected_metric1, data=df, ax=ax)
ax.set_title(f"Scatterplot of GHI by Country")
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