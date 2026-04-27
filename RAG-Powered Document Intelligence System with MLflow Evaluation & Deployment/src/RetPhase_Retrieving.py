#%%
# ==========================================================
# Loading
# ==========================================================
# Parameters
import __parameters as _params
TOP_K = getattr(_params, "TOP_K")
SCORE_THRESHOLD = getattr(_params, "SCORE_THRESHOLD")

# Scripts
from RetPhase_VectorStoreClass import VECTOR_STORE
from RetPhase_EmbeddingClass import EMBEDDER

# Libraries
from typing import List, Any, Dict



# ==========================================================
# # Step 6: Create Retriever Class to read from Vector Store
# ==========================================================
class RAGRetriever:
    def __init__(self, vector_store, embedding_manager):
        self.vector_store = vector_store
        self.embedding_manager = embedding_manager

    def retrieve(self, query: str, top_k: int = TOP_K, score_threshold: float = SCORE_THRESHOLD) -> List[Dict[str, Any]]:
        print(f"Retrieving documents for query: '{query}'")
        print(f"Top K: {top_k}, Score threshold: {score_threshold}")
        
        # Generate query embedding
        query_embedding = self.embedding_manager.generate_embeddings([query])[0]
        
        # Search in vector store
        try:
            results = self.vector_store.collection.query(
                query_embeddings=[query_embedding.tolist()],
                n_results=top_k
            )
            
            # Process results
            retrieved_docs = []
            
            if results['documents'] and results['documents'][0]:
                documents = results['documents'][0]
                metadatas = results['metadatas'][0]
                distances = results['distances'][0]
                ids = results['ids'][0]
                
                for i, (doc_id, document, metadata, distance) in enumerate(zip(ids, documents, metadatas, distances)):
                    # Convert distance to similarity score (ChromaDB uses cosine distance)
                    similarity_score = 1 - distance
                    
                    if similarity_score >= score_threshold:
                        retrieved_docs.append({
                            'id': doc_id,
                            'content': document,
                            'metadata': metadata,
                            'similarity_score': similarity_score,
                            'distance': distance,
                            'rank': i + 1
                        })
                
                print(f"Retrieved {len(retrieved_docs)} documents (after filtering)")
            else:
                print("No documents found")
            
            return retrieved_docs
            
        except Exception as e:
            print(f"Error during retrieval: {e}")
            return []

    def format_context(self, retrieved_docs: List[Dict[str, Any]]) -> str:
        if not retrieved_docs:
            return "No relevant documents found."

        context_parts = []
        for doc in retrieved_docs:
            rank = doc["rank"]
            score = doc["similarity_score"]
            source = doc["metadata"].get("source_file", "unknown")
            page = doc["metadata"].get("page", "?")
            content = doc["content"]

            context_parts.append(
                f"[Source {rank}: {source} | Page {page} | Score: {score:.3f}]\n{content}"
            )

        return "\n\n---\n\n".join(context_parts)



RAG_RETRIEVER = RAGRetriever(VECTOR_STORE, EMBEDDER)

if __name__ == "__main__":
    _results = RAG_RETRIEVER.retrieve("when is last time brazil win the world cup?")
    print(RAG_RETRIEVER.format_context(_results))


