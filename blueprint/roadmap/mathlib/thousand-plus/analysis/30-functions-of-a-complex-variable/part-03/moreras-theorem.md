---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Complex.isConservativeOn_and_continuousOn_iff_isDifferentiableOn
mathlib_file: Mathlib/Analysis/Complex/HasPrimitives.lean
---

# Morera's theorem

Mathlib states this as `Complex.isConservativeOn_and_continuousOn_iff_isDifferentiableOn`.

```lean
Complex.isConservativeOn_and_continuousOn_iff_isDifferentiableOn.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {f : ℂ → E} [CompleteSpace E] {U : Set ℂ}
  (hU : IsOpen U) : Complex.IsConservativeOn f U ∧ ContinuousOn f U ↔ DifferentiableOn ℂ f U
```

## Depends on

- [Bochner integral](../../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Field $\C$ of complex numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Lebesgue measure (Measures and integral calculus)](../../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Proof depends on

- [Convex subsets](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Derivative at a point](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Differentiable function between normed vector spaces](../../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Differentials (linear tangent functions)](../../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)

## Sources

- [Mathlib documentation: `Complex.isConservativeOn_and_continuousOn_iff_isDifferentiableOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/HasPrimitives.html#Complex.isConservativeOn_and_continuousOn_iff_isDifferentiableOn)
- [Source of `Complex.isConservativeOn_and_continuousOn_iff_isDifferentiableOn` in Mathlib/Analysis/Complex/HasPrimitives.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/HasPrimitives.lean#L281)
- [1000+ theorems list: Q1140119](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1416)
- [1000+ theorems project: Q1140119](https://1000-plus.github.io/?length=-1#Q1140119)
- [Wikipedia: Morera's theorem](https://en.wikipedia.org/wiki/Morera's_theorem)
- [Wikidata: Q1140119](https://www.wikidata.org/wiki/Q1140119)
