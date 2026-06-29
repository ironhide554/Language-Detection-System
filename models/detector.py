from transformers import pipeline
import streamlit as st


@st.cache_resource
def load_model():

    return pipeline(
        "text-classification",
        model="papluca/xlm-roberta-base-language-detection",
        top_k=5
    )


class LanguageDetector:

    def __init__(self):

        self.model = load_model()

    def detect(self, text):

        result = self.model(text)[0]

        best = result[0]

        return {
            "language": best["label"],
            "code": best["label"],
            "confidence": round(best["score"] * 100, 2),
            "predictions": result,
        }