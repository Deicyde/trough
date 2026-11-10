---
declaration: theorem
origin: cited
lean: CFSG.Milestones.fam_sporadic_native_converse
statement: formalized
proof: formalized
---

# FAM_sporadic_native_converse

The milestone module `CFSG.Milestones.FAM_sporadic_native_converse`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/FAM_sporadic_native_converse.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_sporadic_native_converse.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.fam_sporadic_native_converse` (theorem, [line 10](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_sporadic_native_converse.lean#L10)). Proved here.

```lean
theorem fam_sporadic_native_converse
    (G : Type) [Group G] (hrep : NativeSporadicRep G) :
    Finite G ∧ Nontrivial G ∧ IsSimpleGroup G
```

No case theorem's file imports it, directly or through other files.

## Depends on

- [CAT_native_realization](../part-01/cat-native-realization.md)

## Sources

- [CFSG/Milestones/FAM_sporadic_native_converse.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/FAM_sporadic_native_converse.lean)
