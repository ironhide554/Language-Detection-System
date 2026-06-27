import pandas as pd
import io


def create_prediction_dataframe(predictions):

    rows = []

    for pred in predictions:
        rows.append(
            {
                "Language Code": pred["label"],
                "Confidence (%)": round(pred["score"] * 100, 2)
            }
        )

    return pd.DataFrame(rows)


