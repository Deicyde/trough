---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsAlgebraicSpace.isSheaf_fpqc
statement: formalized
proof: formalized
---

# 66.17 Spaces and fpqc coverings

Section 66.17 of the Stacks Project, [Tag 03W8](https://stacks.math.columbia.edu/tag/03W8). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0APL, a proposition

[Tag 0APL](https://stacks.math.columbia.edu/tag/0APL) in the Stacks Project.

**`AlgebraicGeometry.IsAlgebraicSpace.isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/IndQuasiAffineFpqcSheaf.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/IndQuasiAffineFpqcSheaf.lean#L111).

> **An algebraic space is a sheaf for the fpqc topology**, which is
> [Stacks, Tag 0APL](https://stacks.math.columbia.edu/tag/0APL).

```lean
theorem isSheaf_fpqc (hF : IsAlgebraicSpace B S hS F) :
    Presheaf.IsSheaf
      ((Scheme.fpqcPrecoverage.comap (BigFppfOver.toScheme B S hS)).toGrothendieck) F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.17, Tag 03W8](https://stacks.math.columbia.edu/tag/03W8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
