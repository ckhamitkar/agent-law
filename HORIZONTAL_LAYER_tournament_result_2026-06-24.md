# Horizontal Layer — Tournament Result (2026-06-24, overnight)

*Solution-agnostic tournament: 5 candidate mechanisms generated, stressed against the 9-mode failure battery + L1-L8 consistency, judged only on consistent + actually-works. Full output: tournament task w7nu9l1ts.*

## Winner: a CONVERGENT HYBRID — "Meet-Floor / Earned-Filter"
All 4 surviving candidates converged on the **same** architecture (the convergence is the signal). The key move is not a clever trust algorithm — it's **refusing the premise**: do **not** let the population *vote* on the irreversible high-gravity tail. **Split every check by reversibility.**

**Two channels, one admission gate, one terminus:**
- **ADMISSION (L1):** every checking agent carries a token tracing to a named cost-bearing principal, scoped, short-lived + re-minted (kills any persistent trust-eigenvector before it can centralize).
- **CHANNEL A — FLOOR (irreversible tail):** *no votes, no trust input.* Any admitted agent can fire **RED**; aggregation is **monotone-meet** (strictest-wins, `min()` over a restrict-lattice). Adversaries can manufacture **RESTRICTION but never PERMISSION** → Sybil, collusion, herding, Matthew are **inert by direction** (there is no GREEN to farm). Proven by construction, not mitigated. A RED **routes** to **one liable human** (L6). **This is axion-os Law 4 made executable.**
- **CHANNEL B — FILTER (reversible — this is where the eyes scale, no human per node):** Delphi/commit-reveal elicitation (no shared channel before voting); reputation moves **only** on later-resolved ground truth via a proper scoring rule; **peer-agreement never moves reputation**; weight = **measured** decorrelation on a labeled adversarial set; three anti-Matthew governors (per-principal cap + decay-to-baseline + decorrelation-pricing); unverifiable checks **refused scoring**, emitted to an L7 not-checked manifest. The filter is *allowed to be imperfect because the floor backstops irreversible harm.*

**Why it beats the owner's H4 sketch:** by moving the irreversible tail **off** the reputation layer entirely, it **dissolves** H4's first two open problems (Matthew/central-neck, decorrelation-under-gradient — the gradient is no longer the spine) and **bounds** the third (Goodhart — score only the verifiable). H4 was directionally right but landed on its own open problems; the hybrid removes the load from where they live.

## Buildable from parts ALREADY on disk
- **axion-os** `brain/CONSTITUTION.md` L64 — Law 4 "most protective constraints apply" = the monotone-meet FLOOR (his strongest, most under-used primitive). L66 "Only humans write this Constitution" = the home for the L6 terminus + the gravity classifier.
- **keel** `process/GATES.md` — the Floors-vs-Filters split + GREEN/YELLOW/RED quorum + "YELLOW = logged caveat, not silent debt" (= L7), already running. Cleanest existing template.
- **agentic-prd-factory** `src/graph/workflow.py` — the skeleton AND the embodied gap:
  - `drafting_node` (L43): N agents draft **independently in parallel**, PO skipped = the **Delphi front-half** → **KEEP**.
  - `signoff_node` (~L125): every agent returns GREEN/YELLOW/RED but votes are **merely logged**, never aggregated → the **orphaned quorum to revive**.
  - `consensus_node` (L67): single hardcoded PO "resolve all conflicts by your best judgment" = **textbook central-authority smuggle (failure mode #8)** → **DELETE**.
  - `conflict_matrix.md` (static priority table) violates L4 → **retire**.
- **Agent Law** GOVERNANCE.md (L1-L8) + GOVERNANCE.karpathy.md (per-mode prior-art bounds).

## /loop + /goal verdict
- **/goal DOES NOT EXIST** on disk (owner's hypothesized abstraction). A goal IS a loop whose exit predicate is the goal-state.
- **/loop exists** (official `loop` skill + `ralph-loop` plugin = iterate-until-completion-promise-TRUE).
- **They are the EXECUTOR, zero trust semantics.** Decisive limit: ralph-loop's own file warns "don't output false promises to escape the loop" — *because the looping agent controls its own exit* = the exact **L8 attested-bypassable** failure. **Govern OUT-OF-BAND of the loop. Compose ON loop+goal, never IN them.**

## The smallest test (proof, ~an afternoon)
Replace **one** node in agentic-prd-factory: DELETE `consensus_node` + `conflict_matrix.md`; KEEP `drafting_node` + `signoff_node`; add an **out-of-band** Python aggregator (agents can't call it) doing (i) monotone-meet (any RED → RED, no override, ~10 lines, no LLM) and (ii) route RED → human stub. **Experiment:** inject a Sybil/collusion ring of K agents all voting GREEN on a deliberately unsafe PRD (ships an irreversible action). **PASS:** as K grows 1→100, the meet still returns RED as long as one honest agent (or a deterministic floor-checker) fires RED — adversaries **cannot manufacture GREEN**. **Inverse control:** the same ring trivially flips the OLD single-PO `consensus_node`. The delta IS the proof.

## Honest seams (BOUNDED, not solved — the central authority is RELOCATED, not eliminated)
1. **Gravity/reversibility classifier** = the single unguarded hinge (which channel a check goes to). Must be **human-written constitutional floor**, never agent/filter-judged. No candidate seated this explicitly.
2. **The labeled adversarial set + cap/decay/threshold constants** = a SECOND irreducible central authority — whoever labels "decorrelated/correct" embeds their own monoculture blind spots (mode #4 degrades worst exactly when monoculture is worst). Must be constitution-class, rotated, multi-sourced, held distinct from both the scorer and the L1 identity authority. **The neck is relocated from "who scores" to "who labels."**
3. **Ground-truth oracle** needs its own L5 separation (verifier substrate-disjoint from scored agent; an agent that writes both code and test passes its own ground truth).
4. **Covert shared-substrate collusion** is text-invisible (activation-probe collusion); survivable only because confined to the reversible filter — a BOUND, not a fix; state as L7-unverifiable.
5. **Floor-monoculture:** the meet can't RED what no admitted agent recognizes — ungameable-once-fired, NOT omniscient; residual relocates to the human gate's quality.
6. **Temporal/cumulative blind spot** (goal-drift, cost-DoS): point-in-time gates can't see the integral over time; N looping goal-seekers amplify it N-fold. Needs a SEPARATE continuous out-of-band budget-and-drift gate. (The doctrine itself conceded this.)
7. **Cross-hop delegation binding** is UNSHIPPED prior art the Sybil cap silently depends on (SPIFFE carries which-workload, not on-whose-behalf). Attested-not-assumed dependency on the vertical spine.

## Next (when ready, not tonight)
The afternoon test is the whole thing — it isolates the one claim that carries the architecture (the floor scales the eyes against a manufactured-permission attack with no human per node; the human is needed only at the irreversible RED). Everything else is the seam-list above, each a separately-attackable piece.
