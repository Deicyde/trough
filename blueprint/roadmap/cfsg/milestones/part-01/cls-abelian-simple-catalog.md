---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cls_abelian_simple_catalog
statement: formalized
proof: formalized
---

# CLS_abelian_simple_catalog

The milestone module `CFSG.Milestones.CLS_abelian_simple_catalog`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/CLS_abelian_simple_catalog.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_abelian_simple_catalog.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cls_abelian_simple_catalog` (theorem, [line 11](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_abelian_simple_catalog.lean#L11)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cls_abelian_simple_catalog (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hcomm : ∀ a b : G, a * b = b * a) : InCatalog G
```

No case theorem's file imports it, directly or through other files.

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/CLS_abelian_simple_catalog.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CLS_abelian_simple_catalog.lean)
