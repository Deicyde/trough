---
declaration: theorem
origin: cited
lean: TauCeti.LaurentSeries.Level.ramificationIdx_valuationOfFinrankEq
statement: formalized
proof: formalized
---

# TauCeti.LaurentSeries.Level.ramificationIdx_valuationOfFinrankEq

The ramification index of an extension of degree `e` is `e`, with respect to the
normalized discrete valuation.

```lean
TauCeti.LaurentSeries.Level.ramificationIdx_valuationOfFinrankEq.{u_1, u_2} {K : Type u_1} [Field K]
  [IsAlgClosed K] [CharZero K] {L : Type u_2} [Field L] [Algebra (LaurentSeries K) L] {e : ℕ+}
  (h : Module.finrank (LaurentSeries K) L = ↑e) :
  (IsLocalRing.maximalIdeal
          ↥(TauCeti.LaurentSeries.Level.valuationOfFinrankEq h).valuationSubring).ramificationIdx
      ↥Valued.v.valuationSubring =
    ↑e
```

## Depends on

- [Finite extensions of `K⸨X⸩`](finite-extensions-of-kx.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LaurentSeries.Level.ramificationIdx_valuationOfFinrankEq`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Level/FiniteExtensionValuation.html#TauCeti.LaurentSeries.Level.ramificationIdx_valuationOfFinrankEq).

## Sources

- [Tau Ceti documentation: `TauCeti.LaurentSeries.Level.ramificationIdx_valuationOfFinrankEq`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Level/FiniteExtensionValuation.html#TauCeti.LaurentSeries.Level.ramificationIdx_valuationOfFinrankEq)
- [Source of `TauCeti.LaurentSeries.Level.ramificationIdx_valuationOfFinrankEq` in TauCeti/RingTheory/LaurentSeries/Level/FiniteExtensionValuation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/LaurentSeries/Level/FiniteExtensionValuation.lean#L154)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
