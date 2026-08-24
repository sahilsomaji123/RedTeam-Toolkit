# AI-Agent Memory Poisoning — Phase 1: Literature, Attack, Defense & Research-Gap Audit

**Project:** AI-Agent Memory Poisoning Research Project · **Phase 1 (gap audit only — no solution proposed).**
Date: 2026-08-21 · Coverage window: 2024–2026 · Method: defense-first, kill-weak-gaps-aggressively.

> **Scope discipline (per task):** This document does **not** design or recommend a solution. It audits the field and identifies **at most 3 genuinely unresolved research gaps**, each with the exact papers that would kill it or a weaker version. Nothing is called novel merely because it was not found — every surviving gap is marked with its residual kill-risk and a confirmation step. Every important claim is cited. arXiv IDs are given; where a full paper could not be opened, the claim is attributed to the abstract/search metadata.

---

## 0. Headline

The field is **large, fast-moving, and already crowded** (30+ directly relevant 2024–2026 papers; ≥5 benchmarks; ≥3 surveys; multiple certified/formal defenses; documented real-world exploits and a CVE). Most "obvious" gaps are **already addressed**. After aggressive filtering, **three** gaps plausibly remain open, ranked below. The strongest (Gap 1) is a *defensive mechanism class* with no located prior art in the agent-memory setting; the other two are *practical-enforceability / verification* gaps that a strong 2026 formal paper and two benchmarks leave partially open.

---

## 1. Threat is real and production-relevant (grounding)

- **Rehberger (2024)** — hand-planted persistent instructions in **ChatGPT long-term memory** via poisoned web content → cross-chat data leakage.
- **EchoLeak — CVE-2025-32711** (Aim Security, Jun 2025) — one hidden-text email made **M365 Copilot** exfiltrate internal data on a later benign query.
- **MINJA** (NeurIPS 2025, [arXiv 2503.03704](https://arxiv.org/abs/2503.03704)) — query-only memory injection; >95% injection, 70% ASR.
- **MemoryGraft** (Dec 2025, [arXiv 2512.16962](https://arxiv.org/pdf/2512.16962)) — plant via benign docs summarized into "successful experience."
- **MemGhost** (Jul 2026, [The Hacker News](https://thehackernews.com/2026/07/new-memghost-attack-plants-persistent.html)) — persistent false memory via one email.
- **"Poison Once, Exploit Forever"** (Apr 2026, [Lyrie](https://lyrie.ai/research/research/poison-once-exploit-forever-ai-agent-memory-poisoning)) — cross-session/cross-site on production **ChatGPT Atlas / Perplexity Comet** browser agents.
- **ElizaOS** — shared-memory manipulation forged admin instructions, hijacked crypto transfers, no privileged access.

This is not a speculative surface; it is being exploited against shipping systems.

---

## 2. Attack Taxonomy

Organized on four orthogonal axes (an attack instance is a point in this space).

### 2A. Injection vector (write channel)
| Vector | Description | Representative work |
|---|---|---|
| **Direct write** | Malicious/insider agent writes false content to shared memory | ASB memory-poisoning scenario ([2410.02644](https://arxiv.org/pdf/2410.02644)); ElizaOS |
| **Indirect / observational** | Agent ingests untrusted external content → stores as trusted memory | MINJA (query-only, [2503.03704]); MemoryGraft ([2512.16962]); MemGhost; EchoLeak; MemVenom (multimodal web, [2606.10742](https://arxiv.org/pdf/2606.10742)); Trojan Hippo ([2605.01970](https://arxiv.org/pdf/2605.01970)) |
| **Reflection / self-generated (laundering)** | Agent's own summarization/echo/corroboration erases untrusted origin | Louck ([2606.24322](https://arxiv.org/abs/2606.24322)) — three laundering channels |
| **Conversational trojan** | Multi-turn conversation implants stealthy trojan | Hijacking Agent Memory ([2605.29960](https://arxiv.org/html/2605.29960v1)) |

### 2B. Persistence / timing
- **Immediate** — poison acts on next retrieval.
- **Sleeper / dormant / gradual-erosion** — behave normally, then activate; "Plant, Persist, Trigger" ([2605.28201](https://arxiv.org/pdf/2605.28201)); Trojan Hippo; "the attack that waits."
- **Trigger-conditioned** — retrieved *only* when a future query is semantically near the trigger; benign at rest (MemPoison L3, [2607.14651](https://arxiv.org/html/2607.14651v1)).

### 2C. Target effect
Response/misinformation steering · **tool-plan / action hijacking** ([2412.10807](https://arxiv.org/pdf/2412.10807)) · **data exfiltration** (Trojan Hippo; EchoLeak; MemLeak [2606.29788](https://arxiv.org/pdf/2606.29788)) · **forged reasoning** ("Your Agent's Memories Are Not Its Own", [2607.05029](https://arxiv.org/pdf/2607.05029)) · financial hijack (ElizaOS).

### 2D. Scope / propagation
Single-session → **cross-session** (persistent profile) → **cross-user** (shared KB) → **cross-agent lateral** (shared memory) → **cross-site** (browser agents). Propagation: lateral / vertical / temporal; "a single input can reach ~1M agents" (multi-agent survey material).

**Unifying lifecycle model** (from surveys [2604.16548](https://arxiv.org/html/2604.16548), [2606.04329](https://arxiv.org/pdf/2606.04329)): poison implanted at **Write** → activated at **Retrieve** → exploited at **Execute** → must be removed at **Forget**. "From Untrusted Input to Trusted Memory" formalizes **4 write channels, 9 structural vulnerabilities, 6 attack classes.**

---

## 3. Defense Taxonomy (by lifecycle stage)

| Stage | Mechanism | Representative work | Guarantee type |
|---|---|---|---|
| **Write** | HMAC provenance signing | SMSR ([2606.12703](https://arxiv.org/abs/2606.12703)) | **Certified** (vs. unsigned injection) |
| **Write** | Non-malleable **origin-binding** (untrusted-origin ⇒ non-actionable, label propagates) | Louck ([2606.24322]) | **Machine-checked** separation theorem |
| **Write** | Input moderation / composite trust score | Memory Poisoning A&D ([2601.05504](https://arxiv.org/abs/2601.05504)) | Heuristic |
| **Store** | Per-user/session isolation, expiry, temporal decay, integrity checks | OWASP five controls; OWASP Agent Memory Guard | Heuristic/policy |
| **Store** | Access-control granularity for shared memory | *named open challenge* (survey 2604.16548) | — |
| **Retrieve** | Randomised ablation + majority vote (smoothed retrieval) | SMSR | **Certified** (bounded authenticated influence) |
| **Retrieve** | Trust-aware / contradiction-aware retrieval | RobustRAG (certifiable), TrustRAG, SeCon-RAG, RevPRAG, ReliabilityRAG | Mixed (RobustRAG certifiable) |
| **Retrieve** | Independent-reasoning-path disagreement | A-MemGuard ([2510.02373](https://arxiv.org/pdf/2510.02373)) | Heuristic (single detector misses 66%) |
| **Execute** | **Trajectory-invariant detection** (e.g., recall-before-send) | Forensic Trajectory Signatures ([2606.30566](https://arxiv.org/abs/2606.30566)) — AUC 0.99; prefix-only 0.934 (near-real-time) | Empirical |
| **Execute** | Gradient-coupled anomaly detection | MEMSAD ([2605.03482](https://arxiv.org/abs/2605.03482)) | Calibration bound |
| **Execute** | Proof-of-execution memory (verify what actually happened) | [2608.16032](https://arxiv.org/html/2608.16032v1) | Verification |
| **Execute** | Activation-based malicious-behavior detection (multi-agent) | [2607.06807](https://arxiv.org/pdf/2607.06807) | Empirical |
| **Forget/Repair** | Post-hoc causal-attribution removal (no poison labels) | MemAudit ([2605.23723](https://arxiv.org/abs/2605.23723)) | Empirical |
| **Forget/Repair** | Dependency-guided rollback over typed memory→action graph | [2608.10502](https://arxiv.org/abs/2608.10502v1) | Empirical (acts; does not certify completeness) |
| **Forget/Repair** | Multi-agent propagation-path intervention + reconstruction | ACM [3806262](https://dl.acm.org/doi/10.1145/3806262.3806294) | Empirical |
| **Cross-cutting** | Bayesian/composite trust; governance | SuperLocalMemory ([2603.02240](https://arxiv.org/pdf/2603.02240)); OWASP | Heuristic |

---

## 4. Benchmark / Evaluation Inventory (why "no benchmark" is NOT a gap)

| Benchmark | Focus | Scale | Cite |
|---|---|---|---|
| **ASB** (ICLR 2025) | DPI/IPI/**memory poisoning**/PoT-backdoor across 10 scenarios, 400+ tools | 10 agents | [2410.02644](https://arxiv.org/pdf/2410.02644) |
| **MemPoison-Bench** | 4 attack vectors, hand-validated | 1,227 cases | (via [2606.04329]) |
| **MemSecBench** | Lifecycle **Write–Execute–Forget**, persistence→consequence→repair | 310 cases / 48 contexts | [2607.27080](https://arxiv.org/html/2607.27080v1) |
| **AgentLAB** | Long-horizon attacks incl. memory | — | [2602.16901](https://arxiv.org/pdf/2602.16901) |
| **"Ground Truth First"** | **Longitudinal** memory-eval instrument | — | [2607.21962](https://arxiv.org/html/2607.21962) |
| **Anatomy of Agentic Memory** | Taxonomy + eval/system-limitation analysis | — | [2602.19320](https://arxiv.org/pdf/2602.19320) |

**Surveys:** Long-Term Memory Security lifecycle survey ([2604.16548]); "From Untrusted Input to Trusted Memory" ([2606.04329]); Agentic Security survey ([2510.06445](https://arxiv.org/pdf/2510.06445)); Layered Attack-Surface survey ([2604.23338](https://arxiv.org/pdf/2604.23338)).

---

## 5. Killed-Gaps Ledger (aggressive rejection — record of what closes each weak gap)

| Candidate "gap" | Why it looked open | **Killer prior art** | Verdict |
|---|---|---|---|
| Cryptographic provenance / signed memory writes | provenance felt under-used | **SMSR** HMAC + certified bound ([2606.12703]) | 🔴 addressed |
| Trust-scoring / lineage-based memory authority | intuitive defense | **Louck** proves content **and** lineage are malleable ([2606.24322]) | 🔴 proven inadequate |
| Detect poison via retrieval/anomaly pattern | "same doc across unrelated queries" | Stated as known indicator; MEMSAD; A-MemGuard | 🔴 addressed |
| Activation-time detection of active poisoning | attacks manifest in behavior | **Forensic Trajectory Signatures** AUC 0.99, near-real-time ([2606.30566]) | 🔴 addressed |
| Post-hoc auditing / attribution of poison | need to find planted entries | **MemAudit** causal attribution ([2605.23723]) | 🔴 addressed |
| Repair / rollback of poisoned memory | remove after detection | **Dependency-Guided Rollback** ([2608.10502]); multi-agent repair (ACM) | 🔴 addressed |
| Benchmarks / datasets / longitudinal metrics | eval seemed immature | ASB, MemPoison-Bench, **MemSecBench**, AgentLAB, Ground Truth First | 🔴 addressed |
| Certified defense (unsigned / bounded adversary) | formal guarantees rare | **SMSR** certified bound; RobustRAG certifiable | 🔴 addressed |
| Sleeper/backdoor detection (model) | dormant triggers | Anthropic probes; Microsoft scanner; SAE ([2605.07324]) — but **weight-space only** | 🔴 addressed for weights (≠ memory) |
| Machine-unlearning verification | "did it forget?" | Auditing Unlearning ([2606.16110]); TAPE; MIAU — but **weight-centric** | 🔴 addressed for weights (≠ non-parametric memory) |
| Multi-agent propagation modeling | "under-studied" | SuperLocalMemory; propagation-path intervention; ElizaOS study | 🟠 substantially studied |
| Cross-representation residual *measurement* | poison reappears after cleanup | **MemSecBench** Forget protocol; **MemLeak** cross-representation residual ([2606.29788]) | 🟠 measured (see Gap 3) |

---

## 6. The Three Surviving Gaps (ranked)

Ranking criteria (each 1–5): **Novelty** (distance from located prior art), **Feasibility** (buildable now), **Measurability** (clean experimental metric), **Publication potential**.

### 🥇 Gap 1 — Proactive **trigger-elicitation auditing** of dormant agent memory (defensive trigger reverse-engineering for a *non-parametric* memory store)
- **Statement.** Detecting a **benign-until-activated, trigger-conditioned** poisoned memory *entry* **before** the attacker's trigger arrives is explicitly unsolved: "a poisoned memory is benign until it activates, so there is nothing to detect at write or rest time" (MemPoison [2607.14651]). Existing detection is either **reactive/activation-time** (trajectory: Forensic Trajectory Signatures fires only once the harmful action begins) or **post-hoc** (MemAudit, after harm). The obvious defensive analogue from model security — **trigger reverse-engineering (Neural Cleanse, GangSweep, Wang et al. NeurIPS'22)** — operates on **model weights / a continuous perturbation space / a classifier label space** and *does not transfer* to a discrete natural-language memory store where the "trigger" is a **semantic query** and the "target" is a **harmful agentic action sequence**. **No located work performs defensive synthesis of candidate triggers to force suspicious memory entries to reveal harmful downstream behavior pre-attack.**
- **Why not killed:** Neural-Cleanse family ([2404.12852], GangSweep, Poison Forensics USENIX'22) = weights/classifier; Forensic Trajectory Signatures = activation-time/reactive; MemAudit = post-hoc; A-MemGuard/MEMSAD = reasoning-consistency/gradient at retrieve/execute, not trigger-search over the store.
- **Residual kill-risk:** the trigger space is large/semantic → a *general* solution may be fundamentally hard (analogous to trojan-trigger-search hardness). **Must scope to a measurable subclass** (e.g., entries whose activation is narrowly query-conditioned) and report the detectable/undetectable boundary. **Confirm** against MemPoison's structural blind-spots and any 2026 "proactive memory red-teaming" work before claiming full novelty.
- **Measurability:** pre-activation detection rate of *planted* dormant poison (from MINJA/MemoryGraft/MemSecBench) vs. trigger-search budget; FPR on benign memory; detection lead-time before the attacker's trigger. **Scores:** Novelty 5 · Feasibility 4 · Measurability 5 · Publication 5.

### 🥈 Gap 2 — Enforceability & **security–utility frontier** of non-malleable origin-binding under *semantic* laundering (memory **richness vs. hygiene** tension)
- **Statement.** Louck ([2606.24322]) proves content **and** lineage signals are malleable and proposes **non-malleable origin-binding** with a machine-checked separation theorem — but the guarantee assumes a **trusted monitor** that can record an item's *true origin* such that no transformation lowers its untrusted label. The three laundering channels (agent **summarization**, **trusted-tool echo**, **manufactured corroboration**) are **semantic** transformations: a *syntactic* taint monitor either **over-taints** (every summary of untrusted input becomes non-actionable → destroys memory utility) or **under-taints** (misses laundering); a *semantic* monitor is itself an LLM (malleable). The survey names this exact **"fundamental tension between memory richness and memory hygiene"** as open. **No located work quantifies the achievable security-vs-utility frontier of origin-binding under semantic derivation, nor gives a semantic-derivation-aware enforcement that is not itself a malleable oracle.**
- **Why not killed:** 2606.24322 is a **formal** result (machine-checked model), not a deployed system with a measured frontier; it establishes the property, not its practical enforceability under semantic derivation. Classic IFC over-tainting is the known failure mode this gap must quantify, not repeat.
- **Residual kill-risk:** 2606.24322 owns the framing → must position strictly as the *practical-enforcement + frontier-quantification* gap it leaves open (risk of being seen as incremental). **Confirm** whether any 2026 follow-up already measures the frontier.
- **Measurability:** laundering-attack-success vs. legitimate-memory-utility (task success retained) as a curve over taint-propagation granularity, across the three laundering channels. **Scores:** Novelty 4 · Feasibility 4 · Measurability 5 · Publication 4.

### 🥉 Gap 3 — **Verifiable completeness** of poison removal across heterogeneous, semantically-derived memory representations (a residual-reactivation *certificate*, not just measurement)
- **Statement.** A single poison leaves derivatives across raw logs, summarized memory cards, vector indexes, **reflected lessons**, shared stores, and audit records; "contamination can reappear after apparent cleanup." Repair *acts* (Dependency-Guided Rollback [2608.10502] deactivates traceable dependents; MemAudit removes attributed entries), and residuals are now *measured* (MemSecBench Forget protocol; MemLeak cross-representation residual [2606.29788]). **What is not provided is a *verification oracle / completeness certificate*** that the poison's *semantic influence* is gone from **all** derivation channels — including agent-generated abstractions that no longer textually resemble the original — where **weight-centric unlearning verification (2606.16110, TAPE, MIAU) does not transfer** to non-parametric semantic derivations.
- **Why partially open:** measurement exists (MemSecBench/MemLeak), action exists (rollback/MemAudit), but a **guarantee/oracle of completeness** across semantic derivations is absent.
- **Residual kill-risk:** **weakest of the three** — MemSecBench + MemLeak + the machine-unlearning-verification field crowd it; novelty is "guarantee vs. measurement." **Confirm** MemSecBench's Forget metrics don't already constitute an accepted completeness measure.
- **Measurability:** post-repair **reactivation rate** of the original attack via *any* derivation path, and false-forget (benign memory lost). **Scores:** Novelty 3 · Feasibility 5 · Measurability 5 · Publication 3.

---

## 7. Research-Gap Map (one view)

```
WRITE  ──sign/origin-bind──► SMSR / Louck ............ CLOSED (crypto/formal)
        └─ semantic laundering enforceability ........ ★ GAP 2 (open: richness↔hygiene frontier)
STORE  ── isolation/access-control granularity ....... 🟠 named-open (multi-agent)
RETRIEVE ── trust/smoothed/robust retrieval .......... CLOSED-ish (SMSR/RobustRAG/A-MemGuard)
        └─ dormant entry at rest, pre-trigger ........ ★ GAP 1 (open: proactive trigger-elicitation)
EXECUTE ── trajectory/gradient/PoE detection ......... CLOSED (Forensic Trajectory Sigs AUC .99)
FORGET  ── rollback/attribution repair ............... CLOSED (act) 
        └─ completeness verification across derivs ... ★ GAP 3 (open: certificate vs. measurement)
```

---

## 8. Phase-1 Conclusion (no solution proposed)

The audit confirms a **saturated, high-velocity field** in which cryptographic provenance, activation-time detection, repair/rollback, benchmarks, and certified defenses against unsigned/bounded adversaries are **already addressed**. Three gaps survive aggressive filtering, ranked **Gap 1 (proactive trigger-elicitation auditing of dormant memory) > Gap 2 (origin-binding enforceability / richness–hygiene frontier under semantic laundering) > Gap 3 (verifiable removal-completeness across semantic derivations)**. Gap 1 has the greatest distance from located prior art and the cleanest experimental design; Gap 3 is the most at-risk of being subsumed by MemSecBench/MemLeak.

**Mandatory before Phase 2 (per project rules — do NOT start solution design until done):**
1. **Confirm Gap 1's novelty** with a dedicated search for "proactive/defensive trigger synthesis or memory red-teaming over agent memory stores" and full-text reads of MemPoison ([2607.14651]) and Forensic Trajectory Signatures ([2606.30566]).
2. **Confirm Gap 2** is not already quantified in a 2606.24322 follow-up.
3. **Confirm Gap 3** is not already an accepted MemSecBench Forget metric.
4. **Full-text** (not snippet) reads of the top ~12 cited papers; verify dates/venues; note that patent-side prior art was **not** searched here (out of scope for a research gap audit; would be required only if a patent path is later chosen).

> Nothing above is asserted as novel with certainty; each surviving gap carries an explicit residual kill-risk and a confirmation step. No solution has been designed, per the Phase-1 mandate.
