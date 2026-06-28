import io
import pandas as pd

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


def dataframe_to_csv(df):
    return df.to_csv(index=False).encode("utf-8")


def dataframe_to_excel(df):
    buffer = io.BytesIO()

    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

    return buffer.getvalue()