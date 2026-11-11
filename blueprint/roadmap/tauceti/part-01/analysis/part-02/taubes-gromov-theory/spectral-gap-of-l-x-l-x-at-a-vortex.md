---
declaration: theorem
origin: cited
lean: TauCeti.Vortex.exists_pos_mul_integral_norm_sq_le_integral_norm_sq_gaugeFixedAdjoint
statement: formalized
proof: formalized
---

# Spectral gap of `L_x L_x*` at a vortex

For an actual vortex with unit-modulus end,
there is `c > 0`, depending only on the vortex, such that `c ∫|η|² ≤ ∫|L_x* η|²` for every
compactly supported `C²` field `η`.

```lean
TauCeti.Vortex.exists_pos_mul_integral_norm_sq_le_integral_norm_sq_gaugeFixedAdjoint
  {x : ℂ → EuclideanSpace ℝ (Fin 4)} {μ : MeasureTheory.Measure ℂ} [μ.IsAddHaarMeasure]
  (hx : ContDiff ℝ 1 x) (hsol : ∀ (z : ℂ), TauCeti.Vortex.equation x z = 0)
  (hlim :
    Filter.Tendsto (fun z => 4 * ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2)) (Filter.cocompact ℂ)
      (nhds 1)) :
  ∃ c > 0,
    ∀ (η : ℂ → EuclideanSpace ℝ (Fin 4)),
      ContDiff ℝ 2 η →
        HasCompactSupport η →
          c * ∫ (z : ℂ), ‖η z‖ ^ 2 ∂μ ≤ ∫ (z : ℂ), ‖TauCeti.Vortex.gaugeFixedAdjoint x η z‖ ^ 2 ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Poincaré inequality on a ball](../../part-03/sobolev/part-02/the-poincare-inequality-on-a-ball.md)
- [The Weitzenböck formula at a vortex](the-weitzenbock-formula-at-a-vortex.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.exists_pos_mul_integral_norm_sq_le_integral_norm_sq_gaugeFixedAdjoint`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/SpectralGap.html#TauCeti.Vortex.exists_pos_mul_integral_norm_sq_le_integral_norm_sq_gaugeFixedAdjoint).

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.exists_pos_mul_integral_norm_sq_le_integral_norm_sq_gaugeFixedAdjoint`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/SpectralGap.html#TauCeti.Vortex.exists_pos_mul_integral_norm_sq_le_integral_norm_sq_gaugeFixedAdjoint)
- [Source of `TauCeti.Vortex.exists_pos_mul_integral_norm_sq_le_integral_norm_sq_gaugeFixedAdjoint` in TauCeti/Analysis/PDE/Vortex/SpectralGap.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Vortex/SpectralGap.lean#L147)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TaubesGromov/STATUS.md)
