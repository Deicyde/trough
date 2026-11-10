---
declaration: section
origin: cited
lean: SheafOfModules.LeftDifferentialGradedModule.opRight, SheafOfModules.DifferentialGradedModule.opLeft, SheafOfModules.DifferentialGradedModule.unopLeft, SheafOfModules.DifferentialGradedModule, SheafOfModules.DifferentialGradedModule.Hom, SheafOfModules.LeftDifferentialGradedModule, SheafOfModules.LeftDifferentialGradedModule.Hom, SheafOfModules.differentialGradedModule_abelian_ab5_hasLimits_hasColimits_forget
statement: formalized
proof: formalized
---

# 24.13 Sheaves of differential graded modules

Section 24.13 of the Stacks Project, [Tag 0FRH](https://stacks.math.columbia.edu/tag/0FRH). 3 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FRI, a definition

[Tag 0FRI](https://stacks.math.columbia.edu/tag/0FRI) in the Stacks Project.

**`SheafOfModules.LeftDifferentialGradedModule.opRight`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedOppositeModule.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedOppositeModule.lean#L210). The attribute's comment: “left differential graded modules as right modules over the opposite algebra”.

> **A left differential graded `A`-module read as a right differential graded
> `A.op`-module.** The cochain complex is unchanged and the action is interchanged and twisted by
> the Koszul sign.

```lean
noncomputable def opRight : DifferentialGradedModule.{t, a, w} A.op
```

**`SheafOfModules.DifferentialGradedModule.opLeft`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedOppositeModule.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedOppositeModule.lean#L313). The attribute's comment: “right differential graded modules as left modules over the opposite algebra”.

> **A right differential graded `A`-module read as a left differential graded
> `A.op`-module.** The cochain complex is unchanged and the action is interchanged and twisted by
> the Koszul sign.

```lean
noncomputable def opLeft : LeftDifferentialGradedModule.{t, a, w} A.op
```

**`SheafOfModules.DifferentialGradedModule.unopLeft`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedOppositeModule.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedOppositeModule.lean#L417). The attribute's comment: “right differential graded modules over the opposite algebra as left modules”.

> **A right differential graded `A.op`-module read as a left differential graded
> `A`-module.** The cochain complex is unchanged and the action is interchanged and twisted by the
> Koszul sign.

```lean
noncomputable def unopLeft : LeftDifferentialGradedModule.{t, a, w} A
```

**`SheafOfModules.DifferentialGradedModule`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedForgetColimits.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedForgetColimits.lean#L302). The attribute's comment: “right differential graded modules”.

> A right differential graded module over a sheaf of differential graded algebras.

```lean
structure DifferentialGradedModule (A : DifferentialGradedAlgebra.{t, a} R)
```

**`SheafOfModules.DifferentialGradedModule.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedForgetColimits.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedForgetColimits.lean#L331). The attribute's comment: “homomorphisms of differential graded modules”.

> A morphism of right differential graded modules.

```lean
structure Hom (M N : DifferentialGradedModule.{t, a, m} A)
```

**`SheafOfModules.LeftDifferentialGradedModule`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDifferentialGradedModule.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDifferentialGradedModule.lean#L64). The attribute's comment: “left differential graded modules”.

> A left differential graded module over a sheaf of differential graded algebras. The sign in
> the Leibniz rule is determined by the degree of the algebra section.

```lean
structure LeftDifferentialGradedModule (A : DifferentialGradedAlgebra.{t, a} R)
```

**`SheafOfModules.LeftDifferentialGradedModule.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDifferentialGradedModule.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDifferentialGradedModule.lean#L93). The attribute's comment: “homomorphisms of left differential graded modules”.

> A morphism of left differential graded modules.

```lean
structure Hom (M N : LeftDifferentialGradedModule.{t, a, m} A)
```

## Tag 0FRJ, a lemma

[Tag 0FRJ](https://stacks.math.columbia.edu/tag/0FRJ) in the Stacks Project.

**`SheafOfModules.differentialGradedModule_abelian_ab5_hasLimits_hasColimits_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedModuleCategoryProperties.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedModuleCategoryProperties.lean#L107).

> **Stacks 0FRJ.** Let `R` be a sheaf of rings on a site `(C, J)` and let `A` be a sheaf of
> differential graded `R`-algebras. The category `Mod(A, d)` of right differential graded
> `A`-modules is abelian and has
>
> 1. arbitrary direct sums,
> 2. arbitrary colimits,
> 3. exact filtered colimits,
> 4. arbitrary products,
> 5. arbitrary limits,
>
> and the functor `Mod(A, d) ⥤ Mod(A)` forgetting the differential commutes with all limits and
> with all colimits.
>
> Abelianness is phrased as `Nonempty (Abelian _)` because `CategoryTheory.Abelian` is data; the
> seven remaining clauses are propositions on the nose.

```lean
theorem differentialGradedModule_abelian_ab5_hasLimits_hasColimits_forget
    (A : DifferentialGradedAlgebra.{t, a} R)
    [HasSheafify J AddCommGrpCat.{m}] [J.WEqualsLocallyBijective AddCommGrpCat.{m}] :
    Nonempty (Abelian (DifferentialGradedModule.{t, a, m} A)) ∧
      HasCoproducts.{m} (DifferentialGradedModule.{t, a, m} A) ∧
      HasColimitsOfSize.{m, m} (DifferentialGradedModule.{t, a, m} A) ∧
      AB5OfSize.{m, m} (DifferentialGradedModule.{t, a, m} A) ∧
      HasProducts.{m} (DifferentialGradedModule.{t, a, m} A) ∧
      HasLimitsOfSize.{m, m} (DifferentialGradedModule.{t, a, m} A) ∧
      PreservesLimitsOfSize.{s₁, s₂} (forgetToGradedModule.{t, a, m} A) ∧
      PreservesColimitsOfSize.{s₁, s₂} (forgetToGradedModule.{t, a, m} A)
```

## Tag 0FRK, an equation

[Tag 0FRK](https://stacks.math.columbia.edu/tag/0FRK) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.toCochainComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCohomologySequence.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCohomologySequence.lean#L138). The attribute's comment: “underlying short exact sequence”.

> **A short exact sequence of differential graded modules has an underlying short exact
> sequence of cochain complexes of sheaves of modules.**

```lean
theorem toCochainComplex_shortExact
    (S : ShortComplex (DifferentialGradedModule.{t, a, m} A)) (hS : S.ShortExact) :
    (S.map (toCochainComplex.{t, a, m} A)).ShortExact
```

**`SheafOfModules.DifferentialGradedModule.cohomologyExactAtFirst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCohomologySequence.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCohomologySequence.lean#L155). The attribute's comment: “exactness at the first cohomology sheaf”.

> Exactness of the cohomology sequence at the cohomology of the first module, including the
> connecting map from the preceding degree.

```lean
theorem cohomologyExactAtFirst
    (S : ShortComplex (DifferentialGradedModule.{t, a, m} A)) (hS : S.ShortExact) (n : ℤ) :
    (ShortComplex.mk
      ((toCochainComplex_shortExact A S hS).δ (n - 1) n (by simp))
      (HomologicalComplex.homologyMap S.f.toHomologicalComplex n)
      ((toCochainComplex_shortExact A S hS).δ_comp (n - 1) n (by simp))).Exact
```

**`SheafOfModules.DifferentialGradedModule.cohomologyExactAtMiddle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCohomologySequence.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCohomologySequence.lean#L165). The attribute's comment: “exactness at the middle cohomology sheaf”.

> Exactness of the cohomology sequence at the cohomology of the middle module.

```lean
theorem cohomologyExactAtMiddle
    (S : ShortComplex (DifferentialGradedModule.{t, a, m} A)) (hS : S.ShortExact) (n : ℤ) :
    ((S.map (toCochainComplex.{t, a, m} A)).map
      (HomologicalComplex.homologyFunctor (SheafOfModules.{m} R) (ComplexShape.up ℤ) n)).Exact
```

**`SheafOfModules.DifferentialGradedModule.cohomologyExactAtThird`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCohomologySequence.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCohomologySequence.lean#L174). The attribute's comment: “exactness at the third cohomology sheaf”.

> Exactness of the cohomology sequence at the cohomology of the third module, before the
> canonical connecting map to the next degree.

```lean
theorem cohomologyExactAtThird
    (S : ShortComplex (DifferentialGradedModule.{t, a, m} A)) (hS : S.ShortExact) (n : ℤ) :
    (ShortComplex.mk
      (HomologicalComplex.homologyMap S.g.toHomologicalComplex n)
      ((toCochainComplex_shortExact A S hS).δ n (n + 1) (by simp))
      ((toCochainComplex_shortExact A S hS).comp_δ n (n + 1) (by simp))).Exact
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.13, Tag 0FRH](https://stacks.math.columbia.edu/tag/0FRH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
