from services.embeddings import embedding_model
from pinecone_db import index
from typing import List
from models.schema import FAQ



def add_faq(faq: FAQ):
    # 1. Combine question and answer 
    text = f""" Question: {faq.question} Answer: {faq.answer} """

    # 2. Generate embedding 
    vector = embedding_model.embed_query(text)

    # 3. Store in Pinecone 
    index.upsert( 
        vectors=[ { 
            "id": faq.id, 
            "values": vector, 
            "metadata": { "category": faq.category, "question": faq.question, "answer": faq.answer } } 
            ] )


    return { "message": "FAQ added successfully", "id": faq.id, "dimension": len(vector) }

def add_faqs(faqs: List[FAQ]):
    vectors = []
    for faq in faqs:
        # 1. Combine question and answer 
        text = f""" Question: {faq.question} Answer: {faq.answer} """

        # 2. Generate embedding 
        vector = embedding_model.embed_query(text)

        # 3. Store in Pinecone 
        vectors.append({
            "id": faq.id,
            "values": vector,
            "metadata": { "category": faq.category, "question": faq.question, "answer": faq.answer }
        })

    index.upsert(vectors=vectors)
    return { "message": "FAQs added successfully" }
