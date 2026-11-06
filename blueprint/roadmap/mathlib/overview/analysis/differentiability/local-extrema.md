# Local extrema

**Fermat's Theorem**: the derivative of a function at a local minimum equals zero.

```lean
IsLocalMin.fderiv_eq_zero.{u} {E : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] {f : E → ℝ}
  {a : E} (h : IsLocalMin f a) : fderiv ℝ f a = 0
```

## Depends on

- [Differentials (linear tangent functions)](../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Normed vector space over a normed field](../normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Cluster point](../../topology/general-topology/part-01/cluster-point.md)
- [Differentiable function between normed vector spaces](differentiable-function-between-normed-vector-sp.md)
- [Dual of a normed space](../normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Order topology](../../topology/topological-algebra/order-topology.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `IsLocalMin.fderiv_eq_zero`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/LocalExtr/Basic.html#IsLocalMin.fderiv_eq_zero)
- [Source of `IsLocalMin.fderiv_eq_zero` in Mathlib/Analysis/Calculus/LocalExtr/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/LocalExtr/Basic.lean#L180)
- [Mathlib overview: Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L315)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L470)
