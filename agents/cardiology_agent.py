from rag.domain_retriever import retrieve_domain_knowledge

def cardiology_agent(symptoms):

    context = retrieve_domain_knowledge(symptoms, "cardiology")

    return f"""
Cardiology Knowledge
--------------------
{context}
"""