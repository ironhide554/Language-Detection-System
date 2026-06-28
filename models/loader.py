from __future__ import annotations

import streamlit as st

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
)

MODEL_NAME = "papluca/xlm-roberta-base-language-detection"


@st.cache_resource(show_spinner=False)
def load_model():
    """
    Loads the tokenizer and transformer model only once.
    """

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME
    )

    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME
    )

    model.eval()

    return {
        "tokenizer": tokenizer,
        "model": model,
        "config": model.config,
        "model_name": MODEL_NAME,
    }