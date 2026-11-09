---
declaration: structure
origin: cited
lean: TauCeti.RiemannSurface.MeromorphicFunction
statement: formalized
---

# TauCeti.RiemannSurface.MeromorphicFunction

A **meromorphic function** on a Riemann surface `X`: a holomorphic map `X → OnePoint ℂ` to the
Riemann sphere which is not the constant map `∞`. On a connected `X` these form a field
(`TauCeti.RiemannSurface.MeromorphicFunction.instField`).

```lean
TauCeti.RiemannSurface.MeromorphicFunction.{u_1} (X : Type u_1) [TopologicalSpace X]
  [ChartedSpace ℂ X] : Type u_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.RiemannSurface.MeromorphicFunction`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/FunctionField.html#TauCeti.RiemannSurface.MeromorphicFunction).

## Sources

- [Tau Ceti documentation: `TauCeti.RiemannSurface.MeromorphicFunction`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/FunctionField.html#TauCeti.RiemannSurface.MeromorphicFunction)
- [Source of `TauCeti.RiemannSurface.MeromorphicFunction` in TauCeti/Analysis/Complex/RiemannSurface/FunctionField.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/RiemannSurface/FunctionField.lean#L102)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BelyiMaps/STATUS.md)
