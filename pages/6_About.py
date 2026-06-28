"""
=========================================================
Project : Language Detection System
File    : 6_About.py
Purpose : About Project
=========================================================
"""

from __future__ import annotations

import streamlit as st
import pandas as pd

from utils.styles import load_css

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="About",
    page_icon="ℹ",
    layout="wide"
)

load_css()

# =====================================================
# Title
# =====================================================

st.title("ℹ About Language Detection System")

st.markdown(
"""
An AI-powered multilingual language detection system
built using **Transformer Models**, **PyTorch**,
**Hugging Face**, and **Streamlit**.

This project demonstrates the complete lifecycle of an
NLP application—from inference and batch processing to
evaluation and analytics.
"""
)

st.divider()

# =====================================================
# Project Overview
# =====================================================

st.header("📌 Project Overview")

st.markdown(
"""
The **Language Detection System** is a production-style
Natural Language Processing application capable of
identifying the language of user-provided text using a
pretrained Transformer model.

The project has been designed to showcase:

- Transformer-based NLP
- Batch inference
- Interactive dashboards
- Model evaluation
- Data visualization
- Modern Streamlit UI
- Exportable reports
"""
)

st.info(
"""
Unlike traditional statistical language detection
methods, this application leverages contextual
Transformer embeddings for more accurate predictions.
"""
)

st.divider()

# =====================================================
# Key Features
# =====================================================

st.header("🚀 Key Features")

features = [

    "🌍 Single Text Language Detection",

    "📂 Batch CSV Language Detection",

    "📊 Interactive Analytics Dashboard",

    "📈 Model Evaluation Dashboard",

    "🤖 Transformer-based Language Detection",

    "📥 Downloadable Reports",

    "📉 Confidence Score Visualization",

    "📚 Model Information",

    "📄 CSV / Excel Export",

    "⚡ Fast Inference"

]

for feature in features:

    st.success(feature)

st.divider()

# =====================================================
# Technologies Used
# =====================================================

st.header("🛠 Technologies")

technology = pd.DataFrame({

    "Technology":[

        "Python",

        "Streamlit",

        "Transformers",

        "PyTorch",

        "Pandas",

        "Plotly",

        "Scikit-Learn",

        "NumPy"

    ],

    "Purpose":[

        "Programming Language",

        "Web Interface",

        "Pretrained Transformer",

        "Deep Learning Framework",

        "Data Processing",

        "Visualization",

        "Evaluation Metrics",

        "Numerical Computing"

    ]

})

st.dataframe(
    technology,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================================================
# Project Workflow
# =====================================================

st.header("🔄 Project Workflow")

st.markdown(
"""
User Input
│
▼
Text Preprocessing
│
▼
Tokenizer
│
▼
Transformer Model
│
▼
Language Prediction
│
▼
Confidence Score
│
▼
Dashboard / Reports

"""
)

st.divider()

# =====================================================
# Folder Structure
# =====================================================

st.header("📁 Project Structure")

st.code(
"""
Language-Detection-System
│
├── models/
├── pages/
├── utils/
├── assets/
├── data/
├── outputs/
├── app.py
├── requirements.txt
└── README.md
""",
language="text"
)

st.divider()

# =====================================================
# System Modules
# =====================================================

st.header("📦 Modules")

modules = pd.DataFrame({

    "Module":[

        "Home",

        "Batch Detection",

        "Dashboard",

        "Evaluation",

        "Model Info",

        "About"

    ],

    "Description":[

        "Single language prediction",

        "Bulk language prediction",

        "Analytics & Charts",

        "Performance evaluation",

        "Model documentation",

        "Project information"

    ]

})

st.dataframe(
    modules,
    use_container_width=True,
    hide_index=True
)

st.divider()