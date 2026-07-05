# Situational Memory

*The governance/situational engine, read as a unified memory — and why the memory an agent runs on today is a frozen subset of it.*

---

We did not set out to design a memory. We set out to design a governance sensor — a thing that watches an agent's stream of actions, scores each against a norm, and decides what reaches a human. We built it all the way down, and on the last turn it told us what it was: **a memory.** The same machine that decides *"is this action anomalous enough to escalate?"* is the machine that decides *"is this fact novel enough to store, and is this recollection stale enough to distrust?"* One engine, two readings. This note records the recognition, the architecture, and the honest distance between it and the memory a working agent has right now.

## This is a hypothesis — here is how to kill it

Everything below is a *claim*, not a finding. It arrived through analogy — governance felt like memory felt like human cognition — and a triple-convergence that *feels* this clean is exactly the self-hypnosis to distrust. **Convergence is not equivalence.** The feeling of unification is not evidence of it. So before building anything, state the claims as falsifiable hypotheses and name, for each, the observation that would prove us wrong and the cheap test that would surface it. If a claim has no observation that could refute it, it is not part of the design — it is decoration, and it comes out.

**H0 (the null — test this first, and want it to win).** A simple, well-curated *frozen* store plus a manual "re-verify the load-bearing facts" habit captures most of the value at a fraction of the complexity. *Falsified only if* the full engine (segments + slice-stats + lake re-derivation) beats that baseline on a real corpus by a margin worth the machinery. **If the spike cannot beat H0, the elaboration is intellectual pleasure, not engineering** — and the lean-fit-for-purpose spine says ship H0. This is the most likely outcome and the one to chase hardest.

**H1 — One engine, two readings (the unification).** The governance scorer and the memory scorer are the *same* engine. *Falsified if,* when both are actually built, the shared core needs so many special-cases per reading that it is two engines wearing one name — the "unification" carrying no weight in the code, only in the prose. Test: implement both on one core; measure whether removing the shared part breaks both or neither.

**H2a — Novelty = distance-from-norm (the write-gate).** A fact worth storing is one far from what we already hold. *Falsified if* salience and statistical distance turn out weakly correlated — and there is real reason to fear they are: salience is about **consequence**, distance is about **frequency**, and the most important thing to remember is often the most *ordinary-looking* (a quiet one-line preference, a constraint stated once and calmly). Test: label a corpus for "should this have been remembered?" and check whether statistical novelty predicts it. If it scores near chance, distance is the wrong proxy for salience and the write-gate is wrong.

**H2b — Staleness = drift-from-segment (the recall-gate).** A fact gone stale reads as an anomaly against its cohort. *Falsified if* most real staleness is **invisible** to segment-relative scoring — and seam #3 already admits the hole: a fact can stay perfectly typical of its segment and still be false now (the file was deleted; every token rotated together — a whole-cohort drift the cohort-relative view hides). If catching staleness requires going to the lake/world *anyway*, the statistical layer is doing less work than claimed for recall.

**H3 — Reconsolidation beats freezing.** Re-deriving from the lake keeps memory truer than trusting the frozen fingerprint. *Falsified if* re-derivation introduces *more* error than it removes — and human reconsolidation is precisely how false memories form, so this is a live risk: each re-projection is a fresh chance to distort, and the lake itself may be incomplete or biased. Test: measure fact-accuracy under freeze vs. re-derive over N recall cycles; if re-derive degrades, freezing was safer. Second falsifier — **cost**: if re-derivation is so expensive it is never actually run, the design is right on paper and dead in operation (the auditor too costly to convene).

**H4 — Interpretable fingerprints suffice (neural only for unstructured).** The slice-stats vector carries enough signal for structured dimensions. *Falsified if,* on real data, the statistical fingerprint throws away so much that retrieval collapses — you cannot find the analogous situation because the stats discarded what mattered — and only a neural embedding recovers it, at the cost of the auditability that was the whole point. The happy middle between *auditable* and *accurate* may not exist for rich-but-structured data; that is an empirical question, not an assumption.

**H5 — Dreaming finds real edges (the background pass earns its cost).** An offline process that replays the lake and proposes cross-category connections discovers genuine, useful relationships a single online query never would. *Falsified if* the dreamed edges are mostly **spurious** (apophenia — pattern in noise) and the verification needed to separate real from confabulated costs more than the edges are worth; or if a simple periodic-summarization pass ("reflection") captures the same value without the cross-category machinery. Test: have the dreamer propose N edges, have an independent check verify them against the lake, and measure precision; if precision is low *and* verification is expensive, dreaming is rumination with a compute bill.

A claim surviving all of these is still only **not-yet-refuted**, never proven. Treat the seams later in this note as the next round of falsifiers, not as solved.

## The two parts

**1 — The statistical part: the segmented-norm sensor.**

The naive sensor compares an instance to the whole population and cries wolf at every part-time contractor. The real one compares an instance to *its own cohort.* This move has three names — **stratification / mixture modeling** (statistics), **peer-group analysis** (security/UEBA), **segmentation** (marketing) — and they are one move: *don't score against the global mean, score against the segment.*

The algorithm is already an implementable spec:

> see the population → find *k* segments → compute per-slice **sufficient statistics** (counts, means, variances, histograms) → hold them in memory → score each incoming thing against *its segment's* slices.

The virtue is in *sufficient-statistics-in-memory*: you keep counts and moments per slice, never the raw rows. Streaming, cheap, model-free, **no data retained** — and **auditable**, because the verdict is sayable: *"flagged because it is far from segment-3's norm on the dosing slice."* A learned embedding cannot say that; a regulator does not accept "the embedding said so," they accept the slice. Explainability was chosen here without anyone asking for it — which is exactly what a governance floor requires.

The same segment+slice structure has a dual reading: **anomaly** = "far from segment norm" (the governance door); **description** = "here are the segments and their signatures" (targeting, personas). That duality is proof the *engine* is general — not a license to ship two products.

The honest ceiling of this part — **segmentation builds the *substrate* of a knowledge graph, not the graph.** It gives you the nodes, the segments, their statistical proximity: *density and co-occurrence.* A knowledge graph is *typed, semantic edges* — `Drug —interacts_with→ Drug`. Correlation is not yet a typed edge. The edges need a layer on top — an ontology, or a model that *names* the relationship the correlation implies. **Structure ≠ semantics.** This disanalogy recurs at every level of the design; respect it everywhere.

**2 — The semantic part: the lake and the multi-resolution fingerprint.**

Each dimension of a situation is a "sense" of it. Store a representation **at each level** so a cue can retrieve at whatever altitude it addresses — the *gist* of a decade, the *theme* of a year, the *moment* of an event. Some structure nests (org, time); some is flat (independent dimensions); the design carries both. The payoff query is *"have I seen a situation like this, at **this** altitude?"*

Two disciplines decide whether this is real or a black box:

- **Keep the per-level fingerprint interpretable wherever you can.** "Store the situation as an embedding at each level" quietly invites a *neural* vector at each level, and a neural vector is unauditable (latent dim 287 means nothing). For structured dimensions the level's "embedding" should be the **statistical fingerprint** — the slice-stats vector — which you can both retrieve over *and* explain. Reserve neural embeddings for genuinely unstructured content, and keep them **sensors, never the floor.**

- **The deep tension: drift fights recall.** If dimensions change over time, a fingerprint stored last year lives in a *different space* than today's, and nearest-neighbor across them silently returns "similar" situations that are not comparable — the space moved underneath them. You want embeddings that drift (so they stay relevant) *and* embeddings comparable across time (so "have I seen this before" works). You cannot have both naively.

The resolution is the climax of the whole design, and it is borrowed from how humans remember:

> **Preserve the raw situation in a lake. Treat the multi-level fingerprints as derived, re-projectable indices — never the primary store.** When the dimensions drift, you do not migrate frozen vectors; you **re-embed from the lake in the current space.**

That re-derivation *is* **reconsolidation**, and it runs in **two modes.** *Waking* reconsolidation fires **on recall**: re-read the entry in the present moment's terms, in today's space, the instant it is reached for — a human does not retrieve a frozen memory-vector, they *reconstruct* it from a preserved-ish trace and store the reconstruction. That is why memory drifts yet stays usable: it is re-projected into *now* on every recall, and the fingerprint was never the truth, only an index re-derivable from the trace. The contradiction dissolves the instant the embedding stops being primary. *Dreaming* reconsolidation is the other mode — see below — and it is the half a frozen store has never had.

## The whole engine, end to end

> **lake** (raw, preserved, ground truth) → **multi-level interpretable fingerprints**, re-derived on demand, neural only where the data forces it → **retrieval at each level** (mine to surface, drill to navigate, similarity to recall) → **math scores** against the *segmented, drifting* norm → **dreaming**, offline, proposing cross-category edges that a waking auditor verifies before promotion → **floor + human decide.**

A governance agent that remembers across dimensions the way a person remembers across senses — **re-remembers from the trace, in present terms**, rather than freezing the vector, and **dreams** in the down-time to find the connections the waking query never asks for.

## Dreaming: the background pass

On-recall reconsolidation is *waking* memory — it only fires when something is reached for, and so it can only ever refresh what you happen to ask about. The other half runs **offline, unbidden, while nothing is being asked of it** — which is exactly what sleep is for. The brain does not consolidate when you reach for a memory; it replays the day's traces at rest, moving them from the fast, fragile store into the slow, integrated one and stitching them to everything already held. The background pass is that. Call it **dreaming.**

Dreaming earns its place by closing the gap the statistical layer cannot: **segmentation builds the substrate (nodes, densities) but not the typed edges.** Dreaming is where the edges are *proposed.* The offline process replays across categories, notices that something in segment A keeps co-occurring with something in segment C, and floats a candidate relationship no single online query would surface. That is not retrieval — it is the substrate quietly becoming a graph while the system is idle. (It is also, precisely, cross-domain pattern-recombination — *bisociation* — run on a schedule rather than waited on.)

But dreams confabulate, and that is the seam — the same one as everywhere else. An unconstrained background pattern-matcher does not only find real edges; it manufactures false ones (**apophenia** — the pattern that is not there), and a mind that dreams without a check spirals into **rumination**, promoting noise to belief. So **the dream proposes; it does not dispose.** Every dreamed edge is a *hypothesis*, parked in a provisional store, and a **separate, waking check** verifies it against the lake before it is promoted to canon. The dreamer is allowed to be wrong — generative, high-recall, free; the auditor that decides what becomes real is a **different actor**, because no actor checks its own dreams. Dreaming does not escape the governance architecture — it sits *underneath* it and proves it again: generate freely while idle, verify before promotion, and **decay what never confirms** so the system does not ruminate.

Even the schedule is the human one: you dream in the **down-time, never mid-sprint.** The pass is offline and budgeted — cheap shallow sweeps often, the deep cross-category dive rarely — which is also why it must never sit on the critical path of an action.

## The agent's memory today *is* this design — frozen

Map the engine onto the memory a working agent actually runs on (file-based: a `MEMORY.md` index, topic files, and the raw session transcripts):

| Design piece | In the agent's memory today |
|---|---|
| **The lake** (raw, preserved) | The session transcripts — every word, verbatim. **Exists.** |
| **Derived fingerprints** | The distilled topic files. **Exist — but frozen** (written once, then trusted forever). |
| **Semantic edges** | The `[[wikilinks]]` between files — a hand-built graph. **Exists** (manual, not *dreamed*). |
| **Multi-resolution retrieval** | Gist = the index; moment = drill to the transcript. **Half-exists.** |
| **Statistical / segmented-norm layer** | — **Absent.** |
| **Reconsolidation (waking, on recall)** | — **Absent** (fingerprints are trusted, not re-derived). |
| **Dreaming (offline edge discovery)** | — **Absent** (edges are added by hand, never proposed by a background pass). |

So today's memory is a *frozen, partial* build of the design. It holds the lake, the fingerprints, and the edges, and it is missing exactly the two pieces the design insisted on — **the same two that were missing in the triage wall-and-flag** (the statistical anomaly half, and the honest treatment of what changes over time).

**Upgrade 1 — the statistical half (novelty on write, staleness on recall).** The segment-norm comparison does two jobs in a memory:
- On a **write**: *"is this fact far from what I already hold?"* → **novelty / salience.** Far from the norm → store it. Near an existing fingerprint → it is a duplicate, merge don't multiply. (This is the rule *"check for an existing file that already covers it"* — today done by judgment in the moment, not by a measured norm.)
- On a **recall**: *"has this fact drifted from its segment / its source?"* → **staleness.** A fact about a file or a flag that has moved is an anomaly against the present world, and should be flagged for re-verification before it steers a decision.

**Upgrade 2 — reconsolidation.** A frozen fingerprint rots: the file says a tool is uninstalled long after it was installed. The design already solved this — **do not trust the frozen file; re-derive from the lake on recall, in present terms.** Today's memory freezes the vector; the design says never freeze it.

## Short-term and long-term fall straight out

- **Short-term** = the **hot working set** — the fingerprints loaded into context for the current task, governed by recency/relevance eviction. This is the hot cache.
- **Long-term** = **lake + cold fingerprints**, governed by reconsolidation (re-derive on recall) and segment-norm salience (what earns a place at all, and what gets evicted). This is the cold store.

Memory *is* the caching problem — hit rate, eviction, coherence, *high-stakes-never-cached.* The high-stakes-never-cached rule is the governance floor wearing its memory hat: a load-bearing fact about to drive a consequential action is not served from cache; it is re-derived from the lake and, at sufficient gravity, put in front of a human.

## The journal — the whole thing in one metaphor

A person who journals is running this engine by hand. The day is lossy, so the journal is the **lake** — the long-term store working memory cannot hold. You do not journal *everything*; you journal what is **salient** — and the journal is the cleanest proof of H2a's doubt, because a person writes down the *consequential* moment, not the *statistically rare* one. You record the small decision that changed something, not the loud thing that did not matter. **Humans do not journal by anomaly score; salience is consequence, not frequency.** Re-reading an old entry and finding it means something different now is **waking reconsolidation** — the ink is fixed, the reading drifts. Finding an entry that is simply not true anymore is **staleness.** And the journal is **yours, private, on your shelf** — the local/owned instinct, not a feature bolted on. The reason people journal is not storage and not retrieval; it is **continuity of self** — to stay the same person across the gaps, to not relive the same mistake. That is also the honest answer to "would this make our interactions better?": memory is how a person stays themselves across forgetting, and how a working relationship stays continuous across every reset. Same verb.

The metaphor's value is also where it **breaks** — and the break is the payload. A journal is re-read by the **same person who wrote it**; their body still remembers, the page is only a trigger, so a wrong entry gets caught by a self that was there. An agent's memory is often read by a **fresh instance who was not there** — no lived backstop, only the page. So *distrust the recall* is optional comfort for a journaler and **non-negotiable for an agent**: the human has a self to catch a false entry; the fresh reader has only the words. This is the single strongest reason the post-audit-the-recall discipline is load-bearing here in a way it is not for a person.

## The unifying claim

Governance gates on **risk** (downside, harm); memory gates on **salience** (is it worth keeping?) and **staleness** (is it still true?). Same machine, different question put to the same scores. So the rule that completes the memory is the governance rule inverted for a store whose writes are cheap and reversible:

> **Pre-gate nothing; post-audit the recall.** Trust the store, distrust the read. A recall is a claim, and a claim is audited at gravity — trivial facts used raw, load-bearing facts re-verified against the lake before they act.

## Seams to respect before building

1. **Choosing *k* and the slices is the hard part**, and it inherits the oldest blind spot: you only segment on the features you fed it. Bad segments → bad norms → bad anomalies → bad salience.
2. **Norms drift.** A norm learned once goes stale; the live version needs online updates and an explicit decay/forgetting policy. (Forgetting is a feature, not a bug — it is eviction with a half-life.)
3. **Cohort-relative scoring is blind to a whole-cohort-gone-bad.** If an entire segment is compromised or uniformly stale, "normal for that segment" hides it. Keep a global view alongside the per-segment one.
4. **Cost.** A fingerprint at every level across many drifting dimensions explodes combinatorially. Materialize **lazily** — derive a level's fingerprint from the lake *when queried* — or use nested/matryoshka embeddings (one vector valid at multiple truncations). Do not eagerly store the cross-product.
5. **"The entire situation" is really "the entire *observed* situation."** The memory is only as complete as the dimensions you chose to observe. The blind spot is whatever you left out — and it is silent.

## The spike

It is concrete enough to be an afternoon: *a small corpus → k segments → per-slice sufficient statistics → score a new item for novelty and a recalled item for drift → re-derive one fingerprint from the trace instead of reading the frozen one.* The segmented, reconsolidating version is the one worth spiking; the global-norm, frozen-vector version would undersell it. **Dreaming is a *separate, later* spike** — an offline pass that proposes cross-category edges into a provisional store plus an independent check that verifies them against the lake before promotion (the H5 precision test). Keep it off the first spike's critical path; it earns its place only once the waking engine beats H0.

**Local, and where a model does / does not belong.** This wants to run *locally* — owned hardware, no cloud, the user keeps the lake. That is the correct home (privacy + BoP). But keep the tools straight, because the triage-LoRA analogy is seductive and breaks: the **statistical core stays model-free** (numpy — counts/means/variances; a neural net there destroys the auditability that was the point). A small **local model** earns three jobs only — embedding genuinely unstructured content, reconsolidation (summarizing the trace into a fresh fingerprint), and naming the typed edges segmentation cannot. The **one** place a LoRA is the *right* tool is H2a made buildable: stop *assuming* salience = distance and instead **fine-tune a small local model to learn the user's own salience function** from labeled history ("worth keeping vs. noise, for this user") — same move as teaching the concept of risk, new concept (salience-for-me). It is a **v2**: needs accumulated labels, risks overfitting, and H0 may beat it — so the no-training local spike (embedder + existing files + model-free novelty/staleness score) runs first and gives the null its fair fight. Do not reach for the LoRA in the core.

## Seed — the three-way convergence (2026-06-30, weekend thread, not yet pulled)

*Dropped from a conversation while explaining the work to a friend. A thread to develop, not a claim that's earned. The convergence-**feeling** is not the evidence; it still has to beat H0. Captured so it isn't lost.*

The friend-explanation stripped it to one line: **learning is anomalies and patterns, that's it — an embedding of those is the "vector sense" of a situation, and that lets you compare situations across time.** Three observations fall out, and the third is the new one.

1. **The deeper "that's it."** Pattern and anomaly aren't two things — they're one thing seen from both sides. A pattern is a *compression* (a regularity you can predict); an anomaly is a *compression failure* (the part the pattern couldn't predict). So learning = improving the compression of the situation, which *automatically* sharpens what counts as surprising. The "vector sense" is the **compressed predictive state** of a moment. (MDL / prediction-error / free-energy, arrived at from the build side.)

2. **The primitive is one; the uses are three.** This doc already unifies *memory ↔ governance* (same scores, different question — salience/staleness vs. risk). The friend-line extends it to a third: **learning** *builds* the situational vector, **memory** *stores* it, **governance** *compares it across time to decide trust.* One situational sense; three verbs on it. Drift, salience, and trust-erosion are all the same geometric question — *how far has the sense moved?* — put to different ends.

3. **Why governance is the richest of the three — the payload.** Learning and memory reduce *cleanly* to the situational vector. Governance does **not**, and that incompleteness is the whole point. Governance is the only one of the three that also contains the part that **refuses** the vector: the deterministic floor and the accountable human are precisely *the trust you will not let a vector decide.* So:

   > **Governance = the situational primitive + the honest admission that the primitive is not enough for the irreversible tail.**

   The four observable dimensions (provenance, process, outcomes, drift) *are* the situational sense, measured. The floor and the human-in-the-loop are the refusal of it. That refusal is why governance is a **castle and not just a sensor** — sensor plus the part that doesn't trust the sensor. It also maps straight back to this doc's own asymmetry: *pre-gate nothing / post-audit the recall* works for memory because writes are cheap and reversible; governance keeps a pre-gate precisely because some actions are not. The reversibility axis is what decides which machine you're running.

**Weekend question to pull on:** does the three-way convergence survive a falsifier, or is "same geometry" doing illegitimate work the way it would if you claimed every distance metric is the same problem? Specifically — find the case where learning's question and governance's question come apart *even though the vectors are identical*, and see whether the floor/refusal is the *only* thing that separates them. If it is, the convergence is real and governance's irreducibility is its signature. If something else separates them, the unification is looser than it feels. Test the seam before believing the symmetry.

### The immune-system frame (the analogy that earns its keep — and where it breaks)

The design is, structurally, an **immune system** — and not loosely. Immunology already split the architecture this engine re-derived from scratch, which is itself weak evidence the shape is forced rather than chosen:

- **Innate immunity = the deterministic floor.** Germline-encoded, hardcoded, recognizes fixed danger signatures (PAMPs via pattern-recognition receptors), does not learn, fires by definition. Bright lines.
- **Adaptive immunity = the learned per-segment norm.** Slow, builds a specific response to what it has seen, carries memory. The EWMA norm. → So the two-tier *floor + learned* architecture **is** the innate/adaptive split. Nature shipped it first.
- **Self/nonself discrimination** = normal/anomaly (Forrest's negative selection — the explicit AIS lineage).
- **Immunological memory** (memory B/T cells → faster secondary response) = *this document's* situational memory. Immune memory **is** the stored-sense-compared-across-time primitive.
- **Recognizes molecular *shape*, not pathogen *intent*** = metadata-not-data. The immune system is a metadata reader; it never "understands" the pathogen, it describes its surface.
- **Distributed, local, no central controller** = small agents defending themselves at the edge. The correct deployment shape, argued biologically.
- **Danger theory** (Matzinger: respond to *danger/damage* signals, not mere nonself) = route by **impact/reversibility**, not novelty alone. Biology also rejects "anomalous ⇒ act."
- **Autoimmunity** (attacking self) = false-positive blocks. The entire FP-tuning problem restated: *avoid autoimmunity.*

**Where it breaks — and the break is the payload (this is the seed's three-way claim made flesh).** The immune system has **no human-in-the-loop, no accountable principal, no keep.** It is pure autonomous *observation + floor* — exactly, and only, the part of governance that *reduces to the vector.* It is missing the part that **refuses** the vector. And the failure mode of an autonomous defender with no brake on irreversible action is not hypothetical: **sepsis, cytokine storm, anaphylaxis** — the defender killing the host it was protecting. That is the HITL argument written in biology: *even nature's finest defender, ungoverned on the irreversible, destroys what it defends.* So the immune system is this entire architecture **minus the one thing governance adds** — the accountable human. One line: **you built an immune system, then gave it a conscience.**

Caveat in keeping with this doc's discipline: the elegance is a lens, not a proof. An analogy that maps this cleanly is *suspicious* precisely because it's satisfying — convergence-feeling is not evidence (H0 still has to lose). The frame earns its keep by making the blind spot **precise** (metadata is blind to the semantically-valid-but-malicious; the immune system to the structurally-self-presenting pathogen — molecular mimicry) and by locating governance's irreducible part exactly where biology *lacks* one. Use it to generate falsifiers, not to feel finished.

---

*This is a structure, not a manifesto — an object (a memory) and how to build it. It is the situational-governance engine of Agent Law, read at a different altitude: the auditor that scores actions and the memory that scores facts are the same engine. The honest distance between this design and the memory an agent runs on today is itself the build list.*
