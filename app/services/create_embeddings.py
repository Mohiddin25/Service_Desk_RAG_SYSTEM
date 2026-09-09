import json
from pathlib import Path

from langchain_core.documents import Document
from app.services.embeddings import embedding_model



# Project root directory 
BASE_DIR = Path(__file__).resolve().parent.parent

# Folder where ChromaDB will store vectors 
CHROMA_PATH = BASE_DIR / "chroma_db"


FAQ_PATH = "C:\\Users\\zaffe\\OneDrive\\Desktop\\ServiceDesk\\Service_Desk\\Backend\\ai_services\\data\\faqs.json"
# Load FAQ data
with open(FAQ_PATH, "r", encoding="utf-8") as file:
    faqs = json.load(file)

documents = []


for faq in faqs:

    content = f""" Question: {faq["question"]} Answer: {faq["answer"]}"""

    document = Document(
        page_content=content,
        metadata={
            "id": faq["id"],
            "category": faq["category"]
        }
    )

    documents.append(document)


print(f"Total documents: {len(documents)}")



# Test embedding for first FAQ
"""
vector = embedding_model.embed_query(
    documents[0].page_content
)


print("Embedding created successfully")

print(f"Vector dimensions: {len(vector)}")

print(f"First 10 values: {vector[:10]}")
"""


# Create Chroma vector database
vector_store = Chroma.from_documents( 
    documents=documents, 
    embedding=embedding_model, 
    persist_directory=str(CHROMA_PATH), 
    collection_name="servicedesk_faqs" )