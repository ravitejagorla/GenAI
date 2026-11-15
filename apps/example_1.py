from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

history = []
while True:
    query = input("user : ")
    if query.lower() in ['bye', 'exit', 'quit']:
        print('Bye')
        break
    history.append({'role' : 'user', 'content' : query})
    res = llm.invoke(history).content[0]['text']
    print("ai : ", res)
    history.append({'role' : 'ai', "content" : res})
