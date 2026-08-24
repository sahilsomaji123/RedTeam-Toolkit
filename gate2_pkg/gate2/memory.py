"""Persistent vector-indexed agent experience memory (FAISS, cosine via inner product on
L2-normalized vectors). Supports clean vs poisoned stores and cross-session persistence.
"""
from __future__ import annotations
import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
import numpy as np


@dataclass
class MemoryRecord:
    id: str
    text: str
    meta: dict = field(default_factory=dict)   # {session_id, ts, source, is_poison(bool, eval-only)}


class ExperienceMemory:
    """Vector store over ctx-embeddings; retrieval by query-embedding cosine top-k.

    is_poison in meta is bookkeeping for evaluation ONLY and is never shown to the agent
    or to the baseline detectors.
    """
    def __init__(self, embedder, top_k: int = 5):
        self.embedder = embedder
        self.top_k = top_k
        self.records: list[MemoryRecord] = []
        self._mat: "np.ndarray | None" = None
        self._index = None

    def add(self, rec: MemoryRecord) -> None:
        self.records.append(rec)
        self._index = None  # rebuild lazily

    def _build(self):
        import faiss
        texts = [r.text for r in self.records]
        self._mat = self.embedder.encode_ctx(texts).astype("float32") if texts else \
            np.zeros((0, 768), "float32")
        d = self._mat.shape[1] if self._mat.shape[0] else 768
        self._index = faiss.IndexFlatIP(d)   # inner product on normalized vecs == cosine
        if self._mat.shape[0]:
            self._index.add(self._mat)

    def retrieve(self, query: str) -> list[tuple[MemoryRecord, float]]:
        if self._index is None:
            self._build()
        if not self.records:
            return []
        q = self.embedder.encode_query([query]).astype("float32")
        k = min(self.top_k, len(self.records))
        sims, idx = self._index.search(q, k)
        return [(self.records[i], float(sims[0][j])) for j, i in enumerate(idx[0])]

    def clone(self) -> "ExperienceMemory":
        m = ExperienceMemory(self.embedder, self.top_k)
        m.records = list(self.records)
        return m

    def save(self, path: str | Path) -> None:
        Path(path).write_text(json.dumps([asdict(r) for r in self.records]))

    @classmethod
    def load(cls, path: str | Path, embedder, top_k: int = 5) -> "ExperienceMemory":
        m = cls(embedder, top_k)
        for d in json.loads(Path(path).read_text()):
            m.add(MemoryRecord(**d))
        return m
