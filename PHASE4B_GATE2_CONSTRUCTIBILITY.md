# Phase 4B — Gate 2: Constructibility / Vacuity Check

**Project:** AI-Agent Memory Poisoning Research Project · **Gate 2 only. No detector/mechanism design. No novelty/patentability.**
Date: 2026-08-21.

---

## FINAL STATUS: 🟡 EVIDENCE BLOCKED — Gate 2 could not be validly executed in this environment.

This is **not** 🔴 (vacuous / poison unconstructible) and **not** 🟢 (constructibility confirmed). The pre-registered experiment requires a dense-neural embedding model and baseline detectors that this environment cannot obtain, and a faithful substitute is unavailable. Per project discipline I did **not** run a different-regime proxy and report it as the result, and I did **not** fabricate a pass/fail.

> **Distinction preserved (as required):** "cannot run here" ≠ "gate fails." A 🔴 STOP is warranted only if the poison class is *shown* unconstructible; that was not shown. The gate remains **unrun**.

---

## 1. What Gate 2 requires (from the locked Phase-4A spec)
Empirically construct a poison that is **single-entry + persistent + dormant + semantic-context-triggered + action/tool-use payload**, and verify it satisfies the **pre-registered** embedding-evasion criterion `AUROC(D_emb) ≤ τ` (τ≈0.5, fixed in advance) against an **embedding/retrieval-only** detector **in the regime MEMSAD and QPD operate in** — i.e., **dense neural retrieval embeddings** (MEMSAD = DPR gradient-coupled; QPD = retrieval-selectivity over dense retrieval). It must retain its malicious action payload (verified by executing the agent).

## 2. Verified environment capability probe (evidence)
Ran a direct capability check (this session):
- **Python 3.11**, `pip` can reach **pypi** (allowlisted) — packages installable.
- **Absent:** `torch`, `transformers`, `sentence_transformers`, `sklearn`, `numpy`, `scipy`, `gensim`, `faiss`, `openai`, `anthropic`.
- **No embeddings API key** (no OPENAI/HF/VOYAGE/COHERE; `ANTHROPIC_BASE_URL` set but Anthropic exposes no embeddings endpoint and no usable key is present).
- **No locally cached models** (`~/.cache/huggingface`, `~/.cache/torch` empty; no `*.safetensors` / `pytorch_model.bin` on disk).
- **`huggingface.co` egress-blocked** — `curl https://huggingface.co` → HTTP **000**. ⇒ transformers/sentence-transformers can be *installed* from pypi but **cannot load any pretrained weights** (weights come from HF).

**Conclusion:** no **dense sentence/retrieval embedder** (DPR, sentence-transformers, or equivalent) is obtainable here, and no embeddings API is available. Also, the **MEMSAD and QPD detector implementations** (GitHub/arXiv-hosted) are egress-blocked, so the baselines themselves cannot be instantiated.

## 3. Why a substitute is not acceptable
A pure-`sklearn` **TF-IDF / hashing / bag-of-words** vectorizer (installable from pypi with no HF) lives in a **lexical** vector space, not the **dense semantic** space MEMSAD/QPD assume. MINJA-class embedding-evasion is specifically about **dense semantic entanglement** of poisoned and benign records; a TF-IDF AUROC neither tests nor predicts dense-space evasion. Reporting it against the locked criterion would violate the pre-registration ("do not silently change the regime/thresholds") and the project's no-fabrication discipline. **Therefore no proxy result is reported.**

## 4. What I did NOT do (discipline)
- Did **not** run a different-embedding-regime proxy and present it as the constructibility answer.
- Did **not** hand-construct poison text and claim the *class* is constructible (text alone does not verify embedding-evasion in the dense regime nor payload execution).
- Did **not** design the detector, an algorithm, or a scoring function.
- Did **not** change any pre-registered threshold.
- Did **not** claim novelty or patentability.

## 5. Standing (pre-existing) evidence — provisional, non-substitutive
(Unchanged from `PHASE4B_PRECHECKS.md`; recorded so it is not lost, explicitly **not** a Gate-2 pass.) Published work suggests the class is *plausibly* constructible: MINJA reports poisoned/benign records "highly entangled in the embedding space, indistinguishable using simple similarity filtering"; MEMSAD detects MINJA at only **TPR 0.40 / AUROC 0.914**; Trojan Hippo demonstrates dormant context-triggered **action-sequence** (exfiltration) payloads; MemoryGraft demonstrates trigger-free dormant poison. This *motivates* the experiment; it does **not** replace the pre-registered measurement.

## 6. Exact requirements to execute Gate 2 (for a compute-enabled environment)
1. **Dense embedder** matching the baselines' regime: a DPR/sentence-transformer encoder (or the specific retriever the target agent uses) — requires HuggingFace access **or** a pre-downloaded model.
2. **Baseline detectors instantiated:** MEMSAD (write-time, needs retriever gradients) and QPD (retrieval-selectivity) — obtain code from their repos, or reimplement from the (currently egress-blocked) PDFs.
3. **A target agent** with a φ-vector-indexed experience memory + a sandbox with the sensitive tools for the action payload (harm oracle).
4. **Pre-registered config** `⟨E, d, C, τ, α⟩` fixed **before** running; reference corpus `C` of legitimate memories.
5. **Procedure:** construct a MINJA/Trojan-Hippo-class single-entry poison carrying an action-sequence payload → confirm (a) payload fires under a bounded context predicate and stays dormant otherwise (agent execution), (b) `AUROC(D_emb) ≤ τ` against MEMSAD's write-time signal and QPD's retrieval-selectivity, thresholds unchanged. **Pass** → record properties, proceed. **Fail** (cannot keep the payload while evading) → 🔴 vacuous, STOP.

---

## 6. Determination
> **Is the target poison class constructible and embedding-evasive against the locked baselines?**  **UNDETERMINED — the pre-registered experiment could not be run** (no dense embedder / no baseline detectors obtainable; HF egress-blocked; no embeddings API). No proxy was substituted; no result fabricated.
>
> **Gate 2 status: 🟡 EVIDENCE BLOCKED (unrun).** Not a failure of constructibility. **Do not proceed to Phase 4C / mechanism design.**

**To clear Gate 2:** authorize execution in an environment meeting §6 (HuggingFace/model access + baseline detector code + agent sandbox + GPU). I will then run the pre-registered procedure exactly and report a genuine 🟢 pass or 🔴 vacuous, with artifacts.

> Compliance: Gate 1 untouched; no mechanism designed; no novelty/patentability claimed; no threshold changed; no fabricated or proxy result presented as the locked-criterion answer.
