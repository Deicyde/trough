---
declaration: theorem
origin: cited
lean: SimpleGraph.exists_regular_equipartition_almost_refining
statement: formalized
proof: formalized
---

# Szemerédi's regularity lemma relative to a seed

Every equipartition `P₀` of a finite
graph is almost refined, up to `ε`, by an `ε`-uniform equipartition with at most
`refiningRegularityBound ε #P₀.parts` parts.

```lean
SimpleGraph.exists_regular_equipartition_almost_refining.{u_1} {α : Type u_1} [Fintype α]
  [DecidableEq α] (G : SimpleGraph α) [DecidableRel G.Adj] {ε : ℝ} (P₀ : Finpartition Finset.univ)
  (hP₀ : P₀.IsEquipartition) (hε : 0 < ε) :
  ∃ P,
    P.IsEquipartition ∧
      P.IsUniform G ε ∧
        P.AlmostRefines P₀ ε ∧ P.parts.card ≤ TauCeti.refiningRegularityBound ε P₀.parts.card
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SimpleGraph.exists_regular_equipartition_almost_refining`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.html#SimpleGraph.exists_regular_equipartition_almost_refining).

## Sources

- [Tau Ceti documentation: `SimpleGraph.exists_regular_equipartition_almost_refining`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.html#SimpleGraph.exists_regular_equipartition_almost_refining)
- [Source of `SimpleGraph.exists_regular_equipartition_almost_refining` in TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.lean#L167)
- [Tau Ceti roadmap status: Graph regularity, finite weak regularity, and arity-3 hypergraph complexes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Regularity/STATUS.md)
