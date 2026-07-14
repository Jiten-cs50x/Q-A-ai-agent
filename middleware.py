from typing import Any
from langchain.agents.middleware import AgentMiddleware, AgentState
from langchain_core.documents import Document
from langchain_core.messages import SystemMessage
from config import RETRIEVAL_K, SYSTEM_PROMPT

class State(AgentState):
    context: list[Document]

class RetrieveDocumentsMiddleware(AgentMiddleware[State]):
    state_schema = State

    def __init__(self, vector_store):
        self.vector_store = vector_store

    def before_model(self, state: State) -> dict[str, Any] | None:
        msg = state["messages"][-1]
        query = str(msg.content)
        docs = self.vector_store.similarity_search(query, k=RETRIEVAL_K)

        context = "\n\n".join(
            f"Source: {doc.metadata.get('source', 'unknown')}\n{doc.page_content}"
            for doc in docs
        )

        system_message = SystemMessage(
            content=f"{SYSTEM_PROMPT}\n\nContext:\n{context}"
        )

        return {"messages": [system_message], "context": docs}
