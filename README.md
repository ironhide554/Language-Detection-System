# 🌍 Language Detection System using Transformers

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.47-red.svg)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**An end-to-end Transformer-based multilingual Language Detection System built with Streamlit, Hugging Face Transformers, and PyTorch.**

</div>

---

# 📌 Overview

Language Detection System is a production-style Natural Language Processing (NLP) application capable of identifying the language of user-provided text using a pretrained Transformer model.

The project demonstrates the complete lifecycle of an AI application:

* Language Detection
* Batch Prediction
* Model Evaluation
* Interactive Analytics
* Visualization Dashboard
* Downloadable Reports
* Modern Streamlit Interface

---

# 🚀 Features

## 🌍 Language Detection

* Detect language from any text
* Top-5 predictions
* Confidence score
* Real-time inference

---

## 📂 Batch Detection

* Upload CSV files
* Detect languages in bulk
* Download predictions
* Batch confidence analysis

---

## 📊 Analytics Dashboard

* Prediction statistics
* Confidence distribution
* Language frequency
* Interactive charts
* Prediction history

---

## 📈 Model Evaluation

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Classification Report
* Misclassified Samples

---

## 🤖 Model Information

* Architecture
* Hyperparameters
* Tokenizer Information
* Supported Languages
* Live Inference
* Resource Usage

---

## 📖 About Page

* Project Overview
* Workflow
* Architecture
* Technologies Used
* Future Enhancements
* Learning Outcomes

---

# 🏗 Project Structure

```text
Language-Detection-System/
│
├── assets/
│
├── data/
│
├── models/
│   ├── detector.py
│   ├── evaluator.py
│   ├── history.py
│   ├── loader.py
│   ├── predictor.py
│   └── preprocessor.py
│
├── outputs/
│
├── pages/
│   ├── 1_Home.py
│   ├── 2_Batch_Detection.py
│   ├── 3_Evaluation.py
│   ├── 4_Dashboard.py
│   ├── 5_Model_Info.py
│   └── 6_About.py
│
├── utils/
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 🧠 Model

**Model Name**

```
papluca/xlm-roberta-base-language-detection
```

**Framework**

* Hugging Face Transformers

**Backend**

* PyTorch

**Architecture**

* XLM-RoBERTa

**Task**

* Multilingual Language Detection

---

# ⚙️ Technology Stack

| Category            | Technology                |
| ------------------- | ------------------------- |
| Language            | Python                    |
| UI                  | Streamlit                 |
| Deep Learning       | PyTorch                   |
| NLP                 | Hugging Face Transformers |
| Visualization       | Plotly                    |
| Data Processing     | Pandas                    |
| Machine Learning    | Scikit-Learn              |
| Numerical Computing | NumPy                     |

---

# 🔄 Workflow

```text
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
Dashboard & Reports
```

---

# 📊 Dashboard Features

* KPI Cards
* Confidence Analysis
* Language Distribution
* Interactive Charts
* Prediction History
* Download Reports

---

# 📈 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Classification Report

---

# 💻 Installation

```bash
git clone https://github.com/<your-username>/Language-Detection-System.git

cd Language-Detection-System

python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📂 Supported Pages

| Page              | Description              |
| ----------------- | ------------------------ |
| Home              | Single Text Detection    |
| Batch Detection   | Bulk Language Prediction |
| Evaluation        | Model Evaluation         |
| Dashboard         | Analytics                |
| Model Information | Transformer Details      |
| About             | Project Documentation    |

---

# 🎯 Future Improvements

* Speech Language Detection
* REST API using FastAPI
* Docker Deployment
* User Authentication
* Cloud Deployment
* Mobile Application
* Custom Fine-Tuning
* Explainable AI
* Real-Time Streaming

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

* Natural Language Processing
* Transformer Models
* Hugging Face Transformers
* PyTorch
* Streamlit Development
* Interactive Dashboards
* Model Evaluation
* Software Engineering
* AI Deployment

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Sparsh Tiwari**

B.Tech Computer Science & Engineering (AI & ML)

Passionate about Artificial Intelligence, Machine Learning, Deep Learning, NLP, and Transformer-based Applications.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

</div>
