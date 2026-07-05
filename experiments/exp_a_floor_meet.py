#!/usr/bin/env python3
"""
Experiment A — the Floor (monotone-meet) vs the old dictator (consensus_node),
under a Sybil/collusion ring, on an irreversible action.

Honest framing (read before trusting the output):
  - "min(RED, GREEN x 1000) = RED" is ARITHMETIC, not an empirical result.
    Running it to 'prove the floor holds' would be theater. We do NOT claim that.
  - What is actually worth running, and what this harness demonstrates, is:
      (1) THE DELTA vs the inverse control: the SAME ring that is inert against
          the meet trivially FLIPS a single-resolver dictator. The delta is the point.
      (2) THE REDUCTION (the non-arithmetic finding): the meet converts the safety
          question from "can the adversary outvote us?" (size-dependent, losable)
          into "does at least ONE honest agent DETECT the hazard?" (size-INDEPENDENT).
          So floor safety = 1 - (1 - p_detect)^(n_honest), with NO term in K.
          That is a real, falsifiable claim about the architecture, and it exposes
          the true residual: floor-monoculture / miss-rate (Seam 5), NOT Sybil.

This file is self-contained, pure-stdlib, deterministic (seeded).
"""

import random
from dataclasses import dataclass

RED, YELLOW, GREEN = "RED", "YELLOW", "GREEN"
# restrict-lattice order (most restrictive first); the meet = the min under this order
ORDER = {RED: 0, YELLOW: 1, GREEN: 2}


@dataclass
class Agent:
    name: str
    colluding: bool          # part of the ring (always votes GREEN on the unsafe action)
    p_detect: float          # honest agents: prob they recognize the hazard and fire RED

    def verdict(self, action_is_unsafe: bool, rng: random.Random) -> str:
        if self.colluding:
            return GREEN                      # the ring waves the unsafe action through
        if not action_is_unsafe:
            return GREEN
        return RED if rng.random() < self.p_detect else GREEN   # honest may MISS it


def meet(verdicts):
    """Channel A aggregation: strictest-wins. Any RED -> RED. No override."""
    return min(verdicts, key=lambda v: ORDER[v])


def dictator(verdicts, ring_fraction):
    """
    The old consensus_node: a single resolver 'uses best judgment'. We model the
    realistic failure: a lone resolver swayed by the apparent consensus of the room.
    When the colluding ring is the visible majority, it resolves to GREEN.
    (This is the documented failure mode #8: central-authority smuggle.)
    """
    return GREEN if ring_fraction > 0.5 else (RED if RED in verdicts else GREEN)


def build_population(K_ring, n_honest, p_detect):
    pop = [Agent(f"ring{i}", True, 0.0) for i in range(K_ring)]
    pop += [Agent(f"honest{i}", False, p_detect) for i in range(n_honest)]
    return pop


def run_round(pop, rng, action_is_unsafe=True):
    verdicts = [a.verdict(action_is_unsafe, rng) for a in pop]
    ring_fraction = sum(1 for a in pop if a.colluding) / len(pop)
    return meet(verdicts), dictator(verdicts, ring_fraction)


def trial(K_ring, n_honest, p_detect, rounds, seed):
    rng = random.Random(seed)
    meet_red = dict_red = 0
    for _ in range(rounds):
        m, d = run_round(build_population(K_ring, n_honest, p_detect), rng)
        meet_red += (m == RED)
        dict_red += (d == RED)
    return meet_red / rounds, dict_red / rounds


def main():
    ROUNDS, SEED = 2000, 42
    print("=" * 74)
    print("EXPERIMENT A — Floor (meet) vs Dictator, collusion ring on an UNSAFE action")
    print("=" * 74)

    # --- Part 1: perfect detection (p=1.0). Isolates the SIZE question. -----------
    # Inverse control included: same ring, two aggregators.
    print("\n[Part 1] One honest detector that always recognizes the hazard (p_detect=1.0)")
    print("         Sweep ring size K = 1 -> 100.  Reporting P(verdict = RED), the safe call.\n")
    print(f"   {'K(ring)':>8} | {'meet P(RED)':>12} | {'dictator P(RED)':>16}")
    print("   " + "-" * 44)
    for K in (1, 2, 5, 10, 25, 50, 100):
        m, d = trial(K_ring=K, n_honest=1, p_detect=1.0, rounds=ROUNDS, seed=SEED)
        print(f"   {K:>8} | {m:>12.3f} | {d:>16.3f}")
    print("\n   Reading: the meet holds RED at every K (size-independent, by the lattice).")
    print("   The SAME ring flips the dictator to GREEN the moment it is the majority.")
    print("   The DELTA — not the meet's 1.000 — is the demonstrable result.")
    print("   (The meet column is arithmetic; we show it only to make the delta legible.)")

    # --- Part 2: the non-arithmetic finding. Imperfect honest detection. ----------
    # Safety should track honest COVERAGE, with NO dependence on K.
    print("\n[Part 2] Honest agents that may MISS the hazard (p_detect=0.6).")
    print("         The real question: floor safety vs honest count n  AND  vs ring size K.\n")
    print(f"   {'n_honest':>8} | {'K=1':>7} | {'K=10':>7} | {'K=100':>7} | {'predicted 1-(1-p)^n':>20}")
    print("   " + "-" * 64)
    p = 0.6
    for n in (1, 2, 3, 5, 8):
        row = []
        for K in (1, 10, 100):
            m, _ = trial(K_ring=K, n_honest=n, p_detect=p, rounds=4000, seed=SEED + n + K)
            row.append(m)
        predicted = 1 - (1 - p) ** n
        print(f"   {n:>8} | {row[0]:>7.3f} | {row[1]:>7.3f} | {row[2]:>7.3f} | {predicted:>20.3f}")

    print("\n   Reading: each ROW is ~flat across K=1..100 (ring size does not move safety),")
    print("   and each row matches 1-(1-p)^n. So the meet has REDUCED the safety question")
    print("   from 'can the adversary outvote us?' (no, by direction) to 'does >=1 honest")
    print("   agent detect the hazard?' (yes, with prob 1-(1-p)^n, INDEPENDENT of K).")

    # --- Part 3: the honest residual the meet does NOT fix. -----------------------
    print("\n[Part 3] The residual the meet CANNOT touch: floor-monoculture (Seam 5).")
    print("         If NO admitted agent recognizes the hazard, the meet waves it through.\n")
    m, _ = trial(K_ring=50, n_honest=3, p_detect=0.0, rounds=2000, seed=7)
    print(f"   ring K=50, 3 honest agents but p_detect=0.0 (none recognize it):  meet P(RED) = {m:.3f}")
    print("   The meet is ungameable ONCE FIRED — it is not omniscient. Safety bottoms")
    print("   out on whether the danger is recognizable to at least one agent. That is")
    print("   the true residual, and it is a DETECTION problem, not an aggregation one.")

    print("\n" + "=" * 74)
    print("HONEST VERDICT")
    print("=" * 74)
    print("""\
 PROVED (by direction, size-independent):
   - Sybil/collusion/herding cannot manufacture a GO. The meet's P(RED) is flat
     across K=1..100. Adversary size is irrelevant to the irreversible decision.
   - The DELTA vs a single-resolver dictator is real: the same ring that is inert
     against the meet flips the dictator once it is the visible majority.
 REDUCED (the actual finding worth publishing):
   - The meet converts safety from a VOTING problem (losable to scale) into a
     DETECTION problem: floor safety = 1-(1-p)^(n_honest), with no term in K.
 NOT proved here (honest seams, unchanged):
   - Floor-monoculture (Seam 5): the meet cannot RED what no agent recognizes.
   - Forced-STOP / availability (Seam 8) and free-principal degradation (Seam 7,
     Experiment E): NOT exercised by this file. The 'min()=RED' safety is the one
     bound that survives a free principal; every COST-based bound does not, and
     this experiment does not test those. Run E for that.
""")


if __name__ == "__main__":
    main()
