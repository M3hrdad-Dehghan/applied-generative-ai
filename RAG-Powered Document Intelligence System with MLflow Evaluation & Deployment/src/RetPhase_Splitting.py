# %%
# ==========================================================
# Loading
# ==========================================================
# Parameters
import __parameters as _params
CHUNK_SIZE = getattr(_params, "CHUNK_SIZE")
CHUNK_OVERLAP = getattr(_params, "CHUNK_OVERLAP")

# Libraries
from langchain_text_splitters import RecursiveCharacterTextSplitter


# ==========================================================
# # Step 2: Chunk Documents
# ==========================================================
def split_documents(documents, chunk_size, chunk_overlap):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )

    split_docs = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(split_docs)} chunks")

    # Show example of a chunk
    if split_docs:
        print(f"\nExample chunk:")
        print(f"Content: {split_docs[0].page_content[:200]}...")
        print(f"Metadata: {split_docs[0].metadata}")

    return split_docs


if __name__ == "__main__":
    from RetPhase_Ingesting import ingest_pdf_docs, PDF_DIRECTORY
    PDF_DOCS = ingest_pdf_docs(PDF_DIRECTORY)
    CHUNK = split_documents(PDF_DOCS, CHUNK_SIZE, CHUNK_OVERLAP)
