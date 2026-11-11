---
declaration: theorem
origin: cited
lean: TauCeti.Vortex.exists_exterior_integral_norm_sq_gaugeFixedOperator_ge
statement: formalized
proof: formalized
---

# Exterior coercivity of the gauge-fixed vortex operator

For an actual vortex with
`|α| → 1` and `∇₁ α → 0` at infinity, and `0 < c < 1/2`, there is a radius `R > 0`, depending
only on the vortex and `c`, such that `c² ∫|y|² ≤ ∫|L_x y|²` for every compactly supported `C²`
variation `y` vanishing on the closed disc of radius `R` about the origin. This is the Gårding
inequality `exists_integral_gaugeFixedGradientDensity_add_mul_integral_norm_sq_le` at mass `c²`,
whose compact remainder vanishes for such variations.

```lean
TauCeti.Vortex.exists_exterior_integral_norm_sq_gaugeFixedOperator_ge
  {x : ℂ → EuclideanSpace ℝ (Fin 4)} {μ : MeasureTheory.Measure ℂ} [μ.IsAddHaarMeasure]
  (hx : ContDiff ℝ 1 x) (hsol : ∀ (z : ℂ), TauCeti.Vortex.equation x z = 0)
  (hlim :
    Filter.Tendsto (fun z => 4 * ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2)) (Filter.cocompact ℂ)
      (nhds 1))
  (hcov :
    Filter.Tendsto (fun z => TauCeti.Vortex.covariantDerivative x z 1) (Filter.cocompact ℂ)
      (nhds 0))
  {c : ℝ} (hc : 0 < c) (hc' : c < 1 / 2) :
  ∃ R > 0,
    ∀ (y : ℂ → EuclideanSpace ℝ (Fin 4)),
      ContDiff ℝ 2 y →
        HasCompactSupport y →
          (∀ (z : ℂ), ‖z‖ ≤ R → y z = 0) →
            c ^ 2 * ∫ (z : ℂ), ‖y z‖ ^ 2 ∂μ ≤
              ∫ (z : ℂ), ‖TauCeti.Vortex.gaugeFixedOperator x y z‖ ^ 2 ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gårding's inequality on `H¹(Ω)`](../../part-03/pde/part-01/gardings-inequality-on-h1.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.exists_exterior_integral_norm_sq_gaugeFixedOperator_ge`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/ExteriorEstimate.html#TauCeti.Vortex.exists_exterior_integral_norm_sq_gaugeFixedOperator_ge).

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.exists_exterior_integral_norm_sq_gaugeFixedOperator_ge`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/ExteriorEstimate.html#TauCeti.Vortex.exists_exterior_integral_norm_sq_gaugeFixedOperator_ge)
- [Source of `TauCeti.Vortex.exists_exterior_integral_norm_sq_gaugeFixedOperator_ge` in TauCeti/Analysis/PDE/Vortex/ExteriorEstimate.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Vortex/ExteriorEstimate.lean#L196)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TaubesGromov/STATUS.md)
