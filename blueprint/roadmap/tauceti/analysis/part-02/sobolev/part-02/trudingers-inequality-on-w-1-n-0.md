---
declaration: theorem
origin: cited
lean: TauCeti.W1p.setLIntegral_exp_abs_value_div_rpow_le, TauCeti.setLIntegral_exp_norm_div_rpow_le, TauCeti.setLIntegral_exp_norm_div_rpow_le_of_eLpNorm_fderiv_le
statement: formalized
proof: formalized
---

# Trudinger's inequality on `W^{1,n}_0(Ω)`

Let `n ≥ 2` be the dimension and
`ω = μ(B(0, 1))`. Every `u ∈ W^{1,n}_0(Ω)` satisfies

`∫_Ω exp ((|u| / (c ‖∇u‖_{Lⁿ})) ^ (n / (n - 1))) ≤ e (nⁿ + 5) μ(Ω)`,

where `c = (2e) ^ (1 - 1/n) n⁻¹ ω ^ (-1/n)`. So if `μ(Ω) < ∞` and `∇u ≠ 0`, then
`exp (σ |u| ^ (n / (n - 1)))` is integrable on `Ω` for `σ = (c ‖∇u‖_{Lⁿ}) ^ (-n / (n - 1))`,
although `u` need not be bounded. No regularity of `Ω` is assumed.

```lean
TauCeti.W1p.setLIntegral_exp_abs_value_div_rpow_le.{u_1} {E : Type u_1} [MeasurableSpace E]
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E]
  {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens E}
  {p : ENNReal} [Fact (1 ≤ p)] (hp : p = ↑(Module.finrank ℝ E)) (hn : 2 ≤ Module.finrank ℝ E)
  {u : ↥(TauCeti.W1p mu Omega p)} (hu : u ∈ TauCeti.w1p0Submodule mu Omega p) :
  ∫⁻ (x : E) in ↑Omega,
      ENNReal.ofReal
        (Real.exp
          ((|↑↑(TauCeti.W1p.value u) x| /
              ((2 * Real.exp 1) ^ (1 - (↑(Module.finrank ℝ E))⁻¹) * (↑(Module.finrank ℝ E))⁻¹ *
                  mu.real (Metric.ball 0 1) ^ (-(↑(Module.finrank ℝ E))⁻¹) *
                ‖TauCeti.W1p.gradient u‖)) ^
            (↑(Module.finrank ℝ E) / (↑(Module.finrank ℝ E) - 1)))) ∂mu ≤
    ENNReal.ofReal (Real.exp 1 * (↑(Module.finrank ℝ E) ^ Module.finrank ℝ E + 5)) * mu ↑Omega
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The borderline Sobolev inequality on `W^{1,n}_0(Ω)`](../part-01/the-borderline-sobolev-inequality-on-w-1-n-0.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.setLIntegral_exp_abs_value_div_rpow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Trudinger.html#TauCeti.W1p.setLIntegral_exp_abs_value_div_rpow_le).

## Other forms

**Trudinger's inequality for compactly supported functions.** Formalized in Tau Ceti as [`TauCeti.setLIntegral_exp_norm_div_rpow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Trudinger.html#TauCeti.setLIntegral_exp_norm_div_rpow_le).

```lean
TauCeti.setLIntegral_exp_norm_div_rpow_le.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] {μ : MeasureTheory.Measure E}
  [μ.IsAddHaarMeasure] {u : E → F} {Ω : Set E} (hu : ContDiff ℝ 1 u) (h2u : HasCompactSupport u)
  (hsupp : tsupport u ⊆ Ω) (hn : 2 ≤ Module.finrank ℝ E) :
  ∫⁻ (x : E) in Ω,
      ENNReal.ofReal
        (Real.exp
          ((‖u x‖ /
              ((2 * Real.exp 1) ^ (1 - (↑(Module.finrank ℝ E))⁻¹) * (↑(Module.finrank ℝ E))⁻¹ *
                  μ.real (Metric.ball 0 1) ^ (-(↑(Module.finrank ℝ E))⁻¹) *
                (MeasureTheory.eLpNorm (fderiv ℝ u) (↑(Module.finrank ℝ E)) μ).toReal)) ^
            (↑(Module.finrank ℝ E) / (↑(Module.finrank ℝ E) - 1)))) ∂μ ≤
    ENNReal.ofReal (Real.exp 1 * (↑(Module.finrank ℝ E) ^ Module.finrank ℝ E + 5)) * μ Ω
```

**Trudinger's inequality with a bound on the derivative.** Formalized in Tau Ceti as [`TauCeti.setLIntegral_exp_norm_div_rpow_le_of_eLpNorm_fderiv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Trudinger.html#TauCeti.setLIntegral_exp_norm_div_rpow_le_of_eLpNorm_fderiv_le).

```lean
TauCeti.setLIntegral_exp_norm_div_rpow_le_of_eLpNorm_fderiv_le.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {u : E → F} {Ω : Set E} (hu : ContDiff ℝ 1 u)
  (h2u : HasCompactSupport u) (hsupp : tsupport u ⊆ Ω) (hn : 2 ≤ Module.finrank ℝ E) {A : ℝ}
  (hA : 0 < A)
  (hDu : MeasureTheory.eLpNorm (fderiv ℝ u) (↑(Module.finrank ℝ E)) μ ≤ ENNReal.ofReal A) :
  ∫⁻ (x : E) in Ω,
      ENNReal.ofReal
        (Real.exp
          ((‖u x‖ /
              ((2 * Real.exp 1) ^ (1 - (↑(Module.finrank ℝ E))⁻¹) * (↑(Module.finrank ℝ E))⁻¹ *
                  μ.real (Metric.ball 0 1) ^ (-(↑(Module.finrank ℝ E))⁻¹) *
                A)) ^
            (↑(Module.finrank ℝ E) / (↑(Module.finrank ℝ E) - 1)))) ∂μ ≤
    ENNReal.ofReal (Real.exp 1 * (↑(Module.finrank ℝ E) ^ Module.finrank ℝ E + 5)) * μ Ω
```

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.setLIntegral_exp_abs_value_div_rpow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Trudinger.html#TauCeti.W1p.setLIntegral_exp_abs_value_div_rpow_le)
- [Source of `TauCeti.W1p.setLIntegral_exp_abs_value_div_rpow_le` in TauCeti/Analysis/Sobolev/Trudinger.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/Trudinger.lean#L430)
