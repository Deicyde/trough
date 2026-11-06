# Sequential compactness is equivalent to compactness (Bolzano-Weierstrass)

A version of **Bolzano-Weierstrass**: in a (pseudo)metrizable space, a set is compact if and
only if it is sequentially compact.

```lean
isCompact_iff_isSeqCompact.{u_1} {X : Type u_1} [TopologicalSpace X]
  [TopologicalSpace.PseudoMetrizableSpace X] {s : Set X} : IsCompact s ↔ IsSeqCompact s
```

## Depends on

- [Compactness in terms of filters](../general-topology/part-01/compactness-in-terms-of-filters.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Uniform space](../uniform-notions/uniform-space.md)

## Proof depends on

- [Cauchy sequence](../uniform-notions/cauchy-sequence.md)
- [Limit point](../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)

## Sources

- [Mathlib documentation: `isCompact_iff_isSeqCompact`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Sequences.html#isCompact_iff_isSeqCompact)
- [Source of `isCompact_iff_isSeqCompact` in Mathlib/Topology/Sequences.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Sequences.lean#L413)
- [Mathlib overview: Topology › Metric spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L262)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L413)
