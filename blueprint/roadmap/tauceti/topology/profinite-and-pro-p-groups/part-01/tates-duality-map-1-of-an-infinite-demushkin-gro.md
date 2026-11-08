---
declaration: theorem
origin: cited
lean: TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective, TauCeti.IsProP.cohomologicalDimensionAt_le_two_of_forall_dualityMap2_bijective, TauCeti.IsDemushkin.dualityMap0_zmod_bijective, TauCeti.IsDemushkin.dualityMap0_surjective, TauCeti.IsDemushkin.dualityMap0_bijective, TauCeti.IsDemushkin.dualityMap0_injective, TauCeti.IsDemushkin.dualityMap0_zModTwist_bijective, TauCeti.IsDemushkin.dualityMap1_bijective, TauCeti.IsDemushkin.dualityMap1_zmod_bijective, TauCeti.IsDemushkin.dualityMap2_injective, TauCeti.IsDemushkin.dualityMap2_bijective, TauCeti.IsDemushkin.dualityMap2_zModTwist_bijective
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

- [The Demushkin predicate (Labute, p. 106), for a prime `p` and a topological group `G`](the-demushkin-predicate-labute-p-106-for-a-prime.md)

## Proof depends on

- [The dévissage of Tate's duality maps for an infinite pro-`p` group](../../algebra/part-01/the-devissage-of-tates-duality-maps-for-an-infin.md)
- [Labute's Theorem 2](labutes-theorem-2.md)
- [Tate's criterion for the cohomological dimension of a pro-`p` group](../../algebra/part-02/tates-criterion-for-the-cohomological-dimension.md)
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

**Tate's duality map `α₀` of a Demushkin group is bijective at `M = 𝔽_p`.** Formalized in Tau Ceti as [`TauCeti.IsDemushkin.dualityMap0_zmod_bijective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Basic.html#TauCeti.IsDemushkin.dualityMap0_zmod_bijective).

```lean
TauCeti.IsDemushkin.dualityMap0_zmod_bijective.{u} {p : ℕ} [Fact (Nat.Prime p)] {G : Type u}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [LocallyCompactSpace G]
  (hG : TauCeti.IsDemushkin p G) [DistribMulAction G (ZMod p)] [ContinuousSMul G (ZMod p)]
  (htriv : ∀ (g : G) (m : ZMod p), g • m = m) :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap0 G (ZMod p) (ZMod p))
```

**Tate's duality map `α₀` of a Demushkin group is surjective on every finite discrete `G`-module `M` killed by `p`.** Formalized in Tau Ceti as [`TauCeti.IsDemushkin.dualityMap0_surjective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Basic.html#TauCeti.IsDemushkin.dualityMap0_surjective).

```lean
TauCeti.IsDemushkin.dualityMap0_surjective.{u} {p : ℕ} [Fact (Nat.Prime p)] {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [LocallyCompactSpace G] (hG : TauCeti.IsDemushkin p G)
  [DistribMulAction G (ZMod p)] [ContinuousSMul G (ZMod p)]
  (htriv : ∀ (g : G) (m : ZMod p), g • m = m) (M : Type u) [AddCommGroup M] [TopologicalSpace M]
  [DiscreteTopology M] [DistribMulAction G M] [ContinuousSMul G M] [Finite M]
  (hM : ∀ (x : M), p • x = 0) :
  Function.Surjective ⇑(TauCeti.ContCohomology.dualityMap0 G M (ZMod p))
```

**Tate's duality map `α₀` of an infinite Demushkin group is bijective on every finite discrete `G`-module `M` killed by `p`.** Formalized in Tau Ceti as [`TauCeti.IsDemushkin.dualityMap0_bijective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Basic.html#TauCeti.IsDemushkin.dualityMap0_bijective).

```lean
TauCeti.IsDemushkin.dualityMap0_bijective.{u} {p : ℕ} [Fact (Nat.Prime p)] {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  [Infinite G] (hG : TauCeti.IsDemushkin p G) [DistribMulAction G (ZMod p)]
  [ContinuousSMul G (ZMod p)] (htriv : ∀ (g : G) (m : ZMod p), g • m = m) (M : Type u)
  [AddCommGroup M] [TopologicalSpace M] [DiscreteTopology M] [DistribMulAction G M]
  [ContinuousSMul G M] [Finite M] (hM : ∀ (x : M), p • x = 0) :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap0 G M (ZMod p))
```

**Tate's duality map `α₀` of an infinite Demushkin group is injective on every finite discrete `G`-module `M` killed by `p`.** Formalized in Tau Ceti as [`TauCeti.IsDemushkin.dualityMap0_injective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Basic.html#TauCeti.IsDemushkin.dualityMap0_injective).

```lean
TauCeti.IsDemushkin.dualityMap0_injective.{u} {p : ℕ} [Fact (Nat.Prime p)] {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  [Infinite G] (hG : TauCeti.IsDemushkin p G) [DistribMulAction G (ZMod p)]
  [ContinuousSMul G (ZMod p)] (htriv : ∀ (g : G) (m : ZMod p), g • m = m) (M : Type u)
  [AddCommGroup M] [TopologicalSpace M] [DiscreteTopology M] [DistribMulAction G M]
  [ContinuousSMul G M] [Finite M] (hM : ∀ (x : M), p • x = 0) :
  Function.Injective ⇑(TauCeti.ContCohomology.dualityMap0 G M (ZMod p))
```

**Tate's duality map `α₀` of an infinite Demushkin group with coefficients `I(χ)/pⁱ` is bijective on every finite discrete `G`-module `M` killed by `pⁱ`.** Formalized in Tau Ceti as [`TauCeti.IsDemushkin.dualityMap0_zModTwist_bijective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Twisted.html#TauCeti.IsDemushkin.dualityMap0_zModTwist_bijective).

```lean
TauCeti.IsDemushkin.dualityMap0_zModTwist_bijective.{u} {p : ℕ} [Fact (Nat.Prime p)] {G : Type u}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] [Infinite G] (hG : TauCeti.IsDemushkin p G) (i : ℕ) (M : Type u)
  [AddCommGroup M] [TopologicalSpace M] [DiscreteTopology M] [DistribMulAction G M]
  [ContinuousSMul G M] [Finite M] (hM : ∀ (x : M), p ^ i • x = 0) :
  Function.Bijective
    ⇑(TauCeti.ContCohomology.dualityMap0 G M (TauCeti.ZModTwist (TauCeti.demushkinCharacter hG) i))
```

**Tate's duality map `α₁` of a Demushkin group is bijective on every finite discrete `G`-module `M` killed by `p`.** Formalized in Tau Ceti as [`TauCeti.IsDemushkin.dualityMap1_bijective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Basic.html#TauCeti.IsDemushkin.dualityMap1_bijective).

```lean
TauCeti.IsDemushkin.dualityMap1_bijective.{u} {p : ℕ} [Fact (Nat.Prime p)] {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [LocallyCompactSpace G] (hG : TauCeti.IsDemushkin p G)
  [DistribMulAction G (ZMod p)] [ContinuousSMul G (ZMod p)]
  (htriv : ∀ (g : G) (m : ZMod p), g • m = m) (M : Type u) [AddCommGroup M] [TopologicalSpace M]
  [DiscreteTopology M] [DistribMulAction G M] [ContinuousSMul G M] [Finite M]
  (hM : ∀ (x : M), p • x = 0) :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap1 G M (ZMod p))
```

**Tate's duality map `α₁` of a Demushkin group is bijective at `M = 𝔽_p`.** Formalized in Tau Ceti as [`TauCeti.IsDemushkin.dualityMap1_zmod_bijective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Basic.html#TauCeti.IsDemushkin.dualityMap1_zmod_bijective).

```lean
TauCeti.IsDemushkin.dualityMap1_zmod_bijective.{u} {p : ℕ} [Fact (Nat.Prime p)] {G : Type u}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [LocallyCompactSpace G]
  (hG : TauCeti.IsDemushkin p G) [DistribMulAction G (ZMod p)] [ContinuousSMul G (ZMod p)]
  (htriv : ∀ (g : G) (m : ZMod p), g • m = m) :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap1 G (ZMod p) (ZMod p))
```

**Tate's duality map `α₂` of a Demushkin group is injective on every finite discrete `G`-module `M` killed by `p`.** Formalized in Tau Ceti as [`TauCeti.IsDemushkin.dualityMap2_injective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Basic.html#TauCeti.IsDemushkin.dualityMap2_injective).

```lean
TauCeti.IsDemushkin.dualityMap2_injective.{u} {p : ℕ} [Fact (Nat.Prime p)] {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [LocallyCompactSpace G] (hG : TauCeti.IsDemushkin p G)
  [DistribMulAction G (ZMod p)] [ContinuousSMul G (ZMod p)]
  (htriv : ∀ (g : G) (m : ZMod p), g • m = m) (M : Type u) [AddCommGroup M] [TopologicalSpace M]
  [DiscreteTopology M] [DistribMulAction G M] [ContinuousSMul G M] [Finite M]
  (hM : ∀ (x : M), p • x = 0) :
  Function.Injective ⇑(TauCeti.ContCohomology.dualityMap2 G M (ZMod p))
```

**Tate's duality map `α₂` of an infinite Demushkin group is bijective on every finite discrete `G`-module `M` killed by `p`.** Formalized in Tau Ceti as [`TauCeti.IsDemushkin.dualityMap2_bijective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Basic.html#TauCeti.IsDemushkin.dualityMap2_bijective).

```lean
TauCeti.IsDemushkin.dualityMap2_bijective.{u} {p : ℕ} [Fact (Nat.Prime p)] {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  [Infinite G] (hG : TauCeti.IsDemushkin p G) [DistribMulAction G (ZMod p)]
  [ContinuousSMul G (ZMod p)] (htriv : ∀ (g : G) (m : ZMod p), g • m = m) (M : Type u)
  [AddCommGroup M] [TopologicalSpace M] [DiscreteTopology M] [DistribMulAction G M]
  [ContinuousSMul G M] [Finite M] (hM : ∀ (x : M), p • x = 0) :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap2 G M (ZMod p))
```

**Tate's duality map `α₂` of an infinite Demushkin group with coefficients `I(χ)/pⁱ` is bijective on every finite discrete `G`-module `M` killed by `pⁱ`.** Formalized in Tau Ceti as [`TauCeti.IsDemushkin.dualityMap2_zModTwist_bijective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Twisted.html#TauCeti.IsDemushkin.dualityMap2_zModTwist_bijective).

```lean
TauCeti.IsDemushkin.dualityMap2_zModTwist_bijective.{u} {p : ℕ} [Fact (Nat.Prime p)] {G : Type u}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] [Infinite G] (hG : TauCeti.IsDemushkin p G) (i : ℕ) (M : Type u)
  [AddCommGroup M] [TopologicalSpace M] [DiscreteTopology M] [DistribMulAction G M]
  [ContinuousSMul G M] [Finite M] (hM : ∀ (x : M), p ^ i • x = 0) :
  Function.Bijective
    ⇑(TauCeti.ContCohomology.dualityMap2 G M (TauCeti.ZModTwist (TauCeti.demushkinCharacter hG) i))
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Twisted.html#TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective)
- [Source of `TauCeti.IsDemushkin.dualityMap1_zModTwist_bijective` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Twisted.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/Duality/Twisted.lean#L213)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteProPGroups/STATUS.md)
