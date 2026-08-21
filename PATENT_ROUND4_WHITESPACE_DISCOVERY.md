# Round 4 — Deep White-Space Discovery (AI × Cybersecurity × Forensics)

**Companion to the Round 1–3 reports.** Date: 2026-08-21. Posture: **defense-first, evidence-first. A winner was not forced.**

---

## Final Decision

> ## 🟡 PROMISING BUT REQUIRES ATTORNEY / DEEPER RESEARCH — for exactly **one** narrow candidate.
>
> **No candidate reached a clean 🟢.** Three of the four priority white spaces are already
> crowded or being standardized as of mid-2026. The single direction that survived to 🟡 —
> *cryptographic omission-bounding of endpoint telemetry by reconciling a minimal-TCB external
> observer against the untrusted host log* — addresses a problem the field **openly admits is
> unsolved**, but it sits on a fast-moving, contested frontier where every constituent building
> block already exists, so its **research value clearly exceeds its patent value**, and its
> patentability depends entirely on confining the novelty to one specific reconciliation-proof
> mechanism. This is a *feasibility-spike* recommendation, **not** a build recommendation.

**Per-area status:**

| White space | Status | One-line reason |
|---|---|---|
| **A — AI-agent-generated evidence provenance** | 🔴 CROWDED / DEAD | Being standardized (IETF SCITT "Agent Action Capsule"); AgentBound, hardware-rooted RATS agent-evidence, signed-provenance products all 2026 |
| **B — AI-fabricated / omitted logs & telemetry** | 🟡 (best area) | Cross-source consistency (the natural defense) is being defeated by causal synthetic-log generators; *completeness/omission* proofs are an admitted gap — but a contested one |
| **C — Graph-level post-quantum evidence** | 🟠 LIKELY OBVIOUS | Core solved (Q-Audit defs + Merkle-anchor + hybrid sigs, arXiv 2512.00110); DAG selective-resign flagged as an "emerging direction" others already name |
| **D — Syscall-time TEE-rooted provenance** | 🔴 / 🟠 | Integrity-at-source fully worked: Custos, Nitro (CCS'25, fine-grained), EmLog, HardLog, **patent US12524535 "unforgeable telemetry / TEFTI"** targets suppression/forged counts |

**Standing limitation (unchanged, Rounds 2–4):** every patent database and arXiv/Crossref direct-fetch return HTTP 403 under this session's egress policy. **All patents are `UNVERIFIED — FULL TEXT NOT AVAILABLE`**, used only as corroboration. Absence of a found reference is **not** treated as evidence of novelty.

---

## 1. Landscape & the "impossible triangle" per area (Parts 5–7, 12)

### White Space A — agent-generated evidence provenance → 🔴
The exact idea is being built and standardized in 2026:
- **AgentBound** — "cryptographically verifiable governance receipts that bind every action to the exact delegation, policy, and semantic artifacts… enabling independent replay verification." [arXiv 2606.30970](https://arxiv.org/abs/2606.30970v1)
- **Hardware-rooted attestation for AI-agent evidence: composing IETF RATS with action evidence packages.** [arXiv 2608.00801](https://arxiv.org/html/2608.00801v1)
- **IETF SCITT "Agent Action Capsule"** — binds per-action authorization + memory provenance. [datatracker draft](https://datatracker.ietf.org/doc/html/draft-rampalli-scitt-capsule-provenance-binding-00)
- "Explanation-Bound Tool Execution" (server-verified action claims) [arXiv 2607.25364]; "From Agent Traces to Trust" [arXiv 2606.04990]; commercial signed-provenance (Zylos).
**Negative space closed:** "raw logs are insufficient → capture semantic relationships, cryptographically anchored" is already the community answer. No defensible mechanism remains.

### White Space B — fabricated / omitted telemetry → 🟡 (the live frontier)
- **Offense outpacing the natural defense:** **EvidenceForge** (Cisco Talos, May 2026) and **Microsoft's AI synthetic-attack-log pipeline** (May 2026) generate *causally-ordered, cross-source-synchronized* synthetic logs across 20+ formats — explicitly defeating the classic tell ("independent emitters that don't share state; you see the seams when you cross-reference"). [Talos](https://blog.talosintelligence.com/introducing-evidenceforge-synthetic-security-logs-that-dont-look-as-fake/); [Microsoft](https://www.microsoft.com/en-us/security/blog/2026/05/12/accelerating-detection-engineering-using-ai-assisted-synthetic-attack-logs-generation/)
- **The admitted gap:** IETF "Verifiable Telemetry Ledgers" states a successful verification "**does not by itself establish dataset completeness**." [datatracker](https://datatracker.ietf.org/doc/draft-elkhatabi-verifiable-telemetry-ledgers/). "Proving complete absence of suppressed events across independent vantage points remains a recognized limitation." "Proving no events were omitted requires Merkle trees" — which structurally **cannot** cover events the attacker prevented from ever being recorded.
- **But the frontier is contested:** "Towards Verifiable Network Telemetry without Special-Purpose Hardware" (HotNets 2025) [PDF](https://conferences.sigcomm.org/hotnets/2025/papers/hotnets25-final97.pdf); ZK-over-NetFlow verifiable telemetry.
- **Impossible triangle (real):** *real-time* × *high-volume* × *unforgeable completeness*, when **the endpoint's own (compromised) TCB is the collector**. Existing systems buy two by sacrificing the third.

### White Space C — post-quantum evidence graphs → 🟠
- Solved core: **Q-Audit Integrity / Q-Non-Equivocation / Q-Binding** definitions + Merkle-root anchoring + hybrid (classical+PQ) signatures + PQ signing at 5,000 sig/s. [arXiv 2512.00110](https://arxiv.org/abs/2512.00110)
- Residual "emerging direction" (already named by that literature): extending linkage to **DAG-based provenance graphs** with **dependency-aware selective re-signing**. Ingredients (Merkle transparency logs, skip-lists, hybrid sigs, LTV) all known → obvious-combination risk.

### White Space D — syscall-time TEE-rooted provenance → 🔴/🟠
- **Integrity at source is a mature, competitive field:** **Custos** (TEE tamper-evident auditing), **Nitro / "Rethinking Tamper-Evident Logging"** (CCS 2025 — *fine-grained* detection, no kernel recompile, closing Custos's coarse-grained gap) [arXiv 2509.03821](https://arxiv.org/html/2509.03821v1), **EmLog** (TrustZone log protection at source), **HardLog** (15-s protection window), **eAudit**.
- **Patent US12524535 "unforgeable telemetry in the presence of cyberattacks (TEFTI)"** — probe instructions that "cannot be modified after loading," resisting attempts to "suppress or forge event counts." `UNVERIFIED` but a direct hit on the anti-suppression mechanism.
- **VMI vantage point is old** (Garfinkel–Rosenblum 2003; patents US10944764, US9619346, US8789189): observing a compromised guest "from outside the VM" is not novel.
**Negative space:** the residual is *selective mid-stream suppression by a kernel attacker who unhooks the probe before it counts* — but TEFTI + Nitro + PillarBox's gap-checker contest exactly this.

---

## 2. The 30 candidates and immediate-kill results (Parts 8–9)

Per the task's own principle ("the goal is not to produce many attractive ideas"), most are dispatched by the Part-9 immediate-kill filter in one line. Only survivors get deeper treatment (§3–4).

**White Space A (8):**
1. Agent action capsule w/ per-tool signed receipt — 🔴 = IETF SCITT Agent Action Capsule.
2. Hardware-rooted agent evidence attestation — 🔴 = arXiv 2608.00801 (RATS + action evidence).
3. Cross-agent evidence hand-off provenance — 🔴 = AgentBound delegation binding.
4. Replay-verifiable agent governance receipt — 🔴 = AgentBound replay.
5. Semantic (not chronological) agent provenance graph — 🔴 = "From Agent Traces to Trust."
6. Memory-provenance binding for agent actions — 🔴 = SCITT capsule memory-provenance.
7. Server-verified action claims w/o trusting rationale — 🔴 = Explanation-Bound Tool Execution.
8. Agent identity + signed runtime audit trail — 🔴 = commercial (Zylos) + generic signing.

**White Space B (8):**
9. Classifier for AI-generated logs — 🔴 Part-9 ("generic classification"); adversarially defeatable.
10. Telemetry **microtiming/IET fingerprint** (real vs synthetic) — 🟠 known phenomenon (fraud/Tor/minutiae) + classifier + adversarially learnable.
11. Watermark host-generated events at source — 🟠 = source watermarking + EmLog-style at-source binding; if you can bind at source you don't need to detect fabrication.
12. Cross-source causal-consistency checker — 🔴 directly defeated by EvidenceForge/MS causal generators.
13. **Cross-vantage cryptographic omission-bounding** (reconcile minimal-TCB observer vs host log to *prove* a lower bound on suppressed events) — **🟡 SURVIVES to §4** (novelty must be confined to the reconciliation proof).
14. Replay-attack detection in telemetry via nonce beacons — 🟠 = PillarBox forward-secure + freshness beacons.
15. "Impossible-event" physics checker (e.g., causally impossible orderings) — 🟠 = causal-consistency filters (adversarial-timing work) + EvidenceForge already enforces causal order.
16. Out-of-band low-rate event commitment channel — 🟠 = PillarBox reliable channel + verifiable telemetry ledgers.

**White Space C (7):**
17. Q-Audit for provenance DAGs — 🟠 = 2512.00110 (extend-to-DAG is their named future work).
18. **Dependency-aware selective re-signing of evidence DAGs** under PQ migration — 🟡-leaning-🟠 to §3 (feasible, but obvious-combination risk).
19. Hybrid-signature evidence container — 🔴 = NIST hybrid certs; PAdES LTV.
20. Merkle-anchored cheap PQ migration of cold records — 🔴 = 2512.00110 exactly.
21. Crypto-agility CBOM for forensic stores — 🔴 = CBOM prior art.
22. Skip-list PQ transparency log for evidence — 🔴 = named in 2512.00110 direction.
23. Re-timestamp cadence tuned to graph mutation — 🟠 = Round-3 candidate #10 (already downgraded).

**White Space D (7):**
24. TEE-signed dense syscall sequence counter (suppression-evident) — 🟠 = US12524535 TEFTI + FssAgg + PillarBox gap-checker.
25. Fine-grained tamper-evident eBPF log — 🔴 = Nitro (CCS'25).
26. VMI-below-kernel event capture — 🔴 = VMI mature + patents US10944764/US9619346.
27. Measured-boot-rooted provenance chain — 🔴 = TPM/measured-boot + Custos.
28. Hypervisor-mediated trusted syscall path — 🟠 = VMI syscall trapping (arXiv 1705.06784).
29. TrustZone log protection at source — 🔴 = EmLog.
30. PUF-bound per-event authenticity tag — 🟠 = PUF (mature) + at-source binding = combination.

**Immediate-kill outcome:** 27 of 30 rejected as anticipated or obvious combinations. **Survivors to deeper analysis: #13, #18** (and #24 kept only as a foil to show why #13's vantage-point half is not the novelty).

---

## 3. Survivor #18 — Dependency-aware selective re-signing of evidence DAGs (PQ) — verdict 🟠

- **Mechanism:** when migrating a large evidence provenance DAG to PQ signatures, re-sign only a *dependency-minimal cut* such that every historical verification path remains PQ-verifiable, rather than re-signing all nodes — using the DAG's causal-dependency structure to compute the minimal re-sign set.
- **Closest prior art:** 2512.00110 (Merkle-anchor + migration patterns; explicitly names "DAG-based provenance graphs under quantum adversaries" as a *direction*); Merkle transparency logs; skip-lists; LTV.
- **Kill test:** a skilled person, told to migrate a signed DAG cheaply, would compute a dependency cut and re-sign it — this is graph reachability + hybrid signatures, both standard. **Obvious-combination risk HIGH.** Interesting research, weak patent. **Downgrade to 🟠.**

---

## 4. Survivor #13 — Cross-vantage cryptographic omission-bounding — verdict 🟡 (best of round)

**Technical problem (precise).** Existing tamper-evident logging proves *recorded* events were not altered/deleted (Merkle/hash-chain/FssAgg), and PillarBox detects *total* channel suppression via a coarse liveness gap-checker. **None proves a bound on events the attacker prevented from ever being recorded** ("silent" mid-stream suppression by a kernel-level adversary that unhooks the collector). The field admits this: verification "does not establish completeness."

**Proposed novelty-bearing mechanism (the *only* part that could be non-obvious).** A protocol in which a **minimal-TCB observer** (hardware perf-counter/PMU read from a TEE the guest kernel cannot write, or an independent network/hypervisor vantage) emits an **unforgeable, low-fidelity commitment to the *count and coarse type* of security-relevant events in each epoch**, and a **reconciliation proof** binds that commitment to the endpoint's high-fidelity untrusted log to yield a **cryptographically sound lower bound on the number of omitted events of each class, and localizes the epochs in which omission occurred** — even though the omitted events themselves left no record. The technical effect: turn "we cannot prove completeness" into "we can prove **≥ K** class-C events occurred and **≤ N** are present in the host log, so **≥ K−N were suppressed in epoch t**."

- **Closest prior art & why it doesn't anticipate:**
  - PillarBox gap-checker — detects *total* suppression (no buffer in β seconds), not a *per-class quantitative bound* under partial suppression. [eprint 2013/625](https://eprint.iacr.org/2013/625.pdf)
  - FssAgg / forward-secure — truncation (tail deletion), not mid-stream omission of never-recorded events. [Springer](https://link.springer.com/chapter/10.1007/978-3-319-68637-0_6)
  - US12524535 TEFTI — hardens the *probe* against modification; assumes the probe fires. Does not provide an *independent* count to bound omissions when the probe is bypassed. `UNVERIFIED`.
  - VMI (US10944764, etc.) — supplies an out-of-guest vantage but frames it as *detection/introspection*, not a *cryptographic omission-bound reconciliation proof*. **This is why the novelty cannot be the vantage point — VMI is old — but only the reconciliation-bound mechanism.**
  - Verifiable Telemetry Ledgers / HotNets'25 — verify *recorded* telemetry; explicitly disclaim completeness.
- **Impossible-triangle resolved (the patent-worthy hook, if any):** simultaneously (i) monitor the endpoint itself, (ii) at high volume/real-time, and (iii) obtain an *unforgeable quantitative completeness bound* — by **splitting fidelity across two vantages and reconciling** rather than trusting one collector.
- **Hypothetical independent claim (technical, not legal):** *"A method comprising: at a monitor isolated from a host's operating-system kernel, deriving an unforgeable per-epoch commitment to a count of events of a security-relevant class; receiving a separately-collected host event log; and computing, from the commitment and the log, a cryptographically sound lower bound on the number of said-class events omitted from the log and an identification of the epoch(s) of omission."*
  - Limitation mapping: *isolated monitor* → VMI/TEE (**known**); *unforgeable count commitment* → forward-secure MAC/PMU-attested (**known**); *reconcile to bound omissions per class per epoch* → **not found as a unit (potential novelty)**; *localize omission epoch* → **potential novelty**.
- **Experimental differentiator (Part 16):** on a testbed, run EDR-silencing/unhooking attacks (ETW-disable, syscall unhook, eBPF-rootkit blinding) and measure **omission-detection recall and the tightness of the proven lower bound** vs. (a) host-log-only, (b) PillarBox gap-checker, (c) network-telemetry cross-check baseline — target: detect *selective* suppression that all three baselines miss, with a quantified false-omission rate under benign event loss.
- **Why still only 🟡, not 🟢:** the vantage (VMI/network/PMU) and the primitives (forward-secure commitments, Merkle) are all known; the frontier is openly contested (HotNets'25, IETF drafts); a skilled engineer *might* reach "cross-check an independent observer to find missing events." The **entire** patent hope rests on whether the *quantitative per-class omission-bound-and-localize reconciliation proof under benign-loss noise* is genuinely non-obvious — a question only a full-text patent + IACR/USENIX search (impossible here) can answer. **Research paper potential: high. Patent defensibility: unproven.**
- **Conservative score:**

| Metric | /10 |
|---|---|
| Novelty | 6 |
| Inventive-step potential | 5 |
| Prior-art distance | 5 |
| Technical depth | 8 |
| Feasibility | 7 |
| Experimental demonstrability | 8 |
| Market demand | 7 |
| Research potential | 8 |
| Patent-claim potential | 5 |
| Competition (higher = less) | 4 |
| **Overall** | **≈ 6.1 (🟡)** |

It **fails** a strict Round-3-style build gate (needs Novelty ≥7 **and** distance ≥6). It clears only the softer "worth an attorney conversation + a spike" bar.

---

## 5. Updated DEAD-END MAP (Rounds 1–4)

| Idea | Looked novel because | Killer prior art | Anticipated / Obvious | Failed assumption |
|---|---|---|---|---|
| Verdict Witness (replayable PIDS verdict) | court-grade reproducible verdict | Vigilante SCA; ProvX; zkML; "VERDICT" product | Obvious | replay+minimal-subgraph were unclaimed |
| Oracle-Gated DFIR | per-claim gate + coverage cert | EG-VAR; LLM-Provenance-Forensics; FinGround/DEER; Trust Certificate | Obvious | coverage/gating were unclaimed |
| Prompt-Injection Reconstructor | counterfactual span attribution | AgentSentry; Causal Agent Replay; delta debugging | Anticipated | attribution-by-replay was unclaimed |
| ZK-provenance verdict | privacy + verifiability + minimal witness | zkML; ZKGraph; DARPA SIEVE; abductive AXp; P3GNN | Obvious | only cardinality-minimality-in-ZK novel — but infeasible (co-NP) |
| Anti-forensic destruction-signature | classify attack from watermark destruction | fragile watermark + ML manipulation-type classifier | Obvious | manipulation-type-from-distortion was unclaimed |
| Sensor-physics capture attestation | multi-channel consistency | PRNU + IMU fusion + C2PA + TEE | Obvious | combination of known channels |
| PQ forensic-graph time-sealing | graph-state historical provability | 2512.00110; PAdES; accumulators | Obvious | dependent-claim at best |
| **A: agent evidence provenance (Rd4 #1–8)** | new agent-accountability need | AgentBound; RATS-agent-evidence; IETF SCITT capsule | Anticipated | being standardized in 2026 |
| **B: synthetic-log classifier / consistency (Rd4 #9,#12,#15)** | detect fabricated logs | EvidenceForge/MS causal generators; causal filters | Obvious/defeated | cross-source consistency is now forgeable |
| **B: telemetry microtiming fingerprint (#10)** | PRNU-for-telemetry | IET/temporal-autocorr real-vs-synthetic (fraud/Tor) | Obvious | it's a classifier; adversarially learnable |
| **C: PQ evidence DAG / selective re-sign (#17–23)** | DAG-aware PQ migration | 2512.00110 (+ named future work); hybrid sigs; skip-lists | Obvious | ingredients all standard |
| **D: TEE/VMI/PUF trusted telemetry (#24–30)** | trust at generation | Custos; Nitro (CCS'25); EmLog; US12524535 TEFTI; VMI patents | Anticipated/Obvious | integrity-at-source is a mature field |

**Crowded clusters now off-limits without a genuinely new mechanism:** verifiable/attested/replayable AI-security decisions; agent action provenance/receipts; tamper-evident source logging (TEE/eBPF/VMI); synthetic-log detection by consistency/classifier; PQ migration of audit evidence; ZK-verification of security detections.

---

## 6. The most important question (Part 21)

**"What is the most technically difficult problem in AI + cybersecurity + digital forensics today that products and research still cannot reliably solve?"**
**Proving the *completeness and authenticity of endpoint telemetry that a kernel-level adversary can silently suppress or fabricate* — i.e., trusting the evidence itself.** As AI both defends (SOC/DFIR agents) and attacks (causal synthetic-log generators like EvidenceForge), AI systems increasingly reason over telemetry that can be selectively omitted or convincingly fabricated by an attacker who controls the collecting TCB. Everything downstream (detection, forensics, court admissibility) inherits this un-trusted foundation.

**"Why has it not been solved?"** Self-reference: the endpoint that generates the telemetry is the thing under attack, so its own collector is inside the adversary's reach. Tamper-*evidence* only covers *recorded* events; you cannot Merkle-prove what was never inserted. Pushing the root to hardware/TEE still relies on the compromised kernel to *deliver* events, and independent vantages (network/VMI) see only a low-fidelity slice — so nobody can simultaneously get real-time, high-volume, endpoint-native telemetry *with* an unforgeable completeness guarantee (the impossible triangle).

**"What new mechanism could solve it?"** Cross-vantage *omission-bounding*: reconcile an unforgeable low-fidelity count from a minimal-TCB observer against the rich untrusted host log to prove a quantitative lower bound on suppressed events and localize the epoch — accepting low fidelity in exchange for an unforgeable completeness bound.

**"What prior art makes it risky?"** VMI (mature, patented), PillarBox's gap-checker, FssAgg truncation-resistance, US12524535 TEFTI, HotNets'25 verifiable network telemetry, IETF verifiable-telemetry-ledgers — all adjacent; the mechanism is at best a narrow, contested delta.

**"What experiment would prove it works?"** On an instrumented host, launch real EDR-silencing attacks (ETW-disable, syscall unhook, eBPF-rootkit blinding) and show the reconciliation proof detects and *quantitatively bounds* the selective omission that host-log-only, PillarBox-gap-check, and plain network-cross-check baselines all miss — with a measured false-omission rate under benign event loss (the make-or-break metric).

---

## 7. Recommendation

- **Do not start a build.** No candidate earned it.
- **The single justified next step** is a **2–3 week research/feasibility spike** on candidate #13 (omission-bounding), pursued primarily as a **paper**, with a patentability decision *gated* on: (1) a professional full-text patent + USENIX/NDSS/IEEE-S&P search (which this environment cannot perform — all databases 403), focused on "log completeness proof," "omission/suppression bound," "cross-vantage telemetry reconciliation," and US12524535's claims; (2) a written §103 opinion on whether the reconciliation-bound mechanism clears obviousness over VMI + PillarBox + FssAgg; (3) the benign-loss false-omission metric coming out usably tight. If (1) or (2) is fatal, publish the research and stop the patent track.
- **Everything else from Round 4 is dead or obvious** and recorded in §5 to prevent rediscovery.

> All statements are novelty/obviousness **hypotheses requiring professional patent examination.** No claim of (un)patentability is made with certainty. Patents are `UNVERIFIED — FULL TEXT NOT AVAILABLE` (egress-blocked). A winner was not manufactured: the honest result of Round 4 is **one 🟡 research-first candidate and three dead/crowded areas.**
