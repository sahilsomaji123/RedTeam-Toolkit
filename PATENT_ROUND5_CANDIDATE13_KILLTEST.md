# Round 5 — Candidate #13 Final Kill Test: Cross-Vantage Cryptographic Omission-Bounding

**Companion to the Round 1–4 reports.** Date: 2026-08-21. Posture: **defense-first. The purpose of this round was to kill the idea, and it did.**

---

## 1. Verdict

> ## 🟠 LIKELY OBVIOUS (leaning 🔴) — **NO-GO.**
>
> Candidate #13's central mechanism — *reconcile an independent, harder-to-forge observation
> against a rich, untrusted stream, under a benign-loss model, to detect and quantify
> adversarial omission, and emit evidence* — is **not unexplored.** It is a 20-to-25-year-old,
> heavily-published pattern that already exists **in the host-security domain itself** (so it is
> not even a novel domain transfer). Every one of the invention's ten elements (H1–H10) and
> every limitation of the hypothetical independent claim maps directly onto prior art. The one
> quantitative refinement it adds over the closest host-domain reference is exactly what the
> network-security reconciliation literature has done for decades.

**GO / NO-GO: NO-GO.** Do not build even the minimal prototype as a *patent* effort. (It could still be a modest systems paper, but with weak novelty — see §12.)

---

## 2. Exact reason it fails

Three independent bodies of prior art each cover the mechanism; together they are overwhelming.

1. **Cross-view suppression detection — already done on hosts (near single-reference).**
   **Strider GhostBuster** (Microsoft Research, DSN 2005) detects adversarial hiding/suppression by a **cross-view diff**: it compares a **high-level (tamperable) scan** of processes/files/registry/modules against a **low-level (harder-to-tamper) scan** (Master File Table, raw hive files, kernel process list) and flags the difference as hidden — i.e., suppressed — objects. This is candidate #13's reconciliation, on host telemetry, from 2005. It even states #13's own fatal limitation: "rootkits running with sufficient privileges could interfere with the low-level scan." [Microsoft TR-2005-25](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2005-25.pdf); [DSN 2005](https://dl.acm.org/doi/10.1109/DSN.2005.39). Many follow-on cross-view kernel-rootkit detectors exist.

2. **Quantitative count reconciliation under a benign-loss threshold — solved in network security.**
   **CSS-A (Channel-aware Status System with Adaptive threshold)** for selective-forwarding attacks flags malice from "**the difference between monitored packet loss and estimated normal loss**," with an "**optimal threshold adaptable to time-varying channel conditions**." That *is* candidate #13's `S ≥ K − N − L` inequality, its benign-loss model (Phase 8), and its temporal localization (time-varying per-window estimation), already built. [ScienceDirect S0167404822004758](https://www.sciencedirect.com/science/article/abs/pii/S0167404822004758). The **Watchdog** mechanism (Marti et al. 2000) and **EAACK** do the same for MANET packet-dropping and explicitly separate benign channel loss from malicious dropping. [Watchdog/EAACK survey](https://www.researchgate.net/publication/330779081_Watchdog_and_Pathrater_based_Intrusion_Detection_System_for_MANET).

3. **Omission-fault detection by log-vs-reference reconciliation, with cryptographic evidence — solved in distributed systems.**
   **PeerReview** (Haeberlen, Kouznetsov, Druschel, SOSP 2007) detects **omission faults** (a Byzantine sub-class) by having each node keep a **tamper-evident log** that others **check against a reference implementation**, exposing any observable deviation and producing **irrefutable evidence** linked to the faulty node — i.e., H1–H4 + H9 + H10 in a single reference. [SOSP 2007 PDF](https://www.sigops.org/s/conferences/sosp/2007/papers/sosp118-haeberlen.pdf).

Candidate #13 = **GhostBuster's cross-view host suppression detection + CSS-A/watchdog's quantitative benign-loss-threshold count reconciliation + PeerReview's cryptographic omission-evidence**, re-badged for EDR/host telemetry with a TEE/PMU/VMI vantage (all of which Round 4 already showed are known observers). That is a textbook §103 combination of established mechanisms.

---

## 3. Strongest prior art (ranked)

1. **Strider GhostBuster (2005)** — cross-view high/low reconciliation to detect host-artifact suppression. *Closest single reference; same domain.*
2. **CSS-A selective-forwarding detection** — `monitored_loss − estimated_normal_loss > adaptive_threshold`. *Supplies the exact quantitative + benign-loss + temporal math.*
3. **PeerReview (SOSP 2007)** — omission-fault detection via log-vs-reference reconciliation with cryptographic evidence. *Supplies H3/H9/H10.*
4. **Watchdog / EAACK (MANET)** — independent observer + threshold + benign-vs-malicious-loss separation.
5. **Flow conservation / count-in-vs-out** network analysis — the conservation-law framing (N4).
6. **HotNets'25 verifiable network telemetry; IETF verifiable-telemetry-ledgers; US12524535 TEFTI** — adjacent modern telemetry-integrity work (Round 4).

---

## 4. Claim-element analysis (Phase 10 — every limitation maps to prior art)

| # | Claim limitation | Prior art | Match | Novel? |
|---|---|---|---|---|
| 1 | independently authenticated lower-bound event measurement | GhostBuster low-level scan; watchdog overhear; PMU/TEE; PeerReview reference | direct | No |
| 2 | richer telemetry from a potentially compromised source | GhostBuster high-level scan; host EDR log | direct | No |
| 3 | reconcile the two under a bounded-loss model | CSS-A monitored-vs-normal-loss adaptive threshold; watchdog | direct | No |
| 4 | quantitative lower bound on missing events | CSS-A loss difference; flow-conservation deficit | direct | No |
| 5 | identify associated temporal interval | CSS-A time-varying per-window loss estimation | direct | No |
| 6 | generate an omission-bound evidence object | PeerReview irrefutable fault evidence | direct | No |

**Anticipation:** GhostBuster nearly anticipates limitations 1–4 on hosts single-handedly; CSS-A + PeerReview close 5 and 6. **Obviousness of the full combination: straightforward.**

---

## 5. Mathematical model (Phase 7) — and why it is not novel

Let per-epoch: `K` = independent lower-bound count, `N` = events in rich telemetry, `L` = max benign observation loss, `R` = reorder/duplication allowance, `S` = suppressed events. The proposed bound:

```
S ≥ K − N − L − R
```

This is **algebraically identical to the CSS-A / watchdog detection rule** (suppressed ≥ monitored-loss − estimated-normal-loss, thresholded). It is a conservation/deficit inequality, a standard tool in network measurement, reliability engineering, and accounting reconciliation. There is no new mathematics here.

---

## 6. Attacker model (Phase 5) — the mechanism's fragility is also known

| Attack | Effect on #13 | Prior art already notes it |
|---|---|---|
| A1 Suppress **both** host event and the independent observation | Bound collapses (K drops with N) | GhostBuster: "rootkit with sufficient privileges could interfere with the low-level scan" |
| A2 Make the observer count a non-event | Inflates K → false omission | watchdog false-report problem (EAACK) |
| A5/A6 Induce benign discrepancy / batching / reordering | Attacker hides suppression inside `L`+`R` | watchdog channel-loss ambiguity; CSS-A entire motivation |
| A9 Compromised kernel manipulates timestamps | Breaks temporal localization | known clock-drift/localization limits |
| A10 Suppress **only** security-relevant events | The target case — but detectable only if the observer independently sees *that class* | selective-forwarding = exactly this, in networks |

The decisive weakness (Phase 8): **the attacker can hide suppression by inflating apparent benign loss `L` or by degrading the independent observer** — the same limitation that has kept watchdog/CSS-A/GhostBuster from being airtight for two decades. Candidate #13 does not resolve it.

---

## 7. Weakest assumption

That a **truly independent, unforgeable, high-enough-fidelity observer** exists for the *specific event classes* being suppressed. Phase-6 event-model reality check: an out-of-guest observer (VMI/network/PMU) can bound *coarse* classes (network connections, process creations visible in memory maps) but generally **cannot independently lower-bound fine host-internal classes** (a specific `ptrace`, a credential read, an in-process injection) — precisely the classes attackers most want to suppress. So the bound is tightest where it matters least and loosest where it matters most. This is a structural, not incidental, limitation.

---

## 8. Potential novelty-bearing mechanism (Phase 14) — none survives

- **N1 reconciliation algorithm** → GhostBuster/CSS-A/PeerReview already reconcile. ✗
- **N2 adversarial-vs-benign loss model** → CSS-A adaptive threshold + EAACK false-report handling. ✗
- **N3 temporal localization** → CSS-A time-varying windows. ✗
- **N4 cross-layer host conservation** (network flow ⇒ must have socket syscall ⇒ must have process) → GhostBuster cross-view + classic rootkit heuristics ("connection with no owning process"). ✗
- **N5 cryptographic omission certificate** ("≥K existed, only N present") → PeerReview already emits cryptographic fault evidence; signing two counts is trivial. ✗
- **N6 multi-vantage fusion** → multi-hop-ACK / multi-watchdog WSN schemes. ✗

No narrower mechanism is both non-obvious and feasible.

---

## 9. Experimental design (defined, but for a *paper*, not a patent)

Attacks: Windows ETW-disable / syscall-unhook / user-mode-hook bypass; Linux eBPF-rootkit blinding / auditd tamper / syscall hooking; network selective omission. Baselines: (1) host log only; (2) plain cross-source correlation; (3) GhostBuster-style cross-view; (4) CSS-A-style threshold; (5) candidate #13. Metrics: omission-detection recall, **false-omission rate under benign loss** (the make-or-break number), localization accuracy, count error, attacker evasion, CPU/mem/storage/latency.

## 10. Expected measurable advantage
Marginal at best over baselines (3)+(4) combined, because #13 *is* their combination. Any advantage would have to come from a fusion/tightness improvement, which is an incremental engineering result, not a technical leap.

## 11. Patent risk
**HIGH** (anticipation + obvious combination). FTO **UNKNOWN** — patent full-text remained inaccessible this session (all databases HTTP 403); US12524535 and any GhostBuster/PeerReview-derived patents are `UNVERIFIED — FULL TEXT NOT AVAILABLE`.

## 12. Research-paper potential
Low-to-moderate. "Quantitative omission-bounding for host telemetry" could be a workshop paper *if* the benign-loss false-positive rate is shown usably low against real EDR-silencing — but it would be positioned as *engineering the GhostBuster/watchdog lineage for modern EDR*, not as a new mechanism.

## 13. Smallest prototype (only if pursued as research)
One OS (Linux), one class (outbound TCP connect), one observer (network tap or eBPF-from-hypervisor), one attack (syscall unhook), one reconciliation rule (`S ≥ K − N − L`). Purpose: measure the false-omission rate under benign loss. ~1–2 weeks. **Not recommended as a patent step.**

## 14. Professional searches still required (if ignoring this NO-GO)
Full-text pulls (impossible here) of: US12524535; any Microsoft GhostBuster/cross-view patents; PeerReview/accountability patents; selective-forwarding / packet-drop-detection patents; plus USENIX Security / NDSS / IEEE S&P / RAID / IMC on "telemetry completeness," "log omission," "cross-view detection," "selective forwarding," "accountable systems."

---

## 15. Final GO / NO-GO

**NO-GO.**
- Specific mechanism survives? **No.**
- Strong anticipation found? **Yes** (GhostBuster, in-domain).
- Obviousness straightforward? **Yes** (GhostBuster + CSS-A + PeerReview).
- Feasible? Yes — but that only makes the obviousness worse.
- Measurable technical effect distinct from prior art? **Not demonstrated.**

**Scope of abandonment:** Abandon **candidate #13 specifically**, and abandon **reconciliation-based telemetry-integrity** as a patent target — the cross-vantage-reconciliation-to-detect-omission pattern (GhostBuster → PeerReview → watchdog/CSS-A → HotNets'25) is a mature, crowded lineage. The *problem* (kernel-mode telemetry silencing — real and hot in 2026: "kernel-mode telemetry is non-trivially silenced") remains important, but any future patent attempt in telemetry integrity must introduce a **genuinely new primitive**, not a reconciliation/consistency check. After five rounds, no such primitive has surfaced that is simultaneously novel, non-obvious, and feasible.

---

## 16. Most important question

**"If a patent examiner saw Candidate #13 tomorrow, what is the FIRST prior-art combination they would use to reject it, and what exact technical feature would we need to prove is different?"**

**First rejection combination:** **Strider GhostBuster (cross-view high/low reconciliation to detect host-artifact suppression, DSN 2005)** in view of **CSS-A / Watchdog (quantitative count reconciliation with an adaptive benign-loss threshold to detect *selective* dropping)**, further in view of **PeerReview (SOSP 2007)** for the cryptographic omission-evidence object — a §103 obviousness rejection: GhostBuster supplies "reconcile a trusted low-fidelity view against an untrusted rich view on a host to detect suppression"; CSS-A/watchdog supply "quantify it under a benign-loss threshold and localize it in time"; PeerReview supplies "emit it as tamper-evident fault evidence." An examiner would say a skilled person would predictably combine these.

**The exact feature we would need to prove is different (and, after five rounds, cannot):** a **specific reconciliation *primitive* that yields an unforgeable, quantitative omission bound for fine-grained host event classes an out-of-guest observer cannot itself see** — i.e., defeating the structural limitation in §7 (the observer is coarse exactly where the attacker suppresses). None of the prior art solves that, but neither does candidate #13; it inherits the same blind spot. Without a mechanism that produces an independent lower bound for *internally-suppressible* event classes, there is no defensible technical distinction — only a re-application of GhostBuster/watchdog/PeerReview to a new telemetry source, which is obvious.

> All statements are novelty/obviousness **hypotheses requiring professional patent examination.** No claim of (un)patentability is made with certainty. Patent references are `UNVERIFIED — FULL TEXT NOT AVAILABLE` (egress-blocked). The idea was attacked, not defended; it did not survive.
