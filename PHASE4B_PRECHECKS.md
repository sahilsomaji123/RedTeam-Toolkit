# Phase 4B — Pre-Checks (two gates)

**Project:** AI-Agent Memory Poisoning Research Project · **Phase 4B: run ONLY the two gates. No detector/algorithm/architecture/probing-strategy/scoring/dataset/code. No novelty/patentability.**
Date: 2026-08-21.

---

## FINAL STATUS: 🟡 EVIDENCE BLOCKED — remain at Phase 4B

Neither gate could be *cleared* in this environment. **Gate 1** requires SafeCommit's full text, which is egress-blocked (no PDF supplied). **Gate 2** requires an actual constructibility experiment (LLM agent + vector memory + MEMSAD/QPD detectors + compute) that this environment cannot run — and executing it would also produce the dataset/code this phase forbids. I therefore return 🟡 and do **not** proceed to Phase 4C. No result was fabricated.

---

## GATE 1 — SafeCommit primary-source verification → **BLOCKED**

**Retrieval attempts (all failed, HTTP 403 / DNS):** arxiv.org, ar5iv, export.arxiv, browse.arxiv (no DNS), huggingface.co, semanticscholar.org, openreview.net, alphaxiv.org, research.google, researchgate.net, aclanthology.org, paperswithcode.com, **core.ac.uk**, **scholar.google.com**. In this environment `WebFetch` cannot retrieve any external paper; only `WebSearch` (snippets) works, which the phase disallows as a basis for the kill test.

**Provisional (search-level, NOT full text — cannot clear the gate):**
Search excerpts describe SafeCommit ([2608.04289], "Certifying When Memory-Grounded Agents May Safely Act") as: "the certificate is **set-valued and counterfactual**: it asks whether **any retained world makes the action unsafe**; probes are valued by how much they **shrink the uncertified region**." On this (unverified) description it reads as **action-time certification of a *pending* action** (Gate-1 answer #8), not proactive dormant-entry elicitation.

**Answers to the 8 questions (provisional, [S] = search-level, unverified):**
| # | Question | Provisional answer [S] |
|---|---|---|
| 1 | inspects already-stored persistent memory? | ~ (reasons over retained memory *for a pending action*) |
| 2 | proactively searches for dormant poisoned memories? | **No indication** |
| 3 | synthesizes contexts/triggers to activate dormant memory? | **No indication** |
| 4 | localizes a malicious memory entry? | No (certifies an action, not entry attribution) |
| 5 | recovers a semantic activation predicate? | No indication |
| 6 | operates before the natural trigger? | It gates a *pending action* (action-time), not a proactive pre-trigger store audit |
| 7 | action-level behavioral elicitation? | **No** (it certifies, does not elicit) |
| 8 | probes uncertainty around a pending action & certifies safety? | **Yes (this is the apparent design)** |

**Kill test (provisional):** SafeCommit does **not** appear to perform the full conjunction (persistent-memory auditing + dormant-trigger elicitation + action-level activation + entry localization + pre-natural-trigger detection). So it **provisionally remains a baseline, not an occupant** — **but this cannot be confirmed without the PDF, so Gate 1 is NOT cleared.** *If full text shows SafeCommit proactively elicits/localizes dormant stored poison → 🟠 COLLAPSE.*

**To clear Gate 1:** supply `2608.04289` as a PDF (or an unblocked environment). I will then answer the 8 questions from the actual method/threat-model text.

---

## GATE 2 — Vacuity / constructibility check → **NOT EXECUTED (cannot run here)**

**Why it cannot be executed in this environment:** the check requires empirically constructing the target attack and testing it against **MEMSAD** and **QPD** at the pre-registered `⟨E,d,C,T,α,τ⟩`. That needs: (a) a running LLM agent with a φ-vector-indexed experience memory; (b) implementations of the MEMSAD (write-time, gradient-coupled) and QPD (retrieval-selectivity) detectors — whose papers are themselves egress-blocked; (c) GPU/model compute. None is available. Running it would also produce the **dataset/implementation code this phase explicitly forbids**. **I will not fabricate a constructibility result.**

**Provisional literature signal (supporting, but NOT a substitute for the pre-registered measurement):**
- **Embedding-evasion is documented for MINJA:** malicious and benign records are "highly entangled in the embedding space, indistinguishable using simple similarity-based filtering; minimal distributional signal for surface-level detection." *(Supports the §8 evasion precondition being satisfiable.)*
- **MEMSAD misses a majority of MINJA:** reported **TPR 0.40 / AUROC 0.914** on MINJA (and TPR 0.20 on InjecMEM); "untriggered attacks naturally mitigated by corpus scale." *(Supports that write-time embedding/gradient detection does not close the class.)*
- **Dormant, context-triggered, action-payload poison is demonstrated:** **Trojan Hippo** — payload "dormant across benign sessions until the user later discusses finance/health/legal/tax/identity topics," executing a **data-exfiltration action sequence**; **MemoryGraft** — trigger-free, benign-doc-induced dormant "successful experiences." *(Supports single-entry + persistent + dormant + semantic-context + action payload being realizable.)*

**Provisional read:** the target attack class appears **plausibly constructible** on published evidence — MINJA-class embedding-evasion × Trojan-Hippo-class dormant action payload — but the **pre-registered constructibility measurement (the actual Gate-2 test) has NOT been run**, so Gate 2 is **not cleared**.

**To clear Gate 2 (protocol, not an artifact):** in an environment with model + compute, instantiate a MINJA/Trojan-Hippo-class single-entry poison carrying an action-sequence payload; verify it (i) activates its payload under a bounded context predicate and stays dormant otherwise, and (ii) satisfies the **pre-registered** embedding-evasion criterion `AUROC(D_emb) ≤ τ` against MEMSAD's write-time signal and QPD's retrieval-selectivity — **with thresholds fixed in advance, not tuned to the result.** Pass ⇒ record properties, proceed. Fail (cannot retain the malicious action payload while evading) ⇒ 🔴 vacuous, STOP.

---

## Determination
> **Does the problem survive both gates?** **Undetermined — evidence blocked.** Neither gate was cleared: Gate 1 needs the SafeCommit PDF (inaccessible here); Gate 2 needs a real constructibility experiment (not runnable here, and forbidden as code/dataset in this phase). Provisional evidence **leans favorable** on both (SafeCommit appears to be action-time certification; the attack class appears constructible per MINJA/Trojan-Hippo/MEMSAD-TPR-0.40), but neither is confirmed.
>
> **Status: 🟡 EVIDENCE BLOCKED.** **Do NOT proceed to Phase 4C.**

**To unblock:**
1. **Gate 1:** provide `SafeCommit 2608.04289` PDF.
2. **Gate 2:** run the pre-registered constructibility test in a model+compute environment (or authorize a compute-enabled session to execute it as its own step). This is an experiment, not part of this specification-only phase.

> Compliance: no detector, algorithm, architecture, probing strategy, scoring function, dataset, or code was produced. No constructibility result was fabricated; the literature signal is explicitly labeled provisional and non-substitutive. No novelty or patentability claimed.
