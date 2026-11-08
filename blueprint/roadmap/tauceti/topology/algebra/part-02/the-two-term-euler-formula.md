---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.finrank_cohomFp_zero_sub_finrank_cohomFp_one_openSubgroup, TauCeti.IsProP.topologicalGeneratorRankNat_add_index, TauCeti.CohomologicalDimensionLE.finrank_cohomFp_zero_sub_finrank_cohomFp_one_openSubgroup, TauCeti.CohomologicalDimensionLE.topologicalGeneratorRankNat_add_index, TauCeti.CohomologicalDimensionLE.one_sub_topologicalGeneratorRankNat_eq, TauCeti.IsProP.one_sub_topologicalGeneratorRankNat_eq
statement: formalized
proof: formalized
---

# The two-term Euler formula

Let `G` be a topologically finitely generated profinite pro-`p`
group whose explicit `H²` vanishes on the discrete modules of order `p` with trivial action, and
let `U` be an open subgroup. Then, in `ℤ`,

```text
dim H⁰(U, 𝔽_p) - dim H¹(U, 𝔽_p) = [G : U] * (dim H⁰(G, 𝔽_p) - dim H¹(G, 𝔽_p)).
```

The four spaces are finite-dimensional: `H⁰` always, and `H¹` because `G` and `U` are
topologically finitely generated (`TauCeti.IsProP.finite_cohomFp_one_iff`).

```lean
TauCeti.IsProP.finrank_cohomFp_zero_sub_finrank_cohomFp_one_openSubgroup.{u} {p : ℕ}
  [hp : Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G)
  (h2 :
    ∀ (A : Type u) [inst : AddCommGroup A] [inst_1 : TopologicalSpace A]
      [inst_2 : DiscreteTopology A] [inst_3 : DistribMulAction G A] [inst_4 : ContinuousSMul G A]
      [Finite A],
      Nat.card A = p →
        (∀ (g : G) (a : A), g • a = a) → Subsingleton (TauCeti.ContCohomology.H2 G A))
  (U : OpenSubgroup G) :
  ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p (↥↑U) 0).toModuleCat) -
      ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p (↥↑U) 1).toModuleCat) =
    ↑(↑U).index *
      (↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p G 0).toModuleCat) -
        ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p G 1).toModuleCat))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Burnside's basis theorem, cardinal form](../part-01/burnsides-basis-theorem-cardinal-form.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.finrank_cohomFp_zero_sub_finrank_cohomFp_one_openSubgroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/Finrank.html#TauCeti.IsProP.finrank_cohomFp_zero_sub_finrank_cohomFp_one_openSubgroup).

## Other forms

**The two-term Euler formula.** Formalized in Tau Ceti as [`TauCeti.IsProP.topologicalGeneratorRankNat_add_index`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/Basic.html#TauCeti.IsProP.topologicalGeneratorRankNat_add_index).

```lean
TauCeti.IsProP.topologicalGeneratorRankNat_add_index.{u} {p : ℕ} [hp : Fact (Nat.Prime p)]
  {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G)
  (h2 :
    ∀ (A : Type u) [inst : AddCommGroup A] [inst_1 : TopologicalSpace A]
      [inst_2 : DiscreteTopology A] [inst_3 : DistribMulAction G A] [inst_4 : ContinuousSMul G A]
      [Finite A],
      Nat.card A = p →
        (∀ (g : G) (a : A), g • a = a) → Subsingleton (TauCeti.ContCohomology.H2 G A))
  (U : OpenSubgroup G) :
  TauCeti.topologicalGeneratorRankNat ↥↑U ⋯ + (↑U).index =
    1 + (↑U).index * TauCeti.topologicalGeneratorRankNat G hfg
```

**The two-term Euler formula under `cd_p G ≤ 1`.** Formalized in Tau Ceti as [`TauCeti.CohomologicalDimensionLE.finrank_cohomFp_zero_sub_finrank_cohomFp_one_openSubgroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/Finrank.html#TauCeti.CohomologicalDimensionLE.finrank_cohomFp_zero_sub_finrank_cohomFp_one_openSubgroup).

```lean
TauCeti.CohomologicalDimensionLE.finrank_cohomFp_zero_sub_finrank_cohomFp_one_openSubgroup.{u}
  {p : ℕ} [hp : Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G) (hcd : TauCeti.CohomologicalDimensionLE p G 1)
  (U : OpenSubgroup G) :
  ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p (↥↑U) 0).toModuleCat) -
      ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p (↥↑U) 1).toModuleCat) =
    ↑(↑U).index *
      (↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p G 0).toModuleCat) -
        ↑(Module.finrank (ZMod p) ↑(TauCeti.cohomFp p G 1).toModuleCat))
```

**The two-term Euler formula under `cd_p G ≤ 1`.** Formalized in Tau Ceti as [`TauCeti.CohomologicalDimensionLE.topologicalGeneratorRankNat_add_index`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/Basic.html#TauCeti.CohomologicalDimensionLE.topologicalGeneratorRankNat_add_index).

```lean
TauCeti.CohomologicalDimensionLE.topologicalGeneratorRankNat_add_index.{u} {p : ℕ}
  [hp : Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G) (hcd : TauCeti.CohomologicalDimensionLE p G 1)
  (U : OpenSubgroup G) :
  TauCeti.topologicalGeneratorRankNat ↥↑U ⋯ + (↑U).index =
    1 + (↑U).index * TauCeti.topologicalGeneratorRankNat G hfg
```

**The two-term Euler formula under `cd_p G ≤ 1`, in `ℤ`.** Formalized in Tau Ceti as [`TauCeti.CohomologicalDimensionLE.one_sub_topologicalGeneratorRankNat_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/Basic.html#TauCeti.CohomologicalDimensionLE.one_sub_topologicalGeneratorRankNat_eq).

```lean
TauCeti.CohomologicalDimensionLE.one_sub_topologicalGeneratorRankNat_eq.{u} {p : ℕ}
  [hp : Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G) (hcd : TauCeti.CohomologicalDimensionLE p G 1)
  (U : OpenSubgroup G) :
  1 - ↑(TauCeti.topologicalGeneratorRankNat ↥↑U ⋯) =
    ↑(↑U).index * (1 - ↑(TauCeti.topologicalGeneratorRankNat G hfg))
```

**The two-term Euler formula, in `ℤ`.** Formalized in Tau Ceti as [`TauCeti.IsProP.one_sub_topologicalGeneratorRankNat_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/Basic.html#TauCeti.IsProP.one_sub_topologicalGeneratorRankNat_eq).

```lean
TauCeti.IsProP.one_sub_topologicalGeneratorRankNat_eq.{u} {p : ℕ} [hp : Fact (Nat.Prime p)]
  {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G)
  (h2 :
    ∀ (A : Type u) [inst : AddCommGroup A] [inst_1 : TopologicalSpace A]
      [inst_2 : DiscreteTopology A] [inst_3 : DistribMulAction G A] [inst_4 : ContinuousSMul G A]
      [Finite A],
      Nat.card A = p →
        (∀ (g : G) (a : A), g • a = a) → Subsingleton (TauCeti.ContCohomology.H2 G A))
  (U : OpenSubgroup G) :
  1 - ↑(TauCeti.topologicalGeneratorRankNat ↥↑U ⋯) =
    ↑(↑U).index * (1 - ↑(TauCeti.topologicalGeneratorRankNat G hfg))
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.finrank_cohomFp_zero_sub_finrank_cohomFp_one_openSubgroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/Finrank.html#TauCeti.IsProP.finrank_cohomFp_zero_sub_finrank_cohomFp_one_openSubgroup)
- [Source of `TauCeti.IsProP.finrank_cohomFp_zero_sub_finrank_cohomFp_one_openSubgroup` in TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/Finrank.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ProP/EulerCharacteristic/Finrank.lean#L78)
