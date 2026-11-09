# Congruence in $\Z$

`a ≡ b [ZMOD n]` when `a % n = b % n`.

```lean
Int.ModEq (n a b : ℤ) : Prop
```

## Depends on

- [Integer](../../../overview/general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `Int.ModEq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/ModEq.html#Int.ModEq)
- [Source of `Int.ModEq` in Mathlib/Data/Int/ModEq.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Data/Int/ModEq.lean#L28)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L152)
