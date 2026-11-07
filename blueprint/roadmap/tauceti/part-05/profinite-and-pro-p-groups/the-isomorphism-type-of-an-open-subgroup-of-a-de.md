---
declaration: theorem
origin: cited
lean: TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff
statement: formalized
proof: formalized
---

# The isomorphism type of an open subgroup of a Demushkin group

an open subgroup `U` of an
infinite Demushkin group `G` is topologically isomorphic to a Demushkin group `H` if and only if
`H` has rank `2 + [G : U] (n(G) - 2)` and the canonical character of `H` has image `χ(U)`, where
`χ` is the canonical character of `G`.

```lean
TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff.{u, v} {p : ℕ} [Fact (Nat.Prime p)]
  {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] [Infinite G] (hG : TauCeti.IsDemushkin p G) (U : OpenSubgroup G)
  {H : Type v} [Group H] [TopologicalSpace H] [IsTopologicalGroup H] [CompactSpace H]
  [TotallyDisconnectedSpace H] (hH : TauCeti.IsDemushkin p H) :
  Nonempty (↥↑U ≃ₜ* H) ↔
    TauCeti.demushkinRank hH = 2 + (↑U).index * (TauCeti.demushkinRank hG - 2) ∧
      (TauCeti.demushkinCharacter hH).range =
        Subgroup.map (TauCeti.demushkinCharacter hG).toMonoidHom ↑U
```

## Depends on

- [The Demushkin predicate](the-demushkin-predicate.md)

## Proof depends on

- [An open subgroup of an infinite Demushkin group is Demushkin](an-open-subgroup-of-an-infinite-demushkin-group.md)
- [The classification of Demushkin groups](the-classification-of-demushkin-groups.md)
- [Dimension shifting in every positive degree](../../part-02/continuous-cohomology-of-profinite-groups/dimension-shifting-in-every-positive-degree.md)
- [Tate's theorem: an infinite Demushkin group has `p`-cohomological dimension exactly `2`](tates-theorem-an-infinite-demushkin-group-has-p.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/OpenSubgroup.html#TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/OpenSubgroup.html#TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff)
- [Source of `TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/OpenSubgroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/OpenSubgroup.lean#L65)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteProPGroups/STATUS.md)
