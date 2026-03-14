from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load the same embedding model
embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Connect to existing vector DB
db = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding
)

def retrieve_medical_knowledge(query, k=5):
    
    docs = db.similarity_search(query, k=k)
    
    results = []
    
    for doc in docs:
        results.append(doc.page_content)
        
    return "\n\n".join(results)