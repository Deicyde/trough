---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cls_characteristic_two_classification
statement: formalized
proof: formalized
---

# CLS_characteristic_two_classification

The milestone module `CFSG.Milestones.CLS_characteristic_two_classification`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CLS_characteristic_two_classification.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_characteristic_two_classification.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cls_characteristic_two_classification` (theorem, [line 3078](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_characteristic_two_classification.lean#L3078)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cls_characteristic_two_classification
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper InCatalog G)
    (hchar : IsCharTwoType G) : InCatalog G
```

No case theorem's file imports it, directly or through other files.

## Depends on

- [CFSG.Assembly.large_even](../../case-division/case-hle-largeevenstatement.md)
- [CFSG.Assembly.quasithin](../../case-division/case-hqt-quasithinstatement.md)
- [CFSG.Assembly.rank_three_even](../../case-division/case-hr3-rankthreestatement.md)

## Sources

- [CFSG/Milestones/CLS_characteristic_two_classification.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_characteristic_two_classification.lean)
