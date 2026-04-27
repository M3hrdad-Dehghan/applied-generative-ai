#%%

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import mlflow
import itertools
from pathlib import Path

from EvalPhase_Dataset import EVAL_DATASET
from EvalPhase_Metrics import evaluate_query, aggregate_metrics

from RetPhase_Ingesting import ingest_pdf_docs
from RetPhase_Splitting import split_documents
from RetPhase_EmbeddingClass import EmbeddingManager
from RetPhase_VectorStoreClass import VectorStore
from RetPhase_Retrieving import RAGRetriever
import __parameters as _params


# ==========================================================
# Hyperparameter Grid
# ==========================================================
PARAM_GRID = {
    "embedding_model": [
        "all-MiniLM-L6-v2",
        "all-mpnet-base-v2",
    ],
    "chunk_size":      [300, 500, 700, 1000],
    "chunk_overlap":   [50, 100, 150, 200],
    "top_k":           [3, 5, 10],
    "score_threshold": [0.1, 0.2, 0.3],
}


# ==========================================================
# Helpers
# ==========================================================
def _build_index(embedding_model: str, chunk_size: int, chunk_overlap: int):
    print(f"\n>>> Indexing: model={embedding_model} | chunk={chunk_size} | overlap={chunk_overlap}")

    docs = ingest_pdf_docs(_params.PDF_DIRECTORY)
    chunks = split_documents(docs, chunk_size, chunk_overlap)

    embedder = EmbeddingManager(embedding_model)
    vector_store = VectorStore()

    texts = [doc.page_content for doc in chunks]
    embeddings = embedder.generate_embeddings(texts)

    vector_store.clear_collection()
    vector_store.add_documents(chunks, embeddings)

    return embedder, vector_store


def _run_eval(retriever: RAGRetriever, top_k: int, score_threshold: float) -> dict:
    per_question = []
    for entry in EVAL_DATASET:
        retrieved = retriever.retrieve(entry["question"], top_k, score_threshold)
        result = evaluate_query(entry, retrieved)
        per_question.append(result)

    return {
        "aggregate": aggregate_metrics(per_question),
        "per_question": per_question,
    }


# ==========================================================
# Main Experiment Loop
# ==========================================================
def run_experiments():
    mlflow.set_tracking_uri(Path(os.path.join(os.path.dirname(__file__), "mlruns")).as_uri())
    mlflow.set_experiment("RAG Hyperparameter Search")

    index_configs = list(itertools.product(
        PARAM_GRID["embedding_model"],
        PARAM_GRID["chunk_size"],
        PARAM_GRID["chunk_overlap"],
    ))

    query_configs = list(itertools.product(
        PARAM_GRID["top_k"],
        PARAM_GRID["score_threshold"],
    ))

    total_runs = len(index_configs) * len(query_configs)
    run_number = 0

    for embedding_model, chunk_size, chunk_overlap in index_configs:
        # Reindex once per index config
        embedder, vector_store = _build_index(embedding_model, chunk_size, chunk_overlap)
        retriever = RAGRetriever(vector_store, embedder)

        for top_k, score_threshold in query_configs:
            run_number += 1
            print(f"\n[{run_number}/{total_runs}] top_k={top_k} | threshold={score_threshold}")

            results = _run_eval(retriever, top_k, score_threshold)
            agg = results["aggregate"]

            with mlflow.start_run():
                # Log parameters
                mlflow.log_param("embedding_model",  embedding_model)
                mlflow.log_param("chunk_size",        chunk_size)
                mlflow.log_param("chunk_overlap",     chunk_overlap)
                mlflow.log_param("top_k",             top_k)
                mlflow.log_param("score_threshold",   score_threshold)

                # Log aggregate metrics
                mlflow.log_metric("mean_hit_rate",       agg["mean_hit_rate"])
                mlflow.log_metric("mean_precision_at_k", agg["mean_precision_at_k"])
                mlflow.log_metric("mean_recall_at_k",    agg["mean_recall_at_k"])
                mlflow.log_metric("total_hits",          agg["total_hits"])

                # Log per-question breakdown as a text artifact
                lines = ["id | hit | prec | recall | retrieved | question"]
                for r in results["per_question"]:
                    lines.append(
                        f"{r['id']} | {r['hit_rate']} | {r['precision_at_k']:.2f} | "
                        f"{r['recall_at_k']:.2f} | {r['num_retrieved']} | {r['question'][:60]}"
                    )
                artifact_path = os.path.join(os.path.dirname(__file__), "_tmp_results.txt")
                with open(artifact_path, "w") as f:
                    f.write("\n".join(lines))
                mlflow.log_artifact(artifact_path, artifact_path="per_question")
                os.remove(artifact_path)

    print(f"\nDone. {total_runs} runs logged.")
    print("Launch MLflow UI with:")
    print(f"  cd \"{os.path.dirname(__file__)}\"")
    print(f"  mlflow ui")


if __name__ == "__main__":
    run_experiments()