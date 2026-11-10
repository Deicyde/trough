---
declaration: theorem
origin: cited
lean: CFSG.Milestones.lr_nonabelian_simple_two_rank_lower_bound
statement: formalized
proof: formalized
---

# LR_nonabelian_simple_two_rank_lower_bound

The milestone module `CFSG.Milestones.LR_nonabelian_simple_two_rank_lower_bound`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/LR_nonabelian_simple_two_rank_lower_bound.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_nonabelian_simple_two_rank_lower_bound.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.lr_nonabelian_simple_two_rank_lower_bound` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_nonabelian_simple_two_rank_lower_bound.lean#L12)). Proved here.

```lean
theorem _root_.CFSG.Milestones.lr_nonabelian_simple_two_rank_lower_bound (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (heven : Even (Nat.card G)) :
    2 ≤ twoRank G
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CFSG.Assembly.low_two_rank](../../case-division/case-hlow-lowtworankstatement.md)

## Sources

- [CFSG/Milestones/LR_nonabelian_simple_two_rank_lower_bound.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/LR_nonabelian_simple_two_rank_lower_bound.lean)
