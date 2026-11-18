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
- [Source of `TauCeti.AlgebraicGeometry.relativeSpecEquiv` in TauCeti/AlgebraicGeometry/RelativeSpec/Equivalence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/RelativeSpec/Equivalence.lean#L111)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
