
from __future__ import annotations

import streamlit as st
import pandas as pd

from models.loader import load_model
from utils.styles import load_css


st.set_page_config(
    page_title="Model Information",
    page_icon="🤖",
    layout="wide",
)

load_css()


# Load Model


@st.cache_resource
def get_model():

    return load_model()
    
assets = get_model()

model = assets["model"]

tokenizer = assets["tokenizer"]

config = assets["config"]


# Title


st.title("🤖 Model Information")

st.markdown(
"""
Explore the architecture, configuration, performance,
and capabilities of the Transformer Language Detection Model.
"""
)

st.divider()


# Model Overview


st.header("📌 Model Overview")

col1, col2 = st.columns([1,2])

with col1:

    st.image(
        "https://huggingface.co/front/assets/huggingface_logo.svg",
        width=170,
    )

with col2:

    st.markdown(
"""
### papluca/xlm-roberta-base-language-detection

A multilingual Transformer model fine-tuned for
language identification using XLM-RoBERTa.

The model can accurately detect multiple languages
from short or long text using contextual embeddings.

It is lightweight, fast, and suitable for
real-time language detection applications.
"""
    )

st.divider()


# Model Cards


metric1, metric2, metric3, metric4 = st.columns(4)

metric1.metric(
    "Architecture",
    "XLM-RoBERTa"
)

metric2.metric(
    "Framework",
    "Transformers"
)

metric3.metric(
    "Task",
    "Language Detection"
)

metric4.metric(
    "Backend",
    "PyTorch"
)

metric5, metric6, metric7, metric8 = st.columns(4)

metric5.metric(
    "Languages",
    "20"
)

metric6.metric(
    "Tokenizer",
    "SentencePiece"
)

metric7.metric(
    "License",
    "MIT"
)

metric8.metric(
    "Inference",
    "CPU/GPU"
)

st.divider()


# Architecture


st.header("🏗 Model Architecture")

st.markdown(
"""
The language detection system is based on **XLM-RoBERTa**,
a multilingual Transformer encoder developed by Facebook AI.

Pipeline:

Text Input

⬇

SentencePiece Tokenizer

⬇

XLM-RoBERTa Encoder

⬇

Pooling Layer

⬇

Classification Head

⬇

Language Probability Distribution
"""
)

st.info(
"""
Unlike traditional machine learning methods,
Transformer models understand contextual
relationships between words, enabling
robust language detection even for
short text snippets.
"""
)

st.divider()


# Hyperparameters


st.header("⚙ Model Hyperparameters")

config = config

parameters = pd.DataFrame({

    "Parameter":[
        "Hidden Size",
        "Number of Layers",
        "Attention Heads",
        "Vocabulary Size",
        "Maximum Position Embeddings",
        "Hidden Dropout",
        "Attention Dropout",
        "Model Type"
    ],

    "Value":[
        config.hidden_size,
        config.num_hidden_layers,
        config.num_attention_heads,
        config.vocab_size,
        config.max_position_embeddings,
        config.hidden_dropout_prob,
        config.attention_probs_dropout_prob,
        config.model_type
    ]

})

st.dataframe(
    parameters,
    use_container_width=True,
    hide_index=True
)

st.divider()

# Tokenizer Information


st.header("📝 Tokenizer")

tokenizer = tokenizer

tokenizer_df = pd.DataFrame({

    "Property":[
        "Tokenizer Class",
        "Model Maximum Length",
        "Padding Side",
        "Truncation Side",
        "Vocabulary Size"
    ],

    "Value":[
        tokenizer.__class__.__name__,
        tokenizer.model_max_length,
        tokenizer.padding_side,
        tokenizer.truncation_side,
        tokenizer.vocab_size
    ]

})

st.dataframe(
    tokenizer_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# Supported Languages


st.header("🌍 Supported Languages")

supported_languages = pd.DataFrame({

    "Language Code":[
        "ar","bg","de","el","en",
        "es","fr","hi","it","ja",
        "nl","pl","pt","ru","sw",
        "th","tr","ur","vi","zh"
    ],

    "Language":[
        "Arabic",
        "Bulgarian",
        "German",
        "Greek",
        "English",
        "Spanish",
        "French",
        "Hindi",
        "Italian",
        "Japanese",
        "Dutch",
        "Polish",
        "Portuguese",
        "Russian",
        "Swahili",
        "Thai",
        "Turkish",
        "Urdu",
        "Vietnamese",
        "Chinese"
    ]

})

search = st.text_input(
    "🔍 Search Language"
)

filtered_languages = supported_languages.copy()

if search:

    filtered_languages = filtered_languages[
        filtered_languages.astype(str)
        .apply(
            lambda row:
            row.str.lower().str.contains(
                search.lower()
            )
        )
        .any(axis=1)
    ]

st.dataframe(
    filtered_languages,
    use_container_width=True,
    hide_index=True
)

st.divider()


# Model Performance


st.header("📈 Model Performance")

metric1, metric2, metric3, metric4 = st.columns(4)

metric1.metric(
    "Accuracy",
    "~99.6%"
)

metric2.metric(
    "Precision",
    "~99.6%"
)

metric3.metric(
    "Recall",
    "~99.6%"
)

metric4.metric(
    "F1 Score",
    "~99.6%"
)

st.caption(
"""
Performance values are based on the model's published benchmark
and may vary depending on the evaluation dataset and preprocessing.
"""
)

st.divider()
