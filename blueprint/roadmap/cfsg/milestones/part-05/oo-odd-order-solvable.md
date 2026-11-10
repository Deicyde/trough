---
declaration: theorem
origin: cited
lean: CFSG.Milestones.odd_order_solvable
statement: formalized
proof: formalized
---

# OO_odd_order_solvable

The milestone module `CFSG.Milestones.OO_odd_order_solvable`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/OO_odd_order_solvable.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/OO_odd_order_solvable.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.odd_order_solvable` (theorem, [line 11](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/OO_odd_order_solvable.lean#L11)). Proved here.

```lean
theorem _root_.CFSG.Milestones.odd_order_solvable {G : Type*} [Group G] [Finite G]
    (_h : Odd (Nat.card G)) : Group.IsSolvable G
```

The files of 6 case theorems import it, directly or through other files: [`CFSG.Assembly.low_two_rank`](../../case-division/case-hlow-lowtworankstatement.md), [`CFSG.Assembly.component_dichotomy`](../../case-division/case-hdich-dichotomystatement.md), [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CFSG.FeitThompson.isSolvable_of_odd_natCard](../../case-division/case-hodd-oddorderstatement.md)

## Sources

- [CFSG/Milestones/OO_odd_order_solvable.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/OO_odd_order_solvable.lean)
