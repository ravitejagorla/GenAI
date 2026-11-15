from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
llm = ChatGroq(model = "openai/gpt-oss-20b", streaming=True)
res = llm.stream("what is women?")
for chunk in res:
    print(chunk.content, end='')
print()