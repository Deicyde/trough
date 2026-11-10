---
declaration: theorem
origin: cited
lean: CFSG.Milestones.fam_sporadic_representatives_definition
statement: formalized
proof: formalized
---

# FAM_sporadic_representatives

The milestone module `CFSG.Milestones.FAM_sporadic_representatives`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/FAM_sporadic_representatives.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_sporadic_representatives.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.fam_sporadic_representatives_definition` (theorem, [line 9](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_sporadic_representatives.lean#L9)). Proved here.

```lean
theorem fam_sporadic_representatives_definition (G : Type) [Group G] :
    Blueprint.NativeSporadic.SporadicRep G ↔
      ∃ s : TauCeti.SporadicName, Nonempty (G ≃* Blueprint.NativeSporadic.Carrier s)
```

No case theorem's file imports it, directly or through other files.

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/FAM_sporadic_representatives.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_sporadic_representatives.lean)
