from datasets import load_dataset
import pandas as pd


def load_language_identification(split="test"):

    dataset = load_dataset(
        "papluca/language-identification",
        split=split,
    )

    df = dataset.to_pandas()

    df = df.rename(
        columns={
            "text": "Text",
            "labels": "Language Code",
        }
    )

    return df