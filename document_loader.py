from pathlib import Path
from pypdf import PdfReader
from langchain_core.documents import Document
from config import DOCS_DIR

def load_documents():
    docs = []
    for path in Path(DOCS_DIR).rglob("*"):
        if path.suffix.lower() in {".md", ".txt"}:
            docs.append(Document(
                page_content=path.read_text(encoding="utf-8", errors="ignore"),
                metadata={"source": str(path)}
            ))
        elif path.suffix.lower() == ".pdf":
            text = "\n".join(page.extract_text() or "" for page in PdfReader(str(path)).pages)
            docs.append(Document(page_content=text, metadata={"source": str(path)}))
    return docs
