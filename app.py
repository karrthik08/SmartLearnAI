import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="SmartLearn AI", layout="centered")
st.title("SmartLearn AI: Flashcard & Quiz Generator")

st.markdown("Enter your academic content below:")

text_input = st.text_area("Paste your notes or study material", height=300)

if text_input:
    with st.spinner("Generating flashcards..."):
        qg = pipeline("text2text-generation", model="valhalla/t5-small-qg-hl")
        input_text = "highlight: " + text_input.strip()
        output = qg(input_text, max_length=64, num_return_sequences=5)
        st.subheader(" Flashcard Questions:")
        for i, res in enumerate(output):
            st.markdown(f"**Q{i+1}:** {res['generated_text']}")
