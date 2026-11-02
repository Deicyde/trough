---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: IntervalIntegrable.ae_hasDerivAt_integral
mathlib_file: Mathlib/MeasureTheory/Integral/IntervalIntegral/LebesgueDifferentiationThm.lean
---

# Differentiability of integrals with respect to parameters

The (local) interval version of the *Lebesgue Differentiation Theorem*: if `f : ℝ → E` is
interval integrable on `a..b`, then for almost every `x ∈ uIcc a b`, for any `c ∈ uIcc a b`, the
derivative of `∫ (t : ℝ) in c..x, f t` at `x` is equal to `f x`.

```lean
IntervalIntegrable.ae_hasDerivAt_integral.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [CompleteSpace E] {f : ℝ → E} {a b : ℝ}
  (hf : IntervalIntegrable f MeasureTheory.volume a b) :
  ∀ᵐ (x : ℝ),
    x ∈ Set.uIcc a b → ∀ c ∈ Set.uIcc a b, HasDerivAt (fun x => ∫ (t : ℝ) in c..x, f t) (f x) x
```

## Depends on

- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Derivative at a point](../../single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Lebesgue measure (Measures and integral calculus)](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Proof depends on

- [Affine space](../../../overview/geometry/affine-and-euclidean-geometry/affine-space.md)
- [Measurable function](../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)

## Sources

- [Mathlib documentation: `IntervalIntegrable.ae_hasDerivAt_integral`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/IntervalIntegral/LebesgueDifferentiationThm.html#IntervalIntegrable.ae_hasDerivAt_integral)
- [Source of `IntervalIntegrable.ae_hasDerivAt_integral` in Mathlib/MeasureTheory/Integral/IntervalIntegral/LebesgueDifferentiationThm.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/IntervalIntegral/LebesgueDifferentiationThm.lean#L64)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L520)
