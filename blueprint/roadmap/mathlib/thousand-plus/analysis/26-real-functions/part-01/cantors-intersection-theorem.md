# Cantor's intersection theorem

Cantor's intersection theorem for `sInter`:
the intersection of a directed family of nonempty compact closed sets is nonempty.

```lean
IsCompact.nonempty_sInter_of_directed_nonempty_isCompact_isClosed.{u} {X : Type u}
  [TopologicalSpace X] {S : Set (Set X)} [hS : Nonempty ↑S]
  (hSd : DirectedOn (fun x1 x2 => x1 ⊇ x2) S) (hSn : ∀ U ∈ S, U.Nonempty)
  (hSc : ∀ U ∈ S, IsCompact U) (hScl : ∀ U ∈ S, IsClosed U) : (⋂₀ S).Nonempty
```

## Depends on

- [Compactness in terms of filters](../../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)

## Sources

- [Mathlib documentation: `IsCompact.nonempty_sInter_of_directed_nonempty_isCompact_isClosed`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Compactness/Compact.html#IsCompact.nonempty_sInter_of_directed_nonempty_isCompact_isClosed)
- [Source of `IsCompact.nonempty_sInter_of_directed_nonempty_isCompact_isClosed` in Mathlib/Topology/Compactness/Compact.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Compactness/Compact.lean#L326)
- [1000+ theorems list: Q1050203](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1238)
- [1000+ theorems project: Q1050203](https://1000-plus.github.io/all.html?length=-1#Q1050203)
- [Wikipedia: Cantor's intersection theorem](https://en.wikipedia.org/wiki/Cantor's_intersection_theorem)
- [Wikidata: Q1050203](https://www.wikidata.org/wiki/Q1050203)
