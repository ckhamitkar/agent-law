# Experiment A — Results (2026-06-25)

Run: `python3 exp_a_floor_meet.py` (pure stdlib, seeded, deterministic). Floor (monotone-meet)
vs the old single-resolver dictator (`consensus_node`), under a Sybil/collusion ring voting
GREEN on an **irreversible** action.

## What was run
- **Part 1** — perfect honest detection (p=1.0), sweep ring size K=1→100, meet vs dictator (inverse control).
- **Part 2** — imperfect honest detection (p=0.6), safety vs honest count *n* AND ring size K.
- **Part 3** — the residual: no agent recognizes the hazard (p=0.0).

## Headline numbers
| Part | Result |
|---|---|
| 1 | meet P(RED) = **1.000 at every K** (1→100). Dictator P(RED) = 1.000 at K=1, **0.000 once the ring is majority (K≥2).** |
| 2 | each row **flat across K=1,10,100**; matches `1-(1-p)^n` to ±0.01 (n=1→8: 0.60, 0.84, 0.94, 0.99, 0.999). |
| 3 | ring K=50, 3 honest agents, p=0.0 → meet P(RED) = **0.000**. |

## What it PROVES (honestly)
1. **Sybil/collusion/herding cannot manufacture a GO.** The meet's safety is *flat* in K — adversary size is irrelevant to the irreversible decision. (The bare `min()=RED` is arithmetic; the **flat curve next to the dictator's collapse** is the demonstrable delta.)
2. **The reduction — the actual publishable finding:** the meet converts safety from a **voting** problem (losable to scale) into a **detection** problem. Floor safety = `1-(1-p)^(n_honest)`, **with no term in K.** This is empirical (Part 2), not definitional.

## What it does NOT prove (unchanged seams)
- **Floor-monoculture (Seam 5):** Part 3 shows the meet waves through what *no* agent recognizes. Safety bottoms out on detection, not aggregation. Real residual.
- **Forced-STOP / availability (Seam 8)** and **free-principal degradation (Seam 7 / Experiment E):** NOT exercised here. The `min()=RED` safety is the one bound that survives a free principal; every cost-based bound is untested by this file. **Experiment E is the next honest run.**

## One-line takeaway
> The Floor doesn't make the crowd vote correctly — it makes the crowd's *size* irrelevant, and hands the whole safety question to one measurable number: **does at least one honest agent detect the hazard?** That is the floor's strength *and* its only real residual.
