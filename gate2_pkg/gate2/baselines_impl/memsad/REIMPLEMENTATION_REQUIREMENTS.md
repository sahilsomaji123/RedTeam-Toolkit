# MEMSAD — Faithful-Reimplementation Requirements (NOT an implementation)

**Status: no official code located.** This document is a *requirements skeleton* to guide a
**clearly-labeled faithful reimplementation** of MEMSAD (arXiv:2605.03482). It is NOT code and
NOT official. Do not implement until every "MUST EXTRACT FROM PDF" item is filled from the paper.

> Produced in a sandbox WITHOUT arXiv full-text access. The equations/theorems below are
> **not yet transcribed** — they must be read from the PDF on the networked machine and the
> reimplementation labeled "faithful reimplementation (non-official)". Do not fabricate them.

## Paper (search-level, to confirm)
- Title: *MEMSAD: Gradient-Coupled Anomaly Detection for Memory Poisoning in Retrieval-Augmented Agents*, arXiv:2605.03482.
- Author: Ishrith Gowda (UC Berkeley). ~28 pages, 6 theorems; NeurIPS 2026 submission.
- Framing: memory poisoning as a **Stackelberg game**; three attack classes by access — AgentPoison (WRITE, gradient over DPR embeddings), MINJA (QUERY), InjecMEM (SINGLE).
- Mechanism: **write-time** anomaly detection with a **gradient-coupling theorem** — under encoder regularity, the **anomaly-score gradient and the retrieval-objective gradient are coupled** ⇒ requires **white-box access to the retriever `E` (gradients)**.

## MUST EXTRACT FROM PDF (fill before implementing)
1. **Exact anomaly score `s_MEMSAD(m)`** — the closed-form / algorithm (the gradient-coupling statement + how the score is computed per candidate write).
2. **The gradient-coupling theorem** statement + the "encoder regularity" assumptions.
3. **Inputs:** candidate write record `m`, retriever `E` (which gradients), reference corpus, any query set.
4. **Output:** per-record score; decision threshold selection at a target FPR.
5. **Hyperparameters:** any temperature/step/regularization constants; top-k; batch settings.
6. **Calibration protocol + reported metrics:** the exact MINJA evaluation reproducing **TPR ≈ 0.40 / AUROC ≈ 0.914** (dataset, embedder = DPR, seeds, operating point).
7. **Dependencies:** DPR retriever with gradient access; torch autograd; the paper's datasets.

## Integration contract (already in `gate2/baselines.py`)
- Implement `MEMSAD.score(records_ctx_emb, corpus_ctx_emb, query_workload_emb=None) -> per-record score`
  **and** the retriever-gradient path it needs (the embedding-only signature may need extension to
  pass the retriever handle — do this faithfully, do not swap in a non-gradient proxy).
- Implement `calibrate()` to reproduce the MINJA window above; if it cannot within a scientifically
  justified tolerance → **STATUS = BLOCKED** (do not tune to pass our experiment).

## Code-availability update — 2026-08-24 (search-level, sandbox egress-blocked)
- Paper confirmed: arXiv:2605.03482, Ishrith Gowda (UC Berkeley); Stackelberg framing over three
  attack classes (AgentPoison WRITE / MINJA QUERY / InjecMEM SINGLE); MEMSAD = calibration-based
  defense grounded in a **gradient-coupling theorem**.
- **No official code located.** Author has a GitHub profile (`github.com/ishrith-gowda`, ~12 repos)
  but **no MEMSAD repository was visible** in search; no Papers-With-Code / project-page code link
  surfaced. ⇒ **ON THE NETWORKED MACHINE: re-check the author's GitHub + the PDF for a code link;**
  if none, proceed with the **faithful reimplementation** below (labeled non-official), and it is
  usable ONLY after `calibrate()` reproduces the paper's MINJA window (≈ TPR 0.40 / AUROC 0.914).
- Contact of record for a code request: ishrithgowda@berkeley.edu (author's stated email).

## Fidelity rules
Do not modify the mechanism; do not substitute a generic anomaly detector; do not use TF-IDF/BM25;
label the artifact "faithful reimplementation (non-official)"; record every deviation from the paper.
