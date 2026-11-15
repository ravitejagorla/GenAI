import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_community.utilities import GoogleSerperAPIWrapper
load_dotenv()
search = GoogleSerperAPIWrapper()
llm = ChatGroq(model = "openai/gpt-oss-20b", streaming = True)
if 'memory' not in st.session_state:
    st.session_state.memory = MemorySaver()
agent = create_agent(
    model = llm,
    tools = [search.run],
    checkpointer = st.session_state.memory,
    system_prompt = 'you are an agent and you can search on google'
)
st.title('Q & A chat bot')
if 'messages' not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])
query = st.chat_input('ask :')
if query:
    st.chat_message('user').markdown(query)
    st.session_state.messages.append({'role' : 'user', 'content' : query})
    response = agent.stream(
            {'messages' : [{'role' : "user", "content" : query}]},
            {'configurable' : {'thread_id' : '1'}},
            stream_mode = "messages"
        )
    ai_container = st.chat_message('ai')
    with ai_container:
        space = st.empty()
        message = ""
        for chunk in response:
            message += chunk[0].content
            space.write(message)
        st.session_state.messages.append({'role' : 'ai', 'content' : message})