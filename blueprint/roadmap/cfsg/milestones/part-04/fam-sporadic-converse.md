---
declaration: theorem
origin: cited
lean: CFSG.Milestones.fam_sporadic_converse_tauCeti, CFSG.Milestones.fam_sporadic_converse
statement: formalized
proof: formalized
---

# FAM_sporadic_converse

The milestone module `CFSG.Milestones.FAM_sporadic_converse`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/FAM_sporadic_converse.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_sporadic_converse.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.fam_sporadic_converse_tauCeti` (theorem, [line 14](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_sporadic_converse.lean#L14)). Proved here.

```lean
theorem _root_.CFSG.Milestones.fam_sporadic_converse_tauCeti
    (s : TauCeti.SporadicName) :
    Finite s.Group ∧ IsSimpleGroup s.Group
```

`CFSG.Milestones.fam_sporadic_converse` (theorem, [line 24](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_sporadic_converse.lean#L24)). Proved here.

```lean
theorem fam_sporadic_converse
    (G : Type) [Group G]
    (hrep : Blueprint.NativeSporadic.SporadicRep G) : Finite G ∧ IsSimpleGroup G
```

The files of 3 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [FAM_M_finiteness](fam-m-finiteness.md)
- [FAM_M_simplicity](fam-m-simplicity.md)

## Sources

- [CFSG/Milestones/FAM_sporadic_converse.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_sporadic_converse.lean)
