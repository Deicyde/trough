# Hindman's theorem (Ramsey theory)

The strong form of **Hindman's theorem**: in any finite
cover of an FS-set, one the parts contains an FS-set.

```lean
Hindman.FS_partition_regular.{u_1} {M : Type u_1} [AddSemigroup M] (a : Stream' M) (s : Set (Set M))
  (sfin : s.Finite) (scov : ∀ (m : M), Hindman.FS a m → m ∈ ⋃₀ s) :
  ∃ c ∈ s, ∃ b, ∀ (m : M), Hindman.FS b m → m ∈ c
```

## Depends on

- [Stream](../../data-structures/list-like-structures/stream.md)

## Proof depends on

- [Compactness in terms of filters](../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Continuous function](../../topology/general-topology/part-01/continuous-function.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)

## Sources

- [Mathlib documentation: `Hindman.FS_partition_regular`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Hindman.html#Hindman.FS_partition_regular)
- [Source of `Hindman.FS_partition_regular` in Mathlib/Combinatorics/Hindman.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Combinatorics/Hindman.lean#L192)
- [Mathlib overview: Combinatorics › Ramsey theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L536)
