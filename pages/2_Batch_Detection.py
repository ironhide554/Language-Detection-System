import streamlit as st
import pandas as pd

from models.detector import LanguageDetector
from models.predictor import BatchPredictor
from utils.styles import load_css

load_css()

from utils.helper import (
    dataframe_to_csv,
    dataframe_to_excel,
)

from utils.metrics import calculate_statistics
from utils.charts import language_distribution

st.title("📂 Batch Language Detection")

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.write("Preview")

    st.dataframe(df.head())

    text_column = st.selectbox(
        "Select Text Column",
        df.columns
    )

    detector = LanguageDetector()

    predictor = BatchPredictor(detector)

    if st.button("Start Detection"):

        progress = st.progress(0)

        result = predictor.predict_dataframe(
            df,
            text_column,
            progress.progress
        )

        st.success("Detection Completed")

        st.dataframe(result)

        statistics = calculate_statistics(result)

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Samples",
            statistics["Total Samples"]
        )

        col2.metric(
            "Languages",
            statistics["Unique Languages"]
        )

        col3.metric(
            "Avg Confidence",
            f'{statistics["Average Confidence"]}%'
        )

        st.plotly_chart(
            language_distribution(result),
            use_container_width=True
        )

        st.download_button(
            "⬇ Download CSV",
            dataframe_to_csv(result),
            "predictions.csv",
            "text/csv"
        )

        st.download_button(
            "⬇ Download Excel",
            dataframe_to_excel(result),
            "predictions.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )