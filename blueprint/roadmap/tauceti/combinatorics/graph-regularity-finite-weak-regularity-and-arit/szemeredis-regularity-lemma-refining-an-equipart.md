---
declaration: theorem
origin: cited
lean: SimpleGraph.exists_regular_exact_refining_equipartition
statement: formalized
proof: formalized
---

# Szemerédi's regularity lemma refining an equipartition exactly

Every equipartition `P` of a
finite graph is refined exactly by a `δ`-uniform equipartition with at most
`nestedRefinementBound δ #P.parts` parts.

```lean
SimpleGraph.exists_regular_exact_refining_equipartition.{u_1} {α : Type u_1} [Fintype α]
  [DecidableEq α] (G : SimpleGraph α) [DecidableRel G.Adj] (P : Finpartition Finset.univ)
  (hP : P.IsEquipartition) {δ : ℝ} (hδ : 0 < δ) :
  ∃ Q ≤ P,
    Q.IsEquipartition ∧
      Q.IsUniform G δ ∧ Q.parts.card ≤ TauCeti.nestedRefinementBound δ P.parts.card
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Szemerédi's regularity lemma below a starting equipartition](szemeredis-regularity-lemma-below-a-starting-equ.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.exists_regular_exact_refining_equipartition`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.html#SimpleGraph.exists_regular_exact_refining_equipartition).

## Sources

- [Tau Ceti documentation: `SimpleGraph.exists_regular_exact_refining_equipartition`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.html#SimpleGraph.exists_regular_exact_refining_equipartition)
- [Source of `SimpleGraph.exists_regular_exact_refining_equipartition` in TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.lean#L199)
