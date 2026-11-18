---
declaration: def
origin: cited
lean: TauCeti.Toric.affineToricIntegralModelBaseChangeIso
statement: formalized
---

# TauCeti.Toric.affineToricIntegralModelBaseChangeIso

The complex base change of the integral dual-semigroup model is the native affine
toric scheme, with its original coordinate ring, over `Spec ℂ`.

```lean
TauCeti.Toric.affineToricIntegralModelBaseChangeIso {V N : Type} [AddCommGroup V]
  [_root_.Module ℝ V] [AddCommGroup N] {i : N →+ V} (hi : TauCeti.Toric.IsIntegralLattice i)
  (σ : PointedCone ℝ V) :
  CategoryTheory.Over.mk
      (CategoryTheory.Limits.pullback.snd
        (AlgebraicGeometry.Spec.algebraMap ℤ
          (AddMonoidAlgebra ℤ ↥(TauCeti.Toric.dualSemigroup hi σ)))
        (AlgebraicGeometry.Spec.algebraMap ℤ ℂ)) ≅
    CategoryTheory.Over.mk
      (AlgebraicGeometry.Spec.algebraMap ℂ (TauCeti.Toric.affineCoordinateRing hi σ))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.affineToricIntegralModelBaseChangeIso`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Algebraic/IntegralModel.html#TauCeti.Toric.affineToricIntegralModelBaseChangeIso).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.affineToricIntegralModelBaseChangeIso`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Algebraic/IntegralModel.html#TauCeti.Toric.affineToricIntegralModelBaseChangeIso)
- [Source of `TauCeti.Toric.affineToricIntegralModelBaseChangeIso` in TauCeti/Geometry/Toric/Algebraic/IntegralModel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Toric/Algebraic/IntegralModel.lean#L70)
- [Tau Ceti roadmap status: Gröbner bases, affine semigroups and algebraic degenerations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GroebnerGeometry/STATUS.md)
