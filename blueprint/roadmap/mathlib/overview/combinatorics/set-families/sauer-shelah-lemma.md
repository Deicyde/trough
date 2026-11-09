# Sauer-Shelah lemma

The **Sauer-Shelah lemma**.

```lean
Finset.card_shatterer_le_sum_vcDim.{u_1} {α : Type u_1} [DecidableEq α] {𝒜 : Finset (Finset α)}
  [Fintype α] : 𝒜.shatterer.card ≤ ∑ k ≤ 𝒜.vcDim, (Fintype.card α).choose k
```

## Depends on

- [VC dimension](vc-dimension.md)

## Proof depends on

- [Formula for the Number of Combinations](../../../hundred-theorems/part-03/formula-for-the-number-of-combinations.md)

## Sources

- [Mathlib documentation: `Finset.card_shatterer_le_sum_vcDim`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SetFamily/Shatter.html#Finset.card_shatterer_le_sum_vcDim)
- [Source of `Finset.card_shatterer_le_sum_vcDim` in Mathlib/Combinatorics/SetFamily/Shatter.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Combinatorics/SetFamily/Shatter.lean#L196)
- [Mathlib overview: Combinatorics › Set families](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L520)
