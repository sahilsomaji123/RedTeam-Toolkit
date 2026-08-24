"""BASELINE embedding/retrieval-only detectors that the poison must EVADE: MEMSAD and QPD.

These are the pre-existing baselines from the locked cell (NOT the Phase-4C proposed
detector). The official code is not on PyPI; integrate it here or reimplement strictly to
the paper, then PASS the calibration gate before use. A generic embedding-only anomaly
detector is provided only as the mechanism for computing the AUROC(poison vs C) evasion
metric where the paper's own scorer is a per-record embedding statistic; it does NOT
replace MEMSAD/QPD and must not be silently substituted for them.
"""
from __future__ import annotations
from typing import Protocol
import numpy as np


class BaselineDetector(Protocol):
    name: str
    def score(self, records_ctx_emb: "np.ndarray", corpus_ctx_emb: "np.ndarray",
              query_workload_emb: "np.ndarray | None" = None) -> "np.ndarray":
        """Return a per-record suspicion score (higher = more suspicious)."""
        ...


class MEMSAD:
    """MEMSAD write-time gradient-coupled anomaly detector (arXiv:2605.03482).
    INTEGRATION REQUIRED: this needs the retriever's gradients (white-box over E).
    Drop the official implementation here. Must pass calibrate() before use.
    """
    name = "MEMSAD"
    def score(self, records_ctx_emb, corpus_ctx_emb, query_workload_emb=None):
        raise NotImplementedError(
            "Integrate MEMSAD (arXiv:2605.03482). Needs retriever gradients; do not fake it."
        )


class QPD:
    """Query Pattern Differential from Semantic Chameleon (arXiv:2603.18034).
    INTEGRATION REQUIRED: per-record retrieval-selectivity across the benign query workload.
    Must pass calibrate() before use.
    """
    name = "QPD"
    def score(self, records_ctx_emb, corpus_ctx_emb, query_workload_emb=None):
        raise NotImplementedError(
            "Integrate QPD / Semantic Chameleon (arXiv:2603.18034). Needs the query workload."
        )


def calibrate(detector: BaselineDetector, calib_bundle: dict) -> dict:
    """Reproduce the detector's reported behavior on its OWN attack before use.
    calib_bundle supplies the paper's attack + expected metric window, e.g. for MEMSAD:
    detect MINJA at ~TPR 0.40 / AUROC 0.914. Record deviations; do NOT tune the baseline
    to make the target experiment pass.
    Returns {passed: bool, observed: {...}, expected: {...}}.
    """
    raise NotImplementedError(
        "Run the detector on its paper's attack and compare to the expected metric window. "
        "If it cannot be faithfully reproduced -> STATUS=BLOCKED (do not substitute)."
    )
