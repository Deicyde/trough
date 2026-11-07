---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.relativeSpecBaseChangeIso
statement: formalized
---

# Relative Spec commutes with base change, naturally in the algebra

For `f : Y ⟶ X`,
taking the relative spectrum of the pullback of a quasicoherent algebra is naturally isomorphic
to base changing its relative spectrum along `f`.

```lean
TauCeti.AlgebraicGeometry.relativeSpecBaseChangeIso.{u} {X Y : AlgebraicGeometry.Scheme}
  (f : Y ⟶ X) :
  (TauCeti.AlgebraicGeometry.QuasicoherentAlgebra.pullback f).op.comp
      (TauCeti.AlgebraicGeometry.relativeSpec Y) ≅
    (TauCeti.AlgebraicGeometry.relativeSpec X).comp
      (TauCeti.AlgebraicGeometry.baseChangeAffineSchemeOver f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.relativeSpecBaseChangeIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/RelativeSpec/BaseChange.html#TauCeti.AlgebraicGeometry.relativeSpecBaseChangeIso).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.relativeSpecBaseChangeIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/RelativeSpec/BaseChange.html#TauCeti.AlgebraicGeometry.relativeSpecBaseChangeIso)
- [Source of `TauCeti.AlgebraicGeometry.relativeSpecBaseChangeIso` in TauCeti/AlgebraicGeometry/RelativeSpec/BaseChange.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/RelativeSpec/BaseChange.lean#L269)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
