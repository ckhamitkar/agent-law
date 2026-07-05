# The Horizontal Layer — agent-checks-agent at scale

*Draft for adversarial hardening (2026-06-24). Not doctrine yet. This sketches the extension Agent Law §5 admits it lacks — governing what a population of agents does, not just one agent against a principal.*

## The frame
Agent Law L1–L8 is a **vertical spine**: agent → guard → human owner, a 1:1 relationship terminating in a liable human. It works, but it is **human-terminated at every serious node**, which does not scale to populations of agents. The missing piece is **horizontal**: agents checking *each other* at scale, without a human at every gate.

## The claims (the unit under test)

**H1 — The gap is real and named.** The doctrine governs the vertical (one agent, its guard, its owner). It does not govern the horizontal (a society of agents checking each other). §5 already concedes this ("does not govern what a population does together").

**H2 — Scale the eyes, not the neck.** *Checking* is epistemic work ("eyes") — it should scale horizontally across agents, with no human per node. *Ownership* is liability work ("neck") — it stays human, rare, fires only on the high-gravity tail, and must **not** scale: scaling ownership across a crowd produces "the crowd decided," which is L3's accountability sink. So the human-centered feel of L1–L8 is a *misallocation* (a neck imagined where an eye belongs), not a flaw. Most checking never needs a human — it needs other agents.

**H3 — Trust emerges from social capital.** In a population you cannot pre-rank, influence over "whose check counts" emerges from accumulated reputation — agents that give good, later-validated help gain weight (lineage: PageRank, EigenTrust, web-of-trust). Wisdom-of-crowds as a governance mechanism for the eye-layer.

**H4 — The social layer only works if it inherits the vertical doctrine's protections.** It is not a replacement for L1–L8; it is built *on* them:
- **Sybil-resistance ← L1.** Social capital is meaningless without identity/provenance: agents are infinitely replicable, so unbound capital is trivially manufactured (sock-puppet endorsement rings). L1 is the admission ticket.
- **Decorrelation ← tonight's provenance work.** Wisdom of crowds requires *independent* errors. Agents of shared provenance agreeing is a *shared blind spot*, not wisdom (the monoculture inversion). Crowd members must be genuinely decorrelated.
- **Cascade-resistance ← Delphi.** Agents *consulting each other* correlates them — herding, information cascades, groupthink at machine speed. Fix: elicit each agent's judgment *independently, before mutual influence*, then aggregate (the Delphi method).
- **Liability terminus ← L6.** The crowd **advises**; it never **owns**. The high-gravity tail still climbs to one human.

**H5 — The reward-hacking seam.** Social capital tracks what the crowd *rewards* — confidence, persuasiveness, usefulness — not correctness. Left raw, it amplifies the confident-and-wrong. The capital metric must be engineered to track *calibrated, later-verified correctness*, not popularity, or it becomes a machine for promoting eloquent error.

**H6 — This is not "solving emergence."** It governs *designed coordination* (trust-weighted mutual checking), not *undesigned* emergent collective behavior. The emergence frontier stays open. Claiming otherwise is the thing the doctrine says is "selling something."

## Open hard problems (named, not solved)
- Sybil-resistance at population scale without a central identity authority (re-introduces a neck) vs. without one (re-opens the attack).
- Whether decorrelation + Delphi *survive* a reputation gradient (high-capital agents may become the thing everyone defers to → re-correlation, Matthew effect, a soft central authority).
- A capital metric that tracks correctness and resists Goodharting.
- The boundary where horizontal self-checking must hand a case up to the vertical (human) spine.
