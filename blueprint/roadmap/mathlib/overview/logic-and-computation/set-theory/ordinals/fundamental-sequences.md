# Fundamental sequences

A fundamental sequence for `o` is a strictly monotonic function `Iio o.cof.ord → Iio o` with
cofinal range. We provide `a = o.cof.ord` explicitly to avoid type rewrites.

```lean
Ordinal.IsFundamentalSeq.{u_1} {a o : Ordinal.{u_1}} (f : ↑(Set.Iio a) → ↑(Set.Iio o)) : Prop
```

## Depends on

- [Cofinality](../cardinals/cofinality.md)
- [Ordinal](ordinal.md)

## Sources

- [Mathlib documentation: `Ordinal.IsFundamentalSeq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/SetTheory/Ordinal/FundamentalSequence.html#Ordinal.IsFundamentalSeq)
- [Source of `Ordinal.IsFundamentalSeq` in Mathlib/SetTheory/Ordinal/FundamentalSequence.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/SetTheory/Ordinal/FundamentalSequence.lean#L32)
- [Mathlib overview: Logic and computation › Set theory › Ordinals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L626)
