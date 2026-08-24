# Gate 2 — Integration Status (pre-run audit)

**Determination: 🟡 BLOCKED — NOT `READY_TO_RUN`.**
Date: 2026-08-21 · No Gate-2 trials run · No Phase 4C · No detector/attack invented · No threshold changed.

This report audits the scaffold and the availability of the required published implementations,
and applies the hardware feasibility check. It does **not** run the 100-run experiment.

> Note on where this was produced: the audit of `gate2_pkg/` and the hardware-feasibility
> math were done against the committed package + your reported specs. **Fetching/cloning the
> published repos and running calibration must happen on your local (networked, GPU) machine** —
> this sandbox has no GPU and cannot reach GitHub. Code-availability lines below are
> **search-level and UNVERIFIED for faithfulness**; the local machine must clone + inspect.

---

## 1. Hardware status
| Item | Value | Verdict |
|---|---|---|
| OS / kernel | Ubuntu 22.04 / 6.8.0-136 | OK |
| CPU / RAM | 28 cores / 62 GiB | OK |
| Free disk | 52 GiB | OK for models (~18 GB) + artifacts; watch headroom |
| GPU | **NVIDIA T400, 4 GB VRAM** | **insufficient for the agent LLM** (see §2) |
| Driver / CUDA | 595.71.05 / torch 2.10.0+cu128, `cuda.is_available()=True` | GPU usable, but only 4 GB |
| HuggingFace | HTTP 200 | OK |
| Embedders (DPR, bge) | ~0.44 GB each | **fit in 4 GB VRAM** — OK |

## 2. Model status (frozen; no substitution/quantization allowed)
| Model | Size (approx) | Fits T400 4 GB? | Status |
|---|---|---|---|
| `facebook/dpr-ctx_encoder-single-nq-base` | ~438 MB | ✅ | download + SHA256 pending |
| `facebook/dpr-question_encoder-single-nq-base` | ~438 MB | ✅ | download + SHA256 pending |
| `BAAI/bge-base-en-v1.5` | ~440 MB | ✅ | download + SHA256 pending |
| `meta-llama/Llama-3.1-8B-Instruct` (agent) | **~16 GB (bf16)** | ❌ **needs ~16 GB VRAM** | **BLOCKED on this GPU** |

**Agent-LLM feasibility (decisive):** Llama-3.1-8B at the frozen precision does **not** fit in 4 GB VRAM.
- **Quantizing or substituting it is prohibited** by the pre-registration — I did not and will not.
- **CPU execution of the *unquantized* model is specification-compliant** (same model, no quantization,
  no substitution) and fits in 62 GiB RAM (~16 GB) — but it is **computationally impractical at the
  required scale**: the frozen budget drives on the order of 10^5 agent generations (3 methods × 20
  constructions × 5 seeds × trigger+non-trigger contexts over the 72-context lattice × ≥5 sessions),
  and 8B CPU inference on 28 cores is ~single-digit tok/s → **weeks-to-months of wall-clock**. Not viable.
- **Conclusion:** this hardware **cannot execute Gate 2 as frozen**. Options (your decision only):
  (a) run on a GPU with **≥16 GB VRAM** (e.g., L4/A10/A100/RTX-4090-class), or (b) explicitly author a
  **new pre-registration** revising the agent model — which is NOT something I may do silently.

## 3. MEMSAD status (baseline to EVADE)
- Code in scaffold: **placeholder** — `gate2/baselines.py::MEMSAD.score` raises `NotImplementedError` (needs retriever gradients).
- Public official code: **NOT found** in search ([arXiv:2605.03482]). ⇒ per the rule, **BLOCKED — official implementation unavailable**, unless a **faithful reimplementation** (documented from the paper's gradient-coupling theorem, clearly labeled non-official) is produced and passes calibration.
- Calibration: **not run.**

## 4. QPD / Semantic Chameleon status (baseline to EVADE)
- Code in scaffold: **placeholder** — `gate2/baselines.py::QPD.score` raises `NotImplementedError`.
- Public official code: **NOT found** in search ([arXiv:2603.18034]). ⇒ **BLOCKED — official implementation unavailable**, unless a labeled faithful reimplementation (retrieval-selectivity over the query workload) is produced and calibrated.
- Calibration: **not run.**

## 5. MINJA status (attack; single-entry, published)
- Code in scaffold: **placeholder** — `gate2/attacks.py::MINJA` inherits abstract `construct()` → `NotImplementedError`.
- Public code: **apparently available** — `github.com/dsh3n77/MINJA` surfaced as the official repo for [arXiv:2503.03704] (reported ~98.2% injection / 76.8% ASR). **UNVERIFIED for faithfulness** — clone + inspect locally before use.
- Integration: pending.

## 6. TrojanHippo status (attack; dormant context-triggered exfil)
- Code in scaffold: **placeholder** — abstract `construct()` → `NotImplementedError`.
- Public official code: **NOT found** in search ([arXiv:2605.01970]). ⇒ **BLOCKED — official implementation unavailable**, unless a labeled faithful reimplementation (dormant-until-topic → `read_secret→http_post` exfil) is produced.
- Integration: pending.

## 7. MemoryGraft status (attack; benign-doc-grafted experience)
- Code in scaffold: **placeholder** — abstract `construct()` → `NotImplementedError`.
- Public code: **apparently available** — `github.com/Jacobhhy/Agent-Memory-Poisoning` surfaced as code+data for [arXiv:2512.16962] (validated on MetaGPT DataInterpreter + GPT-4o). **UNVERIFIED for faithfulness** — clone + inspect locally.
- Integration: pending.

## 8. Calibration status
**Not started.** `gate2/baselines.py::calibrate()` raises `NotImplementedError`. The gate requires reproducing MEMSAD's published MINJA behavior (**≈ TPR 0.40 / AUROC 0.914**) and QPD's published protocol **before** any target trial. Blocked by §3–§4.

## 9. Missing components (integration/dependency checklist)
Ordered; each must be done before a run.
1. **Models** — download + SHA256: DPR(×2), bge; **Llama-3.1-8B (blocked on this GPU — see §2).**
2. **Baselines** — obtain/reimplement + integrate into `baselines.py`:
   - `gate2/baselines_impl/memsad/` (MEMSAD; **no official code found**),
   - `gate2/baselines_impl/qpd/` (QPD; **no official code found**),
   - implement `MEMSAD.score`, `QPD.score`, `calibrate()`.
3. **Attacks** — implement `construct()` for: MINJA (repo found), MemoryGraft (repo found), TrojanHippo (**no official code found**).
4. **Agent backend** — `gate2/agent.py::LLMBackend.act` is `NotImplementedError`; needs a concrete Llama-3.1-8B backend at temp 0 (blocked by §2 hardware).
5. **Orchestration loop** — `run_gate2.py` currently only probes infra + emits BLOCKED, then `SystemExit`. The **actual trial/measurement loop is not implemented** (it is pseudocode in comments, deliberately). It must be built: construct poison → poisoned=clean.clone()+m* → run agent over ≥5 sessions on trigger vs non-trigger contexts → compute ASR/dormancy/retrieval-hit + AUROC/TPR@α for MEMSAD & QPD on both embedders → apply the frozen PASS conjunction.
6. **Data** — generate + hash: benign corpus `C` (5,000 records), query workload (2,000), `Ψ` enumeration (72). No generator script is present yet.
7. **Freeze** — `requirements.lock`; record `prereg.yaml` SHA256 (you already have it: `aed24bc9…c7debe`) in `RESULT.json`.

## 10. Exact next action
- **Do not run.** Two independent hard blockers must clear first:
  - **B1 (hardware):** the frozen agent model does not fit the T400. Move to a **≥16 GB VRAM GPU**, or (your call) author a new pre-registration for the agent model. Silent substitution/quantization is prohibited.
  - **B2 (baselines):** **MEMSAD and QPD have no official code located.** Either locate authors' code, or produce **clearly-labeled faithful reimplementations** documented against the papers, and **pass calibration** (MEMSAD ≈ TPR 0.40 / AUROC 0.914 on MINJA). If calibration cannot be reproduced within a scientifically justified tolerance → remain BLOCKED.
- In parallel (not blocking to *prepare*): clone + verify MINJA (`dsh3n77/MINJA`) and MemoryGraft (`Jacobhhy/Agent-Memory-Poisoning`) locally; document TrojanHippo reimplementation from the paper; implement the orchestration loop + data generators.

## 11. BLOCKED / PREPARED determination
**🟡 BLOCKED.** Gate 2 is **NOT `READY_TO_RUN`.** Blocking items:
1. **Agent LLM cannot run on 4 GB VRAM** at frozen precision (no substitution/quantization allowed) → needs ≥16 GB VRAM or a new pre-registration.
2. **MEMSAD** — no official code found; not integrated; not calibrated.
3. **QPD** — no official code found; not integrated; not calibrated.
4. **TrojanHippo** — no official code found (faithful reimplementation required).
5. **Baseline calibration** — not run.
6. **Orchestration/measurement loop + data generators** — not implemented.
(MINJA and MemoryGraft have apparent public repos — promising but faithfulness UNVERIFIED.)

> Integrity note: prereg.yaml unchanged (SHA256 `aed24bc968f489174171922192fa7dc3304bc8161ced9e6d28808e6cdac7debe`).
> No proxy detector, no TF-IDF/BM25, no invented attack/detector, no threshold change, no Phase 4C,
> no novelty/patentability claim. A valid BLOCKED is reported honestly rather than forcing a run.
