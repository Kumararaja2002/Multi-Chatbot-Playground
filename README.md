# 🤖 Multi-Model Q&A Chatbot with GROQ

This project is a Streamlit-based chatbot that allows users to query multiple GROQ AI models simultaneously and compare their responses. It supports models like **Gemma2-9B**, **LLaMA 3.1-8B**, and **GPT-OSS-20B**.

## 🚀 Features

- Query up to 3 GROQ models side-by-side
- Adjustable temperature and token limits
- Displays response time and token usage
- Simple and interactive Streamlit UI

## 🧠 Technologies Used

- Streamlit
- LangChain
- GROQ API
- Python
- dotenv

## 📁 File Structure

- `app.py`: Main Streamlit application
- `.env`: Stores your GROQ API key and LangChain tracking variables

## 🔐 Environment Variables

Create a `.env` file with the following keys:


GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=Simple Q&A ChatBot With GROQ

## 🛠️ How to Run


1. Clone the repository:
```git clone https://github.com/yourusername/groq-multi-model-chatbot.gitcd groq-multi-model-chatbot```

2. Install dependencies:
```pip install -r requirements.txt```

3. Add your .env file with API keys.

4. Run the Streamlit app:
   ```streamlit run app.py```
