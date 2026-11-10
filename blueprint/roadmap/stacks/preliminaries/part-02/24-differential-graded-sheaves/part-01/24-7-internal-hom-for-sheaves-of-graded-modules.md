---
declaration: section
origin: cited
lean: SheafOfModules.GradedLocalHom, SheafOfModules.IsGradedSheafHom
statement: formalized
proof: formalized
---

# 24.7 Internal hom for sheaves of graded modules

Section 24.7 of the Stacks Project, [Tag 0FR3](https://stacks.math.columbia.edu/tag/0FR3). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FR3, the section

[Tag 0FR3](https://stacks.math.columbia.edu/tag/0FR3) in the Stacks Project.

**`SheafOfModules.GradedLocalHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHom.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHom.lean#L157). The attribute's comment: “local sections of the graded internal hom”.

> A local section of `SheafHom^n_A(M, L)` over an object `U` of the site: a map
> `M|_U → L|_U` of right graded `A|_U`-modules homogeneous of degree `n`, written out as a family
> of maps on sections over the objects `V ⟶ U` of the slice site.

```lean
structure GradedLocalHom (M : GradedModule.{t, a, w} A) (L : GradedModule.{t, a, z} A) (n : ℤ)
    (U : C)
```

**`SheafOfModules.IsGradedSheafHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHom.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInternalHom.lean#L417). The attribute's comment: “the graded internal hom of two right graded modules”.

> A graded sheaf of `R`-modules `G` is the graded internal hom `SheafHom^gr_A(M, L)` of two
> right graded `A`-modules when its degree-`n` sections over `U` are the degree-`n` local
> homomorphisms `M|_U → L|_U`, additively, `R`-linearly and compatibly with restriction.

```lean
structure IsGradedSheafHom (M : GradedModule.{t, a, w} A) (L : GradedModule.{t, a, z} A)
    (G : ℤ → SheafOfModules.{h} R)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.7, Tag 0FR3](https://stacks.math.columbia.edu/tag/0FR3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
