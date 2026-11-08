---
declaration: theorem
origin: cited
lean: SimpleGraph.exists_regular_equipartition_almost_refining, SimpleGraph.szemeredi_regularity_le, SimpleGraph.exists_regular_exact_refining_equipartition, SimpleGraph.exists_regular_almostRefines_le_card
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

## Other forms

**Szemerédi's regularity lemma below a starting equipartition.** Formalized in Tau Ceti as [`SimpleGraph.szemeredi_regularity_le`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.html#SimpleGraph.szemeredi_regularity_le).

```lean
SimpleGraph.szemeredi_regularity_le.{u_1} {α : Type u_1} [Fintype α] [DecidableEq α]
  (G : SimpleGraph α) [DecidableRel G.Adj] {ε : ℝ} {P₁ : Finpartition Finset.univ}
  (hP₁ : P₁.IsEquipartition) (hP₇ : 7 ≤ P₁.parts.card) (hPε : 100 ≤ 4 ^ P₁.parts.card * ε ^ 5)
  (hα :
    SzemerediRegularity.stepBound^[⌊4 / ε ^ 5⌋₊] P₁.parts.card *
        16 ^ SzemerediRegularity.stepBound^[⌊4 / ε ^ 5⌋₊] P₁.parts.card ≤
      Fintype.card α) :
  ∃ P ≤ P₁,
    P.IsEquipartition ∧
      P.IsUniform G ε ∧
        P.parts.card ≤ SzemerediRegularity.stepBound^[⌊4 / ε ^ 5⌋₊ + 1] P₁.parts.card
```

**Szemerédi's regularity lemma refining an equipartition exactly.** Formalized in Tau Ceti as [`SimpleGraph.exists_regular_exact_refining_equipartition`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.html#SimpleGraph.exists_regular_exact_refining_equipartition).

```lean
SimpleGraph.exists_regular_exact_refining_equipartition.{u_1} {α : Type u_1} [Fintype α]
  [DecidableEq α] (G : SimpleGraph α) [DecidableRel G.Adj] (P : Finpartition Finset.univ)
  (hP : P.IsEquipartition) {δ : ℝ} (hδ : 0 < δ) :
  ∃ Q ≤ P,
    Q.IsEquipartition ∧
      Q.IsUniform G δ ∧ Q.parts.card ≤ TauCeti.nestedRefinementBound δ P.parts.card
```

**Szemerédi's regularity lemma relative to a seed, with a minimum number of parts.** Formalized in Tau Ceti as [`SimpleGraph.exists_regular_almostRefines_le_card`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.html#SimpleGraph.exists_regular_almostRefines_le_card).

```lean
SimpleGraph.exists_regular_almostRefines_le_card.{u_1} {α : Type u_1} [Fintype α] [DecidableEq α]
  (G : SimpleGraph α) [DecidableRel G.Adj] {ε : ℝ} (P₀ : Finpartition Finset.univ)
  (hP₀ : P₀.IsEquipartition) {l : ℕ} (hl : l ≤ Fintype.card α) (hε : 0 < ε) :
  ∃ P,
    P.IsEquipartition ∧
      P.IsUniform G ε ∧
        P.AlmostRefines P₀ ε ∧
          l ≤ P.parts.card ∧
            P.parts.card ≤
              TauCeti.nestedRefinementBound ε
                (max (max l P₀.parts.card) ⌈2 * ↑(max l P₀.parts.card) / ε⌉₊)
```

## Sources

- [Tau Ceti documentation: `SimpleGraph.exists_regular_equipartition_almost_refining`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.html#SimpleGraph.exists_regular_equipartition_almost_refining)
- [Source of `SimpleGraph.exists_regular_equipartition_almost_refining` in TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.lean#L167)
- [Tau Ceti roadmap status: Graph regularity, finite weak regularity, and arity-3 hypergraph complexes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Regularity/STATUS.md)
