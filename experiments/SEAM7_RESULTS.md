# Seam 7 — Results (2026-07-05)

**Cross-hop delegation binding: the mechanism `exp_e` called "the single highest-value
thing to build next."** Turns `c` (marginal cost to mint a fresh, reputation-clean
principal) from a hand-set literal into a shipped, tested mechanism — and renders the
BoP cost-source problem as a curve instead of a caveat.

Files (pure stdlib, seeded, deterministic):
- `seam7_delegation.py` — the mechanism (+ `python3 seam7_delegation.py` demo)
- `test_seam7.py` — `python3 -m unittest test_seam7 -v` → **16/16 pass**
- `exp_e_driven.py` — reuses `exp_e`'s bound math verbatim, drives `c` from the real mint

> This ships an identity *mechanism*. It does **not** repeal Douceur (2002). It
> instantiates one admissible cost-source and shows which source the BoP constraint admits.

## What ships unconditionally (proven by `test_seam7.py`)
| Property | Test |
|---|---|
| **Attenuation only narrows** — caps AND-fold, TTL/budget min-fold; a "widen" caveat is a no-op | `test_cannot_widen_past_an_earlier_narrowing` |
| **Cross-hop accountability** — root principal survives arbitrary depth, cannot be swapped | `test_root_survives_arbitrary_depth`, `test_cannot_swap_the_accountable_root` |
| **Responsibility = leaf, Accountability = root** — distinct fields, both derived at verify | `test_root_survives_arbitrary_depth` |
| **Forgery / tamper / unknown-caveat rejected (fail closed)** | `test_tampered_caveat_rejected`, `test_forged_identifier_rejected`, `test_unknown_caveat_fails_closed` |
| **PoW-gated minting** — an unminted/under-mined root is not a principal | `test_unminted_root_rejected` |
| **TTL binds at every hop** | `test_expired_token_rejected`, `test_child_ttl_binds_even_if_root_still_valid` |

This is the binding `HORIZONTAL_LAYER §7` called *"unshipped… the next thing to build,
not the next thing to claim."* It is now built and tested. Ports to ed25519/SPIFFE with
no change to the construction.

## What ships conditionally — the cost-source (`exp_e_driven.py`)
> **Corrected 2026-07-05.** An earlier draft modeled the honest minter as a poor BoP
> phone and concluded PoW is fatally regressive. That's wrong for the current system:
> **agents run server-side** (the Mini, the harness, `triage-backend`'s graph); the
> phone apps are local-AI clients with *no delegation chain*. The honest minter is a
> **Mini**. PoW's per-device regressivity is a *future* constraint (activates only when
> agents go on-device), filed not active.

**Part 1 — the degradation curve, now driven by a real knob D** (identical shape to
`exp_e`'s hand-set table, but the x-axis is a parameter you mine to):

| difficulty D | c(D)=2^D hashes | max escalations (B=2^24) |
|---|---|---|
| 0 (Seam 7 unbuilt) | 1 | 16,777,216 |
| 12 | 4,096 | 4,096 |
| 20 | 1,048,576 | 16 |
| 24 | 16,777,216 | 1 |

**Part 2 — server-side feasible difficulty.** A Mini mints roots *rarely* and
long-lived, so it tolerates a ~60s one-off mint → difficulty ceiling **D≈35** (vs ~16 on
a phone). At D=35 a single machine/GPU pays **34s / 3.4s** of wall-clock per re-mint (a
real speed-bump); a rented farm pays **3.4 ms** — PoW does not wall a farm.

**Part 3 — the lever is re-mint FREQUENCY, not per-mint cost.** Per-mint deterrence fails
vs a farm, but Seam 8/9 *force* re-mints (one principal per flooded RED; a re-mint per
audit catch). Feeding `exp_e.ring_payoff` the aggregate cost: a farm is deterred once the
attack forces **≳10^6 re-mints/round** (payoff 1.00→0.31→−1.00). PoW's job server-side is
to make each *forced* re-mint cost non-zero — turning Seam 8/9's "must re-mint" from free
into metered.

## The decision this hands back (Anjali / Charu)
- The cryptographic core is done and unconditional. **The cost-source is a values call.**
- **Server-side (today):** PoW is a viable *speed-bump* — it bites casual/single-machine
  adversaries and, via the frequency lever, meters even a farm — but it is **not** a hard
  wall against a well-funded farm on its own.
- For a hard wall (a cost the attacker cannot out-hardware), both pluggable behind the
  same `Token`/`verify` boundary:
  1. **Authority mint** — a signing service issues roots; simplest server-side, dents
     *zero accounts*.
  2. **Device attestation** (Play Integrity / TEE key) — the answer for the *future*
     on-device-agents case; near-zero honest cost, real attacker cost, dents *zero cloud*.
- Deployed proof (later, not here): wire a verified token as the principal on the
  out-of-band aggregator over a real multi-node graph (`triage-backend/triage/graph.py`),
  per `HORIZONTAL_LAYER §6`.

## Unchanged after this build
Douceur still holds; the two free-principal survivors from Experiment A/E are untouched
(forced-GO impossibility; cryptographic draw-skew detection). Seam 7 converts *every
cost-based bound* from "conditional on an unbuilt mechanism" to "conditional on a values
decision about the cost-source" — a strictly smaller, nameable gap.
