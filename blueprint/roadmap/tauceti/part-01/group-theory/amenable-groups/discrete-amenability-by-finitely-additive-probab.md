---
declaration: theorem
origin: cited
lean: TauCeti.amenable_iff_exists_invariantContent
statement: formalized
proof: formalized
---

# Discrete amenability by finitely additive probabilities

A discrete group is amenable
exactly when it admits a left-invariant finitely additive probability on all subsets.

```lean
TauCeti.amenable_iff_exists_invariantContent.{u_1} (G : Type u_1) [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [DiscreteTopology G] :
  TauCeti.Amenable G ↔ ∃ ν, ν Set.univ = 1 ∧ ∀ (g : G) (s : Set G), ν (g • s) = ν s
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.amenable_iff_exists_invariantContent`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Content.html#TauCeti.amenable_iff_exists_invariantContent).

## Sources

- [Tau Ceti documentation: `TauCeti.amenable_iff_exists_invariantContent`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Content.html#TauCeti.amenable_iff_exists_invariantContent)
- [Source of `TauCeti.amenable_iff_exists_invariantContent` in TauCeti/GroupTheory/Amenable/Content.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Amenable/Content.lean#L213)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AmenableGroups/STATUS.md)
