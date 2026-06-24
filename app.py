import streamlit as st
from agent import run_agent

st.set_page_config(
    page_title="My First Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 My First Agent")

with st.sidebar:
    city = st.text_input("City", "Dallas")

user_request = st.text_area(
    "Ask your agent",
    f"Give me my morning brief. Include business news, stocks, Gmail emails, and weather for {city}."
)

if st.button("Run Agent"):
    with st.spinner("Agent is thinking and using tools..."):
        response = run_agent(user_request)

    st.subheader("Agent Response")
    st.markdown(response)