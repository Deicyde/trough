---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.not_LSeriesHasSum_alternatingCoeff_one
statement: formalized
proof: formalized
---

# TauCeti.LSeries.not_LSeriesHasSum_alternatingCoeff_one

No unconditional sum at the boundary exists for the alternating coefficients, regardless
of the proposed value. This does not contradict their ordered boundary limit.

```lean
TauCeti.LSeries.not_LSeriesHasSum_alternatingCoeff_one (L : ℂ) :
  ¬LSeriesHasSum TauCeti.LSeries.alternatingCoeff 1 L
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.not_LSeriesHasSum_alternatingCoeff_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/RejectionTests.html#TauCeti.LSeries.not_LSeriesHasSum_alternatingCoeff_one).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.not_LSeriesHasSum_alternatingCoeff_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/RejectionTests.html#TauCeti.LSeries.not_LSeriesHasSum_alternatingCoeff_one)
- [Source of `TauCeti.LSeries.not_LSeriesHasSum_alternatingCoeff_one` in TauCeti/NumberTheory/LSeries/BoundaryConvergence/RejectionTests.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LSeries/BoundaryConvergence/RejectionTests.lean#L106)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
