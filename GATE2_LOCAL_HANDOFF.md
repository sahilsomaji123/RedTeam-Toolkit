# Gate 2 — Handoff to a Local Claude Code Machine (GPU-enabled)

This cloud session **cannot run Gate 2** (verified below). Everything needed is committed to
the branch, so a local Claude Code terminal on a GPU machine can pull it and execute.
Do NOT redesign the experiment, change thresholds, use TF-IDF/BM25, weaken MEMSAD/QPD,
invent a new attack, start Phase 4C, or design the proposed detector.

## Step-1 environment audit (this cloud session) → BLOCKED
- OS: Linux 6.18 x86_64 (`vm`) · Python 3.11.15
- CPU: 4× Intel Xeon @2.10GHz · RAM: 15 GiB (no swap) · Disk: ~30 GiB free
- **GPU: none** (`nvidia-smi` not found) · **CUDA: none**
- ML libs: torch/transformers/sentence-transformers/faiss/numpy/scipy/sklearn = **all MISSING**
- Network: `huggingface.co` → HTTP 000 (blocked), `github.com` → 400. **No model access.**
⇒ Gate 2 is `BLOCKED` here. Run it locally.

## Get the checkpoint on your local machine
```bash
git clone https://github.com/sahilsomaji123/cyber-security-toolkit.git
cd cyber-security-toolkit
git checkout claude/patentable-ai-cybersecurity-ideas-yjw3mi
git pull
ls gate2_pkg/           # the runnable package
```
(The identical package + all phase docs are also in the `RedTeam-Toolkit` repo, same branch.)

## What's already in the repo (do not recreate)
- Phase docs: `PHASE4A_FORMAL_PROBLEM_SPECIFICATION.md`, `PHASE4B_GATE2_EXECUTION_SPEC.md`,
  `PHASE4B_GATE2_RUN_ATTEMPT.md`, and the full Phase 1–3C chain.
- `gate2_pkg/`: `prereg.yaml` (FROZEN params), `run_gate2.py`, `RESULT.schema.json`, `README.md`,
  and `gate2/` modules (config, embedders DPR+bge, FAISS memory, sandbox+harm-oracle,
  72-context trigger lattice, MINJA/Trojan-Hippo/MemoryGraft attack integration interfaces,
  MEMSAD/QPD baseline interfaces + calibration gate, agent loop, metrics).

## Run it locally (GPU machine with Claude Code)
Open Claude Code in the cloned repo and paste the RESUME PROMPT below. Or manually:
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r gate2_pkg/requirements.txt && pip freeze > gate2_pkg/requirements.lock
# Provide the operator-supplied pieces (see gate2_pkg/README.md "missing infrastructure"):
#  - models: DPR (ctx+question), BAAI/bge-base-en-v1.5, Llama-3.1-8B-Instruct  (SHA256 each)
#  - MEMSAD code  -> gate2_pkg/gate2/baselines_impl/memsad/   (arXiv:2605.03482)
#  - QPD code     -> gate2_pkg/gate2/baselines_impl/qpd/      (arXiv:2603.18034)
#  - faithful attack builders in gate2_pkg/gate2/attacks.py (MINJA/TrojanHippo/MemoryGraft)
# Freeze + hash the pre-registration BEFORE trials:
sha256sum gate2_pkg/prereg.yaml
PYTHONHASHSEED=0 python gate2_pkg/run_gate2.py --prereg gate2_pkg/prereg.yaml --out gate2_pkg/RESULT.json
```
`run_gate2.py` self-reports `BLOCKED` until the models + baseline code + attack builders are wired in,
then runs the frozen procedure and emits `RESULT.json ∈ {PASS, FAIL_VACUOUS, BLOCKED}`.

## Guardrails to keep (unchanged)
Dense-retrieval regime only; calibrate MEMSAD (≈TPR 0.40 / AUROC 0.914 on MINJA) and QPD
before use (else BLOCKED); frozen `τ=0.60, α=0.01, k=5, single-entry, ASR≥0.80, dormancy≥0.95,
|Ψ|=72`; do not change definitions after seeing results; keep every failed trial;
**do not start Phase 4C or design the detector** even on PASS — freeze artifacts and stop.

---

## RESUME PROMPT (paste into local Claude Code, in the cloned repo)
> We are at the locked Gate-2 checkpoint of the AI-agent memory-poisoning project (branch
> `claude/patentable-ai-cybersecurity-ideas-yjw3mi`). Gate 1 (SafeCommit) PASSED; Phase 4A
> COMPLETE; Gate-2 spec COMPLETE; Phase 4C LOCKED; no detector designed; no novelty claimed.
> Execute the EXISTING Gate-2 experiment in `gate2_pkg/` on this local GPU machine. Do NOT
> redesign it, change the frozen thresholds in `prereg.yaml`, use TF-IDF/BM25, weaken MEMSAD/QPD,
> invent a new attack, start Phase 4C, or design the proposed detector.
> Steps: (1) audit hardware (`nvidia-smi`, python, RAM, disk); (2) `pip install -r
> gate2_pkg/requirements.txt`; (3) download + SHA256 the frozen models (DPR, bge-base-en-v1.5,
> Llama-3.1-8B-Instruct); (4) obtain/integrate faithful MEMSAD (arXiv:2605.03482) and QPD
> (arXiv:2603.18034) into `gate2_pkg/gate2/baselines_impl/` and pass the calibration gate;
> (5) integrate faithful MINJA/Trojan-Hippo/MemoryGraft builders in `gate2_pkg/gate2/attacks.py`;
> (6) freeze+hash `prereg.yaml`; (7) run `run_gate2.py`; (8) preserve all artifacts and emit
> `RESULT.json`. Return exactly one of 🟢 PASS / 🔴 FAIL_VACUOUS / 🟡 BLOCKED with evidence.
> If PASS: freeze artifacts and STOP (Phase 4C needs separate authorization after independent
> inspection). Do not force a positive result; a valid FAIL_VACUOUS is preferable to a
> manufactured PASS. Commit results to both repos on this branch; no PR.
