---
declaration: theorem
origin: cited
lean: CFSG.Assembly.large_even
statement: formalized
proof: formalized
---

# CFSG.Assembly.large_even

The case `hle : LargeEvenStatement` of [`CFSG.Assembly.classification`](reduction.md). What it asserts, defined in [CFSG/Assembly/Reduction.lean, line 46](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L46):

```lean
@[expose] def LargeEvenStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G] [IsSimpleGroup G], (∃ a b : G, a * b ≠ b * a) →
    KProper C G → IsCharTwoType G → 4 ≤ evenRank G → C G
```

The theorem the top theorem's proof gives for it, quoted from [CFSG/Assembly/LargeEven.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/LargeEven.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Assembly.large_even` (theorem, [line 3740](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/LargeEven.lean#L3740)). Proved here.

```lean
theorem large_even
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper InCatalog G) (hchar : IsCharTwoType G)
    (he : 4 ≤ evenRank G) : InCatalog G
```

Its file imports, directly or through other files, 59 milestone modules: [AT_alternating_automorphism_permutation](../milestones/part-01/at-alternating-automorphism-permutation.md), [CAT_native_realization](../milestones/part-01/cat-native-realization.md), [CLS_component_dichotomy](../milestones/part-01/cls-component-dichotomy.md), [CLS_component_free_centralizer_quotient_characteristic_two](../milestones/part-01/cls-component-free-centralizer-quotient-characte.md), [CLS_component_free_involution_odd_cores_trivial](../milestones/part-01/cls-component-free-involution-odd-cores-trivial.md), [CLS_connectivity_MacWilliams_four_generator](../milestones/part-01/cls-connectivity-macwilliams-four-generator.md), [CLS_involution_centralizers_characteristic_two_transfer](../milestones/part-01/cls-involution-centralizers-characteristic-two-t.md), [CL_LIT_Aschbacher_component_type_theorem_5](../milestones/part-02/cl-lit-aschbacher-component-type-theorem-5.md), [CL_LIT_Aschbacher_proper_two_generated_core](../milestones/part-02/cl-lit-aschbacher-proper-two-generated-core.md), [CL_LIT_Borel_Tits_local_parabolic](../milestones/part-02/cl-lit-borel-tits-local-parabolic.md), [CL_LIT_Curtis_Tits_presentation_theorem](../milestones/part-02/cl-lit-curtis-tits-presentation-theorem.md), [CL_LIT_Fischer_3T_existence_uniqueness](../milestones/part-02/cl-lit-fischer-3t-existence-uniqueness.md), [CL_LIT_Fischer_three_transposition_theorem](../milestones/part-02/cl-lit-fischer-three-transposition-theorem.md), [CL_LIT_GH74_sectional_two_rank_four](../milestones/part-02/cl-lit-gh74-sectional-two-rank-four.md), [CL_LIT_GMS_Monster_uniqueness](../milestones/part-02/cl-lit-gms-monster-uniqueness.md), [CL_LIT_Goldschmidt_strongly_closed_abelian](../milestones/part-02/cl-lit-goldschmidt-strongly-closed-abelian.md), [CL_LIT_Goldschmidt_strongly_closed_abelian_models](../milestones/part-02/cl-lit-goldschmidt-strongly-closed-abelian-model.md), [CL_LIT_Gorenstein_Walter_L_balance](../milestones/part-02/cl-lit-gorenstein-walter-l-balance.md), [CL_LIT_Griess_Schur_multipliers_Lie_type](../milestones/part-02/cl-lit-griess-schur-multipliers-lie-type.md), [CL_LIT_Monster_existence_Griess_Conway](../milestones/part-02/cl-lit-monster-existence-griess-conway.md), [CL_LIT_SQTK_simple_list](../milestones/part-02/cl-lit-sqtk-simple-list.md), [CL_LIT_SQTK_simple_listBase](../milestones/part-03/cl-lit-sqtk-simple-listbase.md), [CL_LIT_Stroth_Leon_Sims_Baby_Monster_recognition](../milestones/part-03/cl-lit-stroth-leon-sims-baby-monster-recognition.md), [CL_LIT_Timmesfeld_1978_large_extraspecial](../milestones/part-03/cl-lit-timmesfeld-1978-large-extraspecial.md), [CL_LIT_Walter_abelian_Sylow_two_simple](../milestones/part-03/cl-lit-walter-abelian-sylow-two-simple.md), [CL_LIT_classical_involution_theorem](../milestones/part-03/cl-lit-classical-involution-theorem.md), [CL_LIT_signalizer_functor_theorem](../milestones/part-03/cl-lit-signalizer-functor-theorem.md), [CTGMS_Bender_1971_even_rank_one_model_and_strong_embedding_input](../milestones/part-03/ctgms-bender-1971-even-rank-one-model-and-strong.md), [CT_catalog_nonabelian_type_partition](../milestones/part-03/ct-catalog-nonabelian-type-partition.md), [FAM_M_finiteness](../milestones/part-04/fam-m-finiteness.md), [FAM_M_simplicity](../milestones/part-04/fam-m-simplicity.md), [FAM_Th_simplicity](../milestones/part-04/fam-th-simplicity.md), [FAM_classical_model_membership](../milestones/part-04/fam-classical-model-membership.md), [FAM_sporadic_converse](../milestones/part-04/fam-sporadic-converse.md), [LC_GL_GF2_recognition_rank_four](../milestones/part-04/lc-gl-gf2-recognition-rank-four.md), [LC_GL_constructed_pretrichotomy_rank_four](../milestones/part-04/lc-gl-constructed-pretrichotomy-rank-four.md), [LC_GL_embedding_theorem_D1_rank_four](../milestones/part-04/lc-gl-embedding-theorem-d1-rank-four.md), [LC_GL_embedding_theorem_D2_rank_four](../milestones/part-04/lc-gl-embedding-theorem-d2-rank-four.md), [LC_GL_local_rank_bounds](../milestones/part-05/lc-gl-local-rank-bounds.md), [LC_GL_preuniqueness_exclusion_rank_four](../milestones/part-05/lc-gl-preuniqueness-exclusion-rank-four.md), [LC_GL_standard_type_recognition_rank_four](../milestones/part-05/lc-gl-standard-type-recognition-rank-four.md), [LC_GL_theorem_A](../milestones/part-05/lc-gl-theorem-a.md), [LC_GL_theorem_C_rank_four](../milestones/part-05/lc-gl-theorem-c-rank-four.md), [LC_GL_uniqueness_exclusion_rank_four](../milestones/part-05/lc-gl-uniqueness-exclusion-rank-four.md), [LC_generalized_fitting_self_centralizing](../milestones/part-05/lc-generalized-fitting-self-centralizing.md), [LR_Brauer_Suzuki_central_involution](../milestones/part-05/lr-brauer-suzuki-central-involution.md), [LR_Glauberman_Z_star_central_Sylow_involution](../milestones/part-05/lr-glauberman-z-star-central-sylow-involution.md), [LR_dihedral_simple_recognition](../milestones/part-05/lr-dihedral-simple-recognition.md), [LR_nonabelian_simple_two_rank_lower_bound](../milestones/part-05/lr-nonabelian-simple-two-rank-lower-bound.md), [LR_rank_two_isomorphism_types](../milestones/part-05/lr-rank-two-isomorphism-types.md), [LR_semidihedral_simple_recognition](../milestones/part-05/lr-semidihedral-simple-recognition.md), [LR_wreathed_simple_recognition](../milestones/part-05/lr-wreathed-simple-recognition.md), [OO_odd_order_solvable](../milestones/part-05/oo-odd-order-solvable.md), [QT_faithful_local_empty_classification](../milestones/part-05/qt-faithful-local-empty-classification.md), [QT_unique_Shult_simple_strongly_closed_TI_models](../milestones/part-06/qt-unique-shult-simple-strongly-closed-ti-models.md), [QT_unique_maximal_local_classification](../milestones/part-06/qt-unique-maximal-local-classification.md), [SE_simple_strong_embedding_models](../milestones/part-06/se-simple-strong-embedding-models.md), [SG_two_signalizer_completeness](../milestones/part-06/sg-two-signalizer-completeness.md), [ZJ_glauberman_characteristic](../milestones/part-06/zj-glauberman-characteristic.md).

## Depends on

- [LC_GL_GF2_recognition_rank_four](../milestones/part-04/lc-gl-gf2-recognition-rank-four.md)
- [LC_GL_constructed_pretrichotomy_rank_four](../milestones/part-04/lc-gl-constructed-pretrichotomy-rank-four.md)
- [LC_GL_preuniqueness_exclusion_rank_four](../milestones/part-05/lc-gl-preuniqueness-exclusion-rank-four.md)
- [LC_GL_standard_type_recognition_rank_four](../milestones/part-05/lc-gl-standard-type-recognition-rank-four.md)

## Sources

- [CFSG/Assembly/LargeEven.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/LargeEven.lean#L3740)
