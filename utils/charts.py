import plotly.express as px


def language_distribution(df):

    counts = (
        df["Language Code"]
        .value_counts()
        .reset_index()
    )

    counts.columns = ["Language", "Count"]

    fig = px.bar(
        counts,
        x="Language",
        y="Count",
        title="Detected Languages"
    )

    return fig