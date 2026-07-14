from pathlib import Path
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from document_loader import load_documents
from config import DB_DIR, EMBED_MODEL, CHUNK_SIZE, CHUNK_OVERLAP

def get_vectorstore():
    embeddings = OllamaEmbeddings(model=EMBED_MODEL)
    if Path(DB_DIR).exists():
        print(f"Reusing existing data {DB_DIR} for embeddings...")
        return Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

    docs = load_documents()
    print(f"Loaded {len(docs)} documents. Splitting...")

    chunks = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    ).split_documents(docs)

    vs = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR,
    )
    print(f"Vectorstore built with {len(chunks)} chunks.")
    return vs
