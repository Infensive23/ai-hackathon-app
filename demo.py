import streamlit as st
from google import genai

# 1. UI Setup: Design the page header
st.set_page_config(page_title="My AI App", page_icon="💡")
st.title("💡 Jaiswal & Co. AI Assistant")
st.write("Welcome to your custom AI. Type a question below!")

# 2. Authentication
API_KEY = "AIzaSyDeQOektG1rbHGtrrrowEoiaO80udzj1I0" 

# 3. UI Input: Create a text box for the user
user_question = st.text_input("Your Question:")

# 4. UI Action: Create a clickable button
if st.button("Generate Answer"):
    
    # Check if the user actually typed something
    if user_question:
        
        # Show a loading spinner while the AI thinks
        with st.spinner("Thinking..."):
            client = genai.Client(api_key=API_KEY)
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_question
            )
            
            # Print the final answer on the web page beautifully
            st.markdown(response.text)
    
    else:
        st.warning("Please type a question first!")