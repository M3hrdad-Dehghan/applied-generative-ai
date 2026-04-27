# %%
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================================================
# Used in the step 1 and file "RetPhase_Ingesting"
PDF_DIRECTORY = (PROJECT_ROOT / "data").as_posix()

# ==========================================================
# Used in the step 2 and file "RetPhase_Splitting"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

# ==========================================================
# Used in the step 3 and file "RetPhase_EmbeddingClass"
VECTORIZER_MODEL_NAME = "all-MiniLM-L6-v2"

# ==========================================================
# Used in the step 4 and file "RetPhase_VectorStoreClass"
VECTOR_STORE_DIRECTORY = (PROJECT_ROOT / "data" / "vector_store").as_posix()

# ==========================================================
# Used in the step 5 and file "RetPhase_Vectorizing"

# ==========================================================
# Used in the step 6 and file "RetPhase_Retrieving"
TOP_K = 3
SCORE_THRESHOLD = 0.2

# ==========================================================
# Used in the step 7 and file "AugPhase_SystemPrompt"

# ==========================================================
# Used in the step 8 & 9 and file "AugPhase_Answering"
LLM_MODEL_NAME = "claude-opus-4-5"
LLM_MAX_TOKENS = 1024