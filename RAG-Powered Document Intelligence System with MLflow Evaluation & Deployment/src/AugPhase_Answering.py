#%%
# ==========================================================
# Loading
# ==========================================================
# Libraries
from anthropic import Anthropic
import os
from dotenv import load_dotenv

# Parameters or environment variables
load_dotenv()
print("API key loaded:", bool(os.getenv("API_KEY")))
import __parameters as _params
LLM_MODEL_NAME = getattr(_params, "LLM_MODEL_NAME")
LLM_MAX_TOKENS = getattr(_params, "LLM_MAX_TOKENS")

# Scripts
from RetPhase_Retrieving import RAG_RETRIEVER
from AugPhase_SystemPrompt import SYSTEM_PROMPT


# ==========================================================
# Step 8: RAG-Augmented LLM Call
# ==========================================================
def ask_with_context(client: Anthropic, query: str, conversation_history: list) -> str:
    # Retrieve relevant chunks
    retrieved_docs = RAG_RETRIEVER.retrieve(query)

    # Format into a readable context block
    context = RAG_RETRIEVER.format_context(retrieved_docs)

    # Augment the user message with context
    augmented_user_message = (
        f"Context from documents:\n\n{context}\n\n"
        f"---\n\n"
        f"Question: {query}"
    )

    # Append augmented message to history
    conversation_history.append({
        "role": "user",
        "content": augmented_user_message
    })

    # Call the LLM
    response = client.messages.create(
        model=LLM_MODEL_NAME,
        max_tokens=LLM_MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=conversation_history
    )

    assistant_reply = response.content[0].text

    # Store the plain assistant reply in history (not the augmented prompt)
    conversation_history.append({
        "role": "assistant",
        "content": assistant_reply
    })

    return assistant_reply


# ==========================================================
# Step 9: Conversation Loop
# ==========================================================
def run_rag_chat():
    client = Anthropic(api_key=os.getenv("API_KEY"))
    conversation_history = []

    print("\n=== RAG Chat Assistant ===")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        query = input("You: ").strip()

        if not query:
            continue
        if query.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        reply = ask_with_context(client, query, conversation_history)
        print(f"\nAssistant: {reply}\n")


# ==========================================================
# Entry Point
# ==========================================================
if __name__ == "__main__":
    run_rag_chat()
