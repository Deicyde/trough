---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.linearSpecEquiv
statement: formalized
---

# TauCeti.AlgebraicGeometry.linearSpecEquiv

The anti-equivalence `(QuasicoherentSheaf X)ᵒᵖ ≌ QuasicoherentLinearScheme X`: `linearSpec X`
and the degree-one functor are quasi-inverse, with unit the inverse of `degreeOneLinearSpecIso`
and counit `linearSpecDegreeOneIso`. It is the composite of the graded symmetric-algebra
equivalence `QCoh(X) ≌ FreeGrQCAlg(X)` and of `freeGradedRelativeSpecEquiv X`.

```lean
TauCeti.AlgebraicGeometry.linearSpecEquiv.{u} (X : AlgebraicGeometry.Scheme) :
  (TauCeti.AlgebraicGeometry.QuasicoherentSheaf X)ᵒᵖ ≌
    TauCeti.AlgebraicGeometry.QuasicoherentLinearScheme X
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.AlgebraicGeometry.relativeSpecEquiv](tauceti-algebraicgeometry-relativespecequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.linearSpecEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/VectorBundle/LinearScheme.html#TauCeti.AlgebraicGeometry.linearSpecEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.linearSpecEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/VectorBundle/LinearScheme.html#TauCeti.AlgebraicGeometry.linearSpecEquiv)
- [Source of `TauCeti.AlgebraicGeometry.linearSpecEquiv` in TauCeti/AlgebraicGeometry/VectorBundle/LinearScheme.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/VectorBundle/LinearScheme.lean#L292)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
