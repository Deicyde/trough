---
declaration: theorem
origin: cited
lean: GraphCoveringTheory.KuroshStatement.kurosh_decomposition_with_inclusions
statement: formalized
proof: formalized
---

# Kurosh and Schreier subgroup theorems via covering graphs

> Proves the Kurosh subgroup theorem for arbitrary subgroups of indexed free products, with factors given by actual intersections with conjugates of the original factors and with the decomposition maps induced by their inclusions. The development constructs Bass–Serre trees, quotient graphs, graph-of-groups covers, path lifting, and normal forms. It also gives an explicit finite Schreier basis and classifies automorphisms of a finite regular Schreier action by its quotient group. The finite-graph basis infrastructure is reused from LeanPool.FiniteGraphFundamentalGroup.

*Quoted from the card [LeanPool/projects/kurosh.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/kurosh.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`GraphCoveringTheory.KuroshStatement.kurosh_decomposition_with_inclusions`](https://leanpool.github.io/lean-pool/LeanPool/Kurosh/KuroshSolution.html#GraphCoveringTheory.KuroshStatement.kurosh_decomposition_with_inclusions) (theorem; a main declaration), declared in [LeanPool/Kurosh/KuroshSolution.lean, line 134](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Kurosh/KuroshSolution.lean#L134): “Every subgroup H of an arbitrary indexed free product admits a free product decomposition into a free group and subgroups of H that are intersections with conjugates of the original factors. The isomorphism to H is induced by the actual subgroup inclusions and a homomorphism from the free factor.” Its source, as the card gives it: “Kurosh subgroup theorem; upstream inclusion-preserving statement.”
- [`GraphCoveringTheory.Kurosh.kurosh_decomposition`](https://leanpool.github.io/lean-pool/LeanPool/Kurosh/KuroshTheorem.html#GraphCoveringTheory.Kurosh.kurosh_decomposition) (theorem), declared in [LeanPool/Kurosh/KuroshTheorem.lean, line 51](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Kurosh/KuroshTheorem.lean#L51): “H is isomorphic to the free product of its nontrivial vertex stabilizers in the quotient Bass–Serre graph and the free group of that graph.”
- [`GraphCoveringTheory.schreier_basis_fintype`](https://leanpool.github.io/lean-pool/LeanPool/Kurosh/IndexFormula.html#GraphCoveringTheory.schreier_basis_fintype) (theorem), declared in [LeanPool/Kurosh/IndexFormula.lean, line 201](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Kurosh/IndexFormula.lean#L201): “A finite-index subgroup H of a free group on any finite generator type of cardinality r has an explicit free basis of size d\*r + 1 - d, where d is its index and subtraction is natural-number subtraction. This formulation also covers the empty generator type.”
- [`GraphCoveringTheory.schreier_basis_fintype_proved`](https://leanpool.github.io/lean-pool/LeanPool/Kurosh/IndexFormula.html#GraphCoveringTheory.schreier_basis_fintype_proved) (theorem), declared in [LeanPool/Kurosh/IndexFormula.lean, line 309](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Kurosh/IndexFormula.lean#L309): “If the finite generator type is nonempty, the basis has the classical Schreier size 1 + d\*(r - 1).” Its source, as the card gives it: “Schreier index formula; DOI 10.1007/BF02952517.”
- [`GraphCoveringTheory.finiteIndexQuotientDeckGroupEquiv`](https://leanpool.github.io/lean-pool/LeanPool/Kurosh/Deck.html#GraphCoveringTheory.finiteIndexQuotientDeckGroupEquiv) (def), declared in [LeanPool/Kurosh/Deck.lean, line 171](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Kurosh/Deck.lean#L171): “For a finite-index normal subgroup H of a group G, the automorphism group of the finite regular Schreier G-action is isomorphic to G/H by right translations. This is a theorem about the action, not a classification of general topological covers.”
- [`GraphCoveringTheory.Kurosh.kurosh_subgroup_is_free_of_trivial_stabilizers`](https://leanpool.github.io/lean-pool/LeanPool/Kurosh/KuroshFreeCorollary.html#GraphCoveringTheory.Kurosh.kurosh_subgroup_is_free_of_trivial_stabilizers) (theorem), declared in [LeanPool/Kurosh/KuroshFreeCorollary.lean, line 161](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Kurosh/KuroshFreeCorollary.lean#L161): “A subgroup with trivial stabilizers at every vertex of its quotient Bass–Serre graph is a free group.”

## Project

- Authors: Arthur Freitas Ramos, David Barros Hulak, Ruy J. G. B. de Queiroz.
- Source: *Schreier and Kurosh subgroup theorems via covering graphs*, [doi:10.1007/BF01449159](https://doi.org/10.1007/BF01449159).
- Project repository: [Arthur742Ramos/KuroshSubgroupTheorem](https://github.com/Arthur742Ramos/KuroshSubgroupTheorem), at commit [91170712](https://github.com/Arthur742Ramos/KuroshSubgroupTheorem/tree/911707126c8b9bb0c764bf853008fe1053c0aad9).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 20E07, 05C25, 18B40.
- In Lean Pool: [LeanPool/Kurosh](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Kurosh), from the card [LeanPool/projects/kurosh.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/kurosh.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/kurosh.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/kurosh.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Kurosh](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Kurosh)
