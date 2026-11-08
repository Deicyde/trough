---
declaration: theorem
origin: cited
lean: GoemansFlow.goemans_cost_conjecture_false
statement: formalized
proof: formalized
---

# Counterexample to Goemans' unsplittable-flow cost conjecture

> Refutes Goemans' cost conjecture for single-source unsplittable flow, Conjecture 1.3 of Traub, Vargas Koch, and Zenklusen's paper. A simple, loopless, acyclic graph with seven vertices and nine arcs admits a splittable flow of cost 58, but every unsplittable routing within the additive maximum-demand capacity bound costs at least 60, attained by an explicit routing. The development proves completeness of the walk enumeration and transfers the refutation from integers to any linearly ordered commutative ring, including the rationals and reals. Jason Hickey directed Claude's formal verification of the counterexample discovered by Dmitry Rybin with GPT-5.6 Pro; upstream also acknowledges Katherine Schlitz. Planarity is not part of the formalized claim.

*Quoted from the card [LeanPool/projects/goemans-cost-counterexample.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/goemans-cost-counterexample.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`GoemansFlow.goemans_cost_conjecture_false`](https://leanpool.github.io/lean-pool/LeanPool/GoemansFlow/Counterexample.html#GoemansFlow.goemans_cost_conjecture_false) (theorem; a main declaration), declared in [LeanPool/GoemansFlow/Counterexample.lean, line 577](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GoemansFlow/Counterexample.lean#L577): “The rational form of Goemans' cost conjecture is false, even for simple, loopless, acyclic finite digraphs with explicit capacities, positive demands, and distinct terminals different from the source.” Its source, as the card gives it: “Conjecture 1.3 of arXiv:2308.02651v1”
- [`GoemansFlow.not_GoemansCostConjectureFull`](https://leanpool.github.io/lean-pool/LeanPool/GoemansFlow/Counterexample.html#GoemansFlow.not_GoemansCostConjectureFull) (theorem), declared in [LeanPool/GoemansFlow/Counterexample.lean, line 562](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GoemansFlow/Counterexample.lean#L562): “The same cost conjecture is false over every linearly ordered commutative ring, by transfer of the integer counterexample.”
- [`GoemansFlow.optimum_is_sixty`](https://leanpool.github.io/lean-pool/LeanPool/GoemansFlow/Counterexample.html#GoemansFlow.optimum_is_sixty) (theorem), declared in [LeanPool/GoemansFlow/Counterexample.lean, line 405](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GoemansFlow/Counterexample.lean#L405): “On the explicit seven-vertex, nine-arc instance, the minimum cost among unsplittable routings satisfying the additive maximum-demand capacity bound is exactly 60.”
- [`GoemansFlow.fractional_cost`](https://leanpool.github.io/lean-pool/LeanPool/GoemansFlow/Counterexample.html#GoemansFlow.fractional_cost) (theorem), declared in [LeanPool/GoemansFlow/Counterexample.lean, line 129](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GoemansFlow/Counterexample.lean#L129): “The given splittable flow on the counterexample instance costs exactly 58.”
- [`GoemansFlow.path_complete`](https://leanpool.github.io/lean-pool/LeanPool/GoemansFlow/Counterexample.html#GoemansFlow.path_complete) (theorem), declared in [LeanPool/GoemansFlow/Counterexample.lean, line 255](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GoemansFlow/Counterexample.lean#L255): “For each of the three terminals, the lists of arcs giving a walk from the source are exactly the two explicitly exhibited paths.”

## Project

- Authors: Jason Hickey.
- Source: *A verified counterexample to Goemans' cost conjecture* by Jason Hickey, [arXiv:2308.02651](https://arxiv.org/abs/2308.02651), [https://github.com/jyh/dinitz-verify/tree/ffba3523f0edd14be3460d039f22a6b98c02fd9e](https://github.com/jyh/dinitz-verify/tree/ffba3523f0edd14be3460d039f22a6b98c02fd9e).
- Project repository: [jyh/dinitz-verify](https://github.com/jyh/dinitz-verify), at commit [ffba3523](https://github.com/jyh/dinitz-verify/tree/ffba3523f0edd14be3460d039f22a6b98c02fd9e).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 90C35, 05C21.
- In Lean Pool: [LeanPool/GoemansFlow](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GoemansFlow), from the card [LeanPool/projects/goemans-cost-counterexample.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/goemans-cost-counterexample.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/goemans-cost-counterexample.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/goemans-cost-counterexample.yaml)
- [Lean Pool at 2b205bf9: LeanPool/GoemansFlow](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GoemansFlow)
