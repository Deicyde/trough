---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cls_component_dichotomy
statement: formalized
proof: formalized
---

# CLS_component_dichotomy

The milestone module `CFSG.Milestones.CLS_component_dichotomy`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CLS_component_dichotomy.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_component_dichotomy.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cls_component_dichotomy` (theorem, [line 11](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_component_dichotomy.lean#L11)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cls_component_dichotomy (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hrank : 3 ≤ twoRank G)
    (hconn : (involutionGraph G).Connected) : IsComponentType G ∨ IsCharTwoType G
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CFSG.Assembly.component_dichotomy](../../case-division/case-hdich-dichotomystatement.md)

## Sources

- [CFSG/Milestones/CLS_component_dichotomy.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_component_dichotomy.lean)
