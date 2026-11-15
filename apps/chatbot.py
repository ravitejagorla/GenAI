from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
st.title("Ask Me...")
st.markdown("you know what to do")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])
query = st.chat_input("ask : ")
if query:
    st.session_state.messages.append({'role': "user", "content" : query})
    st.chat_message('user').markdown(query)
    res = llm.invoke(st.session_state.messages).content[0]['text']
    st.session_state.messages.append({'role' : "ai", "content" : res})
    st.chat_message('ai').markdown(res)
