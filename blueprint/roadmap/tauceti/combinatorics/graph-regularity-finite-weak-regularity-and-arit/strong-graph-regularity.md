---
declaration: theorem
origin: cited
lean: SimpleGraph.exists_strong_regular
statement: formalized
proof: formalized
---

# Strong graph regularity

Let `ε > 0` and let `F : ℕ → ℝ` be a positive schedule. Every
equipartition `P₀` of a finite graph `G` is almost refined, up to `ε`, by the coarse partition `P`
of a strong regularity witness `(P, Q)`, where `P` has at least `l` parts for any requested
`l ≤ card α`, and `Q` has at most `strongGraphRegularityBound ε F (max l #P₀.parts)` parts.

```lean
SimpleGraph.exists_strong_regular.{u_1} {α : Type u_1} [Fintype α] [DecidableEq α]
  (G : SimpleGraph α) [DecidableRel G.Adj] (P₀ : Finpartition Finset.univ)
  (hP₀ : P₀.IsEquipartition) {l : ℕ} (hl : l ≤ Fintype.card α) {ε : ℝ} (hε : 0 < ε) {F : ℕ → ℝ}
  (hF : ∀ (n : ℕ), 0 < F n) :
  ∃ P Q, G.StrongRegular P Q ε F (max l P₀.parts.card) ∧ P.AlmostRefines P₀ ε ∧ l ≤ P.parts.card
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Szemerédi's regularity lemma relative to a seed](szemeredis-regularity-lemma-relative-to-a-seed.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.exists_strong_regular`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/StrongRegularity.html#SimpleGraph.exists_strong_regular).

## Sources

- [Tau Ceti documentation: `SimpleGraph.exists_strong_regular`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/StrongRegularity.html#SimpleGraph.exists_strong_regular)
- [Source of `SimpleGraph.exists_strong_regular` in TauCeti/Combinatorics/Regularity/Graph/StrongRegularity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Regularity/Graph/StrongRegularity.lean#L156)
- [Tau Ceti roadmap status: Graph regularity, finite weak regularity, and arity-3 hypergraph complexes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Regularity/STATUS.md)
