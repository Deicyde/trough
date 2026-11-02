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

- [Ball](ball.md)
- [Basis](../../linear-algebra/fundamentals/basis.md)
- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Continuous linear map](../topological-algebra/continuous-linear-map.md)
- [Equivalence of norms in finite dimension](../../analysis/normed-vector-spaces-banach-spaces/equivalence-of-norms-in-finite-dimension.md)
- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Finite product of metric spaces](../../../undergraduate/topology/topology-and-metric-spaces/finite-product-of-metric-spaces.md)
- [Linear independence](../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Local ring](../../general-algebra/rings/local-ring.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Topological ring](../topological-algebra/topological-ring.md)

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
