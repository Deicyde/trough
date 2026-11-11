---
declaration: theorem
origin: cited
lean: TauCeti.LaurentSeries.Level.ContinuousKaehlerDifferential.coeff_neg_one_equivLaurentSeries_trace
statement: formalized
proof: formalized
---

# The trace preserves residues

When `d` is nonzero in `K`, for every one-form `ω = g du`
on the level `L = K⸨u⸩`, the residue of `Tr_{L/F} ω` at `t` is the residue of `ω` at `u`:
`Res_F (Tr_{L/F} ω) = Res_L ω`.

```lean
TauCeti.LaurentSeries.Level.ContinuousKaehlerDifferential.coeff_neg_one_equivLaurentSeries_trace.{u_1}
  {K : Type u_1} [Field K] {d : ℕ+} [NeZero ↑↑d]
  (ω : TauCeti.LaurentSeries.Level.ContinuousKaehlerDifferential K d) :
  ((TauCeti.ContinuousKaehlerDifferential.equivLaurentSeries K)
          ((TauCeti.LaurentSeries.Level.ContinuousKaehlerDifferential.trace K d) ω)).coeff
      (-1) =
    ((TauCeti.LaurentSeries.Level.ringEquivLaurentSeries K d)
          ((TauCeti.LaurentSeries.Level.ContinuousKaehlerDifferential.equivLevel K d) ω)).coeff
      (-1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LaurentSeries.Level.ContinuousKaehlerDifferential.coeff_neg_one_equivLaurentSeries_trace`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Level/KaehlerDifferential.html#TauCeti.LaurentSeries.Level.ContinuousKaehlerDifferential.coeff_neg_one_equivLaurentSeries_trace).

## Sources

- [Tau Ceti documentation: `TauCeti.LaurentSeries.Level.ContinuousKaehlerDifferential.coeff_neg_one_equivLaurentSeries_trace`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Level/KaehlerDifferential.html#TauCeti.LaurentSeries.Level.ContinuousKaehlerDifferential.coeff_neg_one_equivLaurentSeries_trace)
- [Source of `TauCeti.LaurentSeries.Level.ContinuousKaehlerDifferential.coeff_neg_one_equivLaurentSeries_trace` in TauCeti/RingTheory/LaurentSeries/Level/KaehlerDifferential.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/LaurentSeries/Level/KaehlerDifferential.lean#L336)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
