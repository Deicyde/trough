---
declaration: theorem
origin: cited
lean: PowerSeries.isAlgebraic_of_isAutomatic_coeff
statement: formalized
proof: formalized
---

# Automatic power series are algebraic

Over a finite field `K` with `q` elements, a power
series whose coefficient sequence is `q`-automatic is algebraic over `K[X]`.

```lean
PowerSeries.isAlgebraic_of_isAutomatic_coeff.{u_1} {K : Type u_1} [Field K] [Fintype K]
  {f : PowerSeries K} (hf : TauCeti.IsAutomatic (Fintype.card K) fun n => (PowerSeries.coeff n) f) :
  IsAlgebraic (Polynomial K) f
```

## Depends on

- [TauCeti.IsAutomatic](tauceti-isautomatic.md)

## Lean

Formalized in Tau Ceti as [`PowerSeries.isAlgebraic_of_isAutomatic_coeff`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Christol.html#PowerSeries.isAlgebraic_of_isAutomatic_coeff).

## Sources

- [Tau Ceti documentation: `PowerSeries.isAlgebraic_of_isAutomatic_coeff`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Christol.html#PowerSeries.isAlgebraic_of_isAutomatic_coeff)
- [Source of `PowerSeries.isAlgebraic_of_isAutomatic_coeff` in TauCeti/RingTheory/PowerSeries/Christol.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/PowerSeries/Christol.lean#L122)
- [Tau Ceti roadmap status: Classical arithmetic, sequences, polynomials and reciprocity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassicalArithmeticCompletion/STATUS.md)
