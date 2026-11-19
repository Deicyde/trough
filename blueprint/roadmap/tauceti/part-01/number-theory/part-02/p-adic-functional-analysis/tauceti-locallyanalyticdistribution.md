---
declaration: def
origin: cited
lean: TauCeti.LocallyAnalyticDistribution
statement: formalized
---

# TauCeti.LocallyAnalyticDistribution

The locally analytic distributions on `ℤ_p` with values in `K`: the `K`-linear functionals
on the locally analytic functions `LA(ℤ_p, K)` whose restriction to every analytic stage
`LA_h(K)` is continuous, that is, bounded for the Gauss norm.

```lean
TauCeti.LocallyAnalyticDistribution.{u_1} (p : ℕ) [Fact (Nat.Prime p)] (K : Type u_1)
  [NontriviallyNormedField K] [Algebra ℤ_[p] K] [IsBoundedSMul ℤ_[p] K] [IsUltrametricDist K]
  [CompleteSpace K] : Submodule K (Module.Dual K (TauCeti.LocallyAnalytic p K K))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LocallyAnalyticDistribution`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Dual.html#TauCeti.LocallyAnalyticDistribution).

## Sources

- [Tau Ceti documentation: `TauCeti.LocallyAnalyticDistribution`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Dual.html#TauCeti.LocallyAnalyticDistribution)
- [Source of `TauCeti.LocallyAnalyticDistribution` in TauCeti/NumberTheory/Padics/Distribution/Dual.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Padics/Distribution/Dual.lean#L76)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
