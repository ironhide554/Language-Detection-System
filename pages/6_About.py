
from __future__ import annotations

import streamlit as st
import pandas as pd

from utils.styles import load_css


st.set_page_config(
    page_title="About",
    page_icon="ℹ",
    layout="wide"
)

load_css()


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

st.header("🏗 System Architecture")

st.info(
"""
The application follows a modular architecture where
the user interface, prediction engine, analytics,
and evaluation modules remain independent.
This makes the project scalable and easier to maintain.
"""
)

st.divider()



st.header("🧠 NLP Pipeline")

pipeline = pd.DataFrame({

    "Stage":[
        "Input",
        "Preprocessing",
        "Tokenization",
        "Transformer",
        "Classification",
        "Confidence Estimation",
        "Visualization"
    ],

    "Description":[
        "User enters text",
        "Cleaning and formatting",
        "SentencePiece Tokenizer",
        "XLM-RoBERTa Encoder",
        "Language Prediction",
        "Softmax Probabilities",
        "Dashboard & Reports"
    ]

})

st.dataframe(
    pipeline,
    use_container_width=True,
    hide_index=True
)

st.divider()



st.header("⚙ Processing Steps")

steps = [

    "Receive multilingual text input.",

    "Validate input length.",

    "Tokenize using SentencePiece.",

    "Convert tokens into embeddings.",

    "Pass embeddings through Transformer encoder.",

    "Generate logits for all supported languages.",

    "Apply Softmax to obtain probabilities.",

    "Select Top-K predictions.",

    "Display confidence scores.",

    "Generate analytics and downloadable reports."

]

for i, step in enumerate(steps, start=1):

    st.write(f"**Step {i}:** {step}")

st.divider()


st.header("📊 Evaluation Dataset")

dataset = pd.DataFrame({

    "Property":[
        "Dataset",
        "Languages",
        "Task",
        "Text Type",
        "Evaluation"
    ],

    "Value":[
        "Language Identification Benchmark",
        "20 Supported Languages",
        "Language Classification",
        "Multilingual Sentences",
        "Accuracy, Precision, Recall, F1"
    ]

})

st.dataframe(
    dataset,
    use_container_width=True,
    hide_index=True
)

st.divider()



st.header("🎯 Project Objectives")

objectives = [

    "Develop an end-to-end multilingual language detection application.",

    "Demonstrate Transformer-based Natural Language Processing.",

    "Provide an intuitive user interface for language prediction.",

    "Support both single and batch inference.",

    "Visualize prediction statistics interactively.",

    "Evaluate model performance using benchmark metrics.",

    "Generate downloadable reports for users.",

    "Create a portfolio-ready AI project."

]

for objective in objectives:

    st.success(objective)

st.divider()



st.header("🔥 Challenges Faced")

challenges = [

    "Handling multilingual Unicode text.",

    "Optimizing Transformer inference speed.",

    "Building responsive Streamlit dashboards.",

    "Managing prediction history efficiently.",

    "Supporting multiple export formats.",

    "Maintaining a modular project architecture.",

    "Visualizing evaluation metrics effectively."

]

for challenge in challenges:

    st.warning(challenge)

st.divider()


st.header("🚀 Future Enhancements")

future = [

    "Support 100+ languages.",

    "Real-time speech language detection.",

    "Language translation integration.",

    "REST API deployment using FastAPI.",

    "Docker containerization.",

    "Cloud deployment (AWS / Azure / GCP).",

    "User authentication and saved history.",

    "Custom Transformer fine-tuning.",

    "Automatic language correction.",

    "Explainable AI (XAI) visualizations."

]

for item in future:

    st.info(item)

st.divider()


st.header("📚 Learning Outcomes")

learning = pd.DataFrame({

    "Skill":[
        "Natural Language Processing",
        "Transformer Models",
        "Deep Learning",
        "Streamlit",
        "Data Visualization",
        "Model Evaluation",
        "Software Engineering",
        "Project Deployment"
    ],

    "Knowledge Gained":[
        "Language Detection",
        "XLM-RoBERTa",
        "PyTorch",
        "Interactive Applications",
        "Plotly",
        "Evaluation Metrics",
        "Modular Architecture",
        "Production-ready AI Systems"
    ]

})

st.dataframe(
    learning,
    use_container_width=True,
    hide_index=True
)

st.divider()