---
declaration: theorem
origin: cited
lean: CompactnessConjecture.quantitativeCompactnessCounterexample
statement: formalized
proof: formalized
---

# Counterexamples to graph compactness and two-degenerate extremal bounds

> Formalizes two counterexamples in extremal graph theory. The first gives a finite family of connected bipartite cyclic graphs whose family extremal number grows strictly slower than every member's extremal number, disproving the Erdős--Simonovits compactness conjecture. The second constructs a connected bipartite two-degenerate graph with extremal number at least c n^(3/2+ε), disproving the proposed universal n^(3/2) upper bound under the stated bipartition degree condition.

*Quoted from the card [LeanPool/projects/compactness-and-degeneracy.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/compactness-and-degeneracy.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`CompactnessConjecture.quantitativeCompactnessCounterexample`](https://leanpool.github.io/lean-pool/LeanPool/CompactnessAndDegeneracy/Compactness.html#CompactnessConjecture.quantitativeCompactnessCounterexample) (theorem; a main declaration), declared in [LeanPool/CompactnessAndDegeneracy/Compactness.lean, line 9547](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompactnessAndDegeneracy/Compactness.lean#L9547): “There is a nonempty finite family of connected bipartite cyclic graphs such that every member has a uniform positive n^(4/3)-scale extremal lower bound, while every family-free host on n vertices has its sixteenth power of the edge count bounded by a constant times n^21. Consequently the family is not compact and the Erdős--Simonovits compactness conjecture is false.”
- [`TwoDegenerateGraphs.twoDegenerateExtremalCounterexample`](https://leanpool.github.io/lean-pool/LeanPool/CompactnessAndDegeneracy/Degeneracy.html#TwoDegenerateGraphs.twoDegenerateExtremalCounterexample) (theorem), declared in [LeanPool/CompactnessAndDegeneracy/Degeneracy.lean, line 9185](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompactnessAndDegeneracy/Degeneracy.lean#L9185): “There is a connected bipartite two-degenerate finite graph H such that each side of every two-coloring has a vertex of degree greater than two, yet ex(n,H) is eventually at least c n^(3/2+ε) for some positive constants c and ε.”

## Project

- Authors: OpenAI, Dean Cureton.
- Source: *Ten Advances in Mathematics and Theoretical Computer Science* by OpenAI.
- Project repository: [openai/ten-proofs](https://github.com/openai/ten-proofs), at commit [94bc0feb](https://github.com/openai/ten-proofs/tree/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 05C35, 05C75.
- In Lean Pool: [LeanPool/CompactnessAndDegeneracy](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompactnessAndDegeneracy), from the card [LeanPool/projects/compactness-and-degeneracy.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/compactness-and-degeneracy.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/compactness-and-degeneracy.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/compactness-and-degeneracy.yaml)
- [Lean Pool at 2b205bf9: LeanPool/CompactnessAndDegeneracy](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompactnessAndDegeneracy)
