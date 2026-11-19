---
declaration: theorem
origin: cited
lean: TauCeti.star_mul_mul_eq_zero_iff_of_nonneg
statement: formalized
proof: formalized
---

# TauCeti.star_mul_mul_eq_zero_iff_of_nonneg

A corner of a positive element vanishes exactly when the element annihilates the
compressing factor on the right.

```lean
TauCeti.star_mul_mul_eq_zero_iff_of_nonneg.{u_1} {A : Type u_1} [NonUnitalCStarAlgebra A]
  [PartialOrder A] [StarOrderedRing A] {a : A} (ha : 0 ≤ a) (b : A) : star b * a * b = 0 ↔ a * b = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.star_mul_mul_eq_zero_iff_of_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Compression.html#TauCeti.star_mul_mul_eq_zero_iff_of_nonneg).

## Sources

- [Tau Ceti documentation: `TauCeti.star_mul_mul_eq_zero_iff_of_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Compression.html#TauCeti.star_mul_mul_eq_zero_iff_of_nonneg)
- [Source of `TauCeti.star_mul_mul_eq_zero_iff_of_nonneg` in TauCeti/Analysis/CStarAlgebra/Compression.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/CStarAlgebra/Compression.lean#L28)
- [Tau Ceti roadmap status: C*-algebras, operator spaces and approximation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CStarAlgebras/STATUS.md)
