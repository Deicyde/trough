---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cls_qtke_classification_even_characteristic, CFSG.Milestones.cls_qtke_classification
statement: formalized
proof: formalized
---

# CLS_QTKE_classification

The milestone module `CFSG.Milestones.CLS_QTKE_classification`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CLS_QTKE_classification.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_QTKE_classification.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cls_qtke_classification_even_characteristic` (theorem, [line 1866](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_QTKE_classification.lean#L1866)). Proved here.

```lean
theorem cls_qtke_classification_even_characteristic
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a)
    (hqtke : QuasithinUnique.quasithinIsQTKECat G) : Blueprint.Catalog G
```

`CFSG.Milestones.cls_qtke_classification` (theorem, [line 1874](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_QTKE_classification.lean#L1874)). Proved here.

```lean
theorem cls_qtke_classification
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper Blueprint.Catalog G)
    (hchar : IsCharTwoType G) (he : evenRank G ≤ 2) : Blueprint.Catalog G
```

No case theorem's file imports it, directly or through other files.

## Depends on

- [QT_faithful_local_nonempty_classification](../part-05/qt-faithful-local-nonempty-classification.md)
- [QT_unique_maximal_local_classification](../part-06/qt-unique-maximal-local-classification.md)

## Sources

- [CFSG/Milestones/CLS_QTKE_classification.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_QTKE_classification.lean)
