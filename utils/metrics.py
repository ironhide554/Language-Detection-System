def calculate_statistics(df):

    stats = {}

    stats["Total Samples"] = len(df)

    stats["Average Confidence"] = round(
        df["Confidence (%)"].mean(), 2
    )

    stats["Unique Languages"] = df["Language Code"].nunique()

    return stats