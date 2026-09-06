
from langchain_huggingface import HuggingFaceEmbeddings
import os


embedding_model = HuggingFaceEmbeddings(
    model_name=os.getenv("EMBEDDING_MODEL")
)

def create_embedding(text: str): 
    return embedding_model.embed_query(text)



