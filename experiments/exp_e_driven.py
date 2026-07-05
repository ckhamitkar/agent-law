#!/usr/bin/env python3
"""
Experiment E, DRIVEN -- close the loop exp_e_principal_cost.py left open.

exp_e_principal_cost.py rendered the doctrine's cost-based bounds as a curve in
`c` = marginal cost to mint a fresh principal -- but `c` was a HAND-SET literal
(`for c in (100, 50, 10, ...)`). Seam 7 (seam7_delegation.py) now SHIPS a mechanism
that sets `c`, so this file re-runs the SAME bound math (imported verbatim from
exp_e) with `c` derived from the real proof-of-work knob D.

CORRECTED 2026-07-05: agents run SERVER-SIDE today (the Mac Mini, the harness,
triage-backend's graph). The phone apps are local-AI clients with NO delegation
chain -- so the honest principal-minter is a Mini, not a BoP handset. An earlier
draft of Part 2/3 modeled a poor phone paying PoW; that regressivity is a FUTURE
constraint (activates only when agents go on-device), not the current one. Parts
2/3 now work the actual actors: an honest Mini that mints RARELY (few, long-lived
roots) vs an attacker who must RE-MINT often (to defeat batching + shed reputation),
possibly on rented farm hardware.

  Part 1 -- does driving `c` from a real mint reproduce the degradation curve? (Yes.)
  Part 2 -- server-side, how high can D go before the honest Mini's rare mint stops
            being tolerable, and what does that cost each adversary tier?
  Part 3 -- the softened scissor: PoW server-side bites a casual/single-machine
            adversary hard, but a rented farm still out-hashes one honest node, so
            the deterrent leans on the FREQUENCY the attacker must re-mint, not on
            per-mint cost. A hard wall against a funded farm still needs an
            attestation/authority mint.

Pure stdlib, deterministic. Imports the bound models from exp_e verbatim.
"""

from math import log2
from exp_e_principal_cost import max_escalations, ring_payoff
from seam7_delegation import mint_cost

# --- illustrative, clearly-labelled assumptions (order-of-magnitude, server-side) --
HR_MINI = 1e9        # SHA-256 H/s on a Mac Mini (OpenSSL + hardware SHA extensions)
HR_1GPU = 1e10       # a single commodity GPU
HR_FARM = 1e13       # a rented GPU/ASIC farm the attacker can spin up
FARM_USD_PER_SEC = 1e-3   # rented farm-second, illustrative
V_REP = 10.0         # reputation at stake, in identity-dollars (exp_e default)
HONEST_MINT_OK_SEC = 60.0  # a Mini mints roots RARELY + long-lived, so 60s is fine


def part1_escalation_curve_driven_by_D():
    print("=" * 78)
    print("[Part 1]  Forced-STOP bound, with c DRIVEN by real PoW difficulty D")
    print("=" * 78)
    print("  Reusing exp_e.max_escalations(B, c) verbatim. Attacker budget B fixed in")
    print("  hashes; c(D)=mint_cost(D)=2**D hashes. escalations = B / c(D).\n")
    B_hashes = 2 ** 24
    print(f"   {'difficulty D':>12} | {'c(D)=2**D hashes':>18} | {'max escalations':>16} | regime")
    print("   " + "-" * 72)
    for Dv in (0, 4, 8, 12, 16, 20, 24):
        c = mint_cost(Dv)
        e = max_escalations(B_hashes, c)
        regime = ("Seam 7 UNBUILT (c=1, ~free)" if Dv == 0
                  else "bounded" if e <= 16 else "degrading")
        print(f"   {Dv:>12} | {int(c):>18,} | {e:>16,.0f} | {regime}")
    print("\n  Reading: identical shape to exp_e's hand-set table -- but the x-axis is now")
    print("  a knob you SET (mine to difficulty D), not a number you asserted.\n")


def _mint_seconds(Dv, hashrate):
    return mint_cost(Dv) / hashrate


def part2_server_side_feasible_difficulty():
    print("=" * 78)
    print("[Part 2]  Server-side: how high can D go, and what does it cost each adversary")
    print("=" * 78)
    honest_max_D = int(log2(HONEST_MINT_OK_SEC * HR_MINI))
    print(f"  Honest minter = a Mini ({HR_MINI:.0e} H/s) that mints roots RARELY and")
    print(f"  long-lived, so it tolerates a {HONEST_MINT_OK_SEC:.0f}s one-off mint.")
    print(f"  => feasible difficulty ceiling D_max = floor(log2({HONEST_MINT_OK_SEC:.0f} * {HR_MINI:.0e})) = {honest_max_D}")
    print(f"  Compare: a BoP phone (1e5 H/s, <10s budget) could only reach D~=16. Server-")
    print(f"  side buys ~{honest_max_D-16} more bits of difficulty -- that is the whole change.\n")
    print(f"  Per-mint cost to each adversary tier at D = D_max = {honest_max_D}:")
    print(f"   {'adversary':>22} | {'hashrate':>10} | {'per-mint time':>14} | note")
    print("   " + "-" * 66)
    for name, hr in (("single machine", HR_MINI), ("one GPU", HR_1GPU), ("rented farm", HR_FARM)):
        s = _mint_seconds(honest_max_D, hr)
        s_str = f"{s:.3g} s" if s >= 1 else f"{s*1e3:.3g} ms"
        note = "re-mint hurts (wall-clock)" if s >= 1 else "re-mint is cheap"
        print(f"   {name:>22} | {hr:>10.0e} | {s_str:>14} | {note}")
    print("\n  Reading: at the honest-feasible ceiling, a single-machine or single-GPU")
    print("  adversary pays SECONDS of wall-clock per re-mint -- a real speed-bump. A")
    print("  rented farm pays milliseconds -- PoW does not wall it. The honest party's")
    print("  advantage is not hardware; it is FREQUENCY (Part 3).\n")


def part3_frequency_is_the_lever():
    print("=" * 78)
    print("[Part 3]  The lever is re-mint FREQUENCY, not per-mint hardware cost")
    print("=" * 78)
    honest_max_D = int(log2(HONEST_MINT_OK_SEC * HR_MINI))
    per_mint_farm = _mint_seconds(honest_max_D, HR_FARM) * FARM_USD_PER_SEC
    print(f"  At D_max={honest_max_D}, a farm's per-mint $ = {per_mint_farm:.2g}$ -- far below V_rep=${V_REP:.0f}.")
    print("  So per-mint deterrence FAILS vs a farm. But the attacker doesn't mint once:")
    print("  Seam 8 (defeat batching) forces 1 fresh principal PER flooded RED; Seam 9")
    print("  (shed reputation after an audit catch) forces a re-mint per catch. Aggregate")
    print("  cost = (re-mints) x per-mint. Feed exp_e.ring_payoff the AGGREGATE cost the")
    print("  attacker eats per collusion round, as a function of how many re-mints a round")
    print("  demands:\n")
    print(f"   {'re-mints / round':>18} | {'aggregate $/round':>18} | {'ring payoff @a=0.2':>18} | deters?")
    print("   " + "-" * 72)
    for remints in (1, 1e2, 1e4, 1e6, 3e6):
        agg = remints * per_mint_farm
        payoff = ring_payoff(0.2, agg, V_rep=V_REP, seed=7)   # exp_e's model, verbatim
        deters = "yes" if payoff < 0.5 else "no"
        print(f"   {remints:>18,.0f} | {agg:>17.3g}$ | {payoff:>18.3f} | {deters}")
    print("\n  Reading: even a farm is deterred ONCE the attack it's running forces enough")
    print("  re-mints (the audit + batching machinery is what forces them). PoW's job")
    print("  server-side is to make each of those forced re-mints cost non-zero wall-clock")
    print("  and dollars -- turning Seam 8/9's 'must re-mint' from free into metered. It is")
    print("  a speed-bump that the doctrine's OTHER mechanisms amplify, not a standalone wall.\n")


def main():
    print("\n" + "#" * 78)
    print("# EXPERIMENT E, DRIVEN -- c set by the shipped Seam 7 mint (server-side actors)")
    print("#" * 78 + "\n")
    part1_escalation_curve_driven_by_D()
    part2_server_side_feasible_difficulty()
    part3_frequency_is_the_lever()
    print("=" * 78)
    print("HONEST VERDICT")
    print("=" * 78)
    print("""\
 SHOWN:
   - Seam 7 ships the mechanism exp_e assumed: c is a function of a real knob D, and
     the forced-STOP degradation curve reproduces from it (Part 1).
   - Server-side (today's actual deployment: agents on the Mini, not on phones), the
     honest minter tolerates a far higher difficulty ceiling (~D=35 vs ~16 on a phone)
     because it mints rarely and long-lived (Part 2). PoW there is a real speed-bump
     against a casual/single-machine adversary.
   - A rented farm still out-hashes one honest node, so PoW per-mint does NOT wall it
     (Part 2). The deterrent then rests on re-mint FREQUENCY: Seam 8/9 force the
     attacker to re-mint, and PoW makes each forced re-mint cost non-zero -- deterrence
     returns once the attack demands enough re-mints (Part 3).
 CORRECTED FROM THE PRIOR DRAFT:
   - The "PoW is regressive against the poor BoP phone" claim does NOT apply now --
     agents are server-side; phones are local-AI clients with no delegation. That
     regressivity is a FUTURE constraint, filed for when/if agents go on-device.
 THEREFORE (the decision this hands back to Anjali/Charu):
   - Attenuation + cross-hop accountability ship UNCONDITIONALLY (see test_seam7.py).
   - Cost-source, server-side: PoW is a viable SPEED-BUMP (casual adversaries + the
     frequency lever), NOT a hard wall vs a funded farm. For a hard wall you still
     want a mint the attacker cannot out-hardware: DEVICE ATTESTATION (for the future
     on-device case) or an AUTHORITY MINT (server-side, dents 'zero accounts'). Both
     pluggable behind the same Token/verify boundary.
 NOT a safety claim:
   - Douceur is not repealed. This shows what PoW buys for the current server-side
     deployment and where it stops, not that the fleet is Sybil-proof.
""")


if __name__ == "__main__":
    main()
