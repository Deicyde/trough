---
declaration: section
origin: cited
lean: SheafOfModules.LocalHom, SheafOfModules.LocalHom.comp
statement: formalized
proof: formalized
---

# 24.16 Internal hom for sheaves of differential graded modules

Section 24.16 of the Stacks Project, [Tag 0FRN](https://stacks.math.columbia.edu/tag/0FRN). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FRN, the section

[Tag 0FRN](https://stacks.math.columbia.edu/tag/0FRN) in the Stacks Project.

**`SheafOfModules.LocalHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHom.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHom.lean#L161). The attribute's comment: “local sections of the graded internal hom”.

> A local section of `SheafHom^n_A(M, L)` over `U`: a map `M|_U → L|_U` of right differential
> graded `A|_U`-modules homogeneous of degree `n`.

```lean
structure LocalHom (M : DifferentialGradedModule.{t, a, w} A)
    (L : DifferentialGradedModule.{t, a, z} A) (n : ℤ) (U : C)
    extends LocalGradedHom M L n U
```

**`SheafOfModules.LocalHom.comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHom.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInternalHom.lean#L226). The attribute's comment: “the composition map of the internal hom”.

> The composition of local homomorphisms of right differential graded `A|_U`-modules.

```lean
def LocalHom.comp {K : DifferentialGradedModule.{t, a, s} A}
    {M : DifferentialGradedModule.{t, a, w} A} {L : DifferentialGradedModule.{t, a, z} A}
    {n m nm : ℤ} {U : C} (g : LocalHom K M n U) (f : LocalHom M L m U) (h : n + m = nm) :
    LocalHom K L nm U
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.16, Tag 0FRN](https://stacks.math.columbia.edu/tag/0FRN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
