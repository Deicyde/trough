---
declaration: theorem
origin: cited
lean: TauCeti.exists_fourierMultiplierCLM_eq_and_norm_le_of_norm_iteratedFDeriv_le, TauCeti.exists_eLpNorm_fourierMultiplierCLM_le_of_norm_iteratedFDeriv_le, SchwartzMap.exists_eLpNorm_fourierMultiplierCLM_le_of_norm_iteratedFDeriv_le, TauCeti.exists_eLpNorm_fourierInv_apply_le_of_norm_iteratedFDeriv_le
statement: formalized
proof: formalized
---

# The Mihlin–Hörmander multiplier theorem on `Lᵖ`

Let `V` be a real inner product space of
finite dimension `n ≥ 1`, let `2N > n` and `1 < p < ∞`. There is a constant `C` such that for
every symbol `m` of temperate growth satisfying Mihlin's condition of order `N` with constant `A`,

`‖D^k m ξ‖ ≤ A / ‖ξ‖ ^ k` for every `k ≤ N` and every `ξ ≠ 0`,

the Fourier multiplier `𝓕⁻ (m • 𝓕 f)` of the tempered distribution of any `f ∈ Lᵖ(V, F)` is an
`Lᵖ` function `g` with `‖g‖_p ≤ C A ‖f‖_p`.

```lean
TauCeti.exists_fourierMultiplierCLM_eq_and_norm_le_of_norm_iteratedFDeriv_le.{u_1, u_2}
  {V : Type u_1} {F : Type u_2} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [NormedAddCommGroup F] [InnerProductSpace ℂ F] [FiniteDimensional ℝ V] [MeasurableSpace V]
  [BorelSpace V] [CompleteSpace F] [Nontrivial V] {N : ℕ} (hN : Module.finrank ℝ V < 2 * N)
  {p : ENNReal} [Fact (1 ≤ p)] (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ {m : V → ℂ},
      Function.HasTemperateGrowth m →
        ∀ {A : NNReal},
          (∀ k ≤ N, ∀ (ξ : V), ξ ≠ 0 → ‖iteratedFDeriv ℝ k m ξ‖ ≤ ↑A / ‖ξ‖ ^ k) →
            ∀ (f : ↥(MeasureTheory.Lp F p MeasureTheory.volume)),
              ∃ g,
                (TemperedDistribution.fourierMultiplierCLM F m)
                      (MeasureTheory.Lp.toTemperedDistribution f) =
                    MeasureTheory.Lp.toTemperedDistribution g ∧
                  ‖g‖ ≤ ↑C * ↑A * ‖f‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Calderón–Zygmund theorem](../../../measure-theory/integral/part-01/the-calderon-zygmund-theorem.md)
- [Hölder's inequality for disjoint pieces](../../../measure-theory/function/part-01/holders-inequality-for-disjoint-pieces.md)
- [Plancherel bound for Fourier multipliers](../../part-03/fourier/part-01/plancherel-bound-for-fourier-multipliers.md)
- [Plancherel's theorem for the inverse Fourier transform of Schwartz functions](../../part-03/distribution/plancherels-theorem-for-the-inverse-fourier-tran.md)
- [The weighted Plancherel bound](../../part-03/distribution/the-weighted-plancherel-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_fourierMultiplierCLM_eq_and_norm_le_of_norm_iteratedFDeriv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/MihlinHormander.html#TauCeti.exists_fourierMultiplierCLM_eq_and_norm_le_of_norm_iteratedFDeriv_le).

## Other forms

**The Mihlin–Hörmander multiplier theorem.** Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_fourierMultiplierCLM_le_of_norm_iteratedFDeriv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/MihlinHormander.html#TauCeti.exists_eLpNorm_fourierMultiplierCLM_le_of_norm_iteratedFDeriv_le).

```lean
TauCeti.exists_eLpNorm_fourierMultiplierCLM_le_of_norm_iteratedFDeriv_le.{u_1, u_2} {V : Type u_1}
  {F : Type u_2} [NormedAddCommGroup V] [InnerProductSpace ℝ V] [NormedAddCommGroup F]
  [InnerProductSpace ℂ F] [FiniteDimensional ℝ V] [MeasurableSpace V] [BorelSpace V]
  [CompleteSpace F] [Nontrivial V] {N : ℕ} (hN : Module.finrank ℝ V < 2 * N) {p : ENNReal}
  (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ {m : V → ℂ},
      ContDiffOn ℝ (↑⊤) m {0}ᶜ →
        ∀ {A : NNReal},
          (∀ k ≤ N, ∀ (ξ : V), ξ ≠ 0 → ‖iteratedFDeriv ℝ k m ξ‖ ≤ ↑A / ‖ξ‖ ^ k) →
            ∀ (m' : ↥(MeasureTheory.Lp ℂ ⊤ MeasureTheory.volume)),
              ↑↑m' =ᵐ[MeasureTheory.volume] m →
                ∀ (f : ↥(MeasureTheory.Lp F 2 MeasureTheory.volume)),
                  MeasureTheory.eLpNorm (↑↑((MeasureTheory.Lp.fourierMultiplierCLM F m') f)) p
                      MeasureTheory.volume ≤
                    ↑C * ↑A * MeasureTheory.eLpNorm (↑↑f) p MeasureTheory.volume
```

**The Mihlin–Hörmander multiplier theorem on Schwartz functions.** Formalized in Tau Ceti as [`SchwartzMap.exists_eLpNorm_fourierMultiplierCLM_le_of_norm_iteratedFDeriv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/MihlinHormander.html#SchwartzMap.exists_eLpNorm_fourierMultiplierCLM_le_of_norm_iteratedFDeriv_le).

```lean
SchwartzMap.exists_eLpNorm_fourierMultiplierCLM_le_of_norm_iteratedFDeriv_le.{u_1, u_2}
  {V : Type u_1} {F : Type u_2} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [NormedAddCommGroup F] [InnerProductSpace ℂ F] [FiniteDimensional ℝ V] [MeasurableSpace V]
  [BorelSpace V] [CompleteSpace F] [Nontrivial V] {N : ℕ} (hN : Module.finrank ℝ V < 2 * N)
  {p : ENNReal} (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ {m : V → ℂ},
      Function.HasTemperateGrowth m →
        ∀ {A : NNReal},
          (∀ k ≤ N, ∀ (ξ : V), ξ ≠ 0 → ‖iteratedFDeriv ℝ k m ξ‖ ≤ ↑A / ‖ξ‖ ^ k) →
            ∀ (φ : SchwartzMap V F),
              MeasureTheory.eLpNorm (⇑((SchwartzMap.fourierMultiplierCLM F m) φ)) p
                  MeasureTheory.volume ≤
                ↑C * ↑A * MeasureTheory.eLpNorm (⇑φ) p MeasureTheory.volume
```

**The Mihlin–Hörmander theorem for operator-valued symbols.** Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_fourierInv_apply_le_of_norm_iteratedFDeriv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/MihlinHormander.html#TauCeti.exists_eLpNorm_fourierInv_apply_le_of_norm_iteratedFDeriv_le).

```lean
TauCeti.exists_eLpNorm_fourierInv_apply_le_of_norm_iteratedFDeriv_le.{u_1, u_3, u_4} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [MeasurableSpace V]
  [BorelSpace V] {G : Type u_3} {H : Type u_4} [NormedAddCommGroup G] [NormedSpace ℂ G]
  [FiniteDimensional ℂ G] [NormedAddCommGroup H] [NormedSpace ℂ H] [FiniteDimensional ℂ H]
  [Nontrivial V] {N : ℕ} (hN : Module.finrank ℝ V < 2 * N) {p : ENNReal} (hp : 1 < p)
  (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ {b : V → G →L[ℂ] H},
      Function.HasTemperateGrowth b →
        ∀ {A : NNReal},
          (∀ k ≤ N, ∀ (ξ : V), ξ ≠ 0 → ‖iteratedFDeriv ℝ k b ξ‖ ≤ ↑A / ‖ξ‖ ^ k) →
            ∀ (u : SchwartzMap V G),
              MeasureTheory.eLpNorm
                  (FourierTransformInv.fourierInv fun ξ => (b ξ) ((FourierTransform.fourier u) ξ)) p
                  MeasureTheory.volume ≤
                ↑C * ↑A * MeasureTheory.eLpNorm (⇑u) p MeasureTheory.volume
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_fourierMultiplierCLM_eq_and_norm_le_of_norm_iteratedFDeriv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/MihlinHormander.html#TauCeti.exists_fourierMultiplierCLM_eq_and_norm_le_of_norm_iteratedFDeriv_le)
- [Source of `TauCeti.exists_fourierMultiplierCLM_eq_and_norm_le_of_norm_iteratedFDeriv_le` in TauCeti/Analysis/Fourier/MihlinHormander.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Fourier/MihlinHormander.lean#L361)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PDE/STATUS.md)
