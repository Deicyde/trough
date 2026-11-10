---
declaration: theorem
origin: cited
lean: CFSG.Milestones.qt_unique_shult_simple_strongly_closed_ti_models
statement: formalized
proof: formalized
---

# QT_unique_Shult_simple_strongly_closed_TI_models

The milestone module `CFSG.Milestones.QT_unique_Shult_simple_strongly_closed_TI_models`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/QT_unique_Shult_simple_strongly_closed_TI_models.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_unique_Shult_simple_strongly_closed_TI_models.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.qt_unique_shult_simple_strongly_closed_ti_models` (theorem, [line 13](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_unique_Shult_simple_strongly_closed_TI_models.lean#L13)). Proved here.

```lean
theorem _root_.CFSG.Milestones.qt_unique_shult_simple_strongly_closed_ti_models
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (T : Sylow 2 G) (U : Subgroup G) (hUT : U ≤ (T : Subgroup G)) (hU : U ≠ ⊥)
    (hUel : IsElemAbelian 2 U)
    (hclosed : fusionStronglyClosed (U : Set G) (T : Subgroup G))
    (hTI : fusionIsTI U) :
    fusionIsBenderGroup G
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CFSG.FeitThompson.isSolvable_of_odd_natCard](../../case-division/case-hodd-oddorderstatement.md)
- [CLS_connectivity_MacWilliams_four_generator](../part-01/cls-connectivity-macwilliams-four-generator.md)
- [FAM_classical_model_membership](../part-04/fam-classical-model-membership.md)
- [LR_Glauberman_Z_star_central_Sylow_involution](../part-05/lr-glauberman-z-star-central-sylow-involution.md)

## Sources

- [CFSG/Milestones/QT_unique_Shult_simple_strongly_closed_TI_models.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_unique_Shult_simple_strongly_closed_TI_models.lean)
