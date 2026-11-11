---
declaration: theorem
origin: cited
lean: TauCeti.W1p.eLpNorm_value_le_mul_measure_rpow_mul_enorm_gradient, TauCeti.eLpNorm_le_mul_measure_rpow_mul_eLpNorm_fderiv
statement: formalized
proof: formalized
---

# The borderline Sobolev inequality on `W^{1,n}_0(Ω)`

Let `n` be the dimension and
`ω = μ(B(0, 1))`. If `Ω` has finite measure, then every `u ∈ W^{1,n}_0(Ω)` lies in `L^q(Ω)` for
every finite `q ≥ n`, with

`‖u‖_{L^q} ≤ n⁻¹ ω ^ (-1/n) (q (1 - 1/n) + 1) ^ (1 - 1/n + 1/q) μ(Ω) ^ (1/q) ‖∇u‖_{Lⁿ}`.

No regularity of `Ω` is assumed.

```lean
TauCeti.W1p.eLpNorm_value_le_mul_measure_rpow_mul_enorm_gradient.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)] (hp : p = ↑(Module.finrank ℝ E))
  (hOmega : mu ↑Omega ≠ ⊤) {q : NNReal} (hq : ↑(Module.finrank ℝ E) ≤ q)
  {u : ↥(TauCeti.W1p mu Omega p)} (hu : u ∈ TauCeti.w1p0Submodule mu Omega p) :
  MeasureTheory.eLpNorm (↑↑(TauCeti.W1p.value u)) (↑q) (mu.restrict ↑Omega) ≤
    ENNReal.ofReal
          ((↑(Module.finrank ℝ E))⁻¹ * mu.real (Metric.ball 0 1) ^ (-(↑(Module.finrank ℝ E))⁻¹) *
            (↑q * (1 - (↑(Module.finrank ℝ E))⁻¹) + 1) ^ (1 - (↑(Module.finrank ℝ E))⁻¹ + (↑q)⁻¹)) *
        mu ↑Omega ^ (↑q)⁻¹ *
      ‖TauCeti.W1p.gradient u‖ₑ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Sobolev inequality on `W^{1,p}_0` of a ball](../part-02/the-sobolev-inequality-on-w-1-p-0-of-a-ball.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.eLpNorm_value_le_mul_measure_rpow_mul_enorm_gradient`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Trudinger.html#TauCeti.W1p.eLpNorm_value_le_mul_measure_rpow_mul_enorm_gradient).

## Other forms

**The borderline Sobolev inequality for compactly supported functions.** Formalized in Tau Ceti as [`TauCeti.eLpNorm_le_mul_measure_rpow_mul_eLpNorm_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Trudinger.html#TauCeti.eLpNorm_le_mul_measure_rpow_mul_eLpNorm_fderiv).

```lean
TauCeti.eLpNorm_le_mul_measure_rpow_mul_eLpNorm_fderiv.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [Nontrivial E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {u : E → F} {Ω : Set E} (hu : ContDiff ℝ 1 u)
  (h2u : HasCompactSupport u) (hsupp : tsupport u ⊆ Ω) {q : NNReal}
  (hq : ↑(Module.finrank ℝ E) ≤ q) :
  MeasureTheory.eLpNorm u (↑q) μ ≤
    ENNReal.ofReal
          ((↑(Module.finrank ℝ E))⁻¹ * μ.real (Metric.ball 0 1) ^ (-(↑(Module.finrank ℝ E))⁻¹) *
            (↑q * (1 - (↑(Module.finrank ℝ E))⁻¹) + 1) ^ (1 - (↑(Module.finrank ℝ E))⁻¹ + (↑q)⁻¹)) *
        μ Ω ^ (↑q)⁻¹ *
      MeasureTheory.eLpNorm (fderiv ℝ u) (↑(Module.finrank ℝ E)) μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.eLpNorm_value_le_mul_measure_rpow_mul_enorm_gradient`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Trudinger.html#TauCeti.W1p.eLpNorm_value_le_mul_measure_rpow_mul_enorm_gradient)
- [Source of `TauCeti.W1p.eLpNorm_value_le_mul_measure_rpow_mul_enorm_gradient` in TauCeti/Analysis/Sobolev/Trudinger.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/Trudinger.lean#L403)
