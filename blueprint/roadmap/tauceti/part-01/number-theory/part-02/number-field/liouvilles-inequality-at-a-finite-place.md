---
declaration: theorem
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.abs_log_valuation_mul_log_absNorm_le_logHeight₁, NumberField.FinitePlace.abs_log_le_logHeight₁, NumberField.InfinitePlace.abs_log_le_logHeight₁, NumberField.InfinitePlace.abs_mult_mul_log_le_logHeight₁
statement: formalized
proof: formalized
---

# Liouville's inequality at a finite place

The absolute value of the order
`-WithZero.log (v.valuation K x)` of an element `x` of a number field at a finite place `v`,
weighted by the logarithm of the norm of `v`, is at most the logarithmic height of `x`. Both sides
vanish at `x = 0`.

```lean
IsDedekindDomain.HeightOneSpectrum.abs_log_valuation_mul_log_absNorm_le_logHeight₁.{u_1}
  {K : Type u_1} [Field K] [NumberField K]
  (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)) (x : K) :
  ↑|((IsDedekindDomain.HeightOneSpectrum.valuation K v) x).log| *
      Real.log ↑(Ideal.absNorm v.asIdeal) ≤
    Height.logHeight₁ x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsDedekindDomain.HeightOneSpectrum.abs_log_valuation_mul_log_absNorm_le_logHeight₁`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Places/Height.html#IsDedekindDomain.HeightOneSpectrum.abs_log_valuation_mul_log_absNorm_le_logHeight%E2%82%81).

## Other forms

**Liouville's inequality at a finite place, for the absolute value of a `FinitePlace`.** Formalized in Tau Ceti as [`NumberField.FinitePlace.abs_log_le_logHeight₁`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Places/Height.html#NumberField.FinitePlace.abs_log_le_logHeight%E2%82%81).

```lean
NumberField.FinitePlace.abs_log_le_logHeight₁.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (v : NumberField.FinitePlace K) (x : K) : |Real.log (v x)| ≤ Height.logHeight₁ x
```

**Liouville's inequality at an infinite place, unweighted.** Formalized in Tau Ceti as [`NumberField.InfinitePlace.abs_log_le_logHeight₁`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Places/Height.html#NumberField.InfinitePlace.abs_log_le_logHeight%E2%82%81).

```lean
NumberField.InfinitePlace.abs_log_le_logHeight₁.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (w : NumberField.InfinitePlace K) (x : K) : |Real.log (w x)| ≤ Height.logHeight₁ x
```

**Liouville's inequality at an infinite place.** Formalized in Tau Ceti as [`NumberField.InfinitePlace.abs_mult_mul_log_le_logHeight₁`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Places/Height.html#NumberField.InfinitePlace.abs_mult_mul_log_le_logHeight%E2%82%81).

```lean
NumberField.InfinitePlace.abs_mult_mul_log_le_logHeight₁.{u_1} {K : Type u_1} [Field K]
  [NumberField K] (w : NumberField.InfinitePlace K) (x : K) :
  |↑w.mult * Real.log (w x)| ≤ Height.logHeight₁ x
```

## Sources

- [Tau Ceti documentation: `IsDedekindDomain.HeightOneSpectrum.abs_log_valuation_mul_log_absNorm_le_logHeight₁`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Places/Height.html#IsDedekindDomain.HeightOneSpectrum.abs_log_valuation_mul_log_absNorm_le_logHeight%E2%82%81)
- [Source of `IsDedekindDomain.HeightOneSpectrum.abs_log_valuation_mul_log_absNorm_le_logHeight₁` in TauCeti/NumberTheory/NumberField/Global/Places/Height.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/Global/Places/Height.lean#L239)
