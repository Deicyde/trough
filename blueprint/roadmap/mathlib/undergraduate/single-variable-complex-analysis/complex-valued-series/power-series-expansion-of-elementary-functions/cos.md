---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Complex.hasSum_cos
mathlib_file: Mathlib/Analysis/SpecialFunctions/Trigonometric/Series.lean
---

# Cos (power series expansion of elementary functions)

The power series expansion of `Complex.cos`.

```lean
Complex.hasSum_cos (z : ℂ) :
  HasSum (fun n => (-1) ^ n * z ^ (2 * n) / ↑(2 * n).factorial) (Complex.cos z)
```

## Depends on

- [Cos (extension of trigonometric functions to the complex plane)](../extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Field $\C$ of complex numbers](../../../ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Infinite sum](../../../../overview/topology/topological-algebra/infinite-sum.md)
- [Metric space](../../../../overview/topology/metric-spaces/metric-space.md)

## Proof depends on

- [Absolutely convergent series in Banach spaces](../../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Closure](../../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../topology/topology-and-metric-spaces/homeomorphisms.md)
- [Linear map](../../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Matrix exponential](../../../linear-algebra/exponential/matrix-exponential.md)
- [Open map](../../../../overview/topology/general-topology/part-01/open-map.md)
- [Product of vector spaces](../../../linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Radius of convergence](../radius-of-convergence.md)
- [Squeeze theorem](../../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Topological module](../../../../overview/topology/topological-algebra/topological-module.md)
- [Topology of a metric space](../../../topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `Complex.hasSum_cos`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Trigonometric/Series.html#Complex.hasSum_cos)
- [Source of `Complex.hasSum_cos` in Mathlib/Analysis/SpecialFunctions/Trigonometric/Series.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/SpecialFunctions/Trigonometric/Series.lean#L70)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Complex-valued series › power series expansion of elementary functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L379)
