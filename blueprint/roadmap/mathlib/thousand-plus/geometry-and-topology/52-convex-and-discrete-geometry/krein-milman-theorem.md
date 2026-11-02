---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: closure_convexHull_extremePoints
mathlib_file: Mathlib/Analysis/Convex/KreinMilman.lean
---

# Krein–Milman theorem

**Krein-Milman theorem**: In an LCTVS, any compact convex set is the closure of the convex hull
of its extreme points.

```lean
closure_convexHull_extremePoints.{u_1} {E : Type u_1} [AddCommGroup E] [_root_.Module ℝ E]
  [TopologicalSpace E] [T2Space E] [IsTopologicalAddGroup E] [ContinuousSMul ℝ E]
  [LocallyConvexSpace ℝ E] {s : Set E} (hscomp : IsCompact s) (hAconv : Convex ℝ s) :
  closure ((convexHull ℝ) (Set.extremePoints ℝ s)) = s
```

## Depends on

- [Bornology](../../../overview/analysis/topological-vector-spaces/bornology.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Compactness in terms of filters](../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Convex hull of a subset of an affine real space](../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-hull-of-a-subset-of-an-affine-real-space.md)
- [Extreme point](../../../undergraduate/affine-and-euclidean-geometry/convexity/extreme-point.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Local convexity](../../../overview/analysis/topological-vector-spaces/local-convexity.md)
- [Order (Real numbers)](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)
- [Uniform space](../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Dual of a normed space](../../../overview/analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `closure_convexHull_extremePoints`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/KreinMilman.html#closure_convexHull_extremePoints)
- [Source of `closure_convexHull_extremePoints` in Mathlib/Analysis/Convex/KreinMilman.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Convex/KreinMilman.lean#L94)
- [1000+ theorems list: Q642620](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L655)
- [1000+ theorems project: Q642620](https://1000-plus.github.io/?length=-1#Q642620)
- [Wikipedia: Krein–Milman theorem](https://en.wikipedia.org/wiki/Krein%E2%80%93Milman_theorem)
- [Wikidata: Q642620](https://www.wikidata.org/wiki/Q642620)
