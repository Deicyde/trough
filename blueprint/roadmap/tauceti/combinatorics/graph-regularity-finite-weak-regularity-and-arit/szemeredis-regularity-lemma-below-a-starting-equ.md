---
declaration: theorem
origin: cited
lean: SimpleGraph.szemeredi_regularity_le
statement: formalized
proof: formalized
---

# Szemerédi's regularity lemma below a starting equipartition

If `P₁` is an equipartition
with at least `7` parts and `100 ≤ 4 ^ #P₁.parts * ε ^ 5`, and the graph is large enough, then
some `ε`-uniform equipartition refines `P₁` and has at most
`stepBound^[⌊4 / ε ^ 5⌋₊ + 1] #P₁.parts` parts.

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

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SimpleGraph.szemeredi_regularity_le`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.html#SimpleGraph.szemeredi_regularity_le).

## Sources

- [Tau Ceti documentation: `SimpleGraph.szemeredi_regularity_le`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.html#SimpleGraph.szemeredi_regularity_le)
- [Source of `SimpleGraph.szemeredi_regularity_le` in TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Regularity/Graph/SeededRegularity.lean#L62)
