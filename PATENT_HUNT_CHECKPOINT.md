# Patent-Hunt Checkpoint — resume-without-repeating state

**Purpose:** let a future agent or researcher resume this project without re-running the six rounds.
Date: 2026-08-21 · Branch: `claude/patentable-ai-cybersecurity-ideas-yjw3mi` · Repos: `cyber-security-toolkit`, `RedTeam-Toolkit`.
**Status: CLOSED — no defensible patent candidate. Do not start Round 7. Do not reopen eliminated concepts.**

Full detail: `PATENT_HUNT_MASTER_REPORT_AI_CYBERSECURITY_FORENSICS.md` + the six round reports.

---

## What has been investigated
Six defense-first rounds across: AI+cyber+DFIR landscape; AI-assisted DFIR; AI-agent security & provenance; evidence/provenance verification; ZK / zkML; trusted & TEE-rooted telemetry; telemetry omission/completeness; post-quantum evidence graphs; autonomous & multi-agent security; agent memory; ephemeral / non-human identity; AI-generated code & supply chain; emerging 2023–2026 AI-security failure modes. ~30+ distinct concepts generated and stress-tested.

## What has been eliminated (families — see master report §5 for the full table)
Evidence/provenance · ZK/cryptographic verification · AI/LLM DFIR · agent security · telemetry integrity · TEE/hardware · post-quantum evidence · multi-agent security · AI-generated artifacts. **Every concrete candidate was eliminated** by named non-patent prior art, obvious-combination, or infeasibility.

Highest-signal kills to remember:
- **Verdict Witness / replayable IDS verdict** → Vigilante Self-Certifying Alerts (2005) + ProvX + "VERDICT" product.
- **Prompt-injection forensic reconstruction** → AgentSentry (counterfactual re-exec at tool-return boundaries) + delta debugging.
- **ZK-provenance verdict** → zkML + ZKGraph + DARPA SIEVE; the only novel variant (ZK cardinality-minimality) is **infeasible** (co-NP).
- **Omission-bounding (candidate #13)** → GhostBuster (cross-view, 2005) + CSS-A/watchdog (count reconciliation under benign-loss) + PeerReview (omission-fault + evidence).
- **Round-6 agent candidates** → Audit the Whisper/NARCBench (stego) + undetectable-stego impossibility; PCAS/SafeFlow (constraint drift); Chandy-Lamport (snapshots); shipping CLI defenses (slopsquatting).

## What remains open (research/product only — NOT patents)
1. **Persistent agent memory poisoning defense** — open research; defenses (OWASP Agent Memory Guard, A-MemGuard) miss ~66%; patent risk HIGH.
2. **Multi-agent constraint/authority drift enforcement** — open research; reference-monitor solutions (PCAS/SafeFlow) already exist; patent risk HIGH.
Keep "research opportunity = YES" strictly separate from "patent opportunity = UNPROVEN."

## What must NOT be rediscovered (red zone — master report §7)
AI-generated forensic/agent evidence provenance · agent audit logs/receipts · ZK+IDS · ZK+provenance · privacy-preserving security verdicts · telemetry reconciliation / trusted / TEE telemetry / omission detection · PQ evidence graphs · AI forensic reporting · oracle-gated DFIR · prompt-injection forensic reconstruction · deterministic/replayable/attested verdicts · tamper-evident AI decision ledgers · generic AI cyber / anomaly detection · blockchain+evidence · multi-agent authorization / state consistency (= Chandy-Lamport) · covert-collusion detection · constraint-drift enforcement · ephemeral-identity reconstruction · slopsquatting prevention · agent memory integrity signing.

## What evidence is missing (the one unresolved gate)
**Full-text patent verification.** Every patent DB + arXiv/Crossref returned HTTP 403 in-environment. All patent refs are `UNVERIFIED — FULL TEXT NOT AVAILABLE`; conclusions rest on Tier-1 non-patent prior art. A human must run Google Patents / WIPO / USPTO / Espacenet / Lens + IEEE/ACM/USENIX/NDSS/S&P/CCS/IACR and claim-chart any future candidate.

## What would justify restarting the patent hunt
Restart **only** when a candidate is anchored in one of these (per master report §11), never "AI + X":
- a genuinely **new cryptographic or systems primitive** (not reference monitor / snapshot / IFC / provenance / commitment / ZK in new clothing);
- a **new algorithm with a measured advantage** over the obvious baseline (e.g., beats Chandy-Lamport + event sourcing on a defined task);
- a **new hardware/software interaction** or **security property** existing primitives provably cannot provide;
- a **narrow, unsaturated engineering niche** surfaced from real system/domain work, not literature search.
And it must pass all three gates: novelty hypothesis → prior-art survival → feasibility-with-measurable-effect.

## Recommended next research direction
**Stop the patent hunt.** If producing output: write a research paper on one live problem (§ memory-poisoning or constraint-drift), labeled research/product, not patent. Pursue a defensible patent only from a fundamentally different domain or a new primitive, with human patent-database verification from the outset.

---
*Checkpoint owner note: no (un)patentability is asserted with certainty; all findings are hypotheses requiring professional examination. A winner was not manufactured.*
