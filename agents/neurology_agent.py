from rag.domain_retriever import retrieve_domain_knowledge

def neurology_agent(symptoms):

    context = retrieve_domain_knowledge(symptoms, "neurology")

    return f"""
Neurology Knowledge
--------------------
{context}
"""