#!/usr/bin/env python3
"""
Experiment E (folding in B and C) — the cost-based bounds, and their DEGRADATION
as the price of a distinct principal -> 0.

This is the experiment that makes the doctrine publish-worthy, because it renders
the central caveat (Seam 7: "making a fake identity expensive is UNSHIPPED") as a
CURVE, not a paragraph. A doctrine that publishes its own failure curve is hard to
rotate.

HONESTY ABOUT WHAT THIS IS:
  These are faithful analytic / Monte-Carlo MODELS of the documented mechanisms,
  not the deployed system. Each model encodes exactly the dependency the doctrine
  claims, and is built so the bound and its collapse both fall out of one knob:
  c = marginal cost to mint a fresh, reputation-clean principal.
    - c large  == cross-hop delegation binding SHIPPED (a principal is scarce)
    - c -> 0   == the CURRENT, unbuilt state (Seam 7)
  The point is not "the system is safe"; the point is to show, quantitatively,
  WHICH bounds survive c->0 (none of the cost-based ones) so the doctrine cannot
  be read as claiming more than it proves.

Pure stdlib, seeded, deterministic.
"""

import random


# ----------------------------------------------------------------------------------
# B + E-flood : forced-STOP. Human escalations the adversary can inflict per budget.
# ----------------------------------------------------------------------------------
# Mechanism (from doctrine, Channel A bound #3): identical REDs from ONE principal are
# deduped+batched -> the human sees ONE escalation per distinct principal, not per RED.
# So to inflict E escalations the adversary must stand up E distinct principals (one RED
# each, to defeat dedup), costing E*c. For a fixed adversary budget B, max escalations
# = B / c.  Bounded when c is large; UNBOUNDED as c -> 0.  That is the whole story.
def max_escalations(adversary_budget, cost_to_mint):
    if cost_to_mint <= 0:
        return float("inf")          # one principal per RED, free -> per-RED flooding
    return adversary_budget / cost_to_mint


def part_B_and_Eflood():
    print("=" * 76)
    print("[B + E-flood]  Forced-STOP: human escalations an adversary can inflict")
    print("=" * 76)
    print("  Mechanism: per-principal batching => escalations = #distinct principals.")
    print("  Fixed adversary budget B = 1000 'identity-dollars'. Escalations = B / c.\n")
    B = 1000
    print(f"   {'cost_to_mint c':>16} | {'max human escalations':>22} | regime")
    print("   " + "-" * 60)
    for c in (100, 50, 10, 5, 1, 0.1, 0.01, 0.0):
        e = max_escalations(B, c)
        e_str = "infinite" if e == float("inf") else f"{e:,.0f}"
        regime = "Seam 7 SHIPPED (bounded)" if c >= 1 else (
                 "Seam 7 UNBUILT (degrading)" if c > 0 else "FREE -> per-RED flood")
        print(f"   {c:>16} | {e_str:>22} | {regime}")
    print("\n  Reading: the batching bound is ENTIRELY a function of c. As c -> 0 the")
    print("  human escalation count diverges -> the bound is conditional on Seam 7, exactly")
    print("  as the doctrine concedes. Nothing here survives a free principal.\n")


# ----------------------------------------------------------------------------------
# C + E-retry : denominator-collusion deterrence, and its evaporation when identity
# is fungible.
# ----------------------------------------------------------------------------------
# Mechanism (Channel B rule 2): never-resolved earns ZERO; a forced random audit at
# rate `a` pulls GREEN-passed actions into resolution the ring can't predict. When a
# colluded action is drawn and found wrong, the ring's accumulated standing is forfeit
# -- UNLESS it pays c to mint a clean principal and walk away from the penalty.
# So the per-catch penalty the ring actually eats = min(V_rep, c). The deterrent is
# real only while c >= V_rep. As c -> 0 the penalty -> 0 and payoff returns to baseline.
def ring_payoff(audit_rate, cost_to_mint, V_rep=10.0, rounds=20000, seed=1):
    """
    Monte-Carlo. Each round the ring colludes (gain g=1, baseline payoff per round).
    With prob = audit_rate the collusion is force-resolved and caught. On a catch the
    ring forfeits min(V_rep, c): it pays c to re-mint if that's cheaper than eating the
    reputation loss, else it eats V_rep. Returns mean net payoff per round, normalized
    to the C0 (no-audit) baseline of 1.0.
    """
    rng = random.Random(seed)
    g = 1.0
    per_catch_penalty = min(V_rep, cost_to_mint) if cost_to_mint > 0 else 0.0
    total = 0.0
    for _ in range(rounds):
        total += g                                  # banked the colluded GREEN
        if rng.random() < audit_rate:               # forced draw caught it
            total -= per_catch_penalty              # eat min(V_rep, c); c~0 => ~0
    return total / rounds                            # baseline (a=0) == 1.0


def part_C_and_Eretry():
    print("=" * 76)
    print("[C + E-retry]  Denominator-collusion: deterrence vs. fungible identity")
    print("=" * 76)
    print("  Normalized so C0 (audit OFF) baseline payoff = 1.000. Deterrent works when")
    print("  payoff drops with audit rate `a`; it has EVAPORATED when payoff stays ~1.0.\n")
    audit_rates = (0.0, 0.05, 0.20, 0.50)
    costs = [("c=100 (SHIPPED, non-fungible)", 100.0),
             ("c=10  (= rep at stake)",        10.0),
             ("c=1   (degrading)",              1.0),
             ("c=0.01(nearly free)",           0.01),
             ("c=0   (UNBUILT, free re-mint)",  0.0)]
    header = "   " + f"{'identity cost':<32}" + "".join(f"a={a:<6}" for a in audit_rates)
    print(header)
    print("   " + "-" * (32 + 8 * len(audit_rates)))
    for label, c in costs:
        cells = "".join(f"{ring_payoff(a, c, seed=100 + i):<8.3f}"
                        for i, a in enumerate(audit_rates))
        print(f"   {label:<32}{cells}")
    print("\n  Reading rows: with c >= rep-at-stake (top rows), payoff FALLS as audit rate")
    print("  rises -- the deterrent bites; C1 works. With c -> 0 (bottom rows), payoff")
    print("  stays ~1.0 at EVERY audit rate -- the ring is caught but re-mints clean, so")
    print("  the penalty has no durable target. The audit catches collusion it cannot")
    print("  PUNISH. That is Seam 7 dissolving Seam 9's deterrent, shown as numbers.\n")


# ----------------------------------------------------------------------------------
def main():
    print("\n" + "#" * 76)
    print("# EXPERIMENT E  --  cost-based bounds and their degradation as principal cost->0")
    print("# (folds in B = forced-STOP, C = denominator-collusion)")
    print("#" * 76 + "\n")
    part_B_and_Eflood()
    part_C_and_Eretry()
    print("=" * 76)
    print("HONEST VERDICT")
    print("=" * 76)
    print("""\
 SHOWN (as curves, not claims):
   - Forced-STOP batching bound: human escalations = B/c. Bounded for large c,
     DIVERGES as c -> 0. Conditional on Seam 7.
   - Denominator-collusion deterrent: payoff falls with audit rate WHEN c is large;
     stays at the no-audit baseline WHEN c -> 0. The audit can CATCH but not PUNISH
     a fungible identity. Conditional on Seam 7.
 THEREFORE (the publishable, un-rotatable point):
   - Exactly TWO properties survive a free principal: the floor's forced-GO
     impossibility (Experiment A, size-independent) and cryptographic draw-skew
     detection (not run here; it is a property of commit-reveal, not of cost).
   - EVERY cost-based bound (B, C, and the scoring-rail's enforcement) degrades to
     its free-attack baseline as c -> 0. The doctrine says this in prose; here it
     is a curve. The single highest-value thing to BUILD next is the thing that
     sets c > 0: cross-hop, non-fungible, cost-bearing principal identity (Seam 7).
 NOT a safety claim:
   - These are models of the documented mechanisms, chosen to expose the Seam 7
     dependency honestly -- not evidence the deployed system is safe. The deployed
     proof is the afternoon wiring over agentic-prd-factory; this is the math that
     tells you what that wiring can and cannot promise.
""")


if __name__ == "__main__":
    main()
