---
declaration: theorem
origin: cited
lean: CFSG.Milestones.fam_sporadic_finiteness_tauCeti, CFSG.Milestones.fam_sporadic_finiteness
statement: formalized
proof: formalized
---

# FAM_sporadic_finiteness

The milestone module `CFSG.Milestones.FAM_sporadic_finiteness`, one of those CFSG/Milestones.lean imports.

It declares 2 results, quoted from [CFSG/Milestones/FAM_sporadic_finiteness.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_sporadic_finiteness.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.fam_sporadic_finiteness_tauCeti` (theorem, [line 11](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_sporadic_finiteness.lean#L11)). Proved here.

```lean
theorem fam_sporadic_finiteness_tauCeti
    (G : Type) [Group G]
    (hrep : ∃ s : TauCeti.SporadicName, Nonempty (G ≃* s.Group)) : Finite G
```

`CFSG.Milestones.fam_sporadic_finiteness` (theorem, [line 26](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_sporadic_finiteness.lean#L26)). Proved here.

```lean
theorem fam_sporadic_finiteness
    (G : Type) [Group G]
    (hrep : Blueprint.NativeSporadic.SporadicRep G) : Finite G
```

No case theorem's file imports it, directly or through other files.

## Depends on

- [FAM_M_finiteness](fam-m-finiteness.md)

## Sources

- [CFSG/Milestones/FAM_sporadic_finiteness.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_sporadic_finiteness.lean)
