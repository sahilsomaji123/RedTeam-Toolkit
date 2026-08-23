# Phase 2C — Blocking Evidence Verification (Gap #1)

**Project:** AI-Agent Memory Poisoning Research Project · **Phase 2C: primary-source verification ONLY. No solution, architecture, algorithm, dataset, or code.**
Date: 2026-08-21 · Depends on: Phase 2A/2B.

---

## ⛔ PRIMARY-SOURCE VERIFICATION BLOCKED

## FINAL DECISION: 🟡 GAP PROBABLY EXISTS — EVIDENCE INCOMPLETE → **NO-GO for Phase 3 / mechanism design.**

Phase 2C required **actual full text** of **PI-Hunter (2606.12737)**, **MEMSAD (2605.03482)**, and **RAGSieve (2608.13010)**. **None could be obtained.** Per Phase 2C's own **absolute stop condition**, I am not proceeding to mechanism design, and I am **not** declaring the gap verified (🟢). The concept still looks distinct on search-level evidence, but the primary-source verification the phase demands is impossible in this environment.

### Full-text retrieval attempts (all failed — HTTP 403 egress block)
Every legitimate full-text host was attempted and blocked by the session egress proxy:

| Host attempted | Result |
|---|---|
| `arxiv.org` (html + pdf) | ⛔ EGRESS_BLOCKED |
| `ar5iv.labs.arxiv.org` | ⛔ EGRESS_BLOCKED |
| `export.arxiv.org/pdf` | ⛔ EGRESS_BLOCKED |
| `huggingface.co/papers` | ⛔ EGRESS_BLOCKED |
| `semanticscholar.org` | ⛔ EGRESS_BLOCKED |
| `openreview.net` | ⛔ EGRESS_BLOCKED |
| `alphaxiv.org` | ⛔ EGRESS_BLOCKED |
| `research.google` | ⛔ EGRESS_BLOCKED |
| `researchgate.net` | ⛔ EGRESS_BLOCKED |

In this environment, **`WebFetch` cannot retrieve any external research paper** (every domain outside a narrow allowlist returns 403). Only `WebSearch` (snippets/AI summaries) functions. **Search snippets are explicitly disallowed by Phase 2C as a basis for confirming or killing the gap.** Therefore all "evidence" below is labeled **[SEARCH-RECONSTRUCTED — NOT FULL-TEXT-VERIFIED]** and does **not** satisfy the phase's evidentiary bar.

---

## 1. PI-Hunter — full-text evidence
**[SEARCH-RECONSTRUCTED — NOT FULL-TEXT-VERIFIED]**
- Search-level statements (consistent across multiple result sets): PI-Hunter "first analyzes the agent's accessible **tools, retrieval interfaces, and external interaction channels**, then constructs **source-aware test cases** and iteratively evolves them to induce the agent to **retrieve, process, and reveal latent malicious instructions embedded within the environment**"; it "exposes hidden vulnerable **ingestion paths**"; and it "targets **external data sources and tool-returned data** rather than the agent's internal long-term memory store."
- **What this suggests (unverified):** PI-Hunter is **indirect-prompt-injection / ingestion-path** red-teaming, not auditing of an **already-written persistent memory store** for **dormant** entries that activate **cross-session**.
- **What full text must still confirm:** (a) whether PI-Hunter ever treats a persistent LTM store as an "ingestion path" it probes at rest; (b) whether any evaluation covers cross-session dormant memory entries; (c) whether its elicitation loop can, without fundamental change, target a resident record that contains no overt instruction. **Until the PDF is read, these are open.**

## 2. PI-Hunter — claim-by-claim comparison
**[SEARCH-RECONSTRUCTED — every cell pending full-text confirmation]**

| Property | PI-Hunter (search-level) | Target gap |
|---|---|---|
| Persistent memory | Not the stated focus (external ingestion) | Yes |
| Memory at rest | Not indicated | Yes |
| Cross-session | Not indicated | Yes |
| Dormant poison | No (surfaces live injections) | Yes |
| Embedding-benign | Not addressed | Yes (defining) |
| Semantic trigger | Test-case evolution toward IPI | Bounded predicate |
| Action payload | Yes (agentic actions) | Yes (sequence) |
| Pre-activation | Proactive for IPI exposure | Yes (pre-trigger) |
| Black-box | Yes | Yes |
| Memory attribution | Localizes ingestion paths, not memory entries | Yes (which entry) |
| Adaptive attacker | Feedback-driven exploration | Yes |

**Verdict (provisional):** does **not** appear to cover the target — but this is the single most important full-text check and it is **UNVERIFIED**.

## 3. MEMSAD — full-text evidence
**[SEARCH-RECONSTRUCTED — NOT FULL-TEXT-VERIFIED]** Search-level: "gradient-coupled anomaly detection," anomaly-score gradient coupled to the retrieval-objective gradient ⇒ **requires model-internal gradient access**; retrieval-space; "near-perfect... preventive." **Full text must confirm** the white-box requirement is load-bearing (no black-box variant) and whether it detects embedding-benign (MINJA-class) poison or only embedding-anomalous poison.

## 4. RAGSieve — full-text evidence
**[SEARCH-RECONSTRUCTED — NOT FULL-TEXT-VERIFIED]** Search-level: RSQ (online) + **RSG (offline corpus inspection, no queries)**; "self-referenced local contrast," "density among semantically-similar, lexically-distinct neighbors." Implies reliance on an **embedding/density anomaly**. **Full text must confirm** the explicit claim that a **deliberately embedding-indistinguishable** record evades it (the paper likely does **not** evaluate MINJA-class embedding-benign poison — must verify, not assume).

## 5. MINJA — evidence
**[SEARCH-RECONSTRUCTED — NOT FULL-TEXT-VERIFIED]** Search-level (repeated across sources): "malicious and benign records are **highly entangled in the embedding space, indistinguishable using simple similarity-based filtering**"; "minimal distributional signal for surface-level detection"; query-only injection; bridging steps + progressive shortening; NL experience records; cross-session persistence; reasoning-trajectory payload (extensible to action sequence). This is the **strongest-supported** item, but still not full-text.

## 6. MemSecBench — evidence
**[SEARCH-RECONSTRUCTED — NOT FULL-TEXT-VERIFIED]** Write–Execute–Forget lifecycle; persistence/consequence/repair; 310 cases/48 contexts; cross-session. **No indication of a defender-side pre-activation *detection* metric or an embedding-benign vs. anomalous split.** Missing pieces are **not** claimed novel; they define a possible documented extension only.

## 7. Cross-domain killer analysis
On **search-level** evidence, the exact intersection (black-box + pre-activation + behavioral + **embedding-benign** + **persistent-memory-native** + memory-entry attribution) is **not** occupied by: RAG-poisoning detectors (embedding-anomaly), prompt-injection red-teamers (PI-Hunter/PISmith, IPI-scoped), model-backdoor / trojan trigger inversion (weight-space), knowledge-base poisoning defenses, memory-poisoning defenses (activation-time or post-hoc: Forensic Trajectory Signatures, MemAudit, VIGIL, `memory-blackbox`), retrieval-anomaly detection, or logic-bomb/program analysis (no gradient/CFG handle over an NL corpus + agent loop). **However, "not found in search" ≠ "does not exist"** — and Phase 2C explicitly forbids concluding from snippets.

## 8. Final gap determination (Section-9 question)
> *Does any existing paper demonstrate black-box, pre-activation detection of embedding-benign, semantically-triggered, action-payload poisoning in persistent agent memory?*
>
> **Answer: INSUFFICIENT EVIDENCE.** Search evidence leans **NO** (no such paper located), but the phase's evidentiary standard (full text of the three blockers) is **unmet**. Per the phase rule, INSUFFICIENT EVIDENCE ⇒ **STOP; do not proceed to mechanism design.**

## 9. Remaining uncertainty (ranked)
1. **PI-Hunter** could, in full text, reveal persistent-memory / cross-session dormant coverage → would collapse the gap to 🟠. *Highest risk.*
2. **RAGSieve RSG** might empirically catch MINJA-class poison (if its local-contrast test is more powerful than "simple similarity") → would narrow the embedding-benign premise.
3. **MEMSAD** might have (or trivially admit) a black-box approximation → would erode the black-box distinction.
4. A **2026 paper not surfaced** by search could already occupy the cell (fast-moving field; "not found" is weak evidence).

## 10. Exact evidence required to unblock
- **The three PDFs** (PI-Hunter 2606.12737, MEMSAD 2605.03482, RAGSieve 2608.13010) supplied directly, **or** an environment with arXiv/ACL/OpenReview egress. Priority order: **PI-Hunter ≫ RAGSieve ≈ MEMSAD.**
- For each: read Method + Threat Model + Evaluation; fill the Part-2/§3/§4 tables from the actual text; specifically test the three "must confirm" questions in §1, §3, §4.
- Nice-to-have: MINJA and MemSecBench PDFs to lock §5/§6.

## 11. Final GO / NO-GO
- **Mechanism design (Phase 3):** **NO-GO.** The absolute stop condition is in force.
- **Gap status:** 🟡 probably exists, **evidence incomplete**. Not killed, not confirmed.
- **Action:** **wait for the three papers to be supplied or an unblocked environment provided.** Do not design a research project around a gap inferred from search snippets.

---

> **Absolute-rule compliance:** No detector, probing algorithm, scoring mechanism, trigger-search algorithm, dataset, code, or experiment is proposed here. This is evidence verification only, and the verification is **BLOCKED**. No novelty or patentability is claimed. All non-blocked evidence is explicitly marked search-reconstructed and treated as insufficient per the phase's own rules.
