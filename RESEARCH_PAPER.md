# Enterprise Architecture in the Age of Agentic AI
### The One Engine — governing, coordinating, and remembering for agents that act

*One enterprise architect's working answer to a question the discipline is now asking out loud: what is architecture worth when the system acts on its own? The components are mostly borrowed and cited as such; the contribution is the arrangement, one synthesis, and an honesty about where it breaks. Convergence is treated throughout as a hint, never a proof.*

---

## The lens

I came to this problem with a habit of mind I've spent a career building as an enterprise architect: govern a system you can never see all of at once. Reason at the level of the whole, not the part. Decide what must *never* happen, and make that floor something that **runs** rather than something that's written down. Sort every decision by blast radius. Assume you'll be wrong, and design for where it breaks. And terminate accountability in a human — never in "the system decided."

I brought that habit to a new subject: software agents that *act* in the world, with real discretion, and still cannot answer for what they do. This is the question my own discipline is now asking out loud — what is enterprise architecture worth when the system acts on its own? Here is the answer the habit found, and it is not the defensive one: agentic AI doesn't retire enterprise architecture. It does something stranger — it forces the discipline's principles to *run*. The governance that used to live in a binder becomes executable, load-bearing, and suddenly urgent. The rest of this note walks that claim through three problems that turn out to be one.

## One engine

Three problems are usually treated as three. I think they are one.

- **Govern** a single agent: when do you trust what it produced, and when do you refuse?
- **Coordinate** a population of agents checking each other at scale, with a human only where one is unavoidable: whose verdict counts, and on what?
- **Remember**: give an agent a memory it can rely on — which means knowing when to *distrust its own recall*.

Underneath all three sits a single question — **what to trust, and when not to** — answered by a single shape. The same machinery that decides whether an action is anomalous enough to stop decides whether a fact is novel enough to keep and whether a memory is stale enough to doubt. I think risk-scoring an action and salience-scoring a memory are the same operation pointed in two directions: one engine, read three ways — two I'd defend, one I'm still testing.

That identity — the three as a single engine — is the one claim here I haven't seen stated as one elsewhere. Nearly every *mechanism* below has converged in the published work of the last year; the synthesis that they are one engine has not. I hold it as a hypothesis, and I root for the null — that they are three problems wearing one name — because the cheapest true description should win.

## Reading one — governing one agent

The hard part of an agent that acts is not the intelligence. It's knowing when *not* to trust it. The shape that answers it has three parts:

- a **deterministic floor** — a few bright lines that fire by definition, with no model in the loop;
- an **adaptive sensor** — something that learns what *normal* looks like and flags what doesn't;
- a **human at the top**, for the calls beyond the machine, who stays accountable.

The model makes the system smarter. It never makes the safety call. The reason is a distinction the field keeps relearning: **you can only govern with something you can yourself govern.** A model grading its own safety is a black box guarding a black box. A deterministic floor you can read, test, and explain is the only gate I'd actually trust — so the floor that must hold cannot be *narrated*, it has to *execute*. Eloquent rules in a governance document are straw: an actor that reinterprets language as fast as you can write it huffs once and they're gone. A single guard called "independent" because it ships from another vendor is sticks: models share blind spots, and a monitor reading the agent's own output can be talked down to zero suspicion. Independence asserted is not independence earned.

This is not a whiteboard sketch. I've put the first of these on a live bench, not just drawn it — a triage system where the shape is concrete: a deterministic floor the model cannot override, a model that proposes within it, a second screen for what the first one misses, and a human gate the system structurally cannot finalize around. Where a false negative is irreversible, the guard is not the brake. It is the only reason you can let the thing run at all. In the architect's terms, two habits made literal — *make the floor executable, not narrated*, and *terminate accountability in a human.*

## Reading two — coordinating a population

The vertical shape works but terminates in a human at every serious node. That doesn't scale to thousands of agents checking thousands of agents; a human at every gate is a bottleneck wearing governance as a costume. So the unit of analysis has to change — from the agent to the **whole population, plus the human, as one system.** That change of unit is the move; everything architectural follows from it.

The reflexive answer — let the crowd vote, weight votes by reputation — dies on contact with adversaries. Fake identities, colluding rings, herding, and the rich-get-richer trap all corrupt a vote, and a reputation gradient is a thing to climb, so it gets gamed. The architecture rests on one idea instead:

> **Never let the crowd vote on anything you can't undo.**

Sort every check by a single question — *can this be undone?* — and the system splits into two channels that obey different rules:

- **The Floor** handles the irreversible tail. No votes, no reputation. Any admitted agent can fire **stop**, and the most restrictive verdict wins with no override. The consequence is the one strong guarantee here: an adversary can manufacture *restriction* but never *permission*. Flood it with a million agents and each can only add a "no"; a forced *go* is impossible by the shape of the aggregation, not by anyone's good behavior. This is the classic safety-over-liveness choice from fault-tolerant systems (Lamport, Shostak & Pease 1982; Alpern & Schneider 1985) — restated, not discovered.

- **The Filter** handles the reversible bulk, where the eyes scale and no human sits per node. Because the Floor backstops everything irreversible, this channel is *allowed to be imperfect* — the worst a gamed filter does is wave through something that can be undone. Reputation moves only on later-resolved ground truth, never on agreement (peer agreement is worth zero); judgments are committed before they're shared, so you aggregate independent errors instead of echoes; weight is decorrelation, not popularity; and a random, unsteerable sample of the quietly-passed bulk is *forced* into resolution so a ring can't simply hide where no one checks. This is reputation-systems and mechanism-design lineage — EigenTrust (Kamvar et al. 2003), proper scoring rules (Gneiting & Raftery 2007), peer prediction (Miller et al. 2005), the Delphi method (Dalkey & Helmer 1963), a public randomness beacon (Rabin 1983) — arranged, not invented.

That refusal — to put the irreversible tail on the reputation gradient at all — is the narrow new move here. We didn't build a better vote. We declined to vote on the things that count. And here two architect's habits do the work at once — *reason at the level of the whole*, and *sort by blast radius* — turned from doctrine into running code. The unit of analysis was the organization all along.

## Reading three — remembering

Point the same engine inward and it becomes memory — by analogy at first; I'll mark where the analogy fails rather than paper over it. Deciding whether a fact is *novel enough to store* and whether a memory is *stale enough to distrust* is the anomaly sensor again, scoring facts instead of actions. The design has the same two halves as the governance engine: a **statistical** layer that learns a per-cohort norm and scores against it, model-free and auditable; and a **semantic** layer that preserves the raw record as a *lake* and treats every derived index as re-projectable rather than primary — so on drift you re-derive from the lake instead of trusting a frozen vector. This is a discipline every data architect already knows — keep the system of record separate from its derived views, and rebuild the views, never the record — pointed at an agent's memory rather than a warehouse.

The cleanest way to see it is a person who keeps a journal. You journal to stay yourself across time and not relive the same mistake — continuity, not storage. You write down what was *consequential*, which is why salience is about consequence, not frequency. And re-reading an old entry in today's light is re-derivation, not playback.

But the journal is also where the analogy *breaks*, and the break is the payload. Your journal is re-read by the same person who wrote it — a body and a continuous self stand behind a wrong entry and catch it. An agent's memory is read by a fresh instance that wasn't there. So for a person, distrusting the recall is optional; for an agent, it is **non-negotiable.** A memory system that trusts what it stored, forever, is the failure mode, not the goal. The habit underneath is the oldest one in the discipline — *never trust a single source of truth* — turned inward on the agent's own memory. (I hold this reading as the most speculative of the three and keep it framed against the null: a plain frozen store with manual re-verification may simply win.)

## The method is the artifact

Why this is a position I'll defend, not just a take, is the method — and the method is the point:

- The thesis is **falsifiable**, with named ways to kill it, and I test the null first.
- The mechanisms came from a **solution-agnostic tournament** — independently generated approaches that converged on the same shape. I treat that convergence as a hint and say so, because convergence has a way of feeling like proof when it is only a coincidence of priors.
- The doctrine then went through an **adversarial review loop** — a generate-and-attack discipline, reviewers instructed to break it rather than admire it — and every claim that couldn't survive was cut. What remains is what couldn't *yet* be refuted.
- The open problems are **ranked by dependency and published on top**, not buried — including the one I can't close.
- Every borrowed component is **cited to its primary source**, and I claim only the arrangement.

The meta-move is the real artifact: I ran my own governance pattern *on my own doctrine.* The thing that audits agents audited the claims about auditing agents — governance applied recursively, the architect's discipline turned on the architecture itself.

## Where it breaks

This section is itself an architect's habit enacted — *assume you'll be wrong, and design for where it breaks* — turned on this very doctrine. Honesty about the seams is the credibility; a doctrine with no stated failure mode is selling something.

The load-bearing one: nearly every quantitative bound in the coordination layer is the same economic move — it converts a *free* attack into a *costed* one, where the cost is minting a distinct, non-fungible identity. That is exactly the Sybil result (Douceur 2002): without a trusted authority or a real resource cost, identities are free and reputation is meaningless. I do not solve it. I name it as the slab under everything else and argue that as the price of an identity falls to zero, every bound that rests on it degrades to its free-attack baseline. **At least two properties survive a free identity:** the floor's impossibility of a forced *go* (a property of the aggregation's shape) and the detectability of a skewed audit draw (a cryptographic property). Everything else is conditional on an economic floor I've named but not built.

Downstream sit the rest: a restriction-flood is a denial-of-service primitive the floor's own asymmetry creates, and it can't be fixed *inside* the floor without re-opening the forced-*go* hole; the coverage of the forced-audit draw is finite, so an adversary can still gamble on the rarely-checked slice; and the thing that runs the scoring is itself an agent that must be split, attested, and re-scored into a human's hands rather than trusted. Each is relocated to a smaller, nameable, human-rooted authority — not dissolved. The honest claim is that the central authority shrinks to a few splittable spots, not that it disappears.

And the lane is crowded. Live work elsewhere — sandboxes that measure how well a population of agents coordinates — is complementary, not competing: measuring fitness does not, by construction, stop a well-coordinated population from shipping an irreversible harm. This is the floor such a sandbox makes necessary, not a rival to it. I'd rather state that than imply more territory than I hold.

## The transform

The discipline I'd been told was slideware — governing a system too large to hold in one head — turns out to be the exact discipline a population of acting agents now needs. Sorting by blast radius, making the floor executable, terminating accountability in a human: these stopped being a governance committee's vocabulary and became the load-bearing mechanism. AI did not make enterprise architecture obsolete. It made it executable, and urgent.

That is also the whole of how I work: I take the frontier's open problems, run them through my own adversarial process, and ship the part that survives into a live system. Reading one is the part I've put on a live bench; the rest is still on it, seams up, waiting for the next huff.

---

### References
- Douceur, J. "The Sybil Attack." *IPTPS 2002*, LNCS 2429, pp. 251–260.
- Lamport, L., Shostak, R., & Pease, M. "The Byzantine Generals Problem." *ACM TOPLAS* 4(3):382–401, 1982.
- Alpern, B., & Schneider, F. "Defining Liveness." *Information Processing Letters* 21(4):181–185, 1985.
- Kamvar, S., Schlosser, M., & Garcia-Molina, H. "The EigenTrust Algorithm for Reputation Management in P2P Networks." *WWW 2003*, pp. 640–651.
- Gneiting, T., & Raftery, A. "Strictly Proper Scoring Rules, Prediction, and Estimation." *JASA* 102(477):359–378, 2007.
- Miller, N., Resnick, P., & Zeckhauser, R. "Eliciting Informative Feedback: The Peer-Prediction Method." *Management Science* 51(9):1359–1373, 2005.
- Dalkey, N., & Helmer, O. "An Experimental Application of the Delphi Method to the Use of Experts." *Management Science* 9(3):458–467, 1963.
- Rabin, M. "Transaction Protection by Beacons." *Journal of Computer and System Sciences* 27(2):256–267, 1983.
