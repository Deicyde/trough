---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_gorenstein_walter_l_balance
statement: formalized
proof: formalized
---

# CL_LIT_Gorenstein_Walter_L_balance

The milestone module `CFSG.Milestones.CL_LIT_Gorenstein_Walter_L_balance`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CL_LIT_Gorenstein_Walter_L_balance.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Gorenstein_Walter_L_balance.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_gorenstein_walter_l_balance` (theorem, [line 11](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Gorenstein_Walter_L_balance.lean#L11)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_gorenstein_walter_l_balance
    (X : Type) [Group X] [Finite X] (hK : lBalanceIsKGroup X)
    (p : ℕ) (hp : p.Prime) (P : Subgroup X) (hP : IsPGroup p P) :
    lBalancePLayer p (Subgroup.normalizer (P : Set X)) ≤ lBalancePLayer p ⊤ ∧
    lBalancePLayer p (Subgroup.centralizer (P : Set X)) ≤ lBalancePLayer p ⊤ ∧
    (lBalancePrimeCore p (⊤ : Subgroup X) = ⊥ →
      ∀ a ∈ lBalancePLayer p (Subgroup.normalizer (P : Set X)),
        ∀ b ∈ lBalancePrimeCore p (Subgroup.normalizer (P : Set X)), a * b = b * a)
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CFSG.Assembly.disconnected_involution_graph](../../case-division/case-hdisc-disconnectedstatement.md)
- [CLS_component_dichotomy](../part-01/cls-component-dichotomy.md)
- [CL_LIT_Curtis_Tits_presentation_theorem](cl-lit-curtis-tits-presentation-theorem.md)
- [CL_LIT_Fischer_three_transposition_theorem](cl-lit-fischer-three-transposition-theorem.md)
- [CL_LIT_GMS_Monster_uniqueness](cl-lit-gms-monster-uniqueness.md)
- [CL_LIT_Goldschmidt_strongly_closed_abelian_models](cl-lit-goldschmidt-strongly-closed-abelian-model.md)
- [CL_LIT_Griess_Schur_multipliers_Lie_type](cl-lit-griess-schur-multipliers-lie-type.md)
- [CL_LIT_Monster_existence_Griess_Conway](cl-lit-monster-existence-griess-conway.md)
- [CL_LIT_signalizer_functor_theorem](../part-03/cl-lit-signalizer-functor-theorem.md)
- [CT_catalog_nonabelian_type_partition](../part-03/ct-catalog-nonabelian-type-partition.md)
- [FAM_M_finiteness](../part-04/fam-m-finiteness.md)
- [FAM_M_simplicity](../part-04/fam-m-simplicity.md)
- [LC_generalized_fitting_self_centralizing](../part-05/lc-generalized-fitting-self-centralizing.md)
- [LR_nonabelian_simple_two_rank_lower_bound](../part-05/lr-nonabelian-simple-two-rank-lower-bound.md)
- [LR_semidihedral_simple_recognition](../part-05/lr-semidihedral-simple-recognition.md)

## Sources

- [CFSG/Milestones/CL_LIT_Gorenstein_Walter_L_balance.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Gorenstein_Walter_L_balance.lean)
