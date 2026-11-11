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
- [Source of `TauCeti.AlgebraicGeometry.relativeSpecBaseChangeIso` in TauCeti/AlgebraicGeometry/RelativeSpec/BaseChange.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/RelativeSpec/BaseChange.lean#L269)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
