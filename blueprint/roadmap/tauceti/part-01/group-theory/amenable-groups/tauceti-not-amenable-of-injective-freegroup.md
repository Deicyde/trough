---
declaration: theorem
origin: cited
lean: TauCeti.not_amenable_of_injective_freeGroup
statement: formalized
proof: formalized
---

# TauCeti.not_amenable_of_injective_freeGroup

A discrete group containing a free group on at least two generators, as the image of an
injective homomorphism, is not amenable.

```lean
TauCeti.not_amenable_of_injective_freeGroup.{u_1, u_2} {G : Type u_1} [Group G] [TopologicalSpace G]
  [DiscreteTopology G] {α : Type u_2} [Nontrivial α] (φ : FreeGroup α →* G)
  (hφ : Function.Injective ⇑φ) : ¬TauCeti.Amenable G
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)

## Proof depends on

- [TauCeti.not_amenable_freeGroup](tauceti-not-amenable-freegroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.not_amenable_of_injective_freeGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/FreeGroup.html#TauCeti.not_amenable_of_injective_freeGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.not_amenable_of_injective_freeGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/FreeGroup.html#TauCeti.not_amenable_of_injective_freeGroup)
- [Source of `TauCeti.not_amenable_of_injective_freeGroup` in TauCeti/GroupTheory/Amenable/FreeGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Amenable/FreeGroup.lean#L44)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AmenableGroups/STATUS.md)
