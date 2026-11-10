---
declaration: theorem
origin: cited
lean: CFSG.Milestones.ctss_sporadic_standard_centerless_m12_j2_and_other_quotients_frontier, CFSG.Milestones.ctss_sporadic_standard_centerless_m12_j2_and_other_quotients_frontier_models
statement: formalized
proof: formalized
---

# CTSS_sporadic_standard_centerless_M12_J2_and_other_quotients_frontier

The milestone module `CFSG.Milestones.CTSS_sporadic_standard_centerless_M12_J2_and_other_quotients_frontier`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CTSS_sporadic_standard_centerless_M12_J2_and_other_quotients_frontier.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTSS_sporadic_standard_centerless_M12_J2_and_other_quotients_frontier.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.ctss_sporadic_standard_centerless_m12_j2_and_other_quotients_frontier` (theorem, [line 3286](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTSS_sporadic_standard_centerless_M12_J2_and_other_quotients_frontier.lean#L3286)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ctss_sporadic_standard_centerless_m12_j2_and_other_quotients_frontier
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : CFSG.Assembly.KProper CFSG.Blueprint.Catalog G)
    (L : Subgroup G) (hL : standardComponentIsStandard L)
    (hcore : ∀ t : G, orderOf t = 2 →
      standardComponentOddCore (Subgroup.centralizer ({t} : Set G)) = ⊥)
    (S : Sylow 2 (Subgroup.centralizer (L : Set G)))
    (hS : IsCyclic (S : Subgroup (Subgroup.centralizer (L : Set G))))
    (htype : Blueprint.Recognition.Exact.EvenStandardType (L ⧸ Subgroup.center L))
    (hexc : ¬ Blueprint.Recognition.Exact.EvenStandardException (L ⧸ Subgroup.center L))
    (hres : Blueprint.Recognition.Exact.EvenStandardResidual L)
    (hspor : Blueprint.NativeSporadic.SporadicRep (L ⧸ Subgroup.center L))
    (hMJ : Blueprint.NativeSporadic.IsSporadic (L ⧸ Subgroup.center L) .M12 ∨
      Blueprint.NativeSporadic.IsSporadic (L ⧸ Subgroup.center L) .J2 → Subgroup.center L = ⊥) :
    Nat.card G ∈ standardComponentEvenSporadicOrders
```

`CFSG.Milestones.ctss_sporadic_standard_centerless_m12_j2_and_other_quotients_frontier_models` (theorem, [line 3328](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTSS_sporadic_standard_centerless_M12_J2_and_other_quotients_frontier.lean#L3328)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ctss_sporadic_standard_centerless_m12_j2_and_other_quotients_frontier_models
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : CFSG.Assembly.KProper CFSG.Blueprint.Catalog G)
    (L : Subgroup G) (hL : standardComponentIsStandard L)
    (hcore : ∀ t : G, orderOf t = 2 →
      standardComponentOddCore (Subgroup.centralizer ({t} : Set G)) = ⊥)
    (S : Sylow 2 (Subgroup.centralizer (L : Set G)))
    (hS : IsCyclic (S : Subgroup (Subgroup.centralizer (L : Set G))))
    (htype : Blueprint.Recognition.Exact.EvenStandardType (L ⧸ Subgroup.center L))
    (hexc : ¬ Blueprint.Recognition.Exact.EvenStandardException (L ⧸ Subgroup.center L))
    (hres : Blueprint.Recognition.Exact.EvenStandardResidual L)
    (hspor : Blueprint.NativeSporadic.SporadicRep (L ⧸ Subgroup.center L))
    (hMJ : Blueprint.NativeSporadic.IsSporadic (L ⧸ Subgroup.center L) .M12 ∨
      Blueprint.NativeSporadic.IsSporadic (L ⧸ Subgroup.center L) .J2 → Subgroup.center L = ⊥) :
    Blueprint.Recognition.EvenSporadicOutcome G
```

The files of 2 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [CL_LIT_Curtis_Tits_presentation_theorem](../part-02/cl-lit-curtis-tits-presentation-theorem.md)
- [CL_LIT_Fischer_three_transposition_theorem](../part-02/cl-lit-fischer-three-transposition-theorem.md)
- [CL_LIT_GMS_Monster_uniqueness](../part-02/cl-lit-gms-monster-uniqueness.md)
- [CL_LIT_Monster_existence_Griess_Conway](../part-02/cl-lit-monster-existence-griess-conway.md)
- [CL_LIT_classical_involution_theorem](cl-lit-classical-involution-theorem.md)
- [CT_even_small_Lie_standard_frontier](ct-even-small-lie-standard-frontier.md)
- [CT_even_standard_residual_reduction](ct-even-standard-residual-reduction.md)
- [FAM_sporadic_converse](../part-04/fam-sporadic-converse.md)

## Sources

- [CFSG/Milestones/CTSS_sporadic_standard_centerless_M12_J2_and_other_quotients_frontier.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CTSS_sporadic_standard_centerless_M12_J2_and_other_quotients_frontier.lean)
