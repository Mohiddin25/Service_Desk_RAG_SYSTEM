
# from pathlib import Path
# from langchain_chroma import Chroma
# from services.embeddings import embedding_model


# # Project root
# BASE_DIR = Path(__file__).resolve().parent.parent

# CHROMA_PATH = BASE_DIR / "chroma_db"


# # Load existing ChromaDB
# vector_store = Chroma(
#     collection_name="servicedesk_faqs",
#     embedding_function=embedding_model,
#     persist_directory=str(CHROMA_PATH)
# )


# # User query
# query = "My office Wi-Fi is not working"


# # Semantic search
# results = vector_store.similarity_search(
#     query,
#     k=3
# )


# print("\nUser Query:")
# print(query)

# print("\nRelevant FAQs:\n")

# for i, document in enumerate(results, start=1):

#     print(f"--- Result {i} ---")

#     print("FAQ ID:", document.metadata["id"])
#     print("Category:", document.metadata["category"])

#     print(document.page_content)

#     print()

