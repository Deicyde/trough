---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: IsPicardLindelof.exists_eq_forall_mem_Icc_hasDerivWithinAt
mathlib_file: Mathlib/Analysis/ODE/ExistUnique.lean
---

# Cauchy-Lipschitz Theorem

**Picard-Lindelöf (Cauchy-Lipschitz) theorem**, differential form. This version shows the
existence of a local solution whose initial point `x` may be different from the centre `x₀` of
the closed ball within which the properties of the vector field hold.

```lean
IsPicardLindelof.exists_eq_forall_mem_Icc_hasDerivWithinAt.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E] {f : ℝ → E → E} {tmin tmax : ℝ}
  {t₀ : ↑(Set.Icc tmin tmax)} {x₀ x : E} {a r L K : NNReal} (hf : IsPicardLindelof f t₀ x₀ a r L K)
  (hx : x ∈ Metric.closedBall x₀ ↑r) :
  ∃ α, α ↑t₀ = x ∧ ∀ t ∈ Set.Icc tmin tmax, HasDerivWithinAt α (f t (α t)) (Set.Icc tmin tmax) t
```

## Depends on

- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Continuous linear map](../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Field $\R$ of real numbers](../../ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Metric structure](../../single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)

## Proof depends on

- [$C^k$ function](../../../overview/analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Affine function](../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Compact open topology](../../../overview/topology/general-topology/part-01/compact-open-topology.md)
- [Completion of an abelian topological group](../../../overview/topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Contraction mapping theorem](../../../overview/topology/metric-spaces/contraction-mapping-theorem.md)
- [Derivative at a point](../../single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Derivative of the inverse of a function](../../single-variable-real-analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Differentials (linear tangent functions)](../differential-calculus/differentials-linear-tangent-functions.md)
- [Euclidean affine space](../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Fundamental Theorem of Integral Calculus](../../../hundred-theorems/part-01/fundamental-theorem-of-integral-calculus.md)
- [Holomorphic functions](../../single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Matrix exponential](../../linear-algebra/exponential/matrix-exponential.md)
- [Sequential space](../../../overview/topology/general-topology/part-01/sequential-space.md)
- [The Number of Subsets of a Set](../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)
- [Uniform convergence](../../../overview/topology/uniform-notions/uniform-convergence.md)

## Sources

- [Mathlib documentation: `IsPicardLindelof.exists_eq_forall_mem_Icc_hasDerivWithinAt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/ODE/ExistUnique.html#IsPicardLindelof.exists_eq_forall_mem_Icc_hasDerivWithinAt)
- [Source of `IsPicardLindelof.exists_eq_forall_mem_Icc_hasDerivWithinAt` in Mathlib/Analysis/ODE/ExistUnique.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/ODE/ExistUnique.lean#L54)
- [Mathlib undergraduate list: Multivariable calculus › Differential equations](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L476)
- [1000+ theorems list: Q530152](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L531)
- [1000+ theorems project: Q530152](https://1000-plus.github.io/?length=-1#Q530152)
- [Wikipedia: Picard–Lindelöf theorem](https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem)
- [Wikidata: Q530152](https://www.wikidata.org/wiki/Q530152)
