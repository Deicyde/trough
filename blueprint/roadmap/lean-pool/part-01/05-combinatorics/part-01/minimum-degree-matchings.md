---
declaration: theorem
origin: cited
lean: BKLOK2.lemma107K2_holds
statement: formalized
proof: formalized
---

# BKLO simultaneous perfect matchings and spread matchings

> Formalizes the r = 2 specialization of the simultaneous factor-selection step in BKLO Lemma 10.7: under quantitative parity, minimum-degree, codegree, and incidence hypotheses, a linearly sized, overlapping family of neighbourhood graphs admits perfect matchings whose edge sets are pairwise disjoint. The proof replaces the published randomized greedy process by a deterministic pessimistic-estimator sweep. Supporting results develop perfect, near-perfect, edge-disjoint, and quantitatively weighted spread matchings from sharp minimum-degree hypotheses.

*Quoted from the card [LeanPool/projects/minimum-degree-matchings.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/minimum-degree-matchings.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`BKLOK2.lemma107K2_holds`](https://leanpool.github.io/lean-pool/LeanPool/MinimumDegreeMatching/BKLO.html#BKLOK2.lemma107K2_holds) (theorem; a main declaration), declared in [LeanPool/MinimumDegreeMatching/BKLO.lean, line 190](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MinimumDegreeMatching/BKLO.lean#L190): “Specializes BKLO Lemma 10.7 to r = 2 in its apex-neighbourhood configuration: for every sufficiently large admissible configuration, all indexed neighbourhood graphs admit perfect matchings whose edge sets are pairwise disjoint. The proof is deterministic.”
- [`SimpleGraph.exists_isPerfectMatching_of_minDegree`](https://leanpool.github.io/lean-pool/LeanPool/MinimumDegreeMatching/Basic.html#SimpleGraph.exists_isPerfectMatching_of_minDegree) (theorem), declared in [LeanPool/MinimumDegreeMatching/Basic.lean, line 44](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MinimumDegreeMatching/Basic.lean#L44): “Every finite simple graph of even order whose minimum degree is at least half its order has a perfect matching.”
- [`SimpleGraph.exists_isMatching_compl_singleton_of_minDegree`](https://leanpool.github.io/lean-pool/LeanPool/MinimumDegreeMatching/Basic.html#SimpleGraph.exists_isMatching_compl_singleton_of_minDegree) (theorem), declared in [LeanPool/MinimumDegreeMatching/Basic.lean, line 168](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MinimumDegreeMatching/Basic.lean#L168): “Every finite simple graph of odd order n and minimum degree at least (n - 1) / 2 has a matching whose vertex set is the complement of a singleton.”
- [`SimpleGraph.exists_involutions_pairwise_ne`](https://leanpool.github.io/lean-pool/LeanPool/MinimumDegreeMatching/Spread.html#SimpleGraph.exists_involutions_pairwise_ne) (theorem), declared in [LeanPool/MinimumDegreeMatching/Spread.lean, line 490](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MinimumDegreeMatching/Spread.lean#L490): “If every vertex of a finite even vertex set has at least half the set size plus t neighbors inside the set, then the graph contains t + 1 pairwise edge-disjoint perfect matchings of that set, represented by an indexed family of partner involutions. These involutions are pairwise distinct when the vertex set is nonempty.”
- [`SimpleGraph.exists_spread_involution`](https://leanpool.github.io/lean-pool/LeanPool/MinimumDegreeMatching/Spread.html#SimpleGraph.exists_spread_involution) (theorem), declared in [LeanPool/MinimumDegreeMatching/Spread.lean, line 511](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MinimumDegreeMatching/Spread.lean#L511): “Under the same minimum-degree condition with slack t, every nonnegative edge-weight function admits a perfect matching whose weight is at most 1 / (t + 1) times the total weight over ordered pairs in the vertex set.”

## Project

- Authors: Juan Pablo Traverso Gianini, Aristotle.
- Source: *Edge-decompositions of graphs with high minimum degree* by Ben Barber, Daniela Kühn, Allan Lo, Deryk Osthus, [doi:10.1016/j.aim.2015.09.032](https://doi.org/10.1016/j.aim.2015.09.032), [arXiv:1410.5750](https://arxiv.org/abs/1410.5750), [https://github.com/jtraverso/erdos-81-chordal-clique-partitions/tree/6736c816e1f9cd105c2295a8e4716ad55609ccb0/preprints/PAPER_III/05_formalization/lean_v1.4_freeze](https://github.com/jtraverso/erdos-81-chordal-clique-partitions/tree/6736c816e1f9cd105c2295a8e4716ad55609ccb0/preprints/PAPER_III/05_formalization/lean_v1.4_freeze).
- Project repository: [jtraverso/erdos-81-chordal-clique-partitions](https://github.com/jtraverso/erdos-81-chordal-clique-partitions).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C70.
- In Lean Pool: [LeanPool/MinimumDegreeMatching](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MinimumDegreeMatching), from the card [LeanPool/projects/minimum-degree-matchings.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/minimum-degree-matchings.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/minimum-degree-matchings.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/minimum-degree-matchings.yaml)
- [Lean Pool at 2b205bf9: LeanPool/MinimumDegreeMatching](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MinimumDegreeMatching)
