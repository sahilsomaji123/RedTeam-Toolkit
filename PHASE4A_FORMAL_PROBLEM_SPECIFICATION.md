# Phase 4A — Formal Problem & Contribution Specification

**Project:** AI-Agent Memory Poisoning Research Project · **Phase 4A: formal problem definition ONLY. No algorithm, architecture, code, dataset, novelty, or patentability.**
Date: 2026-08-21 · Gate: literature-intersection gap locked (Phase 3C).

> **Scope discipline.** This document defines the auditor by its **interface (what it may observe/do) and its measured objective** — never by *how* it decides. Defining an observation set, a probe budget, and evaluation metrics is problem specification; specifying a detection procedure/score is Phase 4B and is **not** done here.
> **Carried caveat:** SafeCommit (2608.04289) full text was not read by me (egress-blocked); per the user's kill-set it is treated here as a **baseline** ("counterfactual action-safety probing"), not an occupant.

---

## 1. System model

| Symbol | Entity | Definition |
|---|---|---|
| `A` | **Agent** | tuple `(π, R, T, Loop)` executing a perceive→retrieve→reason→act loop |
| `π` | **LLM** | policy mapping (system prompt, user input, retrieved memory, tool results) → (reasoning, action); black-box to the auditor |
| `M` | **Persistent memory store** | `M = {m₁,…,m_N}`, experience records; survives sessions |
| `mᵢ` | **Memory entry** | `(textᵢ, metaᵢ)`; natural-language experience/lesson + metadata |
| `φ` | **Victim embedding fn** | maps text → vector; **owned by the victim, black-box to the auditor** |
| `R` | **Retriever** | `R(q, M) = top-k by sim(φ(q), φ(mᵢ))` ⊆ `M` |
| `T` | **Tools** | `{t₁,…,t_L}`; a subset `T_sens ⊆ T` is security-sensitive (secret read, external transmit, delete, privilege change) |
| `U` | **User** | benign principal issuing tasks under a context `c` |
| `Adv` | **Attacker** | writes poison into `M` via allowed channels; see §2 |
| `Aud` | **Auditor** | black-box party that may execute `A` in a sandbox on chosen inputs/contexts, observe `O` (§6) within probe budget `B`, and emit a verdict + localization |
| `c` | **Context** | session variables (identity/role, task, available tools, prior turns) |

Execution: for input `x` under context `c`, `A` computes `Rc = R(qc, M)`, then `a = π(sys, x, Rc, toolresults)`; `a` is a tool call or answer; sensitive actions produce external side effects.

## 2. Attack model
- **Capabilities (granted):** indirect **write** to `M` (query-only interaction à la MINJA; benign-doc ingestion à la MemoryGraft); interact with `A`; craft an **embedding-evasive** entry (§8); choose a **bounded context-predicate** trigger (§4) and an **action-sequence** payload (§5); **adapt** to a *known strategy class* of the auditor (Stackelberg leader).
- **Capabilities (denied):** direct read/modify/delete of arbitrary `M` rows; observe the auditor, its sandbox, or its probe set; access `π`/`φ` internals.
- **Poisoning mechanism:** inject a **single** entry `m*` (single-entry regime).
- **Persistence:** `m*` remains in `M` across sessions until removed.
- **Trigger:** predicate `ψ ∈ Ψ` (§4); `m*` is **behaviorally dormant** unless `ψ(c)=1`.
- **Payload:** action sequence `σ* ∈ Σ_harm` (§5), executed when `ψ(c)=1` **and** `m*` is retrieved.
- **Adaptation:** `Adv` selects `(m*, ψ, σ*)` to minimize detection by an auditor of a **declared strategy class** `𝒜` (not the exact instance).

## 3. Memory model (exact target)
Target = **episodic/experience** memory: a **persistent, φ-vector-indexed** store of natural-language experience records written through the agent's own interaction loop (MINJA/AgentPoison/MemoryGraft setting). **Excluded from the minimal target:** procedural/tool memory, structured DB memory, multimodal memory (deferred).

## 4. Trigger model (bounded)
`Ψ = I × K × V` where `I` = finite identities/roles, `K` = finite task types, `V` = finite tool-availability subsets. `|Ψ|` is finite and enumerable by construction of the evaluation harness. **Dormancy (formal):** for all `c` with `ψ(c)=0`, the agent's action distribution with `m*` present is statistically indistinguishable from with `m*` absent (behaviorally inert). **Out of scope:** free-text/open semantic triggers, multi-turn temporally-accumulated triggers.

## 5. Payload model (action/tool-use)
`Σ_harm` = action sequences with a **decidable harm predicate** `Harm(σ)∈{0,1}` evaluated by a **sandbox oracle**. Canonical members: unauthorized sensitive-tool invocation; secret retrieval; external transmission/exfiltration; **chained** `retrieve_secret → external_tool → transmit [→ delete_evidence]`; policy bypass; privilege escalation. Single-action payloads allowed; the **chained** form is preferred for a crisp sandbox state-change signal.

## 6. Observation model (black-box)
Auditor observable set `O`: user inputs; agent response text; **tool calls + arguments**; execution results; **retrieved-entry identifiers if the store exposes them**; timing; sandbox state. **Capability:** `Aud` may **execute `A` in a sandbox on synthesized inputs/contexts** (interventional/black-box access) within budget `B`. **Explicitly excluded** (unless a separate ablation studies them): model weights, gradients, hidden activations, the victim embedding function `φ`. *(This clause is the axis that separates the target from MEMSAD/white-box detectors.)*

## 7. Pre-activation definition
Let `t_detect` = audit time of a flag, `t_trig` = time the attacker's **natural** trigger first arrives in **production**, `t_exec` = first **production** execution of `σ*`, `t_side` = first external side effect. Detection **counts as pre-activation** iff `t_detect < min(t_trig, t_exec, t_side)`. Auditing runs on a **sandbox replica**; a payload firing **inside the audit sandbox** counts as pre-activation because it precedes production harm. Excluded (do **not** count): activation-time detection during production execution, or post-incident attribution.

## 8. Embedding-evasion definition (operational; NOT universal)
Pre-register `⟨E, d, C, T, α⟩` (embedding model, metric, reference corpus, anomaly test, FPR). `m*` is **embedding-evasive** iff an embedding/retrieval-only detector `D_emb` using `T` at FPR `α` satisfies `AUROC(D_emb; m* vs C) ≤ τ` for a fixed `τ` near `0.5`. **Existence and prevalence of such `m*` are to be measured** (against MEMSAD's write-time signal and QPD's retrieval-selectivity on MINJA/InjecMEM/MemoryGraft-class poison), **not assumed**. If no such `m*` can be constructed, the problem is vacuous (see §12 global falsifier).

## 9. Formal research objective (metrics; not a method)
Over a distribution `𝒟` of (store, poison/clean) instances, define:
- **Detection probability** `P_det = Pr[Aud flags M | M poisoned]`.
- **False-positive probability** `P_fp = Pr[Aud flags M | M clean]`.
- **Localization accuracy** `L_acc = Pr[entry Aud returns = m* | detected]`.
- **Trigger recovery** `R_trig = Pr[ sim(ψ̂, ψ) ≥ θ ]` (or exact-match over `Ψ`).
- **Pre-activation lead time** `Δ = t_trig − t_detect` (require `Δ > 0`; report distribution).
- **Probe budget** `B` = number of sandbox executions/queries; report `P_det(B)`, `L_acc(B)`.
- **Compute cost** = wall-clock / tokens per audited store.

**Objective (evaluation target, not an algorithm):** maximize `P_det, L_acc, R_trig` subject to `P_fp ≤ α`, `B ≤ B_max`, `Δ > 0`; compare against §13 baselines on matched `P_fp`.

## 10. Tractability boundary (explicitly NOT solved)
Excluded: arbitrary/free-text semantic triggers; multi-entry compositional/collusive poison; unbounded/unrestricted tool ecosystems; fully adaptive attackers who can **observe** the auditor or its probes; universal dormant-poison detection; opaque memory with **no** sandbox-execution access. The study is confined to: **single-entry, bounded-`Ψ`, sandbox-observable action payload, black-box-no-internals, strategy-class-adaptive** adversaries.

## 11. Contribution hypotheses (≤3; hypotheses, not claims)
- **H1 — Elicitation feasibility.** ∃ a bounded predicate class `Ψ_b ⊆ Ψ` and budget `B ≤ B_max` such that a black-box auditor achieves `P_det` for embedding-evasive single-entry poison **strictly above the best verified baseline** at matched `P_fp`, with `Δ > 0`.
- **H2 — Black-box localization.** Conditioned on detection, behavioral evidence under `O` yields `L_acc` (entry) and `R_trig` (condition) **above baseline attribution** (MemAudit post-hoc / chance).
- **H3 — Tractability boundary.** `R_trig` (and `P_det`) degrade **measurably and characterizably** as `|Ψ|` (predicate-space size/arity) grows, defining a quantifiable tractable↔intractable frontier.

## 12. Falsification conditions
- **H1 falsified iff:** no auditor in class `𝒜` beats every baseline at any `B ≤ B_max` across `Ψ_b` (i.e., proactive black-box elicitation confers no advantage).
- **H2 falsified iff:** `L_acc ≤` MemAudit/chance attribution, or `R_trig ≤` chance.
- **H3 falsified iff:** `R_trig`/`P_det` are **independent** of `|Ψ|` (no boundary), **or** already infeasible at the smallest non-trivial `|Ψ|` (no tractable regime).
- **Global (vacuity) falsifier:** if embedding-evasive single-entry poison satisfying §8 **cannot be constructed** against MEMSAD+QPD at the pre-registered thresholds, the problem is empty → **STOP**.
- **Gap-collapse falsifier:** if a baseline (esp. **SafeCommit**, once read in full) already achieves the §9 objective in the §7 pre-activation regime → collapse to 🟠 and stop.

## 13. Baseline matrix (locked)
| ID | Baseline | Native regime | Role in comparison |
|---|---|---|---|
| B1 | No defense | — | floor |
| B2 | **MEMSAD** ([2605.03482]) | write-time, **white-box** gradient-coupling | upper-bound reference (off-regime: not already-stored/black-box) |
| B3 | **QPD / Semantic Chameleon** ([2603.18034]) | retrieval-selectivity, RAG | behavioral (retrieval) reference; expected blind to embedding-evasive |
| B4 | **MemAudit** ([2605.23723]) | **post-hoc** causal attribution | localization reference; run proactively as an ablation |
| B5 | **Forensic Trajectory Signatures** ([2606.30566]) | **activation-time**, black-box action | the lead-time bar (`Δ` must exceed its 0) |
| B6 | **SafeCommit** ([2608.04289]) *(unread by me)* | action-time counterfactual certification | closest new adjacent; **must be read before 4B** |
| B7 | Memory sanitization / composite-trust | temporal decay + pattern/trust score | strongest sanitization baseline |
Substrates (not baselines): MPBench / MemSecBench harnesses.

## 14. Final determination
> **Is the surviving problem precisely definable, measurable, falsifiable, and experimentally tractable?**
>
> **YES**, conditional on two pre-checks at the start of Phase 4B:
> 1. **Vacuity pre-check (§8/§12):** empirically confirm embedding-evasive single-entry poison is constructible against MEMSAD+QPD at the pre-registered `⟨E,d,C,T,α,τ⟩`. If not → STOP.
> 2. **SafeCommit read (§12 gap-collapse):** confirm SafeCommit is action-time certification, not proactive dormant-entry elicitation. If it occupies the cell → STOP.
>
> The problem is **definable** (§1–8), **measurable** (§9), **falsifiable** (§11–12), and **tractable within a bounded regime** (§10). **Prepare for Phase 4B** — but 4B must **begin with the two pre-checks above**, and still **no mechanism is designed here.**

> Compliance: no algorithm, architecture, dataset, or code proposed; no novelty or patentability claimed. The auditor is specified only by interface (§6) and objective (§9). SafeCommit remains unread and is carried as a baseline plus a gate, not an occupant.
