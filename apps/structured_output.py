from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
load_dotenv()
class Response(BaseModel):
    name: str = Field(description="Full name")
    email: str = Field(description="Email")
    age:int = Field(description="Age")
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
prompt = [{'role' : "user", "content" : "My name is Ravi Teja Gorla. I am 26. My mail id is rt.gorla@gmail.com"}]
structured_llm = llm.with_structured_output(Response)
res = structured_llm.invoke(prompt)
print(res, type(res))
print('name: ', res.name)
print('email:', res.email)
print('age:', res.age)
