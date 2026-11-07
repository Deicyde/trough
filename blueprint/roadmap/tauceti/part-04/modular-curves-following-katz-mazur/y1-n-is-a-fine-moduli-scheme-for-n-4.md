---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneNaiveRepresentableBy
statement: formalized
---

# `Y₁(N)` is a fine moduli scheme for `N ≥ 4`

For `N ≥ 4`, the naive moduli problem
`[Γ₁(N)]` over `Ell/B` is represented by the universal elliptic curve over `Y₁(N)`
(`EllObj.yOne B N`): the naive `[Γ₁(N)]`-structures on an object `X` of `Ell/B` correspond to
the arrows `X ⟶ EllObj.yOne B N`, by pulling back the point `(0, 0)`
(`naiveLevelEquiv_gammaOneNaiveRepresentableBy_homEquiv`).

```lean
TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneNaiveRepresentableBy.{u}
  {B : AlgebraicGeometry.Scheme} {N : ℕ} [NeZero N] (h4 : 4 ≤ N) :
  CategoryTheory.Functor.RepresentableBy (TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneNaive B N)
    (TauCeti.AlgebraicGeometry.EllObj.yOne B N)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneNaiveRepresentableBy`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/YOne.html#TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneNaiveRepresentableBy).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneNaiveRepresentableBy`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/YOne.html#TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneNaiveRepresentableBy)
- [Source of `TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneNaiveRepresentableBy` in TauCeti/AlgebraicGeometry/ModularCurve/YOne.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/ModularCurve/YOne.lean#L661)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularCurves/STATUS.md)
