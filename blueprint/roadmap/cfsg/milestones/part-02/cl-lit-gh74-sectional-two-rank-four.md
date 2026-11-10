---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_gh74_sectional_two_rank_four, CFSG.Milestones.cl_lit_gh74_sectional_two_rank_four_models
statement: formalized
proof: formalized
---

# CL_LIT_GH74_sectional_two_rank_four

The milestone module `CFSG.Milestones.CL_LIT_GH74_sectional_two_rank_four`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CL_LIT_GH74_sectional_two_rank_four.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_GH74_sectional_two_rank_four.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_gh74_sectional_two_rank_four` (theorem, [line 1638](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_GH74_sectional_two_rank_four.lean#L1638)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_gh74_sectional_two_rank_four
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hrank : 3 ≤ twoRank G)
    (hsect : ∀ P : Subgroup G, IsPGroup 2 P →
      ∃ s : Finset G, s.card ≤ 4 ∧ Subgroup.closure (s : Set G) = P) :
    Nat.card G ∈ gorensteinHarada74Orders
```

`CFSG.Milestones.cl_lit_gh74_sectional_two_rank_four_models` (theorem, [line 1659](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_GH74_sectional_two_rank_four.lean#L1659)). Proved here.

```lean
theorem cl_lit_gh74_sectional_two_rank_four_models
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hrank : 3 ≤ Open.twoRank G)
    (hsect : ∀ P : Subgroup G, IsPGroup 2 P →
      ∃ s : Finset G, s.card ≤ 4 ∧ Subgroup.closure (s : Set G) = P) :
    (∃ p f : ℕ, p.Prime ∧ p ≠ 2 ∧ 1 ≤ f ∧
      (Blueprint.LieModel G .G2 0 p f ∨ Blueprint.LieModel G .trialityD4 0 p f)) ∨
    (∃ p f : ℕ, p.Prime ∧ p ≠ 2 ∧ 1 ≤ f ∧ Blueprint.LieModel G .PSp 2 p f) ∨
    (∃ f : ℕ, Blueprint.LieModel G .twistedG2 0 3 f) ∨
    (∃ p f : ℕ, p.Prime ∧ p ≠ 2 ∧ 1 ≤ f ∧ p ^ f % 8 ≠ 1 ∧
      Blueprint.LieModel G .PSL 4 p f) ∨
    (∃ p f : ℕ, p.Prime ∧ p ≠ 2 ∧ 1 ≤ f ∧ p ^ f % 8 ≠ 7 ∧
      Blueprint.LieModel G .PSU 4 p f) ∨
    (∃ p f : ℕ, p.Prime ∧ 1 ≤ f ∧ p ^ f % 4 = 3 ∧ Blueprint.LieModel G .PSL 5 p f) ∨
    (∃ p f : ℕ, p.Prime ∧ 1 ≤ f ∧ p ^ f % 4 = 1 ∧ Blueprint.LieModel G .PSU 5 p f) ∨
    (Blueprint.LieModel G .PSL 2 2 3 ∨ Blueprint.LieModel G .PSL 2 2 4 ∨
      Blueprint.LieModel G .PSL 3 2 2 ∨ Blueprint.LieModel G .twistedB2 0 2 3) ∨
    (∃ n : ℕ, 8 ≤ n ∧ n ≤ 11 ∧ Nonempty (G ≃* alternatingGroup (Fin n))) ∨
    (Blueprint.NativeSporadic.IsSporadic G .M12 ∨ Blueprint.NativeSporadic.IsSporadic G .M22 ∨
      Blueprint.NativeSporadic.IsSporadic G .M23 ∨ Blueprint.NativeSporadic.IsSporadic G .J1 ∨
      Blueprint.NativeSporadic.IsSporadic G .J2 ∨ Blueprint.NativeSporadic.IsSporadic G .J3 ∨
      Blueprint.NativeSporadic.IsSporadic G .McL ∨ Blueprint.NativeSporadic.IsSporadic G .Ly)
```

The files of 3 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CL_LIT_Aschbacher_component_type_theorem_5](cl-lit-aschbacher-component-type-theorem-5.md)
- [CL_LIT_Aschbacher_proper_two_generated_core](cl-lit-aschbacher-proper-two-generated-core.md)
- [CL_LIT_Borel_Tits_local_parabolic](cl-lit-borel-tits-local-parabolic.md)
- [CL_LIT_signalizer_functor_theorem](../part-03/cl-lit-signalizer-functor-theorem.md)
- [FAM_M_finiteness](../part-04/fam-m-finiteness.md)
- [FAM_M_simplicity](../part-04/fam-m-simplicity.md)
- [LC_generalized_fitting_self_centralizing](../part-05/lc-generalized-fitting-self-centralizing.md)
- [QT_faithful_local_empty_classification](../part-05/qt-faithful-local-empty-classification.md)
- [QT_unique_maximal_local_classification](../part-06/qt-unique-maximal-local-classification.md)
- [SG_two_signalizer_completeness](../part-06/sg-two-signalizer-completeness.md)
- [ZJ_glauberman_characteristic](../part-06/zj-glauberman-characteristic.md)

## Sources

- [CFSG/Milestones/CL_LIT_GH74_sectional_two_rank_four.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_GH74_sectional_two_rank_four.lean)
