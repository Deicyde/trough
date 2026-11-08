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

- [The Demushkin predicate (Labute, p. 106), for a prime `p` and a topological group `G`](the-demushkin-predicate-labute-p-106-for-a-prime.md)

## Proof depends on

- [The abelianization structure theorem for one-relator pro-`p` groups](../../algebra/part-01/the-abelianization-structure-theorem-for-one-rel.md)
- [An open subgroup of an infinite Demushkin group is Demushkin (Serre's exposé, §9.2)](an-open-subgroup-of-an-infinite-demushkin-group.md)
- [Burnside's basis theorem, cardinal form](../../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The classification of Demushkin groups (Labute)](the-classification-of-demushkin-groups-labute.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Injectivity of Tate's duality map `α₂` descends to an open subgroup](../../../representation-theory/homological/injectivity-of-tates-duality-map-2-descends-to-a.md)
- [Labute's Theorem 2](labutes-theorem-2.md)
- [Shapiro's lemma in every degree](../../../representation-theory/homological/shapiros-lemma-in-every-degree.md)
- [Tate's duality map `α₁` of an infinite Demushkin group with coefficients `I(χ)/pⁱ` is bijective on every finite discrete `G`-module `M` killed by `pⁱ`](tates-duality-map-1-of-an-infinite-demushkin-gro.md)
- [The three-term Euler formula](../../algebra/part-02/the-three-term-euler-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/OpenSubgroup.html#TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/OpenSubgroup.html#TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff)
- [Source of `TauCeti.IsDemushkin.nonempty_continuousMulEquiv_openSubgroup_iff` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/OpenSubgroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/OpenSubgroup.lean#L65)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteProPGroups/STATUS.md)
