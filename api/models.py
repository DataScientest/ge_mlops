from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentiment_analyzer = SentimentIntensityAnalyzer()


def model(sentence: str):
    return sentiment_analyzer.polarity_scores(sentence)["compound"]
