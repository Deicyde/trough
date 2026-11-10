---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cls_component_classification
statement: formalized
proof: formalized
---

# CLS_component_classification

The milestone module `CFSG.Milestones.CLS_component_classification`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CLS_component_classification.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_component_classification.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cls_component_classification` (theorem, [line 3082](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_component_classification.lean#L3082)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cls_component_classification
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper InCatalog G) (hrank : 3 ≤ twoRank G)
    (hcomp : IsComponentType G) : InCatalog G
```

No case theorem's file imports it, directly or through other files.

## Depends on

- [CFSG.Assembly.component_type](../../case-division/case-hcomp-componentstatement.md)

## Sources

- [CFSG/Milestones/CLS_component_classification.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_component_classification.lean)
