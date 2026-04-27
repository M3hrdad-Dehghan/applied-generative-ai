
# %%
# ==========================================================
# Loading
# ==========================================================
# Parameters
import __parameters as _params
PDF_DIRECTORY = getattr(_params, "PDF_DIRECTORY")

# Libraries
from langchain_community.document_loaders import PyPDFLoader
import pathlib


# ==========================================================
# Step 1: Ingest Documents
# ==========================================================
def ingest_pdf_docs(pdf_directory):
    all_documents = []
    pdf_dir = pathlib.Path(pdf_directory)

    # Find all PDF files recursively
    pdf_files = list(pdf_dir.glob("**/*.pdf"))
    print(f"Found {len(pdf_files)} PDF files to process")

    for pdf_file in pdf_files:
        print(f"\nProcessing: {pdf_file.name}")
        try:
            loader = PyPDFLoader(str(pdf_file))
            documents = loader.load()

            # Add source information to metadata
            for doc in documents:
                doc.metadata['source_file'] = pdf_file.name
                doc.metadata['file_type'] = 'pdf'

            all_documents.extend(documents)
            print(f"  ✓ Loaded {len(documents)} pages")

        except Exception as e:
            print(f"  ✗ Error: {e}")

    print(f"\nTotal documents loaded: {len(all_documents)}")
    return all_documents

if __name__ == "__main__":
    PDF_DOCS = ingest_pdf_docs(PDF_DIRECTORY)
