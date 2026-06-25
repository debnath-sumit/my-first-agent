from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm(model_name):
    if model_name.startswith("llama"):
        return ChatGroq(
            model=model_name,
            temperature=0
        )

    if model_name.startswith("gemini"):
        return ChatGoogleGenerativeAI(
            model=model_name,
            temperature=0
        )

    raise ValueError(f"Unsupported model: {model_name}")