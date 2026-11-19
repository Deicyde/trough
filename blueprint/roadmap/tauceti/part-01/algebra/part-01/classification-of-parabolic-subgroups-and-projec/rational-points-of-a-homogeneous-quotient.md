---
declaration: def
origin: cited
lean: CommHopfAlgCat.fppfHomogeneousQuotientRationalPointsEquiv
statement: formalized
---

# Rational points of a homogeneous quotient

Over an algebraically closed field `k`, the
`k`-points of the fppf homogeneous quotient `G/N` are the left cosets `G(k)/N(k)`.

```lean
CommHopfAlgCat.fppfHomogeneousQuotientRationalPointsEquiv.{u} {k : Type u} [Field k] [IsAlgClosed k]
  (H : CommHopfAlgCat k) (I : TauCeti.HopfIdeal k ↑H) :
  ↑(TauCeti.HopfAlgebra.points ↧k) ⧸ TauCeti.CommHopfAlgCat.quotientPointsSubgroup H I ↧k ≃
    (H.fppfHomogeneousQuotient I).obj.obj (Opposite.op (Opposite.op ↧k))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Fppf covers of an algebraically closed field split](fppf-covers-of-an-algebraically-closed-field-spl.md)

## Lean

Formalized in Tau Ceti as [`CommHopfAlgCat.fppfHomogeneousQuotientRationalPointsEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/RationalPoints.html#CommHopfAlgCat.fppfHomogeneousQuotientRationalPointsEquiv).

## Sources

- [Tau Ceti documentation: `CommHopfAlgCat.fppfHomogeneousQuotientRationalPointsEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/RationalPoints.html#CommHopfAlgCat.fppfHomogeneousQuotientRationalPointsEquiv)
- [Source of `CommHopfAlgCat.fppfHomogeneousQuotientRationalPointsEquiv` in TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/RationalPoints.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/RationalPoints.lean#L74)
- [Tau Ceti roadmap status: Classification of parabolic subgroups and projective homogeneous spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FlagVarieties/STATUS.md)
