---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.finrank_cohomFp_zero_sub_finrank_cohomFp_one_add_finrank_cohomFp_two_openSubgroup, TauCeti.IsProP.one_sub_topologicalGeneratorRankNat_add_finrank_H2, TauCeti.CohomologicalDimensionLE.finrank_cohomFp_zero_sub_finrank_cohomFp_one_add_finrank_cohomFp_two_openSubgroup, TauCeti.CohomologicalDimensionLE.one_sub_topologicalGeneratorRankNat_add_finrank_H2
statement: formalized
proof: formalized
---

# The three-term Euler formula

Let `G` be a topologically finitely generated profinite
pro-`p` group whose canonical `H³` vanishes on the discrete modules of order `p` with trivial
action, with `H²(G, 𝔽_p)` finite, and let `U` be an open subgroup. Then, in `ℤ`,

```text
dim H⁰(U) - dim H¹(U) + dim H²(U) = [G : U] * (dim H⁰(G) - dim H¹(G) + dim H²(G)),
```

for the cohomology with trivial coefficients `𝔽_p`. The six spaces are finite-dimensional: `H⁰`
always, `H¹` because `G` and `U` are topologically finitely generated, and `H²(U, 𝔽_p)` by
`TauCeti.IsProP.finite_cohomFp_openSubgroup`.

```lean
TauCeti.IsProP.finrank_cohomFp_zero_sub_finrank_cohomFp_one_add_finrank_cohomFp_two_openSubgroup.{u}
  {p : ℕ} [hp : Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G)
  (h3 :
    ∀ (A : Type u) [inst : AddCommGroup A] [inst_1 : TopologicalSpace A]
      [inst_2 : DiscreteTopology A] [inst_3 : DistribMulAction G A] [ContinuousSMul G A] [Finite A],
      Nat.card A = p →
        (∀ (g : G) (a : A), g • a = a) →
          Subsingleton ↑(continuousCohomology 3 (TauCeti.ofDiscreteModule ℤ G A)).toModuleCat)
  [Finite ↑(TauCeti.cohomFp p G 2).toModuleCat] (U : OpenSubgroup G) :
  ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p (↥↑U) 0).toModuleCat) -
        ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p (↥↑U) 1).toModuleCat) +
      ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p (↥↑U) 2).toModuleCat) =
    ↑(↑U).index *
      (↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p G 0).toModuleCat) -
          ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p G 1).toModuleCat) +
        ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p G 2).toModuleCat))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Burnside's basis theorem, cardinal form](../part-01/burnsides-basis-theorem-cardinal-form.md)
- [Shapiro's lemma in every degree](../../../representation-theory/homological/shapiros-lemma-in-every-degree.md)
- [The three-term Euler identity under `cd_p G ≤ 2`](the-three-term-euler-identity-under-cd-p-g-2.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.finrank_cohomFp_zero_sub_finrank_cohomFp_one_add_finrank_cohomFp_two_openSubgroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/Finrank.html#TauCeti.IsProP.finrank_cohomFp_zero_sub_finrank_cohomFp_one_add_finrank_cohomFp_two_openSubgroup).

## Other forms

**The three-term Euler formula.** Formalized in Tau Ceti as [`TauCeti.IsProP.one_sub_topologicalGeneratorRankNat_add_finrank_H2`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/ThreeTerm.html#TauCeti.IsProP.one_sub_topologicalGeneratorRankNat_add_finrank_H2).

```lean
TauCeti.IsProP.one_sub_topologicalGeneratorRankNat_add_finrank_H2.{u} {p : ℕ}
  [hp : Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] [TotallyDisconnectedSpace G] [DistribMulAction G (ZMod p)]
  [ContinuousSMul G (ZMod p)] (hG : TauCeti.IsProP p G)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G) (htriv : ∀ (g : G) (x : ZMod p), g • x = x)
  (h3 :
    ∀ (A : Type u) [inst : AddCommGroup A] [inst_1 : TopologicalSpace A]
      [inst_2 : DiscreteTopology A] [inst_3 : DistribMulAction G A] [ContinuousSMul G A] [Finite A],
      Nat.card A = p →
        (∀ (g : G) (a : A), g • a = a) →
          Subsingleton ↑(continuousCohomology 3 (TauCeti.ofDiscreteModule ℤ G A)).toModuleCat)
  (U : OpenSubgroup G) [Finite (TauCeti.ContCohomology.H2 G (ZMod p))] :
  1 - ↑(TauCeti.topologicalGeneratorRankNat ↥↑U ⋯) +
      ↑(Module.finrank (ZMod p) (TauCeti.ContCohomology.H2 (↥↑U) (ZMod p))) =
    ↑(↑U).index *
      (1 - ↑(TauCeti.topologicalGeneratorRankNat G hfg) +
        ↑(Module.finrank (ZMod p) (TauCeti.ContCohomology.H2 G (ZMod p))))
```

**The three-term Euler formula under `cd_p G ≤ 2`.** Formalized in Tau Ceti as [`TauCeti.CohomologicalDimensionLE.finrank_cohomFp_zero_sub_finrank_cohomFp_one_add_finrank_cohomFp_two_openSubgroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/Finrank.html#TauCeti.CohomologicalDimensionLE.finrank_cohomFp_zero_sub_finrank_cohomFp_one_add_finrank_cohomFp_two_openSubgroup).

```lean
TauCeti.CohomologicalDimensionLE.finrank_cohomFp_zero_sub_finrank_cohomFp_one_add_finrank_cohomFp_two_openSubgroup.{u}
  {p : ℕ} [hp : Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G) (hcd : TauCeti.CohomologicalDimensionLE p G 2)
  [Finite ↑(TauCeti.cohomFp p G 2).toModuleCat] (U : OpenSubgroup G) :
  ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p (↥↑U) 0).toModuleCat) -
        ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p (↥↑U) 1).toModuleCat) +
      ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p (↥↑U) 2).toModuleCat) =
    ↑(↑U).index *
      (↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p G 0).toModuleCat) -
          ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p G 1).toModuleCat) +
        ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p G 2).toModuleCat))
```

**The three-term Euler formula under `cd_p G ≤ 2`.** Formalized in Tau Ceti as [`TauCeti.CohomologicalDimensionLE.one_sub_topologicalGeneratorRankNat_add_finrank_H2`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/ThreeTerm.html#TauCeti.CohomologicalDimensionLE.one_sub_topologicalGeneratorRankNat_add_finrank_H2).

```lean
TauCeti.CohomologicalDimensionLE.one_sub_topologicalGeneratorRankNat_add_finrank_H2.{u} {p : ℕ}
  [hp : Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] [TotallyDisconnectedSpace G] [DistribMulAction G (ZMod p)]
  [ContinuousSMul G (ZMod p)] (hG : TauCeti.IsProP p G)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G) (htriv : ∀ (g : G) (x : ZMod p), g • x = x)
  (hcd : TauCeti.CohomologicalDimensionLE p G 2) (U : OpenSubgroup G)
  [Finite (TauCeti.ContCohomology.H2 G (ZMod p))] :
  1 - ↑(TauCeti.topologicalGeneratorRankNat ↥↑U ⋯) +
      ↑(Module.finrank (ZMod p) (TauCeti.ContCohomology.H2 (↥↑U) (ZMod p))) =
    ↑(↑U).index *
      (1 - ↑(TauCeti.topologicalGeneratorRankNat G hfg) +
        ↑(Module.finrank (ZMod p) (TauCeti.ContCohomology.H2 G (ZMod p))))
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.finrank_cohomFp_zero_sub_finrank_cohomFp_one_add_finrank_cohomFp_two_openSubgroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/Finrank.html#TauCeti.IsProP.finrank_cohomFp_zero_sub_finrank_cohomFp_one_add_finrank_cohomFp_two_openSubgroup)
- [Source of `TauCeti.IsProP.finrank_cohomFp_zero_sub_finrank_cohomFp_one_add_finrank_cohomFp_two_openSubgroup` in TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/Finrank.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/Finrank.lean#L111)
