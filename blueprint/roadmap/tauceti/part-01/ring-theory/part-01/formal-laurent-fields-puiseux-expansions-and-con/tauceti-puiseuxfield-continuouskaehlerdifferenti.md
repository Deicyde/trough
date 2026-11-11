---
declaration: def
origin: cited
lean: TauCeti.puiseuxField.ContinuousKaehlerDifferential
statement: formalized
---

# TauCeti.puiseuxField.ContinuousKaehlerDifferential

The **continuous Kähler differentials** `Ω¹_cont(P/K)` of the Puiseux field `P`: the quotient
of the Kähler differentials `Ω[P⁄K]` by the kernel of the `P`-linear map `f dg ↦ f * dg/dt`
induced by the derivative `d/dt`.

```lean
TauCeti.puiseuxField.ContinuousKaehlerDifferential.{u_1} (K : Type u_1) [Field K] [CharZero K] :
  Type u_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.puiseuxField.ContinuousKaehlerDifferential`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/KaehlerDifferential/Basic.html#TauCeti.puiseuxField.ContinuousKaehlerDifferential).

## Sources

- [Tau Ceti documentation: `TauCeti.puiseuxField.ContinuousKaehlerDifferential`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/KaehlerDifferential/Basic.html#TauCeti.puiseuxField.ContinuousKaehlerDifferential)
- [Source of `TauCeti.puiseuxField.ContinuousKaehlerDifferential` in TauCeti/RingTheory/LaurentSeries/Puiseux/KaehlerDifferential/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/LaurentSeries/Puiseux/KaehlerDifferential/Basic.lean#L77)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
