---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cls_component_free_centralizer_quotient_characteristic_two
statement: formalized
proof: formalized
---

# CLS_component_free_centralizer_quotient_characteristic_two

The milestone module `CFSG.Milestones.CLS_component_free_centralizer_quotient_characteristic_two`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CLS_component_free_centralizer_quotient_characteristic_two.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_component_free_centralizer_quotient_characteristic_two.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cls_component_free_centralizer_quotient_characteristic_two` (theorem, [line 53](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_component_free_centralizer_quotient_characteristic_two.lean#L53)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cls_component_free_centralizer_quotient_characteristic_two (G : Type) [Group G] [Finite G]
    (hcomp : ¬ IsComponentType G) (t : G) (ht : orderOf t = 2) :
    dichotomyCharP 2 (Subgroup.centralizer ({t} : Set G) ⧸
        oddCore (Subgroup.centralizer ({t} : Set G))) ∧
      (oddCore (Subgroup.centralizer ({t} : Set G)) = ⊥ →
        dichotomyCharP 2 (Subgroup.centralizer ({t} : Set G)))
```

The files of 5 case theorems import it, directly or through other files: [`CFSG.Assembly.component_dichotomy`](../../case-division/case-hdich-dichotomystatement.md), [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/CLS_component_free_centralizer_quotient_characteristic_two.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_component_free_centralizer_quotient_characteristic_two.lean)
