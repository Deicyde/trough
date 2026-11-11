---
declaration: theorem
origin: cited
lean: LocallyLipschitzOn.ae_differentiableWithinAt_of_mem, LocallyLipschitzOn.ae_differentiableAt_of_mem
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

## Sources

- [Tau Ceti documentation: `LocallyLipschitzOn.ae_differentiableWithinAt_of_mem`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Rademacher.html#LocallyLipschitzOn.ae_differentiableWithinAt_of_mem)
- [Source of `LocallyLipschitzOn.ae_differentiableWithinAt_of_mem` in TauCeti/Analysis/Calculus/Rademacher.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Rademacher.lean#L58)
