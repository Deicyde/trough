---
declaration: section
origin: cited
lean: DifferentialGradedModule.acyclic, DifferentialGradedModule.quasiIsomorphisms, DifferentialGradedModule.quasiIsomorphisms_map_iff, DifferentialGradedModule.acyclic_isClosedUnderIsomorphisms, DifferentialGradedModule.degreeZeroCohomologyDescent, DifferentialGradedModule.acyclic_isTriangulated, DifferentialGradedModule.acyclic_isSaturated, DifferentialGradedModule.acyclic_trW_eq_quasiIsomorphisms
statement: formalized
proof: formalized
---

# 22.22 The derived category

Section 22.22 of the Stacks Project, [Tag 09KV](https://stacks.math.columbia.edu/tag/09KV). 5 tags here are carried by 33 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09KW, a lemma

[Tag 09KW](https://stacks.math.columbia.edu/tag/09KW) in the Stacks Project.

**`DifferentialGradedModule.acyclic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean#L102). The attribute's comment: “acyclic subcategory”.

> The acyclic differential graded modules, as a class of objects of the
> homotopy category of right differential graded `A`-modules.

```lean
def acyclic : ObjectProperty (HomotopyCategory.{u, v, w} A)
```

**`DifferentialGradedModule.quasiIsomorphisms`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean#L109). The attribute's comment: “quasi-isomorphisms”.

> The quasi-isomorphisms in the homotopy category of right differential graded
> `A`-modules: those morphisms all of whose representing homomorphisms are
> quasi-isomorphisms of the underlying cochain complexes.

```lean
def quasiIsomorphisms : MorphismProperty (HomotopyCategory.{u, v, w} A)
```

**`DifferentialGradedModule.quasiIsomorphisms_map_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean#L221). The attribute's comment: “quasi-isomorphisms represented by DG-module maps”.

> A homomorphism of differential graded modules induces a quasi-isomorphism in the
> homotopy category exactly when it is a quasi-isomorphism of the underlying cochain
> complexes.

```lean
theorem quasiIsomorphisms_map_iff {M N : DifferentialGradedModule.{u, v, w} A} (g : M ⟶ N) :
    quasiIsomorphisms A ((toHomotopyCategory A).map g) ↔
      QuasiIso ((forgetToCochainComplex A).map g)
```

**`DifferentialGradedModule.acyclic_isClosedUnderIsomorphisms`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean#L231). The attribute's comment: “strict fullness”.

> Acyclicity is invariant under isomorphism in the homotopy category: an isomorphism there
> is represented by a homotopy equivalence of the underlying cochain complexes, so it induces
> isomorphisms on all homology.

```lean
instance acyclic_isClosedUnderIsomorphisms :
    (acyclic.{u, v, w} A).IsClosedUnderIsomorphisms
```

**`DifferentialGradedModule.degreeZeroCohomologyDescent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean#L324). The attribute's comment: “factorization of degree-zero cohomology”.

> Degree-zero cohomology of differential graded modules factors through the homotopy
> category, and the resulting functor factors in turn through the localization at the
> quasi-isomorphisms.  Both factorizations are the universal ones: the first is the lift along
> the quotient by homotopy, available because homotopic homomorphisms agree on cohomology, and
> the second is the lift along the localization functor, available because a quasi-isomorphism
> becomes invertible on cohomology.

```lean
noncomputable def degreeZeroCohomologyDescent :
    DegreeZeroCohomologyDescent.{u, v, w} A
```

**`DifferentialGradedModule.acyclic_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean, line 599](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean#L599). The attribute's comment: “triangulated subcategory”.

> Acyclic differential graded modules form a triangulated subcategory of the homotopy category:
> they are the objects killed by degree-zero cohomology in every shift, and degree-zero cohomology
> is a homological functor.

```lean
instance acyclic_isTriangulated : (acyclic.{u, v, w} A).IsTriangulated
```

**`DifferentialGradedModule.acyclic_isSaturated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean, line 607](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean#L607). The attribute's comment: “saturation of acyclic modules”.

> The triangulated subcategory of acyclic differential graded modules is saturated: the kernel of
> a homological functor is stable under retracts, and a direct summand is a retract.

```lean
instance acyclic_isSaturated : (acyclic.{u, v, w} A).IsSaturated
```

**`DifferentialGradedModule.acyclic_trW_eq_quasiIsomorphisms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean, line 629](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean#L629). The attribute's comment: “associated multiplicative system”.

> The morphisms of the homotopy category whose cone is acyclic are exactly the
> quasi-isomorphisms.

```lean
theorem acyclic_trW_eq_quasiIsomorphisms :
    (acyclic.{u, v, w} A).trW = quasiIsomorphisms.{u, v, w} A
```

**`DifferentialGradedModule.quasiIsomorphisms_isSaturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean, line 672](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean#L672). The attribute's comment: “saturated multiplicative system”.

> The quasi-isomorphisms of the homotopy category of right differential graded `A`-modules form
> a saturated multiplicative system: they are the morphisms whose cone lies in the kernel of
> degree-zero cohomology, and the multiplicative system attached to the kernel of a homological
> functor on a triangulated category is saturated.

```lean
theorem quasiIsomorphisms_isSaturated : (quasiIsomorphisms.{u, v, w} A).IsSaturated
```

**`DifferentialGradedModule.localization_kernel_eq_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean, line 683](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean#L683). The attribute's comment: “kernel of localization”.

> The objects of the homotopy category annihilated by the localization at the
> quasi-isomorphisms are exactly the acyclic differential graded modules: the acyclic modules are a
> strictly full saturated triangulated subcategory, and such a subcategory is the kernel of the
> localization at the multiplicative system it determines.

```lean
theorem localization_kernel_eq_acyclic :
    ((quasiIsomorphisms.{u, v, w} A).Q).kernel = acyclic.{u, v, w} A
```

**`DifferentialGradedModule.quasiIsomorphisms_iff_forall_isIso_degreeZeroCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategoryIsoDetection.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategoryIsoDetection.lean#L82). The attribute's comment: “cohomology detects quasi-isomorphisms”.

> **Cohomology detects quasi-isomorphisms on the homotopy category.** A morphism of `K(A, d)` is
> a quasi-isomorphism exactly when degree-zero cohomology of each of its shifts is an isomorphism.
> No representability is assumed of the morphism.

```lean
theorem quasiIsomorphisms_iff_forall_isIso_degreeZeroCohomology {X Y : HomotopyCategory A}
    (g : X ⟶ Y) :
    quasiIsomorphisms' A g ↔
      ∀ n : ℤ, IsIso ((degreeZeroCohomologyOnHomotopy' A).map (g⟦n⟧'))
```

**`DifferentialGradedModule.acyclic'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean#L446). The attribute's comment: “acyclic subcategory”.

> The acyclic differential graded modules, as objects of the homotopy category.

```lean
def acyclic' : ObjectProperty (HomotopyCategory.{u, u, u} A)
```

**`DifferentialGradedModule.quasiIsomorphisms'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean, line 451](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean#L451). The attribute's comment: “quasi-isomorphisms”.

> The quasi-isomorphisms in the homotopy category of differential graded modules.

```lean
def quasiIsomorphisms' :
    MorphismProperty (HomotopyCategory.{u, u, u} A)
```

**`DifferentialGradedModule.degreeZeroCohomologyDescent'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean, line 501](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean#L501). The attribute's comment: “factorization of degree-zero cohomology”.

> The canonical descent data for degree-zero cohomology.

```lean
noncomputable def degreeZeroCohomologyDescent' :
    DegreeZeroCohomologyDescent' A
```

**`DifferentialGradedModule.quasiIsomorphisms_map_iff'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean, line 537](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean#L537). The attribute's comment: “quasi-isomorphisms represented by DG-module maps”.

> A DG-module map induces a quasi-isomorphism in the homotopy category
> exactly when it is a quasi-isomorphism of the underlying cochain complexes.

```lean
theorem quasiIsomorphisms_map_iff'
    {M N : DifferentialGradedModule.{u, u, u} A} (g : M ⟶ N) :
    quasiIsomorphisms' A ((toHomotopyCategory.{u, u, u} A).map g) ↔
      QuasiIso ((forgetToCochainComplex A).map g)
```

**`DifferentialGradedModule.acyclic_isClosedUnderIsomorphisms'`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean, line 546](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean#L546). The attribute's comment: “strict fullness”.

> Acyclicity is invariant under isomorphism in the homotopy category.

```lean
instance acyclic_isClosedUnderIsomorphisms' :
    (acyclic' A).IsClosedUnderIsomorphisms
```

**`DifferentialGradedModule.acyclic_isTriangulated'`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean, line 570](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean#L570). The attribute's comment: “triangulated subcategory”.

> Acyclic differential graded modules form a triangulated subcategory.

```lean
instance acyclic_isTriangulated' : (acyclic' A).IsTriangulated
```

**`DifferentialGradedModule.acyclic_isSaturated'`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean, line 578](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean#L578). The attribute's comment: “saturation of acyclic modules”.

> The triangulated subcategory of acyclic modules is saturated.

```lean
instance acyclic_isSaturated' : (acyclic' A).IsSaturated
```

**`DifferentialGradedModule.acyclic_trW_eq_quasiIsomorphisms'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean, line 620](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean#L620). The attribute's comment: “associated multiplicative system”.

> The morphisms whose cones are acyclic are exactly the quasi-isomorphisms.

```lean
theorem acyclic_trW_eq_quasiIsomorphisms' :
    (acyclic' A).trW = quasiIsomorphisms' A
```

**`DifferentialGradedModule.quasiIsomorphisms_isSaturated'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean, line 652](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean#L652). The attribute's comment: “saturated multiplicative system”.

> Quasi-isomorphisms form a saturated multiplicative system.

```lean
theorem quasiIsomorphisms_isSaturated' :
    (quasiIsomorphisms' A).IsSaturated
```

**`DifferentialGradedModule.localization_kernel_eq_acyclic'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean, line 664](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean#L664). The attribute's comment: “kernel of localization”.

> The objects annihilated by localization at quasi-isomorphisms are exactly
> the acyclic differential graded modules.

```lean
theorem localization_kernel_eq_acyclic' :
    ((quasiIsomorphisms' A).Q).kernel = acyclic' A
```

## Tag 09KX, a definition

[Tag 09KX](https://stacks.math.columbia.edu/tag/09KX) in the Stacks Project.

**`DifferentialGradedModule.derivedCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/DerivedCategory.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/DerivedCategory.lean#L70). The attribute's comment: “derived category”.

> The derived category of a differential graded algebra `A`: the localization of the homotopy
> category of right differential graded `A`-modules at the quasi-isomorphisms.

```lean
abbrev derivedCategory : Type _
```

**`DifferentialGradedModule.derivedCategory_eq_verdierQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/DerivedCategory.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/DerivedCategory.lean#L93). The attribute's comment: “Verdier quotient”.

> The derived category is the Verdier quotient of the homotopy category by the full
> triangulated subcategory of acyclic modules: the two descriptions are localizations of the
> homotopy category at the same class of morphisms, by
> `DifferentialGradedModule.acyclic_trW_eq_quasiIsomorphisms`.

```lean
theorem derivedCategory_eq_verdierQuotient :
    derivedCategory.{u, v, w} A = (acyclic.{u, v, w} A).verdierQuotient
```

**`DifferentialGradedModule.degreeZeroCohomology_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/DerivedCategory.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/DerivedCategory.lean#L108). The attribute's comment: “uniqueness of degree-zero cohomology”.

> Degree-zero cohomology on the derived category is the unique descent of degree-zero
> cohomology on the homotopy category: any functor on the derived category whose composite with the
> localization functor is degree-zero cohomology on the homotopy category is uniquely isomorphic to
> `DifferentialGradedModule.degreeZeroCohomologyOnLocalization`, by an isomorphism compatible with
> the given identification.

```lean
theorem degreeZeroCohomology_unique
    (G : derivedCategory.{u, v, w} A ⥤ ModuleCat.{w} R)
    (α : (quasiIsomorphisms A).Q ⋙ G ≅ degreeZeroCohomologyOnHomotopy A) :
    ∃! e : G ≅ degreeZeroCohomologyOnLocalization A,
      Functor.whiskerLeft (quasiIsomorphisms A).Q e.hom ≫
        (degreeZeroCohomologyOnLocalizationIso A).hom = α.hom
```

**`DifferentialGradedModule.derivedCategory'`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategory.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategory.lean#L82). The attribute's comment: “derived category”.

> The derived category `D(A, d)` of right differential graded `A`-modules: the localization
> of the homotopy category `K(A, d)` at the quasi-isomorphisms.

```lean
abbrev derivedCategory' : Type (u + 1)
```

**`DifferentialGradedModule.derivedCategory_eq_verdierQuotient'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategory.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategory.lean#L106). The attribute's comment: “Verdier quotient”.

> The derived category is the Verdier quotient of the homotopy category by the triangulated
> subcategory of acyclic differential graded modules.

```lean
theorem derivedCategory_eq_verdierQuotient' :
    derivedCategory' A = (acyclic' A).verdierQuotient
```

**`DifferentialGradedModule.degreeZeroCohomology_unique'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategory.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategory.lean#L117). The attribute's comment: “uniqueness of degree-zero cohomology”.

> Degree-zero cohomology on the derived category is the unique descent of degree-zero
> cohomology on the homotopy category: a functor `G` on `D(A, d)` together with an identification
> `α` of its restriction along the quotient functor with
> `DifferentialGradedModule.degreeZeroCohomologyOnHomotopy'` agrees with
> `DifferentialGradedModule.degreeZeroCohomologyOnLocalization'` by a unique natural isomorphism
> compatible with `α`.

```lean
theorem degreeZeroCohomology_unique' (G : derivedCategory' A ⥤ ModuleCat.{u} R)
    (α : (quasiIsomorphisms' A).Q ⋙ G ≅ degreeZeroCohomologyOnHomotopy' A) :
    ∃! e : G ≅ degreeZeroCohomologyOnLocalization' A,
      Functor.whiskerLeft (quasiIsomorphisms' A).Q e.hom ≫
        (degreeZeroCohomologyOnLocalizationIso' A).hom = α.hom
```

Declarations registered for the tag:

- [`DifferentialGradedModule.degreeZeroCohomologyOnLocalization`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean#L341), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/DGA/DerivedCategory.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/DerivedCategory.lean#L97) (StacksFrontier): “degree-zero cohomology”.
- [`DifferentialGradedModule.degreeZeroCohomologyOnLocalizationIso`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/QuasiIsomorphisms.lean#L355), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/DGA/DerivedCategory.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/DerivedCategory.lean#L99) (StacksFrontier): “cohomology factorization”.
- [`DifferentialGradedModule.degreeZeroCohomologyOnLocalization'`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean#L516), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategory.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategory.lean#L98) (StacksFrontier): “degree-zero cohomology on the derived category”.
- [`DifferentialGradedModule.degreeZeroCohomologyOnLocalizationIso'`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/QuasiIsomorphism.lean#L529), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategory.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategory.lean#L100) (StacksFrontier): “factorization of degree-zero cohomology through the derived category”.

## Tag 09KY, a lemma

[Tag 09KY](https://stacks.math.columbia.edu/tag/09KY) in the Stacks Project.

**`DifferentialGradedModule.exists_homEquiv_of_propertyPResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategoryHom.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategoryHom.lean#L136). The attribute's comment: “morphisms\_from\_p\_resolution”.

> **Stacks 09KY(1).** *"Let `P → M` be a P-resolution as in Lemma 09KP. Then
> `Hom_{D(A,d)}(M, N) = Hom_{K(Mod_{(A,d)})}(P, N)`."*
>
> The identification sends a morphism `g : M ⟶ N` of the derived category to the unique morphism
> `P ⟶ N` of the homotopy category whose image in `D(A, d)` is the resolution map followed by
> `g`.

```lean
theorem exists_homEquiv_of_propertyPResolution {P M : DifferentialGradedModule A} (f : P ⟶ M)
    (hf : QuasiIso ((forgetToCochainComplex A).map f))
    (hP : Nonempty (PropertyPFiltration P)) (N : DifferentialGradedModule A) :
    ∃ e : ((quasiIsomorphisms' A).Q.obj ((toHomotopyCategory A).obj M) ⟶
            (quasiIsomorphisms' A).Q.obj ((toHomotopyCategory A).obj N)) ≃
          ((toHomotopyCategory A).obj P ⟶ (toHomotopyCategory A).obj N),
      ∀ g, (quasiIsomorphisms' A).Q.map (e g) =
        (quasiIsomorphisms' A).Q.map ((toHomotopyCategory A).map f) ≫ g
```

**`DifferentialGradedModule.exists_homEquiv_of_propertyIResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategoryHom.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategoryHom.lean#L156). The attribute's comment: “morphisms\_into\_i\_resolution”.

> **Stacks 09KY(2).** *"Let `N → I` be an I-resolution as in Lemma 09KU. Then
> `Hom_{D(A,d)}(M, N) = Hom_{K(Mod_{(A,d)})}(M, I)`."*
>
> The identification sends a morphism `g : M ⟶ N` of the derived category to the unique morphism
> `M ⟶ I` of the homotopy category whose image in `D(A, d)` is `g` followed by the resolution
> map.

```lean
theorem exists_homEquiv_of_propertyIResolution {N I : DifferentialGradedModule A} (f : N ⟶ I)
    (hf : QuasiIso ((forgetToCochainComplex A).map f))
    (hI : Nonempty (PropertyIFiltration I)) (M : DifferentialGradedModule A) :
    ∃ e : ((quasiIsomorphisms' A).Q.obj ((toHomotopyCategory A).obj M) ⟶
            (quasiIsomorphisms' A).Q.obj ((toHomotopyCategory A).obj N)) ≃
          ((toHomotopyCategory A).obj M ⟶ (toHomotopyCategory A).obj I),
      ∀ g, (quasiIsomorphisms' A).Q.map (e g) =
        g ≫ (quasiIsomorphisms' A).Q.map ((toHomotopyCategory A).map f)
```

## Tag 09QI, a lemma

[Tag 09QI](https://stacks.math.columbia.edu/tag/09QI) in the Stacks Project.

**`DifferentialGradedModule.derivedCategoryQ_preservesCoproducts`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategoryCoproducts.lean, line 697](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategoryCoproducts.lean#L697). The attribute's comment: “direct\_sums”.

> **Stacks Tag 09QI**, the direct-sum half: *"direct sums in `D(A, d)` are obtained by taking
> direct sums of differential graded modules"*, in the form that the canonical functor
> `Mod_{(A,d)} ⥤ D(A, d)` — the quotient by homotopy followed by the localization at the
> quasi-isomorphisms — preserves direct sums. Preservation of colimits of discrete diagrams
> records both that the image of a direct sum is a direct sum and that its coproduct injections
> are the images of the canonical ones.
>
> The family is replaced by a family of property-(P) resolutions `Pᵢ → Mᵢ`: the direct sum of
> those resolutions is again a quasi-isomorphism, so the two diagrams have isomorphic images in
> `D(A, d)`, and the image of `⨁ᵢ Pᵢ` is a direct sum because `⨁ᵢ Pᵢ` is orthogonal on the left
> to the acyclic modules.

```lean
instance derivedCategoryQ_preservesCoproducts (A : DifferentialGradedAlgebra R) (ι : Type u) :
    PreservesColimitsOfShape (Discrete ι)
      (toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q)
```

**`DifferentialGradedModule.derivedCategoryQ_preservesProducts`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategoryProducts.lean, line 539](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategoryProducts.lean#L539). The attribute's comment: “products”.

> *"Products in `D(A, d)` are obtained by taking products of differential graded modules"*,
> in the form that the canonical functor
> `Mod_{(A,d)} ⥤ D(A, d)` — the quotient by homotopy followed by the localization at the
> quasi-isomorphisms — preserves products. Preservation of limits of discrete diagrams records both
> that the image of a product is a product and that its projections are the images of the canonical
> ones, including for the empty family.

```lean
instance derivedCategoryQ_preservesProducts (A : DifferentialGradedAlgebra.{u, u} R) (ι : Type u) :
    PreservesLimitsOfShape (Discrete ι)
      (toHomotopyCategory.{u, u, u} A ⋙ (quasiIsomorphisms' A).Q)
```

## Tag 0FQE, a remark

[Tag 0FQE](https://stacks.math.columbia.edu/tag/0FQE) in the Stacks Project.

**`DifferentialGradedModule.property_of_coproducts_of_two_out_of_three_of_shifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategoryDevissage.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategoryDevissage.lean#L275).

> *"Let `R` be a ring. Let `(A, d)` be a differential graded `R`-algebra.
> Using P-resolutions we can sometimes reduce statements about general objects of `D(A, d)` to
> statements about `A[k]`. Namely, let `T` be a property of objects of `D(A, d)` and assume that*
>
> 1. *if `Kᵢ`, `i ∈ I` is a family of objects of `D(A, d)` and `T(Kᵢ)` holds for all `i ∈ I`, then
>    `T(⨁ Kᵢ)`,*
> 2. *if `K → L → M → K[1]` is a distinguished triangle of `D(A, d)` and `T` holds for two, then
>    `T` holds for the third object, and*
> 3. *`T(A[k])` holds for all `k ∈ ℤ`.*
>
> *Then `T` holds for all objects of `D(A, d)`."*
>
> The object denoted `A` in the source is the image of the regular module `A` in `D(A, d)`, so
> hypothesis (3) is `T` on each shift of that image. Hypothesis (2) is stated as the conjunction of
> its three implications, one for each position of the triangle. Isomorphism invariance of `T` is
> not assumed.

```lean
theorem property_of_coproducts_of_two_out_of_three_of_shifts
    (A : DifferentialGradedAlgebra R) (T : derivedCategory' A → Prop)
    (hsum : ∀ {ι : Type u} (K : ι → derivedCategory' A), (∀ i, T (K i)) → T (∐ K))
    (htriangle : ∀ Δ : Pretriangulated.Triangle (derivedCategory' A),
      Δ ∈ Pretriangulated.distinguishedTriangles →
      (T Δ.obj₁ → T Δ.obj₂ → T Δ.obj₃) ∧ (T Δ.obj₁ → T Δ.obj₃ → T Δ.obj₂) ∧
      (T Δ.obj₂ → T Δ.obj₃ → T Δ.obj₁))
    (hshift : ∀ k : ℤ, T (((toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj
      (regularModule A))⟦k⟧)) :
    ∀ K : derivedCategory' A, T K
```

**`DifferentialGradedModule.General.property_of_coproducts_of_two_out_of_three_of_shifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategoryDevissage.lean, line 1204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedCategoryDevissage.lean#L1204). The attribute's comment: “algebra carrier universe independent of the base ring; cone-triangle structure”.

> The dévissage with the carrier of the algebra in a universe of its own. *"Let `R` be
> a ring. Let `(A, d)` be a differential graded `R`-algebra. Using P-resolutions we can sometimes
> reduce statements about general objects of `D(A, d)` to statements about `A[k]`. Namely, let `T`
> be a property of objects of `D(A, d)` and assume that*
>
> 1. *if `Kᵢ`, `i ∈ I` is a family of objects of `D(A, d)` and `T(Kᵢ)` holds for all `i ∈ I`, then
>    `T(⨁ Kᵢ)`,*
> 2. *if `K → L → M → K[1]` is a distinguished triangle of `D(A, d)` and `T` holds for two, then
>    `T` holds for the third object, and*
> 3. *`T(A[k])` holds for all `k ∈ ℤ`.*
>
> *Then `T` holds for all objects of `D(A, d)`."*
>
> This is `DifferentialGradedModule.property_of_coproducts_of_two_out_of_three_of_shifts` with the
> universe of the base ring `R` and the universe of the carrier of `A` independent of one another.
>
> The object denoted `A` in the source is the image of the regular module `A` in `D(A, d)`, so
> hypothesis (3) is `T` on each shift of that image. Hypothesis (2) is stated as the conjunction of
> its three implications, one for each position of the triangle. Isomorphism invariance of `T` is
> not assumed.

```lean
theorem property_of_coproducts_of_two_out_of_three_of_shifts
    (A : DifferentialGradedAlgebra.{u, v} R) (T : derivedCategory.{u, v, v} A → Prop)
    (hsum : ∀ {ι : Type v} (K : ι → derivedCategory.{u, v, v} A), (∀ i, T (K i)) → T (∐ K))
    (htriangle : ∀ Δ : Pretriangulated.Triangle (derivedCategory.{u, v, v} A),
      Δ ∈ Pretriangulated.distinguishedTriangles →
      (T Δ.obj₁ → T Δ.obj₂ → T Δ.obj₃) ∧ (T Δ.obj₁ → T Δ.obj₃ → T Δ.obj₂) ∧
      (T Δ.obj₂ → T Δ.obj₃ → T Δ.obj₁))
    (hshift : ∀ k : ℤ, T (((toHomotopyCategory A ⋙ (quasiIsomorphisms A).Q).obj
      (regularModule A))⟦k⟧)) :
    ∀ K : derivedCategory.{u, v, v} A, T K
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.22, Tag 09KV](https://stacks.math.columbia.edu/tag/09KV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
