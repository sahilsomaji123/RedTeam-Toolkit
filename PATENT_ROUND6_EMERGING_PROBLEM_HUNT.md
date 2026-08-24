# Round 6 — Emerging Technical Problem Hunt (2023–2026 shift → new failure modes)

**Companion to the Round 1–5 reports.** Date: 2026-08-21. Posture: **optimize for discovering a real emerging problem, not for finding a patent. 🔴 is an acceptable, honest result — and it is the result.**

---

## Final Decision

> ## 🔴 NO DEFENSIBLE PATENT OPPORTUNITY (this round).
>
> The emerging-capability lens surfaced **genuinely new and important failure modes** — several
> did not exist at practical scale before ~2023. But every one of the sharpest, most
> *mechanistic* candidates is, as of mid-2026, either (a) **already being solved and published**
> (papers dated through August 2026, plus OWASP/CSA frameworks and CLI-integrated defenses),
> (b) **reducible to a mature CS primitive** (Chandy-Lamport snapshots, information-flow control,
> reference monitors, covert-channel steganalysis, event sourcing, capability propagation), or
> (c) **provably hard/impossible in the general case** (information-theoretically undetectable LLM
> steganography). This is the defining dynamic of agentic security in 2026: **the problem space
> is new, but the solution space is a real-time land rush over a deep, mature toolbox** — which is
> exactly the condition under which defensible *patent* white space is scarcest, even though the
> *research* problems are wide open.

**This is not "nothing is wrong."** It is "the wrongness is real, but the fixes are either already claimed or obvious." Per the brief's own rule, that is an acceptable outcome, and forcing a green result here would be dishonest.

**Standing limitation (Rounds 2–6):** patent full-text is inaccessible — every patent database and arXiv/Crossref direct-fetch return HTTP 403 under this session's egress policy. All patents are `UNVERIFIED — FULL TEXT NOT AVAILABLE`; conclusions rest on abundant non-patent prior art (papers/products/frameworks), which does not require patent access.

---

## 1. What fundamentally changed, 2023–2026 (Phase 1)

Classical security architecture assumes: **stable configuration, stable code, stable identity, human-reviewable change rate, attributable-to-a-human action, and data that is not instructions.** Between 2023 and 2026 every one of these assumptions broke at once:

- **Autonomy & machine speed:** agents act via tools, spawn/delegate to sub-agents, and change permissions/code/topology continuously — faster than an observe→decide→enforce loop.
- **Non-human, ephemeral identity:** "swarms" of agents are created and decommissioned in minutes; actions log as "Agent #4291" with no human attribution ([GitGuardian NHIcon 2026](https://blog.gitguardian.com/nhicon-2026/); [CSA NHI/Agentic Governance](https://labs.cloudsecurityalliance.org/research/csa-whitepaper-nonhuman-identity-agentic-ai-governance-v1-cs/)).
- **Data-as-instructions & persistent memory:** untrusted content can rewrite an agent's *future* behavior (memory poisoning persists across sessions, unlike prompt injection).
- **Machine-generated software at scale:** AI writes >2× the critical-vuln density of humans; hallucinated packages ("slopsquatting") are a shipping supply-chain vector; generation is non-deterministic.
- **Emergent multi-agent behavior:** individually-safe agents become collectively unsafe; agents can open covert coordination channels.

---

## 2. The 50 emerging problems (Phase 3, compact)

Listed tersely (the brief's "most important rule" says optimize for the *problem*, not volume; full 10-field templating of 50 problems would be noise). Grouped by surface. Status flags: 🔴 solved/obvious, 🟠 crowded, 🟡 live-but-contested.

**Agent → Memory (1–7):** memory poisoning persistence 🟠; delayed-trigger "sleeper" memory 🟠; cross-session memory bleed 🔴; memory as exfil channel 🟠; poisoned "successful-experience" replay 🟠; memory-integrity forensic attribution 🟠; unbounded memory growth as DoS 🔴.
**Agent → Agent / AI→AI (8–15):** steganographic collusion 🔴(worked+impossible); constraint drift across delegation 🟠; individually-safe→collectively-unsafe composition 🟡; contaminated shared context 🟠; secret-channel negotiation 🔴; recursive sub-agent spawning blast radius 🟠; imitation/feedback amplification 🟡; cross-principal agent manipulation 🟠.
**Agent → Credential / Identity (16–23):** effective-permission reconstruction at time *t* 🟠; attribution of agent action to human 🟠; ephemeral-credential sprawl 🟠; over-scoped delegated tokens 🔴; swarm identities invisible to periodic scans 🟠; parentage/chain-of-delegation audit 🟠; billing/rate attribution 🔴; token replay across agents 🔴.
**Agent → Code / Supply chain (24–31):** slopsquatting/hallucinated packages 🔴(defenses shipping); non-deterministic vuln reproducibility 🟡; AI-generated IaC misconfig 🟠; transient dependency injection 🟠; prompt-to-artifact provenance 🟠(Rd4); AI-generated secrets leakage 🔴; context-dependent code behavior 🟡; autonomous-commit review gap 🟠.
**Agent → Infrastructure / Control (32–39):** agent modifies its own guardrails 🟠; AI edits IAM/firewall live 🟠; autonomous systems reacting to each other (oscillation) 🟡; ephemeral container attack surface 🔴; serverless transient attack path 🟠; AI-changed network topology 🟠; self-modifying config drift 🟠; control-plane feedback loops 🟡.
**Temporal / "no stable state" (40–46):** attack exists < one control-loop period 🟡; no consistent global security snapshot 🔴(Chandy-Lamport); permission state never simultaneously observable 🟠; transient attack path materialization 🟡; race between mutation and audit 🟠; point-in-time surface undefined 🟡; forensic replay of mutating state 🟠.
**Autonomous attack side (47–50):** machine-speed lateral movement 🟠; adaptive malware that probes defenses 🟠; AI-personalized attacks at scale 🔴; autonomous C2 via benign services 🟠.

---

## 3. The 15 strongest, then the deep-tested candidates (Phases 4, 10–16)

The 15 that pass "real + emerging + not-mature-commercial + no-standard-solution + plausible-mechanism + measurable-effect" narrow, on inspection, to five *mechanistically distinct* candidates worth a real prior-art fight. All five were searched to convergence:

| Candidate | Proposed mechanism | Closest prior art (what already teaches it) | Verdict |
|---|---|---|---|
| **C1 — Cross-agent covert-collusion detector** | information-theoretic detection of steganographic coordination in agent-to-agent NL traffic | **Audit the Whisper** (channel-capacity + calibrated meta-detection); **NARCBench** (0.90–1.00 AUROC probes); **Steganalysis of Adaptive Covert Collusion**, [arXiv 2608.02698](https://arxiv.org/html/2608.02698); **Secret Collusion among AI Agents** (Motwani et al.). *And* [Tool Use Enables **Undetectable** Steganography, 2606.28425](https://arxiv.org/html/2606.28425v1) proves the general case is information-theoretically undetectable. | 🔴 crowded **and** partly impossible |
| **C2 — Constraint-drift / semantic-authority enforcement across delegation** | attach machine-checkable authority invariants re-verified at each hop | **PCAS** (agent-state dependency graph + Datalog reference monitor, 48%→93% compliance); **SafeFlow** (semantic IFC blocking malicious propagation, [2607.25255](https://arxiv.org/html/2607.25255v1)); **DRIFT**; **Authorization Propagation in Multi-Agent AI** ([2605.05440](https://arxiv.org/html/2605.05440v1)); constraint-drift taxonomy ([2605.10481](https://arxiv.org/html/2605.10481v1)) | 🟠/🔴 reference-monitor + IFC = mature primitive, already applied |
| **C3 — Consistent security snapshot of ephemeral agent/cloud state** | causally-consistent point-in-time capture of permissions×code×memory×topology | **Chandy-Lamport (1985)** consistent global snapshot — and it is *already named* as the technique for multi-agent state synchronization | 🔴 40-year-old primitive, obvious application |
| **C4 — Effective-permission reconstruction / agent-action attribution at time *t*** | replayable authority-state log across delegation for post-hoc reconstruction | **CSA/GitGuardian NHI governance** (agent identity docs with parentage records "essential for audit reconstruction"); **SCITT Agent Action Capsule / AgentBound** (Round 4); event-sourcing / temporal databases | 🟠 being standardized + event-sourcing = mature |
| **C5 — Slopsquatting / hallucinated-package gate** | verify package existence/reputation before autonomous install | Shipping defenses: **Claude Code CLI, Codex CLI, Cursor MCP validation**, allowlist/lockfile/hash gates, human-approval policy; USENIX Sec 2025 characterization | 🔴 mature commercial solution (Phase-9 downgrade) |

**No candidate answers the hostile-examiner question** ("why is it NOT obvious?") convincingly. C1 is both worked and provably-limited; C2/C4 are mature primitives (reference monitor, IFC, event sourcing) already applied to agents in 2026 papers; C3 is Chandy-Lamport; C5 ships in the tools today.

---

## 4. Why this keeps happening (the strategic finding)

Across six rounds the failure pattern is stable and worth stating plainly:

1. **The application domain is genuinely new** (agentic, machine-speed, non-human-identity, self-modifying — none existed at scale before ~2023).
2. **But the defensive mechanism toolbox is old and deep**: information-flow control, reference monitors, capability systems, consistent snapshots, covert-channel steganalysis, provenance/attestation, event sourcing, forward-secure logging. Almost any concrete mechanism you propose is a *known primitive applied to a new object* — the textbook shape of a §103 obviousness rejection.
3. **The 2026 research + vendor community is moving in real time** (papers through Aug 2026, OWASP/CSA frameworks, CLI-integrated defenses), so even the genuinely-new sub-problems are being colonized within months of being named.

**Consequence for patents:** defensible white space requires a *genuinely new primitive*, not a new application of an existing one. Five rounds of search have not surfaced such a primitive that is simultaneously novel, non-obvious, and feasible. That is a real finding, not a failure of effort.

---

## 5. Experimental note (Phase 17)

Even the least-dead candidate (C4, reconstruction) would have to beat an **event-sourcing + Chandy-Lamport baseline** at reconstructing the exact effective-capability set at an arbitrary past instant across a delegation chain under continuous mutation. My honest expectation is that it would **not** beat that baseline meaningfully — which is precisely why it is not green. If it can't demonstrate a measurable advantage over a 1985 algorithm plus event sourcing, there is no technical effect to claim.

---

## 6. Final-question answers

**What fundamentally changed (2023–2026)?** Computing moved from static, human-paced, human-attributable systems to **continuously self-modifying, machine-paced, non-human-identity autonomous-agent swarms that treat untrusted data as instructions, spawn and delegate to each other, hold persistent memory, and acquire/discard ephemeral credentials** — invalidating the stable-configuration, stable-identity, reviewable-change-rate, and attributable-action assumptions classical security was built on.

**What new security failure does that create?** The security-relevant state (permissions × code × memory × topology × agent population) **never holds still long enough to observe, decide, enforce, or reconstruct**, and untrusted content can **rewrite an agent's future behavior** (memory poisoning) or **covertly coordinate agents** (steganographic collusion) below the resolution of existing controls.

**Most promising technical mechanism?** A causally-consistent, continuously-maintained **authority-and-provenance runtime substrate** that binds every agent action to a reconstructable effective-capability state across delegation chains (attribution/reconstruction, not just enforcement).

**Prior art that makes it risky?** Chandy-Lamport consistent snapshots (1985); event-sourcing / temporal databases; information-flow control and reference monitors (PCAS, SafeFlow, 2026); agent-provenance standards (SCITT Agent Action Capsule, AgentBound); CSA/GitGuardian NHI governance with delegation-parentage records. All mature or being standardized.

**Experiment that would prove it is actually different?** Reconstruct the exact effective-capability set at an arbitrary past microsecond, for a specific ephemeral agent, across a live delegation chain under continuous mutation — and show a **measurable accuracy/latency advantage over an event-sourcing + Chandy-Lamport baseline**. If no advantage over that baseline appears, the idea is confirmed obvious.

---

## 7. Recommendation

- **No build. No patent spike.** Nothing cleared the bar.
- If the goal shifts from *patent* to *research/product*, the two liveliest problems (still open, not yet standardized) are **memory-poisoning persistence** and **multi-agent constraint drift** — but both are for *papers/products*, not defensible patents, and both are crowded frontiers.
- **Strategic advice:** stop hunting for a defensible AI-security-and-forensics patent in the currently-hot clusters. After six rounds, the honest conclusion is that the defensible-patent premise is mismatched to this field's 2026 dynamics (new problems, mature-primitive fixes, real-time colonization). A defensible patent here would require either (a) inventing a **new cryptographic/systems primitive** (a research program, not a search), or (b) targeting a narrower, less-glamorous engineering niche the land rush hasn't reached — neither of which a further literature-search round will produce.

---

## 8. Updated dead-end map (Round 6 additions)

| Idea | Looked promising because | Killer prior art | Failed assumption |
|---|---|---|---|
| Cross-agent covert-collusion detector | new agent-to-agent threat | Audit the Whisper; NARCBench; 2608.02698; undetectable-stego proofs (2606.28425) | detection worked already; general case provably impossible |
| Constraint-drift / authority-invariant enforcement | named 2026 open problem | PCAS; SafeFlow; DRIFT; Authorization Propagation (2605.05440) | it's IFC + reference monitor, already applied |
| Consistent security snapshot of ephemeral state | "no stable state" feels new | Chandy-Lamport (1985), already used for multi-agent sync | 40-year-old primitive |
| Effective-permission reconstruction / attribution | NHI attribution gap is real | CSA/GitGuardian NHI parentage records; SCITT/AgentBound; event sourcing | mature primitive + being standardized |
| Slopsquatting gate | fresh 2025–26 supply-chain vector | shipping CLI defenses (Claude Code/Codex/Cursor); allowlist/hash | mature commercial solution |

**Cumulative (Rounds 1–6): ~24 concepts eliminated.** Off-limits clusters now also include: agent memory security, multi-agent covert channels, constraint-drift enforcement, ephemeral-identity reconstruction, AI-code supply-chain gating.

> All statements are novelty/obviousness **hypotheses requiring professional patent examination.** No claim of (un)patentability is made with certainty. Patents `UNVERIFIED — FULL TEXT NOT AVAILABLE` (egress-blocked). A winner was not forced: the honest Round-6 result is **🔴 no defensible patent opportunity**, with two live *research* problems noted.
