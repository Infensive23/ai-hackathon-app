import streamlit as st
from google import genai

st.title("Jaiswal & Co. AI")

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
                # Using the absolute latest stable model name
                response = client.models.generate_content(
                    model='gemini-1.5-flash', 
                    contents=user_input
                )
                st.success("Done!")
                st.write(response.text)
            except Exception as e:
                # Agar flash nahi chala, toh ye pro try karega
                try:
                    response = client.models.generate_content(
                        model='gemini-1.5-pro', 
                        contents=user_input
                    )
                    st.write(response.text)
                except:
                    st.error(f"Google API Error: {e}")
