import streamlit as st
from google import genai

# 1. Page Setup
st.title("Jaiswal & Co. AI")

# 2. Get the Key from Secrets
# Check: This name MUST match the one in Streamlit Settings
try:
    API_KEY = st.secrets["MY_API_KEY"]
except:
    st.error("Secret Key 'MY_API_KEY' not found in Streamlit Settings!")
    st.stop()

# 3. Input and Button
user_input = st.text_input("Ask me anything:")

if st.button("Submit"):
    if user_input:
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=user_input
        )
        st.write(response.text)
