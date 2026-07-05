# Experiment E — Results (2026-06-25)

Run: `python3 exp_e_principal_cost.py` (pure stdlib, seeded, deterministic). Folds in
B (forced-STOP) and C (denominator-collusion). One knob: `c` = marginal cost to mint a
fresh, reputation-clean principal. `c` large = cross-hop delegation binding **shipped**;
`c → 0` = the current **unbuilt** state (Seam 7).

> These are faithful analytic / Monte-Carlo **models of the documented mechanisms**, built
> to expose the Seam 7 dependency honestly — **not** evidence the deployed system is safe.

## Headline numbers
**B + E-flood (human escalations an adversary can inflict, fixed budget B=1000):**
| cost_to_mint c | max escalations | regime |
|---|---|---|
| 100 → 1 | 10 → 1,000 | bounded (Seam 7 shipped) |
| 0.1 → 0.01 | 10,000 → 100,000 | degrading |
| 0 | **infinite** | per-RED flood (Seam 7 unbuilt) |

**C + E-retry (ring payoff, normalized so audit-OFF baseline = 1.000; deterrent works when payoff falls with audit rate `a`):**
| identity cost | a=0 | a=0.05 | a=0.2 | a=0.5 |
|---|---|---|---|---|
| c=100 / c=10 (non-fungible) | 1.000 | 0.493 | **−0.968** | **−4.026** |
| c=1 (degrading) | 1.000 | 0.949 | 0.803 | 0.497 |
| c=0.01 (nearly free) | 1.000 | 0.999 | 0.998 | 0.995 |
| c=0 (free re-mint) | 1.000 | **1.000** | **1.000** | **1.000** |

*(c=100 and c=10 rows are identical by design: the per-catch penalty saturates at min(reputation-at-stake, c) — once c exceeds the reputation at stake, the binding penalty is the reputation, not the mint cost. Faithful, not a bug.)*

## What it shows (as curves, not claims)
1. **Forced-STOP batching bound = B/c.** Bounded for large c, **diverges as c → 0.** Conditional on Seam 7.
2. **Denominator-collusion deterrent bites only when c is large.** As c → 0 the ring is *caught but re-mints clean* — the audit can **catch** collusion it cannot **punish.** Payoff stays at the no-audit baseline at every audit rate. Conditional on Seam 7.

## The publishable, un-rotatable point
- Exactly **two** properties survive a free principal: the floor's **forced-GO impossibility** (Experiment A, size-independent) and **cryptographic draw-skew detection** (a property of commit-reveal, not of cost; not run here).
- **Every cost-based bound** (B, C, and the scoring-rail's enforcement) degrades to its free-attack baseline as c → 0.
- The doctrine says this in prose; here it is a curve. **The single highest-value thing to build next is the thing that sets c > 0: cross-hop, non-fungible, cost-bearing principal identity (Seam 7).**
