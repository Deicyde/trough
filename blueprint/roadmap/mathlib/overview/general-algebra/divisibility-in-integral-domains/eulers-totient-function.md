---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Nat.totient
mathlib_file: Mathlib/Data/Nat/Totient.lean
---

# Euler's totient function ($\varphi$)

Euler's totient function. This counts the number of naturals strictly less than `n` which are
coprime with `n`.

```lean
Nat.totient (n : ℕ) : ℕ
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Nat.totient`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient)
- [Source of `Nat.totient` in Mathlib/Data/Nat/Totient.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Nat/Totient.lean#L35)
- [Mathlib overview: General algebra › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L92)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L156)
