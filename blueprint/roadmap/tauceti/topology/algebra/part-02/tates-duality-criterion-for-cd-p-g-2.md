---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.cohomologicalDimensionAt_le_two_of_forall_dualityMap2_bijective
statement: formalized
proof: formalized
---

# Tate's duality criterion for `cd_p G ≤ 2`

Let `G` be a profinite pro-`p` group and `N` a
discrete `G`-module. If Tate's duality map in degree two,
`α₂ : H²(G, M) → Hom(H⁰(G, InternalHom G M N), H²(G, N))`, is bijective for every finite discrete
`G`-module `M` killed by `p`, then `cd_p G ≤ 2`: duality makes `H²(G, -)` right exact on those
modules (`TauCeti.ContCohomology.DiscreteShortExact.coeffMap_proj_surjective_of_dualityMap2`), and
right exactness bounds the dimension. For an infinite Demushkin group and `N = 𝔽_p` the hypothesis
is Tate's perfect duality, and the conclusion is the upper bound in `cd_p G = 2`.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Tate's criterion for the cohomological dimension of a pro-`p` group](tates-criterion-for-the-cohomological-dimension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.cohomologicalDimensionAt_le_two_of_forall_dualityMap2_bijective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/CohomologicalDimension.html#TauCeti.IsProP.cohomologicalDimensionAt_le_two_of_forall_dualityMap2_bijective).

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.cohomologicalDimensionAt_le_two_of_forall_dualityMap2_bijective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/CohomologicalDimension.html#TauCeti.IsProP.cohomologicalDimensionAt_le_two_of_forall_dualityMap2_bijective)
- [Source of `TauCeti.IsProP.cohomologicalDimensionAt_le_two_of_forall_dualityMap2_bijective` in TauCeti/Topology/Algebra/Group/Profinite/ProP/CohomologicalDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ProP/CohomologicalDimension.lean#L204)
