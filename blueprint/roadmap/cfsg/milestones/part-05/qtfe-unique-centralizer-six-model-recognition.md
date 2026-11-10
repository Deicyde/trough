---
declaration: theorem
origin: cited
lean: CFSG.Milestones.qtfe_unique_centralizer_six_model_recognition
statement: formalized
proof: formalized
---

# QTFE_unique_centralizer_six_model_recognition

The milestone module `CFSG.Milestones.QTFE_unique_centralizer_six_model_recognition`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/QTFE_unique_centralizer_six_model_recognition.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QTFE_unique_centralizer_six_model_recognition.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.qtfe_unique_centralizer_six_model_recognition` (theorem, [line 637](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QTFE_unique_centralizer_six_model_recognition.lean#L637)). Proved here.

```lean
theorem qtfe_unique_centralizer_six_model_recognition
    (G : Type) [Group G] [Finite G] (T Mc : Subgroup G)
    (hQTFE : CFSG.Quasithin.quasithinQTFE14Cat G T Mc) :
    Nonempty (G ≃* NativeSporadic.J2) ∨
    Nonempty (G ≃* NativeSporadic.J3) ∨
    LieModel G .trialityD4 0 2 1 ∨
    LieModel G .Tits 0 2 1 ∨
    (∃ (k : Type) (_ : Field k) (_ : Finite k), Nat.card k = 2 ∧
      Nonempty (G ≃* ↥⁅adjointGroup .G2 k, adjointGroup .G2 k⁆)) ∨
    Nonempty (G ≃* NativeSporadic.M12)
```

No case theorem's file imports it, directly or through other files.

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

- [CFSG/Milestones/QTFE_unique_centralizer_six_model_recognition.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QTFE_unique_centralizer_six_model_recognition.lean)
