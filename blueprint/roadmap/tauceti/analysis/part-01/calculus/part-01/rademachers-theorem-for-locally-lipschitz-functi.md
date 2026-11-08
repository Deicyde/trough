---
declaration: theorem
origin: cited
lean: LocallyLipschitzOn.ae_differentiableWithinAt_of_mem, LocallyLipschitzOn.ae_differentiableAt_of_mem, TauCeti.ae_eventually_ne_top_and_differentiableAt_toReal
statement: formalized
proof: formalized
---

# Rademacher's theorem for locally Lipschitz functions

a function between
finite-dimensional real normed spaces which is locally Lipschitz on a set is differentiable
within that set at almost every point of it.

```lean
LocallyLipschitzOn.ae_differentiableWithinAt_of_mem.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {s : Set E}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {f : E → F}
  (hf : LocallyLipschitzOn s f) : ∀ᵐ (x : E) ∂μ, x ∈ s → DifferentiableWithinAt ℝ f s x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LocallyLipschitzOn.ae_differentiableWithinAt_of_mem`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Rademacher.html#LocallyLipschitzOn.ae_differentiableWithinAt_of_mem).

## Other forms

**Rademacher's theorem for locally Lipschitz functions on an open set.** Formalized in Tau Ceti as [`LocallyLipschitzOn.ae_differentiableAt_of_mem`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Rademacher.html#LocallyLipschitzOn.ae_differentiableAt_of_mem).

```lean
LocallyLipschitzOn.ae_differentiableAt_of_mem.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {s : Set E}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {f : E → F}
  (hf : LocallyLipschitzOn s f) (hs : IsOpen s) : ∀ᵐ (x : E) ∂μ, x ∈ s → DifferentiableAt ℝ f x
```

**Rademacher's theorem for extended-real convex functions.** Formalized in Tau Ceti as [`TauCeti.ae_eventually_ne_top_and_differentiableAt_toReal`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Differentiability.html#TauCeti.ae_eventually_ne_top_and_differentiableAt_toReal).

```lean
TauCeti.ae_eventually_ne_top_and_differentiableAt_toReal.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {f : E → EReal} [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] (hf : Convex ℝ {p | f p.1 ≤ ↑p.2})
  (hbot : ∀ (x : E), f x ≠ ⊥) :
  ∀ᵐ (x : E) ∂μ,
    f x ≠ ⊤ → (∀ᶠ (x' : E) in nhds x, f x' ≠ ⊤) ∧ DifferentiableAt ℝ (fun x' => (f x').toReal) x
```

## Sources

- [Tau Ceti documentation: `LocallyLipschitzOn.ae_differentiableWithinAt_of_mem`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Rademacher.html#LocallyLipschitzOn.ae_differentiableWithinAt_of_mem)
- [Source of `LocallyLipschitzOn.ae_differentiableWithinAt_of_mem` in TauCeti/Analysis/Calculus/Rademacher.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/Rademacher.lean#L58)
