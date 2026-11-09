---
declaration: theorem
origin: cited
lean: TauCeti.W1p.dist_preciseRepresentative_le_of_setIntegral_norm_gradient_le
statement: formalized
proof: formalized
---

# The pointwise Morrey estimate

Let `u ∈ W^{1,p}(Ω)`, `α > 0`, `d = dist x y`, and
suppose that `closedBall x (2 d) ⊆ Ω` and that the gradient of `u` satisfies the growth condition
`∫_{B(z, r)} ‖∇u‖ ≤ M r^(n - 1 + α)` for `z = x`, `0 < r ≤ 2 d` and for `z = y`, `0 < r ≤ d`.
Then the precise representative `u*` of `u` satisfies

`|u*(x) - u*(y)| ≤ 2 · 2^α · 2ⁿ / (1 - 2^(-α)) · 2^(n + 1) / ω · M d^α`,

where `ω` is the measure of the unit ball.

```lean
TauCeti.W1p.dist_preciseRepresentative_le_of_setIntegral_norm_gradient_le.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)] {α M : ℝ} (hα : 0 < α)
  (u : ↥(TauCeti.W1p mu Omega p)) {x y : E} (hxy : Metric.closedBall x (2 * dist x y) ⊆ ↑Omega)
  (hx :
    ∀ (r : ℝ),
      0 < r →
        r ≤ 2 * dist x y →
          ∫ (z : E) in Metric.ball x r, ‖↑↑(TauCeti.W1p.gradient u) z‖ ∂mu ≤
            M * r ^ (↑(Module.finrank ℝ E) - 1 + α))
  (hy :
    ∀ (r : ℝ),
      0 < r →
        r ≤ dist x y →
          ∫ (z : E) in Metric.ball y r, ‖↑↑(TauCeti.W1p.gradient u) z‖ ∂mu ≤
            M * r ^ (↑(Module.finrank ℝ E) - 1 + α)) :
  dist (TauCeti.MeasureTheory.preciseRepresentative mu (↑↑(TauCeti.W1p.value u)) x)
      (TauCeti.MeasureTheory.preciseRepresentative mu (↑↑(TauCeti.W1p.value u)) y) ≤
    2 * 2 ^ α * (2 ^ Module.finrank ℝ E / (1 - 2 ^ (-α))) *
      (2 ^ (Module.finrank ℝ E + 1) / mu.real (Metric.ball 0 1) * M * dist x y ^ α)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The local Campanato estimate](../../../../measure-theory/function/the-local-campanato-estimate.md)
- [The Poincaré inequality on a ball](the-poincare-inequality-on-a-ball.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.dist_preciseRepresentative_le_of_setIntegral_norm_gradient_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/DirichletGrowth.html#TauCeti.W1p.dist_preciseRepresentative_le_of_setIntegral_norm_gradient_le).

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.dist_preciseRepresentative_le_of_setIntegral_norm_gradient_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/W1p/DirichletGrowth.html#TauCeti.W1p.dist_preciseRepresentative_le_of_setIntegral_norm_gradient_le)
- [Source of `TauCeti.W1p.dist_preciseRepresentative_le_of_setIntegral_norm_gradient_le` in TauCeti/Analysis/Sobolev/W1p/DirichletGrowth.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/W1p/DirichletGrowth.lean#L123)
