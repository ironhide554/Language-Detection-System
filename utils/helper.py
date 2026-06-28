import io
import pandas as pd


def dataframe_to_csv(df):
    return df.to_csv(index=False).encode("utf-8")


def dataframe_to_excel(df):
    buffer = io.BytesIO()

    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

    return buffer.getvalue()