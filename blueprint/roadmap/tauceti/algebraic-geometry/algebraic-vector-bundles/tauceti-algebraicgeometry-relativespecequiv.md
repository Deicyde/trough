---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.relativeSpecEquiv
statement: formalized
---

# TauCeti.AlgebraicGeometry.relativeSpecEquiv

Relative Spec and the algebra of regular functions give an anti-equivalence between
quasi-coherent commutative algebras and affine schemes over an arbitrary base scheme. Its unit
and counit are the canonical section and affine-chart comparisons.

```lean
TauCeti.AlgebraicGeometry.relativeSpecEquiv.{u} (X : AlgebraicGeometry.Scheme) :
  (TauCeti.AlgebraicGeometry.QuasicoherentAlgebra X)ᵒᵖ ≌
    TauCeti.AlgebraicGeometry.AffineSchemeOver X
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.relativeSpecEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/RelativeSpec/Equivalence.html#TauCeti.AlgebraicGeometry.relativeSpecEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.relativeSpecEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/RelativeSpec/Equivalence.html#TauCeti.AlgebraicGeometry.relativeSpecEquiv)
- [Source of `TauCeti.AlgebraicGeometry.relativeSpecEquiv` in TauCeti/AlgebraicGeometry/RelativeSpec/Equivalence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/RelativeSpec/Equivalence.lean#L111)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
