---
declaration: theorem
origin: cited
lean: TauCeti.not_exists_riemannianEDist_le_mul_exp_maximalIntegralCurve_neg_mgradient_pow_four
statement: formalized
proof: formalized
---

# Polynomial, not exponential, convergence to a degenerate minimum

For `x₀ ≠ 0`, the
trajectory of `-grad x⁴` through `x₀` converges to `0`, but its distance to `0` is bounded by
`C exp (-μ t)` for large `t` for no `μ > 0` and `C > 0`. So the nondegeneracy hypothesis of
`TauCeti.exists_riemannianEDist_le_mul_exp_maximalIntegralCurve_neg_mgradient` cannot be
dropped.

```lean
TauCeti.not_exists_riemannianEDist_le_mul_exp_maximalIntegralCurve_neg_mgradient_pow_four {x₀ : ℝ}
  (hx₀ : x₀ ≠ 0) :
  ¬∃ μ > 0,
      ∃ C > 0,
        ∀ᶠ (t : ℝ) in Filter.atTop,
          Manifold.riemannianEDist (modelWithCornersSelf ℝ ℝ)
              (maximalIntegralCurve
                (-TauCeti.Manifold.mgradient (modelWithCornersSelf ℝ ℝ) fun y => y ^ 4) x₀ t)
              0 ≤
            ENNReal.ofReal (C * Real.exp (-(μ * t)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.not_exists_riemannianEDist_le_mul_exp_maximalIntegralCurve_neg_mgradient_pow_four`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Examples/ExponentialConvergence.html#TauCeti.not_exists_riemannianEDist_le_mul_exp_maximalIntegralCurve_neg_mgradient_pow_four).

## Sources

- [Tau Ceti documentation: `TauCeti.not_exists_riemannianEDist_le_mul_exp_maximalIntegralCurve_neg_mgradient_pow_four`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Examples/ExponentialConvergence.html#TauCeti.not_exists_riemannianEDist_le_mul_exp_maximalIntegralCurve_neg_mgradient_pow_four)
- [Source of `TauCeti.not_exists_riemannianEDist_le_mul_exp_maximalIntegralCurve_neg_mgradient_pow_four` in TauCeti/Geometry/Manifold/Morse/Examples/ExponentialConvergence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/Examples/ExponentialConvergence.lean#L147)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MorseTheory/STATUS.md)
