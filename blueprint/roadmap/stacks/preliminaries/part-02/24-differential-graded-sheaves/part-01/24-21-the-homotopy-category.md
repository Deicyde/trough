---
declaration: section
origin: cited
lean: SheafOfModules.DifferentialGradedModule.homotopyCategoryEquivalence, SheafOfModules.DifferentialGradedModule.homotopyCategoryEquivalence_obj, SheafOfModules.DifferentialGradedModule.homotopyCategoryEquivalence_map, SheafOfModules.DifferentialGradedModule.Homotopy, SheafOfModules.DifferentialGradedModule.Homotopic, SheafOfModules.DifferentialGradedModule.HomotopyCategory, SheafOfModules.DifferentialGradedModule.homotopic_congruence, SheafOfModules.DifferentialGradedModule.HomotopyCategory.hasProducts
statement: formalized
proof: formalized
---

# 24.21 The homotopy category

Section 24.21 of the Stacks Project, [Tag 0FRZ](https://stacks.math.columbia.edu/tag/0FRZ). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FRZ, the section

[Tag 0FRZ](https://stacks.math.columbia.edu/tag/0FRZ) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.homotopyCategoryEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean, line 571](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean#L571).

> The homotopy category of right differential graded modules over a sheaf of differential
> graded algebras is the homotopy category of their differential graded category.

```lean
noncomputable def homotopyCategoryEquivalence :
    HomotopyCategory.{u, v, w} A ≌ (dgCategoryData.{u, v, w} A).category.K
```

**`SheafOfModules.DifferentialGradedModule.homotopyCategoryEquivalence_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean, line 578](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean#L578).

> The identification of the two homotopy categories sends a differential graded module to
> itself.

```lean
theorem homotopyCategoryEquivalence_obj (M : DifferentialGradedModule.{u, v, w} A) :
    (homotopyCategoryEquivalence A).functor.obj ((HomotopyCategory.quotient A).obj M) =
      asObject A M
```

**`SheafOfModules.DifferentialGradedModule.homotopyCategoryEquivalence_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean, line 586](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean#L586).

> The identification of the two homotopy categories sends the homotopy class of a morphism
> to the homotopy class of the closed degree-zero homogeneous map with the same underlying
> cochain.

```lean
theorem homotopyCategoryEquivalence_map {M N : DifferentialGradedModule.{u, v, w} A}
    (f : M ⟶ N) :
    ∃ c : (dgCategoryData.{u, v, w} A).category.Cocycle (asObject A M) (asObject A N),
      HEq (asCochain A c.val) (Cochain.ofHom f.toHomologicalComplex) ∧
        HEq ((homotopyCategoryEquivalence A).functor.map
            ((HomotopyCategory.quotient A).map f))
          (Quotient.mk ((dgCategoryData A).category.homotopySetoid _ _) c)
```

## Tag 0FS0, a definition

[Tag 0FS0](https://stacks.math.columbia.edu/tag/0FS0) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.Homotopy`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopy.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopy.lean#L58). The attribute's comment: “homotopies”.

> A homotopy between two morphisms of right differential graded modules: a map of graded
> modules of degree `-1` whose commutator with the differentials is the difference of the two
> morphisms.

```lean
structure Homotopy {M N : DifferentialGradedModule.{t, a, m} A} (f g : M ⟶ N)
```

**`SheafOfModules.DifferentialGradedModule.Homotopic`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopy.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopy.lean#L74). The attribute's comment: “homotopic morphisms”.

> Two morphisms of right differential graded modules are homotopic if there is a homotopy
> between them.

```lean
abbrev Homotopic {M N : DifferentialGradedModule.{t, a, m} A} (f g : M ⟶ N) : Prop
```

## Tag 0FS1, a definition

[Tag 0FS1](https://stacks.math.columbia.edu/tag/0FS1) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.HomotopyCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategory.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategory.lean#L149). The attribute's comment: “the homotopy category”.

> The homotopy category of right differential graded modules over a sheaf of differential
> graded algebras: the quotient of the category of right differential graded modules by the
> homotopy relation.

```lean
abbrev HomotopyCategory (A : DifferentialGradedAlgebra.{t, a} R) : Type _
```

**`SheafOfModules.DifferentialGradedModule.homotopic_congruence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategory.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategory.lean#L155). The attribute's comment: “homotopy classes form a congruence”.

> Being homotopic is an equivalence relation compatible with composition on either side.

```lean
theorem homotopic_congruence (A : DifferentialGradedAlgebra.{t, a} R) :
    CategoryTheory.Congruence
      (fun {M N : DifferentialGradedModule.{t, a, m} A} (f g : M ⟶ N) => Homotopic f g)
```

## Tag 0FS2, a lemma

[Tag 0FS2](https://stacks.math.columbia.edu/tag/0FS2) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.HomotopyCategory.hasProducts`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryProducts.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryProducts.lean#L108). The attribute's comment: “homotopy\_products”.

> The homotopy category of right differential graded modules admits arbitrary products.

```lean
noncomputable instance hasProducts (A : DifferentialGradedAlgebra.{t, a} R) :
    HasProducts.{m} (HomotopyCategory.{t, a, m} A)
```

**`SheafOfModules.DifferentialGradedModule.HomotopyCategory.hasCoproducts_ringedSite`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryRingedSite.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryRingedSite.lean#L120). The attribute's comment: “homotopy\_direct\_sums”.

> The homotopy category of right differential graded modules over a sheaf of differential
> graded algebras on a ringed site admits arbitrary direct sums.
>
> No side condition is carried: the two sheafification conditions of
> `SheafOfModules.DifferentialGradedModule.HomotopyCategory.hasCoproducts` are discharged here
> from the essential smallness of the site.

```lean
instance hasCoproducts_ringedSite {X : AlgebraicGeometry.RingedSite.{u, v, w}}
    (A : DifferentialGradedAlgebra.{w, a} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    HasCoproducts.{max u v m} (HomotopyCategory.{w, a, max u v m} A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.21, Tag 0FRZ](https://stacks.math.columbia.edu/tag/0FRZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
