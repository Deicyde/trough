---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Metric.isCompact_iff_isClosed_bounded, FiniteDimensional.proper
mathlib_file: Mathlib/Topology/MetricSpace/Bounded.lean
---

# Heine-Borel theorem (proper metric space version)

Mathlib records this with 2 declarations.

`Metric.isCompact_iff_isClosed_bounded`: The **Heine–Borel theorem**:
In a proper metric space, a set is compact if and only if it is closed and bounded.

```lean
Metric.isCompact_iff_isClosed_bounded.{u_2} {α : Type u_2} {s : Set α} [MetricSpace α]
  [ProperSpace α] : IsCompact s ↔ IsClosed s ∧ Bornology.IsBounded s
```

`FiniteDimensional.proper`: Any finite-dimensional vector space over a locally compact field is proper.
We do not register this as an instance to avoid an instance loop when trying to prove the
properness of `𝕜`, and the search for `𝕜` as an unknown metavariable. Declare the instance
explicitly when needed.

```lean
FiniteDimensional.proper.{u, v} (𝕜 : Type u) [NontriviallyNormedField 𝕜] (E : Type v)
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] [LocallyCompactSpace 𝕜] [FiniteDimensional 𝕜 E] :
  ProperSpace E
```

## Depends on

- [Compactness in terms of filters](../general-topology/part-01/compactness-in-terms-of-filters.md)
- [Finite-dimensionality](../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Normed vector space over a normed field](../../analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Aleph numbers](../../logic-and-computation/set-theory/cardinals/aleph-numbers.md)
- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Closure](../general-topology/part-01/closure.md)
- [Continuous linear map](../topological-algebra/continuous-linear-map.md)
- [Equivalence of norms in finite dimension](../../analysis/normed-vector-spaces-banach-spaces/equivalence-of-norms-in-finite-dimension.md)
- [Existence of bases](../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Finite product of metric spaces](../../../undergraduate/topology/topology-and-metric-spaces/finite-product-of-metric-spaces.md)
- [Fundamental sequences](../../logic-and-computation/set-theory/ordinals/fundamental-sequences.md)
- [Hilbert basis theorem](../../general-algebra/polynomials-and-power-series/hilbert-basis-theorem.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Isomorphism with $K^n$](../../linear-algebra/finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Lipschitz continuity](lipschitz-continuity.md)
- [Local ring](../../general-algebra/rings/local-ring.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Open map](../general-topology/part-01/open-map.md)
- [Polynomial in several indeterminates](../../general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Subring](../../general-algebra/rings/subring.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Tychonoff's theorem](../../../thousand-plus/geometry-and-topology/54-general-topology/part-02/tychonoffs-theorem.md)
- [Uniformly continuous function](../uniform-notions/uniformly-continuous-function.md)
- [Well-ordering theorem](../../../thousand-plus/general-topics-history-and-foundations/03-mathematical-logic-and-foundations/part-03/well-ordering-theorem.md)

## Sources

- [Mathlib documentation: `Metric.isCompact_iff_isClosed_bounded`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Bounded.html#Metric.isCompact_iff_isClosed_bounded)
- [Source of `Metric.isCompact_iff_isClosed_bounded` in Mathlib/Topology/MetricSpace/Bounded.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/MetricSpace/Bounded.lean#L332)
- [Mathlib documentation: `FiniteDimensional.proper`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Module/FiniteDimension.html#FiniteDimensional.proper)
- [Source of `FiniteDimensional.proper` in Mathlib/Analysis/Normed/Module/FiniteDimension.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Module/FiniteDimension.lean#L542)
- [Mathlib overview: Topology › Metric spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L263)
- [Mathlib undergraduate list: Single Variable Real Analysis › Topology of R](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L293)
- [1000+ theorems list: Q253214](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L278)
- [1000+ theorems project: Q253214](https://1000-plus.github.io/?length=-1#Q253214)
- [Wikipedia: Heine–Borel theorem](https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem)
- [Wikidata: Q253214](https://www.wikidata.org/wiki/Q253214)
