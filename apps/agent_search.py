from dotenv import load_dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
load_dotenv()
search = GoogleSerperAPIWrapper()
llm = ChatGroq(model="openai/gpt-oss-20b")
agent = create_agent(
    model = llm,
    tools = [search.run],
    checkpointer=InMemorySaver(),
    system_prompt = 'you are an agent and you can search on google'
)
while True:
    query = input("user : ")
    if query.lower() in ['bye', 'exit', 'quit']:
        print('ai : Bye')
        break
    response = agent.invoke(
        {'messages' : [{'role' : "user", "content" : query}]},
        {'configurable' : {'thread_id' : '1'}}
    )
    print('ai : ', response['messages'][-1].content)