---
declaration: section
origin: cited
lean: SheafOfModules.forgetToGradedModule_isRightAdjoint, SheafOfModules.dgHull_acyclic, SheafOfModules.dgHull_unit_mono, SheafOfModules.dgHull_differential_cokernel_iso
statement: formalized
proof: formalized
---

# 24.24 The differential graded hull of a graded module

Section 24.24 of the Stacks Project, [Tag 0FSJ](https://stacks.math.columbia.edu/tag/0FSJ). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FSK, a lemma

[Tag 0FSK](https://stacks.math.columbia.edu/tag/0FSK) in the Stacks Project.

**`SheafOfModules.forgetToGradedModule_isRightAdjoint`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedForgetRightAdjoint.lean, line 668](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedForgetRightAdjoint.lean#L668).

> For a sheaf of differential graded algebras, the functor from right differential graded
> modules to right graded modules that forgets the differential has a left adjoint.

```lean
instance forgetToGradedModule_isRightAdjoint (A : DifferentialGradedAlgebra.{t, a} R) :
    (forgetToGradedModule.{t, a, m} A).IsRightAdjoint
```

## Tag 0FSL, a lemma

[Tag 0FSL](https://stacks.math.columbia.edu/tag/0FSL) in the Stacks Project.

**`SheafOfModules.dgHull_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedForgetRightAdjoint.lean, line 702](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedForgetRightAdjoint.lean#L702). The attribute's comment: “part (3)”.

> The differential graded hull of a right graded module is acyclic.

```lean
theorem dgHull_acyclic (A : DifferentialGradedAlgebra.{t, a} R)
    (N : GradedModule.{t, a, m} A.toGradedAlgebra) :
    (((forgetToGradedModule.{t, a, m} A).leftAdjoint.obj N).complex).Acyclic
```

**`SheafOfModules.dgHull_unit_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedForgetRightAdjoint.lean, line 714](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedForgetRightAdjoint.lean#L714). The attribute's comment: “part (1)”.

> The unit of the adjunction embeds a right graded module into its differential graded
> hull.

```lean
theorem dgHull_unit_mono (A : DifferentialGradedAlgebra.{t, a} R)
    (N : GradedModule.{t, a, m} A.toGradedAlgebra) :
    Mono ((Adjunction.ofIsRightAdjoint (forgetToGradedModule.{t, a, m} A)).unit.app N)
```

**`SheafOfModules.dgHull_differential_cokernel_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedGrothendieck.lean, line 626](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedGrothendieck.lean#L626). The attribute's comment: “part (2)”.

> **Tag 0FSL, part (2).** The differential of the differential graded hull induces an
> isomorphism from a graded module to the shift by one of the cokernel of the adjunction unit;
> in each homogeneous degree it is the unit followed by the differential and the projection to
> the cokernel.

```lean
theorem dgHull_differential_cokernel_iso :
    ∃ f : GradedModule.ShiftedHom N (cokernel ((Adjunction.ofIsRightAdjoint
        (forgetToGradedModule.{t, a, m} A)).unit.app N)) 1,
      (∀ n : ℤ, IsIso (f.app n)) ∧
      (∀ n : ℤ, HEq (f.app n)
        (((Adjunction.ofIsRightAdjoint (forgetToGradedModule.{t, a, m} A)).unit.app N).app n
          ≫ ((forgetToGradedModule.{t, a, m} A).leftAdjoint.obj N).complex.d n (n + 1)
          ≫ (cokernel.π ((Adjunction.ofIsRightAdjoint
              (forgetToGradedModule.{t, a, m} A)).unit.app N)).app (n + 1)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.24, Tag 0FSJ](https://stacks.math.columbia.edu/tag/0FSJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
