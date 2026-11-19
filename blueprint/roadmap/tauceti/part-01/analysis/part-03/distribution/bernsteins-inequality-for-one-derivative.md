---
declaration: theorem
origin: cited
lean: TauCeti.exists_lineDerivOp_eq_and_norm_le_of_isVanishingOn_fourier, TemperedDistribution.exists_littlewoodPaleyBlock_eq_and_norm_le_of_le, TauCeti.exists_eq_and_norm_le_of_isVanishingOn_fourier
statement: formalized
proof: formalized
---

# Bernstein's inequality for one derivative

There is a constant `C`, depending only on
`E`, with the following property. For `1 ≤ p ≤ ∞`, an `Lᵖ` function `f` whose Fourier transform
vanishes outside the closed ball of radius `R > 0` has its derivative `∂_m f` in `Lᵖ`, with
`‖∂_m f‖_p ≤ C R ‖m‖ ‖f‖_p`.

```lean
TauCeti.exists_lineDerivOp_eq_and_norm_le_of_isVanishingOn_fourier.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F] :
  ∃ C,
    0 ≤ C ∧
      ∀ {p : ENNReal} [inst : Fact (1 ≤ p)] {R : ℝ},
        0 < R →
          ∀ (f : ↥(MeasureTheory.Lp F p MeasureTheory.volume)),
            Distribution.IsVanishingOn
                (⇑(FourierTransform.fourier (MeasureTheory.Lp.toTemperedDistribution f)))
                (Metric.closedBall 0 R)ᶜ →
              ∀ (m : E),
                ∃ g,
                  LineDeriv.lineDerivOp m (MeasureTheory.Lp.toTemperedDistribution f) =
                      MeasureTheory.Lp.toTemperedDistribution g ∧
                    ‖g‖ ≤ C * R * ‖m‖ * ‖f‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Young's convolution inequality](../convolution/youngs-convolution-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_lineDerivOp_eq_and_norm_le_of_isVanishingOn_fourier`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.html#TauCeti.exists_lineDerivOp_eq_and_norm_le_of_isVanishingOn_fourier).

## Other forms

**Bernstein's inequality for the Littlewood–Paley blocks.** Formalized in Tau Ceti as [`TemperedDistribution.exists_littlewoodPaleyBlock_eq_and_norm_le_of_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TemperedDistribution/LittlewoodPaley.html#TemperedDistribution.exists_littlewoodPaleyBlock_eq_and_norm_le_of_le).

```lean
TemperedDistribution.exists_littlewoodPaleyBlock_eq_and_norm_le_of_le.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℂ F] (φ : ContDiffBump 0)
  [CompleteSpace F] {p r : ENNReal} [Fact (1 ≤ p)] [Fact (1 ≤ r)] (hpr : p ≤ r) :
  ∃ C,
    0 ≤ C ∧
      ∀ (j : ℕ) (u : TemperedDistribution E F) (f : ↥(MeasureTheory.Lp F p MeasureTheory.volume)),
        (TemperedDistribution.littlewoodPaleyBlock F φ j) u =
            MeasureTheory.Lp.toTemperedDistribution f →
          ∃ g,
            (TemperedDistribution.littlewoodPaleyBlock F φ j) u =
                MeasureTheory.Lp.toTemperedDistribution g ∧
              ‖g‖ ≤ C * 2 ^ (↑(Module.finrank ℝ E) * (p.toReal⁻¹ - r.toReal⁻¹) * ↑j) * ‖f‖
```

**Bernstein's inequality without derivatives.** Formalized in Tau Ceti as [`TauCeti.exists_eq_and_norm_le_of_isVanishingOn_fourier`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.html#TauCeti.exists_eq_and_norm_le_of_isVanishingOn_fourier).

```lean
TauCeti.exists_eq_and_norm_le_of_isVanishingOn_fourier.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F] {p q : ENNReal}
  [hp : Fact (1 ≤ p)] [Fact (1 ≤ q)] (hpq : p ≤ q) :
  ∃ C,
    0 ≤ C ∧
      ∀ {R : ℝ},
        0 < R →
          ∀ (f : ↥(MeasureTheory.Lp F p MeasureTheory.volume)),
            Distribution.IsVanishingOn
                (⇑(FourierTransform.fourier (MeasureTheory.Lp.toTemperedDistribution f)))
                (Metric.closedBall 0 R)ᶜ →
              ∃ g,
                MeasureTheory.Lp.toTemperedDistribution f =
                    MeasureTheory.Lp.toTemperedDistribution g ∧
                  ‖g‖ ≤ C * R ^ (↑(Module.finrank ℝ E) * (p.toReal⁻¹ - q.toReal⁻¹)) * ‖f‖
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_lineDerivOp_eq_and_norm_le_of_isVanishingOn_fourier`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.html#TauCeti.exists_lineDerivOp_eq_and_norm_le_of_isVanishingOn_fourier)
- [Source of `TauCeti.exists_lineDerivOp_eq_and_norm_le_of_isVanishingOn_fourier` in TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.lean#L244)
