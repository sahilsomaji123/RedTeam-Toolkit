# Patent-Hunt Master Report — AI × Cybersecurity × Cyber-Forensics

**Authoritative consolidation of a six-round, defense-first patent-discovery investigation.**
Date: 2026-08-21 · Branch: `claude/patentable-ai-cybersecurity-ideas-yjw3mi` · Repos: `cyber-security-toolkit`, `RedTeam-Toolkit`.

This report supersedes nothing — the six round reports remain the primary record — but it is the single place to start. It consolidates findings, prevents rediscovery of dead ends, and defines a clean checkpoint.

---

## 3. Executive Summary

### Final result: **NO DEFENSIBLE PATENT CANDIDATE IDENTIFIED**

This does **not** mean no patentable invention exists in this space. It means precisely:

> No candidate investigated during the six-round defense-first process currently has sufficient evidence of **novelty + inventive step + technical feasibility** to justify substantial development or a patent filing.

Every concrete candidate generated (≈30+ distinct concepts across six rounds) was eliminated by **named non-patent prior art** (peer-reviewed papers, standards, and shipping products), an **obvious-combination** argument, or a **feasibility** failure. The investigation repeatedly converged on one structural reason (see §10): in AI-security-and-forensics, the *problem space is new but the solution primitives are old*, so almost every proposed mechanism reads as a known primitive applied to a new object — the textbook shape of an obviousness rejection.

**Two hard constraints on the strength of these conclusions:**
1. **Patent full-text was never verifiable in the research environment** — every patent database (Google Patents, USPTO/PPUBS, Espacenet, WIPO PATENTSCOPE, Lens, Justia, FreePatentsOnline) and even arXiv/Crossref direct-fetch returned HTTP 403 under the session egress policy. All patent references are therefore `UNVERIFIED — FULL TEXT NOT AVAILABLE`. The load-bearing evidence is non-patent prior art (which needs no patent access). See §12.
2. **No (un)patentability determination is made with certainty.** Everything is a novelty/obviousness **hypothesis requiring professional patent examination.**

---

## 4. Research Trajectory

| Round | Strategy | Candidates | Result |
|---|---|---|---|
| 1 | Broad AI/Cyber/DFIR landscape + prior-art + market/gap analysis | ~24 initial → top 8 → top 3 | 3 leading candidates proposed |
| 2 | Adversarial re-verification of the top 3 | 3 | **All 3 eliminated** (anticipated / obvious) |
| 3 | Narrowing to the ZK-provenance hypothesis (+ minimality proof) | 1 (+ sub-variants) | **Likely obvious**; only novel variant (ZK cardinality-minimality) is **infeasible** (co-NP) |
| 4 | Four fresh white spaces (agent evidence, fabricated telemetry, PQ evidence graphs, TEE-rooted provenance) | ~30 (27 killed on sight) | One 🟡 survivor: candidate #13 (omission-bounding) |
| 5 | Final kill test of candidate #13 | 1 | **NO-GO** — anticipated by GhostBuster + CSS-A/watchdog + PeerReview |
| 6 | Emerging-capability lens (2023–2026 shift → new failure modes) | ~24 problems, 5 mechanisms deep-tested | **No defensible candidate** — solved/obvious/infeasible |

**Cumulative:** ~30+ distinct concepts eliminated; 0 survived to a clean defensible-patent status.

---

## 5. Complete Dead-End Map

Definitive table of eliminated concepts. **Purpose: prevent future rediscovery under new terminology.** Patent references are `UNVERIFIED` (search-metadata only); paper/product references are verified as existing via search.

### Family A — Evidence / provenance
| Concept | Why it looked promising | Killer prior art | Failure mode | Round |
|---|---|---|---|---|
| Verdict Witness (deterministically-replayable PIDS verdict) | court-grade reproducible detection evidence | Vigilante Self-Certifying Alerts (2005); ProvX (minimal subgraph); "VERDICT" agentic-DFIR product | Obvious combination | 1–2 |
| Cross-Source Verifiable Evidence Graph (per-edge proofs) | admissible auto-correlation across tools | CASE/UCO ontologies; Forensic-Chain blockchain CoC | Obvious combination | 1 |
| Sensor-physics capture attestation (multi-channel) | beyond-C2PA authenticity | C2PA hw signing; PRNU; IMU/rolling-shutter fusion | Obvious combination | 1 |
| Anti-forensic destruction-signature watermark | classify attack from watermark destruction manifold | fragile watermarking + ML manipulation-type classifier (Nature SciRep 2025) | Obvious | 1, 4 |

### Family B — ZK / cryptographic verification
| Concept | Why it looked promising | Killer prior art | Failure mode | Round |
|---|---|---|---|---|
| ZK-provenance verdict (privacy + verifiability) | verify a detection without revealing graph/model | zkML (EuroSys'24); ZKGraph; DARPA SIEVE; P3GNN; abductive AXp | Obvious combination | 3 |
| ZK proof of witness **subset**-minimality | provably minimal evidence in ZK | abductive explanations + zkML repeated | Obvious | 3 |
| ZK proof of witness **cardinality**-minimality | genuinely under-explored | (none found) — but co-NP / ∀-quantified | **Infeasible** with current SNARKs | 3 |
| Cross-vantage cryptographic **omission-bounding** (#13) | prove a lower bound on suppressed events | **GhostBuster** (cross-view, 2005) + **CSS-A/watchdog** (count-reconciliation under benign-loss) + **PeerReview** (omission-fault + evidence) | Anticipated / obvious | 4–5 |

### Family C — AI / LLM DFIR
| Concept | Why it looked promising | Killer prior art | Failure mode | Round |
|---|---|---|---|---|
| Oracle-Gated DFIR (per-claim gate + coverage cert) | eliminate LLM forensic hallucination | EG-VAR (tool-attested verified claims); LLM-Provenance-Forensics; FinGround/DEER (atomic-claim coverage); Trust Certificate | Obvious combination | 1–2 |
| AI-generated forensic timeline w/ confidence + replay | trustworthy auto-timeline | DFIR-Chain timelines | Thin over prior art | 1 |

### Family D — Agent security
| Concept | Why it looked promising | Killer prior art | Failure mode | Round |
|---|---|---|---|---|
| Prompt-Injection Forensic Reconstructor | counterfactual span attribution of injection | **AgentSentry** (counterfactual re-exec at tool-return boundaries); Causal Agent Replay; delta debugging | Single-ref near-anticipation | 1–2 |
| AI-agent evidence provenance / receipts | new agent-accountability need | AgentBound; RATS-agent-evidence (2608.00801); IETF SCITT Agent Action Capsule | Being standardized | 4 |
| Cross-agent covert-collusion detector | detect steganographic coordination | Audit the Whisper; NARCBench; Steganalysis 2608.02698; **undetectable-stego proofs** (2606.28425) | Worked + partly impossible | 6 |
| Constraint-drift / authority enforcement | named 2026 open problem | PCAS (Datalog reference monitor); SafeFlow (semantic IFC); DRIFT; Authorization Propagation | IFC + reference monitor already applied | 6 |
| Effective-permission reconstruction / attribution | NHI attribution gap | CSA/GitGuardian NHI parentage records; SCITT/AgentBound; event sourcing | Mature primitive + standardizing | 6 |

### Family E — Telemetry integrity
| Concept | Why it looked promising | Killer prior art | Failure mode | Round |
|---|---|---|---|---|
| Deterministic verifier for AI-SOC dispositions | non-circular verification of auto-close | SOCpilot (policy compliance verifier) | Obvious combination | 1 |
| Fabricated/synthetic-log detector (consistency/classifier) | detect forged telemetry | EvidenceForge / MS causal generators (defeat cross-source consistency) | Defeated / classifier | 4 |
| Telemetry microtiming fingerprint (real vs synthetic) | "PRNU for telemetry" | IET/temporal-autocorr real-vs-synthetic (fraud/Tor) | Classifier; adversarially learnable | 4 |
| TEE-signed suppression-evident syscall counter | trust at generation | US12524535 TEFTI; FssAgg; PillarBox gap-checker | Anticipated | 4 |

### Family F — TEE / hardware security
| Concept | Why it looked promising | Killer prior art | Failure mode | Round |
|---|---|---|---|---|
| Syscall-time TEE-rooted provenance | authentic-at-generation logging | Custos; Nitro (CCS'25, fine-grained); EmLog; HardLog; VMI patents | Mature field | 4 |
| Portable pre-action agent authorization proof | verifiable agent authz | Proof-of-Guardrail; VET; CVA | Anticipated | 1 |
| Generic "tamper-evident AI decision ledger" | signed replayable decisions | AuditableLLM; AuditWeave; Proof-of-Execution | Crowded / anticipated | 1–2 |

### Family G — Post-quantum evidence
| Concept | Why it looked promising | Killer prior art | Failure mode | Round |
|---|---|---|---|---|
| PQ forensic-graph time-sealing | graph-state historical provability | PQ audit-evidence (2512.00110); PAdES; accumulators | Obvious / dependent-claim | 1, 4 |
| Dependency-aware selective re-signing of evidence DAGs | cheap PQ migration of DAGs | 2512.00110 (names DAG as future work); hybrid sigs; skip-lists | Obvious combination | 4 |

### Family H — Multi-agent security
| Concept | Why it looked promising | Killer prior art | Failure mode | Round |
|---|---|---|---|---|
| Consistent security snapshot of ephemeral state | "no stable state" feels new | **Chandy-Lamport (1985)**, already used for multi-agent sync | 40-year-old primitive | 6 |
| Individually-safe→collectively-unsafe composition guard | genuine emergent-safety gap | Open Challenges in Multi-Agent Security (2505.02077); constraint-drift taxonomy | Live research, no defensible mechanism | 6 |

### Family I — AI-generated artifacts
| Concept | Why it looked promising | Killer prior art | Failure mode | Round |
|---|---|---|---|---|
| Slopsquatting / hallucinated-package gate | fresh 2025–26 supply-chain vector | Shipping CLI defenses (Claude Code/Codex/Cursor); allowlist/hash | Mature commercial solution | 6 |
| Non-deterministic AI-code reproducibility for forensics | can't reproduce vulnerable artifact | generation-context logging = agent provenance (Rd4); temporal DBs | Obvious / crowded | 6 |

---

## 6. Prior-Art Pattern Analysis

Eight recurring reasons candidates failed. Each is a standing obviousness trap.

- **Pattern 1 — Known primitive + new application.** e.g., deterministic replay (Vigilante) → PIDS verdicts. New object, old mechanism.
- **Pattern 2 — Known cryptography + cybersecurity.** e.g., PQ signatures/Merkle → evidence graphs. The crypto is standardized; the application is routine.
- **Pattern 3 — Known provenance + AI.** e.g., provenance/attestation → agent actions. Provenance is a mature discipline (CASE/UCO, SCITT).
- **Pattern 4 — Known TEE + telemetry.** e.g., TEE/attested logging → syscall provenance (Custos/EmLog/Nitro/TEFTI).
- **Pattern 5 — Known ZK + security.** e.g., zkML/ZKGraph/DARPA-SIEVE → verify a detection privately.
- **Pattern 6 — Known IFC / reference monitor + agents.** e.g., PCAS/SafeFlow → constraint-drift enforcement.
- **Pattern 7 — Known distributed-systems technique + agentic systems.** e.g., Chandy-Lamport snapshots, PeerReview omission-fault detection, event sourcing.
- **Pattern 8 — Emerging problem but mature underlying primitive.** The whole Round-6 dynamic: new failure mode, decades-old fix.

**Why these create obviousness risk:** under a KSR-style analysis, combining known elements according to their established functions to yield predictable results is *prima facie* obvious. When the "invention" is (mature primitive) applied to (new but analogous object) with a reasonable expectation of success, an examiner has a ready §103 rejection — and in this field the primitives are unusually deep and well-documented, so the rejection is almost always available.

---

## 7. Technology Red-Zone Map

**Do not re-search these without a genuinely new primitive** (see §11). Re-entering any of these under new terminology will reproduce a dead end:

- AI-generated forensic evidence provenance · AI-agent provenance / agent audit logs / receipts
- ZK + IDS · ZK + provenance · privacy-preserving security verdicts · ZK proof of detection
- telemetry reconciliation · trusted telemetry · telemetry omission/completeness detection · TEE telemetry
- post-quantum evidence graphs / selective re-signing
- AI forensic reporting · oracle-gated DFIR · prompt-injection forensic reconstruction
- deterministic/replayable/attested security verdicts · tamper-evident AI decision ledgers
- generic AI cybersecurity · generic AI anomaly/threat detection · blockchain + forensic evidence
- generic multi-agent authorization · generic multi-agent state consistency · generic slopsquatting prevention
- cross-agent covert-collusion detection · constraint-drift enforcement · ephemeral-identity reconstruction
- consistent security snapshot of ephemeral state (= Chandy-Lamport) · agent memory integrity signing

---

## 8. What Actually Remains Open (categorized — not patent claims)

These are **not** patent opportunities. Categories kept strictly separate:

| Area | Research | Engineering | Product | Patent |
|---|---|---|---|---|
| Persistent agent memory poisoning | **YES** (open) | YES | YES (defenses selling) | **UNPROVEN** |
| Multi-agent constraint/authority drift | **YES** (open) | YES | YES (PCAS/SafeFlow-style) | **UNPROVEN** |
| Individually-safe → collectively-unsafe composition | **YES** (open) | partial | early | UNPROVEN |
| Non-deterministic AI-code forensic reproducibility | YES (niche) | YES | maybe | UNLIKELY |
| Undetectable-stego lower bounds / detectable-subclass carving | **YES** (theory) | hard | no | UNLIKELY (impossibility results) |

**Do not conflate "research opportunity = YES" with "patent opportunity = YES."** In every row above they diverge.

---

## 9. Two Live Research Directions (research/product only — NOT patents)

### A. Persistent AI-agent memory poisoning
- **Current attacks:** MINJA (NeurIPS 2025, poison via normal queries); MemoryGraft (Dec 2025, plant via benign docs→summarized-to-memory); "sleeper"/delayed-trigger memory attacks. Persists across sessions (unlike prompt injection).
- **Existing defenses:** OWASP Agent Memory Guard (runtime read/write detector pipeline, mid-2026); A-MemGuard; OWASP five controls (sanitize, isolate, expire, audit-before-persist, cryptographic integrity). **Gap:** A-MemGuard evaluation found advanced LLM detectors miss ~66% of poisoned entries.
- **Research questions:** can memory writes be gated by *provenance of the content that produced them* rather than content inspection? Can trigger-latent poisoning be detected before activation? Is there a formal separation between "learned experience" and "injected instruction"?
- **Experiments:** measured miss-rate vs. OWASP Agent Memory Guard on MINJA/MemoryGraft corpora; time-to-trigger detection latency.
- **Products:** mem0 guidance, OWASP, WorkOS write-ups — active vendor space.
- **Patent risk:** HIGH (content-inspection detectors are being published rapidly; provenance-gating overlaps Round-4 agent-provenance red zone).

### B. Multi-agent constraint / authority drift
- **Mechanics:** constraints lose "operational force" across delegation, memory, tool-use, audit (five drift modes: memory/authority/information-flow/accountability/utility-induced — 2605.10481). Children should not exceed parent scope; enforcement must be in a deterministic runtime channel, not model prose.
- **Existing approaches:** **PCAS** (agent-state dependency graph + Datalog reference monitor, 48%→93% compliance); **SafeFlow** (semantic IFC); **DRIFT**; Authorization Propagation (2605.05440).
- **Research gaps:** *semantic* checkability (same syntactic action, drifted meaning) without a non-deterministic LLM judge; formal guarantees on drift bounds across long trajectories.
- **Experiments:** compliance rate + drift-detection latency vs. PCAS baseline on multi-hop delegation benchmarks.
- **Patent risk:** HIGH (reference monitor + IFC are mature; already applied in 2026 papers).

---

## 10. The Most Important Strategic Finding

> **The problem space is new, but the solution primitives are old.**

AI agents, agentic DFIR, non-human identity swarms, machine-speed self-modifying infrastructure — all genuinely new (2023–2026). But the defensive toolbox reached for again and again is mature: **reference monitors, information-flow control, capability systems, distributed snapshots (Chandy-Lamport), provenance/attestation, cryptographic commitments, zero-knowledge proofs, anomaly detection, covert-channel steganalysis, forward-secure logging, event sourcing.**

**Core rule for future patent research:**

> **New object + old primitive ≠ automatically novel invention.**

Applying a mature primitive to a new-but-analogous object, with a reasonable expectation of success, is the canonical §103 obviousness pattern. A defensible invention in this field must contribute something the primitive itself does not already provide — a *new* primitive, a *new* security property, or a *measured* technical advantage a skilled person would not have predicted.

---

## 11. What Would Actually Change the Result

A future candidate could survive only if it is one of these (and "AI + X" is **never** sufficient):

- **A genuinely new cryptographic primitive** (e.g., an efficient succinct argument for a property current systems cannot prove — noting that even the co-NP minimality case in Round 3 was infeasible, so this bar is high).
- **A genuinely new systems mechanism** with no established analog (not a reference monitor, snapshot, IFC label, or provenance chain in new clothing).
- **A new algorithm with a *measured* technical advantage** over the obvious baseline (e.g., beating Chandy-Lamport + event sourcing on a defined reconstruction task — Round 6 judged this unlikely).
- **A new hardware/software interaction** that provides a security property software alone cannot (and that TEE/PUF/measured-boot prior art does not already cover).
- **A new security property** existing primitives provably cannot deliver.
- **A narrow, unglamorous engineering niche** the 2026 land rush has not yet reached (more plausible than any of the above, but requires domain-specific discovery, not literature search).

---

## 12. Patent Verification Limitation

> Full-text patent verification could not be completed in the research environment because patent databases and certain primary research sources were inaccessible through the available network (HTTP 403 on Google Patents, USPTO/PPUBS, Espacenet, WIPO, Lens, Justia, FreePatentsOnline, and arXiv/Crossref direct-fetch).

Evidence must be read in three tiers, never collapsed:
- **Tier 1 — Verified non-patent prior art:** papers, standards, and products located and characterized via search (e.g., PeerReview SOSP 2007, ZKGraph, PCAS, GhostBuster DSN 2005, C2PA, EvidenceForge). These carry the analysis.
- **Tier 2 — Search-result-only patent evidence:** patent numbers + titles + one-line descriptions surfaced by search (e.g., US12524535 TEFTI, US20250209208A1, US11847234B2). Corroborative only.
- **Tier 3 — Unverified patent references:** anything whose claims were not read. **Never presented as definitive prior art.**

No unverified patent was used to *establish* anticipation; unverified patents only *corroborate* conclusions already supported by Tier-1 non-patent prior art.

---

## 13. Required Human Verification

For any future serious candidate, complete the verification this environment could not:

**Patents:** Google Patents · WIPO PATENTSCOPE · USPTO (PatFT/PPUBS) · EPO/Espacenet · Lens.
**Research:** IEEE Xplore · ACM DL · USENIX · NDSS · IEEE S&P · CCS · IACR ePrint · Springer · Elsevier.

For each candidate: (1) identify earliest disclosure; (2) read full text; (3) read independent claims; (4) check priority dates; (5) map patent families; (6) review forward/backward citations; (7) perform a limitation-by-limitation claim chart against the closest references; then (8) obtain a written patent-counsel §102/§103 opinion.

---

## 14. Final Patent-Hunt Checklist (reusable)

- [ ] Define the technical problem (concrete, not "AI needs X")
- [ ] Define the technical mechanism (Input → mechanism → transformation → measurable effect)
- [ ] Search the exact concept
- [ ] Search conceptual equivalents (rename aggressively)
- [ ] Search individual components
- [ ] Search component combinations (this is where obviousness lives)
- [ ] Search patents (full text, not snippets)
- [ ] Search papers · [ ] Search products · [ ] Search GitHub · [ ] Search standards
- [ ] Identify earliest disclosure date
- [ ] Single-reference anticipation test
- [ ] Obviousness / KSR combination test
- [ ] Identify a measurable technical effect vs. the obvious baseline
- [ ] Test feasibility (build the smallest thing that proves the mechanism)
- [ ] Actively attempt to kill the invention
- [ ] Professional full-text patent search
- [ ] Patent-counsel opinion
- [ ] Only then prototype substantially

---

## 15. Final Decision Framework — three gates

- **GATE 1 — Technical novelty hypothesis.** Is a *specific mechanism* meaningfully different from known primitives? If NO → **STOP.**
- **GATE 2 — Prior-art survival.** Does it survive aggressive single-reference + obviousness analysis (incl. cross-domain primitives)? If NO → **STOP.**
- **GATE 3 — Technical feasibility.** Can it be implemented *and* experimentally demonstrated to beat the obvious baseline? If NO → **STOP.**

Only candidates passing all three enter **Prototype → Patent strategy.** Across six rounds, **zero** candidates passed all three.

---

## 16. Final Recommendation

**Chosen option: A + B (stop the patent hunt; convert one live problem into a research paper) — explicitly NOT "keep searching for patents."**

- **Option A — Stop patent hunting (now).** Six rounds and ~30+ eliminations establish that the explored families are saturated. Another search round will, with high confidence, return another 🔴. Recommended.
- **Option B — Develop a research paper from a live problem.** If output value is wanted, the two live problems (§9) — memory-poisoning defense, constraint-drift enforcement — are publishable, with the honest caveat that both are crowded and neither is a patent play.
- **Option C — Professional patent verification** — reserve for a *future, independently generated* candidate, not the dead ones here.
- **Option D — A completely different technical domain** — the only path with a real chance of a defensible patent, but it must start from a new primitive or an unsaturated engineering niche (§11), not from "AI + security."

**Do not** commission a six-month build. **Do not** reopen any red-zone concept. **Do not** manufacture a winner.

---

## 18. Final Conclusion

> **Six rounds of defense-first investigation did not identify a sufficiently defensible AI / cybersecurity / cyber-forensics patent candidate. The investigation should therefore stop generating patent candidates from the explored technology families. Future work should either pursue research/product opportunities in the remaining live problems or restart patent discovery only from a fundamentally different technical domain or a genuinely new primitive.**

Companion file: `PATENT_HUNT_CHECKPOINT.md` (resume-without-repeating state).
Primary record: the six round reports (`PATENTABLE_IDEAS_…`, `PATENT_REVERIFICATION_ADVERSARIAL`, `PATENT_ROUND3_…`, `PATENT_ROUND4_…`, `PATENT_ROUND5_…`, `PATENT_ROUND6_…`).

*All statements are novelty/obviousness hypotheses requiring professional patent examination. Patent references are `UNVERIFIED — FULL TEXT NOT AVAILABLE`. Absence of a found reference has not been treated as evidence of novelty.*
