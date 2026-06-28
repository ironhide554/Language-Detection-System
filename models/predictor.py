import pandas as pd
from tqdm import tqdm


class BatchPredictor:

    def __init__(self, detector):
        self.detector = detector

    def predict_dataframe(self, dataframe, text_column, progress_callback=None):
        """
        Run language detection on every row in the dataframe.
        """

        results = []

        total = len(dataframe)

        for index, text in enumerate(
            tqdm(dataframe[text_column], total=total)
        ):

            if pd.isna(text):
                text = ""

            prediction = self.detector.detect(str(text))

            results.append(
                {
                    "Text": text,
                    "Language Code": prediction["language"],
                    "Confidence (%)": prediction["confidence"],
                }
            )

            if progress_callback:
                progress_callback((index + 1) / total)

        return pd.DataFrame(results)