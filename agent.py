from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from middleware import RetrieveDocumentsMiddleware, State
from config import CHAT_MODEL

def build_agent(vector_store):
    model = ChatOllama(model=CHAT_MODEL, temperature=0)
    return create_agent(
        model=model,
        tools=[],
        middleware=[RetrieveDocumentsMiddleware(vector_store)],
        state_schema=State,
    )
