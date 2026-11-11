---
declaration: theorem
origin: cited
lean: TauCeti.exists_iteratedLineDerivOp_eq_and_norm_le_of_isVanishingOn_fourier
statement: formalized
proof: formalized
---

# Bernstein's inequalities

For `1 ≤ p ≤ q ≤ ∞` there is a constant `C`, depending only on
`E`, `p` and `q`, with the following property. Let `f ∈ Lᵖ` have Fourier transform vanishing
outside the closed ball of radius `R > 0`. Then for all directions `m₁, …, mₖ` the derivative
`∂_{m₁} ⋯ ∂_{mₖ} f` is an `Lᵠ` function `g` with

`‖g‖_q ≤ C ^ (k + 1) R ^ (k + n (1/p - 1/q)) ‖m₁‖ ⋯ ‖mₖ‖ ‖f‖_p`,

where `n` is the dimension of `E` and `1/∞ = 0`.

```lean
TauCeti.exists_iteratedLineDerivOp_eq_and_norm_le_of_isVanishingOn_fourier.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F]
  {p q : ENNReal} [Fact (1 ≤ p)] [Fact (1 ≤ q)] (hpq : p ≤ q) :
  ∃ C,
    0 ≤ C ∧
      ∀ (k : ℕ) (m : Fin k → E) {R : ℝ},
        0 < R →
          ∀ (f : ↥(MeasureTheory.Lp F p MeasureTheory.volume)),
            Distribution.IsVanishingOn
                (⇑(FourierTransform.fourier (MeasureTheory.Lp.toTemperedDistribution f)))
                (Metric.closedBall 0 R)ᶜ →
              ∃ g,
                LineDeriv.iteratedLineDerivOp m (MeasureTheory.Lp.toTemperedDistribution f) =
                    MeasureTheory.Lp.toTemperedDistribution g ∧
                  ‖g‖ ≤
                    (C ^ (k + 1) * R ^ (↑k + ↑(Module.finrank ℝ E) * (p.toReal⁻¹ - q.toReal⁻¹)) *
                        ∏ i, ‖m i‖) *
                      ‖f‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bernstein's inequality without derivatives](bernsteins-inequality-without-derivatives.md)
- [Young's convolution inequality](../convolution/youngs-convolution-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_iteratedLineDerivOp_eq_and_norm_le_of_isVanishingOn_fourier`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.html#TauCeti.exists_iteratedLineDerivOp_eq_and_norm_le_of_isVanishingOn_fourier).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_iteratedLineDerivOp_eq_and_norm_le_of_isVanishingOn_fourier`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.html#TauCeti.exists_iteratedLineDerivOp_eq_and_norm_le_of_isVanishingOn_fourier)
- [Source of `TauCeti.exists_iteratedLineDerivOp_eq_and_norm_le_of_isVanishingOn_fourier` in TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.lean#L291)
