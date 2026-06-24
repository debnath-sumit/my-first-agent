import feedparser

CNN_BUSINESS_RSS = "http://rss.cnn.com/rss/edition_business.rss"

def get_business_news(limit=5):
    feed = feedparser.parse(CNN_BUSINESS_RSS)

    news = []

    for entry in feed.entries[:limit]:
        news.append(
            {
                "title": entry.title,
                "link": entry.link
            }
        )

    return news