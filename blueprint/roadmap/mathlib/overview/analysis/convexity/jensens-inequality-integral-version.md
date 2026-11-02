---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ConvexOn.map_integral_le
mathlib_file: Mathlib/Analysis/Convex/Integral.lean
---

# Jensen's inequality (integral version)

**Jensen's inequality**: if a function `g : E → ℝ` is convex and continuous on a convex closed
set `s`, `μ` is a probability measure on `α`, and `f : α → E` is a function sending `μ`-a.e.  points
to `s`, then the value of `g` at the expected value of `f` is less than or equal to the expected
value of `g ∘ f` provided that both `f` and `g ∘ f` are integrable. See also
`ConvexOn.map_centerMass_le` for a finite sum version of this lemma.

```lean
ConvexOn.map_integral_le.{u_1, u_2} {α : Type u_1} {E : Type u_2} {m0 : MeasurableSpace α}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E] {μ : MeasureTheory.Measure α}
  {s : Set E} {f : α → E} {g : E → ℝ} [MeasureTheory.IsProbabilityMeasure μ] (hg : ConvexOn ℝ s g)
  (hgc : ContinuousOn g s) (hsc : IsClosed s) (hfs : ∀ᵐ (x : α) ∂μ, f x ∈ s)
  (hfi : MeasureTheory.Integrable f μ) (hgi : MeasureTheory.Integrable (g ∘ f) μ) :
  g (∫ (x : α), f x ∂μ) ≤ ∫ (x : α), g (f x) ∂μ
```

## Depends on

- [Bochner integral](../measures-and-integral-calculus/part-01/bochner-integral.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Convex function](convex-function.md)
- [Inner product space, over $R$ or $C$](../hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Probability measure](../../probability-theory/definitions-in-probability-theory/probability-measure.md)

## Proof depends on

- [Affine space](../../geometry/affine-and-euclidean-geometry/affine-space.md)
- [Approximation by step functions](../../../undergraduate/measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)
- [Arithmetic Mean/Geometric Mean](../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Characteristic p](../../general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../topology/general-topology/part-01/closed-map.md)
- [Fatou's lemma](../measures-and-integral-calculus/part-01/fatous-lemma.md)
- [Monotone convergence theorem](../measures-and-integral-calculus/part-01/monotone-convergence-theorem.md)
- [Pointwise convergence](../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)

## Sources

- [Mathlib documentation: `ConvexOn.map_integral_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Integral.html#ConvexOn.map_integral_le)
- [Source of `ConvexOn.map_integral_le` in Mathlib/Analysis/Convex/Integral.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Convex/Integral.lean#L191)
- [Mathlib overview: Analysis › Convexity](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L324)
