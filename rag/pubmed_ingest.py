from Bio import Entrez
import os
import time

Entrez.email = "myresearchworkpaper@gmail.com"

topics = {
    "cardiology": "chest pain heart disease diagnosis angina myocardial infarction symptoms",
    "neurology": "headache migraine neurological diagnosis stroke symptoms epilepsy",
    "pulmonology": "shortness of breath cough lung disease asthma pneumonia symptoms"
}

os.makedirs("data", exist_ok=True)


def fetch_pubmed(topic, query, max_results=10):

    folder = f"data/{topic}"
    os.makedirs(folder, exist_ok=True)

    print(f"\nFetching {topic} papers...")

    search = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=max_results
    )

    record = Entrez.read(search)
    ids = record["IdList"]

    # Determine how many papers already exist
    existing_files = [f for f in os.listdir(folder) if f.endswith(".txt")]
    existing_count = len(existing_files)

    print(f"Existing papers: {existing_count}")
    print(f"New papers found: {len(ids)}")

    for i, paper_id in enumerate(ids):

        index = existing_count + i
        filepath = f"{folder}/paper_{index}.txt"

        # Skip if file already exists
        if os.path.exists(filepath):
            continue

        try:
            fetch = Entrez.efetch(
                db="pubmed",
                id=paper_id,
                rettype="abstract",
                retmode="text"
            )

            abstract = fetch.read()

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(abstract)

            print(f"Saved {filepath}")

            # PubMed polite delay
            time.sleep(0.3)

        except Exception as e:
            print(f"Error fetching paper {paper_id}: {e}")

    print(f"{topic} ingestion complete.")


for topic, query in topics.items():
    fetch_pubmed(topic, query)