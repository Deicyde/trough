---
declaration: theorem
origin: cited
lean: IsStarProjection.conjugate_le_iff_commute
statement: formalized
proof: formalized
---

# IsStarProjection.conjugate_le_iff_commute

Compression of a positive element by a projection lies below that element exactly when
the projection commutes with it. Positivity is needed only for the reverse implication.

```lean
IsStarProjection.conjugate_le_iff_commute.{u_1} {A : Type u_1} [NonUnitalCStarAlgebra A]
  [PartialOrder A] [StarOrderedRing A] {p a : A} (hp : IsStarProjection p) (ha : 0 ≤ a) :
  p * a * p ≤ a ↔ Commute p a
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.star_mul_mul_eq_zero_iff_of_nonneg](tauceti-star-mul-mul-eq-zero-iff-of-nonneg.md)

## Lean

Formalized in Tau Ceti as [`IsStarProjection.conjugate_le_iff_commute`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Compression.html#IsStarProjection.conjugate_le_iff_commute).

## Sources

- [Tau Ceti documentation: `IsStarProjection.conjugate_le_iff_commute`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Compression.html#IsStarProjection.conjugate_le_iff_commute)
- [Source of `IsStarProjection.conjugate_le_iff_commute` in TauCeti/Analysis/CStarAlgebra/Compression.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/Compression.lean#L72)
- [Tau Ceti roadmap status: C*-algebras, operator spaces and approximation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CStarAlgebras/STATUS.md)
