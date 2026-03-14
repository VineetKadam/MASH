import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

docs = []

# Load documents
for file in os.listdir("data"):
    loader = TextLoader(f"data/{file}", encoding="utf-8")
    docs.extend(loader.load())

print(f"Loaded {len(docs)} documents")

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

print(f"Created {len(chunks)} chunks")

# Load embedding model
embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Create vector DB
db = Chroma.from_documents(
    chunks,
    embedding,
    persist_directory="vector_db"
)

db.persist()

print("Vector database created successfully")