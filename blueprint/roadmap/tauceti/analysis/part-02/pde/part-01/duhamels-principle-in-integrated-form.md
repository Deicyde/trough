---
declaration: theorem
origin: cited
lean: TauCeti.heatDuhamelPotential_eq_integral
statement: formalized
proof: formalized
---

# Duhamel's principle in integrated form

Let `f` be jointly measurable and essentially
bounded on `(0, t) × E`, with `f(s, ·)` `α`-Hölder for almost every `0 < s < t`, where `α > 0`.
Then the Duhamel potential `w` satisfies `w(t, x) = ∫₀ᵗ (Δw(σ, x) + f(σ, x)) dσ`.

```lean
TauCeti.heatDuhamelPotential_eq_integral.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] {f : ℝ → E → F}
  {M t : ℝ} {H α : NNReal} (hf : MeasureTheory.StronglyMeasurable (Function.uncurry f))
  (hfM : ∀ᵐ (s : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo 0 t), ∀ᵐ (y : E), ‖f s y‖ ≤ M)
  (hH : ∀ᵐ (s : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo 0 t), HolderWith H α (f s)) (hα : 0 < α)
  (ht : 0 ≤ t) (x : E) :
  TauCeti.heatDuhamelPotential f t x =
    ∫ (σ : ℝ) in 0..t, Laplacian.laplacian (TauCeti.heatDuhamelPotential f σ) x + f σ x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder bound on the Laplacian of a heat convolution](holder-bound-on-the-laplacian-of-a-heat-convolut.md)
- [Hölder bounds on the derivatives of a heat convolution](holder-bounds-on-the-derivatives-of-a-heat-convo.md)
- [The temporal Hölder estimate of the Cauchy heat potential](../part-02/the-temporal-holder-estimate-of-the-cauchy-heat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.heatDuhamelPotential_eq_integral`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/DuhamelPotential/HeatEquation.html#TauCeti.heatDuhamelPotential_eq_integral).

## Sources

- [Tau Ceti documentation: `TauCeti.heatDuhamelPotential_eq_integral`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HeatKernel/DuhamelPotential/HeatEquation.html#TauCeti.heatDuhamelPotential_eq_integral)
- [Source of `TauCeti.heatDuhamelPotential_eq_integral` in TauCeti/Analysis/PDE/HeatKernel/DuhamelPotential/HeatEquation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/HeatKernel/DuhamelPotential/HeatEquation.lean#L302)
