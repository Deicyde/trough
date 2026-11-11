---
declaration: theorem
origin: cited
lean: AbsolutelyContinuousOnInterval.lintegral_mul_metricDerivative_le_dissipation
statement: formalized
proof: formalized
---

# Young's inequality along a curve

the integral of `g (u r) |u'|(r)` is at most the
dissipation.

```lean
AbsolutelyContinuousOnInterval.lintegral_mul_metricDerivative_le_dissipation.{u_1} {X : Type u_1}
  [PseudoMetricSpace X] {p q : ℝ} {g : X → ENNReal} {u : ℝ → X} {s t : ℝ}
  (hpq : p.HolderConjugate q) (hu : AbsolutelyContinuousOnInterval u s t) :
  ∫⁻ (r : ℝ) in Set.uIoc s t, g (u r) * TauCeti.metricDerivative u r ≤
    TauCeti.dissipation p q g u s t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AbsolutelyContinuousOnInterval.lintegral_mul_metricDerivative_le_dissipation`](https://taucetiproject.org/docs/TauCeti/Analysis/GradientFlow/MaximalSlope/Basic.html#AbsolutelyContinuousOnInterval.lintegral_mul_metricDerivative_le_dissipation).

## Sources

- [Tau Ceti documentation: `AbsolutelyContinuousOnInterval.lintegral_mul_metricDerivative_le_dissipation`](https://taucetiproject.org/docs/TauCeti/Analysis/GradientFlow/MaximalSlope/Basic.html#AbsolutelyContinuousOnInterval.lintegral_mul_metricDerivative_le_dissipation)
- [Source of `AbsolutelyContinuousOnInterval.lintegral_mul_metricDerivative_le_dissipation` in TauCeti/Analysis/GradientFlow/MaximalSlope/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/GradientFlow/MaximalSlope/Basic.lean#L162)
