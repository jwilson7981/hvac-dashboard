import streamlit as st
import os

st.set_page_config(page_title="HVAC Debug", layout="wide")
st.title("📂 Streamlit File Debugger")

st.subheader("🗂️ Files visible to Streamlit:")
files = os.listdir(".")
for f in files:
    st.write(f)

if "Projects.xlsx" in files:
    st.success("✅ Projects.xlsx was found.")
else:
    st.error("❌ Projects.xlsx NOT FOUND. Check file name and repo location.")
