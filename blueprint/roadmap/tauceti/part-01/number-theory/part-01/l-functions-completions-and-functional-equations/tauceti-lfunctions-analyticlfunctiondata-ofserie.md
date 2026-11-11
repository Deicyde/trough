---
declaration: def
origin: cited
lean: TauCeti.LFunctions.AnalyticLFunctionData.ofSeries
statement: formalized
---

# TauCeti.LFunctions.AnalyticLFunctionData.ofSeries

The analytic card obtained by canonically continuing a completed Dirichlet series from
`Re s > 1`. The root number is `Λ(2) / conj Λ(-1)`. The supplied polar divisor is data, not a
claim about the resulting function. If no continuation exists, the completed function and root
number are zero, by the convention for `meromorphicContinuation`.

```lean
TauCeti.LFunctions.AnalyticLFunctionData.ofSeries (coeff : ℕ → ℂ) (conductor : ℕ+)
  (gammaR gammaC : Multiset ℂ) (polarOrder : ℂ →₀ ℕ) : TauCeti.LFunctions.AnalyticLFunctionData
```

## Depends on

- [Completed L-function data in the analytic normalization](completed-l-function-data-in-the-analytic-normal.md)
- [TauCeti.meromorphicContinuation](tauceti-meromorphiccontinuation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.AnalyticLFunctionData.ofSeries`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Data/Series.html#TauCeti.LFunctions.AnalyticLFunctionData.ofSeries).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.AnalyticLFunctionData.ofSeries`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Data/Series.html#TauCeti.LFunctions.AnalyticLFunctionData.ofSeries)
- [Source of `TauCeti.LFunctions.AnalyticLFunctionData.ofSeries` in TauCeti/NumberTheory/LFunctions/Data/Series.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LFunctions/Data/Series.lean#L40)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LFunctions/STATUS.md)
