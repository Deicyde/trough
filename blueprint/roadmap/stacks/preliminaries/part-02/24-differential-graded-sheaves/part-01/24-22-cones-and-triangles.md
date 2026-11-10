---
declaration: section
origin: cited
lean: SheafOfModules.DifferentialGradedModule.hasZeroObject, SheafOfModules.DifferentialGradedModule.hasBinaryBiproducts, SheafOfModules.DifferentialGradedModule.shiftAxiomB, SheafOfModules.DifferentialGradedModule.shiftPackage_nonempty, SheafOfModules.DifferentialGradedModule.conePackage_nonempty, SheafOfModules.DifferentialGradedModule.conePackage, SheafOfModules.DifferentialGradedModule.coneSituation, SheafOfModules.DifferentialGradedModule.HomotopyCategory.instHasShift
statement: formalized
proof: formalized
---

# 24.22 Cones and triangles

Section 24.22 of the Stacks Project, [Tag 0FS3](https://stacks.math.columbia.edu/tag/0FS3). 6 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FS4, a lemma

[Tag 0FS4](https://stacks.math.columbia.edu/tag/0FS4) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.hasZeroObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAxiomA.lean, line 740](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAxiomA.lean#L740). The attribute's comment: “axiom\_a”.

> The zero differential graded module has unique homogeneous maps to and from every object in
> every degree.

```lean
theorem hasZeroObject :
    ∃ Z : (dgCategoryData A).category.Obj,
      (∀ (M : (dgCategoryData A).category.Obj) (n : ℤ),
        Nonempty ((dgCategoryData A).category.Hom Z M n) ∧
          Subsingleton ((dgCategoryData A).category.Hom Z M n)) ∧
      (∀ (M : (dgCategoryData A).category.Obj) (n : ℤ),
        Nonempty ((dgCategoryData A).category.Hom M Z n) ∧
          Subsingleton ((dgCategoryData A).category.Hom M Z n))
```

**`SheafOfModules.DifferentialGradedModule.hasBinaryBiproducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAxiomA.lean, line 856](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAxiomA.lean#L856). The attribute's comment: “axiom\_a”.

> Any two right differential graded modules admit a differential graded direct sum with closed
> degree-zero structure maps.

```lean
theorem hasBinaryBiproducts
    (M N : (dgCategoryData A).category.Obj) :
    Nonempty (DGCategory.BinaryBiproductData (dgCategoryData A).category M N)
```

**`SheafOfModules.DifferentialGradedModule.shiftAxiomB`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAxiomB.lean, line 1421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAxiomB.lean#L1421). The attribute's comment: “axiom\_b”.

> The canonical DG shifts and Hom-complex shift isomorphisms for sheaf DG modules.

```lean
noncomputable def shiftAxiomB : CanonicalShiftAxiomB.{u, v, w} A
```

## Tag 0FS5, a definition

[Tag 0FS5](https://stacks.math.columbia.edu/tag/0FS5) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.shiftPackage_nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCone.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCone.lean#L324). The attribute's comment: “fixed shifted module for the canonical cone projection”.

> The degree-one shift of a right differential graded module exists with
> the unchanged right action.

```lean
theorem shiftPackage_nonempty {A : DifferentialGradedAlgebra.{t, a} R}
    (K : DifferentialGradedModule.{t, a, m} A) : Nonempty (ShiftPackage K)
```

**`SheafOfModules.DifferentialGradedModule.conePackage_nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCone.lean, line 613](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCone.lean#L613). The attribute's comment: “existence of the cone with its canonical maps”.

> The mapping-cone construction exists with its componentwise action and
> canonical inclusion and projection.

```lean
theorem conePackage_nonempty {A : DifferentialGradedAlgebra.{t, a} R}
    {K L : DifferentialGradedModule.{t, a, m} A} (f : K ⟶ L) : Nonempty (ConePackage f)
```

**`SheafOfModules.DifferentialGradedModule.conePackage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCone.lean, line 695](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCone.lean#L695). The attribute's comment: “the cone construction”.

> The cone and its canonical maps, characterized by the
> mapping-cone complex and the direct-sum action.

```lean
noncomputable def conePackage {A : DifferentialGradedAlgebra.{t, a} R}
    {K L : DifferentialGradedModule.{t, a, m} A} (f : K ⟶ L) : ConePackage f
```

## Tag 0FS6, a lemma

[Tag 0FS6](https://stacks.math.columbia.edu/tag/0FS6) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.coneSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAxiomC.lean, line 861](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAxiomC.lean#L861).

> The differential graded category of right sheaf modules admits cones whose connecting
> arrows are the shifts of the original morphisms, using the fixed axiom (B) shift.

```lean
theorem coneSituation {X : AlgebraicGeometry.RingedSite.{u, u, u}}
    (A : DifferentialGradedAlgebra.{u, v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    ∃ S : DGCategory.ConeSituation
        (dgCategoryData.{u, v, w} A).category,
      S.shift = (shiftAxiomB A).axiomB
```

## Tag 0FS7, a proposition

[Tag 0FS7](https://stacks.math.columbia.edu/tag/0FS7) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.HomotopyCategory.instHasShift`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean, line 702](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean#L702). The attribute's comment: “part (1): the shift functors”.

> The translation functors of the homotopy category of right differential graded modules,
> lifted from the differential graded shifts along the identification of the two homotopy
> categories.

```lean
noncomputable instance instHasShift : HasShift (HomotopyCategory.{u, v, w} A) ℤ
```

**`SheafOfModules.DifferentialGradedModule.HomotopyCategory.instPretriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean, line 727](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean#L727). The attribute's comment: “the pre-triangulated structure”.

> The homotopy category of right differential graded modules is pretriangulated.

```lean
noncomputable instance instPretriangulated :
    Pretriangulated (HomotopyCategory.{u, v, w} A)
```

**`SheafOfModules.DifferentialGradedModule.HomotopyCategory.instIsTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean, line 734](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean#L734).

> **Tag 0FS7.** The homotopy category of right differential graded modules over a sheaf of
> differential graded algebras on a ringed site is a triangulated category.

```lean
instance instIsTriangulated : IsTriangulated (HomotopyCategory.{u, v, w} A)
```

**`SheafOfModules.DifferentialGradedModule.HomotopyCategory.distinguished_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean, line 795](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean#L795). The attribute's comment: “part (2): the distinguished triangles”.

> A triangle of the homotopy category of right differential graded modules is distinguished
> exactly when it is isomorphic to the triangle built from an admissible short exact sequence of
> right differential graded modules, the connecting arrow being the class of `π d s`.

```lean
theorem distinguished_iff (T : Pretriangulated.Triangle (HomotopyCategory.{u, v, w} A)) :
    T ∈ Pretriangulated.distinguishedTriangles (C := HomotopyCategory.{u, v, w} A) ↔
      ∃ (M N P : DifferentialGradedModule.{u, v, w} A) (f : M ⟶ N) (g : N ⟶ P)
        (δ : (quotient A).obj P ⟶
          (shiftFunctor (HomotopyCategory.{u, v, w} A) (1 : ℤ)).obj ((quotient A).obj M))
        (E : DGCategory.GradedSplitShortExact (A := (dgCategoryData.{u, v, w} A).category)
          (asObject A M) (asObject A N) (asObject A P)),
        cocycleOfHom A (dgCategoryData A) f = E.a ∧
          cocycleOfHom A (dgCategoryData A) g = E.b ∧
          Nonempty (T ≅ Pretriangulated.Triangle.mk ((quotient A).map f)
            ((quotient A).map g) δ) ∧
          Nonempty ((homotopyCategoryToDG A).mapTriangle.obj
              (Pretriangulated.Triangle.mk ((quotient A).map f) ((quotient A).map g) δ) ≅
            DGCategory.GradedSplitShortExact.associatedKTriangle
              (dgConeSituation A).shift E)
```

**`SheafOfModules.DifferentialGradedModule.HomotopyCategory.shiftFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean, line 828](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedHomotopyCategoryTriangulated.lean#L828). The attribute's comment: “part (1): the shift functors are those of Section 24.20”.

> The degree-one translation of the homotopy category is the shift of differential graded
> modules of Stacks 0FS5.

```lean
theorem shiftFunctor_obj (M : DifferentialGradedModule.{u, v, w} A) :
    (shiftFunctor (HomotopyCategory.{u, v, w} A) (1 : ℤ)).obj ((quotient A).obj M) =
      (quotient A).obj (shift M)
```

## Tag 0FS8, a remark

[Tag 0FS8](https://stacks.math.columbia.edu/tag/0FS8) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.coneIdentity_hom_equiv_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeIdentity.lean, line 944](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeIdentity.lean#L944).

> A morphism from the identity cone is uniquely specified by a pair of global
> sections `(x,y)` with `x = d y`; the equivalence evaluates at the canonical
> unit elements in degrees zero and minus one.

```lean
theorem coneIdentity_hom_equiv_sections (A : DifferentialGradedAlgebra.{t, a} R)
    (M : DifferentialGradedModule.{t, a, a} A) :
    ∃ e : (identityCone A ⟶ M) ≃
        { p : (M.complex.X 0).sections × (M.complex.X (-1)).sections //
          ∀ U : Cᵒᵖ,
            p.1.eval U =
              (M.complex.d (-1) 0).val.app U (p.2.eval U) },
      ∀ (f : identityCone A ⟶ M) (U : Cᵒᵖ),
        (e f).1.1.eval U =
          (f.toHomologicalComplex.f 0).val.app U
            (((conePackage (𝟙 (regularModule A))).componentIso 0).inv.val.app U
              ((biprod.inr : (regularModule A).complex.X 0 ⟶
                  (regularModule A).complex.X 1 ⊞ (regularModule A).complex.X 0).val.app U
                (A.one.eval U))) ∧
        (e f).1.2.eval U =
          (f.toHomologicalComplex.f (-1)).val.app U
            (((conePackage (𝟙 (regularModule A))).componentIso (-1)).inv.val.app U
              ((biprod.inl : (regularModule A).complex.X 0 ⟶
                  (regularModule A).complex.X 0 ⊞ (regularModule A).complex.X (-1)).val.app U
                (A.one.eval U)))
```

## Tag 0FS9, a lemma

[Tag 0FS9](https://stacks.math.columbia.edu/tag/0FS9) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.isGrothendieckAbelian`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedGrothendieck.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedGrothendieck.lean#L129).

> **Stacks Project, Tag 0FS9.** Let `(C, O)` be a ringed site and let `(A, d)` be a
> differential graded `O`-algebra. The category `Mod(A, d)` of right differential graded
> `A`-modules is a Grothendieck abelian category.
>
> It is abelian and has filtered colimits by Tag 0FRJ, those colimits are exact by
> `filteredColimits_exact`, it is locally small, and it has the separator
> `⨁_{k, U} j_{U!} C_U[k]`, the direct sum of the shifts of the cones on the identities of the
> restrictions of `A` to the objects of the site.

```lean
noncomputable instance isGrothendieckAbelian (A : DifferentialGradedAlgebra.{t, a} R) :
    IsGrothendieckAbelian.{max u v a w} (DifferentialGradedModule.{t, a, max u v a w} A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.22, Tag 0FS3](https://stacks.math.columbia.edu/tag/0FS3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
