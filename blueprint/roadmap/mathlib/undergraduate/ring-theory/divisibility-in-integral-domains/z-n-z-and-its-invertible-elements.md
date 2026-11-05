---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: ZMod.unitOfCoprime
mathlib_file: Mathlib/Data/ZMod/Basic.lean
---

# $\Z/n\Z$ and its invertible elements

`unitOfCoprime` makes an element of `(ZMod n)ˣ` given
a natural number `x` and a proof that `x` is coprime to `n`

```lean
ZMod.unitOfCoprime {n : ℕ} (x : ℕ) (h : x.Coprime n) : (ZMod n)ˣ
```

## Depends on

- [Integer](../../../overview/general-algebra/numbers/integer.md)
- [Ring](../../../overview/general-algebra/rings/ring.md)

## Sources

- [Mathlib documentation: `ZMod.unitOfCoprime`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/ZMod/Basic.html#ZMod.unitOfCoprime)
- [Source of `ZMod.unitOfCoprime` in Mathlib/Data/ZMod/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/ZMod/Basic.lean#L792)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L155)
