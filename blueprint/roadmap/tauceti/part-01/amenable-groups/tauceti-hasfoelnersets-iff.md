---
declaration: theorem
origin: cited
lean: TauCeti.hasFoelnerSets_iff
statement: formalized
proof: formalized
---

# TauCeti.hasFoelnerSets\_iff

A group has Følner sets exactly when for every finite `K ⊆ G` and every `ε > 0` there is a
finite nonempty `F ⊆ G` with `|gF △ F| < ε · |F|` for all `g ∈ K`.

```lean
TauCeti.hasFoelnerSets_iff.{u_1} {G : Type u_1} [Group G] [DecidableEq G] :
  TauCeti.HasFoelnerSets G ↔
    ∀ (K : Finset G) (ε : ℝ),
      0 < ε → ∃ F, F.Nonempty ∧ ∀ g ∈ K, ↑(symmDiff (g • F) F).card < ε * ↑F.card
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.hasFoelnerSets_iff`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Foelner.html#TauCeti.hasFoelnerSets_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.hasFoelnerSets_iff`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Foelner.html#TauCeti.hasFoelnerSets_iff)
- [Source of `TauCeti.hasFoelnerSets_iff` in TauCeti/GroupTheory/Amenable/Foelner.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Amenable/Foelner.lean#L157)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AmenableGroups/STATUS.md)
