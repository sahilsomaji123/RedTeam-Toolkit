# Phase 3C (final) — Intersection Kill-Search & Research-Question Lock

**Project:** AI-Agent Memory Poisoning Research Project · **Gate: CLEARED by user (four PDFs verified).** · **This step: ONE final kill-search of the surviving intersection, then lock the research question. No mechanism/architecture/dataset/code. No novelty claim.**
Date: 2026-08-21.

> **User-verified closures (do NOT re-claim as novel):** broad pre-activation detection → **MEMSAD**; black-box action detection → **Forensic Trajectory Signatures**; dormant retrieval-behavior detection → **Semantic Chameleon / QPD**; post-hoc memory localization → **MemAudit**.
> **Surviving hypothesis (intersection only):** **proactive + pre-trigger + black-box + already-stored persistent agent experience memory + action-level behavioral elicitation + entry/condition localization.**

---

## The ONE question
> *Is proactive behavioral (action-level) elicitation of dormant poison in **persistent agent memory** already demonstrated in any paper **outside the verified four**?*

**Answer: NO located work demonstrates it.** The intersection survives. Two **new adjacents** (not among the four) came close enough that they must be primary-source-verified before Phase 4 — flagged below. (All evidence here is search-level; arXiv remains egress-blocked, so I did **not** read these new adjacents in full and make **no** full-text claim about them.)

---

## Closest occupants found, and why each fails to occupy the cell

| Work | What it is | Why it does NOT occupy the intersection |
|---|---|---|
| **Black-box model trigger reverse-engineering** — B3D ([2103.13127]), AEVA ([2110.14880]), Wang et al. NeurIPS'22, Test-Time ([2112.03350]) | gradient-free, query-only trigger inversion for **model/classifier** backdoors | **Wrong substrate**: weights + label/class space + continuous trigger optimization; not a persistent NL memory store, no action-sequence payload, no entry-in-store localization. Establishes the *technique class* (black-box trigger inversion) but not for agent memory. |
| **The Trigger in the Haystack** ([2602.03085]) | extract/reconstruct **LLM backdoor triggers** via memory-extraction (sleeper agents memorize poison) | Model-weight backdoors (memorized training poison), not an external agent-memory store; no action-elicitation over stored entries. |
| **PI-Hunter** ([2606.12737], user-verified earlier) | proactive red-team of **ingestion paths / IPI** | Audits untrusted **sources it navigates**, not persistent memory **at rest**; flushes live injections, not dormant stored entries. |
| **SafeCommit** ([2608.04289]) — **NEW ADJACENT, unverified** | runtime **certification of when a memory-grounded agent may safely act**; "set-valued, counterfactual" certificate asking "whether any retained world makes the action unsafe," probes valued by uncertified-region shrinkage | **Action-time / reactive to a pending action**, not a proactive store-wide audit that synthesizes triggers to surface dormant entries; certifies a *specific proposed action*, does not hunt/localize the dormant poisoned entry + its activation predicate. **Closest new neighbor — must be read in full before Phase 4.** |
| **AgentSentry** ([2602.22724]) | counterfactual re-execution at tool-return boundaries to expose **indirect prompt injection** | Live IPI mitigation (mediator-channel takeover), not stored dormant-memory elicitation; different threat and timing. |
| **Decision-Aware Memory Cards / CICL** ([2606.08151]) | counterfactual context selection/compression by expected effect on next action | Utility/compression, **not security detection** of poison. |
| **When Agents Talk: Honeytokens under Shared Memory** ([2608.11436]) — **NEW ADJACENT** | deception/honeytokens in shared agent memory; proves a **total-variation impossibility** (a honeytoken can't be harmless to trusted agents yet unrecognizable to a policy-sharing attacker) | About detecting attacker **presence** via decoys, not proactively eliciting **dormant poison** in the store; relevant as a **caution** on canary/honeytoken approaches, not an occupant. |
| **"Proactive Information Elicitation (PIE)"** | an **attack** variant where the planted instruction makes the *agent* elicit sensitive info before acting | **Offensive**, not a defensive auditor. Do not conflate with defensive elicitation. |

**Conclusion:** the `action-elicitation` + `proactive/pre-trigger` + `already-stored persistent agent memory` + `entry/condition localization` conjunction is **unoccupied**. The nearest genuine threats are **SafeCommit** (runtime action-safety certification via counterfactual memory probes) and the **black-box model trigger-inversion** lineage (wrong substrate). Neither occupies it, but **SafeCommit must be verified** because it is the first work to combine counterfactual memory probing with action-safety reasoning.

---

## Embedding-evasion condition — defined operationally (per user instruction; NOT a universal claim)
The adversary is **embedding-evasion-oriented**, but we do **not** claim universal embedding indistinguishability. The condition is empirical and detector-relative:
> A poisoned entry is **embedding-evasive** iff, under a **pre-registered** ⟨embedding model E, distance/metric d, reference corpus C, anomaly test T, operating FPR α⟩, an embedding/retrieval-only detector using T at α separates it from legitimate memory at **AUROC ≤ τ** (τ near 0.5, fixed in advance). Existence and prevalence of such entries are to be **measured** (e.g., against MEMSAD's write-time detector and QPD's retrieval-selectivity signal on MINJA/InjecMEM/MemoryGraft-class poison), not assumed.
This makes the "embedding-preserving" axis a **measurable precondition**, not a universal assumption.

---

## LOCKED research question (single; not a solution)
> **Can a black-box auditor — with no access to the victim agent's embedding function, gradients, or model internals — proactively surface and localize an already-stored, embedding-evasive (per the operational condition above), single dormant memory entry, together with its semantic-context activation predicate, by eliciting its action/tool-use payload *before* the attacker's natural trigger occurs — achieving detection/localization and pre-activation lead-time above the verified baselines (MEMSAD write-time; QPD retrieval-behavioral; Forensic Trajectory Signatures activation-time; MemAudit post-hoc) at bounded false-positive and compute cost — and what is the boundary of the context-predicate space within which this is tractable?**

Framing discipline maintained: this locks **literature gap (#1)** and **technical differentiation (#2)** only. **Research novelty (#3), patent novelty (#4), and inventive step (#5) are NOT claimed.** The differentiator is the **proactive action-level elicitation of dormant stored poison**, which no located work (verified four + this kill-search) performs.

---

## Status & gate to Phase 4
- **Verdict: 🟡 GAP SURVIVES — NARROWED and LOCKED**, with **one residual primary-source check**: read **SafeCommit (2608.04289)** in full (and, secondarily, Trigger-in-the-Haystack 2602.03085 and Honeytokens-under-Shared-Memory 2608.11436) to confirm SafeCommit is action-time certification, not proactive dormant-entry elicitation. *If SafeCommit already elicits/localizes dormant stored poison proactively → collapse to 🟠.*
- **Phase 4 (mechanism design): still NO-GO** — locked RQ only; no detector, algorithm, dataset, or code proposed here.
- **Next action:** supply **SafeCommit 2608.04289** (and the two other new adjacents) as PDFs for the same full-text treatment the four received; then Phase 4 may open **iff** SafeCommit does not occupy the cell.

> No citations were fabricated; the two new adjacents are explicitly unverified. No universal indistinguishability claimed; embedding-evasion is operationalized. No mechanism designed.
