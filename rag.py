from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.tools.retriever import create_retriever_tool

embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
PERSIST_DIR = "chroma_db"

def match_property_id(user_text):
    vectordb = Chroma(
        collection_name="property_metadata",
        embedding_function=embedding,
        persist_directory=PERSIST_DIR
    )
    retriever = vectordb.as_retriever(search_kwargs={"k": 1})
    results = retriever.get_relevant_documents(user_text)
    if results:
        return results[0].metadata.get("property_id")
    return None

def get_rag_tool(property_id):
    vectordb = Chroma(
        collection_name=f"property_{property_id}",
        embedding_function=embedding,
        persist_directory=PERSIST_DIR
    )
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    return create_retriever_tool(
        retriever,
        name="property_docs",
        description="Useful for answering questions from the house manual or local guides"
    )
