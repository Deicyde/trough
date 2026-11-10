---
declaration: section
origin: cited
lean: AlgebraicGeometry.EquivariantModule, AlgebraicGeometry.equivariantGroupoidMorphism, AlgebraicGeometry.equivariantPullback, AlgebraicGeometry.gradedGmAction, AlgebraicGeometry.GmEquivariant.gradedDescentMorphism_homogeneous, AlgebraicGeometry.GmEquivariant.gradedModuleEquivariantSheaf, AlgebraicGeometry.GmEquivariant.gradedModuleEquivariantSheaf_module, AlgebraicGeometry.GmEquivariant.gradedModuleEquivariantSheaf_alpha
statement: formalized
proof: formalized
---

# 39.12 Equivariant quasi-coherent sheaves

Section 39.12 of the Stacks Project, [Tag 03LE](https://stacks.math.columbia.edu/tag/03LE). 5 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03LF, a definition

[Tag 03LF](https://stacks.math.columbia.edu/tag/03LF) in the Stacks Project.

**`AlgebraicGeometry.EquivariantModule`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantModule.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantModule.lean#L183). References: SGA 3 I (6.5.1), “equivariant module”; SGA 3 I (6.5).

> A quasi-coherent module on `X` equivariant for a given action of `G`, written directly in
> terms of the action map and the projection.

```lean
structure EquivariantModule
```

## Tag 03LG, a lemma

[Tag 03LG](https://stacks.math.columbia.edu/tag/03LG) in the Stacks Project.

**`AlgebraicGeometry.equivariantGroupoidMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/ActionGroupoidPullback.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/ActionGroupoidPullback.lean#L217). The attribute's comment: “action-groupoid morphism”.

> **Stacks Project, Tag 03LG.** An equivariant morphism induces the specified morphism of
> action groupoids.

```lean
noncomputable def equivariantGroupoidMorphism (f : Y ⟶ X) [IsModHom G f] :
    EquivariantGroupoidMorphism B G X Y f
```

**`AlgebraicGeometry.equivariantPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/ActionGroupoidPullback.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/ActionGroupoidPullback.lean#L306). The attribute's comment: “the functor”. References: SGA 3 I (6.5.2); SGA 3 I (6.3.1).

> **Stacks Project, Tag 03LG.** Pullback of equivariant quasi-coherent modules along an
> equivariant morphism `f`. Its action on modules, on equivariant structures and on morphisms is
> that of the pullback functor along the induced morphism of action groupoids.

```lean
noncomputable def equivariantPullback (f : Y ⟶ X) [IsModHom G f] :
    Stacks.Groupoids.GroupoidScheme.QuasicoherentModule (actionGroupoid B G X) ⥤
      Stacks.Groupoids.GroupoidScheme.QuasicoherentModule (actionGroupoid B G Y)
```

## Tag 0EKJ, an example

[Tag 0EKJ](https://stacks.math.columbia.edu/tag/0EKJ) in the Stacks Project.

**`AlgebraicGeometry.gradedGmAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedAction.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedAction.lean#L189). The attribute's comment: “graded_ring_gm_action”. References: EGA II (8.3.9), “partial”.

> **Stacks Project, Tag 0EKJ.** An integer grading defines the multiplicative-group action
> on the spectrum whose coordinate map sends a homogeneous element of degree `n` to `a ⊗ Tⁿ`.

```lean
noncomputable def gradedGmAction {A : Type u} [CommRing A] {σ : Type v}
    [SetLike σ A] [AddSubmonoidClass σ A] (𝒜 : ℤ → σ) [GradedRing 𝒜] :
    GradedGmAction 𝒜
```

**`AlgebraicGeometry.GmEquivariant.gradedDescentMorphism_homogeneous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleEquivariantSheaf.lean, line 562](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleEquivariantSheaf.lean#L562). The attribute's comment: “the descent morphism on homogeneous sections”.

> On the canonical pullback of a homogeneous section of degree `n` along the action, the
> descent morphism is multiplication by the character `xⁿ`.

```lean
theorem gradedDescentMorphism_homogeneous {n : ℤ} (m : ℳ n) :
    (gradedDescentMorphism 𝒜 ℳ).app ⊤
        (pullbackSection (gradedGmAction 𝒜).action.smul.left (tilde (moduleOf A M))
          (tilde.toOpen (moduleOf A M) ⊤ (m : M))) =
      laurentCoordinate A n • pullbackSection (snd gm.{u} (specAOver A)).left
        (tilde (moduleOf A M)) (tilde.toOpen (moduleOf A M) ⊤ (m : M))
```

**`AlgebraicGeometry.GmEquivariant.gradedModuleEquivariantSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleEquivariantSheaf.lean, line 619](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleEquivariantSheaf.lean#L619). The attribute's comment: “graded_module_equivariant_sheaf”.

> Let `A` be a `ℤ`-graded ring and let `X = Spec A` carry the `𝐆ₘ`-action attached to the
> grading. A graded `A`-module `M` makes the associated quasi-coherent module `M~` a
> `𝐆ₘ`-equivariant quasi-coherent `𝒪_X`-module, whose descent morphism carries the canonical
> pullback of a homogeneous section of degree `n` to `xⁿ` times that section.

```lean
noncomputable def gradedModuleEquivariantSheaf : GradedEquivariantModule.{u} 𝒜
```

**`AlgebraicGeometry.GmEquivariant.gradedModuleEquivariantSheaf_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleEquivariantSheaf.lean, line 629](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleEquivariantSheaf.lean#L629). The attribute's comment: “underlying module”.

> The underlying quasi-coherent module of the equivariant module attached to a graded module
> is `M~`.

```lean
theorem gradedModuleEquivariantSheaf_module :
    underlyingModule 𝒜 (gradedModuleEquivariantSheaf 𝒜 ℳ) = tilde (moduleOf A M)
```

**`AlgebraicGeometry.GmEquivariant.gradedModuleEquivariantSheaf_alpha`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleEquivariantSheaf.lean, line 636](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleEquivariantSheaf.lean#L636). The attribute's comment: “descent morphism”.

> The descent morphism of the equivariant module attached to a graded module is
> `gradedDescentMorphism`.

```lean
theorem gradedModuleEquivariantSheaf_alpha :
    descentMorphism 𝒜 (gradedModuleEquivariantSheaf 𝒜 ℳ) = gradedDescentMorphism 𝒜 ℳ
```

## Tag 0EKK, a lemma

[Tag 0EKK](https://stacks.math.columbia.edu/tag/0EKK) in the Stacks Project.

**`AlgebraicGeometry.gradingOfGmAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedActionOfGmAction.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedActionOfGmAction.lean#L389). References: EGA II (8.3.9), “special case”.

> **Stacks Project, Tag 0EKK.** An action of the multiplicative group scheme on
> an affine scheme determines an integer grading of its coordinate ring, and is
> the action associated to that grading.

```lean
noncomputable def gradingOfGmAction (X : Scheme.{u}) [IsAffine X]
    [X.Over (Spec (.of (ULift.{u} ℤ)))]
    (action : ModObj
      (multiplicativeGroupULift.asOver (Spec (.of (ULift.{u} ℤ))))
      (X.asOver (Spec (.of (ULift.{u} ℤ))))) :
    Σ (𝒜 : ℤ → AddSubgroup Γ(X, ⊤)),
      {graded : GradedRing 𝒜 //
        (letI := action
         letI : X.isoSpec.hom.IsOver (Spec (.of (ULift.{u} ℤ))) :=
           ⟨specULiftZIsTerminal.hom_ext _ _⟩
         letI : IsMonHom
             (Iso.refl (multiplicativeGroupULift.asOver (Spec (.of (ULift.{u} ℤ))))).hom :=
           ⟨by exact Category.comp_id _, by simp⟩
         ModObj.ofIso (Iso.refl (multiplicativeGroupULift.asOver (Spec (.of (ULift.{u} ℤ)))))
           (X.isoSpec.asOver (Spec (.of (ULift.{u} ℤ))))) =
          (letI := graded; (gradedGmAction 𝒜).action)}
```

## Tag 0EKL, a lemma

[Tag 0EKL](https://stacks.math.columbia.edu/tag/0EKL) in the Stacks Project.

**`AlgebraicGeometry.GmEquivariant.homogeneousPartDecomposition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleEquivariantComparison.lean, line 800](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleEquivariantComparison.lean#L800). The attribute's comment: “the canonical grading of the global sections”.

> **Stacks Project, Tag 0EKL.** The canonical grading of the global sections of a
> `𝐆ₘ`-equivariant quasi-coherent module on `Spec A`: the canonical homogeneous pieces decompose
> the global sections as an internal direct sum.

```lean
noncomputable def homogeneousPartDecomposition (F : GradedEquivariantModule.{u} 𝒜) :
    DirectSum.Decomposition (homogeneousPart 𝒜 F)
```

**`AlgebraicGeometry.GmEquivariant.tildeHomogeneousIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleEquivariantIsomorphism.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleEquivariantIsomorphism.lean#L199). The attribute's comment: “the comparison is an isomorphism of equivariant modules”.

> **Stacks Project, Tag 0EKL.** For a `𝐆ₘ`-equivariant quasi-coherent module `F` on
> `X = Spec A` and `M = Γ(X, F)` with its canonical grading, the canonical comparison `M~ ⟶ F` is
> an isomorphism of `𝐆ₘ`-equivariant modules, the equivariant structure on `M~` being the one
> attached to the grading of `M`.

```lean
noncomputable def tildeHomogeneousIso :
    gradedModuleEquivariantSheaf 𝒜 (homogeneousPart 𝒜 F) ≅ F
```

**`AlgebraicGeometry.GmEquivariant.tildeHomogeneousIso_hom_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleEquivariantIsomorphism.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleEquivariantIsomorphism.lean#L212). The attribute's comment: “the equivariant isomorphism is the canonical comparison”.

> **Stacks Project, Tag 0EKL.** The isomorphism of `𝐆ₘ`-equivariant modules above is the
> canonical comparison of a quasi-coherent module on an affine scheme with the module associated to
> its global sections.

```lean
theorem tildeHomogeneousIso_hom_hom :
    @EquivariantModule.Hom.hom _ base.{u} gm.{u} (specAOver A)
        AlgebraicGeometry.instGrpObjSpecAsOverSpec (gradedGmAction 𝒜).action
        (gradedModuleEquivariantSheaf 𝒜 (homogeneousPart 𝒜 F)) F
        (@CategoryTheory.Iso.hom _ _ _ _ (tildeHomogeneousIso 𝒜 F)) =
      Scheme.Modules.fromTildeΓNatTrans.app (underlyingModule 𝒜 F)
```

**`AlgebraicGeometry.GmEquivariant.homogeneousPart`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleOfEquivariantModule.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleOfEquivariantModule.lean#L270). The attribute's comment: “the canonical homogeneous pieces of the global sections”.

> The canonical degree-`n` piece of the global sections of a `𝐆ₘ`-equivariant quasi-coherent
> module on `Spec A`: the sections on which the descent morphism of the equivariant structure
> multiplies the canonical pullback section by the character `x ↦ xⁿ` of `𝐆ₘ`.

```lean
noncomputable def homogeneousPart (F : GradedEquivariantModule.{u} 𝒜) (n : ℤ) :
    AddSubgroup ((moduleSpecΓFunctor (R := .of A)).obj (underlyingModule 𝒜 F))
```

**`AlgebraicGeometry.GmEquivariant.gradedSMul_homogeneousPart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleOfEquivariantModule.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GradedModuleOfEquivariantModule.lean#L382). The attribute's comment: “compatibility of the canonical homogeneous pieces with the grading of A”.

> The canonical homogeneous pieces of the global sections of a `𝐆ₘ`-equivariant quasi-coherent
> module on `Spec A` are compatible with the grading of `A`: a homogeneous function of degree `i`
> carries the degree-`n` piece into the degree-`i + n` piece.

```lean
theorem gradedSMul_homogeneousPart (F : GradedEquivariantModule.{u} 𝒜) :
    SetLike.GradedSMul 𝒜 (homogeneousPart 𝒜 F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.12, Tag 03LE](https://stacks.math.columbia.edu/tag/03LE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
