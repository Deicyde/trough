---
declaration: theorem
origin: cited
lean: TauCeti.topologicalGeneratorRankNat_le_of_openSubgroup_of_finiteIndex, TauCeti.topologicalGeneratorRankNat_le_of_openSubgroup
statement: formalized
proof: formalized
---

# The Schreier bound

Let `U` be an open subgroup of finite index in a topologically
finitely generated topological group `G`. Then `U` is topologically finitely generated
(`TauCeti.IsTopologicallyFinitelyGenerated.of_openSubgroup_of_finiteIndex`), and
`d(U) ≤ 1 + [G : U] * (d(G) - 1)`, with subtraction in `ℕ`. This is the topological form of
Schreier's index formula `Subgroup.rank_le_one_add_index_mul_rank_sub_one`. The bound is sharp:
finite-index subgroups of nontrivial finitely generated discrete free groups attain it, by the
Nielsen–Schreier theorem.

```lean
TauCeti.topologicalGeneratorRankNat_le_of_openSubgroup_of_finiteIndex.{u} {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] (hG : TauCeti.IsTopologicallyFinitelyGenerated G)
  (U : OpenSubgroup G) [(↑U).FiniteIndex] :
  TauCeti.topologicalGeneratorRankNat ↥↑U ⋯ ≤
    1 + (↑U).index * (TauCeti.topologicalGeneratorRankNat G hG - 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schreier's index formula](../../../group-theory/other-results/schreiers-index-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.topologicalGeneratorRankNat_le_of_openSubgroup_of_finiteIndex`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Rank.html#TauCeti.topologicalGeneratorRankNat_le_of_openSubgroup_of_finiteIndex).

## Other forms

**The Schreier bound for open subgroups of a compact group.** Formalized in Tau Ceti as [`TauCeti.topologicalGeneratorRankNat_le_of_openSubgroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Rank.html#TauCeti.topologicalGeneratorRankNat_le_of_openSubgroup).

```lean
TauCeti.topologicalGeneratorRankNat_le_of_openSubgroup.{u} {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  (hG : TauCeti.IsTopologicallyFinitelyGenerated G) (U : OpenSubgroup G) :
  TauCeti.topologicalGeneratorRankNat ↥↑U ⋯ ≤
    1 + (↑U).index * (TauCeti.topologicalGeneratorRankNat G hG - 1)
```

## Sources

- [Tau Ceti documentation: `TauCeti.topologicalGeneratorRankNat_le_of_openSubgroup_of_finiteIndex`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Rank.html#TauCeti.topologicalGeneratorRankNat_le_of_openSubgroup_of_finiteIndex)
- [Source of `TauCeti.topologicalGeneratorRankNat_le_of_openSubgroup_of_finiteIndex` in TauCeti/Topology/Algebra/Group/Profinite/Rank.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Rank.lean#L323)
