import streamlit as st

st.set_page_config(
    page_title="Language Detection System",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌍 Language Detection System")

st.markdown(
    """
    Welcome to the **Language Detection System**.

    Use the navigation menu on the left to access:

    - 🏠 Home
    - 📂 Batch Detection
    - 📊 Evaluation
    - 📈 Dashboard
    - 🤖 Model Information
    - ℹ️ About
    """
)

st.info(
    "Phase 1 completed successfully. The application structure is ready."
)