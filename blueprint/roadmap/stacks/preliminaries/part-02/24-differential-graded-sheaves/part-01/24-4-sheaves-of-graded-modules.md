---
declaration: section
origin: cited
lean: SheafOfModules.GradedModule, SheafOfModules.GradedModule.Hom, SheafOfModules.GradedModule.regularModule, SheafOfModules.LeftGradedModule, SheafOfModules.LeftGradedModule.Hom, SheafOfModules.LeftGradedModule.instCategory, SheafOfModules.GradedModule.hasCoproducts, SheafOfModules.GradedModule.pieceFunctor_preservesCoproducts
statement: formalized
proof: formalized
---

# 24.4 Sheaves of graded modules

Section 24.4 of the Stacks Project, [Tag 0FQY](https://stacks.math.columbia.edu/tag/0FQY). 2 tags here are carried by 15 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FQZ, a definition

[Tag 0FQZ](https://stacks.math.columbia.edu/tag/0FQZ) in the Stacks Project.

**`SheafOfModules.GradedModule`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedDegreeColimits.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedDegreeColimits.lean#L144). The attribute's comment: “right graded modules, over a sheaf of rings on an arbitrary site”.

> A right graded module over a sheaf of graded algebras.

```lean
structure GradedModule (A : GradedAlgebra.{t, a} R)
```

**`SheafOfModules.GradedModule.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedDegreeColimits.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedDegreeColimits.lean#L178). The attribute's comment: “homomorphisms of right graded modules”.

> A homomorphism of right graded modules over a sheaf of graded algebras.

```lean
structure Hom (M N : GradedModule.{t, a, m} A)
```

**An instance with no name** in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedDegreeColimits.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedDegreeColimits.lean#L219). The attribute's comment: “the category of right graded modules”.

> The category of right graded modules over a fixed sheaf of graded algebras.

```lean
instance : Category (GradedModule.{t, a, m} A)
```

**`SheafOfModules.GradedModule.regularModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensorUnitor.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedRelativeTensorUnitor.lean#L108). The attribute's comment: “a sheaf of graded algebras as a right graded module over itself”.

> A sheaf of graded algebras, acting on itself on the right. This is the graded counterpart of
> `SheafOfModules.DifferentialGradedModule.regularModule`.

```lean
def regularModule (A : GradedAlgebra.{t, m} R) : GradedModule.{t, m, m} A
```

**`SheafOfModules.LeftGradedModule`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftGradedModule.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftGradedModule.lean#L58). The attribute's comment: “left graded modules, over a sheaf of rings on an arbitrary site”.

> A left graded module over a sheaf of graded algebras.

```lean
structure LeftGradedModule (A : GradedAlgebra.{t, a} R)
```

**`SheafOfModules.LeftGradedModule.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftGradedModule.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftGradedModule.lean#L93). The attribute's comment: “homomorphisms of left graded modules”.

> A homomorphism of left graded modules over a sheaf of graded algebras.

```lean
structure Hom (M N : LeftGradedModule.{t, a, m} A)
```

**`SheafOfModules.LeftGradedModule.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftGradedModule.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftGradedModule.lean#L135). The attribute's comment: “the category of left graded modules”.

> The category of left graded modules over a fixed sheaf of graded algebras.

```lean
instance instCategory : Category (LeftGradedModule.{t, a, m} A)
```

## Tag 0FR0, a lemma

[Tag 0FR0](https://stacks.math.columbia.edu/tag/0FR0) in the Stacks Project.

**`SheafOfModules.GradedModule.hasCoproducts`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleAbelian.lean, line 1522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleAbelian.lean#L1522). The attribute's comment: “direct\_sums”.

> **Graded modules over a sheaf of graded algebras have arbitrary direct sums**, formed
> degreewise.

```lean
instance hasCoproducts : HasColimitsOfShape (Discrete ι) (GradedModule.{t, a, m} A)
```

**`SheafOfModules.GradedModule.pieceFunctor_preservesCoproducts`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleAbelian.lean, line 1530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleAbelian.lean#L1530). The attribute's comment: “direct\_sums”.

> **Taking a fixed homogeneous component commutes with set-indexed direct sums.**

```lean
instance pieceFunctor_preservesCoproducts (n : ℤ) :
    PreservesColimitsOfShape (Discrete ι) (pieceFunctor.{t, a, m} A n)
```

**`SheafOfModules.GradedModule.abelian`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleAbelian.lean, line 1570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleAbelian.lean#L1570). The attribute's comment: “abelian”.

> **The category of right graded modules over a sheaf of graded algebras is abelian.**
>
> Kernels and cokernels are formed degreewise, and the coimage-image comparison of a homomorphism
> is an isomorphism because it is one in each homogeneous degree.

```lean
noncomputable instance abelian : Abelian (GradedModule.{t, a, m} A)
```

**`SheafOfModules.GradedModule.pieceFunctor_preservesColimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleAbelian.lean, line 1610](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleAbelian.lean#L1610). The attribute's comment: “degree\_preserves\_colimits”.

> **Taking a fixed homogeneous component of a graded module commutes with all colimits.**
>
> The module universe is `max u m'` for a site `C : Type u`, because that is the hom universe of
> `SheafOfModules.{max u m'} R` and `PreservesColimits` quantifies over diagrams of that size;
> `pieceFunctor_preservesColimitsOfSize'` is the same content with the size universe free.

```lean
instance pieceFunctor_preservesColimits (n : ℤ) :
    PreservesColimits (pieceFunctor.{t, a, max u m'} A n)
```

**`SheafOfModules.GradedModule.pieceFunctor_preservesLimitsOfSize`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleDegreeLimits.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleDegreeLimits.lean#L62). The attribute's comment: “degree\_preserves\_limits”. References: SGA 6 VI (2.7), “partial”.

> **Taking a fixed homogeneous component of a graded module commutes with all limits.**
>
> A limit of any shape of the size of the module universe is built from products and equalizers,
> and the degree-`n` component preserves both: products and kernels of graded modules are formed
> degreewise.

```lean
instance pieceFunctor_preservesLimitsOfSize (n : ℤ) :
    PreservesLimitsOfSize.{m, m} (pieceFunctor.{t, a, m} A n)
```

**`SheafOfModules.GradedModule.filteredColimits_exact`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleFilteredColimits.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleFilteredColimits.lean#L133). The attribute's comment: “filtered\_colimits\_exact”.

> **Filtered colimits of right graded modules over a sheaf of graded algebras are exact**, at
> every size at which those colimits exist.

```lean
instance filteredColimits_exact (A : GradedAlgebra.{t, a} R)
    [HasFilteredColimitsOfSize.{s, s'} (GradedModule.{t, a, max u m'} A)] :
    AB5OfSize.{s, s'} (GradedModule.{t, a, max u m'} A)
```

**`SheafOfModules.GradedModule.ab5OfSize`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleFilteredColimits.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleFilteredColimits.lean#L146). The attribute's comment: “filtered\_colimits\_exact”.

> **Filtered colimits of right graded modules are exact**, unconditionally, at the module
> universe `max u m'` of a site `C : Type u`.
>
> The graded modules have all colimits of that size, so the size hypothesis of
> `filteredColimits_exact` is discharged rather than assumed.

```lean
theorem ab5OfSize (A : GradedAlgebra.{t, a} R) :
    AB5OfSize.{max u m', max u m'} (GradedModule.{t, a, max u m'} A)
```

**`SheafOfModules.GradedModule.hasLimitsOfSize`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleLimits.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleLimits.lean#L62). The attribute's comment: “limits”.

> **Graded modules over a sheaf of graded algebras admit all small limits.**
>
> A limit of any shape of the size of the module universe is built from degreewise products and
> from equalizers, the latter being the kernel of a difference.

```lean
instance hasLimitsOfSize : HasLimitsOfSize.{m, m} (GradedModule.{t, a, m} A)
```

Declarations registered for the tag:

- [`SheafOfModules.GradedModule.hasProducts`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleProducts.lean#L385), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleLimits.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleLimits.lean#L71) (StacksFrontier): “products”.
- [`SheafOfModules.GradedModule.hasColimitsOfSize`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleAbelian.lean#L1577), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleLimits.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedModuleLimits.lean#L73) (StacksFrontier): “colimits”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.4, Tag 0FQY](https://stacks.math.columbia.edu/tag/0FQY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
