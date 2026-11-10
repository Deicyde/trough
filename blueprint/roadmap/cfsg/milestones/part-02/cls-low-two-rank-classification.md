---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cls_low_two_rank_classification
statement: formalized
proof: formalized
---

# CLS_low_two_rank_classification

The milestone module `CFSG.Milestones.CLS_low_two_rank_classification`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CLS_low_two_rank_classification.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_low_two_rank_classification.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cls_low_two_rank_classification` (theorem, [line 12](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_low_two_rank_classification.lean#L12)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cls_low_two_rank_classification
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (heven : Even (Nat.card G))
    (hrank : twoRank G ≤ 2) : CFSG.Blueprint.Catalog G
```

The files of 1 case theorem import it, directly or through other files: [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [CFSG.Assembly.low_two_rank](../../case-division/case-hlow-lowtworankstatement.md)

## Sources

- [CFSG/Milestones/CLS_low_two_rank_classification.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_low_two_rank_classification.lean)
