import streamlit as st
from google import genai

st.title("Jaiswal & Co. AI")

# Secret key connection
try:
    API_KEY = st.secrets["MY_API_KEY"]
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    st.error(f"Connection Error: {e}")
    st.stop()

user_input = st.text_input("Ask me anything:")

if st.button("Submit"):
    if user_input:
        with st.spinner("AI is thinking..."):
            try:
                # Sabse stable model use kar rahe hain
                response = client.models.generate_content(
                    model='gemini-1.5-flash', 
                    contents=user_input
                )
                st.success("Done!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Google API Error: {e}")
                st.info("Tip: Try generating a NEW API key in Google AI Studio.")
