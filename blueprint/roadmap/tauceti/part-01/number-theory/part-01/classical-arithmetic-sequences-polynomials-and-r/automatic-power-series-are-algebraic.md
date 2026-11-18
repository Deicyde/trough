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

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PowerSeries.isAlgebraic_of_isAutomatic_coeff`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Christol.html#PowerSeries.isAlgebraic_of_isAutomatic_coeff).

## Sources

- [Tau Ceti documentation: `PowerSeries.isAlgebraic_of_isAutomatic_coeff`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Christol.html#PowerSeries.isAlgebraic_of_isAutomatic_coeff)
- [Source of `PowerSeries.isAlgebraic_of_isAutomatic_coeff` in TauCeti/RingTheory/PowerSeries/Christol.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/PowerSeries/Christol.lean#L122)
- [Tau Ceti roadmap status: Classical arithmetic, sequences, polynomials and reciprocity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassicalArithmeticCompletion/STATUS.md)
