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
- [Source of `TauCeti.star_mul_mul_eq_zero_iff_of_nonneg` in TauCeti/Analysis/CStarAlgebra/Compression.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/Compression.lean#L28)
- [Tau Ceti roadmap status: C*-algebras, operator spaces and approximation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CStarAlgebras/STATUS.md)
