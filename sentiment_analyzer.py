from textblob import TextBlob


def analyze_sentiment(text: str):
    """
    Analyzes sentiment from chat text.
    Returns polarity (-1 to 1) and classification.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        label = "Positive"
    elif polarity < -0.1:
        label = "Negative"
    else:
        label = "Neutral"

    return polarity, label


if __name__ == "__main__":
    sample_text = "This lecture is really interesting and helpful!"
    polarity, label = analyze_sentiment(sample_text)
    print("Polarity:", polarity)
    print("Sentiment:", label)
