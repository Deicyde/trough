---
declaration: theorem
origin: cited
lean: TauCeti.CStarAction.dense_entireAnalytic
statement: formalized
proof: formalized
---

# Density of entire analytic elements

The entire analytic elements of a point-norm
continuous real action are dense, since every element is a limit of its Gaussian smearings.

```lean
TauCeti.CStarAction.dense_entireAnalytic.{u_1} {A : Type u_1} [NonUnitalCStarAlgebra A]
  (α : TauCeti.CStarAction (Multiplicative ℝ) A) : Dense ↑α.entireAnalytic
```

## Depends on

- [TauCeti.CStarAction.entireAnalytic](tauceti-cstaraction-entireanalytic.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.dense_entireAnalytic`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/GaussianSmearing.html#TauCeti.CStarAction.dense_entireAnalytic).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.dense_entireAnalytic`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/GaussianSmearing.html#TauCeti.CStarAction.dense_entireAnalytic)
- [Source of `TauCeti.CStarAction.dense_entireAnalytic` in TauCeti/Analysis/CStarAlgebra/Action/GaussianSmearing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CStarAlgebra/Action/GaussianSmearing.lean#L319)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
