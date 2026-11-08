---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.dualityMap0_bijective_dualityMap1_bijective_dualityMap2_injective
statement: formalized
proof: formalized
---

# The dévissage of Tate's duality maps for an infinite pro-`p` group

Under the hypotheses of
`IsProP.dualityMap0_surjective_dualityMap1_bijective_dualityMap2_injective`, if `G` is an infinite
profinite pro-`p` group, then on every finite `p`-primary discrete `G`-module `M` killed by `n`,
`α₀` and `α₁` are bijective and `α₂` is injective: `α₀` is moreover injective by
`IsProP.dualityMap0_injective`.

```lean
TauCeti.IsProP.dualityMap0_bijective_dualityMap1_bijective_dualityMap2_injective.{u, v} {p : ℕ}
  [Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  (hG : TauCeti.IsProP p G) {n : ℕ} (N : Type v) [AddCommGroup N] [TopologicalSpace N]
  [DiscreteTopology N] [DistribMulAction G N] [ContinuousSMul G N] [_root_.Module (ZMod n) N]
  (hN : Module.Baer (ZMod n) N) (hH2 : Module.Baer (ZMod n) (TauCeti.ContCohomology.H2 G N))
  (h :
    ∀ (A : Type u) [inst : AddCommGroup A] [inst_1 : TopologicalSpace A]
      [inst_2 : DiscreteTopology A] [inst_3 : DistribMulAction G A] [inst_4 : ContinuousSMul G A]
      [inst_5 : Finite A],
      Nat.card A = p →
        (∀ (g : G) (a : A), g • a = a) →
          (∀ (a : A), n • a = 0) →
            Function.Surjective ⇑(TauCeti.ContCohomology.dualityMap0 G A N) ∧
              Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap1 G A N) ∧
                Function.Injective ⇑(TauCeti.ContCohomology.dualityMap2 G A N))
  (M : Type u) [AddCommGroup M] [TopologicalSpace M] [DiscreteTopology M] [DistribMulAction G M]
  [ContinuousSMul G M] [Finite M] (hM : TauCeti.IsPPrimaryTorsion p M) (hMn : ∀ (m : M), n • m = 0)
  [CompactSpace G] [TotallyDisconnectedSpace G] [Infinite G] :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap0 G M N) ∧
    Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap1 G M N) ∧
      Function.Injective ⇑(TauCeti.ContCohomology.dualityMap2 G M N)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.dualityMap0_bijective_dualityMap1_bijective_dualityMap2_injective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/TateDuality.html#TauCeti.IsProP.dualityMap0_bijective_dualityMap1_bijective_dualityMap2_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.dualityMap0_bijective_dualityMap1_bijective_dualityMap2_injective`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/TateDuality.html#TauCeti.IsProP.dualityMap0_bijective_dualityMap1_bijective_dualityMap2_injective)
- [Source of `TauCeti.IsProP.dualityMap0_bijective_dualityMap1_bijective_dualityMap2_injective` in TauCeti/Topology/Algebra/Group/Profinite/ProP/TateDuality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ProP/TateDuality.lean#L209)
