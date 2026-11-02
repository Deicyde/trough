---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: BoundedContinuousFunction.exists_extension_norm_eq_of_isClosedEmbedding
mathlib_file: Mathlib/Topology/TietzeExtension.lean
---

# Tietze extension theorem

**Tietze extension theorem** for real-valued bounded continuous maps, a version with a closed
embedding and unbundled composition. If `e : C(X, Y)` is a closed embedding of a topological space
into a normal topological space and `f : X →ᵇ ℝ` is a bounded continuous function, then there exists
a bounded continuous function `g : Y →ᵇ ℝ` of the same norm such that `g ∘ e = f`.

```lean
BoundedContinuousFunction.exists_extension_norm_eq_of_isClosedEmbedding.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [TopologicalSpace X] [TopologicalSpace Y] [NormalSpace Y]
  (f : BoundedContinuousFunction X ℝ) {e : X → Y} (he : Topology.IsClosedEmbedding e) :
  ∃ g, ‖g‖ = ‖f‖ ∧ ⇑g ∘ e = ⇑f
```

## Depends on

- [Continuous function](../../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Induced topology](../../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)

## Proof depends on

- [Characteristic zero](../../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Closed map](../../../../overview/topology/general-topology/part-01/closed-map.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Completeness of spaces of bounded continuous functions](../../../../overview/analysis/normed-vector-spaces-banach-spaces/completeness-of-spaces-of-bounded-continuous-fun.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Lipschitz continuity](../../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [List](../../../../overview/data-structures/list-like-structures/list.md)
- [Topological ring](../../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `BoundedContinuousFunction.exists_extension_norm_eq_of_isClosedEmbedding`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/TietzeExtension.html#BoundedContinuousFunction.exists_extension_norm_eq_of_isClosedEmbedding)
- [Source of `BoundedContinuousFunction.exists_extension_norm_eq_of_isClosedEmbedding` in Mathlib/Topology/TietzeExtension.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/TietzeExtension.lean#L270)
- [1000+ theorems list: Q1346677](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1621)
- [1000+ theorems project: Q1346677](https://1000-plus.github.io/?length=-1#Q1346677)
- [Wikipedia: Tietze extension theorem](https://en.wikipedia.org/wiki/Tietze_extension_theorem)
- [Wikidata: Q1346677](https://www.wikidata.org/wiki/Q1346677)
