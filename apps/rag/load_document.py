from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, PyPDFLoader
load_dotenv()
txt_loader = TextLoader("data/speech.txt")
data = txt_loader.load()
print(data)
print("==========================================================================")
pdf_loader = PyPDFLoader("data/React New Content.pdf")
data = pdf_loader.load()
print(data)
