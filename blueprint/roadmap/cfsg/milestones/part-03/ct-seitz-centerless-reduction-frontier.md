---
declaration: theorem
origin: cited
lean: CFSG.Milestones.ct_seitz_centerless_reduction_frontier
statement: formalized
proof: formalized
---

# CT_Seitz_centerless_reduction_frontier

The milestone module `CFSG.Milestones.CT_Seitz_centerless_reduction_frontier`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CT_Seitz_centerless_reduction_frontier.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_Seitz_centerless_reduction_frontier.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.ct_seitz_centerless_reduction_frontier` (theorem, [line 15](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_Seitz_centerless_reduction_frontier.lean#L15)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ct_seitz_centerless_reduction_frontier
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
    (hZ : Subgroup.center L = ⊥) :
    Blueprint.NativeSporadic.SporadicRep L ∨ Blueprint.Recognition.Exact.EvenBNRankTwoType L ∨
      (Blueprint.LieModel L .PSp 3 2 1 ∨ Blueprint.LieModel L .PSU 6 2 1 ∨
        Blueprint.LieModel L .POmegaMinus 4 2 1 ∨ Blueprint.LieModel L .POmegaPlus 4 2 1)
```

The files of 2 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [CLS_involution_centralizers_characteristic_two_transfer](../part-01/cls-involution-centralizers-characteristic-two-t.md)
- [CL_LIT_Goldschmidt_strongly_closed_abelian_models](../part-02/cl-lit-goldschmidt-strongly-closed-abelian-model.md)
- [CL_LIT_Griess_Schur_multipliers_Lie_type](../part-02/cl-lit-griess-schur-multipliers-lie-type.md)
- [CL_LIT_SQTK_simple_list](../part-02/cl-lit-sqtk-simple-list.md)
- [CT_catalog_nonabelian_type_partition](ct-catalog-nonabelian-type-partition.md)
- [FAM_M_finiteness](../part-04/fam-m-finiteness.md)
- [FAM_M_simplicity](../part-04/fam-m-simplicity.md)
- [LR_nonabelian_simple_two_rank_lower_bound](../part-05/lr-nonabelian-simple-two-rank-lower-bound.md)

## Sources

- [CFSG/Milestones/CT_Seitz_centerless_reduction_frontier.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_Seitz_centerless_reduction_frontier.lean)
