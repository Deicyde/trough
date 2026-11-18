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

## Proof depends on

- [Burnside's basis theorem, cardinal form](../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [The Golod–Shafarevich inequality for finite-dimensional algebras](../../../part-01/ring-theory/part-01/ideal/the-golod-shafarevich-inequality-for-finite-dime.md)

## Lean

Formalized in Tau Ceti as [`IsPGroup.sq_topologicalGeneratorRankNat_lt_four_mul_finrank_cohomFp_two`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/GolodShafarevich.html#IsPGroup.sq_topologicalGeneratorRankNat_lt_four_mul_finrank_cohomFp_two).

## Sources

- [Tau Ceti documentation: `IsPGroup.sq_topologicalGeneratorRankNat_lt_four_mul_finrank_cohomFp_two`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/GolodShafarevich.html#IsPGroup.sq_topologicalGeneratorRankNat_lt_four_mul_finrank_cohomFp_two)
- [Source of `IsPGroup.sq_topologicalGeneratorRankNat_lt_four_mul_finrank_cohomFp_two` in TauCeti/Topology/Algebra/Group/Profinite/ProP/GolodShafarevich.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/Profinite/ProP/GolodShafarevich.lean#L75)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ProfiniteProPGroups/STATUS.md)
