---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_walter_abelian_sylow_two_simple, CFSG.Milestones.cl_lit_walter_abelian_sylow_two_simple_models
statement: formalized
proof: formalized
---

# CL_LIT_Walter_abelian_Sylow_two_simple

The milestone module `CFSG.Milestones.CL_LIT_Walter_abelian_Sylow_two_simple`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CL_LIT_Walter_abelian_Sylow_two_simple.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Walter_abelian_Sylow_two_simple.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_walter_abelian_sylow_two_simple` (theorem, [line 16](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Walter_abelian_Sylow_two_simple.lean#L16)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_walter_abelian_sylow_two_simple
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (P : Sylow 2 G) (hP : IsMulCommutative (P : Subgroup G)) :
    (∃ f : ℕ, 2 ≤ f ∧ Nonempty (G ≃* PSL(2, GaloisField 2 f))) ∨
    (∃ p f : ℕ, ∃ _hp : Fact p.Prime, Odd p ∧ 0 < f ∧ 5 ≤ p ^ f ∧
        (p ^ f % 8 = 3 ∨ p ^ f % 8 = 5) ∧ Nonempty (G ≃* PSL(2, GaloisField p f))) ∨
    (∃ m : ℕ, 1 ≤ m ∧ Nat.card G = ordRee (3 ^ (2 * m + 1))) ∨
    Nonempty (G ≃* walterJ1)
```

`CFSG.Milestones.cl_lit_walter_abelian_sylow_two_simple_models` (theorem, [line 33](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Walter_abelian_Sylow_two_simple.lean#L33)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_walter_abelian_sylow_two_simple_models
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (P : Sylow 2 G) (hP : IsMulCommutative (P : Subgroup G)) :
    (∃ f : ℕ, 2 ≤ f ∧ Blueprint.LieModel G .PSL 2 2 f) ∨
    (∃ p f : ℕ, p.Prime ∧ p ≠ 2 ∧ 1 ≤ f ∧ 5 ≤ p ^ f ∧
      (p ^ f % 8 = 3 ∨ p ^ f % 8 = 5) ∧ Blueprint.LieModel G .PSL 2 p f) ∨
    (∃ f : ℕ, Odd f ∧ 3 ≤ f ∧ Blueprint.LieModel G .twistedG2 0 3 f) ∨
      Blueprint.NativeSporadic.IsSporadic G .J1
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CFSG.FeitThompson.isSolvable_of_odd_natCard](../../case-division/case-hodd-oddorderstatement.md)
- [CLS_connectivity_MacWilliams_four_generator](../part-01/cls-connectivity-macwilliams-four-generator.md)
- [FAM_classical_model_membership](../part-04/fam-classical-model-membership.md)
- [LR_Glauberman_Z_star_central_Sylow_involution](../part-05/lr-glauberman-z-star-central-sylow-involution.md)

## Sources

- [CFSG/Milestones/CL_LIT_Walter_abelian_Sylow_two_simple.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Walter_abelian_Sylow_two_simple.lean)
