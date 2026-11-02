---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ContinuousMap.subalgebra_topologicalClosure_eq_top_of_separatesPoints
mathlib_file: Mathlib/Topology/ContinuousMap/StoneWeierstrass.lean
---

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
- [Lipschitz continuity](../../metric-spaces/lipschitz-continuity.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Topological ring](../../topological-algebra/topological-ring.md)

## Proof depends on

- [Ball](../../metric-spaces/ball.md)
- [Characteristic zero](../../../general-algebra/field-theory/characteristic-zero.md)
- [Field $\R$ of real numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Linear map](../../../linear-algebra/fundamentals/linear-map.md)
- [Order topology](../../topological-algebra/order-topology.md)
- [Polynomial functions](../../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/polynomial-functions.md)
- [Subring](../../../general-algebra/rings/subring.md)

## Sources

- [Mathlib documentation: `ContinuousMap.subalgebra_topologicalClosure_eq_top_of_separatesPoints`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/ContinuousMap/StoneWeierstrass.html#ContinuousMap.subalgebra_topologicalClosure_eq_top_of_separatesPoints)
- [Source of `ContinuousMap.subalgebra_topologicalClosure_eq_top_of_separatesPoints` in Mathlib/Topology/ContinuousMap/StoneWeierstrass.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/ContinuousMap/StoneWeierstrass.lean#L259)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L236)
- [1000+ theorems list: Q939927](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1118)
- [1000+ theorems project: Q939927](https://1000-plus.github.io/?length=-1#Q939927)
- [Wikipedia: Stone–Weierstrass theorem](https://en.wikipedia.org/wiki/Stone%E2%80%93Weierstrass_theorem)
- [Wikidata: Q939927](https://www.wikidata.org/wiki/Q939927)
