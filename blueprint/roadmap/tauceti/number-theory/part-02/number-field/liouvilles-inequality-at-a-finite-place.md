---
declaration: theorem
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.abs_log_valuation_mul_log_absNorm_le_logHeight₁
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

## Sources

- [Tau Ceti documentation: `IsDedekindDomain.HeightOneSpectrum.abs_log_valuation_mul_log_absNorm_le_logHeight₁`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Places/Height.html#IsDedekindDomain.HeightOneSpectrum.abs_log_valuation_mul_log_absNorm_le_logHeight%E2%82%81)
- [Source of `IsDedekindDomain.HeightOneSpectrum.abs_log_valuation_mul_log_absNorm_le_logHeight₁` in TauCeti/NumberTheory/NumberField/Global/Places/Height.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Global/Places/Height.lean#L234)
