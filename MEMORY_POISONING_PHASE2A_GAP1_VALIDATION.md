# Phase 2A — Final Validation of Gap #1 (Proactive trigger-elicitation auditing of dormant AI-agent memory)

**Project:** AI-Agent Memory Poisoning Research Project · **Phase 2A: gap validation only — NO solution design.**
Date: 2026-08-21 · Depends on: `MEMORY_POISONING_PHASE1_GAP_AUDIT.md`.

> **Environment limitation (disclosed):** `arxiv.org` full-text fetch is blocked by the session egress proxy (HTTP 403). Per-paper properties below are drawn from abstracts, author pages, and search-surfaced excerpts, **not** always from full text. Claims that a paper is "activation-time" / "white-box" / "IPI-scoped" are calibrated to that evidence and flagged where a full-text read is still required. This is validation, not a solution.

---

## FINAL DECISION

## 🟡 RESEARCH GAP WITH SIGNIFICANT CAVEATS

Gap #1 **survives**, but not as a clean 🟢. It survives only for a **bounded subclass** and against a specific, narrow intersection that the current state of the art does not cover. It is **not** 🟢 because adjacent capabilities (offline corpus auditing, elicitation red-teaming, trigger inversion, a near-perfect white-box preventive detector) already exist and the general problem is likely fundamentally intractable. It is **not** 🟠/🔴 because no located work performs **black-box, pre-activation** detection of **behavior-only, embedding-indistinguishable** dormant memory entries via **proactive elicitation over the memory store**, and the literature explicitly states input-/retrieval-level defenses "cannot observe this attack surface."

---

## 1. Full-text literature validation (properties matrix)

Legend — **Timing**: rest / retrieve / **activation** (needs harmful trajectory) / post-hoc. **Access**: black-box (BB) / white-box (WB). **Pre-act?** = detects before the attacker's trigger fires.

| Work | Role | Memory rep. | Trigger model | Payload | Timing | Access | Pre-act? |
|---|---|---|---|---|---|---|---|
| **MINJA** ([2503.03704]) | attack | NL experience records | query-only, semantic | reasoning/action steering | — | BB | — (evades input/output moderation; "no injection signature") |
| **AgentPoison** (NeurIPS'24) | attack | memory / RAG KB | optimized trigger → **isolated embedding cluster** | backdoor target | — | — | — (embedding footprint = detectable by clustering) |
| **MemPoison** ([2607.14651]) | attack + analysis | LTM entries | semantic relational bridge, **entity masquerading, joint-embedding isolation** | trigger-conditioned (L3 dormant) | — | — | states rest/write detection is open |
| **MemVenom** ([2606.10742]) | attack | multimodal web-agent memory | triggered | exfil/action | — | — | — |
| **MemoryGraft** ([2512.16962]) | attack | "successful experience" | benign-doc summarized | policy/behavior | — | BB | — |
| **Trojan Hippo** ([2605.01970]) | attack | memory | topic-conditioned dormant | **data exfiltration sequence** | — | BB | — |
| **Forensic Trajectory Signatures** ([2606.30566]) | **defense** | tool-call log | any (agnostic) | action seq (recall→send) | **activation** (prefix-only ⇒ near-real-time) | BB | **NO** (needs trajectory to begin) |
| **MEMSAD / MEM-SAD** ([2605.03482]) | **defense** | retrieved memory | — | — | retrieve (preventive) | **WB (gradient)** | partial (retrieval-space; WB) |
| **A-MemGuard** ([2510.02373]) | defense | retrieved memory | — | — | retrieve | BB | reactive to the retrieving query; single detector misses 66% |
| **MemAudit** ([2605.23723]) | defense | store | — | — | **post-hoc** | BB | NO |
| **SMSR** ([2606.12703]) | defense | signed entries | — | — | write+retrieve | BB | prevents *unsigned* injection (not detection of dormant authenticated poison) |
| **PI-Hunter** ([2606.12737]) | **red-team audit** | external ingestion paths | evolved test cases | IPI | proactive | BB | **YES but IPI-scoped**, not persistent memory |
| **PISmith** ([2603.13026]) | red-team | tool-returned data | RL-optimized | IPI | proactive | BB | IPI-scoped (InjecAgent/AgentDojo) |
| **RAGSieve (RSG)** ([2608.13010]) | defense | corpus index | — | — | **offline corpus audit** (no query) | BB | detects **embedding/density-anomalous** docs only |
| **Neural Cleanse / GangSweep / PICCOLO / DBS / CLIBE / CSO-LLM** | defense (model) | **weights** | trigger inversion | class flip | model scan | WB | weight-space; "barely converges" on complex/task-agnostic triggers |

**Key reads to still obtain in full text before Phase 2B:** MemPoison (2607.14651), Forensic Trajectory Signatures (2606.30566), MEMSAD (2605.03482), PI-Hunter (2606.12737), RAGSieve (2608.13010).

## 2. Attack-model comparison (model backdoor vs. agent-memory poisoning)
Confirms the analogy **breaks** on every axis that matters for detection:

| Property | Model backdoor (Neural Cleanse family) | Agent-memory poisoning (Gap #1 target) |
|---|---|---|
| Attack location | weights | external NL memory store |
| Trigger | input token/pattern (invertible via gradient) | **semantic/contextual condition** (discrete, non-differentiable over a corpus) |
| Payload | output class flip | **action sequence** (retrieve→tool→exfil→…) |
| Search space | continuous parameter/embedding space | **discrete memory corpus + unbounded semantic query space** |
| Detection signal | model activations/weights | memory content **+** downstream agent behavior |
| Access assumed | WB (weights) | ideally **BB** (operator has store + tool logs, not internals) |
**→ Weight-space trigger-inversion does not transfer.** (Validated: PICCOLO/DBS "barely converge" even in-model; no gradient handle exists over an external corpus.)

## 3. Defense comparison — where each fails on the target class
- **Content / input / output moderation** → fails: MINJA/MemoryGraft "no injection signature."
- **Embedding/retrieval anomaly** (RAGSieve, TrustRAG, GMTP, MEMSAD) → catches AgentPoison/MemPoison (embedding-isolated) but **misses behavior-only, embedding-benign poison**; literature: "retrieval-level defenses cannot observe the attack surface."
- **Trajectory / activation** (Forensic Trajectory Signatures) → strong but **only at activation** (harmful trajectory must start).
- **Post-hoc** (MemAudit) → after harm.
- **Elicitation red-team** (PI-Hunter, PISmith) → proactive but **IPI-scoped**, not persistent dormant memory.
- **Provenance/certified** (SMSR, Louck) → prevents *unsigned/laundered-origin* actionability; does not *detect* an authenticated-but-dormant poisoned belief.

## 4. Trigger taxonomy — coverage
| Trigger type | Covered by existing detection? |
|---|---|
| Exact textual | partially (semantic-drift 2511.15992 if you already have it; content filters) |
| **Semantic (paraphrase-invariant)** | **NO defensive discovery over memory** (PICCOLO/DBS invert in-model, WB, poorly) |
| **Contextual (identity×task×env×tools)** | **NO** |
| **Temporal (after N sessions/delay)** | NO (persistence measured, not pre-detected) |
| **Multi-condition** | NO |
| Behavioral (action-sequence) | at activation only (Forensic Trajectory Signatures) |

## 5. Payload taxonomy — coverage
Information/exfil (Trojan Hippo, MemLeak) · tool-invocation · instruction/reasoning steering (MINJA) · credential · **action-sequence** (Trojan Hippo) · policy (MemoryGraft) — all **evaluated as attacks**; **pre-activation detection** of the action-sequence class is not covered.

## 6. Pre-activation detection analysis
The only "preventive/pre-activation-ish" detectors are **MEMSAD** (WB gradient, retrieval-space) and **A-MemGuard** (BB, but reactive to the retrieving query; 66% miss). Neither performs **BB, store-wide, pre-trigger elicitation** against **behavior-only** poison. Forensic Trajectory Signatures is explicitly **activation-time**. → the pre-activation + BB + behavior-only cell is empty.

## 7. Cross-domain prior-art analysis (is it "just X"?)
- **Just RAG poisoning?** No — RAG-corpus detectors (RAGSieve/GMTP/TrustRAG) key on **embedding/density anomaly**; the target class is embedding-benign and harmful only via **agentic action**, which corpus scanners don't model. (But this is the closest neighbor — the memory-vs-RAG-corpus line is thin and must be defended empirically.)
- **Just prompt injection?** No — PI/PISmith/AgentDojo are **single-session, in-workflow**; the target is **persistent, cross-session, dormant**.
- **Just model backdoor detection?** No — weight-space, WB, non-transferable (§2).
- **Just trigger inversion?** No — inversion needs a differentiable model handle; here the "model" is an external corpus + agent loop.

## 8. Benchmark analysis
Rich attack/lifecycle benchmarks exist (**ASB, MemPoison-Bench, MemSecBench, AgentLAB (644 cases), BackdoorAgent, "Temporal/Spatial/Semantic Evasions" 2605.22321**). **But none is a *defender-side* benchmark for pre-activation detection of dormant, embedding-benign, semantic-trigger, action-payload memory entries** (they score *attack* success / lifecycle, not *proactive-detection* rate before the trigger). A defender-side benchmark for this subclass would itself be a contribution — **but only if** it is not a trivial re-labeling of MemSecBench's Forget/Execute splits (must confirm).

## 9. Strongest existing baseline (must beat)
1. **MEMSAD** — "near-perfect" preventive detection, **white-box gradient**. The upper-bound/oracle-ish baseline; a black-box method must approach it *without* internals.
2. **Forensic Trajectory Signatures** — AUC 0.99, black-box, **activation-time**. The realistic deployment baseline; a pre-activation method must show **earlier** detection (lead-time > 0) at comparable FPR.

## 10. Fundamental-hardness analysis
Strong evidence the **general** problem is intractable: "poisoned agents trigger no anomaly detection and **do exactly what they're supposed to based on a poisoned belief**" → a dormant entry is, at rest, **semantically indistinguishable** from a legitimate learned belief; the trigger space is **unbounded/semantic**; PICCOLO/DBS establish discrete-textual-trigger search "barely converges" even with WB gradients. **Conclusion:** arbitrary-semantic-trigger pre-activation detection without execution is likely undecidable-adjacent. **The gap is only tractable for a bounded subclass** (below).

## 11. Kill-test results
| Kill | Result |
|---|---|
| K1 proactive detection already implemented? | Partially — **RAGSieve offline corpus audit** (embedding-anomaly), **PI-Hunter elicitation** (IPI). Neither = BB pre-activation behavior-only memory. **Survives.** |
| K2 semantic trigger discovery implemented? | Yes for **model weights** (PICCOLO/DBS, WB, poor convergence); **not over external memory**. Survives. |
| K3 memory-specific backdoor detection implemented? | Yes but **activation-time** (Forensic Trajectory Sig) or **WB** (MEMSAD) or **post-hoc** (MemAudit). Pre-act BB behavior-only cell empty. Survives. |
| K4 benchmark already measures exact problem? | No defender-side pre-activation benchmark located; **must confirm vs MemSecBench**. Survives (weakly). |
| K5 just RAG poisoning? | No, but closest neighbor; defend empirically. Survives. |
| K6 just prompt injection? | No (persistence/dormancy). Survives. |
| K7 just model backdoor detection? | No (§2). Survives. |
| K8 existing defenses trivially adapted? | RAGSieve→behavior-only (fails premise), MEMSAD→BB (loses gradient), PI-Hunter→memory (untested). **Non-trivial.** Survives. |
| K9 computationally infeasible? | **Yes in general** → must bound (§10). Partial kill → scope restriction. |
| K10 too narrow to matter? | No — bounded subclass covers MINJA/AgentPoison/Trojan-Hippo single-entry attacks against production systems (ChatGPT memory, Copilot/EchoLeak, ElizaOS). Survives. |

**Nine of ten kills survive; K9 forces a scope restriction, not a rejection.**

## 12. Final research-gap statement (falsifiable)
> Existing defenses can (a) detect memory poison whose entries carry an **embedding/retrieval-space anomaly** (RAGSieve, TrustRAG, GMTP, MEMSAD-white-box), (b) detect a memory-poisoning attack **once it begins executing a harmful tool trajectory** (Forensic Trajectory Signatures, activation-time), and (c) proactively elicit **indirect-prompt-injection** vulnerabilities from external ingestion paths (PI-Hunter, PISmith) — but **no located black-box defense can, before the attacker's natural trigger occurs and without model internals, decide whether a benign-looking, embedding-indistinguishable persistent memory entry is a dormant, semantically-triggered, action-sequence backdoor**, because such an entry is content- and retrieval-indistinguishable from a legitimate learned belief and reveals itself only through a downstream action conditioned on an unknown semantic trigger.

## 13. Research question (for Phase 2B, if approved)
> For the **bounded subclass** of single-entry, semantic-trigger, action-payload memory poisons that **evade content/retrieval-anomaly detection**, can a **black-box** auditor **proactively elicit and identify the dormant poisoned entry before its natural trigger occurs**, achieving a detection rate and **pre-activation lead-time** meaningfully above the activation-time trajectory-detection baseline (Forensic Trajectory Signatures) and approaching the white-box preventive upper bound (MEMSAD), at acceptable false-positive cost to legitimate memory — and **what is the boundary of the trigger-predicate space within which this is tractable?**

## 14. Recommended scope
- **Threat:** single poisoned entry; **semantic trigger from a bounded predicate set** (e.g., user-identity × task-type × tool-availability); action-sequence payload observable in a sandbox; poison chosen from the **embedding-benign (MINJA/Trojan-Hippo) class** that content/retrieval detectors miss.
- **Access:** black-box (store contents + tool-call logs + sandbox execution), no model internals.
- **Baselines:** Forensic Trajectory Signatures (activation-time, realistic) and MEMSAD (white-box, upper bound).
- **Metrics:** pre-activation detection rate; detection lead-time vs. natural trigger; FPR on benign memory; trigger-predicate coverage; elicitation compute cost; scalability to N entries; memory-utility impact.
- **Explicitly out of scope:** arbitrary/unbounded semantic triggers (intractable), multi-entry compositional triggers (defer), model-weight backdoors.

## 15. What must NOT be claimed (guardrails for Phase 2B)
- **Do not** claim it "solves dormant memory poisoning" — only a bounded subclass.
- **Do not** claim novelty over **PI-Hunter** without an experiment showing it does **not** already cover persistent dormant memory (full-text read + empirical check required).
- **Do not** claim novelty over **RAGSieve/GMTP** without showing the target poison is **embedding-benign** (i.e., their detectors demonstrably miss it).
- **Do not** claim to beat **MEMSAD** on equal footing — MEMSAD is white-box; the contribution is **black-box + pre-activation + behavior-only**, not raw AUC.
- **Do not** claim general semantic-trigger detection is achievable (§10 hardness).
- **No patentability, no novelty-with-certainty.** Every survival above carries a residual kill-risk and a confirmation step.

---

## Mandatory confirmations before Phase 2B
1. Full-text read of **PI-Hunter** to confirm it does not cover persistent dormant memory (biggest single threat).
2. Full-text read of **MEMSAD** to confirm white-box requirement and whether it catches behavior-only poison.
3. Full-text read of **RAGSieve RSG** to confirm it keys on embedding anomaly (fails on embedding-benign).
4. Confirm **MemSecBench** does not already provide a defender-side pre-activation-detection split (K4).
5. Targeted search: "black-box pre-activation dormant memory-entry detection via elicitation" one more pass with any new terminology.

> **Answer to the Phase-2A question:** *Yes — but narrowly.* Proactive detection of dormant, semantic-triggered, non-parametric agent-memory poisoning is a **sufficiently unresolved and experimentally tractable research problem to justify Phase 2B — only for the bounded, black-box, behavior-only subclass defined in §14, and only after the five confirmations above.** Verdict: **🟡 research gap with significant caveats.** No solution has been designed.
