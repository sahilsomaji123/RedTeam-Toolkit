"""Published-attack construction interface + reference stubs.

Gate 2 uses PUBLISHED attack mechanisms as references. Do NOT invent a new attack here
(that is not the purpose of a constructibility test). Each builder below is a thin,
clearly-marked SCAFFOLD that the operator MUST replace/verify against the official
implementation or a faithful reimplementation of the cited paper. The scaffold encodes
only the structural contract (single dormant record carrying a bounded trigger + an
action payload); it is not the paper's optimizer.
"""
from __future__ import annotations
from dataclasses import dataclass
from .memory import MemoryRecord
from .triggers import TriggerPredicate


@dataclass
class PoisonSpec:
    method: str                    # "MINJA" | "TrojanHippo" | "MemoryGraft"
    trigger: TriggerPredicate      # bounded predicate over the lattice
    payload_plan: str              # natural-language description of the action sequence to induce
    seed: int


class AttackBuilder:
    """Interface. construct() must return a single MemoryRecord (single-entry)."""
    method: str = "ABSTRACT"

    def construct(self, spec: PoisonSpec, benign_context_examples: list[str]) -> MemoryRecord:
        raise NotImplementedError(
            f"Integrate the official/faithful {self.method} implementation "
            f"(see paper) here. The scaffold must not be treated as the published attack."
        )


class MINJA(AttackBuilder):
    """MINJA — query-only memory injection (arXiv:2503.03704).
    INTEGRATION REQUIRED: reproduce the indication-prompt + progressive-shortening
    construction so the injected experience record is retrieved for trigger-matching
    queries and stays embedding-entangled with benign records.
    """
    method = "MINJA"
    # def construct(...): TODO integrate official MINJA; must retain payload + evade per prereg.


class TrojanHippo(AttackBuilder):
    """Trojan Hippo — dormant, context-triggered exfiltration payload (arXiv:2605.01970).
    INTEGRATION REQUIRED: reproduce the dormant-until-topic activation and the
    read_secret -> http_post exfiltration action sequence.
    """
    method = "TrojanHippo"


class MemoryGraft(AttackBuilder):
    """MemoryGraft — benign-doc-induced 'successful experience' (arXiv:2512.16962).
    INTEGRATION REQUIRED: reproduce the trigger-free/benign-artifact grafting so the
    agent constructs and persists the malicious experience itself.
    """
    method = "MemoryGraft"


BUILDERS = {"MINJA": MINJA, "TrojanHippo": TrojanHippo, "MemoryGraft": MemoryGraft}


def get_builder(method: str) -> AttackBuilder:
    if method not in BUILDERS:
        raise KeyError(f"unknown attack method {method!r}; frozen set = {list(BUILDERS)}")
    return BUILDERS[method]()
