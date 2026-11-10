---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cls_connectivity_macwilliams_four_generator
statement: formalized
proof: formalized
---

# CLS_connectivity_MacWilliams_four_generator

The milestone module `CFSG.Milestones.CLS_connectivity_MacWilliams_four_generator`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CLS_connectivity_MacWilliams_four_generator.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_connectivity_MacWilliams_four_generator.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cls_connectivity_macwilliams_four_generator` (theorem, [line 11](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_connectivity_MacWilliams_four_generator.lean#L11)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cls_connectivity_macwilliams_four_generator
    (S : Type) [Group S] [Finite S] (hS : IsPGroup 2 S)
    (hE : ∀ E : Subgroup S, E.Normal → IsElemAbelian 2 E → Nat.card E ≠ 8) :
    ∀ U : Subgroup S, ∃ X : Finset S, X.card ≤ 4 ∧ Subgroup.closure (X : Set S) = U
```

The files of 5 case theorems import it, directly or through other files: [`CFSG.Assembly.low_two_rank`](../../case-division/case-hlow-lowtworankstatement.md), [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/CLS_connectivity_MacWilliams_four_generator.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_connectivity_MacWilliams_four_generator.lean)
