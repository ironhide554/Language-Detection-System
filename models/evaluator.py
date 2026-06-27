from __future__ import annotations

import time
from typing import Callable, Dict

import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)

from models.detector import LanguageDetector


class ModelEvaluator:
    """
    Evaluate the Language Detection model on labelled datasets.
    """

    def __init__(self):

        self.detector = LanguageDetector()


    def predict(
        self,
        dataframe: pd.DataFrame,
        text_column: str,
        label_column: str,
        progress_callback: Callable | None = None,
    ) -> pd.DataFrame:

        predictions = []

        total = len(dataframe)

        for index, row in dataframe.iterrows():

            text = str(row[text_column])

            true_label = str(row[label_column])

            try:

                result = self.detector.detect(text)

                predictions.append(
                    {
                        "Text": text,
                        "Actual": true_label,
                        "Predicted": result["code"],
                        "Language": result["language"],
                        "Confidence": result["confidence"],
                    }
                )

            except Exception:

                predictions.append(
                    {
                        "Text": text,
                        "Actual": true_label,
                        "Predicted": "unknown",
                        "Language": "Unknown",
                        "Confidence": 0.0,
                    }
                )

            if progress_callback:

                progress_callback((index + 1) / total)

        return pd.DataFrame(predictions)

    def evaluate(
        self,
        dataframe: pd.DataFrame,
        text_column: str,
        label_column: str,
        progress_callback: Callable | None = None,
    ) -> Dict:

        start = time.perf_counter()

        prediction_df = self.predict(
            dataframe,
            text_column,
            label_column,
            progress_callback,
        )

        elapsed = round(
            time.perf_counter() - start,
            3,
        )

        y_true = prediction_df["Actual"]

        y_pred = prediction_df["Predicted"]

        accuracy = accuracy_score(
            y_true,
            y_pred,
        )

        precision = precision_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0,
        )

        recall = recall_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0,
        )

        f1 = f1_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0,
        )

        report = classification_report(
            y_true,
            y_pred,
            output_dict=True,
            zero_division=0,
        )

        matrix = confusion_matrix(
            y_true,
            y_pred,
        )

        texts_per_second = (
            round(len(prediction_df) / elapsed, 2)
            if elapsed > 0
            else len(prediction_df)
        )

        return {

            "accuracy": round(accuracy * 100, 2),

            "precision": round(precision * 100, 2),

            "recall": round(recall * 100, 2),

            "f1_score": round(f1 * 100, 2),

            "classification_report": report,

            "confusion_matrix": matrix,

            "predictions": prediction_df,

            "processing_time": elapsed,

            "texts_per_second": texts_per_second,

            "total_samples": len(prediction_df),

            "correct_predictions": (
                prediction_df["Actual"]
                == prediction_df["Predicted"]
            ).sum(),

            "incorrect_predictions": (
                prediction_df["Actual"]
                != prediction_df["Predicted"]
            ).sum(),
        }


    def accuracy(
        self,
        dataframe,
        text_column,
        label_column,
    ):

        return self.evaluate(
            dataframe,
            text_column,
            label_column,
        )["accuracy"]

    def precision(
        self,
        dataframe,
        text_column,
        label_column,
    ):

        return self.evaluate(
            dataframe,
            text_column,
            label_column,
        )["precision"]

    def recall(
        self,
        dataframe,
        text_column,
        label_column,
    ):

        return self.evaluate(
            dataframe,
            text_column,
            label_column,
        )["recall"]

    def f1(
        self,
        dataframe,
        text_column,
        label_column,
    ):

        return self.evaluate(
            dataframe,
            text_column,
            label_column,
        )["f1_score"]

    def report(
        self,
        dataframe,
        text_column,
        label_column,
    ):

        return self.evaluate(
            dataframe,
            text_column,
            label_column,
        )["classification_report"]

    def confusion(
        self,
        dataframe,
        text_column,
        label_column,
    ):

        return self.evaluate(
            dataframe,
            text_column,
            label_column,
        )["confusion_matrix"]