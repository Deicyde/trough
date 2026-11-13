---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.isSheaf_fpqc
statement: formalized
proof: formalized
---

# 87.32 Formal algebraic spaces and fpqc coverings

Section 87.32 of the Stacks Project, [Tag 0AQC](https://stacks.math.columbia.edu/tag/0AQC). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AQD, a lemma

[Tag 0AQD](https://stacks.math.columbia.edu/tag/0AQD) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FpqcSheafGlueing.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FpqcSheafGlueing.lean#L182).

> **Stacks 0AQD.** A formal algebraic space `X` over a scheme `S` contained in a big fppf site
> `B` satisfies the sheaf property for the fpqc topology of the big fppf site of `S`.
>
> By `AlgebraicGeometry.FormalSpace.isSheaf_fpqc_of_isSheafFor_singleton_affine_of_formal` it is
> enough to check the sheaf condition for one surjective, flat, quasi-compact morphism of the
> site, which is `AlgebraicGeometry.FormalSpace.isSheafFor_singleton_of_isFormalAlgebraicSpace`.

```lean
theorem isSheaf_fpqc {X : FppfSheaf B S hS}
    (hX : IsFormalAlgebraicSpace B S hS X) :
    Presheaf.IsSheaf
      ((Scheme.fpqcPrecoverage.comap (BigFppfOver.toScheme B S hS)).toGrothendieck) X.obj
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.32, Tag 0AQC](https://stacks.math.columbia.edu/tag/0AQC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
