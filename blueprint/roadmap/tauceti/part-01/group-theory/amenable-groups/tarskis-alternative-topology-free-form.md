---
declaration: theorem
origin: cited
lean: TauCeti.hasFoelnerSets_iff_not_paradoxical_univ
statement: formalized
proof: formalized
---

# Tarski's alternative, topology-free form

a group has Følner sets exactly when it is not
paradoxical for its left regular action.

```lean
TauCeti.hasFoelnerSets_iff_not_paradoxical_univ.{u_1} {G : Type u_1} [Group G] :
  TauCeti.HasFoelnerSets G ↔ ¬TauCeti.Paradoxical G Set.univ
```

## Depends on

- [TauCeti.Paradoxical](tauceti-paradoxical.md)

## Proof depends on

- [Hall's theorem for expanding sets](../../combinatorics/other-results/halls-theorem-for-expanding-sets.md)
- [Paradoxical decompositions from disjoint subcopies](paradoxical-decompositions-from-disjoint-subcopi.md)
- [TauCeti.Amenable](tauceti-amenable.md)
- [TauCeti.Equidecomposable](tauceti-equidecomposable.md)
- [TauCeti.Mean.instCompactSpace](tauceti-mean-instcompactspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasFoelnerSets_iff_not_paradoxical_univ`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Tarski.html#TauCeti.hasFoelnerSets_iff_not_paradoxical_univ).

## Sources

- [Tau Ceti documentation: `TauCeti.hasFoelnerSets_iff_not_paradoxical_univ`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Tarski.html#TauCeti.hasFoelnerSets_iff_not_paradoxical_univ)
- [Source of `TauCeti.hasFoelnerSets_iff_not_paradoxical_univ` in TauCeti/GroupTheory/Amenable/Tarski.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/Amenable/Tarski.lean#L80)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AmenableGroups/STATUS.md)
