---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy
statement: formalized
---

# TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy

For `N ≥ 4` invertible on `B`, the existing fine curve `Y₁(N)` also represents the
integral Drinfeld `[Γ₁(N)]` problem restricted to `B`.

```lean
TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy.{u} {B : AlgebraicGeometry.Scheme}
  {N : ℕ} [NeZero N] {hN : ∀ (b : ↥B), ↑N ≠ 0} (h4 : 4 ≤ N) :
  CategoryTheory.Functor.RepresentableBy (TauCeti.AlgebraicGeometry.ModuliProblem.gammaOne B N)
    (TauCeti.AlgebraicGeometry.EllObj.yOne B N)
```

## Depends on

- [`Y₁(N)` is a fine moduli scheme for `N ≥ 4`](y1-n-is-a-fine-moduli-scheme-for-n-4.md)

## Proof depends on

- [TauCeti.AlgebraicGeometry.EllipticCurveGeom.etale_torsion_hom_of_forall_intCast_ne_zero](tauceti-algebraicgeometry-ellipticcurvegeom-etal.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.html#TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.html#TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy)
- [Source of `TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRepresentableBy` in TauCeti/AlgebraicGeometry/ModularCurve/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.lean#L186)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularCurves/STATUS.md)
