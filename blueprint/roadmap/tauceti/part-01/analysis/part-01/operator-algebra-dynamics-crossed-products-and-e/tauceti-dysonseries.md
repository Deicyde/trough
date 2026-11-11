---
declaration: def
origin: cited
lean: TauCeti.dysonSeries
statement: formalized
---

# TauCeti.dysonSeries

The Dyson series, or time-ordered exponential, of `p`: the sum of the iterated integrals
`dysonTerm p n t`. For continuous `p` it is the solution of `Γ' t = Γ t * p t` with `Γ 0 = 1`
(`hasDerivAt_dysonSeries`, `eq_mul_dysonSeries`).

```lean
TauCeti.dysonSeries.{u_1} {B : Type u_1} [NormedRing B] [NormedAlgebra ℝ B] (p : ℝ → B) (t : ℝ) : B
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.dysonSeries`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/DysonSeries.html#TauCeti.dysonSeries).

## Sources

- [Tau Ceti documentation: `TauCeti.dysonSeries`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/DysonSeries.html#TauCeti.dysonSeries)
- [Source of `TauCeti.dysonSeries` in TauCeti/Analysis/ODE/DysonSeries.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/ODE/DysonSeries.lean#L175)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
