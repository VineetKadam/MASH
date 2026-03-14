from rag.domain_retriever import retrieve_domain_knowledge

def pulmonology_agent(symptoms):

    context = retrieve_domain_knowledge(symptoms, "pulmonology")

    return f"""
Pulmonology Knowledge
----------------------
{context}
"""