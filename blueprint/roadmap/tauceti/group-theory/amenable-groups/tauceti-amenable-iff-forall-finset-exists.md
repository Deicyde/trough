---
declaration: theorem
origin: cited
lean: TauCeti.amenable_iff_forall_finset_exists
statement: formalized
proof: formalized
---

# TauCeti.amenable_iff_forall_finset_exists

Finite-intersection criterion: a topological group is amenable exactly when every finite
family of invariance equations `m (L_g f) = m f` is satisfied by some mean.

```lean
TauCeti.amenable_iff_forall_finset_exists.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] :
  TauCeti.Amenable G ↔
    ∀ (s : Finset (G × TauCeti.UCB G)),
      ∃ m, ∀ p ∈ s, m ((TauCeti.UCB.leftTranslation p.1) p.2) = m p.2
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)
- [TauCeti.UCB.leftTranslation](tauceti-ucb-lefttranslation.md)

## Proof depends on

- [TauCeti.Mean.instCompactSpace](tauceti-mean-instcompactspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.amenable_iff_forall_finset_exists`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/WeakStar.html#TauCeti.amenable_iff_forall_finset_exists).

## Sources

- [Tau Ceti documentation: `TauCeti.amenable_iff_forall_finset_exists`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/WeakStar.html#TauCeti.amenable_iff_forall_finset_exists)
- [Source of `TauCeti.amenable_iff_forall_finset_exists` in TauCeti/GroupTheory/Amenable/WeakStar.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Amenable/WeakStar.lean#L210)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AmenableGroups/STATUS.md)
