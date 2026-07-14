from vectorstore import get_vectorstore
from agent import build_agent

def main():
    vector_store = get_vectorstore()
    agent = build_agent(vector_store)

    print("\nReady! Ask questions about your documents.\n")

    while True:
        question = input("You: ").strip()
        if not question or question.lower() == "exit":
            break

        result = agent.invoke({
            "messages": [{"role": "user", "content": question}],
            "context": [],
        })

        print(f"\nAnswer: {result['messages'][-1].content}\n")
        print("Sources:")
        seen = set()
        for doc in result.get("context", []):
            source = doc.metadata.get("source", "unknown")
            if source not in seen:
                print("-", source)
                seen.add(source)
        print()

if __name__ == "__main__":
    main()
