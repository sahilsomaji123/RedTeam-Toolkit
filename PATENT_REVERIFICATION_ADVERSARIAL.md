# Independent Adversarial Re-Verification of the Patent Discovery Report

**Companion to `PATENTABLE_IDEAS_AI_CYBERSECURITY_FORENSICS.md`**
Re-verification date: 2026-08-21. Posture: **defense-first, evidence-first, citation-first. Optimized to prevent wasted months, not to deliver good news.**

---

## 0. Bottom line up front

> **I found a material flaw in the previous conclusion.**
>
> **Executive verdict: SIGNIFICANTLY REVISED (bordering on REJECTED).** All three
> leading candidates were rated too optimistically. Under a fresh, hostile search of the
> underlying *mechanisms* (not the invented names), each candidate now faces either a
> **single-reference near-anticipation** or a **straightforward obvious combination** of
> pre-existing work — much of it foundational and years old, some of it 2025–2026 work
> that would be prior art against any new filing. None of the three currently qualifies as
> a clean 🟢 "potentially novel" hypothesis. The strongest survivor is a *narrowed sub-feature*
> of candidate #1, not candidate #1 as written.
>
> This remains subject to professional patent examination; I am not declaring anything
> unpatentable with certainty. But I could not, in good conscience, tell you to build any of
> the three as originally framed.

### Two hard limitations of this re-verification (stated up front)

1. **FULL-TEXT PATENT VERIFICATION WAS IMPOSSIBLE IN THIS ENVIRONMENT.** The mandatory step failed for a structural reason, not a transient one. Every patent host is blocked by this session's egress policy with HTTP 403: `patents.google.com`, `patents.justia.com`, `freepatentsonline.com`, `ppubs.uspto.gov`, `worldwide.espacenet.com`, `patentscope.wipo.int`, `lens.org`, and the PatentsView/USPTO JSON APIs. `arxiv.org` and `crossref.org` are **also** blocked for direct fetch. Only the `WebSearch` tool and a narrow allow-list function. **Therefore every patent below is marked `UNVERIFIED — FULL TEXT NOT AVAILABLE`** and is used only as *corroboration*, never as decisive novelty evidence. The independent, published, non-patent references (ACM/USENIX/arXiv papers, product write-ups) surfaced through search are the load-bearing evidence here.
2. **Search snippets are not full papers.** I read search-engine summaries, not every full text. Claims below are calibrated to that (e.g., "described as," "reported to"). A professional search must pull each primary document.

---

## 1. What I re-verified and how

I reset assumptions ("assume it already exists; find it"), re-read the original report in the repo, and ran ~15 conceptual query sets across the *mechanisms* of each candidate — decomposing each into components (IDS alert / provenance capture / minimal causal subgraph / detector-version freezing / cryptographic hashing / deterministic replay / offline verification / evidentiary packaging) and searching components and pairwise combinations, plus patents, papers, products, and open source. The important new references are cited inline.

---

## 2. Candidate 1 — Verdict Witness

**Original conclusion:** 🥇 Best patent opportunity, Overall ≈ 7.6 🟢. Claimed novelty: *minimal causally-closed subgraph + bitwise-deterministic re-scoring + tri-hash detector-build binding as a court-admissible evidentiary witness.*

### New prior art (the decisive finds)

| Element of Verdict Witness | Pre-existing disclosure | Where |
|---|---|---|
| Independently verifiable, **deterministically replayable security alert** carrying a **machine-verifiable proof** the recipient re-runs offline | **Self-Certifying Alerts (SCA) / Vigilante** — "automatically generated machine-verifiable proofs … independently and inexpensively verified by any host" by "replay of the execution." ~2005, foundational. | [Vigilante, ACM SOSP/TOCS](https://dl.acm.org/doi/10.1145/1455258.1455259); patents US7634813/US7603715/US7634812 `UNVERIFIED` ([USPTO print](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7634813)) |
| **Minimal causal subgraph** whose perturbation flips the malicious verdict | **ProvX** — "minimal structural subset within a graph predicted as malicious that, when perturbed, subverts the model's original prediction." Aug 2025. | [ProvX, arXiv 2508.06073](https://arxiv.org/html/2508.06073v1) |
| Minimal attack subgraph via optimal/Steiner extraction; "scenario graph = causally-dependent subgraph" | **NodLink** (Steiner-tree minimal subgraph); PIDS survey defines scenario graphs | [PIDS survey, ACM CSUR](https://dl.acm.org/doi/10.1145/3539605); [ACTMINER, arXiv 2501.05793](https://arxiv.org/pdf/2501.05793) |
| **Reproducible, forensically-sound IDS pipeline packaged with artifacts for verification**, combining graph modeling + counterfactual + explainability, governed by ISO/IEC 27037/27041/27042 + NIST SP 800-86 | **"Forensic-ready intrusion detection …"** (June 2026): "complete workflow packaged with reproducible outputs and intermediate artifacts supporting verification and reuse." Plus a synthetic-traffic forensic-IDS governed by the ISO/NIST forensic standards. | [ScienceDirect S2215016126002104](https://www.sciencedirect.com/science/article/pii/S2215016126002104); [arXiv 2607.00763](https://arxiv.org/abs/2607.00763) |
| **Committed-model reproducible inference**: publish a hash commitment of model params; return output + proof it came from the committed model | **zkML / cryptographic verifiability of AI pipelines** — mature line of work. | [Cryptographic verifiability of end-to-end AI pipelines, arXiv 2503.22573](https://arxiv.org/html/2503.22573v1); [ZK verifiable inference, arXiv 2511.19902](https://arxiv.org/html/2511.19902) |
| **Signed, offline-verifiable DFIR "verdict" bound to model version + reproducible inputs, made court-admissible** | Described 2026 **agentic-DFIR** practice and a product literally named **VERDICT** ("a DFIR agent … produces a signed, offline-verifiable verdict"); audit log records "model version, input-output documentation" and "ability to reproduce the analysis with the same model version and inputs." | [Secured Intel / Above the Law coverage, 2026](https://abovethelaw.com/2026/07/agentic-ai-for-forensics-investigations-is-fast-auditable-and-about-to-bloody-daubert/); [Decision Evidence Maturity Model, arXiv 2605.04093](https://arxiv.org/pdf/2605.04093) |

### Claim-by-claim (illustrative independent claim vs. prior art)

| Claim limitation | Anticipated by | Similarity | Residual difference |
|---|---|---|---|
| generate anomaly verdict from provenance graph | FLASH/PIDS survey | identical | none |
| extract minimal causally-closed subgraph sufficient to reproduce verdict | ProvX / NodLink / scenario graphs | very high (ProvX = minimal subgraph that flips prediction) | ProvX flips prediction for *explanation*; "sufficient-to-reproduce" framing is a re-label, not a new algorithm |
| bind (weights-hash, pipeline-hash, ruleset-hash) + seed | zkML committed-model inference; ML-SBOM | high | tri-hash granularity is an engineering choice |
| deterministic bitwise re-scoring harness | Vigilante SCA replay; APEX.AI deterministic replay (US12131203 `UNVERIFIED`) | very high | applying replay to a scorer vs. an exploit — same mechanism |
| PQ-signed witness, court-admissible | agentic-DFIR audit logs; PQ audit-evidence (2512.00110) | high | signature choice; not novel |

### Single-reference test
No single reference contains *every* element with identical wording — **but** the agentic-DFIR "signed, offline-verifiable verdict + model-version + reproducible inputs" description (and the June-2026 forensic-ready reproducible IDS paper) come dangerously close to a single-reference anticipation of the *product concept*, missing only the explicit "minimal subgraph" element that ProvX independently supplies.

### Obviousness test
**Fails.** Verdict Witness = PIDS (known) + ProvX minimal subgraph (known) + Vigilante-style self-certifying replay (known, 2005) + zkML committed-model inference (known) + PQ signatures (known). A skilled person building a "forensically reproducible IDS verdict" in 2026 would combine exactly these, and at least one 2026 paper already combines most of them. **Obviousness risk: HIGH.**

### Verdict — Candidate 1: 🟠 Likely obvious as written.
Novelty status: the *packaging* is not novel; the *minimality* element is ProvX; the *replay* element is Vigilante. **The only sliver with a distinct technical effect** is discussed in §6.

---

## 3. Candidate 2 — Oracle-Gated DFIR

**Original conclusion:** 🥈 Best research+patent, ≈ 7.3 🟢. Claimed novelty: *per-atomic-claim emit-gating through deterministic forensic oracles + signed coverage certificate bound to CoC.*

### New prior art

- **Tool-attested, deterministically-verified claim gating already exists.** *EG-VAR* ("Evidence-Grounded Verified Agentic Reasoning … eliminating LLM hallucination via tool-attested kernel proofs") uses a deterministic tool layer + a Lean-4 kernel that *mints verified claims* before a solver LLM may use them — this is emit-gating on deterministic verification. [arXiv 2607.12650](https://arxiv.org/html/2607.12650v1).
- **Forensic-specific claim→ground-truth binding already exists.** *LLM-driven Provenance Forensics* "ensures every LLM-generated claim is tied to verifiable ground truth in the underlying database." [arXiv 2508.21323](https://arxiv.org/html/2508.21323v1).
- **Atomic-claim decomposition + aggregated verification coverage as a quantitative metric already exists.** *FinGround* (atomic claim verification for hallucination detection/grounding) [arXiv 2604.23588](https://arxiv.org/pdf/2604.23588); *DEER* "extracts atomic claims, links them to sources, and aggregates verification outcomes into quantitative metrics" [arXiv 2512.17776](https://arxiv.org/pdf/2512.17776); *Citation-Grounding/Graph-Coverage* explicitly shows the reported hallucination rate is governed by **oracle coverage** [arXiv 2606.00898](https://arxiv.org/html/2606.00898).
- **Signed, version-bound verification certificate already exists.** A *Trust Certificate* is "a machine-verifiable attestation … that binds a specific agent version to its verification evidence." [arXiv 2606.04037](https://arxiv.org/pdf/2606.04037).

### Single-reference test
No single reference is the whole thing, but EG-VAR alone supplies claim-level deterministic gating; adding "the tools are Volatility3/YARA" is application, not mechanism.

### Obviousness test
**Fails.** Oracle-Gated DFIR = EG-VAR/HallucinationGate (gate) + LLM-driven Provenance Forensics (forensic ground-truth binding) + FinGround/DEER (atomic-claim coverage metric) + Trust Certificate (signed version-bound certificate). The "coverage certificate bound to CoC" is a routine composition of a known coverage metric with a known signing/CoC primitive. **Obviousness risk: HIGH.**

### Verdict — Candidate 2: 🟠 Likely obvious. The forensic-oracle *routing table* (claim-type → specific forensic tool + bounded query) is the only element I could not find pre-disclosed as a unit, and it reads as an engineering schema, not an inventive mechanism.

---

## 4. Candidate 3 — Prompt-Injection Forensic Reconstructor

**Original conclusion:** 🥉 Best commercial, ≈ 7.2 🟢. Claimed novelty: *counterfactual span-ablation over deterministic agent replay to isolate the minimal injecting input span, sealed as forensic evidence.*

### New prior art — this candidate is essentially anticipated

- **AgentSentry (Feb 2026)** performs "controlled counterfactual re-executions **at tool-return boundaries**" and "yields an interpretable **localization of the earliest boundary at which injected context becomes the dominant driver** of subsequent unsafe behavior." That is precisely counterfactual-replay attribution of an indirect prompt injection to a specific input locus. [arXiv 2602.22724](https://arxiv.org/html/2602.22724v1). The only difference from the candidate is *framing* — AgentSentry calls it inference-time defense/purification; the candidate calls the same output "forensic evidence."
- **Causal Agent Replay (CAR)** — "counterfactual attribution for LLM-agent failures" by intervening on a step and observing the outcome (do_resample interventions, point-of-commitment locus, Shapley credit). [arXiv 2606.08275](https://arxiv.org/pdf/2606.08275).
- **CausalFlow** (causal debugging of agent traces → minimal validated repairs) [arXiv 2605.25338](https://arxiv.org/pdf/2605.25338); **DoVer** (intervention-driven auto-debugging, "attribution as a hypothesis tested by targeted edit + rerun") [arXiv 2512.06749](https://arxiv.org/html/2512.06749v1/); **AgentDebugX**, **AgenTracer-8B** (failure attribution).
- **Delta debugging** (Zeller, ~1999): the classic algorithm that "removes irrelevant parts of the input until only the smallest failure-inducing chunk remains." The "minimal span" element is textbook.
- **Commercial:** agent-incident-forensics offerings already marketed (e.g., Armalo). [armalo.ai](https://www.armalo.ai/learn/ai-agent-incident-forensics).

### Single-reference test
**PASSES against the candidate (i.e., it is anticipated).** AgentSentry alone discloses counterfactual re-execution at tool-return boundaries to localize the injecting context. Adding "sign the result as a witness" is a trivial, well-known addition.

### Verdict — Candidate 3: 🔴 Already known. Sealing the attribution cryptographically does not rescue it — signed evidence is generic (Critical Rule §10).

---

## 5. Anti-novelty matrix

| Candidate | Strongest reference | Single-ref anticipation? | Obvious combination? | Remaining novelty | Class (old → new) |
|---|---|---|---|---|---|
| 1 Verdict Witness | Vigilante SCA + ProvX + agentic-DFIR "VERDICT" | Near, split across 2 refs | Yes (HIGH) | ZK non-disclosure sub-feature only (§6) | 🟢 7.6 → **🟠 ~4.5** |
| 2 Oracle-Gated DFIR | EG-VAR + LLM-driven Provenance Forensics + FinGround | No, but EG-VAR covers the gate | Yes (HIGH) | forensic claim-type→oracle routing schema | 🟢 7.3 → **🟠 ~4.5** |
| 3 PI Forensic Reconstructor | AgentSentry (+ delta debugging) | **Yes** | Yes (HIGH) | none material | 🟢 7.2 → **🔴 ~2.5** |

---

## 6. Did I resurrect anything? The one surviving sliver

Per instruction, I tried to find something stronger, including from the previously-rejected list.

- **Candidate #4 (destruction-signature anti-forensic tripwire)** — I re-tested it and it is *weaker* than hoped: fragile watermarking already couples tamper localization with "an ML decision layer to classify manipulation types" from block-wise BER features ([Nature Sci Rep 2025](https://www.nature.com/articles/s41598-025-01297-4)). The only residual is *attack-agnostic classification of unseen generative-edit families from the keyed destruction manifold*; partial novelty, **🟡 uncertain**, not clearly better than a narrowed #1.
- **Candidate #3-sensor (multi-channel physics consistency)** — PRNU deepfake detection + IMU/rolling-shutter fusion + TEE attestation are all known; the cross-channel *mutual-consistency proof sealed per-frame* is a combination. **🟡.**

**The single most defensible residual across everything** is a *narrowed* piece of Verdict Witness with a genuinely distinct **technical effect** that none of the anticipating references provide:

> A **zero-knowledge / succinct proof that a committed anomaly-detector build, evaluated on a minimal causal provenance witness subgraph, yields a specific verdict — while disclosing neither the remainder of the enterprise provenance graph nor the detector's weights.**

Why this is different from the killers: Vigilante SCAs, the "VERDICT" agentic-DFIR verdict, and the forensic-ready IDS pipeline all achieve verifiability by **disclosing** the inputs and the model version to the verifier. zkML achieves non-disclosure but has **not**, in what I found, been applied to *provenance-graph intrusion verdicts with selective graph non-disclosure* (the search explicitly noted "specific intrusion detection implementations weren't extensively covered"). Simultaneously proving *a security verdict* while keeping *both the sensitive log graph and the proprietary detector secret* is a concrete technical effect (privacy + verifiability at once) the prior art does not deliver in this domain.

**Honesty check on this sliver:** it is still a **zkML + PIDS combination**, and zkML is mature, so the obviousness risk is real and must be professionally examined. I rate it **🟡 uncertain (new-novelty hypothesis)**, *not* 🟢. It is a hypothesis worth one attorney conversation — not a green light to build.

---

## 7. New scores

| Criterion | Cand 1 (old→new) | Cand 2 (old→new) | Cand 3 (old→new) | Reason for change |
|---|---|---|---|---|
| Novelty | 8 → 3 | 7 → 3 | 8 → 2 | Core elements individually pre-disclosed |
| Inventive step | 8 → 3 | 7 → 3 | 7 → 2 | Straightforward combinations |
| Prior-art distance | 7 → 3 | 6 → 3 | 7 → 2 | AgentSentry/ProvX/Vigilante/EG-VAR close the gap |
| Claim potential | 8 → 4 | 8 → 4 | 7 → 2 | Only narrowed sub-features survive |
| Technical feasibility | 8 → 8 | 8 → 8 | 7 → 8 | Unchanged (all buildable) |
| Market value | 8 → 7 | 9 → 8 | 7 → 7 | Demand real; but incumbents present (VERDICT, Armalo, Exterro) |
| Research value | 8 → 5 | 8 → 6 | 8 → 3 | Space is already publishing heavily |
| **Overall** | **7.6 → ~4.5 🟠** | **7.3 → ~4.5 🟠** | **7.2 → ~2.5 🔴** | Significantly revised |

---

## 8. The most important question, answered concretely

> *"If I gave this to a patent attorney tomorrow, which specific technical feature would I tell them to investigate first as the potential novelty-bearing claim element, and why?"*

**Investigate first:** *a graph-selective zero-knowledge succinct proof that binds (i) a cryptographic commitment to a frozen anomaly-detector build and (ii) a canonicalized minimal causal provenance witness-subgraph to (iii) a specific intrusion verdict, such that an independent verifier confirms the verdict without the prover disclosing the non-witness portion of the provenance graph or the detector's weights.*

**Why this element and not the others:** it is the only feature I could not knock out with a single reference or an obvious two-reference combination *that also produces a distinct technical effect* — simultaneous **confidentiality of the evidence corpus and the model** with **public verifiability of the verdict**. The closest killers (Vigilante SCA, the "VERDICT" product, forensic-ready IDS) all require *revealing* the inputs/model to verify; zkML supplies non-disclosure but has not, per my search, been reduced to practice for *provenance-graph intrusion verdicts with selective subgraph disclosure*. The novelty, if any survives professional search, lives in the **selective-disclosure circuit over a canonical provenance subgraph**, not in "AI," "signing," "replay," or "a verdict."

**What is explicitly NOT the novelty** (do not let anyone claim these): using AI to detect intrusions; hashing a model version; signing an alert; replaying a computation; extracting a minimal subgraph for explanation; producing a court-admissible audit log. Each is separately pre-disclosed above.

---

## 9. Final recommendation

**🥇 Do not prototype any of the three as originally specified.** If you pursue one thread, pursue the **narrowed sliver from §6/§8** — the *graph-selective ZK proof of a PIDS verdict* — and treat it as an unproven hypothesis, not a filing-ready invention.

- **Why it survived:** distinct technical effect (privacy + verifiability together) absent from the closest prior art in this specific domain.
- **Exact novelty hypothesis:** the selective-disclosure ZK circuit binding {committed detector build, canonical minimal witness subgraph, verdict} while hiding the non-witness graph and the weights.
- **Three strongest prior-art threats:** (1) mature **zkML / verifiable-inference** work (obviousness by combination) — [2503.22573], [2511.19902]; (2) **Self-Certifying Alerts / Vigilante** (independently verifiable replayable security alert) — [Vigilante TOCS]; (3) **ProvX** (minimal causal subgraph for provenance detection) — [2508.06073].
- **Three strongest differentiating features to build the case on:** (a) **non-disclosure** of the surrounding provenance graph during verification; (b) **weight-confidential** verdict verification; (c) a **canonicalization of a causal provenance subgraph into a ZK-circuit-friendly witness** (the hard, possibly-novel engineering).
- **What must be experimentally demonstrated:** a working zk-SNARK/STARK that verifies a real PIDS verdict (e.g., over DARPA OpTC) from a witness subgraph in practical prover time, revealing neither the full graph nor the model — and a measured privacy/verifiability trade-off vs. the disclose-everything baselines (Vigilante-style, "VERDICT"-style).
- **What must be verified before filing:** a **professional full-text patent search** (which this environment could not perform — all databases 403-blocked) specifically over "zero-knowledge verifiable inference," "privacy-preserving intrusion detection proof," and "verifiable ML SBOM/attestation"; and full reading of US20250209208A1, US11847234B2, US7634812/7603715/7634813, and US12131203, all currently `UNVERIFIED`.
- **What should NOT be claimed:** anything reciting "AI-based," "blockchain-based," "intelligent," "automated," a signed audit log, a replayable verdict per se, or a minimal explanatory subgraph per se — each is pre-disclosed.
- **What could become the independent claim:** the selective-disclosure ZK verification of a committed-detector verdict over a canonical minimal provenance witness-subgraph, characterized by non-disclosure of the non-witness graph and of the detector weights.

---

## 10. Verdict statements (per the task's absolute rule)

- **Candidate 3 (Prompt-Injection Forensic Reconstructor):** *I found a single-reference near-anticipation (AgentSentry) plus a classic algorithm (delta debugging) that, together, destroy the specific novelty hypothesis. Reject.*
- **Candidates 1 and 2:** *I identified clearly obvious combinations that destroy the specific novelty hypotheses as written; each retains only a narrowed sub-feature that requires professional examination.*
- **The §6/§8 sliver:** *I attempted to invalidate it and could not identify a single-reference anticipation or a clearly obvious combination that destroys its specific novelty hypothesis (graph-and-weight-confidential ZK verification of a provenance-IDS verdict), subject to professional patent examination and subject to the fact that I could not read the full text of any patent in this environment.*

> No claim of patentability is made with certainty. Every conclusion is a novelty **hypothesis** requiring professional prior-art search and legal examination. Patent references are `UNVERIFIED — FULL TEXT NOT AVAILABLE` due to environment egress blocks; "not retrieved" ≠ "does not exist," and equally, my inability to find an anticipating patent is **not** evidence of novelty.
