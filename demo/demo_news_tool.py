from src.tools.news_tool import get_business_news

news = get_business_news()

for item in news:
    print(item["title"])