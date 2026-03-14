from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

def retrieve_domain_knowledge(query, domain, k=5):

    db = Chroma(
        persist_directory=f"vector_db/{domain}",
        embedding_function=embedding
    )

    docs = db.max_marginal_relevance_search(query, k=k)

    return "\n\n".join([doc.page_content for doc in docs])