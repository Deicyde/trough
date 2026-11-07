---
declaration: theorem
origin: cited
lean: TauCeti.exists_fourierMultiplierCLM_eq_and_norm_le_of_norm_iteratedFDeriv_le
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

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_fourierMultiplierCLM_eq_and_norm_le_of_norm_iteratedFDeriv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/MihlinHormander.html#TauCeti.exists_fourierMultiplierCLM_eq_and_norm_le_of_norm_iteratedFDeriv_le).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_fourierMultiplierCLM_eq_and_norm_le_of_norm_iteratedFDeriv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/MihlinHormander.html#TauCeti.exists_fourierMultiplierCLM_eq_and_norm_le_of_norm_iteratedFDeriv_le)
- [Source of `TauCeti.exists_fourierMultiplierCLM_eq_and_norm_le_of_norm_iteratedFDeriv_le` in TauCeti/Analysis/Fourier/MihlinHormander.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Fourier/MihlinHormander.lean#L351)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PDE/STATUS.md)
