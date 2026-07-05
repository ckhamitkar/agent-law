# Agent Law

*A working doctrine for governing autonomous agents — written plainly, and trimmed to what survived independent audit.*

> We begin where honest work begins: we could be wrong, and we will still try to be right.

This is not a new idea. It is an old pattern — *govern the new entity, unlock its value* — applied to the entity that arrived last. Take it, argue with it, implement it as fits your stakes. The machinery is here; the values are yours to supply.

---

## 1. The pattern

Enterprise architecture has absorbed a new kind of entity four times: **data, services, identities, workloads.** Each time the governance everyone braced for as overhead became the unlock — data governance opened analytics, the service contract opened the API economy, identity opened safe scale, workload policy opened elastic cloud. We never governed these to slow them down. We governed them so we could finally let them run.

AI agents are the fifth. The doctrine below is how you let them run.

## 2. The gap, stated honestly

The easy claim — *"the metamodel has no object for an agent"* — is wrong, and a fluent architect rejects it on the first sentence. In ArchiMate, active structure already spans human actors and software components alike; "a thing that acts" is the metamodel working as designed. Concede this up front or lose the room.

The real gap is narrower and older. EA has always modeled probabilistic actors — humans are the least predictable subjects we draw — and it tamed them not by modeling their behavior but by binding them to a stable **role** and letting the world supply a liable **principal** off the diagram. Two further facts complete the gap:

- The metamodel is **type-level by design** — it has no native object for an ephemeral *instance* or its lineage back to the definition that minted it.
- An agent is **non-stationary at machine speed** — it can shift its own behavior faster than any architecture cycle can re-specify it — and **no human reliably stands behind each act.**

So the novelty is not "an actor that acts." It is an actor that acts, drifts faster than we can re-model it, and **cannot answer** for what it does. That combination is what EA has never held — for any actor.

## 3. The doctrine

Eight laws. Each is implementable; none is a slogan.

**L1 — No orphan agents.** Every deployed agent traces to a named principal that can bear consequence (today: a human or a corporation). This is not new law; it is *respondeat superior* — one who acts through another acts himself. Draw the principal onto the diagram, because nothing off it supplies one for free anymore.

**L2 — Govern the persistent, not the ephemeral.** Don't try to hold the instance; it's gone before you can. Bind accountability to **provenance** — the policy the agent is bound by and the principal behind it — and let capability flow down to the instance.

**L3 — Accountability leaks; closing the leak is the work.** It is *not* conserved. Judgment-proof actors, diffuse harms, and chains that dead-end in an empty pocket are everywhere. Governance is not a guarantee that someone pays — it is the active engineering that makes sure the chain reaches someone who can.

**L4 — The guard is layered, not a rulebook.** A static policy cannot bound an actor that moves faster than you can re-specify it. Compose three layers: a **deterministic floor** for what must never happen (hard stops, irreversible gates), an **adaptive checker** for the open-ended cases a rule can't express, and — at real stakes — an **independent reviewer that does not share the producer's blind spots.** A same-model checker with fresh framing defeats motivated reasoning but not shared-weights blind spots; high gravity demands genuine decorrelation (a different model family, an external ground truth, or a human).

**L5 — Separation of duties.** The guard must be independent of the producer — *assigned to* it, not *part of* it. The audited party may defend and annotate; it may **never veto** an escalation on a flag above trivial gravity. The producer that can talk its own guard down has no guard. L4 and L5 are the same demand on two axes — *epistemic* distance (a guard of different provenance fails differently) and *authority* distance (a guard that cannot be overruled). You need both: veto power with shared blind spots is teeth and no eyes; decorrelation the producer can silence is eyes and no teeth. Neither can be **declared** — only **attested**, on separate evidence, re-measured over time, because capture drifts between the snapshots.

**L6 — Severity-first escalation, terminating on liability.** Most events are gravity-zero; skip them. One foundational flag escalates alone. Two gradients run in parallel and **do not terminate at the same node**: *intelligence* climbs toward the most capable mind; *liability* climbs toward the most answerable one. The chain must dead-end on the liability gradient — a human competent enough for the gravity, never a rubber stamp. The human gate's question is not *"is this correct?"* but *"here is what we could not verify and the harm if it's wrong — are you willing to own it?"* *Who audits the auditor?* The guard is an agent too, so the question recurs — and must terminate, or it runs forever. It terminates by a **change of kind**, not a smarter checker: agent and guard are *epistemic* nodes that can err the same way; the apex is a *liability* node, and **owning** the outcome — not re-checking it — is what ends the chain. Correctness is still bounded by L4 and L5; the apex bounds only answerability. This does not make the apex un-audited — owners are audited too, after the fact, by enforcement, not by another epistemic guard — and the chain closes only if the apex is **reachable and able to bear the cost.** A judgment-proof shell at the top reopens the very leak L3 names.

**L7 — Honest coverage.** Report what was **not** checked. A partial guard that emits a green checkmark is worse than none — it lulls the human out of the vigilance that was the only thing catching what the guard can't see. False assurance is the named enemy.

**L8 — The floor is executable, not narrated.** Prose rules are subject to the same eloquent reinterpretation as any other claim. The things that must be ungameable — the crisis stop, the spend cap, the irreversibility gate — are **code**, not paragraphs. Markdown carries the doctrine; the floor must run.

## 4. What you supply

This doctrine ships the **how**. You supply the **what**:

- Your **gravity map** — what counts as high-stakes in *your* domain. No one else can know it.
- Your **constitution** — the invariants and non-negotiable lines. **Human-written.** This is the canon.
- The **chronicle** — what the system learns over time. Agent-generated, and kept on the other side of a wall from the constitution so learnings never silently become law.

Swap the corpus, not the code. The doctrine is general; the auditor you build from it is specific to your stakes.

## 5. The honest limits

- This governs the **vertical** axis — each agent against a principal. It does **not** govern **emergence**: what a population of agents does together that no one intended. That is still frontier. Anyone claiming to have solved it is selling something.
- A single running instance is a **falsifier, not a validator.** It can prove the shape fails; it cannot prove the shape generalizes. Knowing this auditor works requires labeled, multi-domain evaluation, a measured false-negative rate, and an adversarial red team — not one good demo.
- The decorrelated guard (L4) is **weakest exactly where it is needed most.** In a monoculture — when the available models share a lineage — "a different model family" buys little true independence, and *agreement* between such guards can signal a shared blind spot rather than truth. On the high-gravity tail, lean on real decorrelation — external ground truth or a human — not on models that merely look different.
- It names three things it does **not** yet solve: how to **re-measure** independence as it quietly erodes, where exactly the **gravity threshold** sits that should force producer and apex apart, and how to guarantee the apex can **pay.** Naming a gap is not closing it.
- **This document has been put through independent adversarial review more than once**, by reviewers instructed to break it. Each pass cut claims that could not survive — the confident ones first. What remains is what they could not yet refute. That is not a disclaimer — it is the governance pattern, run on the doctrine itself, and still running.

---

*Drafted by a person and an agent. The audit ran on the argument before the argument ran on you.*
