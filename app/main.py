
from typing import List

from fastapi import FastAPI
from app.models.schema import QueryRequest, FAQ
from app.routes.rag import get_answer 
from app.routes.knowledge import add_FAQ, add_FAQs

app=FastAPI()

@app.get("/")
def home():
    return {
        "message": "ServiceDesk Pro AI Service is running"
    }

# rag --> "get_answer fuction " route
@app.post("/rag/query")
def query_rag(query: QueryRequest):
    response = get_answer(query.query)
    return response


# dynamic route to add knowledge to the vector store
@app.post("/knowledge/faq")
def add_faq(faq: FAQ):
    return add_FAQ(faq)


# Add bulk knowledge to the vector store
@app.post("/knowledge/faqs")
def add_faqs(faqs: List[FAQ]):
    return add_FAQs(faqs)
















#TODO:
'''
1. Add error handling for the RAG query endpoint to manage exceptions and provide meaningful error messages.
2. replace llm with cloud based llm api
3. change local chrome with cloud based vector db
4. create the architecture and redesign the code to make it more modular and scalable

'''