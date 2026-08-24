# Round 3 — Adversarial Investigation of the ZK-Provenance Hypothesis

**Companion to `PATENTABLE_IDEAS_AI_CYBERSECURITY_FORENSICS.md` and `PATENT_REVERIFICATION_ADVERSARIAL.md`**
Date: 2026-08-21. Posture: **defense-first, evidence-first. Not optimized for a green result.**

**Hypothesis under test:** *A privacy-preserving verification mechanism in which a zero-knowledge proof demonstrates that a committed detector/model, executed against a selected minimal causal provenance witness-subgraph, produces a specific security verdict — without revealing the complete provenance graph, sensitive evidence, model weights, or unrelated telemetry.*

---

## 1. Executive Verdict

> ## 🟠 → **C. ZK HYPOTHESIS IS LIKELY OBVIOUS.** **STOP — DO NOT BUILD (as specified).**
>
> Every one of the twelve technical elements (A–L) is individually established in the
> prior art, with named references. The *integrating motivation* — "independently verify a
> security detection without revealing the telemetry, the detection thresholds, or the model
> weights" — is not a gap I discovered; it is **explicitly stated** in the ZK-verifiable-computation
> literature and was the funding premise of a multi-year DARPA program (SIEVE). Multiple
> near-neighbour combinations are already published (ZK+anomaly-detection-in-FL, ZK+deepfake-detection,
> ZKGraph private verifiable graph queries, zkML private verifiable inference, abductive minimal
> explanations for IDS, HE/FL privacy-preserving provenance APT detection). Assembling zkML + PIDS +
> a minimal witness is therefore a **predictable application of general-purpose tools to a known
> problem** — the textbook shape of a §103 / inventive-step rejection.
>
> The **one** element I could not find in the prior art — a ZK proof of *cardinality*-minimality
> ("no smaller witness of any composition satisfies the verdict") — is a **co-NP / universally-quantified
> statement that current succinct proof systems cannot practically handle**, so it fails on
> feasibility, not just novelty. The feasible cousin (subset-minimality / irredundancy) decomposes
> into abductive-explanation (known) + zkML run |witness| times (obvious).
>
> **The hypothesis fails the Phase-17 build gate** (which requires Novelty ≥7 **and** Inventive-step ≥6
> **and** Prior-art-distance ≥6 **and** Feasibility ≥6 — see §17). No configuration clears all four.

**Two mandatory honesty caveats, unchanged from Round 2 and material to this verdict:**
1. **FULL-TEXT PATENT VERIFICATION REMAINS IMPOSSIBLE HERE.** Every patent database (Google Patents, USPTO/PPUBS, Espacenet, WIPO, Lens, Justia, FreePatentsOnline) and arXiv/Crossref direct-fetch return HTTP 403 under this session's egress policy. All patents below are **`UNVERIFIED — FULL TEXT NOT AVAILABLE`**, used only as corroboration. My inability to find an anticipating *patent* is **not** evidence of novelty; equally, "likely obvious" here rests on abundant **non-patent** prior art, which does not require patent access.
2. This means the residual risk includes an *already-granted patent I literally cannot see*. A professional full-text search is mandatory before any further spend.

---

## 2. Component-by-component novelty analysis (Phases 1–2, 6)

| # | Element | Established prior art (named) | Novel? |
|---|---|---|---|
| A | committed/deterministic security detector produces verdict | PIDS (FLASH, CONTINUUM); ZKML committed-model inference | No |
| B | events as a provenance graph | PIDS survey (ACM CSUR 3539605); P3GNN | No |
| C | causal reduction to a relevant subset | scenario graph (causally-dependent subgraph); NodLink (Steiner); ACTMINER | No |
| D | selected subgraph as cryptographic witness | ZK witness is standard; ZKGraph verifies a result consistent with a private graph | No |
| E | detector build cryptographically committed | zkML: "public commitment = hash of model params"; ML-SBOM | No |
| F | inputs committed | commitment schemes; zkML input commitments | No |
| G | ZK proof of correct detector execution | **zkML / ZKML (EuroSys 2024), pvCNN, zkPyTorch** | No |
| H | proof: committed detector + witness → verdict V | zkML inference proof = exactly this shape | No |
| I | selective disclosure (verifier doesn't get full evidence) | **ZK selective disclosure (VC/BBS+), ZKGraph, DARPA SIEVE** | No |
| J | model-weight confidentiality | zkML core promise ("convince users output is correct inference without revealing model parameters") | No |
| K | independent third-party verification | SNARK public verifiability | No |
| L | security/forensic application of the above | **DARPA SIEVE / Trail of Bits** (ZK proof of exploitability without revealing exploit); ZK deepfake detection (2507.17010); ZK anomaly detection in FL (2310.04055) | No |

**No single element is novel.** Sources: [ZKML EuroSys](https://ddkang.github.io/papers/2024/zkml-eurosys.pdf); [ZK verifiable ML survey](https://arxiv.org/html/2502.18535v2); [pvCNN](https://arxiv.org/pdf/2201.09186); [ZKGraph](https://arxiv.org/html/2507.00427); [P3GNN](https://arxiv.org/abs/2406.12003); [DARPA SIEVE / Trail of Bits](https://blog.trailofbits.com/2020/05/21/reinventing-vulnerability-disclosure-using-zero-knowledge-proofs/); [ZK deepfake detection](https://arxiv.org/pdf/2507.17010); [ZK anomaly detection in FL](https://arxiv.org/pdf/2310.04055).

---

## 3. The ZK + provenance combination analysis (Phase 3)

- **ZK over private graphs with verifiable results and selective disclosure already exists:** **ZKGraph** — "the first system to leverage non-interactive ZK proofs for the confidential and verifiable evaluation of arbitrary graph queries," using PLONKish circuits for node-neighbourhood expansion and shortest-path, verifying that results are "consistent with the query's constraints and the private graph database." [arXiv 2507.00427](https://arxiv.org/html/2507.00427). Private **subgraph** membership between two private graphs is also a known ZK protocol.
- **Privacy-preserving provenance-based APT detection already exists** (via a *different* privacy primitive): **P3GNN** = Federated Learning + **Paillier homomorphic encryption** over provenance-graph GCN for APT detection. [arXiv 2406.12003](https://arxiv.org/html/2406.12003v1). Swapping HE/FL for ZK to add public verifiability is a predictable substitution given ZKGraph + zkML exist.
- **The exact named integrated system** (zkML + PIDS + GNN + verifiable proof) was *not* found — the search engine flagged it as "an emerging research area." **But combination white-space with all parts known and the motivation documented is the classic setup for an obviousness rejection, not evidence of inventive step.**

**Verdict on the combination: LIKELY OBVIOUS.**

---

## 4. Minimal causal witness analysis (Phase 7)

The idea of a *provably minimal sufficient* witness is **not new** — it is a mature formal-XAI field:

- **Abductive explanations (AXp):** "a minimal set of features sufficient to guarantee the same decision… subset-minimality ensures irredundancy: if any feature is removed, the set no longer guarantees the prediction." [Ignatiev et al., AAAI'19](https://alexeyignatiev.github.io/assets/pdf/inms-aaai19-preprint.pdf); [minimum-size AXp](https://arxiv.org/html/2603.14096). Computing AXp is **NP-hard**; minimum-size is harder.
- **Counterfactual minimal subgraph for PIDS specifically:** **ProvX** finds "the minimal structural subset within a graph predicted as malicious that, when perturbed, subverts the prediction." [arXiv 2508.06073](https://arxiv.org/html/2508.06073v1).
- **Abductive reasoning already applied to IDS:** "Extending Signature-based IDS with Bayesian Abductive Reasoning"; "Formal Reasoning About IDS."

So a *minimal causal provenance witness* = ProvX/abductive-explanation applied to provenance graphs — **already essentially disclosed**. Not the novelty.

---

## 5. The minimality-proof analysis (Phase 8) — the crux, and why it still fails

The sharpest possible distinction was: *prove in ZK that the witness is minimal.* Splitting this precisely decides the whole round:

- **Subset-minimality / irredundancy** ("removing any one element of the witness flips the verdict"): expressible as **|witness| existential checks**, each "here is an assignment where dropping element e changes the output." Feasible in ZK — but it is exactly **abductive-explanation irredundancy (known) proven with zkML run |witness|+1 times (obvious composition)**. No inventive step.
- **Cardinality-minimality** ("no smaller witness of *any* composition satisfies the verdict"): a **∀-quantified / co-NP statement** over exponentially many subsets. The search confirmed (twice) that **succinct proof systems are built for NP/existential statements, and co-NP / non-existence / universal quantification is a known open limitation** ("most practical implementations are designed for existential statements rather than universal ones"). [ZK survey](https://arxiv.org/html/2408.00243v1); [SNARKs for C](https://eprint.iacr.org/2013/507.pdf). This variant is **genuinely under-explored (potential novelty) but likely infeasible** at provenance-graph scale — so it cannot anchor a *buildable* invention.

**Conclusion:** the only novelty-bearing statement is precisely the one current cryptography can't practically prove. That is a research problem for cryptographers, **not** a near-term patentable, prototypable mechanism.

---

## 6. Obviousness attack (Phase 11)

| Question | Answer | Evidence |
|---|---|---|
| Would a skilled person combine zkML with PIDS? | **Yes** | zkML is a general "verify any ML inference privately" tool; PIDS is ML inference over a graph |
| Explicit paper suggesting privacy-preserving verifiable detection? | **Yes** | ZK "enables the server to demonstrate correctness to clients without revealing… detection thresholds"; P3GNN (privacy-preserving PIDS) |
| Is graph input to ZK computation established? | **Yes** | ZKGraph; ZK subgraph isomorphism |
| Is selective disclosure established? | **Yes** | ZK-SD verifiable credentials; DARPA SIEVE |
| Is minimal-evidence selection established? | **Yes** | abductive explanations; ProvX; NodLink |
| Is "verify security fact without revealing sensitive detail" an established ZK motivation? | **Yes** | DARPA SIEVE / Trail of Bits (working impl. on MSP430 vulns) |
| Would combining these teachings be predictable, with a reasonable expectation of success? | **Yes** | each part is engineered and composable |

**All seven point to obviousness.** Under a KSR-style analysis (combining known elements per their established functions to yield predictable results), the broad hypothesis is **LIKELY OBVIOUS**.

---

## 7. Capability comparison matrix (Phase 10)

| Capability | zkML | PIDS | ZKGraph | P3GNN | DARPA SIEVE | **Proposed** |
|---|---|---|---|---|---|---|
| Verifiable inference | ✅ | — | ✅(query) | — | ✅(exploit) | ✅ (reused) |
| Provenance evidence | — | ✅ | ~(graph) | ✅ | — | ✅ (reused) |
| Causal reduction / minimal subset | — | ✅(ProvX/NodLink) | — | — | — | ✅ (reused) |
| Minimal *witness* (provable) | — | ✅(abductive/ProvX) | — | — | — | ~ (reused) |
| Privacy-preserving verification | ✅ | — | ✅ | ✅(HE) | ✅ | ✅ (reused) |
| Model confidentiality | ✅ | — | — | ~ | ✅ | ✅ (reused) |
| Evidence confidentiality | ~ | — | ✅ | ✅ | ✅ | ✅ (reused) |
| Independent verification | ✅ | — | ✅ | — | ✅ | ✅ (reused) |
| **Cardinality-minimality proof in ZK** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ *(nobody — likely infeasible)* |
| Security-verdict proof | ~ | ✅ | — | ✅ | ✅ | ✅ (reused) |

The proposed system's every ✅ is inherited from an existing column. The only empty column across **all** systems is the one it also cannot fill (cardinality-minimality in ZK).

---

## 8. Claim-element kill chart (Phases 14–15)

Illustrative independent claim → hostile mapping.

| Claim limitation | Anticipating reference | Match | Missing from that ref |
|---|---|---|---|
| commit to detector build | zkML public commitment | full | — |
| represent security events as provenance graph | PIDS survey; P3GNN | full | — |
| select minimal causal witness-subgraph | ProvX / abductive AXp / NodLink | full | (ProvX = explanation, not "for proof input" — re-label) |
| ZK-prove committed detector on witness → verdict, hiding graph+weights | zkML + ZKGraph (compose) | high | single ref doesn't do *both* graph-privacy and weight-privacy in one artifact |
| independently verify offline | SNARK verifiability; DARPA SIEVE | full | — |
| prove witness is subset-minimal | abductive irredundancy + zkML×|S| | high | not previously composed *in ZK* — but obvious composition |
| prove witness is cardinality-minimal | **none found** | — | infeasible in current SNARKs (co-NP) |

- **Anticipated?** UNCERTAIN as a *single* reference; **YES in substance across two references** (zkML + ZKGraph).
- **Obvious?** **YES** for the broad claim and for subset-minimality.
- **Novelty-bearing element?** Exactly one: **a succinct ZK proof of *cardinality*-minimality of the witness** — which is presently **infeasible**, hence not a viable claim.

---

## 9. Strongest prior-art threats (ranked)

1. **zkML / ZKML (EuroSys 2024) + the ZK-verifiable-ML survey** — supplies verifiable inference with model-weight confidentiality (elements E, G, H, J, K). [ddkang.github.io/…/zkml-eurosys.pdf](https://ddkang.github.io/papers/2024/zkml-eurosys.pdf)
2. **ZKGraph** — supplies confidential + verifiable computation over a private graph with selective result disclosure (elements B, D, I). [arXiv 2507.00427](https://arxiv.org/html/2507.00427)
3. **DARPA SIEVE / Trail of Bits** — supplies the security-domain motivation and working practice of "ZK-prove a security fact without revealing the sensitive detail" (element L, motivation). [Trail of Bits](https://blog.trailofbits.com/2020/05/21/reinventing-vulnerability-disclosure-using-zero-knowledge-proofs/)
4. **Abductive explanations (AXp) + ProvX** — supply the provably-minimal / minimal-causal witness (elements C, minimal-witness). [Ignatiev AAAI'19](https://alexeyignatiev.github.io/assets/pdf/inms-aaai19-preprint.pdf); [ProvX 2508.06073](https://arxiv.org/html/2508.06073v1)
5. **P3GNN** — privacy-preserving provenance APT detection already exists (via HE/FL). [arXiv 2406.12003](https://arxiv.org/abs/2406.12003)

---

## 10. Remaining novelty-bearing mechanism & feasibility (Phases 12–13)

The uncombined part is **not** the system; it is a **cryptographic primitive**: an efficient succinct argument for **cardinality-minimality** of a graph witness under a committed predicate ("no k-1-node subset satisfies the detector predicate"). This is a co-NP-flavoured statement.

- **Required primitives:** a proof system for universal/co-NP statements (e.g., via a verifiable minimality *certificate* — a MUS/MCS-style certificate — or recursive SNARK composition, or a GKR/IP-for-coNP construction). All are research-grade, not off-the-shelf.
- **Smallest demonstrable prototype (if pursued as a crypto project, not a product):** prove subset-minimality (irredundancy) of a **tiny** witness (≤10 nodes) over a **small** committed GNN on one DARPA OpTC scenario, and *measure* proving time, proof size, and memory. Cardinality-minimality even at this toy scale is the real test.
- **Expected reality:** subset-minimality is buildable but non-inventive; cardinality-minimality proving time is likely to explode. If a toy instance already takes hours or won't compose, the distinguishing feature is dead on feasibility.

**Feasibility score for the novelty-bearing part: ~2–3/10.** Feasibility for the non-novel part: ~7/10.

---

## 11. Scores against the Phase-17 build gate

| Configuration | Novelty | Inventive step | Prior-art distance | Feasibility | Passes gate? |
|---|---|---|---|---|---|
| Broad ZK-provenance verdict | 3 | 3 | 3 | 7 | ❌ (needs all ≥ thresholds) |
| + subset-minimality proof | 4 | 4 | 4 | 6 | ❌ |
| + **cardinality-minimality proof** | 7 | 6 | 7 | **2** | ❌ (feasibility) |

**Gate requires Novelty ≥7 AND Inventive-step ≥6 AND Prior-art-distance ≥6 AND Feasibility ≥6. No row clears all four → STOP, DO NOT BUILD.**

---

## 12. Precise technical problem (Phase 9) — and whether it's solved

*Concrete problem:* "Existing security-verification requires disclosing sensitive telemetry, detection thresholds, or model internals to let a third party independently reproduce a verdict — a conflict between independent verifiability and confidentiality."

*Is it solved by the proposed mechanism?* **The conflict is already resolved by existing tools** — zkML (verify inference, hide weights) + ZKGraph (verify over a private graph) already deliver verifiability-with-confidentiality; DARPA SIEVE already applies exactly this to security facts. The proposed mechanism re-solves an already-solved conflict with a domain relabel. It does **not** introduce a new technical effect beyond what zkML + ZKGraph provide — except (again) the infeasible cardinality-minimality proof.

---

## 13. Patentability-risk assessment

- **Novelty (§102) risk:** moderate-high — no single reference found, but two-reference substance is very close.
- **Inventive step (§103 / KSR) risk:** **HIGH** — the defining problem; predictable combination of general tools with documented motivation.
- **Enablement (§112) risk for the only novel claim:** **HIGH** — cardinality-minimality in ZK may not be enabled/feasible; claiming it risks an unsupported claim.
- **FTO risk:** **UNKNOWN and unquantifiable here** — patent full-text is inaccessible; a blocking patent cannot be excluded.

---

## 14. DEAD-END MAP (Phase 19 — Rounds 1–3, to prevent rediscovery)

| Idea | Why it looked novel | Killer prior art | Why it failed |
|---|---|---|---|
| **Verdict Witness** (replayable PIDS verdict) | reproducible court-grade IDS verdict | Vigilante Self-Certifying Alerts (replayable verifiable alert); ProvX (minimal subgraph); zkML (committed inference); "VERDICT" agentic-DFIR product | obvious combination; core value described in a 2026 product |
| **Oracle-Gated DFIR** (claim-gated LLM forensics) | per-claim oracle gate + coverage certificate | EG-VAR (tool-attested verified claims); LLM-driven Provenance Forensics (claim→DB ground truth); FinGround/DEER (atomic-claim coverage); Trust Certificate | obvious combination |
| **Prompt-Injection Forensic Reconstructor** | counterfactual span-ablation attribution | **AgentSentry** (counterfactual re-exec at tool-return boundaries → localize injecting context); Causal Agent Replay; **delta debugging** | single-reference near-anticipation |
| **Anti-forensic destruction-signature tripwire** (#4) | classify attack from watermark destruction manifold | fragile watermarking + ML manipulation-type classification (Nature Sci Rep 2025) | manipulation-type classification from watermark distortion already done |
| **Sensor-physics capture attestation** (#3) | multi-channel physics consistency | PRNU deepfake detection; IMU/rolling-shutter fusion; C2PA hw signing; TEE attestation | combination of known building blocks |
| **PQ forensic-graph time-sealing** (#10) | graph-state historical provability | PQ audit evidence (2512.00110); PAdES; append-only accumulators | combination; dependent-claim enhancer at best |
| **ZK-provenance verdict** (Round 3) | privacy + verifiability + minimal witness | zkML; ZKGraph; DARPA SIEVE; abductive AXp; P3GNN | obvious combination; only novel variant (cardinality-minimality in ZK) is infeasible |
| Portable pre-action agent proof (#9) | verifiable agent authorization | Proof-of-Guardrail; VET; CVA | anticipated |
| Generic "tamper-evident AI decision ledger" | signed replayable decisions | AuditableLLM; AuditWeave; Proof-of-Execution | anticipated/crowded |

**Crowded clusters to avoid re-entering under new names:** verifiable/replayable/attested security-AI *decisions*; counterfactual attribution for agents/IDS; tool-verified LLM claims; ZK-verifiable ML inference; blockchain/hash-chain chain-of-custody; C2PA-style capture provenance.

---

## 15. Final recommendation

**Do not build the ZK-provenance mechanism as specified.** It is a predictable composition of zkML + ZKGraph + abductive minimal explanations + the DARPA-SIEVE security-ZK motivation, all pre-existing. The single element that would distinguish it (a succinct ZK proof of *cardinality*-minimality of the witness) is a **co-NP cryptography research problem that is likely infeasible** at scale and cannot currently anchor a working prototype or an enabled claim.

If anyone still wants to touch this space, the *only* defensible move is to treat **"succinct/efficient ZK certificates of minimality (MUS/MCS-style) for graph-structured predicates"** as a **pure cryptography research question**, pursued by a proof-systems specialist, decoupled from the security-product framing — and to fund a 2-week feasibility spike *before* anything else. That is a research bet, not a patent play.

**Because the ZK hypothesis fails, per Phase 18 the honest next step is fresh white-space discovery, not another superficial feature bolt-on.** Candidate directions *not yet stress-tested to exhaustion* in Rounds 1–3 (offered as leads for a Round 4, each still requiring the same defense-first gauntlet): forensic integrity/provenance of **AI-agent-generated** evidence and actions (distinct from attribution); **anti-forensics against AI evidence** (detecting AI-fabricated *logs/telemetry*, not media); post-quantum **long-term** evidence at the graph level; hardware/TEE-rooted **syscall-time** provenance authenticity. I am **not** endorsing any of these yet — they are unexamined.

---

## 16. Final verdict statement (per the absolute rule)

> *I attempted to invalidate the ZK-provenance hypothesis. I found that every constituent
> element and the integrating motivation are disclosed in non-patent prior art, and that the
> broad mechanism is a predictable (likely obvious) combination; the one genuinely
> under-explored variant — a zero-knowledge proof of cardinality-minimality of the witness — is
> a co-NP statement that current succinct proof systems cannot practically prove, so it fails on
> feasibility rather than surviving on novelty. This is a **potentially-obvious combination, not a
> potentially-patentable novelty hypothesis**, subject to professional patent examination and
> subject to the fact that no patent full-text could be retrieved in this environment.*

**Verdict: C — ZK HYPOTHESIS IS LIKELY OBVIOUS. Do not build as specified.**

---

## 17. The two final questions

**"If I spend the next six months developing this, what is the single biggest reason I could later discover I wasted them?"**
That a patent examiner (or a 2026 paper/patent I could not access from this environment) treats the whole thing as one obvious §103 combination — because zkML, ZKGraph, DARPA SIEVE, abductive minimal explanations, and privacy-preserving PIDS (P3GNN) all already exist and the "verify-without-revealing" motivation is explicitly documented — and rejects it for lack of inventive step; **or**, if you instead bet everything on the one non-obvious element (cardinality-minimality in ZK), you discover after months of cryptography engineering that proving it is computationally intractable at provenance-graph scale, so you can never demonstrate the very feature that distinguishes the invention. Either way the distinguishing feature evaporates — one on novelty, the other on feasibility.

**"What evidence would I need TODAY to reduce that risk enough to justify continuing?"**
Three things, in order, any one of which can kill it cheaply: **(1)** a **professional full-text patent + IACR/USENIX literature search** (the step this environment structurally cannot perform) specifically over "verifiable/ZK intrusion detection," "ZK proof of ML inference over graphs," and "ZK proof of minimality/minimal unsat core" — if a 2025–2026 reference already integrates these, the idea is dead; **(2)** a **2-week cryptographic feasibility spike** measuring proving time / proof size / memory for a *subset*-minimality proof over a toy committed GNN on one DARPA OpTC scenario, and an honest attempt at *cardinality*-minimality at ≤10 nodes — if even the toy case is impractical, stop; **(3)** a **written inventive-step opinion** from a patent attorney on whether "zkML applied to PIDS with a minimal witness" clears §103 given the references in §9. Do not write a line of production code until (1) and (3) come back non-fatal and (2) shows the distinguishing feature is actually provable.

> All conclusions are **novelty/obviousness hypotheses requiring professional patent examination.** No claim of (un)patentability is made with certainty. Patent references are `UNVERIFIED — FULL TEXT NOT AVAILABLE`. Absence of a found reference has **not** been treated as evidence of novelty.
