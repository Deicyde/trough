# Congruence in $\Z$

`a ≡ b [ZMOD n]` when `a % n = b % n`.

```lean
Int.ModEq (n a b : ℤ) : Prop
```

## Depends on

- [Integer](../../../overview/general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `Int.ModEq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/ModEq.html#Int.ModEq)
- [Source of `Int.ModEq` in Mathlib/Data/Int/ModEq.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Data/Int/ModEq.lean#L27)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L152)
