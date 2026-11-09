# Regularity lemma

Effective **Szemerédi Regularity Lemma**: For any sufficiently large graph, there is an
`ε`-uniform equipartition of bounded size (where the bound does not depend on the graph).

```lean
szemeredi_regularity.{u_1} {α : Type u_1} [DecidableEq α] [Fintype α] (G : SimpleGraph α)
  [DecidableRel G.Adj] {ε : ℝ} {l : ℕ} (hε : 0 < ε) (hl : l ≤ Fintype.card α) :
  ∃ P,
    P.IsEquipartition ∧
      l ≤ P.parts.card ∧ P.parts.card ≤ SzemerediRegularity.bound ε l ∧ P.IsUniform G ε
```

## Depends on

- [Logarithm](../../analysis/special-functions/logarithm.md)
- [Simple graph](simple-graph.md)

## Proof depends on

- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `szemeredi_regularity`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/Regularity/Lemma.html#szemeredi_regularity)
- [Source of `szemeredi_regularity` in Mathlib/Combinatorics/SimpleGraph/Regularity/Lemma.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Combinatorics/SimpleGraph/Regularity/Lemma.lean#L74)
- [Mathlib overview: Combinatorics › Graph theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L530)
