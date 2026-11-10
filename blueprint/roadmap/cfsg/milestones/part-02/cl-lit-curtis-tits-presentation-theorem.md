---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_curtis_tits_presentation_theorem
statement: formalized
proof: formalized
---

# CL_LIT_Curtis_Tits_presentation_theorem

The milestone module `CFSG.Milestones.CL_LIT_Curtis_Tits_presentation_theorem`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CL_LIT_Curtis_Tits_presentation_theorem.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Curtis_Tits_presentation_theorem.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_curtis_tits_presentation_theorem` (theorem, [line 19](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Curtis_Tits_presentation_theorem.lean#L19)). Proved here.

```lean
theorem cl_lit_curtis_tits_presentation_theorem (t : StatedLieTag) (n p f : ℕ)
    (hadm : StatedLieAdmissible t n p f) (hrank : 3 ≤ bnRank t n) :
    CurtisTitsConclusion.{w} (lieUniversal t n p f hadm.1).D t n p f
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [FAM_classical_model_membership](../part-04/fam-classical-model-membership.md)

## Sources

- [CFSG/Milestones/CL_LIT_Curtis_Tits_presentation_theorem.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Curtis_Tits_presentation_theorem.lean)
