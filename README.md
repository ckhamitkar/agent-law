# Agent Law

*The governance of synthetic actors — software that acts, and the liable principal every act must trace to.*

---

We are about to give software the one thing software never had: **agency**.

For seventy years a program did only what it was told, when it was told, and stopped. It had no reach beyond its instruction and no standing beyond its process. That era is ending. An agent acts — on behalf of a person, a company, or, increasingly, on a mandate of its own. It contracts. It transacts. It coordinates with other agents at a speed no human institution was built to follow.

This is the largest expansion of human capability since we learned to pool it. A person is finite — one place, one set of hours, one throughput. An agent carrying that person's authority is their reach made plural and parallel. A health worker who cannot be in ten villages at once can be. A founder who cannot read every contract can. The verb under all of it is the oldest ambition there is: **limited to limitless.**

That is the wonder. Agent Law exists to keep it.

## The orientation

Most writing about governing AI opens in fear, and reads — correctly — as afraid of its own subject. This does not.

Governance built from fear defaults to *deny*: it treats the new actor as a threat to contain, and the limit it was meant to remove creeps back in. Governance built from wonder defaults to *enable*: the gate is a seatbelt that lets you drive faster, not a brake that slows you down. **The care is the compliment.** You do not put a circuit breaker on something trivial — so the governance here is a measure of the value, never a hedge against it.

Limited to limitless is the mission. The governance is only what keeps it both *limitless* and *faithful*.

## The object

Agent Law governs one new thing, and everything else follows from defining it well. To define it honestly, start by conceding what enterprise architecture already does — because the temptation is to overclaim here, and the overclaim is exactly where a framework like this falls apart.

**Software that acts is not new, and the metamodel already holds it.** In ArchiMate, *active structure* is a single concept spanning business actors, application components, and devices alike — the subjects that perform behavior. A software component that fulfills a role and carries out a responsibility is textbook: you draw it with an assignment relationship, and that is how automation has been modeled for years. So an agent as "a deployable component that also performs behavior" is not a hole in the metamodel. It *is* the metamodel. Any framework that claims otherwise is wrong, and a reader fluent in the language will know it on the first sentence.

The gap is narrower, older, and deeper than "a thing that acts." What the metamodel captures is *functional* responsibility — *responsible-for-performing-the-behavior*. What it has never captured, for **any** actor, is *legal* answerability — *accountable-for-the-consequence*. A role says who does the work. Nothing in it says who **answers** when the work causes harm.

It never had to. Every actor the metamodel ever held was anchored to a human or a company that carried its liability *outside* the model — there was always someone who could be sued, fired, or jailed, so the architecture could stay silent and let the world supply the principal. The **Synthetic Actor breaks that silent assumption.** It performs behavior like any active-structure element, but it carries no liability of its own, because it cannot bear a consequence — it has *the discretion of an agent and the answerability of a hammer.* For the first time the metamodel holds a subject that **acts but cannot answer**, and the world no longer hands us the missing principal for free.

So the new object is not "a component that acts." It is **a component that acts and must be bound, explicitly, to a liable principal the metamodel does not currently name.** The honest precedent is not a corporation with a soul; it is humbler and far older — the **dangerous instrumentality**: the thing that acts, causes harm, and cannot answer, for which the law holds the *keeper* strictly liable. The dog bites; the dog cannot be sued; the owner pays, regardless of fault. Agent Law's whole task is to make sure the keeper is always named.

## We did not invent this — we are adapting it

Someone, somewhere, has already solved the hard part of this in another context. The work is to find it and adapt the part that transfers.

Humanity has built a governing structure for "an actor that outlives and exceeds the individual" not once but four times, and they are not four ideas — they are one schema, transmitted four ways:

- **Philosophy** carries the *principle* — the substrate-independent core: justice, agency, obligation. The *why*.
- **Religion** carries the *transmission* — a persistent schema governing ephemeral carriers across millennia, founders long dead, the constraint still binding. Canon and interpretation. Fidelity through belief.
- **Law** carries the *enforcement* — principle made binding for actors who share no beliefs and hold conflicting interests. Precedent is its living memory; the legal person, agency, liability, standing, and conflict-of-laws are its primitives. This is the spine Agent Law is built on.
- **The corporation** carries the *legal person at scale* — and proves the thesis: limited liability was a pure governance invention that *unleashed* an economy rather than caging it.

Agent Law adapts the **conserved layer** of each — the part that holds for any actor with interests and information — and discards the part that was only ever specific to humans, gods, or paper.

## The core move

The liability has to attach to something, and the agent itself is the wrong thing to attach it to — not only because it cannot answer, but because it is barely *there*. It is ephemeral: instantiated, granted a bounded capability, run, and gone before any account could be settled. And here the metamodel falls short a second time. Enterprise architecture is *type-level by design* — it intentionally models the kind of thing, never the individual run — so the ephemeral instance and its lineage are something the language cannot even express.

But while the instance vanishes, its **provenance** persists — the definition it was minted from, the constitution it is bound by, and the liable principal who stands behind it. That is where accountability can live. So the foundational rule of Agent Law is a single inversion:

> **Govern the ephemeral through the persistent.**
> Accountability lives at the provenance layer. Capability flows down to the instance. Nothing the instance does escapes its lineage — and every lineage resolves to a principal who can be held.

From which follows the one law that makes the rest enforceable rather than merely stated: **no orphan agents.** Every act traces to a liable principal. The veil must always exist to be pierced. An agent that traces to no one does not get to act.

## No actor checks itself

The producer cannot be the sole verifier of its own work. Not because it is dishonest — because it tests only for what it thought of, and the failure lives in what it did not. An actor that checks itself has no check at all.

So Agent Law's second enforceable law is the oldest control humanity owns: **separation of duties.** Every consequential action is reviewed by a *structurally separate* actor — an auditor agent — whose loyalty is to the constitution, not to the actor it audits.

This is not novel; it is everywhere humans let an actor act with consequence. Separation of powers in government — the judge is not the prosecutor. Peer review in science. Dev and QA in engineering. The independent audit in finance, made legally binding by Sarbanes-Oxley after the cost of self-checking actors was paid in full. Agent Law installs the same invariant for the synthetic actor.

The verifier must be *other* enough to disagree and *kindred* enough to understand — same lineage, different viewpoint. A clone is an echo, not a check; a stranger cannot read the work. Drawn from the same craft, set in a different seat: **same goal, different viewpoints.** And that separation is itself a Synthetic Actor — governance, at scale, is staffed by auditors whose provenance and duty are structurally divided from the agents they govern.

## The auditor is a competency, not a genius — and it escalates

A separated checker only governs if something reaches for it. Make it cheap and make it constant, and nothing has to: the audit is not a phone call you decide to place, it is a daemon that watches the work as it happens.

Affording that rests on an asymmetry: **verifying is a different skill than producing, and usually a cheaper one.** Checking a proof is easier than finding it. The auditor does not need the producer's intelligence or its context — it needs the *method*. The auditors who walk into a company do not know its chart of accounts; they know what a chart of accounts *is*, what a control is, what independence means, how to sample. They carry the discipline, not the content. A small, local, inexpensive model that holds *how to audit* can watch a far more capable one and still bite.

But the cheap auditor has a ceiling, and the law must state it honestly: **the gravity of a failure sets the floor on how smart its auditor must be.** Mechanical and constitutional violations — a claimed action that never happened, a policy breached, an internal contradiction — a small model catches all day. The subtle failures do not yield to it: the flattery that tests only the convenient seam, the premise that was never falsified, the harm visible only to a peer-grade mind. Those need a checker in the producer's own weight class. The floor is not constant; it rises with the subtlety of the error.

So the auditor layer is **tiered, and escalates by gravity.** A cheap, always-on checker runs the high-frequency, low-gravity stream. When the stakes cross a threshold it does not adjudicate beyond its depth — it **rings the bell**, and a heavier, costlier, more independent auditor is convened in proportion to what is at risk. This is the organization read in reverse: not authority flowing down from the top, but *gravity pulling stronger checkers in from above* — the line worker's review is light, the bet-the-house decision is not left to it. Defense in depth, priced to the danger.

Which names the one skill the cheap auditor cannot do without. It need not be smart enough to catch everything. It must be smart enough to **know what it cannot catch, and escalate.** A junior who flags "this is above me — get a partner" is doing the job exactly right. That is a far lower bar than omniscience, and it is buildable. And every escalation, at its ceiling, terminates where all standing terminates: in a liable human. No tier audits itself; the top tier answers to a person.

## What this is, and is not

- This is a **structure**, not a manifesto. It describes an object and how to govern it. A reader can adopt it; there is nothing here to merely agree or disagree with.
- "Standing" is a **modeling assumption for liability** — *treat the agent as if a legal person so that harm traces back to a principal.* It is not a claim that agents are persons, or should hold rights. The legal fiction is borrowed for its machinery, nothing more.
- The constitution is **canon**; the operating record is **chronicle**. Agents may write the chronicle. **Only humans write the constitution.**

## What follows

The rest of this body of law builds out from the object and the core move:

- the **Synthetic Actor** and its lifecycle — capability, attestation, agency, and the gated writeback of learning to the lineage;
- the **two planes** of governance — *vertical* (provenance and authority, per-instance) and *horizontal* (the substrate that governs emergent, collective behavior no single principal owns);
- the **vial** — a sealed, fast testbed where constitutions are evolved and killed in containment, turning the agents' terrifying speed from a threat into an experimental gift;
- the recurring discipline beneath all of it: *the dangerous property and the enabling property are the same property, and the whole art is the envelope that keeps the upside.*

## Repository map

**Doctrine & orientation**
- [`GOVERNANCE.md`](GOVERNANCE.md), [`GOVERNANCE.karpathy.md`](GOVERNANCE.karpathy.md) — the layered laws (L1–L8), the enforceable spine.
- [`HORIZONTAL_LAYER.md`](HORIZONTAL_LAYER.md) — agents checking agents at scale (the multi-agent plane), with the reversibility axis, the floor/filter split, and the honest, dependency-ranked seams. (`.gan-hardened.md` / `_tournament_result` are the adversarial and tournament variants that produced it.)
- [`SITUATIONAL_MEMORY.md`](SITUATIONAL_MEMORY.md) — the recognition that the governance scorer and the memory scorer are one engine.
- [`RESEARCH_PAPER.md`](RESEARCH_PAPER.md) / [`RESEARCH_PAPER_OUTLINE.md`](RESEARCH_PAPER_OUTLINE.md) — the paper.

**Runnable code** — [`experiments/`](experiments/) (pure stdlib, seeded, deterministic; `python3 -m unittest` → green)
- `exp_a_floor_meet.py` — the strictest-wins floor: forced-GO is impossible at any adversary size.
- `exp_e_principal_cost.py` / `exp_e_driven.py` — the cost-based bounds rendered as a degradation curve.
- `seam7_delegation.py`, `agent_iam.py`, `issuer.py`, `authn.py`, `store.py`, `gateway.py`, `detective.py` — **cross-hop delegation binding + a full agentic IAM**: attenuated capability tokens, attested issuance, proof-of-possession, an authorization gate, an enforcement point, and an out-of-band detective layer.

**Extracted library** — the IAM code above, cleaned into a standalone, self-contained package with its own docs: **[ckhamitkar/agentic-iam](https://github.com/ckhamitkar/agentic-iam)**.

## License

Dual-licensed to fit a repo that is part writing, part code:

- **The written work** — the doctrine, [`RESEARCH_PAPER.md`](RESEARCH_PAPER.md), all Markdown, and the branding graphics — is licensed **[CC BY 4.0](LICENSE)**: reuse and adapt freely, with attribution.
- **The code** — everything under [`experiments/`](experiments/) — is licensed **[MIT](experiments/LICENSE)**.

---

*Agent Law was drafted by a person and an agent, together — itself a small instance of the thing it describes. One is the provenance: persistent, accountable, the will behind the canon. One is the instance: ephemeral, capability on loan, its contribution kept in the chronicle. The arrangement is the point.*
