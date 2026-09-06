from pinecone_db import index


def search_vectors(query_vector, top_k=3):

    results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )

    return results

