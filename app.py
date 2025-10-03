import streamlit as st
import os
import groq
import time
import datetime
from dotenv import load_dotenv
from datetime import datetime
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Load the environment variables
load_dotenv()

# LangSmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = "Simple Q&A ChatBot With GROQ"

# Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the queries."),
        ('user',"Question:{question}")
    ]
)

def get_response(question, api_key, engine, temperatue, max_tokens):
    groq.api_key = api_key

    llm = ChatGroq(model=engine)
    output_parser = StrOutputParser()
    
    chain = prompt | llm | output_parser

    answer = chain.invoke({'question':question})

    return answer

# Title of the Website
st.title = "Q&A ChatBot with GROQ"

# Sidebar for settings
st.sidebar.title('Settings')
api_key=st.sidebar.text_input("Enter your GROQ AI API Key:",type="password")

# Main interface for the user input
st.write(datetime.now())
st.write("Go ahead and ask your question!")
user_input= st.text_input("You:")

# Model 
model1, model2, model3 = st.columns(3)

# Select the GROQ AI Model
with model1:
    engine1 = st.selectbox("Select GROQ AI Model",['gemma2-9b-it','llama-3.1-8b-instant','openai/gpt-oss-20b'], key="engine1")

with model2:
    engine2= st.selectbox("Select GROQ AI Model",['gemma2-9b-it','llama-3.1-8b-instant','openai/gpt-oss-20b'], key="engine2")

with model3:
    engine3= st.selectbox("Select GROQ AI Model",['gemma2-9b-it','llama-3.1-8b-instant','openai/gpt-oss-20b'], key="engine3")

# Adjust the response parameter
temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens",min_value=50, max_value=300, value=150)

# Response
response1,response2,response3 = st.columns(3)
if user_input and api_key:
    with response1:
        if engine1:
            start_time = time.time()
            response1= get_response(user_input, api_key, engine1, temperature, max_tokens)
            end_time = time.time()
            # st.code(response1, language=None, line_numbers=False)  # height not supported in st.code()
            st.text_area("Response from Model 1", value=response1, height=200)
            runtime = end_time - start_time
            tokens = len(response1.split())
            st.write(f"Model response time: {runtime:.2f} seconds")
            st.write(f"Tokens: {tokens}")

            
    with response2:
        if engine2:
            start_time = time.time()
            response2 = get_response(user_input, api_key, engine2, temperature, max_tokens)
            end_time = time.time()
            # st.code(response2, language=None, line_numbers=False)
            st.text_area("Response from Model 2", value=response2, height=200)
            runtime = end_time -start_time
            tokens = len(response2.split())
            st.write(f"Model response time: {runtime:.2f} seconds")
            st.write(f"Tokens: {tokens}")

    with response3:
        if engine3:
            start_time = time.time()
            response3 = get_response(user_input, api_key, engine3, temperature, max_tokens)
            end_time = time.time()
            # st.code(response3, language=None, line_numbers=False)
            st.text_area("Response from Model 3", value=response3, height=200)
            runtime = end_time -start_time
            tokens = len(response2.split())
            st.write(f"Model response time: {runtime:.2f} seconds")
            st.write(f"Tokens: {tokens}")

elif user_input:
    st.warning("Please enter the GROQ API key in the sidebar.")

else:
    st.write("Please provide the user input.")