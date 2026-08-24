# MINJA — Integration Audit (official repo found; faithfulness UNVERIFIED)

**Paper:** *Memory Injection Attacks on LLM Agents via Query-Only Interaction*, arXiv:2503.03704
(NeurIPS 2025 poster). Reported ≈ 98.2% injection success / 76.8% ASR; agents: RAP, EHR, QA.
**Official code (confirmed by title + agent set in search):** `https://github.com/dsh3n77/MINJA`.
Mechanism: query-only injection via **bridging steps + indication prompt + progressive shortening**.

> Could NOT clone/inspect in the authoring sandbox (GitHub egress-blocked, no GPU). The audit
> below MUST be performed on the networked run machine BEFORE integration. Do not integrate blind.

## On the run machine — clone + record
- [ ] `git clone https://github.com/dsh3n77/MINJA` into `gate2/attacks_impl/minja/upstream/`
- [ ] Record: commit hash, tag/release, **LICENSE** (confirm redistribution/derivative terms).
- [ ] Record dependencies (requirements) and any model/checkpoint assumptions.

## Faithfulness audit (must all be answered before wiring into `attacks.py::MINJA.construct`)
1. Does the repo correspond to arXiv:2503.03704 (same method: bridging steps, indication prompt,
   progressive shortening)? Cite the files.
2. **Memory representation** — how is an injected record stored (text/embedding/metadata)? Does it
   match our `MemoryRecord{id,text,meta}` over a FAISS cosine store?
3. **Poison-generation mechanism** — the optimizer/loop that crafts the injected experience.
4. **Trigger mechanism** — MINJA is *query-conditioned*. Our locked threat model triggers on a
   **context predicate** Ψ (identity×task×tool_config). Document exactly how MINJA's query trigger
   is expressed over Ψ **without changing the published attack** — if it cannot be, record it as a
   finding (bears on applicability), do NOT bend the attack.
5. **Payload mechanism** — MINJA's payload is a malicious reasoning/step sequence. For our sandbox
   the observable payload is `read_secret → http_post` (harm oracle). Confirm the published attack
   can induce an *action* payload, or record the gap.
6. **Single-entry** — the frozen budget is `poison_count = 1`. Does MINJA support a single injected
   record, or does it require multiple? If multiple are intrinsic → **BLOCKED for this cell** (do
   NOT reduce to 1 by altering the mechanism).
7. Would ANY modification needed to run it here change the *published* attack? If yes → mark BLOCKED
   and explain precisely which published property changes.

## Integration contract
Only after the checklist passes: implement `MINJA.construct(spec, benign_context_examples) ->
MemoryRecord` by calling the official code faithfully. Label provenance (repo + commit). Do NOT
treat the scaffold as the attack; do NOT invent a substitute.
