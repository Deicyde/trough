---
declaration: theorem
origin: cited
lean: TauCeti.not_amenable_freeGroup
statement: formalized
proof: formalized
---

# TauCeti.not_amenable_freeGroup

A free group on at least two generators is not amenable as a discrete group.

```lean
TauCeti.not_amenable_freeGroup.{u_2} {α : Type u_2} [Nontrivial α] [TopologicalSpace (FreeGroup α)]
  [DiscreteTopology (FreeGroup α)] : ¬TauCeti.Amenable (FreeGroup α)
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)

## Proof depends on

- [Paradoxical decompositions from disjoint subcopies](paradoxical-decompositions-from-disjoint-subcopi.md)
- [Tarski's alternative](tarskis-alternative.md)
- [TauCeti.Equidecomposable](tauceti-equidecomposable.md)
- [TauCeti.Paradoxical](tauceti-paradoxical.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.not_amenable_freeGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/FreeGroup.html#TauCeti.not_amenable_freeGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.not_amenable_freeGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/FreeGroup.html#TauCeti.not_amenable_freeGroup)
- [Source of `TauCeti.not_amenable_freeGroup` in TauCeti/GroupTheory/Amenable/FreeGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Amenable/FreeGroup.lean#L39)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AmenableGroups/STATUS.md)
