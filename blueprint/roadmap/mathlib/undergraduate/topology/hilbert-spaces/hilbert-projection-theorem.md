---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: exists_norm_eq_iInf_of_complete_convex
mathlib_file: Mathlib/Analysis/InnerProductSpace/Projection/Minimal.lean
---

# Hilbert projection theorem

**Existence of minimizers**, aka the **Hilbert projection theorem**.

Let `u` be a point in a real inner product space, and let `K` be a nonempty complete convex subset.
Then there exists a \(unique\) `v` in `K` that minimizes the distance `‖u - v‖` to `u`.

```lean
exists_norm_eq_iInf_of_complete_convex.{u_3} {F : Type u_3} [NormedAddCommGroup F]
  [InnerProductSpace ℝ F] {K : Set F} (ne : K.Nonempty) (h₁ : IsComplete K) (h₂ : Convex ℝ K)
  (u : F) : ∃ v ∈ K, ‖u - v‖ = ⨅ w, ‖u - ↑w‖
```

## Depends on

- [Completeness of R](../../single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Convex subsets](../../affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)

## Proof depends on

- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Continuity of monotone functions](../../single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of-r/continuity-of-monotone-functions.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../topology-and-metric-spaces/homeomorphisms.md)
- [Limits of sequences](../topology-and-metric-spaces/limits-of-sequences.md)
- [Lipschitz continuity](../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `exists_norm_eq_iInf_of_complete_convex`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Projection/Minimal.html#exists_norm_eq_iInf_of_complete_convex)
- [Source of `exists_norm_eq_iInf_of_complete_convex` in Mathlib/Analysis/InnerProductSpace/Projection/Minimal.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/Projection/Minimal.lean#L36)
- [Mathlib undergraduate list: Topology › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L438)
- [1000+ theorems list: Q3527215](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2543)
- [1000+ theorems project: Q3527215](https://1000-plus.github.io/?length=-1#Q3527215)
- [Wikipedia: Hilbert projection theorem](https://en.wikipedia.org/wiki/Hilbert_projection_theorem)
- [Wikidata: Q3527215](https://www.wikidata.org/wiki/Q3527215)
