---
declaration: theorem
origin: cited
lean: CFSG.Milestones.qt_h13_maximal_local_catalog_assembly
statement: formalized
proof: formalized
---

# QT_H13_maximal_local_catalog_assembly

The milestone module `CFSG.Milestones.QT_H13_maximal_local_catalog_assembly`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/QT_H13_maximal_local_catalog_assembly.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_H13_maximal_local_catalog_assembly.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.qt_h13_maximal_local_catalog_assembly` (theorem, [line 1778](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_H13_maximal_local_catalog_assembly.lean#L1778)). Proved here.

```lean
theorem qt_h13_maximal_local_catalog_assembly
    (G : Type) [Group G] [Finite G] (T L : Subgroup G)
    (hH13 : CFSG.Quasithin.H13.QTH13 G T L)
    (hmax : CFSG.Open.quasithinIsMaximalLocal T L) : CFSG.Blueprint.Catalog G
```

The files of 1 case theorem import it, directly or through other files: [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md).

## Depends on

- [CL_LIT_Borel_Tits_local_parabolic](../part-02/cl-lit-borel-tits-local-parabolic.md)
- [CL_LIT_Gorenstein_Walter_L_balance](../part-02/cl-lit-gorenstein-walter-l-balance.md)
- [QT_faithful_local_empty_classification](qt-faithful-local-empty-classification.md)

## Sources

- [CFSG/Milestones/QT_H13_maximal_local_catalog_assembly.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/QT_H13_maximal_local_catalog_assembly.lean)
