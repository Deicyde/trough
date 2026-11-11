---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.topologicalGeneratorRank_eq_rank_continuousZModDual, TauCeti.IsProP.rank_H1_eq_topologicalGeneratorRank, TauCeti.IsProP.finrank_H1_eq_topologicalGeneratorRankNat, TauCeti.IsProP.topologicalClosure_normalClosure_eq_iff_quotient_pLowerCentralStep, TauCeti.topologicalGeneratorRank_le_rank_continuousZModDual, TauCeti.topologicallyGenerates_iff_frattiniQuotient_span_topologicalClosure_eq_top, TauCeti.topologicallyGenerates_iff_frattiniQuotient, TauCeti.IsProP.finrank_continuousZModDual_eq_topologicalGeneratorRankNat, TauCeti.topologicallyGenerates_iff_frattiniQuotient_span_eq_top
statement: formalized
proof: formalized
---

# Burnside's basis theorem, cardinal form

The topological generator rank of a profinite
pro-`p` group is the dimension of its continuous `𝔽_p`-dual over `𝔽_p`. No finiteness hypothesis is
needed, and the statement is an identity of cardinals.

```lean
TauCeti.IsProP.topologicalGeneratorRank_eq_rank_continuousZModDual.{u} {p : ℕ}
  [hp : Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G) :
  TauCeti.topologicalGeneratorRank G = Module.rank (ZMod p) (TauCeti.continuousZModDual p G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Nakayama's lemma for pro-`p` groups](nakayamas-lemma-for-pro-p-groups.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.topologicalGeneratorRank_eq_rank_continuousZModDual`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/DualRank.html#TauCeti.IsProP.topologicalGeneratorRank_eq_rank_continuousZModDual).

## Other forms

**Burnside's basis theorem for `H¹`, cardinal form.** Formalized in Tau Ceti as [`TauCeti.IsProP.rank_H1_eq_topologicalGeneratorRank`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/H1Dual.html#TauCeti.IsProP.rank_H1_eq_topologicalGeneratorRank).

```lean
TauCeti.IsProP.rank_H1_eq_topologicalGeneratorRank.{u} {p : ℕ} [Fact (Nat.Prime p)] {G : Type u}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] [DistribMulAction G (ZMod p)] [ContinuousSMul G (ZMod p)]
  (hG : TauCeti.IsProP p G) (htriv : ∀ (g : G) (m : ZMod p), g • m = m) :
  Module.rank (ZMod p) (TauCeti.ContCohomology.H1 G (ZMod p)) = TauCeti.topologicalGeneratorRank G
```

**Burnside's basis theorem for `H¹`, numerical form.** Formalized in Tau Ceti as [`TauCeti.IsProP.finrank_H1_eq_topologicalGeneratorRankNat`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/H1Dual.html#TauCeti.IsProP.finrank_H1_eq_topologicalGeneratorRankNat).

```lean
TauCeti.IsProP.finrank_H1_eq_topologicalGeneratorRankNat.{u} {p : ℕ} [Fact (Nat.Prime p)]
  {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] [DistribMulAction G (ZMod p)] [ContinuousSMul G (ZMod p)]
  (hG : TauCeti.IsProP p G) (htriv : ∀ (g : G) (m : ZMod p), g • m = m)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G) :
  Module.finrank (ZMod p) (TauCeti.ContCohomology.H1 G (ZMod p)) =
    TauCeti.topologicalGeneratorRankNat G hfg
```

**Burnside's basis theorem for normal generation.** Formalized in Tau Ceti as [`TauCeti.IsProP.topologicalClosure_normalClosure_eq_iff_quotient_pLowerCentralStep`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/NormalGeneration.html#TauCeti.IsProP.topologicalClosure_normalClosure_eq_iff_quotient_pLowerCentralStep).

```lean
TauCeti.IsProP.topologicalClosure_normalClosure_eq_iff_quotient_pLowerCentralStep.{u} {p : ℕ}
  {F : Type u} [Group F] [TopologicalSpace F] [IsTopologicalGroup F] [CompactSpace F]
  [TotallyDisconnectedSpace F] (hF : TauCeti.IsProP p F) (hp : Nat.Prime p) {R : Subgroup F}
  [R.Normal] (hR : IsClosed ↑R) (s : Set ↥R) :
  (Subgroup.normalClosure (Subtype.val '' s)).topologicalClosure = R ↔
    (Subgroup.closure
          (⇑(QuotientGroup.mk' ((TauCeti.pLowerCentralStep p R).subgroupOf R)) ''
            s)).topologicalClosure =
      ⊤
```

**Burnside's basis theorem, cardinal form: the lower bound.** Formalized in Tau Ceti as [`TauCeti.topologicalGeneratorRank_le_rank_continuousZModDual`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/DualRank.html#TauCeti.topologicalGeneratorRank_le_rank_continuousZModDual).

```lean
TauCeti.topologicalGeneratorRank_le_rank_continuousZModDual.{u} {p : ℕ} [hp : Fact (Nat.Prime p)]
  {W : Type u} [CommGroup W] [TopologicalSpace W] [IsTopologicalGroup W] [CompactSpace W]
  [TotallyDisconnectedSpace W] [hW : _root_.Module (ZMod p) (Additive W)] :
  TauCeti.topologicalGeneratorRank W ≤ Module.rank (ZMod p) (TauCeti.continuousZModDual p W)
```

**Burnside's basis theorem, dense spanning form.** Formalized in Tau Ceti as [`TauCeti.topologicallyGenerates_iff_frattiniQuotient_span_topologicalClosure_eq_top`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/Basis.html#TauCeti.topologicallyGenerates_iff_frattiniQuotient_span_topologicalClosure_eq_top).

```lean
TauCeti.topologicallyGenerates_iff_frattiniQuotient_span_topologicalClosure_eq_top.{u_1} {p : ℕ}
  [Fact (Nat.Prime p)] {G : Type u_1} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G) (s : Set G) :
  (Subgroup.closure s).topologicalClosure = ⊤ ↔
    (Submodule.span (ZMod p)
            ((fun g => Additive.ofMul ((QuotientGroup.mk' (TauCeti.proPFrattini p G)) g)) ''
              s)).toAddSubgroup.topologicalClosure =
      ⊤
```

**Burnside's basis theorem, generation form.** Formalized in Tau Ceti as [`TauCeti.topologicallyGenerates_iff_frattiniQuotient`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/Burnside.html#TauCeti.topologicallyGenerates_iff_frattiniQuotient).

```lean
TauCeti.topologicallyGenerates_iff_frattiniQuotient.{u} {p : ℕ} [hp : Fact (Nat.Prime p)]
  {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G) (s : Set G) :
  (Subgroup.closure s).topologicalClosure = ⊤ ↔
    (Subgroup.closure (⇑(QuotientGroup.mk' (TauCeti.proPFrattini p G)) '' s)).topologicalClosure = ⊤
```

**Burnside's basis theorem, numerical form against the dual.** Formalized in Tau Ceti as [`TauCeti.IsProP.finrank_continuousZModDual_eq_topologicalGeneratorRankNat`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/DualRank.html#TauCeti.IsProP.finrank_continuousZModDual_eq_topologicalGeneratorRankNat).

```lean
TauCeti.IsProP.finrank_continuousZModDual_eq_topologicalGeneratorRankNat.{u} {p : ℕ}
  [hp : Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G) :
  Module.finrank (ZMod p) (TauCeti.continuousZModDual p G) =
    TauCeti.topologicalGeneratorRankNat G hfg
```

**Burnside's basis theorem, spanning form.** Formalized in Tau Ceti as [`TauCeti.topologicallyGenerates_iff_frattiniQuotient_span_eq_top`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/Basis.html#TauCeti.topologicallyGenerates_iff_frattiniQuotient_span_eq_top).

```lean
TauCeti.topologicallyGenerates_iff_frattiniQuotient_span_eq_top.{u_1} {p : ℕ} [Fact (Nat.Prime p)]
  {G : Type u_1} [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] [Finite (G ⧸ TauCeti.proPFrattini p G)] (hG : TauCeti.IsProP p G)
  (s : Set G) :
  (Subgroup.closure s).topologicalClosure = ⊤ ↔
    Submodule.span (ZMod p)
        ((fun g => Additive.ofMul ((QuotientGroup.mk' (TauCeti.proPFrattini p G)) g)) '' s) =
      ⊤
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.topologicalGeneratorRank_eq_rank_continuousZModDual`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/DualRank.html#TauCeti.IsProP.topologicalGeneratorRank_eq_rank_continuousZModDual)
- [Source of `TauCeti.IsProP.topologicalGeneratorRank_eq_rank_continuousZModDual` in TauCeti/Topology/Algebra/Group/Profinite/ProP/DualRank.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/ProP/DualRank.lean#L242)
