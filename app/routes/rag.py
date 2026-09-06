from langchain_ollama import ChatOllama
from pathlib import Path

from langchain_chroma import Chroma
from app.services.embeddings import embedding_model
from app.services.embeddings import create_embedding
from app.services.llms_service import generate_answer
from app.services.vector_service import search_vectors

# # --------------------------------------------------
# # Paths
# # --------------------------------------------------

# BASE_DIR = Path(__file__).resolve().parent.parent

# CHROMA_PATH = BASE_DIR / "chroma_db"


# # --------------------------------------------------
# # Vector Database
# # --------------------------------------------------

# vector_store = Chroma(
#     collection_name="servicedesk_faqs",
#     embedding_function=embedding_model,
#     persist_directory=str(CHROMA_PATH)
# )


# # --------------------------------------------------
# # LLM
# # --------------------------------------------------

# llm=ChatOllama(model="qwen3:1.7b", base_url="http://localhost:11434", temperature=0.3)

# --------------------------------------------------
# RAG Function
# --------------------------------------------------

def get_answer(query: str):
    # 1. Convert user query into embedding 
    query_vector = create_embedding(query)

    # 2. Search Pinecone 
    results = search_vectors( query_vector, top_k=3 )

    # 3. Get matching documents 
    matches = results["matches"]


    # 4. Create context 
    context = "\n\n".join( f""" Question: {match['metadata']['question']} Answer: {match['metadata']['answer']} """ for match in matches )

    # 5. Create prompt
    prompt = f"""
    You are an IT Helpdesk assistant.

    Answer the user's question using ONLY the information
    provided in the FAQ context below.

    If the answer cannot be found in the context,
    say that you do not have enough information.

    FAQ Context:
    ----------------
    {context}
    ----------------

    User Question:
    {query}

    Give a concise and helpful answer.
    """

    # 6. Call cloud LLM 
    answer = generate_answer(prompt)

    # 7. Sources 
    sources = [ 
        { "id": match["id"], "category": match["metadata"]["category"] } for match in matches ] 
    
    return { "answer": answer, "sources": sources }







