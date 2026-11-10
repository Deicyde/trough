---
declaration: theorem
origin: cited
lean: CFSG.Milestones.SQTKSimpleList, CFSG.Milestones.cl_lit_sqtk_simple_list, CFSG.Milestones.cl_lit_sqtk_simple_list_simple
statement: formalized
proof: formalized
---

# CL_LIT_SQTK_simple_listBase

The milestone module `CFSG.Milestones.CL_LIT_SQTK_simple_listBase`, which CFSG/Milestones.lean does not import.

It declares 3 results, quoted from [CFSG/Milestones/CL_LIT_SQTK_simple_listBase.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_SQTK_simple_listBase.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.SQTKSimpleList` (def, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_SQTK_simple_listBase.lean#L12)). A definition.

```lean
def SQTKSimpleList (S : Type) [Group S] : Prop
```

`CFSG.Milestones.cl_lit_sqtk_simple_list` (theorem, [line 33](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_SQTK_simple_listBase.lean#L33)). Proved here.

```lean
theorem cl_lit_sqtk_simple_list
    (S : Type) [Group S] [Finite S]
    (hnonab : ∃ a b : S, a * b ≠ b * a) (hSQT : IsStronglyQuasithin S) (hcat : Catalog S) :
    SQTKSimpleList S
```

`CFSG.Milestones.cl_lit_sqtk_simple_list_simple` (theorem, [line 39](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_SQTK_simple_listBase.lean#L39)). Proved here.

```lean
theorem cl_lit_sqtk_simple_list_simple
    (S : Type) [Group S] [Finite S] [IsSimpleGroup S]
    (hnonab : ∃ a b : S, a * b ≠ b * a) (hSQTK : IsSQTKCat S) : SQTKSimpleList S
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [FAM_classical_model_membership](../part-04/fam-classical-model-membership.md)

## Sources

- [CFSG/Milestones/CL_LIT_SQTK_simple_listBase.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_SQTK_simple_listBase.lean)
