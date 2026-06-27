import streamlit as st

st.set_page_config(
    page_title="Language Detection System",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌍 Language Detection System")

st.success(
    "Use the navigation menu on the left to access the application pages."
)

st.markdown(
"""
## Features

- Single Text Detection
- Batch Detection (Coming Soon)
- Evaluation on WiLI-2018
- Dashboard
- Model Information
- Export Results
"""
)