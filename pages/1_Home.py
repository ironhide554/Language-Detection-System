import streamlit as st

from models.detector import LanguageDetector
from utils.language_mapping import get_language_name
from utils.helper import create_prediction_dataframe


st.set_page_config(
    page_title="Language Detection",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Language Detection System")

st.write(
    "Detect the language of any text using a Transformer-based multilingual model."
)

detector = LanguageDetector()

text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Type something..."
)

if st.button("🔍 Detect Language"):

    if text.strip() == "":
        st.warning("Please enter some text.")
        st.stop()

    with st.spinner("Detecting language..."):

        result = detector.detect(text)

    language_code = result["language"]

    language_name = get_language_name(language_code)

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Detected Language",
            language_name
        )

    with col2:

        st.metric(
            "Confidence",
            f"{result['confidence']}%"
        )

    st.divider()

    st.subheader("Top Predictions")

    df = create_prediction_dataframe(
        result["predictions"]
    )

    st.dataframe(
        df,
        use_container_width=True
    )