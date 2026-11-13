---
declaration: section
origin: cited
lean: CategoryTheory.Presheaf.pushforwardSectionsEquiv, CategoryTheory.Presheaf.pushforwardSectionsEquiv_apply, CategoryTheory.Presheaf.pushforwardSectionsEquiv_naturality, AlgebraicGeometry.Stack.abelianPresheafBaseChangeIso, AlgebraicGeometry.Stack.modulePresheafBaseChangeIso, CategoryTheory.TwoFibreProductOver.isIso_presheafRanBaseChange, AlgebraicGeometry.BigFppfOver.isRepresentableMorphism_iff_forall_isRepresentable, AlgebraicGeometry.BigFppfOver.isLeftAdjoint_of_isRepresentableMorphism
statement: formalized
proof: formalized
---

# 96.5 Computing pushforward

Section 96.5 of the Stacks Project, [Tag 06W5](https://stacks.math.columbia.edu/tag/06W5). 4 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06W6, an equation

[Tag 06W6](https://stacks.math.columbia.edu/tag/06W6) in the Stacks Project.

**`CategoryTheory.Presheaf.pushforwardSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/PushforwardSections.lean, line 705](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/PushforwardSections.lean#L705). The attribute's comment: “canonical identification”.

> The pushforward formula for a presheaf along a functor into a category fibred
> in groupoids.
> The projection from the two-fibre product to `𝒳` pulls the presheaf back by
> restriction; its global sections compute the right Kan extension at `y`.

```lean
public noncomputable def pushforwardSectionsEquiv
    (p𝒳 : 𝒳 ⥤ 𝒞) (p𝒴 : 𝒴 ⥤ 𝒞) (f : 𝒳 ⥤ 𝒴)
    (h𝒴 : p𝒴.IsFiberedInGroupoids)
    (hf : f ⋙ p𝒴 = p𝒳) (c : p𝒴.ChoiceOfPullbacks)
    {V : 𝒞} (y : p𝒴.Fiber V) (ℱ : 𝒳ᵒᵖ ⥤ Type w)
    [∀ (G : 𝒳ᵒᵖ ⥤ Type w), f.op.HasPointwiseRightKanExtension G] :
    (f.op.ran.obj ℱ).obj (op y.1) ≃
      Presheaf.globalSections
        ((TwoFibreProductOver.snd (Over.forget V) p𝒳 p𝒴 (c.sliceFunctor y) f).op ⋙ ℱ)
```

**`CategoryTheory.Presheaf.pushforwardSectionsEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/PushforwardSections.lean, line 721](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/PushforwardSections.lean#L721). The attribute's comment: “componentwise characterization by the right Kan counit”.

> At a pair in the two-fibre product, the section corresponding to a pushforward
> section is obtained by restricting along the comparison arrow to `y` and then
> applying the counit of the right Kan extension.

```lean
public theorem pushforwardSectionsEquiv_apply
    (p𝒳 : 𝒳 ⥤ 𝒞) (p𝒴 : 𝒴 ⥤ 𝒞) (f : 𝒳 ⥤ 𝒴)
    (h𝒴 : p𝒴.IsFiberedInGroupoids)
    (hf : f ⋙ p𝒴 = p𝒳) (c : p𝒴.ChoiceOfPullbacks)
    {V : 𝒞} (y : p𝒴.Fiber V) (ℱ : 𝒳ᵒᵖ ⥤ Type w)
    [∀ (G : 𝒳ᵒᵖ ⥤ Type w), f.op.HasPointwiseRightKanExtension G]
    (s : (f.op.ran.obj ℱ).obj (op y.1))
    (P : TwoFibreProductOver (Over.forget V) p𝒳 p𝒴 (c.sliceFunctor y) f) :
    ((Presheaf.globalSectionsEquivSections
        ((TwoFibreProductOver.snd (Over.forget V) p𝒳 p𝒴 (c.sliceFunctor y) f).op ⋙ ℱ))
      (pushforwardSectionsEquiv p𝒳 p𝒴 f h𝒴 hf c y ℱ s)).1 (op P) =
      (f.op.ranCounit.app ℱ).app (op P.y)
        ((f.op.ran.obj ℱ).map (P.iso.inv ≫ c.map P.x.hom y).op s)
```

**`CategoryTheory.Presheaf.pushforwardSectionsEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/PushforwardSections.lean, line 739](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/PushforwardSections.lean#L739). The attribute's comment: “naturality in the presheaf”.

> The pushforward identification commutes with maps of presheaves.

```lean
public theorem pushforwardSectionsEquiv_naturality
    (p𝒳 : 𝒳 ⥤ 𝒞) (p𝒴 : 𝒴 ⥤ 𝒞) (f : 𝒳 ⥤ 𝒴)
    (h𝒴 : p𝒴.IsFiberedInGroupoids)
    (hf : f ⋙ p𝒴 = p𝒳) (c : p𝒴.ChoiceOfPullbacks)
    {V : 𝒞} (y : p𝒴.Fiber V) (ℱ 𝒢 : 𝒳ᵒᵖ ⥤ Type w)
    [∀ (G : 𝒳ᵒᵖ ⥤ Type w), f.op.HasPointwiseRightKanExtension G]
    (η : ℱ ⟶ 𝒢) (s : (f.op.ran.obj ℱ).obj (op y.1)) :
    pushforwardSectionsEquiv p𝒳 p𝒴 f h𝒴 hf c y 𝒢
        (((f.op.ran.map η).app (op y.1)) s) =
      (pushforwardSectionsEquiv p𝒳 p𝒴 f h𝒴 hf c y ℱ s) ≫
        Functor.whiskerLeft
          (TwoFibreProductOver.snd (Over.forget V) p𝒳 p𝒴 (c.sliceFunctor y) f).op η
```

## Tag 075B, a lemma

[Tag 075B](https://stacks.math.columbia.edu/tag/075B) in the Stacks Project.

**`AlgebraicGeometry.Stack.abelianPresheafBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChange.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChange.lean#L256). The attribute's comment: “abelian coefficients”.

> **Stacks 075B at abelian coefficients.** For the canonical 2-cartesian square of categories
> fibred in groupoids over `𝒞`, the base-change transformation `g⁻¹f_* ⟶ f'_*(g')⁻¹` of
> presheaves of abelian groups is an isomorphism, naturally in the presheaf.
>
> Direct image of presheaves is right Kan extension along the opposite functor and inverse image
> is restriction, so the transformation is `CategoryTheory.TwoSquare.ranBaseChange` of the
> opposite square, which is invertible because the square is Guitart exact. The library's
> `CategoryTheory.TwoFibreProductOver.isIso_presheafRanBaseChange` is the same statement at
> coefficients in `Type t`; both are instances of the one coefficient-free input
> `CategoryTheory.TwoFibreProductOver.guitartExact_twoFibreProductSquare`.

```lean
noncomputable def abelianPresheafBaseChangeIso
    (h𝒳 : p𝒳.IsFiberedInGroupoids) (h𝒴' : p𝒴'.IsFiberedInGroupoids)
    (h𝒴 : p𝒴.IsFiberedInGroupoids) (hfc : f ⋙ p𝒴 = p𝒳) (hgc : g ⋙ p𝒴 = p𝒴')
    [∀ G : 𝒳ᵒᵖ ⥤ AddCommGrpCat.{a}, f.op.HasPointwiseRightKanExtension G]
    [∀ G : (TwoFibreProductOver p𝒳 p𝒴' p𝒴 f g)ᵒᵖ ⥤ AddCommGrpCat.{a},
      (TwoFibreProductOver.snd p𝒳 p𝒴' p𝒴 f g).op.HasPointwiseRightKanExtension G] :
    f.op.ran ⋙ (Functor.whiskeringLeft _ _ AddCommGrpCat.{a}).obj g.op ≅
      (Functor.whiskeringLeft _ _ AddCommGrpCat.{a}).obj
          (TwoFibreProductOver.fst p𝒳 p𝒴' p𝒴 f g).op ⋙
        (TwoFibreProductOver.snd p𝒳 p𝒴' p𝒴 f g).op.ran
```

**`AlgebraicGeometry.Stack.modulePresheafBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChange.lean, line 659](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChange.lean#L659). The attribute's comment: “module coefficients, on underlying abelian presheaves”.

> **Stacks 075B at module coefficients.** For the canonical 2-cartesian square of categories
> fibred in groupoids over the big fppf category of `S` and any topology `τ` on `B.Schemes`, the
> two composites `f_* ⋙ g⁻¹` and `(g')⁻¹ ⋙ f'_*` of inverse- and direct-image functors of sheaves
> of modules are isomorphic on underlying abelian presheaves, naturally in the sheaf of modules.
>
> Inverse image of sheaves of modules is objectwise restriction and direct image is the right Kan
> extension along the opposite 1-morphism, both on underlying abelian presheaves
> (`AlgebraicGeometry.Stack.modulePullbackCompToPresheafIso` and
> `AlgebraicGeometry.Stack.moduleSheafPushforwardCompToPresheafIso`), so both composites become
> the two ways round the square of a right Kan extension and a restriction, where they are
> identified by `AlgebraicGeometry.Stack.abelianPresheafBaseChangeIso`. Nothing here is special to
> modules: the Guitart exactness that identification rests on is coefficient-free.

```lean
noncomputable def modulePresheafBaseChangeIso
    (h𝒳 : p𝒳.IsFiberedInGroupoids) (h𝒴' : p𝒴'.IsFiberedInGroupoids)
    (h𝒴 : p𝒴.IsFiberedInGroupoids) (hfc : f ⋙ p𝒴 = p𝒳) (hgc : g ⋙ p𝒴 = p𝒴')
    [∀ G : 𝒳ᵒᵖ ⥤ AddCommGrpCat.{max (u + 1) v₁ w₁ v₂ w₂ v₃ w₃ a},
      f.op.HasPointwiseRightKanExtension G]
    [∀ G : (TwoFibreProductOver p𝒳 p𝒴' p𝒴 f g)ᵒᵖ ⥤ AddCommGrpCat.{max (u + 1) v₁ w₁ v₂ w₂ v₃ w₃ a},
      (TwoFibreProductOver.snd p𝒳 p𝒴' p𝒴 f g).op.HasPointwiseRightKanExtension G] :
    ((moduleSheafPushforward.{u, v₁, w₁, max (u + 1) v₂ w₂ a, v₃, w₃}
          B S hS p𝒳 p𝒴 h𝒳 h𝒴 f hfc τ hτ) ⋙
        (modulePullback.{u, v₂, w₂, max (u + 1) v₁ w₁ v₂ w₂ v₃ w₃ a, v₃, w₃}
          B S hS p𝒴' p𝒴 h𝒴' h𝒴 g hgc τ hτ)) ⋙
      (SheafOfModules.forget (ringStructureSheafCore B S hS p𝒴' h𝒴' τ hτ) ⋙
        PresheafOfModules.toPresheaf (ringStructureSheafCore B S hS p𝒴' h𝒴' τ hτ).obj) ≅
      ((modulePullback.{u, max (u + 1) v₁ v₂ w₃, max u w₁ w₂,
              max (u + 1) v₁ w₁ v₂ w₂ v₃ w₃ a, v₁, w₁}
          B S hS (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g) p𝒳
          (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒴' p𝒴 f g h𝒳 h𝒴' h𝒴 hfc hgc)
            h𝒳 (TwoFibreProductOver.fst p𝒳 p𝒴' p𝒴 f g)
            TwoFibreProductOver.fst_comp_eq τ hτ) ⋙
        (moduleSheafPushforward.{u, max (u + 1) v₁ v₂ w₃, max u w₁ w₂,
              max v₃ a, v₂, w₂}
          B S hS (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g) p𝒴'
          (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒴' p𝒴 f g h𝒳 h𝒴' h𝒴 hfc hgc)
            h𝒴' (TwoFibreProductOver.snd p𝒳 p𝒴' p𝒴 f g)
            TwoFibreProductOver.snd_comp_eq τ hτ)) ⋙
      (SheafOfModules.forget (ringStructureSheafCore B S hS p𝒴' h𝒴' τ hτ) ⋙
        PresheafOfModules.toPresheaf (ringStructureSheafCore B S hS p𝒴' h𝒴' τ hτ).obj)
```

**`CategoryTheory.TwoFibreProductOver.isIso_presheafRanBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/PresheafBaseChange.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInGroupoids/PresheafBaseChange.lean#L183).

> **Stacks 075B**: in a 2-cartesian square of categories fibred in groupoids, the canonical
> base-change transformation `g⁻¹ f_* ⟶ f'_* (g')⁻¹` for presheaves is an isomorphism, naturally in
> the presheaf.

```lean
theorem isIso_presheafRanBaseChange
    (pX : X ⥤ C) (pY' : Y' ⥤ C) (pY : Y ⥤ C)
    (f : X ⥤ Y) (g : Y' ⥤ Y)
    (hX : pX.IsFiberedInGroupoids) (hY' : pY'.IsFiberedInGroupoids)
    (hY : pY.IsFiberedInGroupoids)
    (hf : f ⋙ pY = pX) (hg : g ⋙ pY = pY')
    [∀ (F : Xᵒᵖ ⥤ Type t), f.op.HasPointwiseRightKanExtension F]
    [∀ (F : (TwoFibreProductOver pX pY' pY f g)ᵒᵖ ⥤ Type t),
      (TwoFibreProductOver.snd pX pY' pY f g).op.HasPointwiseRightKanExtension F] :
    IsIso ((TwoSquare.mk
      (TwoFibreProductOver.fst pX pY' pY f g)
      (TwoFibreProductOver.snd pX pY' pY f g) f g
      (TwoFibreProductOver.psiIso pX pY' pY f g).hom).op.ranBaseChange
        (D := Type t))
```

## Tag 06W7, a lemma

[Tag 06W7](https://stacks.math.columbia.edu/tag/06W7) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.isRepresentableMorphism_iff_forall_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Representable.lean, line 344](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Representable.lean#L344).

> **Stacks 06W7.** A morphism of categories fibred in groupoids over the big fppf category of
> `S` is representable if and only if every presheaf `x ↦ Hom(F x, y)` on the source category is
> representable.

```lean
theorem isRepresentableMorphism_iff_forall_isRepresentable
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : Type v} [Category.{u + 1} 𝒳] [Category.{u + 1} 𝒴]
    (p𝒳 : 𝒳 ⥤ BigFppfOver B S hS)
    (p𝒴 : 𝒴 ⥤ BigFppfOver B S hS)
    (F : 𝒳 ⥤ 𝒴) (hF : F ⋙ p𝒴 = p𝒳)
    (h𝒳 : p𝒳.IsFiberedInGroupoids) (h𝒴 : p𝒴.IsFiberedInGroupoids) :
    Stacks.RepresentableMorphism.IsRepresentableMorphism p𝒳 p𝒴 F ↔
      ∀ y : 𝒴, (F.op ⋙ yoneda.obj y).IsRepresentable
```

## Tag 06W8, a lemma

[Tag 06W8](https://stacks.math.columbia.edu/tag/06W8) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.isLeftAdjoint_of_isRepresentableMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentablePushforward.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentablePushforward.lean#L74). The attribute's comment: “existence of the right adjoint”.

> A representable 1-morphism of categories fibred in groupoids over the big fppf category of
> `S` has a right adjoint: its value at `y` is a representing object for the presheaf
> `x ↦ Hom(F x, y)`, which exists by Stacks 06W7.

```lean
theorem isLeftAdjoint_of_isRepresentableMorphism (hF : F ⋙ p𝒴 = p𝒳)
    (h𝒳 : p𝒳.IsFiberedInGroupoids) (h𝒴 : p𝒴.IsFiberedInGroupoids)
    (hrep : Stacks.RepresentableMorphism.IsRepresentableMorphism p𝒳 p𝒴 F) :
    F.IsLeftAdjoint
```

**`AlgebraicGeometry.BigFppfOver.isContinuous_rightAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentablePushforward.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentablePushforward.lean#L93). The attribute's comment: “continuity of the right adjoint”.

> The right adjoint of a representable 1-morphism is continuous for the topologies associated
> (Stacks 06TP) to a topology `τ` on the underlying category of schemes: `F` is cocontinuous by
> Stacks 06NW, and a right adjoint of a cocontinuous functor is continuous.

```lean
theorem isContinuous_rightAdjoint (τ : GrothendieckTopology B.Schemes) :
    letI : F.IsLeftAdjoint :=
      isLeftAdjoint_of_isRepresentableMorphism B S hS p𝒳 p𝒴 F hF h𝒳 h𝒴 hrep
    F.rightAdjoint.IsContinuous (Stack.associatedTopology B S hS p𝒴 τ)
      (Stack.associatedTopology B S hS p𝒳 τ)
```

**`AlgebraicGeometry.BigFppfOver.isMorphismOfSites_rightAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentablePushforward.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentablePushforward.lean#L112). The attribute's comment: “the morphism of sites”.

> The right adjoint of a representable 1-morphism defines a morphism of sites from the
> associated site of `𝒳` to that of `𝒴`: it is continuous, and the left exact left adjoint of its
> pushforward on sheaves is the pushforward along `F`.

```lean
theorem isMorphismOfSites_rightAdjoint (τ : GrothendieckTopology B.Schemes) :
    letI : F.IsLeftAdjoint :=
      isLeftAdjoint_of_isRepresentableMorphism B S hS p𝒳 p𝒴 F hF h𝒳 h𝒴 hrep
    IsMorphismOfSites.{u + 1} F.rightAdjoint (Stack.associatedTopology B S hS p𝒴 τ)
      (Stack.associatedTopology B S hS p𝒳 τ)
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.ranIsoRestrictionOfAdjunction`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L215), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentablePushforward.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentablePushforward.lean#L139) (StacksFrontier): “the presheaf direct image along the right adjoint is restriction”.
- [`CategoryTheory.Adjunction.sheafPushforwardCocontinuousIso`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/PushforwardAdjunction.lean#L70), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentablePushforward.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentablePushforward.lean#L142) (StacksFrontier): “agreement of the two direct images”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.5, Tag 06W5](https://stacks.math.columbia.edu/tag/06W5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
