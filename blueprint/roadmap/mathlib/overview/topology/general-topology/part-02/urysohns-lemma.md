---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: exists_continuous_zero_one_of_isClosed
mathlib_file: Mathlib/Topology/UrysohnsLemma.lean
---

# Urysohn's lemma

Urysohn's lemma: if `s` and `t` are two disjoint closed sets in a normal topological space `X`,
then there exists a continuous function `f : X → ℝ` such that

* `f` equals zero on `s`;
* `f` equals one on `t`;
* `0 ≤ f x ≤ 1` for all `x`.

```lean
exists_continuous_zero_one_of_isClosed.{u_1} {X : Type u_1} [TopologicalSpace X] [NormalSpace X]
  {s t : Set X} (hs : IsClosed s) (ht : IsClosed t) (hd : Disjoint s t) :
  ∃ f, Set.EqOn (⇑f) 0 s ∧ Set.EqOn (⇑f) 1 t ∧ ∀ (x : X), f x ∈ Set.Icc 0 1
```

## Depends on

- [Bornology](../../../analysis/topological-vector-spaces/bornology.md)
- [Continuous function](../part-01/continuous-function.md)
- [Order](../../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Uniform space](../../uniform-notions/uniform-space.md)

## Proof depends on

- [Affine function](../../../geometry/affine-and-euclidean-geometry/affine-function.md)
- [Ball](../../metric-spaces/ball.md)
- [Closure](../part-01/closure.md)
- [Cluster point](../part-01/cluster-point.md)
- [Euclidean affine space](../../../geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Field $\R$ of real numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Finite set](../../../data-structures/sets/finite-set.md)
- [Group](../../../general-algebra/group-theory/part-01/group.md)
- [Hausdorff space](../part-01/hausdorff-space.md)
- [Homeomorphisms](../../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Invertible elements](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Lipschitz continuity](../../metric-spaces/lipschitz-continuity.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Order topology](../../topological-algebra/order-topology.md)
- [Product of vector spaces](../../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological module](../../topological-algebra/topological-module.md)
- [Topological ring](../../topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `exists_continuous_zero_one_of_isClosed`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/UrysohnsLemma.html#exists_continuous_zero_one_of_isClosed)
- [Source of `exists_continuous_zero_one_of_isClosed` in Mathlib/Topology/UrysohnsLemma.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/UrysohnsLemma.lean#L314)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L235)
