import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI Language Translator")

text = st.text_area("Enter text to translate")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Punjabi": "pa",
    "Urdu": "ur"
}

source = st.selectbox("Source Language", languages.keys())
target = st.selectbox("Target Language", languages.keys())

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation Completed!")

        st.text_area(
            "Translated Text",
            translated,
            height=150
        )

st.markdown("""
<style>
.footer {
    position: fixed;
    bottom: 12px;
    right: 20px;
    color: #9ca3af;
    font-size: 13px;
    font-weight: 500;
    font-family: 'Segoe UI', sans-serif;
    opacity: 0.85;
}
</style>

<div class="footer">
    ❤️ Made by Harsh Garg
</div>
""", unsafe_allow_html=True)