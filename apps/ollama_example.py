from langchain_ollama import ChatOllama
llm = ChatOllama(model="gemma3:1b")
res = llm.invoke("hello, i am ravi?")
print(res.content)