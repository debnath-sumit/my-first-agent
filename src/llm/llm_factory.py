# llm/llm_factory.py

from langchain_groq import ChatGroq

def get_llm():
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0
    )