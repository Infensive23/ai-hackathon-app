import streamlit as st
import google.generativeai as genai

st.title("Jaiswal & Co. AI")

if "MY_API_KEY" not in st.secrets:
    st.error("Secrets mein 'MY_API_KEY' nahi mila!")
    st.stop()

genai.configure(api_key=st.secrets["MY_API_KEY"])

user_input = st.text_input("Ask Jaiswal & Co. AI:")

if st.button("Submit"):
    if user_input:
        with st.spinner("Thinking..."):
            try:
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(user_input)
                st.success("Mil gaya answer!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Google API Error: {e}")
                st.info("Tip: Google AI Studio mein ja kar ek NAYI key generate karke Secrets mein update karein.")
