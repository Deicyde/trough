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

- [The abelianization structure theorem for one-relator pro-`p` groups](../../algebra/part-01/the-abelianization-structure-theorem-for-one-rel.md)
- [An open subgroup of an infinite Demushkin group is Demushkin (Serre's exposé, §9.2)](an-open-subgroup-of-an-infinite-demushkin-group.md)
- [Burnside's basis theorem, cardinal form](../../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The classification of Demushkin groups (Labute)](the-classification-of-demushkin-groups-labute.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Labute's Theorem 4: a Demushkin group has exactly one continuous character with the prescription property](../../algebra/part-01/labutes-theorem-4-a-demushkin-group-has-exactly.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [Tate's duality criterion for `cd_p G ≤ 2`](../../algebra/part-02/tates-duality-criterion-for-cd-p-g-2.md)
- [Tate's theorem: an infinite Demushkin group has `p`-cohomological dimension exactly `2`](tates-theorem-an-infinite-demushkin-group-has-p.md)
- [The three-term Euler formula](../../algebra/part-02/the-three-term-euler-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/OpenSubgroup.html#TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/OpenSubgroup.html#TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff)
- [Source of `TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/OpenSubgroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/OpenSubgroup.lean#L65)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteProPGroups/STATUS.md)
