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
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)
- [Uniform space](../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Aleph numbers](../../../overview/logic-and-computation/set-theory/cardinals/aleph-numbers.md)
- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Ball](../../../overview/topology/metric-spaces/ball.md)
- [Closed map](../../../overview/topology/general-topology/part-01/closed-map.md)
- [Convex function](../../../overview/analysis/convexity/convex-function.md)
- [Dual of a normed space](../../../overview/analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Existence of bases](../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Extreme value theorem](../../../overview/topology/topological-algebra/extreme-value-theorem.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Fundamental sequences](../../../overview/logic-and-computation/set-theory/ordinals/fundamental-sequences.md)
- [Hilbert basis theorem](../../../overview/general-algebra/polynomials-and-power-series/hilbert-basis-theorem.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Isomorphism with $K^n$](../../../overview/linear-algebra/finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Lipschitz continuity](../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Local ring](../../../overview/general-algebra/rings/local-ring.md)
- [M. Riesz extension theorem](../../analysis/46-functional-analysis/part-02/m-riesz-extension-theorem.md)
- [Maximal ideal](../../../overview/general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Open map](../../../overview/topology/general-topology/part-01/open-map.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [Polynomial in several indeterminates](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [Quotient space](../../../overview/linear-algebra/fundamentals/quotient-space.md)
- [Subring](../../../overview/general-algebra/rings/subring.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Well-ordering theorem](../../general-topics-history-and-foundations/03-mathematical-logic-and-foundations/part-03/well-ordering-theorem.md)

## Sources

- [Mathlib documentation: `closure_convexHull_extremePoints`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/KreinMilman.html#closure_convexHull_extremePoints)
- [Source of `closure_convexHull_extremePoints` in Mathlib/Analysis/Convex/KreinMilman.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Convex/KreinMilman.lean#L94)
- [1000+ theorems list: Q642620](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L655)
- [1000+ theorems project: Q642620](https://1000-plus.github.io/?length=-1#Q642620)
- [Wikipedia: Krein–Milman theorem](https://en.wikipedia.org/wiki/Krein%E2%80%93Milman_theorem)
- [Wikidata: Q642620](https://www.wikidata.org/wiki/Q642620)
