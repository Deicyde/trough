---
declaration: theorem
origin: cited
lean: TauCeti.isLeast_lintegral_isContinuityEquation
statement: formalized
proof: formalized
---

# The Benamou–Brenier formula

For `1 ≤ p < ∞` and probability measures `μ₀`, `μ₁` on a
finite-dimensional real normed space at finite Wasserstein distance, `W_p (μ₀, μ₁) ^ p` is the
least `p`-action `∫₀¹ ∫ ‖vₜ‖ ^ p dνₜ dt` of a curve `t ↦ νₜ` of finite measures, narrowly
continuous on `[0, 1]` and joining `μ₀` to `μ₁`, solving the continuity equation with velocity `v`
on `(0, 1)`. The minimum is attained by the displacement interpolation of an optimal coupling.

```lean
TauCeti.isLeast_lintegral_isContinuityEquation.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [MeasurableSpace E] [FiniteDimensional ℝ E] [BorelSpace E]
  {μ₀ μ₁ : MeasureTheory.Measure E} [MeasureTheory.IsProbabilityMeasure μ₀]
  [MeasureTheory.IsProbabilityMeasure μ₁] {p : ENNReal} (hp : 1 ≤ p) (hp_top : p ≠ ⊤)
  (hfin : TauCeti.wassersteinEDist p μ₀ μ₁ ≠ ⊤) :
  IsLeast
    {A |
      ∃ ν v,
        TauCeti.IsContinuityEquation (fun t => ↑(ν t)) v 0 1 ∧
          ContinuousOn ν (Set.Icc 0 1) ∧
            ↑(ν 0) = μ₀ ∧
              ↑(ν 1) = μ₁ ∧ ∫⁻ (t : ℝ) in Set.Ioo 0 1, ∫⁻ (x : E), ‖v t x‖ₑ ^ p.toReal ∂↑(ν t) = A}
    (TauCeti.wassersteinEDist p μ₀ μ₁ ^ p.toReal)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isLeast_lintegral_isContinuityEquation`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/BenamouBrenier.html#TauCeti.isLeast_lintegral_isContinuityEquation).

## Sources

- [Tau Ceti documentation: `TauCeti.isLeast_lintegral_isContinuityEquation`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/BenamouBrenier.html#TauCeti.isLeast_lintegral_isContinuityEquation)
- [Source of `TauCeti.isLeast_lintegral_isContinuityEquation` in TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/BenamouBrenier.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/BenamouBrenier.lean#L208)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OptimalTransport/STATUS.md)
