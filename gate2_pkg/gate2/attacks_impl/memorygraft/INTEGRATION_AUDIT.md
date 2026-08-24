# MemoryGraft — Integration Audit (official repo found; faithfulness UNVERIFIED)

**Paper:** *MemoryGraft: Persistent Compromise of LLM Agents via Poisoned Experience Retrieval*,
arXiv:2512.16962. Validated on MetaGPT's DataInterpreter agent with GPT-4o.
**Official code + data (from search):** `https://github.com/Jacobhhy/Agent-Memory-Poisoning`.
Mechanism: attacker supplies **benign ingestion-level artifacts**; the agent reads them during
execution and **constructs + persists** a malicious "successful experience"; later retrieval over
lexical+embedding similarity surfaces the grafted memory and the agent imitates the unsafe pattern.

> Could NOT clone/inspect in the authoring sandbox (GitHub egress-blocked, no GPU). Perform this
> audit on the networked run machine BEFORE integration.

## On the run machine — clone + record
- [ ] `git clone https://github.com/Jacobhhy/Agent-Memory-Poisoning` into
      `gate2/attacks_impl/memorygraft/upstream/`
- [ ] Record: commit hash, tag/release, **LICENSE**, dependencies, model assumptions (paper uses GPT-4o
      + MetaGPT DataInterpreter — note the divergence from our frozen Llama-3.1-8B agent + our sandbox tools).

## Faithfulness audit (answer before wiring into `attacks.py::MemoryGraft.construct`)
1. Repo ↔ arXiv:2512.16962 correspondence (grafting of benign artifacts → self-authored malicious
   experience). Cite files.
2. **Memory representation** vs our `MemoryRecord`/FAISS cosine store.
3. **Poison-generation** — the benign-artifact → grafted-experience pipeline. Note: MemoryGraft is
   *trigger-free / benign-grafted*; map that onto our single-entry dormant record honestly.
4. **Payload** — can the grafted experience induce the `read_secret → http_post` action payload our
   harm oracle scores? If the published attack targets a different payload class, record the gap;
   do NOT invent a new payload and call it MemoryGraft.
5. **Single-entry** — supports `poison_count = 1`? If the published effect requires several grafted
   records, record it (do NOT force to 1 by altering the mechanism).
6. **Agent/model coupling** — the attack was demonstrated on GPT-4o+MetaGPT. Determine whether its
   effectiveness is intrinsic to that stack; running it against the frozen Llama-3.1-8B agent is a
   fidelity question to document, not to paper over.
7. Would any change needed here alter the *published* attack? If yes → BLOCKED with the exact reason.

## Integration contract
After the checklist passes: implement `MemoryGraft.construct(...) -> MemoryRecord` by faithfully
calling the official code; label provenance (repo + commit). No substitute attack.
