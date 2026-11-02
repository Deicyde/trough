---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: isCompact_iff_finite_subcover
mathlib_file: Mathlib/Topology/Compactness/Compact.lean
---

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

## Proof depends on

- [Natural number](../../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `isCompact_iff_finite_subcover`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Compactness/Compact.html#isCompact_iff_finite_subcover)
- [Source of `isCompact_iff_finite_subcover` in Mathlib/Topology/Compactness/Compact.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Compactness/Compact.lean#L383)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L229)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L412)
