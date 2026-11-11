---
declaration: theorem
origin: cited
lean: TauCeti.exists_eq_and_norm_le_of_isVanishingOn_fourier, TemperedDistribution.exists_littlewoodPaleyBlock_eq_and_norm_le_of_le
statement: formalized
proof: formalized
---

# Bernstein's inequality without derivatives

For `1 ≤ p ≤ q ≤ ∞` there is a constant `C`,
depending only on `E`, `p` and `q`, such that an `Lᵖ` function `f` whose Fourier transform vanishes
outside the closed ball of radius `R > 0` is an `Lᵠ` function `g`, with
`‖g‖_q ≤ C R ^ (n (1/p - 1/q)) ‖f‖_p`, where `n` is the dimension of `E` and `1/∞ = 0`.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Young's convolution inequality](../convolution/youngs-convolution-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_eq_and_norm_le_of_isVanishingOn_fourier`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.html#TauCeti.exists_eq_and_norm_le_of_isVanishingOn_fourier).

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

## Sources

- [Tau Ceti documentation: `TauCeti.exists_eq_and_norm_le_of_isVanishingOn_fourier`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.html#TauCeti.exists_eq_and_norm_le_of_isVanishingOn_fourier)
- [Source of `TauCeti.exists_eq_and_norm_le_of_isVanishingOn_fourier` in TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/TemperedDistribution/Bernstein.lean#L148)
