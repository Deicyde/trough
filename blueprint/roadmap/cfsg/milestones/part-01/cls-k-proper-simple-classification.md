---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cls_k_proper_simple_classification, CFSG.Milestones.cls_k_proper_simple_classification_catalog
statement: formalized
proof: formalized
---

# CLS_K_proper_simple_classification

The milestone module `CFSG.Milestones.CLS_K_proper_simple_classification`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/CLS_K_proper_simple_classification.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_K_proper_simple_classification.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cls_k_proper_simple_classification` (theorem, [line 3931](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_K_proper_simple_classification.lean#L3931)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cls_k_proper_simple_classification
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hK : KProper InCatalog G) : InCatalog G
```

`CFSG.Milestones.cls_k_proper_simple_classification_catalog` (theorem, [line 3939](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_K_proper_simple_classification.lean#L3939)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cls_k_proper_simple_classification_catalog
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hK : KCore.KProperAllSimple Blueprint.Catalog G) : Blueprint.Catalog G
```

No case theorem's file imports it, directly or through other files.

## Depends on

- [CFSG.Assembly.large_even](../../case-division/case-hle-largeevenstatement.md)
- [CFSG.Assembly.quasithin](../../case-division/case-hqt-quasithinstatement.md)
- [CFSG.Assembly.rank_three_even](../../case-division/case-hr3-rankthreestatement.md)

## Sources

- [CFSG/Milestones/CLS_K_proper_simple_classification.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_K_proper_simple_classification.lean)
