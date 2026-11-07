---
declaration: def
origin: cited
lean: BialgHom.parabolicLeviFppfQuotientIso
statement: formalized
---

# The fppf quotient `P(λ)/U(λ)` is the dynamic Levi `Z(λ)`

The subgroup in the
quotient is given by its actual defining ideal inside the parabolic coordinate ring.

```lean
BialgHom.parabolicLeviFppfQuotientIso.{u} {R H : Type u} [CommRing R] [CommRing H] [HopfAlgebra R H]
  (l : H →ₐc[R] LaurentPolynomial R) :
  TauCeti.CommHopfAlgCat.fppfQuotientSheaf
      ((↧H).quotient (TauCeti.Cocharacter.parabolicDefiningHopfIdeal l))
      (l.unipotentDefiningHopfIdeal.map
        (CommHopfAlgCat.Hom.hom
          ((↧H).mkQuotient (TauCeti.Cocharacter.parabolicDefiningHopfIdeal l))))
      ⋯ ≅
    TauCeti.CommHopfAlgCat.pointsFppfGroupObject
      ((↧H).quotient (TauCeti.Cocharacter.leviDefiningHopfIdeal l))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`BialgHom.parabolicLeviFppfQuotientIso`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Dynamic/Levi/Quotient.html#BialgHom.parabolicLeviFppfQuotientIso).

## Sources

- [Tau Ceti documentation: `BialgHom.parabolicLeviFppfQuotientIso`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Dynamic/Levi/Quotient.html#BialgHom.parabolicLeviFppfQuotientIso)
- [Source of `BialgHom.parabolicLeviFppfQuotientIso` in TauCeti/Algebra/AlgebraicGroup/Dynamic/Levi/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlgebraicGroup/Dynamic/Levi/Quotient.lean#L175)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ReductiveGroups/STATUS.md)
