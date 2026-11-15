from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
@tool
def add_numbers(a : int, b : int) -> int:
    '''
    It will return sum of two numbers
    Args
        a is number one
        b is number two
    '''
    return a + b
@tool
def multiply_numbers(a : int, b : int) -> int:
    '''
    It will return product of two numbers
    Args
        a is number one
        b is number two
    '''
    return a * b

llm = ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite')
agent = create_agent(
    model=llm, 
    tools=[add_numbers, multiply_numbers],
    system_prompt = """
        You are a mathematics teacher.
        You MUST use the available tools for all calculations.
        Never calculate mathematical operations yourself.
    """
)
response = agent.invoke({'messages' : [{'role' : "user", 'content' : "what is 2 + 4 * 5?"}]})
answer = response['messages'][-1].content[0]['text']
print(answer)