---
declaration: theorem
origin: cited
lean: TauCeti.amenable_iff_not_paradoxical_univ
statement: formalized
proof: formalized
---

# Tarski's alternative

a discrete group is amenable exactly when it is not paradoxical for
its left regular action.

```lean
TauCeti.amenable_iff_not_paradoxical_univ.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [DiscreteTopology G] : TauCeti.Amenable G ↔ ¬TauCeti.Paradoxical G Set.univ
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)
- [TauCeti.Paradoxical](tauceti-paradoxical.md)

## Proof depends on

- [Tarski's alternative, topology-free form](tarskis-alternative-topology-free-form.md)
- [TauCeti.amenable_iff_hasFoelnerSets](tauceti-amenable-iff-hasfoelnersets.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.amenable_iff_not_paradoxical_univ`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Tarski.html#TauCeti.amenable_iff_not_paradoxical_univ).

## Sources

- [Tau Ceti documentation: `TauCeti.amenable_iff_not_paradoxical_univ`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Tarski.html#TauCeti.amenable_iff_not_paradoxical_univ)
- [Source of `TauCeti.amenable_iff_not_paradoxical_univ` in TauCeti/GroupTheory/Amenable/Tarski.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Amenable/Tarski.lean#L96)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AmenableGroups/STATUS.md)
