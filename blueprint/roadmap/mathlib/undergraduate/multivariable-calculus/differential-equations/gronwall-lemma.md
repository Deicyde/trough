---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: norm_le_gronwallBound_of_norm_deriv_right_le
mathlib_file: Mathlib/Analysis/ODE/Gronwall.lean
---

# Grönwall lemma

A Grönwall-like inequality: if `f : ℝ → E` is continuous on `[a, b]`, has right derivative
`f' x` at every point `x ∈ [a, b)`, and satisfies the inequalities `‖f a‖ ≤ δ`,
`∀ x ∈ [a, b), ‖f' x‖ ≤ K * ‖f x‖ + ε`, then `‖f x‖` is bounded by `gronwallBound δ K ε (x - a)`
on `[a, b]`.

```lean
norm_le_gronwallBound_of_norm_deriv_right_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {f f' : ℝ → E} {δ K ε a b : ℝ} (hf : ContinuousOn f (Set.Icc a b))
  (hf' : ∀ x ∈ Set.Ico a b, HasDerivWithinAt f (f' x) (Set.Ici x) x) (ha : ‖f a‖ ≤ δ)
  (bound : ∀ x ∈ Set.Ico a b, ‖f' x‖ ≤ K * ‖f x‖ + ε) (x : ℝ) :
  x ∈ Set.Icc a b → ‖f x‖ ≤ gronwallBound δ K ε (x - a)
```

## Depends on

- [Continuous linear map](../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Exponential](../../../overview/analysis/special-functions/exponential.md)
- [Metric structure](../../single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness of R](../../single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Derivative at a point](../../single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Derivative of a composition of functions](../../../overview/analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Euclidean affine space](../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Field $\C$ of complex numbers](../../ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Norm of a continuous linear map](../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [The Binomial Theorem](../../../hundred-theorems/part-03/the-binomial-theorem.md)
- [Topology on a normed vector space](../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)

## Sources

- [Mathlib documentation: `norm_le_gronwallBound_of_norm_deriv_right_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/ODE/Gronwall.html#norm_le_gronwallBound_of_norm_deriv_right_le)
- [Source of `norm_le_gronwallBound_of_norm_deriv_right_le` in Mathlib/Analysis/ODE/Gronwall.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/ODE/Gronwall.lean#L130)
- [Mathlib undergraduate list: Multivariable calculus › Differential equations](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L478)
