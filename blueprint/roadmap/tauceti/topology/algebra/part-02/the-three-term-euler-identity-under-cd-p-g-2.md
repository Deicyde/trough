---
declaration: theorem
origin: cited
lean: TauCeti.CohomologicalDimensionLE.natCard_H0_mul_natCard_H2_mul_pow, TauCeti.CohomologicalDimensionLE.natCard_H2_openSubgroup_mul_pow, TauCeti.IsProP.natCard_H2_openSubgroup_mul_pow
statement: formalized
proof: formalized
---

# The three-term Euler identity under `cd_p G ≤ 2`

For a topologically finitely generated
profinite pro-`p` group `G` with `cd_p G ≤ 2`, the trivial action on `𝔽_p`, and a finite discrete
`G`-module `M` of order `p ^ k`,
`|H⁰(G, M)| * |H²(G, M)| * p ^ (k * d(G)) = |H¹(G, M)| * p ^ k * |H²(G, 𝔽_p)| ^ k`.

```lean
TauCeti.CohomologicalDimensionLE.natCard_H0_mul_natCard_H2_mul_pow.{u} {p : ℕ}
  [hp : Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] [TotallyDisconnectedSpace G] [DistribMulAction G (ZMod p)]
  [ContinuousSMul G (ZMod p)] (hG : TauCeti.IsProP p G)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G) (htriv : ∀ (g : G) (x : ZMod p), g • x = x)
  (hcd : TauCeti.CohomologicalDimensionLE p G 2) (M : Type u) [AddCommGroup M] [TopologicalSpace M]
  [DiscreteTopology M] [DistribMulAction G M] [ContinuousSMul G M] {k : ℕ}
  (hk : Nat.card M = p ^ k) :
  Nat.card ↥(TauCeti.ContCohomology.H0 G M) * Nat.card (TauCeti.ContCohomology.H2 G M) *
      p ^ (k * TauCeti.topologicalGeneratorRankNat G hfg) =
    Nat.card (TauCeti.ContCohomology.H1 G M) * p ^ k *
      Nat.card (TauCeti.ContCohomology.H2 G (ZMod p)) ^ k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Burnside's basis theorem, cardinal form](../part-01/burnsides-basis-theorem-cardinal-form.md)
- [Shapiro's lemma in every degree](../../../representation-theory/homological/shapiros-lemma-in-every-degree.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CohomologicalDimensionLE.natCard_H0_mul_natCard_H2_mul_pow`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/ThreeTerm.html#TauCeti.CohomologicalDimensionLE.natCard_H0_mul_natCard_H2_mul_pow).

## Other forms

**The three-term Euler identity for an open subgroup under `cd_p G ≤ 2`.** Formalized in Tau Ceti as [`TauCeti.CohomologicalDimensionLE.natCard_H2_openSubgroup_mul_pow`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/ThreeTerm.html#TauCeti.CohomologicalDimensionLE.natCard_H2_openSubgroup_mul_pow).

```lean
TauCeti.CohomologicalDimensionLE.natCard_H2_openSubgroup_mul_pow.{u} {p : ℕ}
  [hp : Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] [TotallyDisconnectedSpace G] [DistribMulAction G (ZMod p)]
  [ContinuousSMul G (ZMod p)] (hG : TauCeti.IsProP p G)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G) (htriv : ∀ (g : G) (x : ZMod p), g • x = x)
  (hcd : TauCeti.CohomologicalDimensionLE p G 2) (U : OpenSubgroup G) :
  p * Nat.card (TauCeti.ContCohomology.H2 (↥↑U) (ZMod p)) *
      p ^ ((↑U).index * TauCeti.topologicalGeneratorRankNat G hfg) =
    p ^ TauCeti.topologicalGeneratorRankNat ↥↑U ⋯ * p ^ (↑U).index *
      Nat.card (TauCeti.ContCohomology.H2 G (ZMod p)) ^ (↑U).index
```

**The three-term Euler identity for the permutation module of an open subgroup, read through Shapiro's lemma.** Formalized in Tau Ceti as [`TauCeti.IsProP.natCard_H2_openSubgroup_mul_pow`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/ThreeTerm.html#TauCeti.IsProP.natCard_H2_openSubgroup_mul_pow).

```lean
TauCeti.IsProP.natCard_H2_openSubgroup_mul_pow.{u} {p : ℕ} [hp : Fact (Nat.Prime p)] {G : Type u}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] [DistribMulAction G (ZMod p)] [ContinuousSMul G (ZMod p)]
  (hG : TauCeti.IsProP p G) (hfg : TauCeti.IsTopologicallyFinitelyGenerated G)
  (htriv : ∀ (g : G) (x : ZMod p), g • x = x)
  (h3 :
    ∀ (A : Type u) [inst : AddCommGroup A] [inst_1 : TopologicalSpace A]
      [inst_2 : DiscreteTopology A] [inst_3 : DistribMulAction G A] [ContinuousSMul G A] [Finite A],
      Nat.card A = p →
        (∀ (g : G) (a : A), g • a = a) →
          Subsingleton ↑(continuousCohomology 3 (TauCeti.ofDiscreteModule ℤ G A)).toModuleCat)
  (U : OpenSubgroup G) :
  p * Nat.card (TauCeti.ContCohomology.H2 (↥↑U) (ZMod p)) *
      p ^ ((↑U).index * TauCeti.topologicalGeneratorRankNat G hfg) =
    p ^ TauCeti.topologicalGeneratorRankNat ↥↑U ⋯ * p ^ (↑U).index *
      Nat.card (TauCeti.ContCohomology.H2 G (ZMod p)) ^ (↑U).index
```

## Sources

- [Tau Ceti documentation: `TauCeti.CohomologicalDimensionLE.natCard_H0_mul_natCard_H2_mul_pow`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/ThreeTerm.html#TauCeti.CohomologicalDimensionLE.natCard_H0_mul_natCard_H2_mul_pow)
- [Source of `TauCeti.CohomologicalDimensionLE.natCard_H0_mul_natCard_H2_mul_pow` in TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/ThreeTerm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/ThreeTerm.lean#L297)
