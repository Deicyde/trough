---
declaration: theorem
origin: cited
lean: CFSG.Milestones.qt_faithful_local_empty_classification
statement: formalized
proof: formalized
---

# QT_faithful_local_empty_classification

The milestone module `CFSG.Milestones.QT_faithful_local_empty_classification`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/QT_faithful_local_empty_classification.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_faithful_local_empty_classification.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.qt_faithful_local_empty_classification` (theorem, [line 638](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_faithful_local_empty_classification.lean#L638)). Proved here.

```lean
theorem qt_faithful_local_empty_classification
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hqtke : QuasithinUnique.quasithinIsQTKECat G)
    (T : Sylow 2 G)
    (hMT : ∃ M₁ M₂ : Subgroup G, M₁ ≠ M₂ ∧
      quasithinIsMaxTwoLocal M₁ ∧ quasithinIsMaxTwoLocal M₂ ∧
      (T : Subgroup G) ≤ M₁ ∧ (T : Subgroup G) ≤ M₂)
    (hLf : ∀ L : Subgroup G, ¬ quasithinIsFaithfulLocal (T : Subgroup G) L) :
    Blueprint.Catalog G
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CFSG.Assembly.disconnected_involution_graph](../../case-division/case-hdisc-disconnectedstatement.md)
- [AT_alternating_automorphism_permutation](../part-01/at-alternating-automorphism-permutation.md)
- [CLS_component_dichotomy](../part-01/cls-component-dichotomy.md)
- [CL_LIT_Fischer_3T_existence_uniqueness](../part-02/cl-lit-fischer-3t-existence-uniqueness.md)
- [CL_LIT_Goldschmidt_strongly_closed_abelian_models](../part-02/cl-lit-goldschmidt-strongly-closed-abelian-model.md)
- [CL_LIT_Griess_Schur_multipliers_Lie_type](../part-02/cl-lit-griess-schur-multipliers-lie-type.md)
- [CL_LIT_SQTK_simple_list](../part-02/cl-lit-sqtk-simple-list.md)
- [CT_catalog_nonabelian_type_partition](../part-03/ct-catalog-nonabelian-type-partition.md)
- [LR_Brauer_Suzuki_central_involution](lr-brauer-suzuki-central-involution.md)
- [LR_nonabelian_simple_two_rank_lower_bound](lr-nonabelian-simple-two-rank-lower-bound.md)
- [LR_wreathed_simple_recognition](lr-wreathed-simple-recognition.md)

## Sources

- [CFSG/Milestones/QT_faithful_local_empty_classification.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_faithful_local_empty_classification.lean)
