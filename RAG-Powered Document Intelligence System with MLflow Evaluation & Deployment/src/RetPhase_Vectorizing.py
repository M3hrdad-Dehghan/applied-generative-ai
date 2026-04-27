#%%
# ==========================================================
# Loading
# ==========================================================
# Scripts
from RetPhase_EmbeddingClass import EMBEDDER
from RetPhase_VectorStoreClass import VECTOR_STORE
from RetPhase_Splitting import CHUNK



# ==========================================================
# # Step 5: Convert Chunks to Embeddings and Store
# ==========================================================
# Extract content from chunks
texts = [doc.page_content for doc in CHUNK]

# Generate the Embeddings by Embedding Manager Class
embeddings = EMBEDDER.generate_embeddings(texts)

# Store in the vector database by Vector Store Class
VECTOR_STORE.add_documents(CHUNK, embeddings)