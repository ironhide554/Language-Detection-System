from transformers import pipeline
import streamlit as st
from utils.language_mapping import get_language_name


@st.cache_resource
def load_model():

    detector = pipeline(
        task="text-classification",
        model="papluca/xlm-roberta-base-language-detection",
        top_k=5,
    )

    return detector


class LanguageDetector:

    def __init__(self):

        self.model = load_model()

    def detect(self, text: str):

        result = self.model(text)[0]

        top_prediction = result[0]

        return {

            "language": top_prediction["label"],

            # ISO language code
            "code": top_prediction["label"],

            "confidence": round(
                top_prediction["score"] * 100,
                2,
            ),

            "predictions": result,

            "text": text,
        }