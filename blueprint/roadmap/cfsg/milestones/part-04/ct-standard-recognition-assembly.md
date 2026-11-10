---
declaration: theorem
origin: cited
lean: CFSG.Milestones.ct_standard_recognition_assembly
statement: formalized
proof: formalized
---

# CT_standard_recognition_assembly

The milestone module `CFSG.Milestones.CT_standard_recognition_assembly`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CT_standard_recognition_assembly.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_standard_recognition_assembly.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.ct_standard_recognition_assembly` (theorem, [line 3405](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_standard_recognition_assembly.lean#L3405)). Proved here.

```lean
theorem _root_.CFSG.Milestones.ct_standard_recognition_assembly
    (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper InCatalog G)
    (L : Subgroup G) (hL : IsStandardSubgroup L) : InCatalog G
```

The files of 2 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md).

## Depends on

- [CT_initial_standard_component_frontier](../part-03/ct-initial-standard-component-frontier.md)
- [CT_odd_standard_recognition_frontier](../part-03/ct-odd-standard-recognition-frontier.md)

## Sources

- [CFSG/Milestones/CT_standard_recognition_assembly.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CT_standard_recognition_assembly.lean)
