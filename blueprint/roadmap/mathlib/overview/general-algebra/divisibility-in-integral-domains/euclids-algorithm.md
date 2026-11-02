---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Nat.xgcd
mathlib_file: Mathlib/Data/Int/GCD.lean
---

# Euclid's' algorithm

Use the extended GCD algorithm to generate the `a` and `b` values
satisfying `gcd x y = x * a + y * b`.

```lean
Nat.xgcd (x y : ℕ) : ℤ × ℤ
```

## Depends on

- [Integer](../numbers/integer.md)

## Sources

- [Mathlib documentation: `Nat.xgcd`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Nat.xgcd)
- [Source of `Nat.xgcd` in Mathlib/Data/Int/GCD.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Int/GCD.lean#L60)
- [Mathlib overview: General algebra › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L91)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L150)
