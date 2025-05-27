import feedparser
from datetime import datetime
import time


def fetch_news(rss_url):

    print(f"Buscando notícias de: {rss_url}")
    feed = feedparser.parse(rss_url)
    news_list = []

    for entry in feed.entries:

        published_str = ""
        try:
            if 'published_parsed' in entry and entry.published_parsed:
                published_str = time.strftime(
                    '%Y-%m-%d %H:%M:%S', entry.published_parsed)
            elif 'published' in entry:
                published_str = entry.published
        except Exception:
            published_str = entry.published if 'published' in entry else ""  # Fallback

        news_list.append({
            'title': entry.title,
            'summary': entry.summary if 'summary' in entry else '',
            'link': entry.link,
            'published': published_str,
            'fetch_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    print(f"Encontradas {len(news_list)} notícias.")
    return news_list
