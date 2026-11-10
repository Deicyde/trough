---
declaration: theorem
origin: cited
lean: CFSG.Milestones.bender_suzuki
statement: formalized
proof: formalized
---

# SE_simple_strong_embedding_models

The milestone module `CFSG.Milestones.SE_simple_strong_embedding_models`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/SE_simple_strong_embedding_models.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/SE_simple_strong_embedding_models.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.bender_suzuki` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/SE_simple_strong_embedding_models.lean#L12)). Proved here.

```lean
theorem _root_.CFSG.Milestones.bender_suzuki {X : Type*} [Group X] [Finite X] [IsSimpleGroup X]
    (M : Subgroup X) (h : CFSG.BenderSuzuki.IsStronglyEmbeddedOrder M) :
    CFSG.BenderSuzuki.IsBenderGroup X
```

The files of 5 case theorems import it, directly or through other files: [`CFSG.Assembly.low_two_rank`](../../case-division/case-hlow-lowtworankstatement.md), [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/SE_simple_strong_embedding_models.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/SE_simple_strong_embedding_models.lean)
