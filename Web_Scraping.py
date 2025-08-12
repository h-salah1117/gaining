
#امبورت لشوية حاجات 
import os
import time
import requests 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
df = pd.read_csv("imdb_movies.csv")

st.title("🎬 IMDb Top 250 Dashboard")
st.write("Explore top-rated movies on IMDb")

# Sidebar filters
year_filter = st.sidebar.multiselect("Select Year(s)", sorted(df["Year"].unique()))
rating_filter = st.sidebar.slider("Minimum Rating", 0.0, 10.0, 8.0)
# Apply filters
filtered_df = df.copy()
if year_filter:
    filtered_df = filtered_df[filtered_df["Year"].isin(year_filter)]
filtered_df = filtered_df[filtered_df["Rating"] >= rating_filter]

# Table
st.subheader("Filtered Movies")
st.dataframe(filtered_df)

# Chart
fig = px.histogram(filtered_df, x="Rating", nbins=20, title="Ratings Distribution")
st.plotly_chart(fig)

# Top 10
st.subheader("Top 10 Movies by Rating")
top10 = filtered_df.sort_values(by="Rating", ascending=False).head(10)
st.table(top10)


