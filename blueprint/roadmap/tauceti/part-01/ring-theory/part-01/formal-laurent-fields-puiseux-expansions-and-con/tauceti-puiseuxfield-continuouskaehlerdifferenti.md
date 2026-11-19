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
- [Source of `TauCeti.puiseuxField.ContinuousKaehlerDifferential` in TauCeti/RingTheory/LaurentSeries/Puiseux/KaehlerDifferential/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/LaurentSeries/Puiseux/KaehlerDifferential/Basic.lean#L77)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
