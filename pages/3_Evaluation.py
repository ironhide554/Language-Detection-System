
from __future__ import annotations

import pandas as pd
import streamlit as st



from models.evaluator import ModelEvaluator


from utils.styles import load_css


st.set_page_config(
    page_title="Model Evaluation",
    page_icon="📊",
    layout="wide",
)

load_css()


st.title("📊 Model Evaluation")

st.markdown(
"""
Evaluate the Transformer Language Detection model
using the **WiLI-2018** dataset.
"""
)


with st.sidebar:

    st.header("Evaluation Settings")

    

    sample_limit = st.number_input(
        "Maximum Samples",
        min_value=100,
        max_value=50000,
        value=1000,
        step=100
    )



from datasets import load_dataset

with st.spinner("Loading evaluation dataset..."):

    dataset = load_dataset(
        "papluca/language-identification",
        split="test",
    )

    dataset = dataset.to_pandas()

dataset = dataset.rename(
    columns={
        "text": "Text",
        "labels": "Language Code",
    }
)

dataset = dataset.head(sample_limit)

st.success(
    f"Loaded {len(dataset)} evaluation samples."
)



st.subheader("Dataset Information")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Samples",
    len(dataset)
)

col2.metric(
    "Languages",
    dataset["Language Code"].nunique()
)

col3.metric(
    "Missing",
    dataset.isnull().sum().sum()
)

distribution = (
    dataset["Language Code"]
    .value_counts()
    .reset_index()
)

distribution.columns = [
    "Language",
    "Count"
]

with st.expander(
    "Language Distribution",
    expanded=False
):

    st.dataframe(
        distribution,
        use_container_width=True
    )


st.subheader("Dataset Preview")

st.dataframe(
    dataset.head(20),
    use_container_width=True,
    height=500
)

st.divider()



run_evaluation = st.button(
    "🚀 Start Evaluation",
    use_container_width=True
)

if not run_evaluation:

    st.stop()



evaluator = ModelEvaluator()

progress = st.progress(0)

status = st.empty()

status.info(
    "Preparing evaluation..."
)



status.info("Running model evaluation...")

results = evaluator.evaluate(
    dataframe=dataset,
    text_column="Text",
    label_column="Language Code",
    progress_callback=progress.progress,
)

st.write("Evaluation Keys")

st.write(results.keys())

st.write("Prediction DataFrame")

st.write(results["predictions"].head())

st.write("Prediction Shape")

st.write(results["predictions"].shape)

progress.progress(1.0)

status.success("Evaluation completed successfully!")



prediction_df = results["predictions"]

accuracy = results["accuracy"]

precision = results["precision"]

recall = results["recall"]

f1_score = results["f1_score"]

processing_time = results["processing_time"]

texts_per_second = results["texts_per_second"]

correct_predictions = results["correct_predictions"]

incorrect_predictions = results["incorrect_predictions"]

classification_report = results["classification_report"]

confusion_matrix = results["confusion_matrix"]



st.divider()

st.header("📈 Evaluation Metrics")

row1 = st.columns(4)

row1[0].metric(
    "Accuracy",
    f"{accuracy}%"
)

row1[1].metric(
    "Precision",
    f"{precision}%"
)

row1[2].metric(
    "Recall",
    f"{recall}%"
)

row1[3].metric(
    "F1 Score",
    f"{f1_score}%"
)

row2 = st.columns(4)

row2[0].metric(
    "Processing Time",
    f"{processing_time} sec"
)

row2[1].metric(
    "Texts / Second",
    texts_per_second
)

row2[2].metric(
    "Correct",
    correct_predictions
)

row2[3].metric(
    "Incorrect",
    incorrect_predictions
)


st.divider()

st.subheader("Prediction Results")

st.dataframe(
    prediction_df.head(100),
    use_container_width=True,
    height=500,
)


search_prediction = st.text_input(
    "Search Prediction"
)

filtered_prediction = prediction_df.copy()

if search_prediction:

    filtered_prediction = filtered_prediction[
        filtered_prediction.astype(str)
        .apply(
            lambda row:
            row.str.lower().str.contains(
                search_prediction.lower()
            )
        )
        .any(axis=1)
    ]

st.dataframe(
    filtered_prediction,
    use_container_width=True,
)



st.divider()

st.header("📋 Classification Report")

report_df = pd.DataFrame(
    classification_report
).transpose()

st.dataframe(
    report_df,
    use_container_width=True,
)


st.divider()

st.subheader("Performance Summary")

summary = f"""
### Transformer Model Performance

- Accuracy : **{accuracy}%**

- Precision : **{precision}%**

- Recall : **{recall}%**

- F1 Score : **{f1_score}%**

- Total Samples : **{results['total_samples']}**

- Correct Predictions : **{correct_predictions}**

- Incorrect Predictions : **{incorrect_predictions}**

- Processing Time : **{processing_time} seconds**

- Throughput : **{texts_per_second} texts/sec**
"""

st.markdown(summary)



st.divider()

st.header("📥 Export Evaluation Results")

download_col1, download_col2 = st.columns(2)

with download_col1:

    st.download_button(
        "⬇ Download Prediction CSV",
        prediction_df.to_csv(index=False).encode("utf-8"),
        file_name="evaluation_predictions.csv",
        mime="text/csv",
        use_container_width=True,
    )

with download_col2:

    st.download_button(
        "⬇ Download Classification Report",
        report_df.to_csv().encode("utf-8"),
        file_name="classification_report.csv",
        mime="text/csv",
        use_container_width=True,
    )

st.divider()



import plotly.express as px
import plotly.graph_objects as go
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt



st.header("📊 Confusion Matrix")

prediction_subset = prediction_df.copy()

top_languages = (
    prediction_subset["Actual"]
    .value_counts()
    .head(20)
    .index
)

filtered = prediction_subset[
    prediction_subset["Actual"].isin(top_languages)
]

cm = confusion_matrix(
    filtered["Actual"],
    filtered["Predicted"],
    labels=top_languages,
)

fig = px.imshow(
    cm,
    x=top_languages,
    y=top_languages,
    aspect="auto",
    text_auto=True,
    color_continuous_scale="Blues",
)

fig.update_layout(
    height=700,
    xaxis_title="Predicted",
    yaxis_title="Actual",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)


st.divider()

st.header("✅ Prediction Quality")

quality_df = pd.DataFrame(
    {
        "Category": [
            "Correct",
            "Incorrect",
        ],
        "Count": [
            correct_predictions,
            incorrect_predictions,
        ],
    }
)

fig = px.pie(
    quality_df,
    names="Category",
    values="Count",
    hole=0.45,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)



st.divider()

st.header("📈 Confidence Distribution")

fig = px.histogram(
    prediction_df,
    x="Confidence",
    nbins=30,
)

fig.update_layout(
    height=450,
)

st.plotly_chart(
    fig,
    use_container_width=True,
)



st.divider()

st.header("🌍 Per-Language Accuracy")

language_accuracy = (
    prediction_df.assign(
        Correct=prediction_df["Actual"]
        == prediction_df["Predicted"]
    )
    .groupby("Actual")["Correct"]
    .mean()
    .reset_index()
)

language_accuracy["Accuracy"] = (
    language_accuracy["Correct"] * 100
)

language_accuracy = language_accuracy.sort_values(
    "Accuracy",
    ascending=False,
)

st.dataframe(
    language_accuracy,
    use_container_width=True,
)

fig = px.bar(
    language_accuracy.head(20),
    x="Actual",
    y="Accuracy",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)



st.divider()

st.header("⚠ Most Misclassified Languages")

misclassified = prediction_df[
    prediction_df["Actual"]
    != prediction_df["Predicted"]
]

mis_summary = (
    misclassified.groupby("Actual")
    .size()
    .reset_index(name="Errors")
    .sort_values(
        "Errors",
        ascending=False,
    )
)

st.dataframe(
    mis_summary,
    use_container_width=True,
)

if not mis_summary.empty:

    fig = px.bar(
        mis_summary.head(20),
        x="Actual",
        y="Errors",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


st.divider()

st.header("❌ Misclassified Samples")

st.dataframe(
    misclassified,
    use_container_width=True,
    height=500,
)


st.divider()

st.header("📝 Final Report")

report = f"""
## Transformer Language Detection Evaluation

Total Samples : {results['total_samples']}

Accuracy : {accuracy} %

Precision : {precision} %

Recall : {recall} %

F1 Score : {f1_score} %

Correct Predictions : {correct_predictions}

Incorrect Predictions : {incorrect_predictions}

Processing Time : {processing_time} sec

Texts / Second : {texts_per_second}
"""

st.markdown(report)



st.download_button(
    label="⬇ Download Evaluation Report",
    data=report,
    file_name="evaluation_report.txt",
    mime="text/plain",
)


st.divider()

st.markdown(
    """
<div style="text-align:center">

### 🌍 Language Detection System

Model Evaluation completed successfully.

Built with ❤️ using

**Transformers • PyTorch • Streamlit • Plotly**

</div>
""",
    unsafe_allow_html=True,
)