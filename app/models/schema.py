from pydantic import BaseModel  

# paydantic model for the request body

class QueryRequest(BaseModel):
    query: str  

# pydantic model for FAQ items 
class FAQ(BaseModel): 
    id: str 
    category: str 
    question: str 
    answer: str

