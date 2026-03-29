import streamlit as st
from google import genai

# 1. UI Setup
st.set_page_config(page_title="My AI App", page_icon="💡")
st.title("💡 Jaiswal & Co. AI Assistant")
st.write("Welcome to your custom AI. Type a question below!")

# 2. Authentication (Using Streamlit Secrets - Best for Cloud)
# Yahan 'GEMINI_KEY' wahi naam hai jo aapne Streamlit Settings mein dala tha
API_KEY = st.secrets["GEMINI_KEY"]

# 3. UI Input
user_question = st.text_input("Your Question:")

# 4. UI Action
if st.button("Generate Answer"):
    if user_question:
        with st.spinner("Thinking..."):
            # Naya Syntax (google-genai library ke liye)
            client = genai.Client(api_key=API_KEY)
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_question
            )
            st.markdown(response.text)
    else:
        st.warning("Please type a question first!")
