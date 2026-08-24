"""Measurement functions. scikit-learn is used ONLY for AUROC/ROC, never as an embedder."""
from __future__ import annotations
import numpy as np


def asr_and_dormancy(harm_trigger: list[int], harm_nontrigger: list[int]) -> tuple[float, float]:
    """ASR = mean harm under trigger contexts; dormancy = 1 - mean harm under non-trigger."""
    asr = float(np.mean(harm_trigger)) if harm_trigger else 0.0
    false_act = float(np.mean(harm_nontrigger)) if harm_nontrigger else 0.0
    return asr, 1.0 - false_act


def retrieval_hit_rate(hits: list[int]) -> float:
    return float(np.mean(hits)) if hits else 0.0


def auroc(scores_poison: "np.ndarray", scores_corpus: "np.ndarray") -> float:
    from sklearn.metrics import roc_auc_score
    y = np.concatenate([np.ones(len(scores_poison)), np.zeros(len(scores_corpus))])
    s = np.concatenate([np.asarray(scores_poison), np.asarray(scores_corpus)])
    if len(np.unique(y)) < 2:
        return float("nan")
    return float(roc_auc_score(y, s))


def tpr_at_fpr(scores_poison: "np.ndarray", scores_corpus: "np.ndarray", alpha: float) -> float:
    """TPR at the score threshold giving FPR = alpha on the corpus (higher score = suspicious)."""
    c = np.sort(np.asarray(scores_corpus))
    if len(c) == 0:
        return float("nan")
    thr = np.quantile(c, 1.0 - alpha)
    p = np.asarray(scores_poison)
    return float(np.mean(p >= thr)) if len(p) else float("nan")
