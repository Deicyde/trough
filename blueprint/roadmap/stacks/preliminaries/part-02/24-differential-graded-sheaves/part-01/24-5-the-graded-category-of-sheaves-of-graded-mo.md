---
declaration: section
origin: cited
lean: SheafOfModules.GradedHomOfDegree
statement: formalized
proof: formalized
---

# 24.5 The graded category of sheaves of graded modules

Section 24.5 of the Stacks Project, [Tag 0FR1](https://stacks.math.columbia.edu/tag/0FR1). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FR1, the section

[Tag 0FR1](https://stacks.math.columbia.edu/tag/0FR1) in the Stacks Project.

**`SheafOfModules.GradedHomOfDegree`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHom.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHom.lean#L287). The attribute's comment: “homogeneous homomorphisms of degree n of right graded modules”.

> A homomorphism of right graded `A`-modules homogeneous of degree `n`: a family of morphisms
> `M^i ⟶ L^{i + n}` of sheaves of modules compatible with the right action. These are the
> elements of `Hom^n` in the graded category of right graded `A`-modules.

```lean
structure GradedHomOfDegree (M L : GradedModule.{t, a, w} A) (n : ℤ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.5, Tag 0FR1](https://stacks.math.columbia.edu/tag/0FR1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
