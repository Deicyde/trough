---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_goldschmidt_strongly_closed_abelian_models
statement: formalized
proof: formalized
---

# CL_LIT_Goldschmidt_strongly_closed_abelian_models

The milestone module `CFSG.Milestones.CL_LIT_Goldschmidt_strongly_closed_abelian_models`, which CFSG/Milestones.lean does not import.

It declares 1 result, quoted from [CFSG/Milestones/CL_LIT_Goldschmidt_strongly_closed_abelian_models.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Goldschmidt_strongly_closed_abelian_models.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_goldschmidt_strongly_closed_abelian_models` (theorem, [line 9](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Goldschmidt_strongly_closed_abelian_models.lean#L9)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_goldschmidt_strongly_closed_abelian_models
    (X : Type) [Group X] [Finite X]
    (S : Sylow 2 X) (A : Subgroup X) (hAS : A ≤ S) (hAab : IsMulCommutative A)
    (hclosed : ∀ a ∈ A, ∀ g : X, g⁻¹ * a * g ∈ (S : Subgroup X) → g⁻¹ * a * g ∈ A) :
    let M : Subgroup X := Subgroup.normalClosure (A : Set X)
    let π := QuotientGroup.mk' (goldschmidtOddCore M)
    let T := ((S : Subgroup X).subgroupOf M).map π ⊓ goldschmidtLayer (M ⧸ goldschmidtOddCore M)
    pCore 2 (M ⧸ goldschmidtOddCore M) ⊔ goldschmidtLayer (M ⧸ goldschmidtOddCore M) = ⊤ ∧
    (A.subgroupOf M).map π =
      pCore 2 (M ⧸ goldschmidtOddCore M) ⊔ Subgroup.closure {t | t ∈ T ∧ t ^ 2 = 1} ∧
    ∀ K : Subgroup (M ⧸ goldschmidtOddCore M), IsComponentOf K ⊤ →
      CFSG.Goldschmidt.SimpleModels (K ⧸ Subgroup.center K)
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CLS_component_free_involution_odd_cores_trivial](../part-01/cls-component-free-involution-odd-cores-trivial.md)
- [CL_LIT_Walter_abelian_Sylow_two_simple](../part-03/cl-lit-walter-abelian-sylow-two-simple.md)
- [CTGMS_Bender_1971_even_rank_one_model_and_strong_embedding_input](../part-03/ctgms-bender-1971-even-rank-one-model-and-strong.md)
- [LR_rank_two_isomorphism_types](../part-05/lr-rank-two-isomorphism-types.md)
- [QT_unique_Shult_simple_strongly_closed_TI_models](../part-06/qt-unique-shult-simple-strongly-closed-ti-models.md)

## Sources

- [CFSG/Milestones/CL_LIT_Goldschmidt_strongly_closed_abelian_models.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Goldschmidt_strongly_closed_abelian_models.lean)
