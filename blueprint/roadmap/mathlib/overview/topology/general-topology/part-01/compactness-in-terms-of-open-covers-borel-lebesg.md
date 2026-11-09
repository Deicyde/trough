# Compactness in terms of open covers (Borel-Lebesgue)

A set `s` is compact if and only if
for every open cover of `s`, there exists a finite subcover.

```lean
isCompact_iff_finite_subcover.{u} {X : Type u} [TopologicalSpace X] {s : Set X} :
  IsCompact s ↔
    ∀ {ι : Type u} (U : ι → Set X), (∀ (i : ι), IsOpen (U i)) → s ⊆ ⋃ i, U i → ∃ t, s ⊆ ⋃ i ∈ t, U i
```

## Depends on

- [Compactness in terms of filters](compactness-in-terms-of-filters.md)
- [Finite set](../../../data-structures/sets/finite-set.md)

## Sources

- [Mathlib documentation: `isCompact_iff_finite_subcover`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Compactness/Compact.html#isCompact_iff_finite_subcover)
- [Source of `isCompact_iff_finite_subcover` in Mathlib/Topology/Compactness/Compact.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Compactness/Compact.lean#L383)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L229)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L412)
