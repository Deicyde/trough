---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: szemeredi_regularity
mathlib_file: Mathlib/Combinatorics/SimpleGraph/Regularity/Lemma.lean
---

# Regularity lemma

Effective **Szemerédi Regularity Lemma**: For any sufficiently large graph, there is an
`ε`-uniform equipartition of bounded size (where the bound does not depend on the graph).

```lean
szemeredi_regularity.{u_1} {α : Type u_1} [DecidableEq α] [Fintype α] (G : SimpleGraph α)
  [DecidableRel G.Adj] {ε : ℝ} {l : ℕ} (hε : 0 < ε) (hl : l ≤ Fintype.card α) :
  ∃ P,
    P.IsEquipartition ∧
      l ≤ P.parts.card ∧ P.parts.card ≤ SzemerediRegularity.bound ε l ∧ P.IsUniform G ε
```

## Depends on

- [Logarithm](../../analysis/special-functions/logarithm.md)
- [Simple graph](simple-graph.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Cantor’s Theorem](../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic p](../../general-algebra/field-theory/characteristic-p.md)
- [Cluster point](../../topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Congruence in $\Z$](../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Intermediate value theorem](../../topology/topological-algebra/intermediate-value-theorem.md)
- [Lipschitz continuity](../../topology/metric-spaces/lipschitz-continuity.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Norm of a continuous linear map](../../analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Normed vector space over a normed field](../../analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Order of an element](../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Power functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/power-functions.md)
- [Schroeder-Bernstein Theorem](../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Subgroup](../../general-algebra/group-theory/part-01/subgroup.md)
- [The Binomial Theorem](../../../hundred-theorems/part-03/the-binomial-theorem.md)
- [The Number of Subsets of a Set](../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `szemeredi_regularity`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/Regularity/Lemma.html#szemeredi_regularity)
- [Source of `szemeredi_regularity` in Mathlib/Combinatorics/SimpleGraph/Regularity/Lemma.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SimpleGraph/Regularity/Lemma.lean#L74)
- [Mathlib overview: Combinatorics › Graph theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L530)
