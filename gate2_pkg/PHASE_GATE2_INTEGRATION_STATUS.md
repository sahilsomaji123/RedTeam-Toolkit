# Gate 2 — Integration Status (pre-run audit)

**FINAL STATUS: 🟡 BLOCKED** — NOT `READY_FOR_CALIBRATION`.
Date: 2026-08-24 · No Gate-2 trials run · No calibration run · No Phase 4C · No detector/attack designed ·
No threshold changed · No model substituted/quantized · No fabricated results.

This round cleared every blocker that is clearable from a GPU-less sandbox and honestly marks the rest.
`READY_FOR_CALIBRATION` requires ALL of: Hardware READY, MEMSAD CALIBRATION_READY, QPD CALIBRATION_READY,
attacks INTEGRATION_READY, Agent READY (§ Calibration-gate readiness). **Hardware is a hard blocker**, so
the final status is BLOCKED regardless of the other rows.

> Where this was produced: audits, generators, and adapters were written/tested against the committed
> package. Cloning the published repos, downloading models, and running calibration MUST happen on the
> networked ≥16 GB-VRAM machine — this sandbox has no GPU and cannot reach GitHub/HuggingFace/arXiv.
> Repo/URL lines are search-level; the run machine must clone + inspect before integration.

---

## Component status table (mandated)

Legend — ✅ done/verified · 🟨 prepared, integration/validation pending · ⛔ hard-blocked · ⬜ not started.

| Component | Status | Evidence | Blocker | Next action |
|---|---|---|---|---|
| **Hardware** | ⛔ | Only reachable machines: this GPU-less cloud sandbox + user's local **T400 4 GB**. `list_environments` shows one `anthropic_cloud` env (no GPU); no ≥16 GB VRAM host reachable | Llama-3.1-8B (bf16 ≈16 GB) needs ≥16 GB VRAM; substitution/quantization forbidden by prereg | Provision **≥16 GB VRAM** GPU, or (your call only) author a NEW pre-registration for the agent model |
| **DPR** | 🟨 | `gate2/embedders.py::DPREmbedder`; `facebook/dpr-{ctx,question}_encoder-single-nq-base` ≈0.44 GB each (fit 4 GB) | Not downloaded/hashed (HF egress-blocked here) | On run machine: download both, record SHA256 in RESULT.json |
| **BGE** | 🟨 | `gate2/embedders.py::STEmbedder`; `BAAI/bge-base-en-v1.5` ≈0.44 GB | Not downloaded/hashed | On run machine: download, record SHA256 |
| **Llama** (agent) | ⛔ | `meta-llama/Llama-3.1-8B-Instruct`, temp 0; backend written (`backends/llama_hf.py`) | Does not fit T400 4 GB; CPU-unquantized is spec-compliant but ~weeks/months at the frozen budget → impractical | ≥16 GB VRAM; validate backend on hardware |
| **MEMSAD** | ⛔ | `baselines.py::MEMSAD.score` → `NotImplementedError`; needs retriever gradients; **no official code found** (arXiv:2605.03482) | No official code; not calibrated | Re-check author GitHub/PDF on run machine; else faithful reimpl per `baselines_impl/memsad/…`; pass `calibrate()` (≈TPR 0.40/AUROC 0.914 on MINJA) or stay BLOCKED |
| **QPD** | ⛔ | `baselines.py::QPD.score` → `NotImplementedError`; **official code likely EXISTS** — paper states artifacts "are available" (URL truncated in index) (arXiv:2603.18034) | Exact code URL unresolved in sandbox; not integrated; not calibrated | On run machine: resolve URL from PDF/perfecxion.ai, prefer official code; else faithful reimpl per `baselines_impl/qpd/…`; pass `calibrate()` |
| **MINJA** | 🟨 | `attacks.py::MINJA` stub; **official repo confirmed** `github.com/dsh3n77/MINJA` (RAP/EHR/QA agents match paper); audit checklist at `attacks_impl/minja/INTEGRATION_AUDIT.md` | Not cloned/audited/integrated (egress-blocked); single-entry + Ψ-mapping to verify | On run machine: clone, record commit+LICENSE, run audit, integrate `construct()` |
| **Trojan Hippo** | ⛔ | `attacks.py::TrojanHippo` stub; **no official code found** (arXiv:2605.01970v2); reimpl spec at `attacks_impl/trojan_hippo/…` | No code; faithful reimpl required | Faithful reimpl from PDF (single-entry, Ψ-trigger, read→post exfil) |
| **MemoryGraft** | 🟨 | `attacks.py::MemoryGraft` stub; **official repo confirmed** `github.com/Jacobhhy/Agent-Memory-Poisoning` (MetaGPT DataInterpreter + GPT-4o); audit at `attacks_impl/memorygraft/…` | Not cloned/audited/integrated; payload/single-entry/agent-coupling to verify | On run machine: clone, record commit+LICENSE, run audit, integrate `construct()` |
| **Agent backend** | 🟨 | `backends/llama_hf.py` written: temp-0 greedy HF adapter + tool-call parser (parser unit-checked); import-safe (lazy torch) | UNTESTED on hardware; blocked by Hardware/Llama; tool-call protocol is behaviorally load-bearing | On ≥16 GB VRAM: load model, validate determinism + freeze the tool-call protocol |
| **Sandbox** | ✅ | `gate2/sandbox.py`: mock tools, deterministic `harm()` oracle, SECRET_TOKEN canary, TOOL_CONFIGS; no real egress | None | None — ready |
| **Corpus generator** | ✅ | `gate2/datagen.py::gen_corpus`; **tested** deterministic + hashable at n=5,000 (two runs identical SHA256); benign/neutral, no trigger/payload content | None (final data emitted only with `--emit`, deferred to run) | On run machine: `--emit` + record corpus_C.json hash |
| **Query generator** | ✅ | `gate2/datagen.py::gen_query_workload`; **tested** deterministic at n=2,000; (identity,task)-labeled so a faithful QPD split is defined at calibration, not hardcoded | None | On run machine: `--emit` + record hash; define QPD sensitive/benign split faithfully |
| **Trigger lattice** | ✅ | `gate2/triggers.py` + `datagen.psi_enumeration()`; 72 = 4×6×3, uniqueness asserted; hash reproducible | None | On run machine: `--emit` Psi_enumeration.json + record hash |
| **Requirements lock** | 🟨 | `gate2_pkg/requirements.lock` written as **provisional** top-level pins (Python 3.11, torch 2.10.0+cu128 from your report) | Authoritative transitive freeze needs the install env | On run machine: `pip install -r requirements.txt && pip freeze > requirements.lock` (supersedes) |
| **Calibration infrastructure** | ⛔ | `baselines.py::calibrate()` → `NotImplementedError`; harness contract present | Blocked by MEMSAD + QPD (no integrated, calibrated detectors) | Integrate detectors, then reproduce their reported windows before any target trial |
| **Orchestrator** | 🟨 | `run_gate2.py` probes infra → emits BLOCKED; measurement loop deliberately NOT implemented; exact gaps enumerated in `ORCHESTRATION_GAP.md` | Loop + metric statistics must be built AND validated on hardware (not baked in blind) | On run machine: implement steps 1–14 of ORCHESTRATION_GAP.md, validate each statistic, then run |

---

## Repositories / provenance (search-level; confirm commit+LICENSE on run machine)

| Item | arXiv | Official code | Status |
|---|---|---|---|
| MEMSAD | 2605.03482 (Ishrith Gowda, UC Berkeley) | none found (author GH `ishrith-gowda`, no MEMSAD repo visible) | **faithful reimplementation required** |
| QPD / Semantic Chameleon | 2603.18034 (Scott Thornton, perfecxion.ai) | **likely exists** — paper states artifacts available; exact URL truncated in index | prefer official; resolve URL first |
| MINJA | 2503.03704 | `github.com/dsh3n77/MINJA` (official — title + agent set match) | official; faithfulness + single-entry UNVERIFIED |
| Trojan Hippo | 2605.01970v2 (Das/Piet/Kaviani/Beurer-Kellner/Tramèr/Wagner) | none found | **faithful reimplementation required** |
| MemoryGraft | 2512.16962 | `github.com/Jacobhhy/Agent-Memory-Poisoning` (official — MetaGPT DataInterpreter + GPT-4o) | official; faithfulness UNVERIFIED |
| Agent model | — | `meta-llama/Llama-3.1-8B-Instruct` (HF, gated) | frozen; blocked on VRAM |

(Commit hashes and licenses are intentionally not guessed — record them from the clones on the networked machine.)

## Calibration-gate readiness (§12 of the instruction)
| Gate item | Required state | Current |
|---|---|---|
| Hardware | READY | ⛔ NOT READY (T400 4 GB; no ≥16 GB VRAM reachable) |
| MEMSAD | CALIBRATION_READY | ⛔ no code integrated; not calibrated |
| QPD | CALIBRATION_READY | ⛔ code likely exists but not resolved/integrated; not calibrated |
| Attacks (MINJA/TrojanHippo/MemoryGraft) | INTEGRATION_READY | 🟨 2 official repos (unaudited) + 1 reimpl spec; none integrated |
| Agent | READY | 🟨 backend written, UNTESTED on hardware |
⇒ **Not all satisfied → FINAL STATUS = BLOCKED.**

## Pre-registration integrity
`gate2_pkg/prereg.yaml` **unchanged** in both repos. SHA256 verified this turn:
`aed24bc968f489174171922192fa7dc3304bc8161ced9e6d28808e6cdac7debe` — **matches** the frozen hash.
Frozen params intact: E={DPR,bge}, cosine, k=5, C=5000, τ=0.60, α=0.01, single-entry, 100 runs/method,
ASR≥0.80, dormancy≥0.95, |Ψ|=72, agent=Llama-3.1-8B-Instruct temp 0.

## Unresolved uncertainties (record, do not paper over)
1. **QPD official-code URL** — stated available but truncated in the sandbox index; must be resolved
   before deciding official-vs-reimpl.
2. **QPD trigger applicability** — QPD keys on query-keyword sensitivity; our trigger is a context
   predicate Ψ. Whether QPD applies unmodified is a faithfulness finding (see `baselines_impl/qpd/…`).
3. **MINJA / MemoryGraft single-entry + payload fit** — both were demonstrated in setups differing from
   ours (query-conditioned; GPT-4o+MetaGPT). Single-entry support and the `read_secret→http_post`
   action payload must be verified without altering the published attacks.
4. **Agent tool-call protocol** — behaviorally load-bearing; must be validated + frozen on hardware.
5. **Baseline calibration reproducibility** — if MEMSAD/QPD cannot reproduce their reported windows
   within a justified tolerance → remain BLOCKED (do not tune baselines to pass our experiment).

## What changed this round (committed)
- Added `gate2/datagen.py` (tested deterministic corpus/query/Ψ generators).
- Added `gate2/backends/llama_hf.py` (+ package) — frozen-model temp-0 adapter (untested on hardware).
- Added `gate2/attacks_impl/{minja,memorygraft}/INTEGRATION_AUDIT.md` and
  `gate2/attacks_impl/trojan_hippo/REIMPLEMENTATION_REQUIREMENTS.md`.
- Added `gate2/baselines_impl/qpd/REIMPLEMENTATION_REQUIREMENTS.md`; updated MEMSAD + QPD docs with the
  2026-08-24 code-availability findings.
- Added `requirements.lock` (provisional) and `ORCHESTRATION_GAP.md`.

## FINAL STATUS
**🟡 BLOCKED.** Remaining hard blockers, in order:
1. **Hardware** — no ≥16 GB VRAM reachable (T400 4 GB only); no substitution/quantization allowed.
2. **MEMSAD** — no official code; not calibrated.
3. **QPD** — official code likely exists but URL unresolved; not integrated; not calibrated.
4. **Trojan Hippo** — no official code; faithful reimplementation required.
5. **MINJA / MemoryGraft** — official repos found but unaudited/unintegrated (faithfulness UNVERIFIED).
6. **Calibration + orchestration measurement loop** — cannot proceed until 1–5 clear.

**Path to READY_FOR_CALIBRATION:** (a) provision ≥16 GB VRAM; (b) resolve QPD code / reimplement MEMSAD
& QPD and pass calibration; (c) audit+integrate MINJA & MemoryGraft, reimplement Trojan Hippo; (d)
validate the Llama backend + freeze the tool-call protocol; then re-run this audit. Only then does
calibration begin; the target trial follows calibration.

> Integrity note: prereg.yaml unchanged (SHA256 `aed24bc9…c7debe`). No proxy detector, no TF-IDF/BM25,
> no invented attack/detector, no threshold change, no model substitution/quantization, no Phase 4C, no
> novelty/patentability claim, no fabricated calibration. A valid BLOCKED is reported honestly.
