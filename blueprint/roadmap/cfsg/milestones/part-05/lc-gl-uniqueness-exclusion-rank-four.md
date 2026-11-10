---
declaration: theorem
origin: cited
lean: CFSG.Milestones.lc_gl_uniqueness_exclusion_rank_four
statement: formalized
proof: formalized
---

# LC_GL_uniqueness_exclusion_rank_four

The milestone module `CFSG.Milestones.LC_GL_uniqueness_exclusion_rank_four`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/LC_GL_uniqueness_exclusion_rank_four.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_uniqueness_exclusion_rank_four.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.lc_gl_uniqueness_exclusion_rank_four` (theorem, [line 3186](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_uniqueness_exclusion_rank_four.lean#L3186)). Proved here.

```lean
theorem _root_.CFSG.Milestones.lc_gl_uniqueness_exclusion_rank_four
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hK : IsKProper G) (hchar : IsCharTwoType G) (he : 4 ≤ evenRank G) :
    ¬ uniqueFourUnique G
```

The files of 1 case theorem import it, directly or through other files: [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CAT_native_realization](../part-01/cat-native-realization.md)
- [CL_LIT_Gorenstein_Walter_L_balance](../part-02/cl-lit-gorenstein-walter-l-balance.md)
- [CL_LIT_Timmesfeld_1978_large_extraspecial](../part-03/cl-lit-timmesfeld-1978-large-extraspecial.md)
- [CL_LIT_classical_involution_theorem](../part-03/cl-lit-classical-involution-theorem.md)
- [FAM_sporadic_converse](../part-04/fam-sporadic-converse.md)

## Sources

- [CFSG/Milestones/LC_GL_uniqueness_exclusion_rank_four.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LC_GL_uniqueness_exclusion_rank_four.lean)
