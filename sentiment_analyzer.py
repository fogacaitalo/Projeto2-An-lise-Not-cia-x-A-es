from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd


def analyze_sentiment(news_list):

    print("Analisando sentimento ...")

    analyzer = SentimentIntensityAnalyzer()
    results = []

    for news in news_list:
        text_to_analyze = f"{news['title']}. {news['summary']}"
        vs = analyzer.polarity_scores(text_to_analyze)

        news['sentiment_compound'] = vs['compound']
        news['sentiment_pos'] = vs['pos']
        news['sentiment_neu'] = vs['neu']
        news['sentiment_neg'] = vs['neg']

        # Classificação baseada no score 'compound'
        if vs['compound'] >= 0.05:
            news['sentiment_label'] = 'Positivo'
        elif vs['compound'] <= -0.05:
            news['sentiment_label'] = 'Negativo'
        else:
            news['sentiment_label'] = 'Neutro'

        results.append(news)

    print("Análise de sentimento concluída.")
    return pd.DataFrame(results)
