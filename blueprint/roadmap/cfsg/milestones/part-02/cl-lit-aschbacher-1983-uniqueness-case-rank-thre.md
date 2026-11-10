---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_aschbacher_1983_uniqueness_case_rank_three
statement: formalized
proof: formalized
---

# CL_LIT_Aschbacher_1983_uniqueness_case_rank_three

The milestone module `CFSG.Milestones.CL_LIT_Aschbacher_1983_uniqueness_case_rank_three`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CL_LIT_Aschbacher_1983_uniqueness_case_rank_three.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Aschbacher_1983_uniqueness_case_rank_three.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_aschbacher_1983_uniqueness_case_rank_three` (theorem, [line 3162](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Aschbacher_1983_uniqueness_case_rank_three.lean#L3162)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_aschbacher_1983_uniqueness_case_rank_three
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : IsKProper G) (hchar : IsCharTwoType G) (he : evenRank G = 3) :
    ¬ uniqueThreeUC G
```

The files of 1 case theorem import it, directly or through other files: [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [CAT_native_realization](../part-01/cat-native-realization.md)
- [CL_LIT_Gorenstein_Walter_L_balance](cl-lit-gorenstein-walter-l-balance.md)
- [CL_LIT_Timmesfeld_1978_large_extraspecial](../part-03/cl-lit-timmesfeld-1978-large-extraspecial.md)
- [CL_LIT_classical_involution_theorem](../part-03/cl-lit-classical-involution-theorem.md)
- [FAM_sporadic_converse](../part-04/fam-sporadic-converse.md)

## Sources

- [CFSG/Milestones/CL_LIT_Aschbacher_1983_uniqueness_case_rank_three.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Aschbacher_1983_uniqueness_case_rank_three.lean)
