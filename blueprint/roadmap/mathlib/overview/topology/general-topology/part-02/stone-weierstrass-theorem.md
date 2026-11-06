# Stone-Weierstrass theorem

The **Stone-Weierstrass Approximation Theorem**,
that a subalgebra `A` of `C(X, ℝ)`, where `X` is a compact topological space,
is dense if it separates points.

```lean
ContinuousMap.subalgebra_topologicalClosure_eq_top_of_separatesPoints.{u_1} {X : Type u_1}
  [TopologicalSpace X] [CompactSpace X] (A : Subalgebra ℝ C(X, ℝ)) (w : A.SeparatesPoints) :
  A.topologicalClosure = ⊤
```

## Depends on

- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Closure](../part-01/closure.md)
- [Compact open topology](../part-01/compact-open-topology.md)
- [Metric space](../../metric-spaces/metric-space.md)
- [Topological ring](../../topological-algebra/topological-ring.md)

## Proof depends on

- [Ball](../../metric-spaces/ball.md)
- [Characteristic zero](../../../general-algebra/field-theory/characteristic-zero.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-04/the-triangle-inequality.md)
- [Weierstrass polynomial approximation theorem](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/weierstrass-polynomial-approximation-theorem.md)

## Sources

- [Mathlib documentation: `ContinuousMap.subalgebra_topologicalClosure_eq_top_of_separatesPoints`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/ContinuousMap/StoneWeierstrass.html#ContinuousMap.subalgebra_topologicalClosure_eq_top_of_separatesPoints)
- [Source of `ContinuousMap.subalgebra_topologicalClosure_eq_top_of_separatesPoints` in Mathlib/Topology/ContinuousMap/StoneWeierstrass.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/ContinuousMap/StoneWeierstrass.lean#L259)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L236)
- [1000+ theorems list: Q939927](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1118)
- [1000+ theorems project: Q939927](https://1000-plus.github.io/all.html?length=-1#Q939927)
- [Wikipedia: Stone–Weierstrass theorem](https://en.wikipedia.org/wiki/Stone%E2%80%93Weierstrass_theorem)
- [Wikidata: Q939927](https://www.wikidata.org/wiki/Q939927)
