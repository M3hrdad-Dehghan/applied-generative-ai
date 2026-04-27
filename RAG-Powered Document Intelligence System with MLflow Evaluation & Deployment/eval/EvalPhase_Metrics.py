# ==========================================================
# Evaluation Metrics
# ==========================================================
from typing import List, Dict, Any


def hit_rate(retrieved_docs: List[Dict], expected_source: str) -> float:
    """1.0 if at least one retrieved chunk comes from the expected source file."""
    for doc in retrieved_docs:
        if doc["metadata"].get("source_file", "") == expected_source:
            return 1.0
    return 0.0


def precision_at_k(retrieved_docs: List[Dict], expected_keywords: List[str]) -> float:
    """Fraction of retrieved chunks that contain at least one expected keyword."""
    if not retrieved_docs:
        return 0.0
    relevant = sum(
        1 for doc in retrieved_docs
        if any(kw.lower() in doc["content"].lower() for kw in expected_keywords)
    )
    return relevant / len(retrieved_docs)


def recall_at_k(retrieved_docs: List[Dict], expected_keywords: List[str]) -> float:
    """Fraction of expected keywords found across all retrieved chunks combined."""
    if not expected_keywords:
        return 0.0
    combined = " ".join(doc["content"].lower() for doc in retrieved_docs)
    found = sum(1 for kw in expected_keywords if kw.lower() in combined)
    return found / len(expected_keywords)


def evaluate_query(entry: Dict[str, Any], retrieved_docs: List[Dict]) -> Dict[str, Any]:
    """Compute all three metrics for a single question."""
    return {
        "id":               entry["id"],
        "question":         entry["question"],
        "hit_rate":         hit_rate(retrieved_docs, entry["source_file"]),
        "precision_at_k":   precision_at_k(retrieved_docs, entry["expected_keywords"]),
        "recall_at_k":      recall_at_k(retrieved_docs, entry["expected_keywords"]),
        "num_retrieved":    len(retrieved_docs),
        "scores":           [round(d["similarity_score"], 4) for d in retrieved_docs],
    }


def aggregate_metrics(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Compute mean metrics across all questions."""
    n = len(results)
    if n == 0:
        return {}
    return {
        "mean_hit_rate":        round(sum(r["hit_rate"]       for r in results) / n, 4),
        "mean_precision_at_k":  round(sum(r["precision_at_k"] for r in results) / n, 4),
        "mean_recall_at_k":     round(sum(r["recall_at_k"]    for r in results) / n, 4),
        "total_hits":           int(sum(r["hit_rate"] for r in results)),
        "num_questions":        n,
    }
