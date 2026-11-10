---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cls_rank_three_even_classification
statement: formalized
proof: formalized
---

# CLS_rank_three_even_classification

The milestone module `CFSG.Milestones.CLS_rank_three_even_classification`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CLS_rank_three_even_classification.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_rank_three_even_classification.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cls_rank_three_even_classification` (theorem, [line 2613](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_rank_three_even_classification.lean#L2613)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cls_rank_three_even_classification
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper InCatalog G) (hchar : IsCharTwoType G)
    (he : evenRank G = 3) : InCatalog G
```

No case theorem's file imports it, directly or through other files.

## Depends on

- [CFSG.Assembly.rank_three_even](../../case-division/case-hr3-rankthreestatement.md)

## Sources

- [CFSG/Milestones/CLS_rank_three_even_classification.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_rank_three_even_classification.lean)
