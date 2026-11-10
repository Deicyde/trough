---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_gl83_theorem_c_preuniqueness_rank_three
statement: formalized
proof: formalized
---

# CL_LIT_GL83_Theorem_C_preuniqueness_rank_three

The milestone module `CFSG.Milestones.CL_LIT_GL83_Theorem_C_preuniqueness_rank_three`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CL_LIT_GL83_Theorem_C_preuniqueness_rank_three.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_GL83_Theorem_C_preuniqueness_rank_three.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_gl83_theorem_c_preuniqueness_rank_three` (theorem, [line 3334](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_GL83_Theorem_C_preuniqueness_rank_three.lean#L3334)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_gl83_theorem_c_preuniqueness_rank_three
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : IsKProper G) (hchar : IsCharTwoType G) (he : evenRank G = 3)
    (hpre : rankThreeAschCoreLocal G 2) :
    rankThreeUC G
```

The files of 1 case theorem import it, directly or through other files: [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [CFSG.Assembly.component_type](../../case-division/case-hcomp-componentstatement.md)
- [CAT_native_realization](../part-01/cat-native-realization.md)
- [CLS_low_two_rank_classification](cls-low-two-rank-classification.md)
- [CL_LIT_AS_vol_I_background](cl-lit-as-vol-i-background.md)
- [CL_LIT_Timmesfeld_1978_large_extraspecial](../part-03/cl-lit-timmesfeld-1978-large-extraspecial.md)
- [LC_GL_embedding_theorem_D2_rank_four](../part-04/lc-gl-embedding-theorem-d2-rank-four.md)

## Sources

- [CFSG/Milestones/CL_LIT_GL83_Theorem_C_preuniqueness_rank_three.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_GL83_Theorem_C_preuniqueness_rank_three.lean)
