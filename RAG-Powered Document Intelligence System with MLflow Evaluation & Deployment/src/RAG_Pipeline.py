# %%
# ==========================================================
# RAG Pipeline — orchestrates all stages
# ==========================================================
import os
from dotenv import load_dotenv
from anthropic import Anthropic

import __parameters as _params
from RetPhase_Ingesting import ingest_pdf_docs
from RetPhase_Splitting import split_documents
from RetPhase_EmbeddingClass import EMBEDDER
from RetPhase_VectorStoreClass import VECTOR_STORE
from RetPhase_Retrieving import RAGRetriever
from AugPhase_SystemPrompt import SYSTEM_PROMPT

load_dotenv()


class RAGPipeline:
    def __init__(self):
        self.embedder = EMBEDDER
        self.vector_store = VECTOR_STORE
        self.retriever = RAGRetriever(self.vector_store, self.embedder)
        api_key = os.getenv("ANTHROPIC_API_KEY") or os.getenv("API_KEY")
        self.client = Anthropic(api_key=api_key)
        self.conversation_history = []

    def reindex(self):
        """ 
        1-RetPhase_Ingesting, 
        2-RetPhase_Splitting, 
        3-RetPhase_EmbeddingClass, 4-RetPhase_VectorStoreClass
        5-Clear Store and RetPhase_Vectorizing
        """
        
        print("\n[1/5] Ingesting documents...")
        docs = ingest_pdf_docs(_params.PDF_DIRECTORY)

        print("\n[2/5] Splitting into chunks...")
        chunks = split_documents(docs, _params.CHUNK_SIZE, _params.CHUNK_OVERLAP)

        print("\n[3-4/5] Generating embeddings...")
        texts = [doc.page_content for doc in chunks]
        embeddings = self.embedder.generate_embeddings(texts)

        print("\n[5/5] Clearing store and saving vectors...")
        self.vector_store.clear_collection()
        self.vector_store.add_documents(chunks, embeddings)

        print("\nReindex complete.")





    def query(self, question: str) -> str:
        """
        6-RetPhase_Retrieving
        7-AugPhase_SystemPrompt
        8-AugPhase_Answering
        """
        retrieved_docs = self.retriever.retrieve(
            question, _params.TOP_K, _params.SCORE_THRESHOLD
        )
        context = self.retriever.format_context(retrieved_docs)

        augmented_message = (
            f"Context from documents:\n\n{context}\n\n"
            f"---\n\n"
            f"Question: {question}"
        )

        self.conversation_history.append({"role": "user", "content": augmented_message})

        response = self.client.messages.create(
            model=_params.LLM_MODEL_NAME,
            max_tokens=_params.LLM_MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=self.conversation_history,
        )

        reply = response.content[0].text
        self.conversation_history.append({"role": "assistant", "content": reply})
        return reply

    def reset_conversation(self):
        """Clear conversation history for a fresh session."""
        self.conversation_history = []


PIPELINE = RAGPipeline()
