---
declaration: theorem
origin: cited
lean: CFSG.Milestones.qt_faithful_local_nonempty_classification
statement: formalized
proof: formalized
---

# QT_faithful_local_nonempty_classification

The milestone module `CFSG.Milestones.QT_faithful_local_nonempty_classification`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/QT_faithful_local_nonempty_classification.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_faithful_local_nonempty_classification.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.qt_faithful_local_nonempty_classification` (theorem, [line 1833](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_faithful_local_nonempty_classification.lean#L1833)). Proved here.

```lean
theorem _root_.CFSG.Milestones.qt_faithful_local_nonempty_classification
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hqtke : quasithinIsQTKE G) (T : Sylow 2 G)
    (hLf : ∃ L : Subgroup G, quasithinIsFaithfulLocal (T : Subgroup G) L) :
    InCatalog G
```

The files of 1 case theorem import it, directly or through other files: [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md).

## Depends on

- [QT_H13_maximal_local_catalog_assembly](qt-h13-maximal-local-catalog-assembly.md)

## Sources

- [CFSG/Milestones/QT_faithful_local_nonempty_classification.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_faithful_local_nonempty_classification.lean)
