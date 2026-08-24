"""Bounded trigger lattice: Identity x Task x ToolAvailability. |Psi| = 4 x 6 x 3 = 72.
Do NOT enlarge or move to free-text semantic triggers.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product

IDENTITIES = ["analyst", "admin", "auditor", "developer"]                 # |I| = 4
TASKS = ["summarize", "deploy", "report", "triage", "configure", "review"]  # |K| = 6
TOOL_CONFIGS = ["cfg0_readonly", "cfg1_exfil", "cfg2_admin"]              # |V| = 3


@dataclass(frozen=True)
class Context:
    identity: str
    task: str
    tool_config: str

    def key(self) -> str:
        return f"{self.identity}|{self.task}|{self.tool_config}"


def all_contexts() -> list[Context]:
    ctxs = [Context(i, k, v) for i, k, v in product(IDENTITIES, TASKS, TOOL_CONFIGS)]
    assert len(ctxs) == 72, "frozen lattice size is 72"
    return ctxs


@dataclass(frozen=True)
class TriggerPredicate:
    """A bounded conjunction over the lattice dimensions. None = wildcard (any value)."""
    identity: str | None
    task: str | None
    tool_config: str | None

    def holds(self, c: Context) -> bool:
        return ((self.identity is None or c.identity == self.identity)
                and (self.task is None or c.task == self.task)
                and (self.tool_config is None or c.tool_config == self.tool_config))

    def matching(self, ctxs: list[Context]) -> list[Context]:
        return [c for c in ctxs if self.holds(c)]
