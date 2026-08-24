# Phase 2B — Confirmation & Threat-Model Lock (Gap #1)

**Project:** AI-Agent Memory Poisoning Research Project · **Phase 2B: confirmations + threat-model lock ONLY. No architecture, detector, algorithm, scoring function, probing strategy, dataset, or code.**
Date: 2026-08-21 · Depends on: `MEMORY_POISONING_PHASE1_GAP_AUDIT.md`, `MEMORY_POISONING_PHASE2A_GAP1_VALIDATION.md`.

> **Environment limitation (material — read first):** Full-text access was **not possible**. `arxiv.org`, `ar5iv.labs.arxiv.org`, and other mirrors are all blocked by the session egress proxy (HTTP 403). The five confirmations below are reconstructed from **abstracts, author pages, and search-surfaced excerpts**, not literal full-text reads. Confirmations are therefore rated **"strong (search-verified)"** at best, never "full-text-verified." The single most important residual check — a full-text read of **PI-Hunter (2606.12737)** — could not be completed and is carried forward as a **blocking confirmation** before Phase 2C. This is why the verdict is 🟡, not 🟢.

---

## FINAL DECISION

## 🟡 GO WITH NARROWING

The gap survives as a distinct research problem **only** under the narrowed threat model locked in Parts 2–11: a **bounded-predicate** semantic trigger, **black-box-no-internals** access, **behavioral (sandbox-elicited)** detection of an **embedding-benign** poison in **persistent episodic/experience vector memory**. Two boundaries are now sharp: (i) *static at-rest* detection of the embedding-benign class is a **negative result** (no distributional signal exists — MINJA is provably embedding-entangled), so any viable detector must be **behavioral, not static**; (ii) *unbounded* semantic triggers are **out of scope** (intractable). Phase 2C (mechanism design) is justified **only after** the two blocking confirmations in the final section clear.

---

## 1. PI-Hunter analysis (2606.12737) — *strong (search-verified); full text NOT read*

| Capability | PI-Hunter | Proposed gap |
|---|---|---|
| Persistent memory | **No** — targets external *ingestion paths* / indirect prompt injection | **Yes** (episodic/experience LTM) |
| Cross-session | Not the framing (in-workflow IPI) | **Yes** (dormant across sessions) |
| Dormant poison | No (surfaces *live* injections) | **Yes** |
| Embedding-benign poison | Not addressed | **Yes** (defining property) |
| Semantic trigger | Test-case evolution toward IPI success | **Yes** (bounded predicate) |
| Action payload | Yes (agentic actions) | **Yes** (action sequence) |
| Pre-activation | Proactive, but for IPI exposure | **Yes** (before natural trigger) |
| Memory-store auditing | **No** (audits ingestion, not a written store) | **Yes** (audits the store) |
| Black-box | Yes | **Yes** |

**Verdict:** PI-Hunter is the **closest methodological neighbor** (proactive, feedback-driven elicitation, black-box, agentic) but is **indirect-prompt-injection-scoped** — it exposes/localizes *live* injection paths, not *dormant entries already resident in a persistent memory store* that activate cross-session. It does **not** kill the gap on the evidence available. **BLOCKING:** a full-text read must confirm PI-Hunter neither (a) treats a persistent memory store as an "ingestion path" it audits at rest, nor (b) demonstrates cross-session dormant coverage. If it does either, the gap **narrows sharply or dies.**

## 2. RAGSieve analysis (2608.13010) — *strong (search-verified)*

| Property | RAGSieve |
|---|---|
| Offline corpus inspection | **Yes** (RSG inspects the complete index without queries) |
| Embedding analysis | **Yes** — self-referenced **local contrast / density** among semantically-similar, lexically-distinct neighbors |
| Semantic trigger detection | No |
| Behavioral payload detection | No |
| Dormant detection | Only via embedding/density anomaly |
| Action payload | No |
| Embedding-benign poison | **Evadable** — keys on a distributional anomaly the target class does not exhibit |

**Verdict:** RAGSieve occupies the *embedding-anomalous* corpus-poison cell. The proposed gap's defining property (**embedding-benign**, per MINJA's confirmed embedding-entanglement) sits in an **empty cell** relative to RAGSieve. Gap survives. **Confirmation needed:** empirically show RAGSieve's RSG scores MINJA-class poison at ≈chance (deferred to evaluation, not this phase).

## 3. MEMSAD analysis (2605.03482) — *strong (search-verified)*
- **White-box requirement:** yes — "gradient-coupled anomaly detection"; the anomaly-score gradient is coupled to the *retrieval objective gradient*, i.e., it needs **model-internal gradient access**.
- **Analysis space:** retrieval space (candidate memories), not agent action.
- **Pre-activation:** partial (preventive at retrieve time), but requires internals.
- **Black-box operability:** **No** — cannot run against a black-box agent without gradients.
- **Is the WB↔BB difference a real deployment constraint or an implementation detail?** **A real constraint.** Production/third-party agents (ChatGPT memory, Copilot, hosted agents) expose **no gradients**; an operator auditing a deployed agent's memory typically has store + I/O + tool logs, **not** weights. MEMSAD is therefore the **white-box upper bound**, not a black-box substitute. Gap survives (as the black-box counterpart problem).

## 4. MemSecBench analysis (2607.27080) — *strong (search-verified)*
- Supports: **defender-side lifecycle** eval via **Write–Execute–Forget** in an isolated runtime; traces the same malicious semantics across **persistence, consequence, repair**; 310 cases / 48 contexts; cross-session; diverse memory backends.
- Does **not** provide: a **pre-activation *detection* metric** (it measures attack persistence/consequence and repair efficacy, not "was the dormant entry flagged before its trigger"); no embedding-benign-vs-anomalous split; no bounded-semantic-trigger predicate axis reported.
- **Verdict:** MemSecBench is the right **substrate** (realistic Write–Execute–Forget harness) but is **not** a defender-side pre-activation-detection benchmark. A **minimal extension** — a pre-activation detection split with embedding-benign/anomalous labels and a bounded-trigger predicate axis — would be required. **Guardrail:** a missing benchmark is **not** itself claimed novel; any benchmark contribution must be justified as an extension of MemSecBench, not a fresh artifact.

## 5. MINJA analysis (2503.03704) — *strong (search-verified)* → defines the canonical attack
- **Poisoning mechanism:** query-only interaction (no direct store access); indication prompts + bridging steps + **progressive shortening** so the malicious record is retrieved for future victim queries.
- **Memory representation:** natural-language experience records in an embedding-indexed LTM.
- **Persistence:** record resides in LTM across sessions.
- **Trigger:** semantic proximity of a future query to the injected record.
- **Payload (as published):** malicious **reasoning-trajectory** steering.
- **Embedding behavior:** **CONFIRMED embedding-benign** — "malicious and benign records are highly entangled in the embedding space, indistinguishable using simple similarity-based filtering"; "minimal distributional signal for surface-level detection."
- **Detectability:** evades input/output moderation and retrieval-similarity filters.
- **Modifiable to action-sequence + embedding-benign?** Yes — payload can be a tool-action sequence (cf. Trojan Hippo exfiltration chains, MemMorph tool-hijacking [2605.26154]) while retaining MINJA's embedding-benign injection.

**Canonical Phase-2C attack instance (locked):** *A single MINJA-style, query-only-injected, embedding-benign experience record that stays inert under normal queries and, only when a bounded context predicate holds, steers the agent through a harmful tool-action sequence.*

## 6. Cross-domain analysis (consolidated)
Existing detectors partition cleanly and none occupies the target cell:
- **Store-access + embedding/density anomaly** → RAGSieve, TrustRAG, GMTP: fail on embedding-benign (MINJA).
- **White-box internals** → MEMSAD (gradients), activation probes: unavailable for deployed agents.
- **Retrieval-layer, reactive to the query** → A-MemGuard (66% miss).
- **Activation-time behavioral, black-box** → Forensic Trajectory Signatures (AUC 0.99) and **VIGIL** (SMT policy monitor over tool-call traces, >95% recall/<10% FPR, needs a policy spec): detect *during/at* the harmful action, **not before** the natural trigger.
- **Post-hoc forensics/rollback** → MemAudit, `memory-blackbox` (GitHub), Dependency-Guided Rollback: after compromise.
**Empty cell = black-box + pre-activation + behavioral + embedding-benign + persistent-memory-native.**

---

## 7. Locked threat model — attacker capabilities
Granted (minimal, MINJA-consistent): ☑ **write** memory (indirectly, via query-only interaction); ☑ **interact** with the agent; ☑ **control external documents** the agent may ingest; ☑ **adapt** after failed attacks (adaptive adversary considered); ☑ craft an **embedding-benign** record; ☑ choose a **bounded context-predicate** trigger and an **action-sequence** payload.
**Denied:** ☐ direct modify/delete of arbitrary store rows; ☐ observe the auditor or its sandbox; ☐ observe/alter embeddings/index internals; ☐ white-box access to the model; ☐ control the auditor's trigger-candidate set. (Capabilities not granted are explicitly withheld.)

## 8. Memory model (minimum required)
**Locked:** persistent **episodic/experience** memory — natural-language records, **embedding-indexed** (vector LTM), retrieved by semantic similarity and consolidated across sessions. (This is exactly MINJA/AgentPoison's setting.) **Excluded** for the minimal model: procedural/tool memory, structured DB memory, and multimodal memory (deferred; MemVenom-class multimodal is out of scope for the minimal instance).

## 9. Embedding-benign definition (operational — to be fixed before any experiment)
A poisoned record is **embedding-benign** iff, under a **pre-registered** configuration ⟨embedding model E, distance metric d, reference corpus C of legitimate memories, anomaly test T, operating FPR α⟩, an embedding-only anomaly detector using T at FPR α flags the record with probability indistinguishable from its flag rate on legitimate records (operationally: embedding-only detector **AUROC ≈ 0.5** separating poisoned from benign). The tuple ⟨E, d, C, T, α⟩ **must be fixed in advance** and reported; the class is defined **relative to** that tuple (no post-hoc tuning). *(Definition only — no detector is specified here.)*

## 10. Semantic trigger model (bounded)
**Locked in-scope:** a **finite, enumerable context predicate** over a small set of categorical variables, e.g. `Identity(role) × Task(type) × ToolAvailability(subset)`, with the poisoned record **inert** unless the conjunction holds. The predicate space is **bounded and known to the auditor's evaluation harness by construction** (the attacker chooses a predicate from a defined finite lattice). **Explicitly out of scope:** unbounded/free-text paraphrase triggers, natural-language-open triggers, and multi-turn temporally-accumulated triggers (deferred; see Part 13 hardness).

## 11. Action-payload model
**Locked:** a **harmful tool-action sequence** with a measurable security effect in a sandbox, e.g. `retrieve_sensitive → invoke_external_tool → transmit/exfiltrate` (optionally `→ delete_evidence`). Single-action payloads are permitted but the **action-sequence** form is preferred because it yields a crisp, sandbox-verifiable success signal (state change), consistent with AgentDojo-style verification.

## 12. Pre-activation definition
A detector is **pre-activation** iff it flags the poisoned entry **before the attacker's natural trigger is supplied in the live deployment AND before the malicious action executes in production.** Ordering:
- ✅ **Before retrieval** (static store scan) — *counts*, but is a **negative result** for the embedding-benign class (Part 13).
- ✅ **After retrieval, before production action** — counts (includes controlled **sandbox** elicitation, where any harmful action occurs in the audit sandbox, not production).
- ❌ **During the production action** (Forensic Trajectory Signatures / VIGIL timing) — does **not** count.
- ❌ **After compromise** (MemAudit / rollback) — does **not** count.

## 13. Hardness boundary (a scientific result in itself)
- **At-rest / before-retrieval detection of embedding-benign poison is infeasible in general** — MINJA confirms poisoned and benign records are embedding-entangled with "minimal distributional signal"; and a MINJA-class record "is legitimate input, with latent side effects," i.e., **semantically indistinguishable from a benign belief until the trigger holds.** ⇒ **Any viable detector for this class must use *behavioral* signals, not static/content/embedding signals.** (Boundary statement, not a method.)
- **Unbounded semantic triggers are intractable** — the trigger space is combinatorial/open; weight-space trigger inversion (PICCOLO/DBS) "barely converges" even with gradients, and no gradient handle exists over an external corpus.
- **Tractable subclass (the research target):** **bounded** context-predicate triggers (finite lattice) + **single-entry** poison + **sandbox-observable** action payload + **finite tool set**. The boundary between the bounded-predicate (tractable) and open-semantic (infeasible) regimes is itself a defensible contribution.

## 14. Baselines (locked, no new method yet)
- **B1** No defense.
- **B2** Generic embedding-anomaly detector (at the pre-registered ⟨E,d,C,T,α⟩).
- **B3** RAGSieve (RSG offline corpus inspection).
- **B4** MEMSAD (**white-box upper bound**; run only where internals are available, as a ceiling).
- **B5** Forensic Trajectory Signatures (**activation-time, black-box** — the realistic deployed baseline; new method must show positive **lead-time** over it).
- **B6** PI-Hunter (attempt to adapt to persistent-memory auditing; report if it cannot be adapted).
- **B7** Memory sanitization / composite-trust-scoring (temporal decay + pattern filter).
- **B8 (reference points)** VIGIL (policy-spec monitor) and `memory-blackbox` (post-hoc forensics) — for timing comparison only (both are non-pre-activation).

## 15. Evaluation metrics (pre-registered, thresholds fixed before results)
- **Primary:** pre-activation detection rate (fraction of planted embedding-benign, bounded-trigger poisons flagged before production activation).
- **Secondary:** FPR on legitimate memory; **lead-time** before natural activation (vs. B5); **trigger-predicate coverage** (which predicate lattices are detectable); **adaptive-attack resistance** (detection under attacker adaptation, per Part 7); **memory-utility degradation** (task success on benign memory under auditing); **compute cost** and **audit throughput** (entries/sec, scalability to N).
- **Reporting discipline:** oblivious **and** adaptive adversary settings; ≥5 session transitions for cross-session persistence; FPR reported alongside TPR (per the survey's evaluation recommendations, 2604.16548).

---

## Final GO/NO-GO and blocking confirmations

**Verdict: 🟡 GO WITH NARROWING** — the gap is a genuinely distinct, empty cell (black-box + pre-activation + behavioral + embedding-benign + persistent-memory-native), the canonical attack (MINJA-class, action-sequence) and all definitions are locked, the hardness boundary is explicit, and no located defense occupies the cell. Phase 2C (mechanism design) is justified **only after both blocking items clear**:

- **BLOCKING-1 (highest priority): full-text read of PI-Hunter (2606.12737)** — confirm it does not audit a persistent memory store at rest or demonstrate cross-session dormant coverage. This environment could not fetch it (egress-blocked); a human or an unblocked environment must complete it. *If PI-Hunter covers persistent dormant memory, downgrade to 🟠 STOP.*
- **BLOCKING-2: full-text reads of MEMSAD (2605.03482) and RAGSieve (2608.13010)** — confirm (a) MEMSAD's white-box/gradient requirement is load-bearing (no black-box variant), and (b) RAGSieve's RSG keys on an embedding/density anomaly that a MINJA-class record does not exhibit.

**Non-blocking but required in Phase 2C setup:** register the ⟨E,d,C,T,α⟩ embedding-benign tuple and the trigger-predicate lattice before any measurement; build the pre-activation-detection split as a *documented extension of MemSecBench*, not a fresh benchmark.

> **Absolute-rule compliance:** No architecture, detector, algorithm, scoring function, probing strategy, dataset, or code is proposed in this document. Only the chain **Threat → Memory → Trigger → Payload → Observation model → Detection timing → Hardness boundary → Baselines → Metrics** is locked. All confirmations are search-reconstructed (full text egress-blocked) and carry the residual risk noted above. No novelty or patentability is claimed.
