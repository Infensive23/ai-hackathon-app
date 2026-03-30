import streamlit as st
import google.generativeai as genai

st.title("Jaiswal & Co. AI")

# Check if the secret key is there
if "MY_API_KEY" not in st.secrets:
    st.error("Please add 'MY_API_KEY' to Streamlit Secrets!")
    st.stop()

# Configure the AI
genai.configure(api_key=st.secrets["MY_API_KEY"])

user_input = st.text_input("Ask me anything:")

if st.button("Submit"):
    if user_input:
        with st.spinner("Wait, I am thinking..."):
            try:
                # Using the most stable model
                model = genai.GenerativeModel('models/gemini-1.5-flash')
                response = model.generate_content(user_input)
                st.success("Success!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
