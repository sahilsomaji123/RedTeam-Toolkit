# Discovery of High-Potential Patentable Ideas in AI, Cybersecurity & Cyber Forensics

**A defense-first R&D and prior-art strategy report**

Prepared as an R&D strategist / patent-researcher / cybersecurity & AI research exercise.
Compiled: 2026-08-21.

> **Scope of confidence and honesty statement.** Nothing in this report is a legal opinion.
> No idea here is claimed to be *definitely patentable*. Everything is framed as a
> **novelty hypothesis** that **requires a professional freedom-to-operate (FTO) and
> patentability search by a registered patent attorney/agent** before any filing decision.
> Every patent, paper, product, and company named below was surfaced through live web
> search and is cited with a URL. Where I could not open the primary document, I say so
> explicitly rather than assert its contents.
>
> **Environment limitation (disclosed per the task's "do not confuse *not found* with
> *does not exist*" rule):** In this research environment, direct fetches to
> `patents.google.com` were blocked by the network egress proxy. Patent numbers, titles,
> and one-line summaries below therefore come from search-result metadata and secondary
> sources, **not** from reading the full patent text. Any patent cited as "closest prior
> art" MUST be pulled and read in full (claims + file wrapper) during professional search.
> Absence of a blocking patent in my search is **not** evidence that none exists.

---

## Table of contents

1. Technology landscape (Phase 1)
2. Major research gaps (Phase 3)
3. Major market gaps (Phase 4)
4. Patent landscape (Phase 2)
5. 24 initial invention candidates (Phase 5)
6. Candidate elimination analysis (Phases 6 & 8)
7. TOP 8 surviving candidates — full detail (Phase 9)
8. Detailed prior-art comparison & novelty/obviousness stress test (Phases 6, 7, 10)
9. Patent-claim opportunities
10. TOP 3 recommendations (Phase 11)
11. The ONE to prototype first + Recommended Next Action

---

## 1. Technology landscape (Phase 1)

Focused on ~2020–2026 developments, with older foundational prior art noted.

### 1.1 AI / Generative AI
- LLM agents and multi-agent systems are moving from chat into **tool-calling autonomy**, which creates a new security surface: agents that *take actions*. A wave of 2025–2026 work tries to make agent actions **authorizable and verifiable** rather than trusted-by-default — e.g., *Cryptographically Verifiable Agent Authorization* ([arXiv 2607.21325](https://arxiv.org/abs/2607.21325v1)), *VET Your Agent: Host-Independent Autonomy via Verifiable Execution Traces* ([arXiv 2512.15892](https://arxiv.org/pdf/2512.15892)), and *Proof-of-Guardrail* using TEEs + remote attestation ([arXiv 2603.05786](https://arxiv.org/pdf/2603.05786)).
- **Content provenance** for generative media matured: **C2PA** reached v2.2 (May 2025, video) and v2.3 (Dec 2025, live-stream CMAF segment signing), with hardware capture-time signing shipping in cameras from Sony/Canon/Nikon/Leica/Samsung ([SoftwareSeni C2PA overview](https://www.softwareseni.com/how-c2pa-content-credentials-work-and-what-their-limits-are/)). **Crucially, C2PA does not detect deepfakes — it records a signer's *assertion*, whose truth depends on the signer.**

### 1.2 Cybersecurity
- **Provenance-based intrusion detection (PIDS)** using GNNs on kernel-audit provenance graphs is the leading academic thread for APT detection: FLASH ([DartLab PDF](https://dartlab.org/assets/pdf/flash.pdf)), CONTINUUM ([arXiv 2501.02981](https://arxiv.org/pdf/2501.02981)), Marlin ([arXiv 2403.12541](https://arxiv.org/pdf/2403.12541)), P3GNN ([arXiv 2406.12003](https://arxiv.org/pdf/2406.12003)). Persistent, admitted weaknesses: **high false-positive rates, weak/untrustworthy explanations, and vulnerability to graph-manipulation evasion** (MirGuard, [arXiv 2508.10639](https://arxiv.org/pdf/2508.10639); reproducibility concerns, [SRI/ACM REP 2025](https://dl.acm.org/doi/10.1145/3736731.3746140)).
- **AI-augmented SOC**: LLMs applied to alert triage, threat hunting, and IR ([MDPI survey](https://www.mdpi.com/2624-800X/5/4/95)). Verification of LLM dispositions is an open problem — SOCpilot verifies *policy compliance* for LLM-assisted IR ([arXiv 2605.05501](https://arxiv.org/html/2605.05501)); AIR adds an agent-safety incident-response loop ([arXiv 2602.11749](https://arxiv.org/html/2602.11749v2)).
- **LLM security** itself: prompt injection is now the top agent risk (survey, [MDPI Information 17(1):54](https://www.mdpi.com/2078-2489/17/1/54)); early detection via semantic analysis is being patented (US20250209208A1, below).

### 1.3 Cyber / Digital Forensics
- **Chain-of-custody (CoC)** is being re-thought for the AI era. Blockchain CoC (Forensic-Chain on Hyperledger, [ResearchGate](https://www.researchgate.net/publication/330303837_Forensic-chain_Blockchain_based_digital_forensics_chain_of_custody_with_PoC_in_Hyperledger_Composer)) provides immutable event logs; a 2024 IEEE TPS survey catalogues the state of the art ([PDF](https://jjbaek35.github.io/papers/tps2024.pdf)).
- **LLMs in DF**: capabilities/limits survey ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2666281725001830)); memory-forensics triage (DFIR-Chain, Volatility3 + YARA + Mistral-7B; [ACM Digital Threats](https://dl.acm.org/doi/full/10.1145/3748263)); transformer memory reverse-engineering (~97% behavior reconstruction, [Computers 15(1):8](https://doi.org/10.3390/computers15010008)); LLM-driven provenance forensics with bounded SQL generation ([arXiv 2508.21323](https://arxiv.org/html/2508.21323v1)).
- **Anti-forensics / counter-forensics** with GANs and adversarial perturbations is a fast-moving arms race that directly attacks the ML detectors used in forensics ([Springer review](https://www.sciencedirect.com/science/article/abs/pii/S1566253525011820); anti-forensics survey, [arXiv 2408.11365](https://arxiv.org/pdf/2408.11365)).

### 1.4 Cryptography / Post-Quantum
- NIST finalized **ML-KEM, ML-DSA, SLH-DSA** (Aug 2024). Long-term **evidence** integrity is an emerging niche: PQ audit evidence for long-lived regulated systems ([arXiv 2512.00110](https://arxiv.org/pdf/2512.00110)), PQ integrity verification architectures ([arXiv 2601.11095](https://arxiv.org/pdf/2601.11095)), PAdES-style periodic re-timestamping.

### 1.5 Privacy / Confidential computing
- **ZKPs for forensics/evidence**: privacy-preserving evidence submission and verification without disclosing content (whistleblower framework, [MDPI](https://www.mdpi.com/2813-5288/3/2/7); AI-enhanced ZKP cloud forensics, [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1084804525002280)).
- **TEE remote attestation** matured (IETF RATS EAT, combined TPM+TEE attestation, [CNCF 2025](https://www.cncf.io/blog/2025/10/08/a-tpm-based-combined-remote-attestation-method-for-confidential-computing/)).

### Where the landscape is hot *and* unsolved
Rapidly developing, commercially valuable, still expert-dependent, error-prone, and manipulation-prone: **(a) PIDS false positives + explanation trust + evasion robustness; (b) forensic soundness of AI-derived conclusions (nothing today lets a court re-verify an AI detector's output as evidence); (c) integrity of evidence against AI-powered anti-forensics; (d) verifiability of autonomous agent security actions.** These four are the spine of the candidates below.

---

## 2. Major research gaps (Phase 3)

Extracted from "limitation / future work / open problem" statements in the literature above. Each is annotated as a *technical* opportunity (T) or merely an engineering/adoption gap (E — generally **not** patentable on its own).

| # | Gap (as stated in literature) | Source thread | Type |
|---|---|---|---|
| G1 | PIDS have **high false positives** and analysts cannot trust the explanation | FLASH, PROVEXPLAINER, MirGuard | **T** |
| G2 | PIDS are **evadable by graph-manipulation** that preserves benign-looking structure | MirGuard [2508.10639] | **T** |
| G3 | AI/ML forensic conclusions are **not independently re-verifiable** by a court/opposing expert | DF-LLM survey; CoC survey | **T** |
| G4 | Anti-forensic GANs remove/forge traces faster than detectors adapt; detectors are **tailored to one attack** | anti-forensics survey [2408.11365] | **T** |
| G5 | C2PA/provenance **records assertions, not truth**; no binding to *what actually happened at the sensor* under adversarial conditions | C2PA limits | **T** (partial) |
| G6 | LLM forensic/IR outputs **hallucinate**; no ground-truth-anchored self-verification at inference time | DFIR triage; AIR; SOCpilot | **T** |
| G7 | Agent security actions lack **portable, host-independent proof** that policy was enforced *before* the action | Proof-of-Guardrail; VET | **T** |
| G8 | Long-term **evidence** integrity is not quantum-safe; re-timestamping schemes are document-centric, not *forensic-graph*-centric | PQ audit evidence [2512.00110] | **T** (partial) |
| G9 | No standard way to do **privacy-minimized disclosure** of a forensic finding (prove a detection without revealing the whole corpus) | ZKP forensics | **T** |
| G10 | Tamper-evident AI audit ledgers exist but are **generic**; they log the *decision*, not a *deterministically replayable* detector state | AuditableLLM, AuditWeave, Proof-of-Execution | E→T only if replay is the claim |

---

## 3. Major market gaps (Phase 4)

Where users still do manual work, tools don't integrate, or output can't be trusted — and *why it hasn't been solved*.

- **DFIR analysts manually correlate** across EDR, SIEM, disk images, memory dumps, and cloud logs; timelines are hand-built. *Why unsolved:* correlation that is *court-defensible* requires provenance the tools don't emit, so automation loses admissibility.
- **AI SOC output can't be independently verified**; SOC leads distrust auto-close. *Why unsolved:* verifying an LLM disposition normally means re-running the same fallible LLM; there is no cheaper deterministic oracle.
- **Deepfake objections now threaten *all* digital evidence** (proposed U.S. FRE 707, not effective before Dec 2027; EU AI Act Art. 50). Products issue "provenance certificates" ([ProofSnap](https://getproofsnap.com/posts/deepfake-evidence-provenance-certificate-fre-707-2026.html)) but these attest *capture conditions*, not sensor-level authenticity under attack. *Why unsolved:* C2PA signs an assertion; a lying/compromised signer breaks it.
- **PIDS aren't deployed** in most SOCs despite strong papers. *Why unsolved:* FP rates and unexplained alerts make them operationally unusable; no vendor has fused robustness + explanation + evidence-grade output.
- **Evidence can be manipulated by AI anti-forensics** and defenders have per-attack detectors only. *Why unsolved:* the arms race favors the attacker; there's no attack-agnostic integrity primitive.
- **Multi-tool DFIR still needs a human to glue** memory (Volatility), disk (Autopsy), network (Zeek), and cloud logs; each has its own object model. *Why unsolved:* no shared, verifiable cross-source evidence graph with provenance.

Buyers: MSSPs/MDR providers, enterprise SOCs, DFIR firms, law-enforcement digital-forensics labs, e-discovery/legal-tech, camera/sensor OEMs, regulated industries (finance, healthcare, critical infrastructure), cyber-insurers.

---

## 4. Patent landscape (Phase 2)

**Method:** conceptual + keyword search via public web. **Limitation:** `patents.google.com` was egress-blocked here; the items below come from search metadata/secondary pages and **must be pulled and read in full during professional search.** I distinguish *granted* vs *application* only where the identifier's kind-code or the source made it explicit.

Concrete patent references surfaced (verify each before relying on it):

- **US20250209208A1** — "Early detection of prompt injection attacks using semantic analysis." *Kind code A1 → published application (pending unless later granted).* Surfaced via [search result set](https://www.mdpi.com/2078-2489/17/1/54). Relevant to LLM-security candidates; **not** to forensic-replay candidates.
- **US11847234B2** — "Verifiable training of model in untrusted environment." *Kind code B2 → granted.* Surfaced in the "verifiable ML / blockchain-anchored" search. Anchors prior art for *training* verifiability (distinct from *inference/detection* replay).

Dense, crowded zones (treat as **high FTO risk**, likely non-novel as generic claims):
- Blockchain chain-of-custody for digital evidence (Forensic-Chain and many derivatives).
- Tamper-evident / hash-chained AI audit logging (AuditableLLM, AuditWeave, blockchain-anchored explainable ML, "Proof of Execution").
- TEE/attestation for agent guardrails and agent authorization (Proof-of-Guardrail, CVA, VET).
- GNN/GNNExplainer for IDS explainability (PROVEXPLAINER and many).
- C2PA capture-time signing.

**Implication:** any candidate whose whole story is "put AI decisions on a hash chain," "attest the agent with a TEE," or "blockchain the chain of custody" is **anticipated or obvious.** Survivors must add a *specific new technical mechanism* on top of these building blocks.

---

## 5. Twenty-four initial invention candidates (Phase 5)

Compact form; the 8 survivors get full treatment in §7. Fields per the task are given in condensed rows (Title / Problem / Existing / Limitation / Proposed mechanism / Novelty hypothesis / Main risk / Confidence).

1. **PIDS-DR — Deterministically Replayable Provenance-IDS Verdicts.** *Problem:* PIDS alerts can't be re-verified by a third party (G1,G3). *Existing:* FLASH/CONTINUUM emit a label + soft explanation; audit ledgers log the label. *Limitation:* re-running needs the model + full graph + same environment; not portable, not minimal. *Proposed:* alongside each verdict, emit a **signed "verdict witness"** = the minimal *causally-closed provenance subgraph* + the frozen model fingerprint + a deterministic replay harness, so any party recomputes the identical score offline from the witness alone. *Novelty hypothesis:* the *minimal causally-closed subgraph extraction bound to deterministic re-scoring as the evidentiary object*, not generic logging. *Risk:* AuditableLLM/Proof-of-Execution replay claims. *Confidence:* Medium-High.
2. **Evasion-Aware Provenance Witness.** Extend #1 so the witness includes a **logic-preserving perturbation certificate** proving the verdict is stable under the class of benign graph transformations MirGuard studies (a certified-robustness radius for provenance graphs). *Novelty:* certified-robustness bound *as admissible metadata*. *Risk:* certified-robustness literature (randomized smoothing) may read on it. *Confidence:* Medium.
3. **Sensor-Bound Capture Attestation beyond C2PA.** Bind media authenticity to a **per-frame TEE hash chain of raw sensor readout + IMU + rolling-shutter timing signature** so re-encoding/deepfake substitution breaks a physics-consistency proof, not just a signer assertion (G5). *Novelty:* physics-consistency proof (sensor noise + motion) as the attestation, not a declarative manifest. *Risk:* PRNU/sensor-fingerprint prior art; C2PA hardware signing. *Confidence:* Medium.
4. **Attack-Agnostic Anti-Forensic Tripwire.** Instead of detecting a specific GAN, embed a **fragile, keyed, physically-plausible micro-watermark in acquisition** whose *statistical destruction pattern* identifies *that tampering occurred and of what class* (G4). *Novelty:* using the *destruction signature* (not survival) of a keyed fragile mark to classify anti-forensic operations. *Risk:* fragile watermarking prior art. *Confidence:* Medium.
5. **Cross-Source Verifiable Evidence Graph (CS-VEG).** A shared object model that ingests memory/disk/network/cloud artifacts into one provenance graph where **every edge carries a portable integrity proof and source-tool attestation**, enabling automated but admissible correlation. *Novelty:* per-edge provenance proofs across heterogeneous forensic tools with a merge protocol that preserves admissibility. *Risk:* CASE/UCO forensic ontologies; blockchain CoC. *Confidence:* Medium.
6. **ZK-Minimal Forensic Disclosure.** Prove "artifact X in corpus C matches indicator I / triggered detector D" via ZK **without disclosing the rest of C** (G9), with the proof *bound to* the CoC hash. *Novelty:* ZK statement templated over forensic-graph predicates + CoC binding. *Risk:* ZKP-for-evidence papers already near this. *Confidence:* Medium.
7. **Ground-Truth-Anchored LLM Forensic Verifier.** Wrap an LLM DFIR analyst so each factual claim is **auto-checked against a deterministic oracle** (Volatility psscan ground truth, YARA hit, log query) *before* it enters the report; unverifiable claims are quarantined (G6). *Novelty:* inference-time *claim→oracle binding* with a coverage metric, not post-hoc RAG citation. *Risk:* SOCpilot policy verification; RAG-with-citations. *Confidence:* Medium.
8. **Deterministic Verifier for AI SOC Dispositions.** For each auto-close, synthesize a **cheap deterministic checker** (compiled from the alert's detection logic) that must agree before the LLM disposition is trusted; disagreement escalates. *Novelty:* auto-compiled deterministic disposition oracle from detection rule + telemetry. *Risk:* SOCpilot; ensemble/verifier literature. *Confidence:* Medium.
9. **Portable Pre-Action Authorization Proof for Security Agents.** Emit, before each agent action, a proof that policy was satisfied that is *verifiable off the executing host* and *replayable*. *Overlaps* Proof-of-Guardrail/VET heavily. *Confidence:* Low (likely anticipated).
10. **PQ-Safe Forensic Graph Time-Sealing.** Re-timestamp not documents but the **evolving evidence *graph*** with hash-based PQ signatures + Merkle-over-time so any historical graph state is provable post-quantum (G8). *Novelty:* graph-diff Merkle accumulator with PQ re-sealing cadence tuned to graph mutation. *Risk:* PAdES/PQ audit-evidence; append-only accumulators. *Confidence:* Medium.
11. **Adversarial-Robustness-Certified Malware Memory Classifier.** Transformer memory RE (Computers 15(1):8) but with a **certified-robustness bound against packing/obfuscation transforms** emitted per classification. *Risk:* certified robustness generic. *Confidence:* Low-Medium.
12. **Deepfake-Resistant Interview/Deposition Capture.** Live capture protocol with **challenge-response liveness fused into the provenance chain** (random on-screen nonce reflected in eye/skin response) for legal video. *Risk:* liveness-detection prior art. *Confidence:* Low-Medium.
13. **Explainable PIDS with Counterfactual Provenance Cut.** Explanation = the **minimal set of edges whose removal flips the verdict**, delivered as the analyst-facing and court-facing rationale. *Overlaps* GNNExplainer/counterfactual-XAI. *Confidence:* Low.
14. **Federated PIDS with Verifiable Contribution.** Cross-org PIDS training where each contribution carries a ZK proof of honest computation. *Overlaps* zkFDL/verifiable FL. *Confidence:* Low.
15. **Agentic Threat-Hunt with Bounded, Signed Query Provenance.** Every LLM-generated hunt query is bound to a signed data-scope + result hash for later audit. *Overlaps* LLM-driven provenance forensics [2508.21323]. *Confidence:* Low.
16. **Prompt-Injection Forensic Reconstructor.** Post-incident, reconstruct *which retrieved/tool content injected* an agent, via causal replay over the agent's execution trace. *Novelty:* causal attribution of injection to a specific input span. *Risk:* US20250209208A1 (detection, not forensics) + VET traces. *Confidence:* Medium.
17. **Hardware-Rooted EDR Event Non-Repudiation at the Syscall.** Sign kernel-audit events at emission inside a TEE so the provenance graph is authentic *before* it reaches userspace. *Risk:* trusted-logging/TPM prior art. *Confidence:* Low-Medium.
18. **Confidential-Compute Forensic Enclave for Encrypted-at-Rest Evidence.** Run analysis inside an attested enclave and emit an attestation that the analysis touched only authorized bytes. *Overlaps* confidential-attestation prior art. *Confidence:* Low.
19. **AI-Generated Timeline with Per-Assertion Confidence + Evidence Pointer.** Timeline where each event links to the raw artifact + a calibrated confidence + a replay token. *Overlaps* DFIR-Chain timelines. *Confidence:* Low.
20. **Adaptive Honeytoken Provenance Weaver.** Seed decoy artifacts whose access *automatically* produces a signed provenance edge proving attacker interaction. *Risk:* honeytoken prior art. *Confidence:* Low.
21. **Robustness-Auditing Oracle for Deployed Security ML.** Continuously fuzz a deployed detector with semantics-preserving inputs and emit a signed drift/robustness certificate. *Risk:* ML-monitoring prior art. *Confidence:* Low.
22. **Cross-Modal Deepfake Consistency Prover.** Prove audio/video/lip/room-acoustics mutual consistency as a single verifiable score bound to CoC. *Risk:* multimodal deepfake detection crowded. *Confidence:* Low-Medium.
23. **PQ-Safe Selective-Disclosure Evidence Container.** File format combining redaction-friendly Merkle trees + PQ signatures + ZK redaction proofs for court exhibits. *Risk:* redactable-signature prior art. *Confidence:* Low-Medium.
24. **Detector-Provenance Binding for Model Supply Chain.** Bind each verdict to an attested (model-weights-hash, feature-pipeline-hash, ruleset-hash) tuple so a verdict is reproducible against a *specific* frozen detector build. *Complements* #1; alone it's close to model-cards/SBOM-for-ML. *Confidence:* Low-Medium.

---

## 6. Candidate elimination analysis (Phases 6 & 8)

Applied the five stress tests (single-reference, combination, obviousness, implementation, patent-claim) and scored each 0–10 across the 11 criteria. Overall = mean of the 11 (freedom-to-operate scored so that *high = safer*).

**Killed / downgraded (with the reference that kills or weakens it):**
- **#9** (portable pre-action proof) → *anticipated* by Proof-of-Guardrail + VET; **Reject**.
- **#14, #15, #18, #21** → *combination of two known tools*; obvious. **Reject/Weak.**
- **#13, #19** → thin over GNNExplainer / DFIR-Chain timelines. **Weak.**
- **#11** → certified robustness is generic; applying to memory RE is an obvious application. **Weak.**
- **#20** → honeytoken + signed log = combination. **Weak.**
- **#23, #24** → close to redactable-signature / ML-SBOM; keep as dependent claims, not standalone. **Interesting.**

**Scoreboard (overall /10, classification):**

| # | Candidate (short) | Novelty | Prior-art dist. | Inventive step | Claim potential | Feasibility | Market | FTO safety | Overall | Class |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Replayable Provenance-IDS verdict witness | 8 | 7 | 8 | 8 | 8 | 8 | 6 | **7.6** | 🟢 Strong |
| 2 | Evasion-aware witness (cert. robustness) | 7 | 6 | 7 | 7 | 6 | 7 | 6 | 6.6 | 🟡 |
| 3 | Sensor-physics capture attestation | 7 | 6 | 7 | 7 | 5 | 9 | 5 | 6.6 | 🟡 |
| 4 | Anti-forensic destruction-signature tripwire | 8 | 7 | 7 | 7 | 6 | 7 | 7 | **7.1** | 🟢 Strong |
| 5 | Cross-source verifiable evidence graph | 7 | 6 | 7 | 8 | 6 | 9 | 6 | **7.0** | 🟢 Strong |
| 6 | ZK-minimal forensic disclosure | 7 | 5 | 7 | 7 | 6 | 7 | 5 | 6.3 | 🟡 |
| 7 | Ground-truth-anchored LLM forensic verifier | 7 | 6 | 7 | 8 | 8 | 9 | 6 | **7.3** | 🟢 Strong |
| 8 | Deterministic verifier for SOC dispositions | 7 | 6 | 7 | 7 | 8 | 9 | 6 | **7.1** | 🟢 Strong |
| 10 | PQ forensic-graph time-sealing | 7 | 6 | 7 | 7 | 6 | 6 | 7 | 6.6 | 🟡 |
| 16 | Prompt-injection forensic reconstructor | 8 | 7 | 7 | 7 | 7 | 7 | 7 | **7.2** | 🟢 Strong |
| 22 | Cross-modal deepfake consistency prover | 6 | 5 | 6 | 6 | 6 | 8 | 5 | 6.0 | 🟡 |
| — | (all Rejected above) | — | — | — | — | — | — | — | ≤5.5 | 🔴/🟠 |

**TOP 8 survivors (highest defensible novelty × feasibility × market):** #1, #7, #4, #16, #8, #5, #3, #10.
(#2 folds into #1 as a dependent claim.)

---

## 7. TOP 8 surviving candidates — full detail (Phase 9)

### Candidate #1 — Deterministically-Replayable Provenance-IDS Verdict Witness ("Verdict Witness")
- **One-line concept.** A provenance-based intrusion detector that, with every alert, emits a compact cryptographically-signed *witness* — the minimal causally-closed provenance subgraph plus a frozen detector fingerprint and deterministic replay recipe — so any independent party can recompute the *identical* verdict offline and use it as tamper-evident, court-defensible evidence.
- **Problem.** PIDS verdicts are neither reproducible by third parties nor admissible; analysts don't trust them (G1) and courts can't verify them (G3).
- **Existing solutions.** FLASH/CONTINUUM/Marlin produce a label + soft explanation; AuditableLLM/AuditWeave/Proof-of-Execution hash-chain the *decision*; blockchain CoC seals evidence *files*.
- **Closest prior art.** Proof-of-Execution ([arXiv 2607.05397](https://arxiv.org/html/2607.05397)) (binds authorization+effect+replay for *agent actions*, not detector verdicts); AuditableLLM ([MDPI Electronics 15(1):56](https://www.mdpi.com/2079-9292/15/1/56)); PROVEXPLAINER ([arXiv 2306.00934](https://arxiv.org/abs/2306.00934)); FLASH.
- **Gap.** No prior art extracts the **minimal causally-closed subgraph that is *sufficient and necessary* to reproduce the score**, binds it to a frozen (weights-hash, feature-pipeline-hash, ruleset-hash) detector build, and packages a deterministic re-scoring harness as the *evidentiary object*. Generic ledgers store the *output*, not a *self-contained recomputation*.
- **Proposed invention.** (a) On alert, compute the *sufficient causal closure* of the triggering nodes via influence tracing over the provenance DAG; (b) canonicalize + hash the subgraph; (c) bind (subgraph-hash ∥ detector-build-hash ∥ input-normalization-seed) into a signed witness with a PQ signature; (d) ship a containerized deterministic replay harness that re-derives the same score bit-for-bit; (e) optional certified-robustness radius (folds in #2).
- **Core novelty (candidate claim spine).** *Minimal causally-closed subgraph extraction + deterministic bitwise-reproducible re-scoring bound into a single signed evidentiary witness.*
- **Architecture.** Provenance collector → GNN/anomaly scorer → **Causal-Closure Extractor** (new) → **Canonicalizer/Hasher** → **Witness Sealer (PQ sign)** → Verifier SDK (independent, offline).
- **Workflow.** Detect → extract minimal causal closure → canonicalize → freeze detector build hashes → sign witness → (any party) replay → recompute → compare score/verdict → accept as evidence.
- **Patentable features (claim elements).** 1) sufficient-causal-closure extraction bound to score reproduction; 2) canonical graph serialization for bitwise replay; 3) tri-hash detector-build binding; 4) deterministic re-scoring harness as evidence; 5) PQ-signed witness; 6) minimality proof (removal of any node changes verdict); 7) certified-robustness annotation; 8) verifier that attests replay determinism.
- **Prior-art risks.** Determinism/replay may be argued obvious over Proof-of-Execution + FLASH; the *minimality/causal-closure* element is the strongest distinguishing feature — pull Proof-of-Execution and any "reproducible ML inference" patents.
- **Market.** MDR/MSSP, enterprise SOC, DFIR, law enforcement, cyber-insurance (verifiable claims).
- **Research potential.** High — "reproducible, court-admissible PIDS verdicts" is a publishable systems + security contribution with measurable determinism + witness-size metrics.
- **Prototype feasibility.** Build on an open PIDS (FLASH-style) + DARPA Transparent Computing / OpTC datasets; implement causal-closure via backward taint over the DAG; determinism via fixed-seed, pinned-container inference; ML-DSA signatures via liboqs. **~3–4 months for a demonstrable PoC.**
- **Score.** Novelty 8 / Prior-art distance 7 / Inventive step 8 / Claim potential 8 / Feasibility 8 / Market demand 8 / Commercial 8 / Research 8 / Impl. difficulty 6 (harder=lower) / Competition 7 / FTO safety 6 → **Overall ≈ 7.6 🟢**.

### Candidate #7 — Ground-Truth-Anchored LLM Forensic Verifier ("Oracle-Gated DFIR")
- **One-line concept.** An LLM DFIR reporter where every factual assertion must pass a *deterministic forensic oracle* (e.g., Volatility3 `psscan`, YARA, a bounded log query) at inference time before it may appear in the report; unverifiable claims are quarantined with a coverage score.
- **Problem.** LLM DFIR output hallucinates; nothing binds each claim to reproducible ground truth (G6). Analysts must re-verify manually, erasing the time savings.
- **Existing.** DFIR-Chain (LLM summarization over Volatility/YARA, no per-claim gating); SOCpilot (verifies *policy compliance*, not *factual* claims); RAG-with-citations (retrieval ≠ verification).
- **Closest prior art.** DFIR-Chain / LLMs-for-memory-forensics ([ACM Digital Threats 3748263](https://dl.acm.org/doi/full/10.1145/3748263)); SOCpilot ([arXiv 2605.05501](https://arxiv.org/html/2605.05501)); LLM-driven provenance forensics ([arXiv 2508.21323](https://arxiv.org/html/2508.21323v1)).
- **Gap.** No prior art performs **claim-level decomposition → automatic mapping of each atomic claim to a deterministic forensic oracle query → gate-before-emit → signed coverage certificate** over the finished report.
- **Core novelty.** *Inference-time atomic-claim-to-forensic-oracle binding with emit-gating and a signed verification-coverage certificate.*
- **Architecture.** LLM analyst → Claim Decomposer → Oracle Router (maps claim type → tool + bounded query) → Deterministic Oracles (Volatility/YARA/log) → Gate → Report + Coverage Certificate.
- **Workflow.** Draft claim → decompose → route to oracle → run → verified? emit + cite reproducible query : quarantine → compute coverage → sign.
- **Patentable features.** 1) atomic-claim decomposition schema for forensic assertions; 2) claim-type→oracle routing; 3) emit-gate on deterministic pass; 4) reproducible query token embedded per claim; 5) coverage certificate (verified/total) signed; 6) quarantine channel; 7) binding of certificate to evidence CoC hash.
- **Prior-art risks.** "Tool-verified LLM" is a rising pattern; strongest distinguisher is *forensic-oracle routing + emit-gate + coverage certificate as an admissibility artifact*.
- **Market.** DFIR firms, LE forensic labs, e-discovery, IR retainers, SOC L1 automation.
- **Research potential.** High — measurable hallucination-elimination + coverage; strong venue fit (DFRWS, USENIX).
- **Prototype feasibility.** Volatility3 + YARA + an LLM; datasets: BCCC-MalMem-SnapLog-2025 (has ground truth). **~2–3 months.**
- **Score → Overall ≈ 7.3 🟢.**

### Candidate #4 — Attack-Agnostic Anti-Forensic Tripwire ("Destruction-Signature Watermark")
- **One-line concept.** Embed a keyed, physically-plausible *fragile* micro-pattern at acquisition whose **manner of destruction** (not survival) is a classifier input, so *any* anti-forensic operation — even an unseen GAN — reveals *that* tampering occurred and *which class* of operation caused it.
- **Problem.** Anti-forensic GANs/adversarial edits defeat detectors that are each trained for one attack (G4); defenders are always a step behind.
- **Existing.** Fragile watermarking (detects *that* an image changed); per-attack anti-forensic detectors; PRNU sensor fingerprints.
- **Closest prior art.** Anti-forensics survey ([arXiv 2408.11365](https://arxiv.org/pdf/2408.11365)); GAN anti-forensics ([Springer](https://link.springer.com/chapter/10.1007/978-981-16-7621-5_17)); trace-removal attack ([arXiv 2203.11433](https://arxiv.org/pdf/2203.11433)).
- **Gap.** Classical fragile marks give a binary "altered/not." No prior art uses the **structured, keyed *destruction pattern* of an acquisition-time mark as a discriminative signature to *classify the anti-forensic operation type* attack-agnostically**, with a keyed proof so an adversary can't forge a "clean" destruction pattern.
- **Core novelty.** *Keyed acquisition watermark engineered so its degradation manifold maps injectively to classes of post-hoc manipulation; classifier operates on the destruction residual, not the survived mark.*
- **Architecture.** Acquisition SDK (embed keyed mark tied to sensor model) → at examination: key-gated extraction of *residual/destruction field* → Destruction-Signature Classifier → tamper-class + confidence bound to CoC.
- **Workflow.** Embed at capture → suspect processing → extract destruction field with secret key → classify operation family → attach signed finding.
- **Patentable features.** 1) acquisition-time keyed mark with engineered fragility manifold; 2) destruction-field extraction under key; 3) mapping destruction pattern → manipulation class; 4) attack-agnostic training regime over transformation families; 5) unforgeability from key-gating; 6) binding to CoC; 7) sensor-model-specific embedding.
- **Prior-art risks.** Fragile watermarking + tamper-localization is a mature field; must show *classification of operation type from destruction structure* is not disclosed. Requires embedding at capture (adoption via camera/app SDK).
- **Market.** Camera/sensor OEMs, evidentiary-camera vendors, insurance claim imaging, journalism, legal video.
- **Research potential.** High and clean experimental story.
- **Prototype feasibility.** Simulate with a watermark embedder + battery of manipulations (JPEG, GAN inpainting, diffusion edit, median filter) + a classifier over the residual. **~3 months.**
- **Score → Overall ≈ 7.1 🟢.**

### Candidate #16 — Prompt-Injection Forensic Reconstructor
- **One-line concept.** Post-incident, deterministically replay an AI agent's execution trace to attribute a compromise to the **specific retrieved/tool-returned input span** that injected it, producing a signed causal-attribution report.
- **Problem.** When an agent is hijacked by prompt injection, responders can't pinpoint *which* content did it or prove it (G6/G7). Detection patents exist; *forensic attribution* does not.
- **Existing.** Prompt-injection detection (US20250209208A1); VET verifiable execution traces (records trace, doesn't attribute causation); injection surveys.
- **Closest prior art.** US20250209208A1 (detection, pre-hoc); VET ([arXiv 2512.15892](https://arxiv.org/pdf/2512.15892)); SCOUT pre-hoc detection ([arXiv 2605.30837](https://arxiv.org/pdf/2605.30837)).
- **Gap.** No prior art does **counterfactual replay over a recorded agent trace to isolate the minimal input span whose removal eliminates the malicious action** and seal that attribution as evidence.
- **Core novelty.** *Counterfactual span-ablation over a deterministic agent trace to produce minimal-cause attribution of an injection, bound to a tamper-evident witness.*
- **Architecture.** Trace recorder (VET-like) → Span Segmenter → Counterfactual Replayer (ablate spans, re-run deterministically) → Minimal-Cause Solver → Signed Attribution Report.
- **Workflow.** Record → segment inputs → ablate + replay → find minimal causal span → sign.
- **Patentable features.** 1) deterministic agent-trace capture for replay; 2) input-span segmentation; 3) counterfactual ablation search for minimal cause; 4) causal-sufficiency test; 5) signed attribution witness; 6) binding to model-build hash.
- **Prior-art risks.** Counterfactual explanation + trace replay could be argued combinable; the *minimal-span injection attribution as forensic evidence* is the distinguisher.
- **Market.** Enterprises deploying agents, AI-security startups, IR firms, model providers.
- **Research potential.** High — first-of-kind agent forensics.
- **Prototype feasibility.** Instrument an open agent framework; deterministic replay via fixed seeds/cached tool outputs; ablation search. **~2–3 months.**
- **Score → Overall ≈ 7.2 🟢.**

### Candidate #8 — Auto-Compiled Deterministic Verifier for AI-SOC Dispositions
- **One-line concept.** For each LLM auto-disposition, *compile a cheap deterministic checker directly from the triggering detection rule + telemetry schema* that must independently agree before the disposition is trusted; disagreement forces escalation.
- **Problem.** Verifying an LLM SOC disposition by re-running an LLM is circular and costly; SOC leads distrust auto-close.
- **Existing.** SOCpilot (policy-compliance verifier); ensembles; human review.
- **Closest prior art.** SOCpilot ([arXiv 2605.05501](https://arxiv.org/html/2605.05501)); AI-augmented SOC survey ([MDPI](https://www.mdpi.com/2624-800X/5/4/95)).
- **Gap.** No prior art **auto-synthesizes a deterministic, detection-rule-derived oracle per alert** to check the LLM's *factual* disposition (vs. policy compliance).
- **Core novelty.** *Compilation of a deterministic disposition-checker from the detection rule's own predicate + telemetry, used as an independent oracle over the LLM verdict.*
- **Architecture.** Detection rule → Rule-to-Checker Compiler → Deterministic Checker → Agreement Gate vs. LLM disposition → escalate/close + signed record.
- **Patentable features.** 1) rule→deterministic-checker compilation; 2) telemetry-schema binding; 3) agreement gate with escalation policy; 4) disagreement-driven active learning; 5) signed disposition record.
- **Prior-art risks.** Detection-as-code + verification is adjacent; distinguisher is *automatic checker synthesis from the rule* as an oracle over the *LLM's* verdict.
- **Market.** SOC/MDR platforms, SOAR vendors.
- **Research potential.** Medium-High.
- **Prototype feasibility.** Sigma rules → compiled checkers over sample telemetry; LLM disposition; agreement metrics. **~2–3 months.**
- **Score → Overall ≈ 7.1 🟢.**

### Candidate #5 — Cross-Source Verifiable Evidence Graph (CS-VEG)
- **One-line concept.** A unified forensic object model where memory, disk, network, and cloud artifacts merge into one provenance graph in which **every edge carries a portable per-edge integrity proof and originating-tool attestation**, enabling automated *and* admissible cross-source correlation.
- **Problem.** DFIR correlation across tools is manual and, when automated, loses admissibility because tools don't emit provenance.
- **Existing.** CASE/UCO forensic ontologies (semantics, not per-edge proofs); blockchain CoC (file-level, not graph-edge-level).
- **Closest prior art.** CASE/UCO; Forensic-Chain ([ResearchGate](https://www.researchgate.net/publication/330303837_Forensic-chain_Blockchain_based_digital_forensics_chain_of_custody_with_PoC_in_Hyperledger_Composer)); CoC survey ([PDF](https://jjbaek35.github.io/papers/tps2024.pdf)).
- **Gap.** No prior art gives **per-edge integrity proofs + tool attestation with a merge protocol that preserves admissibility across heterogeneous sources**.
- **Core novelty.** *Per-edge provenance proof + source-tool remote attestation + admissibility-preserving graph-merge protocol.*
- **Patentable features.** 1) per-edge integrity proof structure; 2) tool-attestation binding; 3) cross-source merge preserving proofs; 4) conflict-resolution with provenance priority; 5) PQ sealing; 6) query interface emitting verifiable sub-evidence.
- **Prior-art risks.** Ontology + blockchain CoC combination is the obviousness threat; the *per-edge proof + attested merge* is the distinguisher.
- **Market.** DFIR platforms (large), LE labs, e-discovery, incident retainers.
- **Research + feasibility.** High market pull; heavier build (**4–6 months** for a two-source PoC: memory + network).
- **Score → Overall ≈ 7.0 🟢.**

### Candidate #3 — Sensor-Physics Capture Attestation (beyond C2PA)
- **One-line concept.** Bind media authenticity to a per-frame TEE hash chain of **raw sensor readout + IMU motion + rolling-shutter timing**, yielding a physics-consistency proof that deepfake substitution or re-encoding breaks — going past C2PA's declarative assertion.
- **Closest prior art.** C2PA hardware signing (assertion-based, [SoftwareSeni](https://www.softwareseni.com/how-c2pa-content-credentials-work-and-what-their-limits-are/)); PRNU sensor fingerprinting; capture-integrity products (ProofSnap).
- **Gap / novelty.** *Cross-checking multiple physical channels (photon-noise statistics, rolling-shutter timing, IMU-motion parallax) for mutual consistency, sealed per-frame in a TEE, so authenticity is a physics proof, not a signer claim.*
- **Risks.** Sensor-fingerprint + secure-capture prior art is substantial; distinguisher is the *multi-physical-channel mutual-consistency proof*. Needs OEM adoption.
- **Market.** Camera/sensor OEMs, evidentiary/bodycam vendors, journalism, insurance. **Overall ≈ 6.6 🟡.**

### Candidate #10 — Post-Quantum Forensic-Graph Time-Sealing
- **One-line concept.** Re-timestamp the *evolving evidence graph* (not documents) using hash-based PQ signatures over a graph-diff Merkle accumulator, so any historical graph state remains provable after quantum computers exist.
- **Closest prior art.** PQ audit-evidence for long-lived systems ([arXiv 2512.00110](https://arxiv.org/pdf/2512.00110)); PAdES long-term signatures; PQ integrity architectures ([arXiv 2601.11095](https://arxiv.org/pdf/2601.11095)).
- **Gap / novelty.** *Graph-diff Merkle accumulator with a PQ re-sealing cadence tuned to graph mutation rate, enabling proof of any past forensic-graph state.* Existing PQ evidence work is document/log-centric, not graph-state-centric.
- **Risks.** Append-only accumulators + PQ signatures are known; distinguisher is *graph-state historical provability with mutation-tuned resealing*. **Overall ≈ 6.6 🟡.**

---

## 8. Prior-art comparison & novelty/obviousness stress test (Phases 6, 7, 10)

For each survivor I play **hostile patent examiner** ("strongest reason this may NOT be patentable"), then state the strongest surviving distinction.

- **#1 Verdict Witness.** *NOT-patentable argument:* obvious to combine FLASH (verdict) + Proof-of-Execution (bind-authorization-effect-replay) + AuditableLLM (hash-chain) — "just make the PIDS output replayable and signed." *Strongest surviving novelty:* the **minimal *causally-closed* subgraph that is provably sufficient-and-necessary to reproduce the score** is a specific technical construct absent from all three; none extract a minimality-certified evidentiary subgraph bound to bitwise re-scoring. **Survives (pending FTO on Proof-of-Execution + reproducible-inference patents).**
- **#7 Oracle-Gated DFIR.** *NOT:* "LLM + tool verification" is trending; DFIR-Chain already pairs Volatility/YARA with an LLM. *Surviving novelty:* **per-atomic-claim emit-gating with an oracle-routing schema and a signed coverage certificate as an admissibility artifact** — DFIR-Chain summarizes *after* the tools; it does not gate each claim or produce a coverage certificate. **Survives.**
- **#4 Destruction-Signature Tripwire.** *NOT:* fragile watermarking + tamper localization is mature. *Surviving novelty:* **classifying the *type* of anti-forensic operation from the *structured destruction residual* of a keyed acquisition mark, attack-agnostically** — prior fragile marks give binary/localized alteration, not operation-class inference from destruction structure. **Survives (novel-mechanism strength; adoption risk).**
- **#16 Injection Reconstructor.** *NOT:* counterfactual explanation + trace replay are each known; combine them. *Surviving novelty:* **minimal-span causal attribution of a prompt injection over a *deterministic agent replay*, sealed as forensic evidence** — detection patents and VET traces neither attribute a minimal causal span nor produce an evidentiary attribution. **Survives.**
- **#8 Auto-Compiled Disposition Verifier.** *NOT:* SOCpilot already verifies LLM IR; detection-as-code exists. *Surviving novelty:* **synthesizing the deterministic checker *from the detection rule's own predicate* to check the LLM's *factual* disposition** (SOCpilot checks *policy*, not factual correctness derived from the rule). **Survives, narrower.**
- **#5 CS-VEG.** *NOT:* CASE/UCO ontology + blockchain CoC → obvious to add integrity to a forensic graph. *Surviving novelty:* **per-edge proof + tool remote attestation + an admissibility-preserving merge protocol** — ontologies model semantics, CoC seals files; neither seals *edges* with tool attestation nor defines an admissibility-preserving merge. **Survives, but heaviest FTO in CoC space.**
- **#3 Sensor-Physics Attestation.** *NOT:* C2PA hardware signing + PRNU. *Surviving novelty:* **multi-physical-channel mutual-consistency proof sealed per frame** vs. single-signer assertion. **Survives conditionally (dense imaging-forensics art).**
- **#10 PQ Graph Time-Sealing.** *NOT:* PQ signatures + Merkle accumulators + PAdES re-timestamping. *Surviving novelty:* **graph-state historical provability with mutation-tuned resealing.** **Survives narrowly; likely a dependent-claim enhancer to #1/#5.**

**White-space verdict (Phase 7).** The richest intersection — *Detect → Investigate → Correlate → Verify → Preserve → Explain → Respond without breaking forensic integrity* — is best hit by **#1 (verify + preserve a detection as evidence)**, **#7 (verify + explain investigative claims)**, and **#16 (investigate + attribute agent compromise)**. These three sit where **research exists + market demand exists + prior art exists but a specific technical gap remains.**

---

## 9. Patent-claim opportunities (illustrative independent-claim spines)

*Illustrative only; not attorney-drafted. Each needs FTO before filing.*

- **#1:** "A method comprising: generating an anomaly verdict from a provenance graph; **extracting a minimal causally-closed subgraph that is sufficient and necessary to reproduce said verdict**; binding a canonical serialization of the subgraph to a tuple of (model-weights hash, feature-pipeline hash, ruleset hash) and a normalization seed; sealing the binding with a post-quantum signature; and providing a deterministic re-scoring harness that recomputes said verdict bitwise from the sealed witness alone."
- **#7:** "…decomposing an LLM-generated forensic report into atomic factual claims; routing each claim by type to a deterministic forensic oracle; **gating emission of each claim on deterministic oracle agreement**; and emitting a signed coverage certificate quantifying verified vs. quarantined claims bound to an evidence chain-of-custody hash."
- **#4:** "…embedding at acquisition a key-dependent fragile pattern whose degradation manifold is engineered to be class-discriminative; extracting, under said key, a destruction-residual field from a query artifact; and **classifying a manipulation-operation type from structural features of said destruction-residual field.**"
- **#16:** "…recording a deterministic execution trace of an AI agent; segmenting agent inputs into spans; **iteratively ablating spans and deterministically replaying** to identify a minimal input span whose removal eliminates a target action; and sealing an attribution witness identifying said span as cause."

---

## 10. TOP 3 recommendations (Phase 11)

**🥇 #1 — Best Patent Opportunity: Candidate #1 (Deterministically-Replayable Provenance-IDS Verdict Witness).**
*Why it survives prior-art analysis:* the **minimal causally-closed, minimality-certified subgraph bound to bitwise-reproducible re-scoring** is a concrete technical construct not disclosed by the closest references (Proof-of-Execution, AuditableLLM, FLASH, PROVEXPLAINER), which store outputs or attest actions rather than package a self-contained recomputation. Strong claim spine, clear infringement read, high commercial pull (verifiable security telemetry for insurance/legal). FTO focus: pull Proof-of-Execution and any "reproducible ML inference / model-provenance verdict" patents.

**🥈 #2 — Best Research + Patent Opportunity: Candidate #7 (Ground-Truth-Anchored LLM Forensic Verifier).**
*Why it survives:* per-claim emit-gating with oracle routing and a signed coverage certificate is a *measurable* hallucination-elimination mechanism (great paper: DFRWS/USENIX) *and* a narrow, concrete claim distinct from DFIR-Chain (post-hoc summarization) and SOCpilot (policy, not fact). Fastest path to both a publication and a filing.

**🥉 #3 — Best Commercial Opportunity: Candidate #16 (Prompt-Injection Forensic Reconstructor).**
*Why it survives:* the agent-security market is exploding and **agent forensics is essentially greenfield**; minimal-span causal attribution over deterministic replay is a first-of-kind capability every enterprise deploying agents will need. Detection patents (US20250209208A1) and VET traces don't attribute cause, leaving room. Strong buyer urgency; moderate build.

---

## 11. The ONE to prototype first + Recommended Next Action

**Prototype FIRST: Candidate #1 — the Verdict Witness.** Rationale: best balance of *defensible novelty × claim clarity × feasibility (open PIDS + public datasets exist) × cross-cutting value* (it also underpins #5 and #10 as dependent claims, and its determinism discipline benefits #7 and #16). It is the cleanest place where **research + market demand + prior art all exist but a specific technical gap (minimality-certified reproducible evidentiary witness) remains.**

### Recommended Next Action — concrete plan for Candidate #1

1. **Professional prior-art / FTO search (weeks 1–3).** Registered patent agent pulls and reads *full text + claims + file wrapper* of: Proof-of-Execution [2607.05397], AuditableLLM (MDPI 15(1):56), US11847234B2 (verifiable training), plus keyword/CPC searches on "reproducible machine-learning inference," "minimal explanatory subgraph," "signed detection evidence," "provenance intrusion detection evidence." **Explicitly resolve any Google Patents access gaps encountered during the initial search.** Deliverable: patentability + FTO memo confirming/refuting the minimality-closure distinction.
2. **Technical specification (weeks 2–4, parallel).** Formalize *sufficient-and-necessary causal closure*, canonical serialization for bitwise determinism, the tri-hash detector-build binding, and the witness/verifier protocol. Define determinism invariants (seeds, container pinning, float determinism).
3. **Architecture (week 4).** Collector → scorer → Causal-Closure Extractor → Canonicalizer/Hasher → PQ Sealer (ML-DSA via liboqs) → offline Verifier SDK.
4. **Prototype (months 2–4).** Implement on an open FLASH-style PIDS over DARPA Transparent Computing / OpTC provenance datasets; backward-taint causal closure; fixed-seed pinned-container inference; witness generation + independent replay verifier.
5. **Experimental validation (months 4–5).** Metrics: witness size vs. full-graph size; **bitwise replay success rate**; verdict-preservation under minimality (removing any closure node flips verdict); robustness annotation vs. MirGuard-style perturbations; verifier runtime. Compare against "log the whole graph" and "hash-chain the label" baselines.
6. **Patent-claim drafting (months 5–6).** Convert the validated minimality-closure + deterministic-replay mechanism into independent + dependent claims (fold #2 certified-robustness and #10 PQ-sealing as dependents); prepare figures from the architecture and workflow.
7. **Filing preparation (month 6).** Provisional application with the working prototype and experimental results as enablement; parallel research paper submission (defensive publication timing coordinated with counsel).

> **Final reminder (Critical Rules).** No idea above is asserted to be patentable. Each is a **novelty hypothesis requiring professional patent examination.** All named patents/papers/products were surfaced via live web search and cited with URLs; none were fabricated. Direct patent-document verification on Google Patents was blocked in this environment and must be completed during step 1. "Not found here" ≠ "does not exist."

---

### Consolidated source list (primary/secondary references cited above)

- Digital Evidence Chain of Custody (IEEE TPS 2024): https://jjbaek35.github.io/papers/tps2024.pdf
- Forensic-Chain (blockchain CoC): https://www.researchgate.net/publication/330303837_Forensic-chain_Blockchain_based_digital_forensics_chain_of_custody_with_PoC_in_Hyperledger_Composer
- C2PA overview & limits: https://www.softwareseni.com/how-c2pa-content-credentials-work-and-what-their-limits-are/
- Cryptographically Verifiable Agent Authorization: https://arxiv.org/abs/2607.21325v1
- VET (Verifiable Execution Traces): https://arxiv.org/pdf/2512.15892
- Proof-of-Guardrail (TEE attestation): https://arxiv.org/pdf/2603.05786
- Proof of Execution (runtime verification for agent actions): https://arxiv.org/html/2607.05397
- AuditableLLM (hash-chain audit): https://www.mdpi.com/2079-9292/15/1/56
- AuditWeave (tamper-evident evidence layer): https://arxiv.org/html/2607.09682v1
- FLASH (PIDS): https://dartlab.org/assets/pdf/flash.pdf
- CONTINUUM (spatio-temporal GNN APT): https://arxiv.org/pdf/2501.02981
- Marlin (knowledge-driven provenance analysis): https://arxiv.org/pdf/2403.12541
- P3GNN (privacy-preserving provenance APT): https://arxiv.org/pdf/2406.12003
- MirGuard (robust PIDS vs graph manipulation): https://arxiv.org/pdf/2508.10639
- PROVEXPLAINER / interpreting GNN-IDS: https://arxiv.org/abs/2306.00934
- Reproducibility of PIDS (ACM REP 2025): https://dl.acm.org/doi/10.1145/3736731.3746140
- Anti-forensics research survey: https://arxiv.org/pdf/2408.11365
- GAN anti-forensic attacks: https://link.springer.com/chapter/10.1007/978-981-16-7621-5_17
- Trace-removal attack on deepfake detection: https://arxiv.org/pdf/2203.11433
- LLMs in digital forensics (survey): https://www.sciencedirect.com/science/article/pii/S2666281725001830
- LLMs for memory forensics (ACM Digital Threats): https://dl.acm.org/doi/full/10.1145/3748263
- Transformer memory reverse engineering: https://doi.org/10.3390/computers15010008
- LLM-driven provenance forensics: https://arxiv.org/html/2508.21323v1
- AI-augmented SOC (survey): https://www.mdpi.com/2624-800X/5/4/95
- SOCpilot (policy-compliance verification for LLM IR): https://arxiv.org/html/2605.05501
- AIR (agent safety via incident response): https://arxiv.org/html/2602.11749v2
- Prompt-injection survey: https://www.mdpi.com/2078-2489/17/1/54
- SCOUT (pre-hoc injection defense): https://arxiv.org/pdf/2605.30837
- PQ audit evidence for long-lived systems: https://arxiv.org/pdf/2512.00110
- PQ integrity verification architectures: https://arxiv.org/pdf/2601.11095
- ZKP evidence (whistleblower framework): https://www.mdpi.com/2813-5288/3/2/7
- AI-enhanced ZKP cloud forensics: https://www.sciencedirect.com/science/article/abs/pii/S1084804525002280
- Deepfake evidence & FRE 707 (secondary): https://getproofsnap.com/posts/deepfake-evidence-provenance-certificate-fre-707-2026.html
- Patent (application) US20250209208A1 — prompt-injection semantic detection (verify on retrieval)
- Patent (granted) US11847234B2 — verifiable training in untrusted environment (verify on retrieval)
