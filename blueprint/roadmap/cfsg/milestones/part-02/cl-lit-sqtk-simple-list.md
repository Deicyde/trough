---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_sqtk_simple_list_section
statement: formalized
proof: formalized
---

# CL_LIT_SQTK_simple_list

The milestone module `CFSG.Milestones.CL_LIT_SQTK_simple_list`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CL_LIT_SQTK_simple_list.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_SQTK_simple_list.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_sqtk_simple_list_section` (theorem, [line 14](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_SQTK_simple_list.lean#L14)). Proved here.

```lean
theorem cl_lit_sqtk_simple_list_section
    (X : Type) [Group X] [Finite X] (hSQTK : IsSQTKCat X)
    (H : Subgroup X) (N : Subgroup H) [N.Normal] [IsSimpleGroup (H ⧸ N)]
    (hnonab : ∃ a b : H ⧸ N, a * b ≠ b * a) : SQTKSimpleList (H ⧸ N)
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CL_LIT_SQTK_simple_listBase](../part-03/cl-lit-sqtk-simple-listbase.md)

## Sources

- [CFSG/Milestones/CL_LIT_SQTK_simple_list.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_SQTK_simple_list.lean)
