---
declaration: theorem
origin: cited
lean: TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective, TauCeti.IsProP.cohomologicalDimensionAt_le_two_of_forall_dualityMap2_bijective
statement: formalized
proof: formalized
---

# Tate's duality map `α₁` of an infinite Demushkin group with coefficients `I(χ)/pⁱ` is bijective on every finite discrete `G`-module `M` killed by `pⁱ`

`H¹(G, M) × H¹(G, Hom(M, I(χ)/pⁱ)) → H²(G, I(χ)/pⁱ)` is a perfect pairing.

```lean
TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective.{u} {p : ℕ} [Fact (Nat.Prime p)] {G : Type u}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] [Infinite G] (hG : TauCeti.IsDemushkin p G) (i : ℕ) (M : Type u)
  [AddCommGroup M] [TopologicalSpace M] [DiscreteTopology M] [DistribMulAction G M]
  [ContinuousSMul G M] [Finite M] (hM : ∀ (x : M), p ^ i • x = 0) :
  Function.Bijective
    ⇑(TauCeti.ContCohomology.dualityMap1 G M (TauCeti.ZModTwist (TauCeti.demushkinCharacter hG) i))
```

## Depends on

- [The Demushkin predicate](the-demushkin-predicate.md)

## Proof depends on

- [Labute's Theorem 2](labutes-theorem-2.md)
- [Tate's criterion for the cohomological dimension of a pro-`p` group](../algebra/part-02/tates-criterion-for-the-cohomological-dimension.md)
- [Tate's theorem: an infinite Demushkin group has `p`-cohomological dimension exactly `2`](tates-theorem-an-infinite-demushkin-group-has-p.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Twisted.html#TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective).

## Other forms

**Tate's duality criterion for `cd_p G ≤ 2`.** Formalized in Tau Ceti as [`TauCeti.IsProP.cohomologicalDimensionAt_le_two_of_forall_dualityMap2_bijective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/CohomologicalDimension.html#TauCeti.IsProP.cohomologicalDimensionAt_le_two_of_forall_dualityMap2_bijective).

```lean
TauCeti.IsProP.cohomologicalDimensionAt_le_two_of_forall_dualityMap2_bijective.{u, v} {p : ℕ}
  [hp : Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] (hG : TauCeti.IsProP p G) [TotallyDisconnectedSpace G] (N : Type v)
  [AddCommGroup N] [TopologicalSpace N] [DiscreteTopology N] [DistribMulAction G N]
  [ContinuousSMul G N]
  (h :
    ∀ (M : Type u) [inst : AddCommGroup M] [inst_1 : TopologicalSpace M]
      [inst_2 : DiscreteTopology M] [inst_3 : DistribMulAction G M] [inst_4 : ContinuousSMul G M]
      [Finite M],
      (∀ (m : M), p • m = 0) → Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap2 G M N)) :
  TauCeti.cohomologicalDimensionAt p G ≤ 2
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Twisted.html#TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective)
- [Source of `TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Twisted.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Twisted.lean#L213)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteProPGroups/STATUS.md)
