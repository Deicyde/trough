---
declaration: theorem
origin: cited
lean: IsPGroup.sq_topologicalGeneratorRankNat_lt_four_mul_finrank_cohomFp_two
statement: formalized
proof: formalized
---

# The Golod–Shafarevich inequality

A nontrivial finite `p`-group `G`, with the discrete
topology, satisfies `d(G)² < 4 r(G)`, where `d(G)` is its generator rank and
`r(G) = dim_{𝔽_p} H²(G, 𝔽_p)` is its relation rank. Finite generation follows from
`TauCeti.isTopologicallyFinitelyGenerated_of_fg`.

```lean
IsPGroup.sq_topologicalGeneratorRankNat_lt_four_mul_finrank_cohomFp_two.{u} {p : ℕ}
  [Fact (Nat.Prime p)] {G : Type u} [Group G] [Finite G] [Nontrivial G] [TopologicalSpace G]
  [DiscreteTopology G] (hG : IsPGroup p G) :
  TauCeti.topologicalGeneratorRankNat G ⋯ ^ 2 <
    4 * Module.finrank (ZMod p) ↑(TauCeti.cohomFp p G 2).toModuleCat
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsPGroup.sq_topologicalGeneratorRankNat_lt_four_mul_finrank_cohomFp_two`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/GolodShafarevich.html#IsPGroup.sq_topologicalGeneratorRankNat_lt_four_mul_finrank_cohomFp_two).

## Sources

- [Tau Ceti documentation: `IsPGroup.sq_topologicalGeneratorRankNat_lt_four_mul_finrank_cohomFp_two`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/GolodShafarevich.html#IsPGroup.sq_topologicalGeneratorRankNat_lt_four_mul_finrank_cohomFp_two)
- [Source of `IsPGroup.sq_topologicalGeneratorRankNat_lt_four_mul_finrank_cohomFp_two` in TauCeti/Topology/Algebra/Group/Profinite/ProP/GolodShafarevich.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ProP/GolodShafarevich.lean#L75)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteProPGroups/STATUS.md)
