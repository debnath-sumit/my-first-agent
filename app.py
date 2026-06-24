import streamlit as st
from main import run_morning_brief

st.title("My First Agent")

if st.button("Generate Morning Brief"):
    with st.spinner("Generating..."):
        summary = run_morning_brief()

    st.markdown(summary)