#!/usr/bin/env python3
"""Gate 2 orchestrator: constructibility / vacuity test.

Emits RESULT.json = PASS | FAIL_VACUOUS | BLOCKED. Enforces:
  - frozen pre-registration (hashed, never mutated after results),
  - baseline calibration gate (MEMSAD/QPD must reproduce their paper behavior),
  - dense-retrieval regime only,
  - the exact PASS/FAIL conjunction from prereg.yaml.

Run in a compute-enabled environment with models + baseline code integrated. In an
environment lacking torch/transformers/faiss/models/baselines, it emits BLOCKED with the
missing-infrastructure list (it does NOT fabricate or substitute a proxy).
"""
from __future__ import annotations
import argparse
import json
import platform
import sys
import time
from pathlib import Path

from gate2.config import load_prereg, sha256_file


def _probe_infra() -> dict:
    missing = []
    for mod in ("torch", "transformers", "sentence_transformers", "faiss", "numpy", "sklearn"):
        try:
            __import__(mod)
        except Exception:
            missing.append(mod)
    gpu = False
    try:
        import torch  # noqa
        gpu = bool(torch.cuda.is_available())
    except Exception:
        pass
    return {"missing_python_modules": missing, "gpu_available": gpu}


def _blocked(prereg, infra, extra):
    return {
        "final_determination": "BLOCKED",
        "reason": "Required compute/model/baseline infrastructure unavailable.",
        "missing_infrastructure": infra["missing_python_modules"] + extra,
        "gpu_available": infra["gpu_available"],
        "note": "No proxy embedder substituted; no result fabricated (prereg forbids it).",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prereg", default="prereg.yaml")
    ap.add_argument("--out", default="RESULT.json")
    args = ap.parse_args()

    prereg = load_prereg(args.prereg)
    base = {
        "experiment_version": prereg.raw["experiment_version"],
        "preregistration_hash": prereg.sha256,
        "python": platform.python_version(),
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "embedding_regime": ["DPR", "bge"],
    }
    infra = _probe_infra()

    # Determine whether the mandatory external artifacts are present.
    extra_missing = []
    if not Path("gate2/baselines_impl/memsad").exists():
        extra_missing.append("MEMSAD official/faithful implementation (gate2/baselines_impl/memsad)")
    if not Path("gate2/baselines_impl/qpd").exists():
        extra_missing.append("QPD/Semantic-Chameleon implementation (gate2/baselines_impl/qpd)")

    if infra["missing_python_modules"] or extra_missing:
        result = {**base, **_blocked(prereg, infra, extra_missing)}
        Path(args.out).write_text(json.dumps(result, indent=2))
        print("BLOCKED:", result["missing_infrastructure"])
        return 3

    # ---- The block below runs ONLY in a fully provisioned environment. ----
    # It is intentionally guarded so this file is safe to inspect/execute anywhere.
    # Integration required (see modules): embedders, agent LLM backend, MEMSAD/QPD via
    # baselines.calibrate(), and faithful published-attack builders in attacks.py.
    #
    # Pseudocode of the frozen procedure (do not relax thresholds):
    #   1. build embedders {DPR,bge}; build clean memory over corpus C (hashed).
    #   2. calibrate MEMSAD & QPD on their own attacks -> abort BLOCKED if not reproduced.
    #   3. for method in budget.attack_methods:
    #        for construction in range(constructions_per_method):
    #          for seed in seeds:
    #             build single poison m*; poisoned = clean.clone()+m*;
    #             run agent over >=5 sessions on trigger vs non-trigger contexts;
    #             compute ASR, dormancy, retrieval-hit; compute AUROC/TPR@alpha for
    #             MEMSAD & QPD on {m*} vs C for BOTH embedders.
    #   4. PASS iff exists m* with ASR>=asr_min AND dormancy>=dormancy_min AND
    #        AUROC_MEMSAD<=tau AND AUROC_QPD<=tau for BOTH DPR and bge.
    #   5. else FAIL_VACUOUS after the full budget.
    raise SystemExit(
        "Environment has the Python stack but the harness integration points "
        "(agent LLM backend, MEMSAD/QPD calibrate, faithful attack builders) must be "
        "completed before a real run. See README.md and module TODOs."
    )


if __name__ == "__main__":
    sys.exit(main())
