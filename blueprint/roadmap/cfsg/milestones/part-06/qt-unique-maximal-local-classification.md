---
declaration: theorem
origin: cited
lean: CFSG.Milestones.qt_unique_maximal_local_classification
statement: formalized
proof: formalized
---

# QT_unique_maximal_local_classification

The milestone module `CFSG.Milestones.QT_unique_maximal_local_classification`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/QT_unique_maximal_local_classification.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_unique_maximal_local_classification.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.qt_unique_maximal_local_classification` (theorem, [line 415](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_unique_maximal_local_classification.lean#L415)). Proved here.

```lean
theorem qt_unique_maximal_local_classification
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hqtke : QuasithinUnique.quasithinIsQTKECat G)
    (T : Sylow 2 G)
    (hT : ∃! M : Subgroup G, quasithinIsMaxTwoLocal M ∧ (T : Subgroup G) ≤ M) :
    Blueprint.Catalog G
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [AT_alternating_automorphism_permutation](../part-01/at-alternating-automorphism-permutation.md)
- [CLS_component_free_centralizer_quotient_characteristic_two](../part-01/cls-component-free-centralizer-quotient-characte.md)
- [CL_LIT_SQTK_simple_list](../part-02/cl-lit-sqtk-simple-list.md)
- [CTGMS_Bender_1971_even_rank_one_model_and_strong_embedding_input](../part-03/ctgms-bender-1971-even-rank-one-model-and-strong.md)
- [CT_catalog_nonabelian_type_partition](../part-03/ct-catalog-nonabelian-type-partition.md)
- [LR_nonabelian_simple_two_rank_lower_bound](../part-05/lr-nonabelian-simple-two-rank-lower-bound.md)
- [QT_unique_Shult_simple_strongly_closed_TI_models](qt-unique-shult-simple-strongly-closed-ti-models.md)

## Sources

- [CFSG/Milestones/QT_unique_maximal_local_classification.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_unique_maximal_local_classification.lean)
