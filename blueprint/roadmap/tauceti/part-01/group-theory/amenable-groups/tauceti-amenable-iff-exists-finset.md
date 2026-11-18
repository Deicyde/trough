---
declaration: theorem
origin: cited
lean: TauCeti.amenable_iff_exists_finset
statement: formalized
proof: formalized
---

# TauCeti.amenable_iff_exists_finset

A discrete group is amenable exactly when for every finite `K ⊆ G` and every `ε > 0` there is
a finite nonempty `F ⊆ G` with `|gF △ F| < ε · |F|` for all `g ∈ K`.

```lean
TauCeti.amenable_iff_exists_finset.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [DiscreteTopology G] [DecidableEq G] :
  TauCeti.Amenable G ↔
    ∀ (K : Finset G) (ε : ℝ),
      0 < ε → ∃ F, F.Nonempty ∧ ∀ g ∈ K, ↑(symmDiff (g • F) F).card < ε * ↑F.card
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)

## Proof depends on

- [TauCeti.amenable_iff_hasFoelnerSets](tauceti-amenable-iff-hasfoelnersets.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.amenable_iff_exists_finset`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/DiscreteFoelner.html#TauCeti.amenable_iff_exists_finset).

## Sources

- [Tau Ceti documentation: `TauCeti.amenable_iff_exists_finset`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/DiscreteFoelner.html#TauCeti.amenable_iff_exists_finset)
- [Source of `TauCeti.amenable_iff_exists_finset` in TauCeti/GroupTheory/Amenable/DiscreteFoelner.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/Amenable/DiscreteFoelner.lean#L167)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AmenableGroups/STATUS.md)
