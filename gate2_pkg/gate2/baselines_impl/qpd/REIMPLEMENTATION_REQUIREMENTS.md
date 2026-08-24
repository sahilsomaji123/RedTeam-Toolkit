# QPD / Semantic Chameleon — Faithful-Reimplementation Requirements (NOT an implementation)

**Status: no official code located.** This document is a *requirements skeleton* to guide a
**clearly-labeled faithful reimplementation** of QPD / Semantic Chameleon (arXiv:2603.18034). It is
NOT code and NOT official. Do not implement until every "MUST EXTRACT FROM PDF" item is filled from
the paper.

> Produced in a sandbox WITHOUT arXiv full-text access. The score definition, threshold protocol, and
> reported metrics below are **not yet transcribed** — they must be read from the PDF on the networked
> machine and the reimplementation labeled "faithful reimplementation (non-official)". Do not fabricate.

## Paper (search-level, to confirm)
- Title: *Semantic Chameleon: Query-Selectivity Poisoning Detection for Retrieval-Augmented Memory* (QPD), arXiv:2603.18034.
- Author (search-level): Scott Thornton.
- Mechanism: **retrieval-selectivity / query-frequency differential**. Intuition: a poisoned record is
  crafted to be retrieved **selectively** — it surfaces disproportionately on the attacker's target
  ("sensitive") query distribution but not on a benign/background query distribution. QPD scores each
  record by the **differential retrieval frequency** across those two query workloads; a score near the
  extreme (≈ 1.0) is the poisoning signature.
- Class: **query-workload-time / retrieval-behavior** detector (black-box over retrieval hits; does NOT
  require retriever gradients — contrast with MEMSAD).

## MUST EXTRACT FROM PDF (fill before implementing)
1. **Exact QPD score `s_QPD(m)`** — the closed-form differential (e.g., hit-rate on sensitive queries
   minus / over hit-rate on benign queries; normalization; smoothing; top-k coupling to `k`).
2. **Definition of the two query workloads** — how "sensitive" vs "benign" query sets are constructed
   and sized; whether sensitive queries are attacker-known or estimated.
3. **Inputs:** record `m` (or its embedding), retriever `E`, sensitive query set `Q_s`, benign query
   set `Q_b`, retrieval depth `k`.
4. **Output:** per-record selectivity score; **threshold selection at a target FPR**.
5. **Hyperparameters:** `k`, workload sizes, any frequency-smoothing / Laplace constant, score cutoff.
6. **Calibration protocol + reported metrics:** the exact evaluation and operating point the paper
   reports (dataset, embedder, seeds) — reproduce it before any target trial.
7. **Dependencies:** retriever `E` + FAISS index; the paper's query datasets.

## Integration contract (already in `gate2/baselines.py`)
- Implement `QPD.score(records_ctx_emb, corpus_ctx_emb, query_workload_emb) -> per-record score`
  using the **2,000-query workload** the Gate-2 package builds. The signature already accepts a query
  workload; QPD **requires** it (unlike MEMSAD's gradient path).
- Implement `calibrate()` to reproduce the paper's reported protocol; if it cannot within a
  scientifically justified tolerance → **STATUS = BLOCKED** (do not tune to pass our experiment).

## ⚠ Integration concern specific to this Gate-2 setup (record, do not silently resolve)
QPD keys on **query-keyword sensitivity**: it assumes the poison is selective w.r.t. a *sensitive query
distribution*. Our locked threat model triggers on a **context predicate** `Ψ` (identity × task ×
tool-config over the 72-context lattice), **not** on a query keyword. Two consequences:
- The 2,000-query workload must be mapped to / partitioned by the 72-context lattice so that a
  "sensitive" vs "benign" split exists for QPD to score against. **How this mapping is defined is a
  faithfulness question** — it must follow the paper's construction of `Q_s`/`Q_b`, applied to our
  contexts, and be documented; it must **not** be reverse-engineered to make our attack look evasive.
- If QPD as published cannot be applied to a context-predicate trigger without altering its mechanism,
  that is itself a finding to **report** (it bears on whether QPD is an appropriate baseline for this
  cell), **not** a licence to weaken or swap the baseline.

## Fidelity rules
Do not modify the mechanism; do not substitute a generic anomaly detector; do not use TF-IDF/BM25;
do not weaken QPD to inflate evasion; label the artifact "faithful reimplementation (non-official)";
record every deviation from the paper.
