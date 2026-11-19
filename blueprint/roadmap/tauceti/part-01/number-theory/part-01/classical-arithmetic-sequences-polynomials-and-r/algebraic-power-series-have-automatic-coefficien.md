---
declaration: theorem
origin: cited
lean: PowerSeries.isAutomatic_coeff_of_isAlgebraic
statement: formalized
proof: formalized
---

# Algebraic power series have automatic coefficients

Over a finite field `K` with `q`
elements, the coefficient sequence of a power series algebraic over `K[X]` is `q`-automatic. This
is the direction "algebraic implies automatic" of Christol's theorem.

```lean
PowerSeries.isAutomatic_coeff_of_isAlgebraic.{u_1} {K : Type u_1} [Field K] [Fintype K]
  {f : PowerSeries K} (hf : IsAlgebraic (Polynomial K) f) :
  TauCeti.IsAutomatic (Fintype.card K) fun n => (PowerSeries.coeff n) f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PowerSeries.isAutomatic_coeff_of_isAlgebraic`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Automatic.html#PowerSeries.isAutomatic_coeff_of_isAlgebraic).

## Sources

- [Tau Ceti documentation: `PowerSeries.isAutomatic_coeff_of_isAlgebraic`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Automatic.html#PowerSeries.isAutomatic_coeff_of_isAlgebraic)
- [Source of `PowerSeries.isAutomatic_coeff_of_isAlgebraic` in TauCeti/RingTheory/PowerSeries/Automatic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/PowerSeries/Automatic.lean#L210)
- [Tau Ceti roadmap status: Classical arithmetic, sequences, polynomials and reciprocity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassicalArithmeticCompletion/STATUS.md)
