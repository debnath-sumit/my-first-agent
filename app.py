import streamlit as st

from news_tool import get_business_news
from stock_tool import get_stock_prices
from gmail_tool import get_top_emails
from ai_summary import generate_summary

st.set_page_config(
    page_title="My First Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 My First Agent")
st.write("Your AI-powered morning brief")

if st.button("Generate Morning Brief"):

    with st.spinner("Fetching business news..."):
        news = get_business_news()

    with st.spinner("Fetching stock prices..."):
        stocks = get_stock_prices(
            ["AAPL", "MSFT", "GOOGL", "NVDA", "TSLA"]
        )

    with st.spinner("Fetching Gmail emails..."):
        emails = get_top_emails()

    with st.spinner("Generating AI summary..."):
        summary = generate_summary(news, stocks, emails)

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📰 News", "📈 Stocks", "📧 Emails", "🧠 AI Summary"]
    )

    with tab1:
        st.subheader("Top Business News")
        for item in news:
            st.markdown(f"- [{item['title']}]({item['link']})")

    with tab2:
        st.subheader("Stock Prices")
        for ticker, price in stocks.items():
            st.metric(label=ticker, value=f"${price}")

    with tab3:
        st.subheader("Top Gmail Emails")
        for email in emails:
            st.markdown(f"**From:** {email['sender']}")
            st.markdown(f"**Subject:** {email['subject']}")
            st.write(email["snippet"])
            st.divider()

    with tab4:
        st.subheader("AI Morning Summary")
        st.markdown(summary)