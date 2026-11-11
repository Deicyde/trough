---
declaration: theorem
origin: cited
lean: TauCeti.W1p.holderOnWith_preciseRepresentative_of_setIntegral_norm_gradient_le, TauCeti.W1p.holderWith_preciseRepresentative_of_setIntegral_norm_gradient_le
statement: formalized
proof: formalized
---

# Morrey's Dirichlet growth theorem

Let `u ∈ W^{1,p}(Ω)` and `α > 0`, and let `K` be a set
of diameter at most `R` whose closed `2R`-thickening lies in `Ω`. If the gradient of `u`
satisfies the growth condition

`∫_{B(x, r)} ‖∇u‖ ≤ M r^(n - 1 + α)` for every `x ∈ K` and `0 < r ≤ 2R`,

then the precise representative of `u` is `α`-Hölder continuous on `K`, with Hölder constant
`2 · 2^α · 2ⁿ / (1 - 2^(-α)) · 2^(n + 1) / ω · M`, where `ω` is the measure of the unit ball.

```lean
TauCeti.W1p.holderOnWith_preciseRepresentative_of_setIntegral_norm_gradient_le.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)] {α : NNReal} (hα : 0 < α)
  {M R : ℝ} (u : ↥(TauCeti.W1p mu Omega p)) {K : Set E} (hKR : ∀ x ∈ K, ∀ y ∈ K, dist x y ≤ R)
  (hK : Metric.cthickening (2 * R) K ⊆ ↑Omega)
  (hgrowth :
    ∀ x ∈ K,
      ∀ (r : ℝ),
        0 < r →
          r ≤ 2 * R →
            ∫ (z : E) in Metric.ball x r, ‖↑↑(TauCeti.W1p.gradient u) z‖ ∂mu ≤
              M * r ^ (↑(Module.finrank ℝ E) - 1 + ↑α)) :
  HolderOnWith
    (2 * 2 ^ ↑α * (2 ^ Module.finrank ℝ E / (1 - 2 ^ (-↑α))) *
        (2 ^ (Module.finrank ℝ E + 1) / mu.real (Metric.ball 0 1) * M)).toNNReal
    α (TauCeti.MeasureTheory.preciseRepresentative mu ↑↑(TauCeti.W1p.value u)) K
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The pointwise Morrey estimate](the-pointwise-morrey-estimate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.holderOnWith_preciseRepresentative_of_setIntegral_norm_gradient_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/DirichletGrowth.html#TauCeti.W1p.holderOnWith_preciseRepresentative_of_setIntegral_norm_gradient_le).

## Other forms

**Morrey's Dirichlet growth theorem on the whole space.** Formalized in Tau Ceti as [`TauCeti.W1p.holderWith_preciseRepresentative_of_setIntegral_norm_gradient_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/DirichletGrowth.html#TauCeti.W1p.holderWith_preciseRepresentative_of_setIntegral_norm_gradient_le).

```lean
TauCeti.W1p.holderWith_preciseRepresentative_of_setIntegral_norm_gradient_le.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure] {p : ENNReal} [Fact (1 ≤ p)]
  {α : NNReal} (hα : 0 < α) {M : ℝ} (u : ↥(TauCeti.W1p mu ⊤ p))
  (hgrowth :
    ∀ (x : E) (r : ℝ),
      0 < r →
        ∫ (z : E) in Metric.ball x r, ‖↑↑(TauCeti.W1p.gradient u) z‖ ∂mu ≤
          M * r ^ (↑(Module.finrank ℝ E) - 1 + ↑α)) :
  HolderWith
    (2 * 2 ^ ↑α * (2 ^ Module.finrank ℝ E / (1 - 2 ^ (-↑α))) *
        (2 ^ (Module.finrank ℝ E + 1) / mu.real (Metric.ball 0 1) * M)).toNNReal
    α (TauCeti.MeasureTheory.preciseRepresentative mu ↑↑(TauCeti.W1p.value u))
```

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.holderOnWith_preciseRepresentative_of_setIntegral_norm_gradient_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/DirichletGrowth.html#TauCeti.W1p.holderOnWith_preciseRepresentative_of_setIntegral_norm_gradient_le)
- [Source of `TauCeti.W1p.holderOnWith_preciseRepresentative_of_setIntegral_norm_gradient_le` in TauCeti/Analysis/Sobolev/W1p/DirichletGrowth.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/W1p/DirichletGrowth.lean#L160)
