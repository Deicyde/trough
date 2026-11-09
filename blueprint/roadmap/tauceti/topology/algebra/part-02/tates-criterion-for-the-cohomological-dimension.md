---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.cohomologicalDimensionAt_le_of_forall_coeffMap_proj_surjective
statement: formalized
proof: formalized
---

# Tate's criterion for the cohomological dimension of a pro-`p` group

Let `G` be a profinite
pro-`p` group. If for every short exact sequence `0 → A → B → C → 0` of finite discrete `G`-modules
killed by `p` the map `Hⁿ(G, B) → Hⁿ(G, C)` is surjective, then `cd_p G ≤ n`: right exactness
kills `Hⁿ⁺¹` on those modules, and dévissage extends the vanishing to every finite discrete
`p`-primary module.

```lean
TauCeti.IsProP.cohomologicalDimensionAt_le_of_forall_coeffMap_proj_surjective.{u} {p : ℕ}
  [hp : Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] (hG : TauCeti.IsProP p G) [TotallyDisconnectedSpace G] (n : ℕ)
  (h :
    ∀ (A B C : Type u) [inst : AddCommGroup A] [inst_1 : TopologicalSpace A]
      [inst_2 : DiscreteTopology A] [inst_3 : DistribMulAction G A] [ContinuousSMul G A] [Finite A]
      [inst_6 : AddCommGroup B] [inst_7 : TopologicalSpace B] [inst_8 : DiscreteTopology B]
      [inst_9 : DistribMulAction G B] [ContinuousSMul G B] [Finite B] [inst_12 : AddCommGroup C]
      [inst_13 : TopologicalSpace C] [inst_14 : DiscreteTopology C] [inst_15 : DistribMulAction G C]
      [ContinuousSMul G C] [Finite C] (S : TauCeti.ContCohomology.DiscreteShortExact G A B C),
      (∀ (a : A), p • a = 0) →
        (∀ (b : B), p • b = 0) →
          (∀ (c : C), p • c = 0) →
            Function.Surjective
              ⇑(CategoryTheory.ConcreteCategory.hom
                  (TauCeti.ContinuousCohomology.coeffMap
                    (TauCeti.ofDiscreteModuleMap S.proj.toIntLinearMap ⋯) n))) :
  TauCeti.cohomologicalDimensionAt p G ≤ ↑n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dimension shifting in every positive degree](../../../representation-theory/continuous-cohomology-of-profinite-groups/dimension-shifting-in-every-positive-degree.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.cohomologicalDimensionAt_le_of_forall_coeffMap_proj_surjective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/CohomologicalDimension.html#TauCeti.IsProP.cohomologicalDimensionAt_le_of_forall_coeffMap_proj_surjective).

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.cohomologicalDimensionAt_le_of_forall_coeffMap_proj_surjective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/CohomologicalDimension.html#TauCeti.IsProP.cohomologicalDimensionAt_le_of_forall_coeffMap_proj_surjective)
- [Source of `TauCeti.IsProP.cohomologicalDimensionAt_le_of_forall_coeffMap_proj_surjective` in TauCeti/Topology/Algebra/Group/Profinite/ProP/CohomologicalDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ProP/CohomologicalDimension.lean#L180)
