---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: AhlswedeZhang.infSum_eq_one
mathlib_file: Mathlib/Combinatorics/SetFamily/AhlswedeZhang.lean
---

# Ahlswede-Zhang identity

The **Ahlswede-Zhang Identity**.

```lean
AhlswedeZhang.infSum_eq_one.{u_1} {α : Type u_1} [Fintype α] [DecidableEq α] {𝒜 : Finset (Finset α)}
  [Nonempty α] (h𝒜₁ : 𝒜.Nonempty) (h𝒜₀ : ∅ ∉ 𝒜) : AhlswedeZhang.infSum 𝒜 = 1
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Rational number](../../general-algebra/numbers/rational-number.md)
- [Set](../../data-structures/sets/set.md)

## Proof depends on

- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Field $\Q$ of rational numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-of-rational-numbers.md)
- [Formula for the Number of Combinations](../../../hundred-theorems/part-03/formula-for-the-number-of-combinations.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure.md)

## Sources

- [Mathlib documentation: `AhlswedeZhang.infSum_eq_one`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SetFamily/AhlswedeZhang.html#AhlswedeZhang.infSum_eq_one)
- [Source of `AhlswedeZhang.infSum_eq_one` in Mathlib/Combinatorics/SetFamily/AhlswedeZhang.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SetFamily/AhlswedeZhang.lean#L429)
- [Mathlib overview: Combinatorics › Set families](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L512)
