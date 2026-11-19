---
declaration: def
origin: cited
lean: CommHopfAlgCat.fppfHomogeneousQuotientTranslation
statement: formalized
---

# CommHopfAlgCat.fppfHomogeneousQuotientTranslation

Left translation on the fppf homogeneous quotient, obtained by sheafifying translation
on the coset presheaf.

```lean
CommHopfAlgCat.fppfHomogeneousQuotientTranslation.{u} {R : Type u} [CommRing R]
  (H : CommHopfAlgCat R) (I : TauCeti.HopfIdeal R ↑H) (g : ↑(TauCeti.HopfAlgebra.points ↧R)) :
  H.fppfHomogeneousQuotient I ≅ H.fppfHomogeneousQuotient I
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CommHopfAlgCat.fppfHomogeneousQuotientTranslation`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/Basic.html#CommHopfAlgCat.fppfHomogeneousQuotientTranslation).

## Sources

- [Tau Ceti documentation: `CommHopfAlgCat.fppfHomogeneousQuotientTranslation`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/Basic.html#CommHopfAlgCat.fppfHomogeneousQuotientTranslation)
- [Source of `CommHopfAlgCat.fppfHomogeneousQuotientTranslation` in TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/Basic.lean#L536)
- [Tau Ceti roadmap status: Classification of parabolic subgroups and projective homogeneous spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FlagVarieties/STATUS.md)
