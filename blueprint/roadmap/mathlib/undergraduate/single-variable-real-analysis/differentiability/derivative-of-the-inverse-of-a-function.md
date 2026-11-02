---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: HasStrictDerivAt.of_local_left_inverse
mathlib_file: Mathlib/Analysis/Calculus/Deriv/Inverse.lean
---

# Derivative of the inverse of a function (Single Variable Real Analysis)

If `f (g y) = y` for `y` in some neighborhood of `a`, `g` is continuous at `a`, and `f` has an
invertible derivative `f'` at `g a` in the strict sense, then `g` has the derivative `f'⁻¹` at `a`
in the strict sense.

This is one of the easy parts of the inverse function theorem: it assumes that we already have an
inverse function.

```lean
HasStrictDerivAt.of_local_left_inverse.{u} {𝕜 : Type u} [NontriviallyNormedField 𝕜] {f g : 𝕜 → 𝕜}
  {f' a : 𝕜} (hg : ContinuousAt g a) (hf : HasStrictDerivAt f f' (g a)) (hf' : f' ≠ 0)
  (hfg : ∀ᶠ (y : 𝕜) in nhds a, f (g y) = y) : HasStrictDerivAt g f'⁻¹ a
```

## Depends on

- [Continuous linear map](../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)

## Proof depends on

- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Homeomorphisms](../../topology/topology-and-metric-spaces/homeomorphisms.md)
- [Lipschitz continuity](../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Metric structure](../topology-of-r/metric-structure.md)
- [Open map](../../../overview/topology/general-topology/part-01/open-map.md)
- [Product of vector spaces](../../linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `HasStrictDerivAt.of_local_left_inverse`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Deriv/Inverse.html#HasStrictDerivAt.of_local_left_inverse)
- [Source of `HasStrictDerivAt.of_local_left_inverse` in Mathlib/Analysis/Calculus/Deriv/Inverse.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Deriv/Inverse.lean#L55)
- [Mathlib undergraduate list: Single Variable Real Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L317)
