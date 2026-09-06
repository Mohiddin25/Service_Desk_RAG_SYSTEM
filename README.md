## RAG SERVICE 
1. Create ai-service folder
2. Set up Python virtual environment
3. Install FastAPI + LangChain
4. Create FAQ dataset
5. Create embeddings
6. Store them in ChromaDB
7. Build the RAG API
8. Connect Express → FastAPI



User Query
    ↓
Convert Query → Embedding
    ↓
Vector Similarity Search
    ↓
Retrieve Relevant FAQs
    ↓
Send Context + Query to LLM
    ↓
Generate Answer