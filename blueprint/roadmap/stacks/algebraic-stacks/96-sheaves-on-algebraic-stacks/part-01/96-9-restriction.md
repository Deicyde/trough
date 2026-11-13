---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isEquivalence_overPost, AlgebraicGeometry.Stack.inducedTopology_overPost, CategoryTheory.Over.post, AlgebraicGeometry.Stack.presheafPullback, AlgebraicGeometry.Stack.restrictToSmallEtale, AlgebraicGeometry.Stack.smallEtaleBaseMorphism, AlgebraicGeometry.Stack.restrictionPushforwardComparison, AlgebraicGeometry.Stack.restrictionPushforwardComparison_app
statement: formalized
proof: formalized
---

# 96.9 Restriction

Section 96.9 of the Stacks Project, [Tag 075C](https://stacks.math.columbia.edu/tag/075C). 8 tags here are carried by 30 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06W0, a lemma

[Tag 06W0](https://stacks.math.columbia.edu/tag/06W0) in the Stacks Project.

**`AlgebraicGeometry.Stack.isEquivalence_overPost`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSiteLocalization.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSiteLocalization.lean#L101). The attribute's comment: “equivalence of categories”.

> **Stacks 06W0.** The canonical localization functor from the slice of a category fibred in
> groupoids at an object `x` to the schemes over the scheme `x` lies over is an equivalence of
> categories.

```lean
theorem isEquivalence_overPost {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids) (x : 𝒳) :
    (Over.post (X := x) (p ⋙ Over.forget (B.obj hS))).IsEquivalence
```

**`AlgebraicGeometry.Stack.inducedTopology_overPost`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSiteLocalization.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSiteLocalization.lean#L110). The attribute's comment: “equivalence of site topologies”.

> **Stacks 06W0.** The canonical localization functor identifies the localization at `x` of
> the associated topology with the localization of the base topology at the scheme `x` lies
> over, so it is an equivalence of sites and not merely of categories.

```lean
theorem inducedTopology_overPost {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids)
    (τ : GrothendieckTopology B.Schemes) (x : 𝒳) :
    (Over.post (X := x) (p ⋙ Over.forget (B.obj hS))).inducedTopology
        (τ.over (p.obj x).left) =
      (associatedTopology B S hS p τ).over x
```

Declarations registered for the tag:

- [`CategoryTheory.Over.post`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.post#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSiteLocalization.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSiteLocalization.lean#L87) (StacksFrontier): “the canonical localization functor”.

## Tag 06W1, a definition

[Tag 06W1](https://stacks.math.columbia.edu/tag/06W1) in the Stacks Project.

**`AlgebraicGeometry.Stack.presheafPullback`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalizationPullback.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocalizationPullback.lean#L81). The attribute's comment: “part (1)”.

> The pullback of a presheaf on a category fibred in groupoids to
> the big fppf site of the scheme underlying an object `x`: restrict to the slice at `x`, then
> transport across the localization equivalence of Stacks 06W0.

```lean
noncomputable abbrev presheafPullback
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids) (x : 𝒳)
    {A : Type t} [Category.{s} A] (F : 𝒳ᵒᵖ ⥤ A) :
    (Over (p.obj x).left)ᵒᵖ ⥤ A
```

**`AlgebraicGeometry.Stack.restrictToSmallEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalizationPullback.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocalizationPullback.lean#L93). The attribute's comment: “part (2)”.

> The restriction of the pulled-back presheaf to the small étale
> site of the same scheme, for an étale site with the same size cutoff.

```lean
noncomputable abbrev restrictToSmallEtale
    (B : BigFppfSite.{u}) (E : BigEtaleSite.{u}) (h : E.cutoff = B.cutoff)
    (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids) (x : 𝒳)
    {A : Type t} [Category.{s} A] (F : 𝒳ᵒᵖ ⥤ A) :
    (SmallEtale E (p.obj x).left.1
      (show E.Contains (p.obj x).left.1 from by simpa [h] using (p.obj x).left.2))ᵒᵖ ⥤ A
```

## Tag 06W2, an equation

[Tag 06W2](https://stacks.math.columbia.edu/tag/06W2) in the Stacks Project.

**`AlgebraicGeometry.Stack.smallEtaleBaseMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestriction.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestriction.lean#L124). The attribute's comment: “the morphism of schemes below an arrow”.

> **Stacks 06W2.** The morphism of the big étale category of schemes below an arrow of a
> category fibred in groupoids: the fppf and étale cutoffs agree, so the scheme morphism
> underlying the arrow is a morphism of the étale site's bounded category.

```lean
def smallEtaleBaseMorphism {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) {x y : 𝒳} (φ : x ⟶ y) :
    E.obj (p.obj x).left.1 (contains_base B E h S hS p x) ⟶
      E.obj (p.obj y).left.1 (contains_base B E h S hS p y)
```

**`AlgebraicGeometry.Stack.restrictionPushforwardComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestriction.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestriction.lean#L137). The attribute's comment: “the comparison with the direct image”.

> **Stacks 06W2.** The comparison `c_φ : F|_{V_ét} ⟶ a_{small, *}(F|_{U_ét})` from the
> restriction of a presheaf at the target of an arrow `φ : x ⟶ y` to the direct image, along the
> underlying morphism of schemes, of its restriction at the source.
>
> The direct image on small étale sites is precomposition with base change, so the target is
> spelled as such.

```lean
noncomputable def restrictionPushforwardComparison {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids) {x y : 𝒳} (φ : x ⟶ y)
    {A : Type t} [Category.{s} A] (F : 𝒳ᵒᵖ ⥤ A) :
    restrictToSmallEtale B E h S hS p hp y F ⟶
      (smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p φ)).op ⋙
        restrictToSmallEtale B E h S hS p hp x F
```

**`AlgebraicGeometry.Stack.restrictionPushforwardComparison_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestriction.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestriction.lean#L240). The attribute's comment: “the component formula”.

> **Stacks 06W2.** On a small étale object `W` over `V`, the comparison with the direct image
> is restriction of `F` along the arrow of `𝒳` between the cartesian lifts of `W` and of its base
> change, characterized by lying over the projection of the base-change square.
>
> This specifies the comparison map, rather than merely producing one.

```lean
theorem restrictionPushforwardComparison_app {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids) {x y : 𝒳} (φ : x ⟶ y)
    {A : Type t} [Category.{s} A] (F : 𝒳ᵒᵖ ⥤ A)
    (W : SmallEtale E (p.obj y).left.1 (contains_base B E h S hS p y)) :
    letI : (Over.post (X := x) (p ⋙ Over.forget (B.obj hS))).IsEquivalence :=
      isEquivalence_overPost B S hS p hp x
    letI : (Over.post (X := y) (p ⋙ Over.forget (B.obj hS))).IsEquivalence :=
      isEquivalence_overPost B S hS p hp y
    let f := smallEtaleBaseMorphism B E h S hS p φ
    let V' := (smallEtaleInclusion B E h (p.obj y).left.1 (contains_base B E h S hS p y)).obj W
    let U' := (smallEtaleInclusion B E h (p.obj x).left.1
      (contains_base B E h S hS p x)).obj ((smallEtaleBaseChange E f).obj W)
    let y' := (Over.post (X := y) (p ⋙ Over.forget (B.obj hS))).inv.obj V'
    let x' := (Over.post (X := x) (p ⋙ Over.forget (B.obj hS))).inv.obj U'
    let εy := (Over.post (X := y) (p ⋙ Over.forget (B.obj hS))).asEquivalence.counit.app V'
    let εx := (Over.post (X := x) (p ⋙ Over.forget (B.obj hS))).asEquivalence.counit.app U'
    ∀ φ' : x'.left ⟶ y'.left, φ' ≫ y'.hom = x'.hom ≫ φ →
      B.inclusion.map (p.map φ').left ≫ B.inclusion.map εy.left =
        B.inclusion.map εx.left ≫ E.inclusion.map (pullback.fst W.obj.hom f) →
      (restrictionPushforwardComparison B E h S hS p hp φ F).app (Opposite.op W) =
        F.map φ'.op
```

**`AlgebraicGeometry.Stack.restrictionPushforwardComparison_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestriction.lean, line 500](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestriction.lean#L500). The attribute's comment: “functoriality in the presheaf”.

> **Stacks 06W2.** The comparison with the direct image is natural in the presheaf.

```lean
theorem restrictionPushforwardComparison_naturality {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids) {x y : 𝒳} (φ : x ⟶ y)
    {A : Type t} [Category.{s} A] {F G : 𝒳ᵒᵖ ⥤ A} (η : F ⟶ G)
    (W : SmallEtale E (p.obj y).left.1 (contains_base B E h S hS p y)) :
    letI : (Over.post (X := x) (p ⋙ Over.forget (B.obj hS))).IsEquivalence :=
      isEquivalence_overPost B S hS p hp x
    letI : (Over.post (X := y) (p ⋙ Over.forget (B.obj hS))).IsEquivalence :=
      isEquivalence_overPost B S hS p hp y
    let y' := (Over.post (X := y) (p ⋙ Over.forget (B.obj hS))).inv.obj
      ((smallEtaleInclusion B E h (p.obj y).left.1 (contains_base B E h S hS p y)).obj W)
    let x' := (Over.post (X := x) (p ⋙ Over.forget (B.obj hS))).inv.obj
      ((smallEtaleInclusion B E h (p.obj x).left.1 (contains_base B E h S hS p x)).obj
        ((smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p φ)).obj W))
    (restrictionPushforwardComparison B E h S hS p hp φ F).app (Opposite.op W) ≫
        η.app (Opposite.op x'.left) =
      η.app (Opposite.op y'.left) ≫
        (restrictionPushforwardComparison B E h S hS p hp φ G).app (Opposite.op W)
```

## Tag 06W3, an equation

[Tag 06W3](https://stacks.math.columbia.edu/tag/06W3) in the Stacks Project.

**`AlgebraicGeometry.Stack.restrictToSmallEtale_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestriction.lean, line 639](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestriction.lean#L639). The attribute's comment: “the restriction is a sheaf”.

> **Stacks 06W3.** The restriction of an étale sheaf on a category fibred in groupoids to the
> small étale site of the scheme an object lies over is a sheaf, not merely a presheaf whose
> sheafification is of interest.

```lean
theorem restrictToSmallEtale_isSheaf {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids) (x : 𝒳)
    (F : Sheaf (associatedTopology B S hS p (etaleTopology B)) (Type (max (u + 1) t))) :
    Presheaf.IsSheaf
      (SmallEtale.topology E (p.obj x).left.1 (contains_base B E h S hS p x))
      (restrictToSmallEtale B E h S hS p hp x F.obj)
```

**`AlgebraicGeometry.Stack.restrictionInverseImageComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestriction.lean, line 724](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestriction.lean#L724). The attribute's comment: “the comparison with the inverse image”.

> **Stacks 06W3.** The comparison `c_φ : a_{small}^{-1}(F|_{V_ét}) ⟶ F|_{U_ét}` from the
> inverse image of the restriction at the target of an arrow `φ : x ⟶ y` to the restriction at
> its source, the mate of the direct-image comparison of Stacks 06W2 under the
> pullback–pushforward adjunction on small étale sheaves.

```lean
noncomputable def restrictionInverseImageComparison {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids) {x y : 𝒳} (φ : x ⟶ y)
    (F : Sheaf (associatedTopology B S hS p (etaleTopology B)) (Type (max (u + 1) t))) :
    ((smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p φ)).sheafPullback
        (Type (max (u + 1) t))
        (SmallEtale.topology E (p.obj y).left.1 (contains_base B E h S hS p y))
        (SmallEtale.topology E (p.obj x).left.1 (contains_base B E h S hS p x))).obj
      (restrictToSmallEtaleSheaf B E h S hS p hp y F) ⟶
    restrictToSmallEtaleSheaf B E h S hS p hp x F
```

## Tag 075D, a lemma

[Tag 075D](https://stacks.math.columbia.edu/tag/075D) in the Stacks Project.

**`AlgebraicGeometry.Stack.smallEtaleStructureComparison_app_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SmallEtaleModuleComparisonComposition.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SmallEtaleModuleComparisonComposition.lean#L56). The attribute's comment: “part (1), for the maps of structure sheaves below an arrow”.

> The map `a_{small}^♯` of structure sheaves below `φ`, applied after the map `b_{small}^♯`
> below `ψ`, is the map below `ψ ∘ φ` followed by restriction along the identification of the two
> base changes.

```lean
theorem smallEtaleStructureComparison_app_comp
    (W : (SmallEtale E (p.obj z).left.1 (contains_base B E h S hS p z))ᵒᵖ)
    (r : (SmallEtale.structureSheaf E (p.obj z).left.1
      (contains_base B E h S hS p z)).obj.obj W) :
    (smallEtaleStructureComparison B E h S hS p hp φ τ hτ).app
        ((smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p ψ)).op.obj W)
        ((smallEtaleStructureComparison B E h S hS p hp ψ τ hτ).app W r) =
      (SmallEtale.structureSheaf E (p.obj x).left.1
          (contains_base B E h S hS p x)).obj.map
        ((smallEtaleBaseChangeCompIso B E h S hS p φ ψ).hom.app W.unop).op
        ((smallEtaleStructureComparison B E h S hS p hp (φ ≫ ψ) τ hτ).app W r)
```

**`AlgebraicGeometry.Stack.restrictModulePushforwardComparison_app_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SmallEtaleModuleComparisonComposition.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SmallEtaleModuleComparisonComposition.lean#L89). The attribute's comment: “part (1), for the direct-image comparison of a presheaf of modules”.

> The direct-image comparison of a presheaf of modules below `φ`, applied after the
> comparison below `ψ`, is the comparison below `ψ ∘ φ` followed by restriction along the
> identification of the two base changes.

```lean
theorem restrictModulePushforwardComparison_app_comp
    (F : PresheafOfModules.{m} (ringStructureSheafCore B S hS p hp τ hτ).obj)
    (W : (SmallEtale E (p.obj z).left.1 (contains_base B E h S hS p z))ᵒᵖ)
    (n : (restrictModuleToSmallEtale B E h S hS p hp z τ hτ F).obj W) :
    (restrictModulePushforwardComparison B E h S hS p hp φ τ hτ F).app
        ((smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p ψ)).op.obj W)
        ((restrictModulePushforwardComparison B E h S hS p hp ψ τ hτ F).app W n) =
      (restrictModuleToSmallEtale B E h S hS p hp x τ hτ F).presheaf.map
        ((smallEtaleBaseChangeCompIso B E h S hS p φ ψ).hom.app W.unop).op
        ((restrictModulePushforwardComparison B E h S hS p hp (φ ≫ ψ) τ hτ F).app W n)
```

**`AlgebraicGeometry.Stack.restrictModulePullbackComparison_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SmallEtalePullbackComparisonComposition.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SmallEtalePullbackComparisonComposition.lean#L90). The attribute's comment: “part (1), for the pullback comparison map of a presheaf of modules”.

> **The comparison map `c_φ` of Stacks 06WC is functorial in the arrow.** For arrows `φ : x ⟶ y`
> and `ψ : y ⟶ z` of `𝒳` lying over morphisms of schemes `a : U ⟶ V` and `b : V ⟶ W`, the pullback
> along `a_{small}^♯` of the comparison map below `ψ`, followed by the comparison map below `φ`, is
> the composition law `AlgebraicGeometry.Stack.smallEtalePullbackComparisonCompIso` for the pullbacks
> followed by the comparison map below `ψ ∘ φ`.

```lean
public theorem restrictModulePullbackComparison_comp :
    (PresheafOfModules.pullback.{u}
          (smallEtaleStructureComparison B E h S hS p hp φ τ hτ)).map
        (restrictModulePullbackComparison B E h S hS p hp ψ τ hτ F) ≫
      restrictModulePullbackComparison B E h S hS p hp φ τ hτ F =
    (smallEtalePullbackComparisonCompIso B E h S hS p hp τ hτ φ ψ).hom.app
        (restrictModuleToSmallEtale B E h S hS p hp z τ hτ F) ≫
      restrictModulePullbackComparison B E h S hS p hp (φ ≫ ψ) τ hτ F
```

**`AlgebraicGeometry.Stack.restrictionPushforwardComparison_app_eval_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SmallEtaleRestrictionFinalComparison.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SmallEtaleRestrictionFinalComparison.lean#L196). The attribute's comment: “part (1), the direct-image comparisons read through the evaluation maps of the restriction of Stacks 06W1, so that no comparison of base changes is left over”.

> **Stacks 075D (1) through the evaluation maps.** For arrows `φ : x ⟶ y` and `ψ : y ⟶ z` of
> `𝒳`, the composite of the two comparison maps of Stacks 06W2, precomposed with the evaluation
> map over `z`, is restriction of `F` along `ψ ∘ φ` followed by the evaluation map over `x`.
>
> Read this way the composition statement of Stacks 075D (1) leaves no comparison of base changes
> over: both the composite `c_φ ∘ c_ψ` and the single `c_{ψ ∘ φ}` become restriction along
> `ψ ∘ φ`, and
> `AlgebraicGeometry.Stack.restrictionPushforwardComparison_app_eval_comp_eq_app_comp` recovers
> `AlgebraicGeometry.Stack.restrictionPushforwardComparison_app_comp` from this form.

```lean
theorem restrictionPushforwardComparison_app_eval_comp {A : Type t} [Category.{s} A]
    (F : 𝒳ᵒᵖ ⥤ A) (φ : x ⟶ y) (ψ : y ⟶ z)
    (W : SmallEtale E (p.obj z).left.1 (contains_base B E h S hS p z)) :
    restrictToSmallEtaleEval B E h S hS p hp z F W ≫
        (restrictionPushforwardComparison B E h S hS p hp ψ F).app (op W) ≫
          (restrictionPushforwardComparison B E h S hS p hp φ F).app (op
            ((smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p ψ)).obj W)) =
      F.map (φ ≫ ψ).op ≫ restrictToSmallEtaleEval B E h S hS p hp x F
        ((smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p φ)).obj
          ((smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p ψ)).obj W))
```

**`AlgebraicGeometry.Stack.restrictModulePushforwardComparison_app_eval_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SmallEtaleRestrictionFinalComparison.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SmallEtaleRestrictionFinalComparison.lean#L294). The attribute's comment: “part (1), for the direct-image comparison of a presheaf of modules read through the evaluation maps of the restriction of Stacks 06W1”.

> **Stacks 075D (1) for the module comparison of Stacks 06WC, through the evaluation maps.**
> The module form of `AlgebraicGeometry.Stack.restrictionPushforwardComparison_app_eval_comp`.

```lean
theorem restrictModulePushforwardComparison_app_eval_comp
    (F : PresheafOfModules.{m} (ringStructureSheafCore B S hS p hp τ hτ).obj)
    (φ : x ⟶ y) (ψ : y ⟶ z)
    (W : SmallEtale E (p.obj z).left.1 (contains_base B E h S hS p z))
    (n : F.presheaf.obj (op z)) :
    (restrictModulePushforwardComparison B E h S hS p hp φ τ hτ F).app
        (op ((smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p ψ)).obj W))
        ((restrictModulePushforwardComparison B E h S hS p hp ψ τ hτ F).app (op W)
          (restrictToSmallEtaleEval B E h S hS p hp z F.presheaf W n)) =
      restrictToSmallEtaleEval B E h S hS p hp x F.presheaf
        ((smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p φ)).obj
          ((smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p ψ)).obj W))
        (F.presheaf.map (φ ≫ ψ).op n)
```

**`AlgebraicGeometry.Stack.restrictToSmallEtaleInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComparison.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComparison.lean#L160). The attribute's comment: “part (3), the identification”.

> Restriction to a small étale site commutes canonically with inverse image along a 1-morphism
> of categories fibred in groupoids: the restriction at `y` of the inverse image of `F` is the
> restriction of `F` at `G y`.

```lean
noncomputable def restrictToSmallEtaleInverseImageIso {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids)
    {𝒴 : Type v'} [Category.{w'} 𝒴] (G : 𝒴 ⥤ 𝒳) (hGp : (G ⋙ p).IsFiberedInGroupoids)
    (hG : (G ⋙ p).IsFibredOneMorphism p G) (y : 𝒴)
    (F : Sheaf (associatedTopology B S hS p (etaleTopology B)) (Type t)) :
    letI : (G ⋙ p).IsFibered := hGp.isFibered
    letI : p.IsFibered := hp.isFibered
    letI := (hG.isContinuous_and_isCocontinuous_inheritedTopology
      ((etaleTopology B).over (B.obj hS))).1
    restrictToSmallEtale B E h S hS (G ⋙ p) hGp y
        ((G.sheafPushforwardContinuous (Type t)
          (associatedTopology B S hS (G ⋙ p) (etaleTopology B))
          (associatedTopology B S hS p (etaleTopology B))).obj F).obj ≅
      restrictToSmallEtale B E h S hS p hp (G.obj y) F.obj
```

**`AlgebraicGeometry.Stack.existsUnique_inverseImageComparisonLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComparison.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComparison.lean#L277). The attribute's comment: “part (3), the unique comparison arrow”.

> Over a small étale object there is exactly one arrow of `𝒳` from the cartesian lift at `G y` to
> the image of the cartesian lift at `y` compatible with the structure morphisms and lying over the
> canonical comparison of their bases.

```lean
theorem existsUnique_inverseImageComparisonLift {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids)
    {𝒴 : Type v'} [Category.{w'} 𝒴] (G : 𝒴 ⥤ 𝒳) (hGp : (G ⋙ p).IsFiberedInGroupoids) (y : 𝒴)
    (W : SmallEtale E (p.obj (G.obj y)).left.1 (contains_base B E h S hS p (G.obj y))) :
    let P := Over.post (X := G.obj y) (p ⋙ Over.forget (B.obj hS))
    let Q := Over.post (X := y) ((G ⋙ p) ⋙ Over.forget (B.obj hS))
    letI : P.IsEquivalence := isEquivalence_overPost B S hS p hp (G.obj y)
    letI : Q.IsEquivalence := isEquivalence_overPost B S hS (G ⋙ p) hGp y
    let V := (smallEtaleInclusion B E h (p.obj (G.obj y)).left.1
      (contains_base B E h S hS p (G.obj y))).obj W
    let a := P.inv.obj V
    let b := Q.inv.obj V
    ∃! φ : a.left ⟶ G.obj b.left,
      (φ ≫ G.map b.hom = a.hom) ∧
      ((p.map φ).left ≫ (Q.objObjPreimageIso V).hom.left =
        (P.objObjPreimageIso V).hom.left)
```

**`AlgebraicGeometry.Stack.restrictToSmallEtaleInverseImageIso_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComparison.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComparison.lean#L338). The attribute's comment: “part (3), the component formula”.

> On sections over a small étale object, the identification
> `AlgebraicGeometry.Stack.restrictToSmallEtaleInverseImageIso` is restriction of `F` along the
> unique comparison arrow of `AlgebraicGeometry.Stack.existsUnique_inverseImageComparisonLift`.

```lean
theorem restrictToSmallEtaleInverseImageIso_app {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids)
    {𝒴 : Type v'} [Category.{w'} 𝒴] (G : 𝒴 ⥤ 𝒳) (hGp : (G ⋙ p).IsFiberedInGroupoids)
    (hG : (G ⋙ p).IsFibredOneMorphism p G) (y : 𝒴)
    (F : Sheaf (associatedTopology B S hS p (etaleTopology B)) (Type t))
    (W : SmallEtale E (p.obj (G.obj y)).left.1 (contains_base B E h S hS p (G.obj y))) :
    letI : (G ⋙ p).IsFibered := hGp.isFibered
    letI : p.IsFibered := hp.isFibered
    letI := (hG.isContinuous_and_isCocontinuous_inheritedTopology
      ((etaleTopology B).over (B.obj hS))).1
    let P := Over.post (X := G.obj y) (p ⋙ Over.forget (B.obj hS))
    let Q := Over.post (X := y) ((G ⋙ p) ⋙ Over.forget (B.obj hS))
    letI : P.IsEquivalence := isEquivalence_overPost B S hS p hp (G.obj y)
    letI : Q.IsEquivalence := isEquivalence_overPost B S hS (G ⋙ p) hGp y
    let V := (smallEtaleInclusion B E h (p.obj (G.obj y)).left.1
      (contains_base B E h S hS p (G.obj y))).obj W
    let a := P.inv.obj V
    let b := Q.inv.obj V
    ∀ φ : a.left ⟶ G.obj b.left, φ ≫ G.map b.hom = a.hom →
      (p.map φ).left ≫ (Q.objObjPreimageIso V).hom.left =
        (P.objObjPreimageIso V).hom.left →
      (restrictToSmallEtaleInverseImageIso B E h S hS p hp G hGp hG y F).hom.app
          (Opposite.op W) = F.obj.map φ.op
```

**`AlgebraicGeometry.Stack.restrictToSmallEtaleSheafInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComparison.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComparison.lean#L409). The attribute's comment: “part (3), on sheaves”.

> The identification `AlgebraicGeometry.Stack.restrictToSmallEtaleInverseImageIso`, as an
> isomorphism of sheaves.

```lean
noncomputable def restrictToSmallEtaleSheafInverseImageIso {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids)
    {𝒴 : Type v'} [Category.{w'} 𝒴] (G : 𝒴 ⥤ 𝒳) (hGp : (G ⋙ p).IsFiberedInGroupoids)
    (hG : (G ⋙ p).IsFibredOneMorphism p G) (y : 𝒴)
    (F : Sheaf (associatedTopology B S hS p (etaleTopology B)) (Type (max (u + 1) t))) :
    letI : (G ⋙ p).IsFibered := hGp.isFibered
    letI : p.IsFibered := hp.isFibered
    letI := (hG.isContinuous_and_isCocontinuous_inheritedTopology
      ((etaleTopology B).over (B.obj hS))).1
    restrictToSmallEtaleSheaf B E h S hS (G ⋙ p) hGp y
        ((G.sheafPushforwardContinuous (Type (max (u + 1) t))
          (associatedTopology B S hS (G ⋙ p) (etaleTopology B))
          (associatedTopology B S hS p (etaleTopology B))).obj F) ≅
      restrictToSmallEtaleSheaf B E h S hS p hp (G.obj y) F
```

**`AlgebraicGeometry.Stack.restrictionPushforwardComparison_comp_inverseImageIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComparison.lean, line 481](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComparison.lean#L481). The attribute's comment: “part (4), for the direct-image comparison of a presheaf of sets”.

> The comparison maps of Stacks 06W2 for `ψ : y' ⟶ y` in `𝒴` and for its image `G ψ` in `𝒳`
> agree under the identifications `AlgebraicGeometry.Stack.restrictToSmallEtaleInverseImageIso`.

```lean
theorem restrictionPushforwardComparison_comp_inverseImageIso {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids)
    {𝒴 : Type v'} [Category.{w'} 𝒴] (G : 𝒴 ⥤ 𝒳) (hGp : (G ⋙ p).IsFiberedInGroupoids)
    (hG : (G ⋙ p).IsFibredOneMorphism p G) {y' y : 𝒴} (ψ : y' ⟶ y)
    (F : Sheaf (associatedTopology B S hS p (etaleTopology B)) (Type t)) :
    letI : (G ⋙ p).IsFibered := hGp.isFibered
    letI : p.IsFibered := hp.isFibered
    letI := (hG.isContinuous_and_isCocontinuous_inheritedTopology
      ((etaleTopology B).over (B.obj hS))).1
    let F' := (G.sheafPushforwardContinuous (Type t)
      (associatedTopology B S hS (G ⋙ p) (etaleTopology B))
      (associatedTopology B S hS p (etaleTopology B))).obj F
    let b := smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p (G.map ψ))
    (restrictToSmallEtaleInverseImageIso B E h S hS p hp G hGp hG y F).hom ≫
        restrictionPushforwardComparison B E h S hS p hp (G.map ψ) F.obj =
      restrictionPushforwardComparison B E h S hS (G ⋙ p) hGp ψ F'.obj ≫
        Functor.whiskerLeft b.op
          (restrictToSmallEtaleInverseImageIso B E h S hS p hp G hGp hG y' F).hom
```

**`AlgebraicGeometry.Stack.restrictionInverseImageComparison_comp_inverseImageIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComparison.lean, line 759](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComparison.lean#L759). The attribute's comment: “part (4)”.

> The comparison maps of Stacks 06W3 for `ψ : y' ⟶ y` in `𝒴` and for its image `G ψ` in `𝒳`
> agree under the identifications
> `AlgebraicGeometry.Stack.restrictToSmallEtaleSheafInverseImageIso`.

```lean
theorem restrictionInverseImageComparison_comp_inverseImageIso {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids)
    {𝒴 : Type v'} [Category.{w'} 𝒴] (G : 𝒴 ⥤ 𝒳) (hGp : (G ⋙ p).IsFiberedInGroupoids)
    (hG : (G ⋙ p).IsFibredOneMorphism p G) {y' y : 𝒴} (ψ : y' ⟶ y)
    (F : Sheaf (associatedTopology B S hS p (etaleTopology B)) (Type (max (u + 1) t))) :
    letI : (G ⋙ p).IsFibered := hGp.isFibered
    letI : p.IsFibered := hp.isFibered
    letI := (hG.isContinuous_and_isCocontinuous_inheritedTopology
      ((etaleTopology B).over (B.obj hS))).1
    let F' := (G.sheafPushforwardContinuous (Type (max (u + 1) t))
      (associatedTopology B S hS (G ⋙ p) (etaleTopology B))
      (associatedTopology B S hS p (etaleTopology B))).obj F
    let a := smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS (G ⋙ p) ψ)
    letI : a.IsContinuous
        (SmallEtale.topology E (p.obj (G.obj y)).left.1
          (contains_base B E h S hS p (G.obj y)))
        (SmallEtale.topology E (p.obj (G.obj y')).left.1
          (contains_base B E h S hS p (G.obj y'))) :=
      smallEtaleBaseChange_isContinuous E (smallEtaleBaseMorphism B E h S hS (G ⋙ p) ψ)
    let iy := restrictToSmallEtaleSheafInverseImageIso B E h S hS p hp G hGp hG y F
    let iy' := restrictToSmallEtaleSheafInverseImageIso B E h S hS p hp G hGp hG y' F
    (a.sheafPullback (Type (max (u + 1) t))
          (SmallEtale.topology E (p.obj (G.obj y)).left.1
            (contains_base B E h S hS p (G.obj y)))
          (SmallEtale.topology E (p.obj (G.obj y')).left.1
            (contains_base B E h S hS p (G.obj y')))).map iy.hom ≫
        restrictionInverseImageComparison B E h S hS p hp (G.map ψ) F =
      restrictionInverseImageComparison B E h S hS (G ⋙ p) hGp ψ F' ≫ iy'.hom
```

**`AlgebraicGeometry.Stack.restrictionInverseImageCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComposition.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComposition.lean#L166). The attribute's comment: “part (1), the identification of successive inverse images”.

> The canonical identification, for arrows `φ : x ⟶ y` and `ψ : y ⟶ z` of a category fibred
> in groupoids, of the composite of the small étale inverse images along the underlying morphisms
> of schemes with the inverse image along the underlying morphism of `ψ ∘ φ`.
>
> This is the identification appearing in **Stacks 075D (1)**. It is the mate of the direct-image
> comparison induced by `AlgebraicGeometry.smallEtaleBaseChange_factoredCompIso`.

```lean
noncomputable def restrictionInverseImageCompIso {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) {x y z : 𝒳} (φ : x ⟶ y) (ψ : y ⟶ z) :
    (smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p ψ)).sheafPullback
        (Type (max (u + 1) t))
        (SmallEtale.topology E (p.obj z).left.1 (contains_base B E h S hS p z))
        (SmallEtale.topology E (p.obj y).left.1 (contains_base B E h S hS p y)) ⋙
      (smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p φ)).sheafPullback
        (Type (max (u + 1) t))
        (SmallEtale.topology E (p.obj y).left.1 (contains_base B E h S hS p y))
        (SmallEtale.topology E (p.obj x).left.1 (contains_base B E h S hS p x)) ≅
    (smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p (φ ≫ ψ))).sheafPullback
      (Type (max (u + 1) t))
      (SmallEtale.topology E (p.obj z).left.1 (contains_base B E h S hS p z))
      (SmallEtale.topology E (p.obj x).left.1 (contains_base B E h S hS p x))
```

**`AlgebraicGeometry.Stack.restrictionPushforwardComparison_app_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComposition.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComposition.lean#L290). The attribute's comment: “part (1), the direct-image form”.

> **Stacks 075D (1)** for the direct-image comparisons of Stacks 06W2: the comparison for a
> composite arrow, followed by restriction along the composition comparison of base changes, is
> the composite of the two comparisons.
>
> This is the form with content; the inverse-image statement of the source is its mate. It holds
> for a presheaf with values in an arbitrary category.

```lean
theorem restrictionPushforwardComparison_app_comp {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids) {x y z : 𝒳}
    (φ : x ⟶ y) (ψ : y ⟶ z) {A : Type t} [Category.{s} A] (F : 𝒳ᵒᵖ ⥤ A)
    (W : SmallEtale E (p.obj z).left.1 (contains_base B E h S hS p z)) :
    (restrictionPushforwardComparison B E h S hS p hp ψ F).app (Opposite.op W) ≫
        (restrictionPushforwardComparison B E h S hS p hp φ F).app (Opposite.op
          ((smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p ψ)).obj W)) =
      (restrictionPushforwardComparison B E h S hS p hp (φ ≫ ψ) F).app (Opposite.op W) ≫
        (restrictToSmallEtale B E h S hS p hp x F).map
          ((smallEtaleBaseChange_factoredCompIso E _ _ _
            (smallEtaleBaseMorphism B E h S hS p φ) (smallEtaleBaseMorphism B E h S hS p ψ)
            (smallEtaleBaseMorphism B E h S hS p (φ ≫ ψ))
            (smallEtaleBaseMorphism_comp B E h S hS p φ ψ).symm).hom.app W).op
```

**`AlgebraicGeometry.Stack.restrictionInverseImageComparison_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComposition.lean, line 414](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionComposition.lean#L414). The attribute's comment: “part (1)”.

> **Stacks 075D (1).** For an étale sheaf on a category fibred in groupoids, the comparison
> map of Stacks 06W3 for a composite arrow is the composite of the two comparison maps, under the
> canonical identification of successive small étale inverse images.

```lean
theorem restrictionInverseImageComparison_comp {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids) {x y z : 𝒳}
    (φ : x ⟶ y) (ψ : y ⟶ z)
    (F : Sheaf (associatedTopology B S hS p (etaleTopology B)) (Type (max (u + 1) t))) :
    ((smallEtaleBaseChange E (smallEtaleBaseMorphism B E h S hS p φ)).sheafPullback
          (Type (max (u + 1) t))
          (SmallEtale.topology E (p.obj y).left.1 (contains_base B E h S hS p y))
          (SmallEtale.topology E (p.obj x).left.1 (contains_base B E h S hS p x))).map
        (restrictionInverseImageComparison B E h S hS p hp ψ F) ≫
      restrictionInverseImageComparison B E h S hS p hp φ F =
    (restrictionInverseImageCompIso B E h S hS p φ ψ).hom.app
        (restrictToSmallEtaleSheaf B E h S hS p hp z F) ≫
      restrictionInverseImageComparison B E h S hS p hp (φ ≫ ψ) F
```

**`AlgebraicGeometry.Stack.isIso_restrictionInverseImageComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionEtaleIso.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SmallEtaleRestrictionEtaleIso.lean#L176). The attribute's comment: “part (2)”.

> **Stacks 075D**, part (2). If an arrow of `𝒳` lies over an étale morphism of schemes, the
> comparison of Stacks 06W3 between the inverse image of the restriction at its target and the
> restriction at its source is an isomorphism.

```lean
theorem isIso_restrictionInverseImageComparison {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids) {x y : 𝒳} (φ : x ⟶ y)
    (hφ : Etale (B.inclusion.map (p.map φ).left))
    (F : Sheaf (associatedTopology B S hS p (etaleTopology B)) (Type (max (u + 1) t))) :
    IsIso (restrictionInverseImageComparison B E h S hS p hp φ F)
```

## Tag 06W9, a lemma

[Tag 06W9](https://stacks.math.columbia.edu/tag/06W9) in the Stacks Project.

**`AlgebraicGeometry.Stack.ringStructureSheafCore_overPost`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalizationStructureSheaf.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocalizationStructureSheaf.lean#L77).

> **Stacks 06W9.** The canonical localization equivalence of Stacks 06W0 carries the structure
> sheaf of the schemes over `(p.obj x).left` to the restriction of the structure sheaf of `𝒳` to
> the slice at `x`, including all restriction maps.

```lean
theorem ringStructureSheafCore_overPost
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids)
    (τ : GrothendieckTopology B.Schemes) (hτ : τ ≤ B.topology) (x : 𝒳) :
    (Over.forget x).op ⋙ (ringStructureSheafCore B S hS p hp τ hτ).obj =
      (Over.post (X := x) (p ⋙ Over.forget (B.obj hS))).op ⋙
        (baseRingStructureSheaf B (p.obj x).left.1 (p.obj x).left.2 τ hτ).obj
```

**`AlgebraicGeometry.Stack.sheafPushforwardContinuous_baseStructureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalizationStructureSheaf.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocalizationStructureSheaf.lean#L142). The attribute's comment: “equivalence of ringed sites”.

> **Stacks 06W9.** The equivalence of Stacks 06W0 is an equivalence of *ringed* sites
> `(𝒳_τ/x, 𝒪_𝒳|_x) ≌ ((Sch/U)_τ, 𝒪)`: the direct image along it of the structure sheaf of the big
> `τ`-site of `U = p(x)` *is* the structure sheaf of `𝒳` restricted to the slice at `x`.
>
> The two sites are identified by `AlgebraicGeometry.Stack.localizationEquivalence` and
> `AlgebraicGeometry.Stack.isDenseSubsite_localizationEquivalence`, and the structure sheaves by
> this equality, which is an equality and not merely an isomorphism.

```lean
theorem sheafPushforwardContinuous_baseStructureSheaf
    (τ : GrothendieckTopology B.Schemes) (hτ : τ ≤ B.topology) (x : 𝒳) :
    ((localizationEquivalence B S hS p hp x).functor.sheafPushforwardContinuous
        CommRingCat.{u} ((associatedTopology B S hS p τ).over x)
        (τ.over (B.obj (p.obj x).left.2))).obj
        (baseStructureSheaf B (p.obj x).left.1 (p.obj x).left.2 τ hτ) =
      (structureSheaf B S hS p hp τ hτ).over x
```

**`AlgebraicGeometry.Stack.sheafPushforwardContinuous_baseRingStructureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalizationStructureSheaf.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocalizationStructureSheaf.lean#L156). The attribute's comment: “equivalence of ringed sites, underlying sheaves of rings”.

> **Stacks 06W9**, the same equivalence of ringed sites read on the underlying sheaves of
> (not necessarily commutative) rings, which is the form the categories of sheaves of modules are
> indexed by: the transport of the base sheaf of rings along the localization equivalence is the
> restriction of the sheaf of rings of `𝒳` to the slice at `x`.

```lean
theorem sheafPushforwardContinuous_baseRingStructureSheaf
    (τ : GrothendieckTopology B.Schemes) (hτ : τ ≤ B.topology) (x : 𝒳) :
    ((localizationEquivalence B S hS p hp x).functor.sheafPushforwardContinuous
        RingCat.{u} ((associatedTopology B S hS p τ).over x)
        (τ.over (B.obj (p.obj x).left.2))).obj
        (baseRingStructureSheaf B (p.obj x).left.1 (p.obj x).left.2 τ hτ) =
      (ringStructureSheafCore B S hS p hp τ hτ).over x
```

## Tag 06WC, an equation

[Tag 06WC](https://stacks.math.columbia.edu/tag/06WC) in the Stacks Project.

**`AlgebraicGeometry.Stack.restrictSheafModulesPullbackComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean#L287). The attribute's comment: “c\_φ of étale sheaves of modules”.

> **Stacks 0761.** The comparison map
> `c_φ : f_{small}^*(F|_{U'_ét}) ⟶ F|_{U_ét}` of Equation (103.7.0.1) for an étale sheaf `F` of
> `𝒪_𝒳`-modules, below an arrow `φ : x ⟶ y` of `𝒳` lying over a morphism of schemes
> `f : U ⟶ U'`. Here `f_{small}^*` is the pullback of modules along the morphism of ringed topoi
> `(Sh(U_ét), 𝒪_U) ⟶ (Sh(U'_ét), 𝒪_{U'})`, that is `SheafOfModules.pullback` along the morphism
> of ringed sites `ε_f` of **Stacks 070R (2)**, whose ring map is the map `f_{small}^♯` of
> **Stacks 06WC**; it includes sheafification.
>
> It is `AlgebraicGeometry.Stack.restrictSheafPullbackComparison` (the adjunct, across
> sheafification on `U_ét`, of the presheaf map
> `AlgebraicGeometry.Stack.restrictModulePullbackComparison` of Sheaves on Stacks, Equation
> (96.9.4.1)) read through the identification
> `AlgebraicGeometry.Stack.sheafifiedPullbackComparisonIso` of the sheafified presheaf pullback
> with `SheafOfModules.pullback`.
>
> This is also **Stacks 06WC**, the comparison map
> `c_φ : a_{small}^*(F|_{V_ét}) ⟶ F|_{U_ét}` of `𝒪_{U_ét}`-modules of Sheaves on Stacks,
> Equation (96.9.4.1), for an étale sheaf `F` of modules on `𝒳`: there too `a_{small}^*` is the
> pullback of sheaves of modules along `ε_a`, the map `a_{small}^♯` being the one of Stacks 070R,
> and `F|_{V_ét}`, `F|_{U_ét}` are the restrictions of Stacks 06WJ.

```lean
noncomputable def restrictSheafModulesPullbackComparison
    (F : SheafOfModules.{u} (ringStructureSheafCore B S hS p hp (etaleTopology B)
      (etaleTopology_le_topology B))) :
    (SheafOfModules.pullback.{u} (SmallEtale.smallEtaleStructureMapRing E
        (smallEtaleBaseMorphism B E h S hS p φ))).obj
        ((restrictSheafToSmallEtale.{u, v, w, u} B E h S hS p hp y).obj F) ⟶
      (restrictSheafToSmallEtale.{u, v, w, u} B E h S hS p hp x).obj F
```

## Tag 06W4, a lemma

[Tag 06W4](https://stacks.math.columbia.edu/tag/06W4) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasConservativeFamily_siteKind`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/EnoughPoints.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/EnoughPoints.lean#L243).

> **Stacks 06W4.** Let `p : 𝒳 ⥤ (Sch/S)_fppf` be a category fibred in groupoids and let
> `τ ∈ {Zar, étale, smooth, syntomic, fppf}`. Then the site `𝒳_τ` has enough points: it has a
> conservative family of points.
>
> The site `𝒳_τ` is `AlgebraicGeometry.BigFppfOver.associatedTopology`, the topology `𝒳`
> inherits along `p` from the localization at `S` of the big `τ` topology (Stacks 06TP). The
> proof is the one of the source: `hasConservativeFamily_associatedTopology` reduces to the
> localizations of the big site, which have enough points by Stacks 06VX.

```lean
theorem hasConservativeFamily_siteKind (hp : p.IsFiberedInGroupoids) (τ : SiteKind) :
    (BigFppfOver.associatedTopology B S hS p τ).HasConservativeFamily.{u + 1}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.9, Tag 075C](https://stacks.math.columbia.edu/tag/075C)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
