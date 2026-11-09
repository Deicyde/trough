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
- [Source of `ZMod.unitOfCoprime` in Mathlib/Data/ZMod/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Data/ZMod/Basic.lean#L792)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L155)
