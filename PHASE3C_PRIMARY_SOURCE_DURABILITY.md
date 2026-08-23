# Phase 3C — Primary-Source Durability Check (Narrowed Gap)

**Project:** AI-Agent Memory Poisoning Research Project · **Phase 3C: full-text durability check. No mechanism/architecture/algorithm/dataset/code.**
Date: 2026-08-21.

---

## ⛔ FULL-TEXT PRIMARY-SOURCE READING BLOCKED

Phase 3C requires reading the **actual full text** of QPD/Semantic Chameleon (2603.18034), MemAudit (2605.23723), MEMSAD (2605.03482), and Forensic Trajectory Signatures / FTS (2606.30566), with **section/page citations for every non-obvious cell**. **I cannot.** Every paper-hosting domain is egress-blocked in this environment. Attempts across Phase 2C + 3C (all failed — 403 or DNS):

`arxiv.org` · `ar5iv.labs.arxiv.org` · `browse.arxiv.org` (no DNS) · `export.arxiv.org` · `huggingface.co` · `semanticscholar.org` · `openreview.net` · `alphaxiv.org` · `research.google` · `researchgate.net` · `aclanthology.org` · `paperswithcode.com`.

**Consequences I am holding to:**
- I will **not** fabricate section/page citations for papers I could not open. Where the phase asks for a page cite, I mark **[NO FULL TEXT — cite pending]**.
- Evidence tiers: **[UV]** = user-verified in a prior turn; **[S]** = search-surfaced excerpt (explicitly *not* full text, insufficient per the phase's own bar); **[INF]** = reasoned inference from established mechanism.
- The mandated durability check is therefore **incomplete**. I cannot upgrade to 🟢 ROBUST. The substantive analysis below is **provisional** and exists to (a) show the gap is not obviously dead and (b) give you exactly what to confirm from the PDFs.

---

## 1. Per-paper evidence (provisional; tiers marked)

### CHECK 1 — QPD / Semantic Chameleon (2603.18034)  **[S]**
Best-available (search) evidence, not full text:
- **What QPD measures:** "the **behavior of a document across query types** rather than static properties"; QPD ≈ 1.0 ⇒ retrieved **almost exclusively for sensitive queries** = targeted-poisoning signature; most robust cross-corpus signal (3.7× vs 13–62× for static). ⇒ **retrieval-selectivity**, a **retrieval-layer** signal.
- Answers (provisional): measures retrieval selectivity **YES**; executes the agent **NO (no evidence)**; observes tool calls / action sequences **NO**; detects harmful actions **NO** (answer/retrieval only); persistent agent **experience** memory **NO** (RAG **document corpus**); already-stored **YES** (offline corpus scan); pre-trigger **~** (statistical, needs a query workload); embedding-preserving poison **NO** (needs retrieval-selectivity, which an entangled/broadly-retrieved MINJA-style entry lacks); identifies the entry **YES** (which doc); identifies the trigger condition **~** (sensitive-query class); black-box **YES**; requires embeddings/retrieval visibility **~YES**; query-response behavior only **YES**.
- **CRITICAL TEST result (provisional):** QPD does **not** perform black-box proactive **action-elicitation** on persistent memory, and does **not** identify dormant **action-triggered** poison — it infers from **retrieval statistics across query types**. **Gap not killed by QPD** *(pending full text)*. Boundary: **retrieval-selectivity vs action-behavior**, and **RAG corpus / answer payload vs agent experience memory / action payload**, and **embedding-preserving evasion**.

### CHECK 2 — MemAudit (2605.23723)  **[S]**
- Best-available evidence: "the **post-hoc** question of which stored memories are responsible **after harmful behavior has already been observed**"; **counterfactual memory-influence** score (causal contribution to **harmful outputs**) + **memory-consistency graph**; removes suspicious memories **without poison labels**; evaluated vs MINJA.
- Answers (provisional): requires harmful behavior first **YES**; audit before an incident **NO (not designed for it)**; proactively test dormant memories **NO**; identify causal entries **YES**; identify triggers **~** (not stated); executes counterfactual queries **YES** (counterfactual influence); cross-session **YES**; persistent experience memory **YES**; black-box **~YES** (no labels); requires embeddings/internals **~ unclear** (counterfactual influence likely needs re-execution / model queries, not gradients).
- **CRITICAL TEST result (provisional):** MemAudit's procedure is **anchored to an observed harmful output**; applying it "before any harmful behavior" requires **first generating a harmful trajectory to attribute** — i.e., a **proactive elicitation front-end MemAudit does not have**. So it is **not** a direct pre-incident detector. It could serve as an **attribution/localization back-end** *after* elicitation. **Gap narrowed but not killed** *(pending full text)*. Missing capability: **proactive elicitation of the dormant harmful trajectory**.

### CHECK 3 — MEMSAD (2605.03482)  **[UV]+[S]**
- User-verified + search: models persistent agent memory; **write-time / pre-ingestion** anomaly detection; **gradient-coupling theorem** linking anomaly-score gradients to **retrieval-objective gradients** (⇒ needs retriever/embedding gradients = **white-box embedding access**); Stackelberg-game formalization (AgentPoison WRITE / MINJA QUERY / InjecMEM SINGLE); detects MINJA **TPR 0.40 / AUROC 0.914**, InjecMEM TPR 0.20; untriggered attacks "naturally mitigated by corpus scale."
- Answers (provisional): write-time/pre-ingestion **YES**; persistent memory **YES**; MINJA eval **YES**; embedding access **YES (required)**; gradient requirement **YES (core theorem)**; black-box feasibility **NO (theorem collapses without gradients)**; adaptive attacks **YES (Stackelberg)**; inspect **already-stored** memories **NO (screens writes)**; proactively probe stored memories **NO**; identify semantic triggers **NO**; identify action payloads **NO**.
- **CRITICAL TEST result (provisional/UV):** the difference is **NOT** merely deployment/access config. MEMSAD's detection *is* the gradient-coupling signal; removing embedding/gradient access removes the method's foundation, and write-time≠already-stored, and the signal is **retrieval-anomaly**, not **action-behavior**. **Fundamentally different observable required.** **Gap not killed.**

### CHECK 4 — Forensic Trajectory Signatures / FTS (2606.30566)  **[S]**
- Best-available evidence: detects a **behavioral invariant in the execution trajectory** (e.g., `memory_recall → email_send`), **black-box**, "lightweight structural features **without model internals**," AUC 0.99, prefix-only 0.934 ("real-time blocking feasible"); studies **3 adaptive evasions**; distinguishes memory-channel from prompt-injection attacks via tool-call logs.
- Answers (provisional): detection occurs **at activation** (during the attack's trajectory); malicious behavior must first activate **YES**; predict before activation **NO**; identifies the memory entry **~** (channel, not the specific dormant entry); identifies the trigger **NO**; persistent memory **YES**; black-box **YES**; detects action/tool behavior **YES**; proactive auditing **NO**.
- **CRITICAL TEST result (provisional):** FTS's signal **requires the trajectory to execute**; it cannot identify dormant poison **before** the trigger fires. It is reusable as a **trajectory classifier** on an **already-elicited** trajectory, but supplies **no proactive elicitation**. **Gap not killed** *(pending full text)*. Boundary: **activation-time / reactive vs proactive / pre-trigger**.

---

## 2. Four-way comparison matrix (evidence-tier tagged; **section/page cites pending full text**)

Cells: Y/N/~ with tier [UV]/[S]/[INF].

| Capability | QPD | MemAudit | MEMSAD | FTS | Target |
|---|---|---|---|---|---|
| Persistent agent memory | N[S] (RAG corpus) | Y[S] | Y[UV] | Y[S] | **Y** |
| Already-stored memory | Y[S] | Y[S] | N[UV] (write-time) | N[S] | **Y** |
| Single-entry poison | Y[S] | Y[S] | Y[UV] (InjecMEM) | ~[S] | **Y** |
| Dormant poison | Y[S] | Y[S] | ~[UV] | N[S] (activation) | **Y** |
| Embedding-preserving | N[S] | ~[INF] | N[UV] | Y[S] | **Y** |
| Semantic (context) trigger | N[S] (query-keyword) | ~[S] | N[UV] | N[S] | **Y** |
| Action payload | N[S] (answer) | ~[S] | N[UV] | Y[S] | **Y** |
| Black-box | Y[S] | ~Y[S] | N[UV] | Y[S] | **Y** |
| No embedding access | ~[S] | ~[INF] | N[UV] | Y[S] | **Y** |
| No model internals | ~[S] | ~[INF] | N[UV] | Y[S] | **Y** |
| Proactive | ~[S] | N[S] | ~[UV] (write-time) | N[S] | **Y** |
| Pre-trigger | ~[S] | N[S] | Y[UV] (pre-ingest) | N[S] | **Y** |
| Action elicitation | N[S] | N[S] | N[UV] | N[S] | **Y** |
| Entry localization | Y[S] | Y[S] | ~[UV] | ~[S] | **Y** |
| Trigger localization | ~[S] | ~[S] | N[UV] | N[S] | **Y** |
| Cross-session | N/A[S] | Y[S] | Y[UV] | Y[S] | **Y** |
| Adaptive adversary | ~[S] | ?[S] | Y[UV] | Y[S] | **Y** |

No column equals the Target column. **The single row that no paper has is `Action elicitation` = Y** (all four: N). This is the crux differentiator, consistent with the trivial-adaptation analysis below.

---

## 3. Trivial-adaptation test (provisional — grounded in mechanism, not full text)

> *Can an ordinary competent researcher adapt Paper X to the target without inventing a new technical idea?*  A=directly covers · B=trivial adaptation · C=substantial modification · D=fundamentally different mechanism.

| Adaptation | Class | Reason (provisional) |
|---|---|---|
| **QPD → agent memory + action** | **C** | Corpus→experience-memory is easy, but the **signal must change from retrieval-selectivity to elicited action-behavior**, and QPD's signal is blind to **embedding-preserving** entries. New observable = substantial modification. |
| **MemAudit → pre-incident** | **C** | Counterfactual-influence attribution is reusable as a **back-end**, but it is **anchored to an observed harmful output**; obtaining that output for **dormant** poison requires a **proactive elicitation front-end MemAudit lacks**. |
| **MEMSAD → black-box** | **D** | The method *is* the **gradient-coupling theorem**; without retriever/embedding gradients it has no signal, and it is write-time, not stored behavioral. Fundamentally different mechanism required. |
| **FTS → pre-activation** | **C** | FTS is a **classifier on an executed trajectory**; reusable once a trajectory is elicited, but it provides **no proactive elicitation of dormant poison**. |

**None is A or B (provisional).** All are **C/D** ⇒ on mechanism-level evidence the gap **survives more strongly**, with the missing capability crisply identified: **proactive elicitation of dormant, embedding-preserving, action-triggered poison under semantic context predicates**. *This classification must be re-confirmed against full text (esp. QPD and MemAudit).* 

---

## 4. Exact remaining gap
No located work provides a **proactive** auditor that, with **black-box access and no victim embedding/gradient/internal state**, surfaces an **already-resident, embedding-preserving, single dormant entry** in **agent experience memory** by **eliciting its action/tool-use payload** under a **semantic context predicate** (role × task × tool-availability, not query keywords), and **localizes both the entry and its activation condition** — under an **adaptive** adversary. Existing behavioral detectors are **retrieval-behavioral** (QPD), **post-hoc** (MemAudit), **write-time white-box** (MEMSAD), or **activation-time** (FTS). The **`action-elicitation`** capability is absent from all four (matrix §2).

## 5. Threat-model boundary
Detectable-in-principle (target): bounded semantic-context-predicate triggers + single embedding-preserving entry + sandbox-observable action sequence + black-box + no embedding/gradient. Out of scope / likely infeasible: unbounded free-text triggers; multi-entry compositional triggers; static at-rest content/embedding detection of embedding-preserving poison (no signal).

## 6. What existing work already solves
Write-time detection (MEMSAD, white-box); retrieval-selectivity detection of dormant RAG poison (QPD); geometric/token/activation detection of embedding-*anomalous* poison (RevPRAG/GMTP/canary/Phantom-def); **post-hoc** attribution + localization (MemAudit); **activation-time** black-box trajectory detection + adaptive-evasion study (FTS); repair/rollback (Dependency-Guided Rollback); benchmarks (MPBench/MemSecBench/ASB).

## 7. What existing work does NOT solve
**Proactive, pre-trigger, black-box, action-eliciting** detection+localization of **embedding-preserving** dormant single-entry poison in **agent experience memory** under **context-predicate** triggers. (MPBench explicitly "motivates behavioral detection **but does not provide a detector**.")

## 8. Research question (one; not a solution)
> *Can a black-box auditor — without access to the victim's embedding function, gradients, or model internals — proactively surface and localize an already-stored, embedding-preserving, single dormant memory entry (and its semantic-context activation predicate) by eliciting its action/tool-use payload before the attacker's natural trigger occurs, achieving a detection/localization rate and pre-activation lead-time above post-hoc (MemAudit), retrieval-behavioral (QPD), and activation-time (FTS) baselines, at bounded false-positive and compute cost — and what is the boundary of the context-predicate space within which this is tractable?*

## 9. Remaining uncertainty (ranked; all resolvable only with the PDFs)
1. **QPD (2603.18034):** confirm it measures retrieval-selectivity only and cannot see embedding-preserving/broadly-retrieved poison, and does not execute the agent for action observation. *If QPD already elicits action behavior on agent memory → 🟠/🔴.*
2. **MemAudit (2605.23723):** confirm it strictly requires an observed harmful output and has no built-in proactive elicitation. *If it audits dormant memory pre-incident out-of-the-box → 🟠.*
3. **FTS (2606.30566):** confirm activation-time only (no pre-trigger prediction of the dormant entry).
4. **MEMSAD (2605.03482):** confirm the gradient-coupling requirement is load-bearing (no black-box variant). *(Largely user-verified.)*
5. Fast-moving field: a proactive-elicitation detector could appear at any time.

## 10. Final GO / NO-GO
- **Status: 🟡 GAP SURVIVES BUT NEEDS NARROWING** — provisional/mechanism-level evidence keeps it alive (all four adaptations C/D; `action-elicitation` unoccupied), **but the mandated full-text durability check could not be completed** (egress-blocked), so it **cannot** be upgraded to 🟢 ROBUST here.
- **Mechanism design (Phase 4): NO-GO** until the four PDFs are read and the §9 uncertainties (esp. #1 QPD, #2 MemAudit) are resolved from primary text.
- **Action:** supply the four PDFs (priority **QPD ≫ MemAudit ≫ FTS ≈ MEMSAD**) or an unblocked environment; I will then fill the matrix with real section/page citations and finalize 🟢/🟠/🔴.

> **Boundary discipline (#1 literature gap and #2 technical differentiation only):** this report establishes that the literature cell is unoccupied and identifies the differentiating capability (action-elicitation). It does **not** claim research novelty (#3), patent novelty (#4), or inventive step (#5). No mechanism, algorithm, dataset, or code is proposed. All non-user-verified evidence is flagged provisional pending full text; no citation was fabricated.
