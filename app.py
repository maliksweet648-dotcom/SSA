import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="SSA - Smart Safety Automation", layout="wide")

# Read HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Render HTML
components.html(html_code, height=1000, scrolling=True)
