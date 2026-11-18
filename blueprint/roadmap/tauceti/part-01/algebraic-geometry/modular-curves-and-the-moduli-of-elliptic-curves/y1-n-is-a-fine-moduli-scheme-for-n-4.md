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
- [Source of `TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneNaiveRepresentableBy` in TauCeti/AlgebraicGeometry/ModularCurve/YOne.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/ModularCurve/YOne.lean#L661)
- [Tau Ceti roadmap status: Modular curves and the moduli of elliptic curves with level structure](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ModularCurves/STATUS.md)
