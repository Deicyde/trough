---
declaration: theorem
origin: cited
lean: CFSG.Milestones.ct_rank_two_standard_recognition_frontier, CFSG.Milestones.ct_rank_two_standard_recognition_frontier_models
statement: formalized
proof: formalized
---

# CT_rank_two_standard_recognition_frontier

The milestone module `CFSG.Milestones.CT_rank_two_standard_recognition_frontier`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CT_rank_two_standard_recognition_frontier.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_rank_two_standard_recognition_frontier.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.ct_rank_two_standard_recognition_frontier` (theorem, [line 917](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_rank_two_standard_recognition_frontier.lean#L917)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ct_rank_two_standard_recognition_frontier
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : CFSG.Assembly.KProper CFSG.Blueprint.Catalog G)
    (L : Subgroup G) (hL : standardComponentIsStandard L)
    (hrank : 2 ≤ pRank 2 (Subgroup.centralizer (L : Set G))) :
    (∃ n : ℕ, 9 ≤ n ∧ Nonempty (G ≃* alternatingGroup (Fin n))) ∨
      Nat.card G ∈ standardComponentRankTwoSporadicOrders
```

`CFSG.Milestones.ct_rank_two_standard_recognition_frontier_models` (theorem, [line 932](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_rank_two_standard_recognition_frontier.lean#L932)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ct_rank_two_standard_recognition_frontier_models
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : CFSG.Assembly.KProper CFSG.Blueprint.Catalog G)
    (L : Subgroup G) (hL : standardComponentIsStandard L)
    (hrank : 2 ≤ pRank 2 (Subgroup.centralizer (L : Set G))) :
    (∃ n : ℕ, 9 ≤ n ∧ Nonempty (G ≃* alternatingGroup (Fin n))) ∨
      (Blueprint.NativeSporadic.IsSporadic G .J2 ∨ Blueprint.NativeSporadic.IsSporadic G .Suz ∨
        Blueprint.NativeSporadic.IsSporadic G .He ∨ Blueprint.NativeSporadic.IsSporadic G .Ru ∨
        Blueprint.NativeSporadic.IsSporadic G .Co1)
```

The files of 2 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [AT_alternating_automorphism_permutation](../part-01/at-alternating-automorphism-permutation.md)
- [CL_LIT_Fischer_three_transposition_theorem](../part-02/cl-lit-fischer-three-transposition-theorem.md)
- [CL_LIT_Goldschmidt_strongly_closed_abelian_models](../part-02/cl-lit-goldschmidt-strongly-closed-abelian-model.md)
- [CL_LIT_Griess_Schur_multipliers_Lie_type](../part-02/cl-lit-griess-schur-multipliers-lie-type.md)
- [CL_LIT_SQTK_simple_list](../part-02/cl-lit-sqtk-simple-list.md)
- [CT_catalog_nonabelian_type_partition](ct-catalog-nonabelian-type-partition.md)
- [FAM_Th_simplicity](../part-04/fam-th-simplicity.md)
- [LR_nonabelian_simple_two_rank_lower_bound](../part-05/lr-nonabelian-simple-two-rank-lower-bound.md)
- [LR_semidihedral_simple_recognition](../part-05/lr-semidihedral-simple-recognition.md)

## Sources

- [CFSG/Milestones/CT_rank_two_standard_recognition_frontier.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_rank_two_standard_recognition_frontier.lean)
