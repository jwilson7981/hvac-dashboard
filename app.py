import streamlit as st
import pandas as pd

st.set_page_config(page_title="HVAC Dashboard", layout="wide")

st.title("Air Tech Mechanical - Project Dashboard")
st.markdown("Below are your currently active projects from `Projects.xlsx`.")

# ✅ Load Excel file
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("Projects.xlsx", sheet_name="Active Projects", engine="openpyxl")
        return df
    except FileNotFoundError:
        st.error("❌ Projects.xlsx not found.")
        return None
    except ValueError:
        st.error("❌ Sheet 'Active Projects' not found in Projects.xlsx.")
        return None

df = load_data()

# ✅ Show table
if df is not None:
    st.dataframe(df, use_container_width=True)
