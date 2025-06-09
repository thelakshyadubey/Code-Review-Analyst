# Updated import: use langchain_groq instead of langchain_openai
# import os
# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")  # Force set manually
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
from io import StringIO
import streamlit as st
from dotenv import load_dotenv
import time
import base64

# Load environment variables from .env file (e.g., GROQ_API_KEY)
load_dotenv()

st.title("Let's do code review for your python code")
st.header("Please upload your .py file here:")

# Function to download the code review result as a .txt file
def text_downloader(raw_text):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    b64 = base64.b64encode(raw_text.encode()).decode()
    new_filename = f"code_review_analysis_file_{timestr}_.txt"
    st.markdown("#### Download File ✅###")
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'
    st.markdown(href, unsafe_allow_html=True)

# Upload Python code
data = st.file_uploader("Upload python file", type=".py")

if data:
    stringio = StringIO(data.getvalue().decode('utf-8'))
    fetched_data = stringio.read()
    st.write(fetched_data)

    # Use ChatGroq instead of ChatOpenAI
    chat = ChatGroq(model_name="llama3-70b-8192", temperature=0.9)

    systemMessage = SystemMessage(
        content="You are a code review assistant. Provide detailed suggestions to improve the given Python code along by mentioning the existing code line by line with proper indent"
    )

    humanMessage = HumanMessage(content=fetched_data)

    # Recommended `invoke()` usage
    finalResponse = chat.invoke([systemMessage, humanMessage])

    st.markdown(finalResponse.content)
    text_downloader(finalResponse.content)
