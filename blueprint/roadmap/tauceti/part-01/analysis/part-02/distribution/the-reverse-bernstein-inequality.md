---
declaration: theorem
origin: cited
lean: OrthonormalBasis.exists_norm_le_div_pow_mul_sum_norm_of_iteratedLineDerivOp_eq, SchwartzMap.exists_eLpNorm_le_eLpNorm_iteratedFDeriv_of_support_fourier_subset, OrthonormalBasis.exists_norm_le_div_mul_sum_norm_of_lineDerivOp_eq
statement: formalized
proof: formalized
---

# The reverse Bernstein inequality

Let `b` be an orthonormal basis of `E` and `B` a real
number. There is a constant `C`, depending only on `b` and `B`, with the following property. Let
`1 ≤ p ≤ ∞` and let `f ∈ Lᵖ` have Fourier transform vanishing on the ball of radius `R > 0` and
outside the closed ball of radius `B R`. If for every `i : Fin k → ι` the derivative
`∂_{b_{i₀}} ⋯ ∂_{b_{iₖ₋₁}} f` of order `k` is the `Lᵖ` function `gᵢ`, then

`‖f‖_p ≤ (C / R) ^ k ∑ᵢ ‖gᵢ‖_p`.

Bernstein's inequality `TauCeti.exists_iteratedLineDerivOp_eq_and_norm_le_of_isVanishingOn_fourier`
provides the functions `gᵢ`, and bounds each of them by a constant multiple of `R ^ k ‖f‖_p`.

```lean
OrthonormalBasis.exists_norm_le_div_pow_mul_sum_norm_of_iteratedLineDerivOp_eq.{u_1, u_2, u_3}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F]
  [NormedSpace ℂ F] [CompleteSpace F] {ι : Type u_3} [Fintype ι] (b : OrthonormalBasis ι ℝ E)
  (B : ℝ) :
  ∃ C,
    0 ≤ C ∧
      ∀ {p : ENNReal} [inst : Fact (1 ≤ p)] (k : ℕ) {R : ℝ},
        0 < R →
          ∀ (f : ↥(MeasureTheory.Lp F p MeasureTheory.volume))
            (g : (Fin k → ι) → ↥(MeasureTheory.Lp F p MeasureTheory.volume)),
            Distribution.IsVanishingOn
                (⇑(FourierTransform.fourier (MeasureTheory.Lp.toTemperedDistribution f)))
                (Metric.ball 0 R ∪ (Metric.closedBall 0 (B * R))ᶜ) →
              (∀ (i : Fin k → ι),
                  LineDeriv.iteratedLineDerivOp (⇑b ∘ i)
                      (MeasureTheory.Lp.toTemperedDistribution f) =
                    MeasureTheory.Lp.toTemperedDistribution (g i)) →
                ‖f‖ ≤ (C / R) ^ k * ∑ i, ‖g i‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bernstein's inequalities](bernsteins-inequalities.md)
- [Young's convolution inequality](../convolution/youngs-convolution-inequality.md)
- [Young's inequality `L¹ ⋆ L² ⊆ L²`](../convolution/youngs-inequality-l1-l2-l2.md)

## Lean

Formalized in Tau Ceti as [`OrthonormalBasis.exists_norm_le_div_pow_mul_sum_norm_of_iteratedLineDerivOp_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.html#OrthonormalBasis.exists_norm_le_div_pow_mul_sum_norm_of_iteratedLineDerivOp_eq).

## Other forms

**The reverse Bernstein inequality.** Formalized in Tau Ceti as [`SchwartzMap.exists_eLpNorm_le_eLpNorm_iteratedFDeriv_of_support_fourier_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/SchwartzSpace/Bernstein.html#SchwartzMap.exists_eLpNorm_le_eLpNorm_iteratedFDeriv_of_support_fourier_subset).

```lean
SchwartzMap.exists_eLpNorm_le_eLpNorm_iteratedFDeriv_of_support_fourier_subset.{u_1, u_2}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F]
  [NormedSpace ℂ F] [CompleteSpace F] (k : ℕ) (θ : ℝ) {p : ENNReal} (hp : 1 ≤ p) :
  ∃ C,
    ∀ {R : ℝ},
      0 < R →
        ∀ (f : SchwartzMap E F),
          Function.support ⇑(FourierTransform.fourier f) ⊆ {ξ | R ≤ ‖ξ‖ ∧ ‖ξ‖ ≤ θ * R} →
            MeasureTheory.eLpNorm (⇑f) p MeasureTheory.volume ≤
              ↑C * ENNReal.ofReal (R⁻¹ ^ k) *
                MeasureTheory.eLpNorm (iteratedFDeriv ℝ k ⇑f) p MeasureTheory.volume
```

**The reverse Bernstein inequality for one derivative.** Formalized in Tau Ceti as [`OrthonormalBasis.exists_norm_le_div_mul_sum_norm_of_lineDerivOp_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.html#OrthonormalBasis.exists_norm_le_div_mul_sum_norm_of_lineDerivOp_eq).

```lean
OrthonormalBasis.exists_norm_le_div_mul_sum_norm_of_lineDerivOp_eq.{u_1, u_2, u_3} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F]
  {ι : Type u_3} [Fintype ι] (b : OrthonormalBasis ι ℝ E) (B : ℝ) :
  ∃ C,
    0 ≤ C ∧
      ∀ {p : ENNReal} [inst : Fact (1 ≤ p)] {R : ℝ},
        0 < R →
          ∀ (f : ↥(MeasureTheory.Lp F p MeasureTheory.volume))
            (g : ι → ↥(MeasureTheory.Lp F p MeasureTheory.volume)),
            Distribution.IsVanishingOn
                (⇑(FourierTransform.fourier (MeasureTheory.Lp.toTemperedDistribution f)))
                (Metric.ball 0 R ∪ (Metric.closedBall 0 (B * R))ᶜ) →
              (∀ (i : ι),
                  LineDeriv.lineDerivOp (b i) (MeasureTheory.Lp.toTemperedDistribution f) =
                    MeasureTheory.Lp.toTemperedDistribution (g i)) →
                ‖f‖ ≤ C / R * ∑ i, ‖g i‖
```

## Sources

- [Tau Ceti documentation: `OrthonormalBasis.exists_norm_le_div_pow_mul_sum_norm_of_iteratedLineDerivOp_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.html#OrthonormalBasis.exists_norm_le_div_pow_mul_sum_norm_of_iteratedLineDerivOp_eq)
- [Source of `OrthonormalBasis.exists_norm_le_div_pow_mul_sum_norm_of_iteratedLineDerivOp_eq` in TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.lean#L550)
