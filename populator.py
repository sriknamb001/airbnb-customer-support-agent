import os
import json
from langchain.schema import Document
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma

embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

PROPERTY_METADATA_DIR = "./data/property_metadata"  # JSON files with property_id, address, name, description
PROPERTY_DOCS_DIR = "./data/properties_docs"        # Text or JSON files with detailed docs per property
PERSIST_DIR = "chroma_db"

def build_property_metadata_vectordb():
    print("Building property metadata vector DB...")
    metadata_list = []
    for filename in os.listdir(PROPERTY_METADATA_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(PROPERTY_METADATA_DIR, filename), "r") as f:
                data = json.load(f)
                metadata_list.append(data)
    documents = []
    for meta in metadata_list:
        text = f"{meta.get('address', '')} {meta.get('name', '')} {meta.get('description', '')}"
        documents.append(Document(page_content=text, metadata={"property_id": meta['property_id']}))
    vectordb = Chroma.from_documents(
        documents,
        embedding,
        collection_name="property_metadata",
        persist_directory=PERSIST_DIR
    )
    vectordb.persist()
    print(f"Indexed {len(documents)} property metadata entries.")

def build_property_docs_vectordbs():
    print("Building per-property docs vector DBs...")
    for filename in os.listdir(PROPERTY_DOCS_DIR):
        if filename.endswith(".json"):
            property_id = filename[:-5]  # remove ".json"
            with open(os.path.join(PROPERTY_DOCS_DIR, filename), "r") as f:
                data = json.load(f)
                # Assume 'docs' field is a list of strings or paragraphs
                docs = data.get("docs", [])
                if not docs:
                    print(f"No docs found for property {property_id}, skipping.")
                    continue
                documents = [Document(page_content=doc, metadata={"property_id": property_id}) for doc in docs]
                vectordb = Chroma.from_documents(
                    documents,
                    embedding,
                    collection_name=f"property_{property_id}",
                    persist_directory=PERSIST_DIR
                )
                vectordb.persist()
                print(f"Indexed {len(documents)} docs for property {property_id}.")

if __name__ == "__main__":
    build_property_metadata_vectordb()
    build_property_docs_vectordbs()
