import streamlit as st
from src.agent import run_agent
from src.memory.pinecone_store import save_memory
from src.memory.pinecone_store import get_memory_stats

st.set_page_config(
    page_title="My First Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 My First Agent")

with st.sidebar:
    city = st.text_input("City", "Dallas")

with st.sidebar:
    st.header("Settings")

    if st.button("Check Memory"):
        stats = get_memory_stats()
        st.write(stats)

user_request = st.text_area(
    "Ask your agent",
    f"Give me my morning brief. Include business news, stocks, and weather for {city}."
)

if st.button("Run Agent"):
    with st.spinner("Agent is thinking and using tools..."):
        response = run_agent(user_request)
        save_memory(response)
        st.subheader("Agent Response")
        st.markdown(response)