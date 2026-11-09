# Ahlswede-Zhang identity

The **Ahlswede-Zhang Identity**.

```lean
AhlswedeZhang.infSum_eq_one.{u_1} {α : Type u_1} [Fintype α] [DecidableEq α] {𝒜 : Finset (Finset α)}
  [Nonempty α] (h𝒜₁ : 𝒜.Nonempty) (h𝒜₀ : ∅ ∉ 𝒜) : AhlswedeZhang.infSum 𝒜 = 1
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Rational number](../../general-algebra/numbers/rational-number.md)

## Proof depends on

- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Field $\Q$ of rational numbers](../../../undergraduate/ring-theory/field-theory/field-q-of-rational-numbers.md)
- [Formula for the Number of Combinations](../../../hundred-theorems/part-03/formula-for-the-number-of-combinations.md)

## Sources

- [Mathlib documentation: `AhlswedeZhang.infSum_eq_one`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SetFamily/AhlswedeZhang.html#AhlswedeZhang.infSum_eq_one)
- [Source of `AhlswedeZhang.infSum_eq_one` in Mathlib/Combinatorics/SetFamily/AhlswedeZhang.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Combinatorics/SetFamily/AhlswedeZhang.lean#L429)
- [Mathlib overview: Combinatorics › Set families](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L512)
