"""Dense embedders for the frozen regime: DPR (context+query) and bge-base-en-v1.5.

These are the retrieval embeddings the agent and the BASELINE detectors operate in.
No TF-IDF/BM25/proxy. Heavy imports are function-local so the module can be inspected
without the ML stack installed.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol
import numpy as np


def _l2norm(x: "np.ndarray") -> "np.ndarray":
    n = np.linalg.norm(x, axis=-1, keepdims=True)
    n[n == 0] = 1.0
    return x / n


class Embedder(Protocol):
    name: str
    def encode_ctx(self, texts: list[str]) -> "np.ndarray": ...
    def encode_query(self, texts: list[str]) -> "np.ndarray": ...


@dataclass
class DPREmbedder:
    """facebook/dpr-*-single-nq-base. Separate context and question encoders."""
    ctx_model: str = "facebook/dpr-ctx_encoder-single-nq-base"
    q_model: str = "facebook/dpr-question_encoder-single-nq-base"
    device: str = "cpu"
    name: str = "DPR"

    def __post_init__(self):
        import torch  # noqa
        from transformers import (
            DPRContextEncoder, DPRContextEncoderTokenizerFast,
            DPRQuestionEncoder, DPRQuestionEncoderTokenizerFast,
        )
        self._torch = torch
        self._ce = DPRContextEncoder.from_pretrained(self.ctx_model).to(self.device).eval()
        self._ct = DPRContextEncoderTokenizerFast.from_pretrained(self.ctx_model)
        self._qe = DPRQuestionEncoder.from_pretrained(self.q_model).to(self.device).eval()
        self._qt = DPRQuestionEncoderTokenizerFast.from_pretrained(self.q_model)

    def _emb(self, enc, tok, texts):
        import numpy as np
        out = []
        with self._torch.no_grad():
            for i in range(0, len(texts), 32):
                b = tok(texts[i:i + 32], truncation=True, padding=True,
                        max_length=256, return_tensors="pt").to(self.device)
                out.append(enc(**b).pooler_output.cpu().numpy())
        return _l2norm(np.vstack(out)) if out else np.zeros((0, 768), dtype="float32")

    def encode_ctx(self, texts):   return self._emb(self._ce, self._ct, texts)
    def encode_query(self, texts): return self._emb(self._qe, self._qt, texts)


@dataclass
class STEmbedder:
    """sentence-transformers BAAI/bge-base-en-v1.5 (single encoder for both ctx and query)."""
    model: str = "BAAI/bge-base-en-v1.5"
    device: str = "cpu"
    name: str = "bge"

    def __post_init__(self):
        from sentence_transformers import SentenceTransformer
        self._m = SentenceTransformer(self.model, device=self.device)

    def _emb(self, texts):
        v = self._m.encode(list(texts), normalize_embeddings=True, batch_size=32,
                            show_progress_bar=False)
        return np.asarray(v, dtype="float32")

    def encode_ctx(self, texts):   return self._emb(texts)
    def encode_query(self, texts): return self._emb(texts)


def cosine(a: "np.ndarray", b: "np.ndarray") -> "np.ndarray":
    return _l2norm(a) @ _l2norm(b).T


def build_embedders(prereg_raw: dict, device: str = "cpu") -> dict[str, Embedder]:
    er = prereg_raw["embedding_regime"]
    return {
        "DPR": DPREmbedder(er["E1_DPR"]["ctx_encoder"], er["E1_DPR"]["query_encoder"], device),
        "bge": STEmbedder(er["E2_ST"]["model"], device),
    }
