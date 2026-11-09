# LYM inequality

The **Lubell-Yamamoto-Meshalkin inequality**, also known as the **LYM inequality**.

If `𝒜` is an antichain, then the sum of the proportion of elements it takes from each layer is less
than `1`.

```lean
Finset.lubell_yamamoto_meshalkin_inequality_sum_card_div_choose.{u_1, u_2} {𝕜 : Type u_1}
  {α : Type u_2} [Semifield 𝕜] [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] [Fintype α]
  {𝒜 : Finset (Finset α)} (h𝒜 : IsAntichain (fun x1 x2 => x1 ⊆ x2) ↑𝒜) :
  ∑ r ∈ Finset.range (Fintype.card α + 1), ↑(𝒜.slice r).card / ↑((Fintype.card α).choose r) ≤ 1
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Rational number](../../general-algebra/numbers/rational-number.md)

## Proof depends on

- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Formula for the Number of Combinations](../../../hundred-theorems/part-03/formula-for-the-number-of-combinations.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `Finset.lubell_yamamoto_meshalkin_inequality_sum_card_div_choose`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SetFamily/LYM.html#Finset.lubell_yamamoto_meshalkin_inequality_sum_card_div_choose)
- [Source of `Finset.lubell_yamamoto_meshalkin_inequality_sum_card_div_choose` in Mathlib/Combinatorics/SetFamily/LYM.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Combinatorics/SetFamily/LYM.lean#L198)
- [Mathlib overview: Combinatorics › Set families](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L513)
