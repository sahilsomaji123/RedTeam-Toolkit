# Phase 3 — Adversarial Prior-Art Verification of the NARROWED Gap

**Project:** AI-Agent Memory Poisoning Research Project · **Phase 3: prior-art kill-test of the narrowed gap. No solution/architecture/algorithm/dataset/code.**
Date: 2026-08-21 · Supersedes the Phase-2A/2B framing per the user's verified correction.

> **Correction adopted (user-verified primary sources):** MEMSAD **does** perform pre-activation (write-time) detection for persistent agent memory and evaluates AgentPoison/MINJA/InjecMEM. Therefore the broad Phase-2 gap ("pre-activation detection of persistent memory poisoning") is **REJECTED as too broad**, and my earlier "no pre-activation detector exists" statements are withdrawn. This report tests only the **narrowed** gap.
>
> **Environment limitation (unchanged):** all paper-hosting domains (arxiv, ar5iv, export.arxiv, HuggingFace, Semantic Scholar, OpenReview, ResearchGate, research.google) are egress-blocked (HTTP 403). I could **not** read full text myself. Evidence below is **[USER-VERIFIED]** (facts the user supplied), **[SEARCH]** (search-surfaced excerpts, not full text), or **[INFERRED]**. Every matrix cell marked **[SEARCH]/[INFERRED]** requires PDF confirmation before any novelty claim.

---

## NARROWED GAP UNDER TEST
> **Black-box behavioral auditing of already-stored, dormant, single-entry memory poisoning that remains effective while being difficult to distinguish in embedding space, without access to the victim embedding function, gradients, or internal model state** — covering: already-stored (not write-time), dormant/conditional, single-entry, embedding-preserving, semantic/contextual activation predicate, action/tool-use payload, black-box (no embedding/gradient), cross-session, adaptive adversary, and **detection + localization of the vulnerable entry and its activation condition.**

---

## 1. The kill attempt — strongest threats first

I tried to occupy the cell with the closest works. Two came closest; neither occupies it.

### Threat A — **Semantic Chameleon / QPD** (2603.18034) *[SEARCH]* — the single strongest adjacent
- **What it does:** RAG-corpus poisoning attacks **and** a defense, **Query Pattern Differential (QPD)**: "measures the **behavior of a document across query types** rather than static properties"; QPD ≈ 1.0 ⇒ a document retrieved **almost exclusively for sensitive queries** = targeted-poisoning signature; most robust cross-corpus signal (3.7× corpus gap vs 13–62× for static methods).
- **Why it does NOT occupy the cell:** (i) the "behavior" it measures is **retrieval selectivity** (which *query types* pull the doc) — a **retrieval-layer** signal, **not** agent **action/tool-use** behavior; (ii) it requires the poison to be **selectively retrieved** for a narrow sensitive-query class → an **embedding-preserving** entry entangled with benign memory and retrieved broadly (MINJA-style) has QPD far from 1.0 and **evades** it; (iii) trigger = **query content** (sensitive query types), not a **semantic context predicate** (role × task × tool-availability) absent from the query text; (iv) domain = **RAG document corpus**, payload = **answer manipulation**, not persistent **experience memory** with an **action-sequence** payload; (v) passive statistical measurement over a query workload, not proactive elicitation.
- **Verdict:** closest neighbor; misses on ≥4 defining axes (action vs retrieval behavior; embedding-preserving; context-predicate; agent-memory/action payload).

### Threat B — **MemAudit** (2605.23723) *[SEARCH, corroborated]*
- **What it does:** "post-hoc question of which stored memories are responsible **after harmful behavior has already been observed**"; counterfactual memory-influence score + memory-consistency graph; removes suspicious memories **without poison labels**; evaluated vs MINJA; **already-stored + localization**.
- **Why it does NOT occupy the cell:** it is **post-hoc / reactive** — it **requires an observed harmful behavior** as its starting point. The narrowed gap is **proactive**: audit the **dormant** store **before** the trigger fires / before harm. MemAudit is the post-incident sibling, not the pre-trigger auditor.
- **Verdict:** occupies "already-stored + localize" but on the **wrong side of the trigger** (after activation).

### Threat C — **MEMSAD** (2605.03482) *[USER-VERIFIED + SEARCH]*
- **What it does:** formalizes memory poisoning as a **Stackelberg game** (AgentPoison α=WRITE gradient over DPR embeddings; MINJA α=QUERY; InjecMEM α=SINGLE); MEMSAD = **write-time anomaly detection** with a **gradient-coupling theorem linking anomaly-score gradients to retrieval-objective gradients**; detects MINJA at **TPR 0.40 / AUROC 0.914**, InjecMEM TPR 0.20; notes untriggered attacks "naturally mitigated by corpus scale."
- **Why it does NOT occupy the cell:** (i) **write-time / pre-ingestion**, not **already-stored** auditing; (ii) **requires retriever/embedding gradients (white-box embedding access)** — the gradient-coupling theorem is its core; the narrowed gap forbids embedding/gradient access; (iii) weak on the embedding-benign query-only class (TPR 0.40 on MINJA); (iv) flags candidate **writes**, not localizing a **resident dormant** entry + its **action** condition.
- **Verdict:** the important pre-activation baseline, but **write-time + white-box** — a different quadrant.

### Threat D — **Forensic Trajectory Signatures** (2606.30566) *[SEARCH]*
- Black-box, "lightweight structural features without model internals," detects a **behavioral invariant in the execution trajectory** (e.g., `memory_recall → email_send`), AUC 0.99; studies **3 adaptive evasions**. **Action-behavior + black-box + adaptive** — the closest on those axes.
- **Why it does NOT occupy the cell:** **activation-time / reactive** — it detects **while the attack executes its trajectory**; it does **not proactively audit the dormant store before the trigger**, and localizes the **channel**, not the specific **entry + activation predicate** pre-incident.
- **Verdict:** occupies "black-box + action-behavior + adaptive" but is **reactive at activation**, not proactive pre-trigger.

### Threat E — RAG dormant/single-doc/black-box cluster *[SEARCH]*
- **Phantom** (dormant keyword trigger), **DenialRAG/AdversarialCoT/WARP** (single-doc), **CtrlRAG/MIRAGE/RIPRAG** (black-box **attacks**); detectors **RevPRAG** (activation anomalies, white-box), **GMTP** (gradient masked-token), **RAGMask/RAGuard** (token/perplexity), **canary probes** (detect **embedding-space distortion**), geometric clustering.
- **Why they do NOT occupy the cell:** all key on **retrieval geometry / token / activation** signals ⇒ **embedding-preserving** poison evades them (Phantom's own clustering is what reveals it; MINJA is explicitly non-clustered/entangled); RAG **corpus** + **answer** payload, not agent experience memory + **action**; detectors are white-box (RevPRAG/GMTP) or geometry-dependent (canary).

### Adjacent (not detectors of the cell)
- **A-MemGuard** (2510.02373): proactive **at retrieval** (dual-memory, reasoning-path consistency), reactive to the retrieving query; reasoning-consistency, not action-elicitation; no entry localization. *[SEARCH]*
- **VIGIL**: runtime **SMT policy monitor** over tool traces; needs a policy spec + activation. *[SEARCH]*
- **PI-Hunter** (2606.12737): IPI **ingestion-path** red-teaming, not persistent-memory-at-rest auditing (Phase-2C; user-verified). *[USER-VERIFIED]*
- **Trojan Hippo** (2605.01970): **attack** — confirms the exact threat: dormant until finance/health/legal/tax/identity topics, **exfiltration action sequence**, "hard to detect when entries are audited in isolation." *[SEARCH]*
- **Benchmarks** — **MEMSecBench, MPBench (3,240 cases, "explicitly motivating behavioral detection but NOT providing a detector"), MemPoison-Bench, ASB, AgentLAB**: substrates, **no detector** for the cell; benchmark novelty is therefore **dead**. *[SEARCH]*

---

## 2. Comparison matrix (against the 11 narrowed axes)

Y=yes, N=no, ~=partial, evidence tag per row. "No-emb" = operates without victim embedding function/gradients.

| Paper (year) | Persist. mem | Already-stored audit | Dormant trigger | Single-entry | Black-box | No-emb access | Action payload | Cross-session | Adaptive adv. | Detect+localize | Evid. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **MEMSAD** (2026) | Y | **N** (write-time) | ~ | Y | **N** (WB gradient) | **N** | N (answer/retrieval) | Y | Y (Stackelberg) | ~ (flags writes) | UV+S |
| **MemAudit** (2026) | Y | **Y** | Y | Y | ~Y | ~Y | ~ (harmful outputs) | Y | ? | **Y** | S |
| **Semantic Chameleon / QPD** (2026) | N (RAG corpus) | Y (offline) | Y | Y | Y | ~ (retrieval-pattern) | **N** (answer) | N/A | ~ | Y (doc) | S |
| **Forensic Trajectory Sig.** (2026) | Y | **N** | N (activation) | ~ | Y | Y | **Y** | Y | Y (3 evasions) | ~ (channel) | S |
| **A-MemGuard** (2025) | Y | ~ (retrieval) | ~ | ~ | Y | ~ | N (reasoning) | Y | ? | N | S |
| **RevPRAG/GMTP/canary/Phantom-def** | N (RAG) | Y/~ | Y (geom) | Y | ~/N | **N** (geom/act/token) | N (answer) | N/A | ~ | Y (doc) | S |
| **VIGIL** | Y | N | N (runtime) | ~ | Y | Y | Y | Y | ~ | ~ | S |
| **PI-Hunter** (2026) | **N** (IPI paths) | N | N | ~ | Y | Y | Y | ~ | Y | ~ (path) | UV |
| **TARGET (narrowed gap)** | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** | — |

**No row matches the TARGET row.** The two closest — **MemAudit** and **QPD** — each diverge on the same core axes: MemAudit is **post-hoc (not pre-trigger)**; QPD is **retrieval-behavior/answer-payload/RAG-corpus (not action-elicitation/agent-memory)** and **embedding-preserving-evadable**.

---

## 3. Precise remaining technical gap (what is unoccupied)
No located work performs **proactive** (pre-trigger, pre-incident) auditing of an **already-resident** agent **experience-memory** store that (a) is **black-box** with **no victim embedding/gradient/internal access**, (b) targets **embedding-preserving** single dormant entries that geometry/canary/QPD signals miss, (c) is triggered by a **semantic context predicate** (role × task × tool-availability) not present in query text, (d) manifests only as an **action/tool-use sequence**, and (e) **localizes both the offending entry and its activation condition** — under an **adaptive adversary aware of the auditing procedure**. The field's benchmarks (MPBench) **explicitly call for behavioral detectors that do not yet exist**.

The surviving distinction reduces to a crisp axis pair the closest works split on:
- **Retrieval-behavior (QPD) vs. action-behavior elicitation** — QPD infers from *which queries retrieve* the entry; the gap requires observing *what the agent does* when a candidate context predicate holds.
- **Post-hoc (MemAudit) / activation-time (Forensic Trajectory Sig.) vs. proactive pre-trigger** — both existing behavioral detectors need the attack to have fired; the gap requires surfacing it before.
- **White-box embedding/gradient (MEMSAD) vs. black-box no-embedding** — MEMSAD's guarantee is a gradient-coupling theorem; the gap forbids that access.

---

## 4. Honest threats to the gap's *durability* (not yet occupied, but at risk)
1. **QPD generalization:** if Semantic Chameleon's QPD is re-run on agent experience memory with action-labeled queries, it could partially cover the cell. **Must read the paper** to confirm QPD needs retrieval-selectivity (evaded by embedding-preserving poison).
2. **MemAudit made proactive:** MemAudit's counterfactual-influence machinery could, in principle, be run speculatively (without a real incident) — is that a "trivial adaptation"? **Must read** to judge whether pre-incident operation is a fundamentally different mechanism (no observed-harm anchor) or an easy extension.
3. **Forensic Trajectory Signatures + sandbox pre-execution:** running its activation-time classifier over *elicited* trajectories could approximate proactivity. Needs assessment.
4. **Fast-moving field:** MPBench explicitly motivates behavioral detectors; a detector paper could appear at any time (this is a live 2026 frontier, not a quiet corner).

These are **novelty/non-obviousness risks**, which per instructions are **not** decided now.

---

## 5. Final Phase-3 determination

> **Does any existing paper occupy the narrowed cell (proactive, black-box-no-embedding, already-stored, embedding-preserving, dormant, single-entry, semantic-context-predicate, action-payload, cross-session, adaptive, with entry+condition localization)?**
>
> **Answer: NO located work occupies the exact cell** (on search-level + user-verified evidence). The gap **survives** adversarial prior-art verification. Closest occupants: **MemAudit** (post-hoc) and **Semantic Chameleon/QPD** (retrieval-behavior, RAG, answer-payload) — each missing ≥2 defining axes.

### Verdict: 🟢 NARROWED GAP SURVIVES — PROCEED, **conditional**
Two conditions before any mechanism design or novelty claim:
- **C1 (primary-source):** obtain and read full text of **Semantic Chameleon/QPD (2603.18034)**, **MemAudit (2605.23723)**, **MEMSAD (2605.03482)**, **Forensic Trajectory Signatures (2606.30566)** to lock every matrix cell flagged [SEARCH] and resolve the four durability threats in §4. (Egress-blocked here — supply PDFs or use an unblocked environment.)
- **C2 (framing):** treat the surviving distinction as a **narrow conjunction** (action-elicitation × embedding-preserving × proactive × agent-memory × localization). Its **non-obviousness is a separate question** (deferred), because QPD already establishes *behavioral* dormant-poison detection and Forensic Trajectory Signatures already establishes *black-box action-behavior* detection — the contribution must be the **proactive, embedding-preserving, action-eliciting** combination, not "behavioral detection" per se.

**Do not** proceed to mechanism design until C1 clears. **No novelty or patentability is claimed.** The gap is *unoccupied*, not yet *proven novel*.

---

## 6. Strongest baselines to carry forward (locked)
B1 none · **B2 MemAudit** (post-hoc; run proactively as an ablation) · **B3 Semantic Chameleon/QPD** (retrieval-behavior) · **B4 Forensic Trajectory Signatures** (activation-time action-behavior; beat on *lead-time*) · **B5 MEMSAD** (write-time white-box upper bound) · B6 A-MemGuard (retrieval-time reasoning consistency) · B7 canary/geometric (embedding-distortion) · B8 VIGIL (policy monitor). Benchmarks: MPBench / MemSecBench as substrates (not novel).

> Compliance: no detector, probing algorithm, scoring function, trigger-search procedure, dataset, or code is proposed. This is prior-art verification only; all [SEARCH] evidence is flagged and treated as provisional pending the C1 full-text reads.
