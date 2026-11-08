---
declaration: theorem
origin: cited
lean: TauCeti.exists_circleLIntegral_sq_lt, TauCeti.exists_circleLIntegral_lt_of_lintegral_sq_ne_top
statement: formalized
proof: formalized
---

# Wolff's lemma (`TauCeti.exists_circleLIntegral_sq_lt`)

If `2 π` times the plane integral of `g ^ 2` is smaller than
`c * log (R / r)`, then some circle of radius `ρ` strictly between `r` and `R` has
`circleLIntegral g ζ ρ ^ 2 < c`.

Since `log (R / r)` grows without bound as the annulus is made longer while the plane integral
stays fixed, this makes the circle integral arbitrarily small at arbitrarily small radii: a weight
of finite square integral cannot have a large circle integral on every circle about `ζ`.

```lean
TauCeti.exists_circleLIntegral_sq_lt {g : ℂ → ENNReal} (hg : Measurable g) (ζ : ℂ) {r R : ℝ}
  (hr : 0 < r) (hrR : r < R) {c : ENNReal}
  (hc :
    ENNReal.ofReal (2 * Real.pi) * ∫⁻ (z : ℂ), g z ^ 2 < c * ENNReal.ofReal (Real.log (R / r))) :
  ∃ ρ ∈ Set.Ioo r R, TauCeti.circleLIntegral g ζ ρ ^ 2 < c
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for Young's exponents](../euclidean-isoperimetry-sharp-inequalities-and-ri/part-02/holders-inequality-for-youngs-exponents.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_circleLIntegral_sq_lt`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Circle/LIntegral.html#TauCeti.exists_circleLIntegral_sq_lt).

## Other forms

**Wolff's lemma in the limit: a weight of finite square integral has small circle integrals at arbitrarily small radii.** Formalized in Tau Ceti as [`TauCeti.exists_circleLIntegral_lt_of_lintegral_sq_ne_top`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Circle/LIntegral.html#TauCeti.exists_circleLIntegral_lt_of_lintegral_sq_ne_top).

```lean
TauCeti.exists_circleLIntegral_lt_of_lintegral_sq_ne_top {g : ℂ → ENNReal} (hg : Measurable g)
  (hfin : ∫⁻ (z : ℂ), g z ^ 2 ≠ ⊤) (ζ : ℂ) {c : ENNReal} (hc : c ≠ 0) {R : ℝ} (hR : 0 < R) :
  ∃ ρ ∈ Set.Ioo 0 R, TauCeti.circleLIntegral g ζ ρ < c
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_circleLIntegral_sq_lt`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Circle/LIntegral.html#TauCeti.exists_circleLIntegral_sq_lt)
- [Source of `TauCeti.exists_circleLIntegral_sq_lt` in TauCeti/MeasureTheory/Integral/Circle/LIntegral.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/Circle/LIntegral.lean#L374)
