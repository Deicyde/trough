---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cls_involution_centralizers_characteristic_two_transfer
statement: formalized
proof: formalized
---

# CLS_involution_centralizers_characteristic_two_transfer

The milestone module `CFSG.Milestones.CLS_involution_centralizers_characteristic_two_transfer`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CLS_involution_centralizers_characteristic_two_transfer.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_involution_centralizers_characteristic_two_transfer.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cls_involution_centralizers_characteristic_two_transfer` (theorem, [line 15](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_involution_centralizers_characteristic_two_transfer.lean#L15)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cls_involution_centralizers_characteristic_two_transfer (G : Type) [Group G] [Finite G]
    (hC : ∀ t : G, orderOf t = 2 → dichotomyCharP 2 (Subgroup.centralizer ({t} : Set G))) :
    IsCharTwoType G
```

The files of 5 case theorems import it, directly or through other files: [`CFSG.Assembly.component_dichotomy`](../../case-division/case-hdich-dichotomystatement.md), [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/CLS_involution_centralizers_characteristic_two_transfer.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_involution_centralizers_characteristic_two_transfer.lean)
