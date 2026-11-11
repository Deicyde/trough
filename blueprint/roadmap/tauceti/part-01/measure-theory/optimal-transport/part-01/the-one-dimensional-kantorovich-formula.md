---
declaration: theorem
origin: cited
lean: TauCeti.wassersteinEDist_one_eq_lintegral_enorm_cdf_sub
statement: formalized
proof: formalized
---

# The one-dimensional Kantorovich formula

The Wasserstein distance at exponent one of two
probability laws on `ℝ` is the area between their cumulative distribution functions.

```lean
TauCeti.wassersteinEDist_one_eq_lintegral_enorm_cdf_sub (μ ν : MeasureTheory.Measure ℝ)
  [MeasureTheory.IsProbabilityMeasure μ] [MeasureTheory.IsProbabilityMeasure ν] :
  TauCeti.wassersteinEDist 1 μ ν =
    ∫⁻ (s : ℝ), ‖↑(ProbabilityTheory.cdf μ) s - ↑(ProbabilityTheory.cdf ν) s‖ₑ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.wassersteinEDist_one_eq_lintegral_enorm_cdf_sub`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/OneDimensional.html#TauCeti.wassersteinEDist_one_eq_lintegral_enorm_cdf_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.wassersteinEDist_one_eq_lintegral_enorm_cdf_sub`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/OneDimensional.html#TauCeti.wassersteinEDist_one_eq_lintegral_enorm_cdf_sub)
- [Source of `TauCeti.wassersteinEDist_one_eq_lintegral_enorm_cdf_sub` in TauCeti/MeasureTheory/OptimalTransport/Wasserstein/OneDimensional.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/OneDimensional.lean#L114)
