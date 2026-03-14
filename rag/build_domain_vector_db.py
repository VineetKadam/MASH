import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=50
)

domains = ["cardiology", "neurology", "pulmonology"]

for domain in domains:

    print(f"Processing {domain}")

    docs = []

    domain_path = f"data/{domain}"

    for file in os.listdir(domain_path):

        if file.endswith(".txt"):

            loader = TextLoader(f"{domain_path}/{file}", encoding="utf-8")
            docs.extend(loader.load())

    chunks = splitter.split_documents(docs)

    db = Chroma.from_documents(
        chunks,
        embedding,
        persist_directory=f"vector_db/{domain}"
    )

    db.persist()

    print(f"{domain} vector DB created")