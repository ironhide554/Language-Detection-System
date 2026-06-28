from transformers import pipeline
import streamlit as st
from models.loader import load_model


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