---
declaration: theorem
origin: cited
lean: TauCeti.puiseuxField.not_completeSpace
statement: formalized
proof: formalized
---

# The Puiseux field is not complete

The partial sums of `∑ j, t ^ ((j + 1) + 1 / (j + 2))`
form a Cauchy sequence without a limit.

```lean
TauCeti.puiseuxField.not_completeSpace.{u_1} (K : Type u_1) [Field K] :
  ¬CompleteSpace ↥(TauCeti.puiseuxField K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.puiseuxField.not_completeSpace`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/Valuation.html#TauCeti.puiseuxField.not_completeSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.puiseuxField.not_completeSpace`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/Valuation.html#TauCeti.puiseuxField.not_completeSpace)
- [Source of `TauCeti.puiseuxField.not_completeSpace` in TauCeti/RingTheory/LaurentSeries/Puiseux/Valuation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/LaurentSeries/Puiseux/Valuation.lean#L241)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
