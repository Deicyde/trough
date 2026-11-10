---
declaration: section
origin: cited
lean: Stacks.Ample.isQuasiAffine_iff_isAmple
statement: formalized
proof: formalized
---

# 28.28 Affine and quasi-affine schemes

Section 28.28 of the Stacks Project, [Tag 01QD](https://stacks.math.columbia.edu/tag/01QD). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01QE, a lemma

[Tag 01QE](https://stacks.math.columbia.edu/tag/01QE) in the Stacks Project.

**`Stacks.Ample.isQuasiAffine_iff_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleWire/Basic.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleWire/Basic.lean#L352). References: EGA II (5.1.2), “more general”; EGA II (6.6.13).

> **Stacks Tag 01QE, unconditionally.** A scheme is quasi-affine if and only if its structure
> sheaf is ample. The hypothesis `∀ n, NonvanishingBasis (pow n)` of
> `Stacks.Ample.isQuasiAffine_iff_isAmpleForPowers`, which is not part of the source, is discharged
> by `Stacks.Ample.unitTensorPowBasis`: its two ingredients are the identification of the stalk of
> `𝒪_X` as an abelian group with `𝒪_{X,x}` as a ring, in the sibling file, and the identification
> of every tensor power of `𝒪_X` with `𝒪_X`, above.

```lean
theorem isQuasiAffine_iff_isAmple (Y : Scheme.{u}) :
    Y.IsQuasiAffine ↔ IsAmple Y (unitModule Y)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.28, Tag 01QD](https://stacks.math.columbia.edu/tag/01QD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
