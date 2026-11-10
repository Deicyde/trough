---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.preservesInjectiveObjects_abelianDirectImage, AlgebraicGeometry.Stack.preservesInjectiveObjects_sheafOfModulesDirectImage, AlgebraicGeometry.Stack.abelianDirectImage_preservesInjectiveObjects, AlgebraicGeometry.Stack.preservesInjectiveObjects_sheafPushforwardCocontinuous, AlgebraicGeometry.Stack.preservesInjectiveObjects_of_adjunction_sheafOfModules_pushforward, AlgebraicGeometry.Stack.hasEqualizers_of_isAlgebraicSpaceIsomPresheaf, AlgebraicGeometry.Stack.hasEqualizers_of_isAlgebraicStack, AlgebraicGeometry.Stack.hasEqualizers_quotientStack
statement: formalized
proof: formalized
---

# 96.17 Injective sheaves

Section 96.17 of the Stacks Project, [Tag 06WW](https://stacks.math.columbia.edu/tag/06WW). 6 tags here are carried by 25 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06WX, a lemma

[Tag 06WX](https://stacks.math.columbia.edu/tag/06WX) in the Stacks Project.

**`AlgebraicGeometry.Stack.preservesInjectiveObjects_abelianDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/InjectiveDirectImage.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/InjectiveDirectImage.lean#L74). The attribute's comment: “part (1)”.

> **Stacks 06WX, part (1).** Direct image along a 1-morphism of fibred categories over the
> big fppf category of a scheme carries injective abelian sheaves to injective abelian sheaves,
> for the site each side inherits from an arbitrary topology on the base. The direct image is the
> right Kan extension along `F.op`, which exists for abelian groups in any universe containing
> the objects of the source and the morphisms of the target.

```lean
theorem preservesInjectiveObjects_abelianDirectImage
    [p.IsFibered] [q.IsFibered] (hF : p.IsFibredOneMorphism q F) :
    letI := (hF.isContinuous_and_isCocontinuous_inheritedTopology (τ.over (B.obj hS))).2
    (F.sheafPushforwardCocontinuous AddCommGrpCat.{max v₁ w₂ t}
      (associatedTopology B S hS p τ)
      (associatedTopology B S hS q τ)).PreservesInjectiveObjects
```

**`AlgebraicGeometry.Stack.preservesInjectiveObjects_sheafOfModulesDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/InjectiveDirectImage.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/InjectiveDirectImage.lean#L106). The attribute's comment: “part (2)”.

> **Stacks 06WX, part (2).** Direct image along a 1-morphism of categories fibred in
> groupoids over the big fppf category of a scheme carries injective sheaves of
> `O_𝒳`-modules to injective sheaves of `O_𝒴`-modules, for every topology coarser than the fppf
> topology. The direct image is `SheafOfModules.directImageOfEq`, the right Kan extension along
> `F.op` with its module structure, which is right adjoint to the inverse image of modules.

```lean
theorem preservesInjectiveObjects_sheafOfModulesDirectImage
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) (hcomp : F ⋙ q = p)
    (hτ : τ ≤ B.topology) :
    letI : p.IsFibered := hp.isFibered
    letI : q.IsFibered := hq.isFibered
    letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
      (τ.over (B.obj hS))).1
    letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
      (τ.over (B.obj hS))).2
    (SheafOfModules.directImageOfEq.{u, max v₁ w₂ t} F (associatedTopology B S hS p τ)
      (associatedTopology B S hS q τ) (ringStructureSheafCore B S hS q hq τ hτ)
      (ringStructureSheafCore_eq_sheafPushforwardContinuous_obj B S hS p q F τ hp hq hcomp
        hτ)).PreservesInjectiveObjects
```

**`AlgebraicGeometry.Stack.abelianDirectImage_preservesInjectiveObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/InjectivePushforward.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/InjectivePushforward.lean#L64). The attribute's comment: “injective_pushforward_abelian”.

> **Stacks 06WX, part (1).** Direct image under a fibred 1-morphism preserves injective
> abelian sheaves, for any of the five associated topologies.

```lean
theorem abelianDirectImage_preservesInjectiveObjects
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 : Type v₁} [Category.{w₁} 𝒳]
    {𝒴 : Type v₂} [Category.{w₂} 𝒴]
    {p𝒳 : 𝒳 ⥤ BigFppfOver B S hS}
    {p𝒴 : 𝒴 ⥤ BigFppfOver B S hS}
    [p𝒳.IsFibered] [p𝒴.IsFibered]
    {F : 𝒳 ⥤ 𝒴} (hF : p𝒳.IsFibredOneMorphism p𝒴 F)
    (τ : SiteKind)
    [∀ (G : 𝒳ᵒᵖ ⥤ AddCommGrpCat.{t}), F.op.HasPointwiseRightKanExtension G] :
    letI := (hF.isContinuous_and_isCocontinuous_inheritedTopology
      (BigFppfOver.baseOverTopology B S hS τ)).2
    (F.sheafPushforwardCocontinuous AddCommGrpCat.{t}
      (BigFppfOver.associatedTopology B S hS p𝒳 τ)
      (BigFppfOver.associatedTopology B S hS p𝒴 τ)).PreservesInjectiveObjects
```

**`AlgebraicGeometry.Stack.preservesInjectiveObjects_sheafPushforwardCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean#L143). The attribute's comment: “part (1)”.

> **Stacks 06WX, part (1).** Direct image along a 1-morphism of fibred categories over the
> big fppf category of a scheme carries injective abelian sheaves to injective abelian sheaves,
> for the site each side inherits from an arbitrary topology on the base.
>
> The inverse image is the left adjoint of direct image and preserves finite limits, hence
> monomorphisms, and a right adjoint of a monomorphism-preserving functor preserves injectives.

```lean
theorem preservesInjectiveObjects_sheafPushforwardCocontinuous
    [p.IsFibered] [q.IsFibered] (hF : p.IsFibredOneMorphism q F)
    [∀ G : 𝒳ᵒᵖ ⥤ AddCommGrpCat.{t}, F.op.HasPointwiseRightKanExtension G] :
    letI := (hF.isContinuous_and_isCocontinuous_inheritedTopology (τ.over (B.obj hS))).2
    (F.sheafPushforwardCocontinuous AddCommGrpCat.{t}
      (associatedTopology B S hS p τ)
      (associatedTopology B S hS q τ)).PreservesInjectiveObjects
```

**`AlgebraicGeometry.Stack.preservesInjectiveObjects_of_adjunction_sheafOfModules_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean#L218). The attribute's comment: “part (2)”.

> **Stacks 06WX, part (2).** Direct image along a 1-morphism of categories fibred in
> groupoids carries injective sheaves of modules to injective sheaves of modules: any functor `G`
> right adjoint to the inverse image of modules preserves injective objects.
>
> `G` is the direct image of sheaves of modules; its existence is Stacks 06X0 and is taken as the
> hypothesis `adj` rather than constructed, so that the statement is about whichever functor is
> adjoint to the inverse image.

```lean
theorem preservesInjectiveObjects_of_adjunction_sheafOfModules_pushforward
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) (hcomp : F ⋙ q = p)
    (hτ : τ ≤ B.topology)
    (G : letI : p.IsFibered := hp.isFibered
      SheafOfModules.{t} (ringStructureSheafCore B S hS p hp τ hτ) ⥤
        SheafOfModules.{t} (ringStructureSheafCore B S hS q hq τ hτ))
    (adj : letI : p.IsFibered := hp.isFibered
      letI : q.IsFibered := hq.isFibered
      letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
        (τ.over (B.obj hS))).1
      SheafOfModules.pushforward.{t}
        (ringStructureSheafCoreHom B S hS p q F τ hp hq hcomp hτ) ⊣ G) :
    G.PreservesInjectiveObjects
```

## Tag 06WY, a lemma

[Tag 06WY](https://stacks.math.columbia.edu/tag/06WY) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasEqualizers_of_isAlgebraicSpaceIsomPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Equalizers.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Equalizers.lean#L68). The attribute's comment: “part (2)”.

> **Stacks 06WY (2).** Let `𝒳` be a category fibred in groupoids over the big fppf site of `S`
> whose isomorphism presheaves `Isom(x, y)` are algebraic spaces. Then `𝒳` has equalizers.

```lean
theorem hasEqualizers_of_isAlgebraicSpaceIsomPresheaf
    (𝒳 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS))
    (h : IsAlgebraicSpaceIsomPresheaf B S hS 𝒳) : HasEqualizers 𝒳.val.obj
```

**`AlgebraicGeometry.Stack.hasEqualizers_of_isAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Equalizers.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Equalizers.lean#L92). The attribute's comment: “part (3)”.

> **Stacks 06WY, part (3).** An algebraic stack over `S` has equalizers, its isomorphism
> presheaves being algebraic spaces.

```lean
theorem hasEqualizers_of_isAlgebraicStack
    (𝒳 : CatFiberedInGroupoids.{u, v, u + 1, t} (BigFppfOver B S hS))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val) : HasEqualizers 𝒳.val.obj
```

**`AlgebraicGeometry.Stack.hasEqualizers_quotientStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Equalizers.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Equalizers.lean#L110). The attribute's comment: “part (3), the quotient stacks of its parenthetical”.

> **Stacks 06WY, part (3), for quotient stacks.** The quotient stack `[U/R]` of a groupoid in
> algebraic spaces over `S` has equalizers.
>
> Its isomorphism presheaves are algebraic spaces by Stacks 04TB,
> `AlgebraicGeometry.Stack.isAlgebraicSpace_isomPresheaf`, and part (2) applies.

```lean
theorem hasEqualizers_quotientStack {A : AlgebraicSpaces B S hS}
    (G : GroupoidInAlgebraicSpaces B S hS A) :
    HasEqualizers (quotientStack G).obj
```

**`AlgebraicGeometry.BigFppfOver.hasPullbacks_of_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FibreProducts.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FibreProducts.lean#L67). The attribute's comment: “part (1)”.

> **Stacks 06WY, part (1).** A category fibred in groupoids over the big fppf category of a
> scheme has fibre products.

```lean
theorem hasPullbacks_of_isFiberedInGroupoids
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 : Type*} [Category 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids) :
    HasPullbacks 𝒳
```

## Tag 06WZ, a lemma

[Tag 06WZ](https://stacks.math.columbia.edu/tag/06WZ) in the Stacks Project.

**`CategoryTheory.CatFiberedInGroupoids.preservesPullbacks_homFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FibreProducts.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FibreProducts.lean#L88). The attribute's comment: “preserves_fibre_products”.

> **Stacks 06WZ.** A morphism of categories fibred in groupoids over a base category with
> fibre products preserves fibre products.

```lean
instance preservesPullbacks_homFunctor (f : 𝒳 ⟶ 𝒴) :
    PreservesLimitsOfShape WalkingCospan (homFunctor f)
```

**`CategoryTheory.CatFiberedInGroupoids.preservesEqualizers_homFunctor_of_faithful`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FibreProducts.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/FibreProducts.lean#L214). The attribute's comment: “preserves_equalizers”.

> **Stacks 06WZ.** A faithful morphism of categories fibred in groupoids preserves
> equalizers.

```lean
instance preservesEqualizers_homFunctor_of_faithful (f : 𝒳 ⟶ 𝒴)
    [Functor.Faithful (homFunctor f)] :
    PreservesLimitsOfShape WalkingParallelPair (homFunctor f)
```

## Tag 06X0, a lemma

[Tag 06X0](https://stacks.math.columbia.edu/tag/06X0) in the Stacks Project.

**`CategoryTheory.TwoFibreProductOver.faithful_fst_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/TwoFibreProductEqualizers.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/TwoFibreProductEqualizers.lean#L260). The attribute's comment: “part (1)”.

> **Stacks 06X0, part (1).** The 2-fibre product of faithful functors is faithful over their
> common target.

```lean
theorem faithful_fst_comp [F.Faithful] [G.Faithful] :
    (TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴 F G ⋙ F).Faithful
```

**`CategoryTheory.TwoFibreProductOver.hasEqualizers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/TwoFibreProductEqualizers.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/TwoFibreProductEqualizers.lean#L276). The attribute's comment: “part (2)”.

> **Stacks 06X0, part (2).** Equalizers in the two source categories induce equalizers in
> their 2-fibre product over the common base.

```lean
theorem hasEqualizers
    (h𝒳 : p𝒳.IsFiberedInGroupoids) (h𝒵 : p𝒵.IsFiberedInGroupoids)
    (h𝒴 : p𝒴.IsFiberedInGroupoids)
    (hF : F ⋙ p𝒴 = p𝒳) (hG : G ⋙ p𝒴 = p𝒵)
    [F.Faithful] [G.Faithful] [HasEqualizers 𝒳] [HasEqualizers 𝒵] :
    HasEqualizers (TwoFibreProductOver p𝒳 p𝒵 p𝒴 F G)
```

## Tag 06X1, a lemma

[Tag 06X1](https://stacks.math.columbia.edu/tag/06X1) in the Stacks Project.

**`AlgebraicGeometry.Stack.exact_sheafPullback_of_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean#L250). The attribute's comment: “part (1)”.

> **Stacks 06X1, part (1).** For a faithful 1-morphism of categories fibred in groupoids
> whose source has equalizers, lower shriek `f_!` on abelian sheaves is exact.
>
> Finite colimits are preserved because `f_!` is a left adjoint. Finite limits are preserved by
> the criterion of Stacks 04BH: the source has fibre products (Stacks 06WY) and equalizers by
> hypothesis, and `f` preserves both (Stacks 06WZ, in the form that places no constraint between
> the universes of source and target).

```lean
theorem exact_sheafPullback_of_faithful
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) (hcomp : F ⋙ q = p)
    [F.Faithful] [HasEqualizers 𝒳]
    [∀ G : 𝒳ᵒᵖ ⥤ Ab.{t}, F.op.HasPointwiseLeftKanExtension G]
    [HasSheafify (associatedTopology B S hS q τ) Ab.{t}] :
    letI : p.IsFibered := hp.isFibered
    letI : q.IsFibered := hq.isFibered
    letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
      (τ.over (B.obj hS))).1
    exactFunctor _ _
      (Functor.sheafPullbackConstruction.sheafPullback F Ab.{t}
        (associatedTopology B S hS p τ) (associatedTopology B S hS q τ))
```

**`AlgebraicGeometry.Stack.injective_sheafPushforwardContinuous_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean#L281). The attribute's comment: “part (2)”.

> **Stacks 06X1, part (2).** The inverse image of an injective abelian sheaf is injective,
> when the 1-morphism is faithful and its source has equalizers.
>
> The inverse image is right adjoint to the exact functor `f_!` of part (1), which therefore
> preserves monomorphisms.

```lean
theorem injective_sheafPushforwardContinuous_obj
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) (hcomp : F ⋙ q = p)
    [F.Faithful] [HasEqualizers 𝒳]
    [∀ G : 𝒳ᵒᵖ ⥤ Ab.{t}, F.op.HasPointwiseLeftKanExtension G]
    [HasSheafify (associatedTopology B S hS q τ) Ab.{t}]
    (I : Sheaf (associatedTopology B S hS q τ) Ab.{t}) [Injective I] :
    letI : p.IsFibered := hp.isFibered
    letI : q.IsFibered := hq.isFibered
    letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
      (τ.over (B.obj hS))).1
    Injective ((F.sheafPushforwardContinuous Ab.{t}
      (associatedTopology B S hS p τ) (associatedTopology B S hS q τ)).obj I)
```

**`AlgebraicGeometry.Stack.isRightAdjoint_sheafPushforwardContinuous_of_essentiallySmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean#L513). The attribute's comment: “f⁻¹ has a left adjoint f_!”.

> **Stacks 06X1, the left adjoint.** For a 1-morphism `f` of categories fibred in groupoids
> over the big fppf category of `S` and any topology `τ` on the underlying category of schemes,
> the inverse image `f⁻¹ : Ab(𝒴_τ) ⥤ Ab(𝒳_τ)` has a left adjoint `f_!`.
>
> The functor `f` is continuous for the associated topologies (Stacks 06NW). The pointwise left Kan
> extensions along `f.op` exist because `𝒳` is essentially small and `𝒴` locally small, and
> sheafification on `𝒴_τ` exists because `𝒴` is essentially small; so `f_!` is the sheafified
> left Kan extension of Stacks 04BG,
> `CategoryTheory.Functor.sheafPullbackConstruction.sheafAdjunctionContinuous`.

```lean
theorem isRightAdjoint_sheafPushforwardContinuous_of_essentiallySmall
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) (hcomp : F ⋙ q = p)
    [EssentiallySmall.{t} 𝒳] [EssentiallySmall.{t} 𝒴] :
    letI : p.IsFibered := hp.isFibered
    letI : q.IsFibered := hq.isFibered
    letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
      (τ.over (B.obj hS))).1
    (F.sheafPushforwardContinuous Ab.{t}
      (associatedTopology B S hS p τ) (associatedTopology B S hS q τ)).IsRightAdjoint
```

**`AlgebraicGeometry.Stack.exact_leftAdjoint_sheafPushforwardContinuous_of_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean#L542). The attribute's comment: “part (1)”.

> **Stacks 06X1, part (1).** For a faithful 1-morphism of categories fibred in groupoids over
> the big fppf category of `S` whose source has equalizers, the left adjoint `f_!` of the inverse
> image `f⁻¹ : Ab(𝒴_τ) ⥤ Ab(𝒳_τ)` is exact, for any topology `τ` on the underlying category of
> schemes.
>
> The left adjoint is isomorphic to the sheafified left Kan extension, which is exact by
> `AlgebraicGeometry.Stack.exact_sheafPullback_of_faithful` (Stacks 04BH, with the hypotheses of
> that criterion supplied by Stacks 06WY and 06WZ); the pointwise Kan extensions and the
> sheafification it uses exist by essential smallness of `𝒳` and `𝒴`.

```lean
theorem exact_leftAdjoint_sheafPushforwardContinuous_of_faithful
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) (hcomp : F ⋙ q = p)
    [F.Faithful] [HasEqualizers 𝒳] [EssentiallySmall.{t} 𝒳] [EssentiallySmall.{t} 𝒴] :
    letI : p.IsFibered := hp.isFibered
    letI : q.IsFibered := hq.isFibered
    letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
      (τ.over (B.obj hS))).1
    letI : (F.sheafPushforwardContinuous Ab.{t}
        (associatedTopology B S hS p τ) (associatedTopology B S hS q τ)).IsRightAdjoint :=
      isRightAdjoint_sheafPushforwardContinuous_of_essentiallySmall B S hS p q F τ hp hq hcomp
    exactFunctor _ _ (F.sheafPushforwardContinuous Ab.{t}
      (associatedTopology B S hS p τ) (associatedTopology B S hS q τ)).leftAdjoint
```

**`AlgebraicGeometry.Stack.injective_sheafPushforwardContinuous_obj_of_essentiallySmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean#L581). The attribute's comment: “part (2)”.

> **Stacks 06X1, part (2).** For a faithful 1-morphism of categories fibred in groupoids over
> the big fppf category of `S` whose source has equalizers, the inverse image of an injective
> abelian sheaf on `𝒴_τ` is an injective abelian sheaf on `𝒳_τ`, for any topology `τ` on the
> underlying category of schemes.
>
> The inverse image is right adjoint to the functor `f_!`, which is exact by part (1) and so
> preserves monomorphisms (Stacks 015Z).

```lean
theorem injective_sheafPushforwardContinuous_obj_of_essentiallySmall
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) (hcomp : F ⋙ q = p)
    [F.Faithful] [HasEqualizers 𝒳] [EssentiallySmall.{t} 𝒳] [EssentiallySmall.{t} 𝒴]
    (I : Sheaf (associatedTopology B S hS q τ) Ab.{t}) [Injective I] :
    letI : p.IsFibered := hp.isFibered
    letI : q.IsFibered := hq.isFibered
    letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
      (τ.over (B.obj hS))).1
    Injective ((F.sheafPushforwardContinuous Ab.{t}
      (associatedTopology B S hS p τ) (associatedTopology B S hS q τ)).obj I)
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.sheafPullbackConstruction.sheafAdjunctionContinuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPullbackConstruction.sheafAdjunctionContinuous#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean#L239) (StacksFrontier): “the adjunction f_! ⊣ f⁻¹”. References: SGA 4 III (1.3), “more general”; SGA 4 III (2.6); SGA 4 IV (4.7), “partial”; SGA 4 IV (4.9.1), “partial”; SGA 4 VI (7.4.13.4).

## Tag 06X2, a lemma

[Tag 06X2](https://stacks.math.columbia.edu/tag/06X2) in the Stacks Project.

**`AlgebraicGeometry.Stack.lowerShriekForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean#L318). The attribute's comment: “underlying abelian sheaves”.

> **Stacks 06X2.** Lower shriek on sheaves of modules agrees, on underlying abelian sheaves,
> with lower shriek on abelian sheaves.
>
> Both sides are computed by sheafifying a presheaf-level left adjoint, and at the presheaf level
> the two agree because every slice functor of a 1-morphism of categories fibred in groupoids is
> an equivalence: that is
> `Stacks.ModuleLowerShriek.pullbackCompToPresheafIso`. Without the slice hypothesis the
> statement is false, by `Stacks.SheafOfModules.lowerShriekForget_not_isomorphic`.

```lean
noncomputable def lowerShriekForgetIso
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) (hcomp : F ⋙ q = p)
    (hτ : τ ≤ B.topology)
    (hPresheaf :
      letI : p.IsFibered := hp.isFibered
      letI : q.IsFibered := hq.isFibered
      letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
        (τ.over (B.obj hS))).1
      (PresheafOfModules.pushforward.{t}
        (ringStructureSheafCoreHom B S hS p q F τ hp hq hcomp hτ).hom).IsRightAdjoint)
    [∀ G : 𝒳ᵒᵖ ⥤ AddCommGrpCat.{t}, F.op.HasPointwiseLeftKanExtension G]
    [HasWeakSheafify (associatedTopology B S hS q τ) AddCommGrpCat.{t}]
    [(associatedTopology B S hS q τ).WEqualsLocallyBijective AddCommGrpCat.{t}] :
    letI : p.IsFibered := hp.isFibered
    letI : q.IsFibered := hq.isFibered
    letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
      (τ.over (B.obj hS))).1
    letI : (PresheafOfModules.pushforward.{t}
      (ringStructureSheafCoreHom B S hS p q F τ hp hq hcomp hτ).hom).IsRightAdjoint := hPresheaf
    letI : (SheafOfModules.pushforward.{t}
      (ringStructureSheafCoreHom B S hS p q F τ hp hq hcomp hτ)).IsRightAdjoint :=
      SheafOfModules.instIsRightAdjointPushforward _
    SheafOfModules.pullback.{t} (ringStructureSheafCoreHom B S hS p q F τ hp hq hcomp hτ) ⋙
        SheafOfModules.toSheaf.{t} (ringStructureSheafCore B S hS q hq τ hτ) ≅
      SheafOfModules.toSheaf.{t} (ringStructureSheafCore B S hS p hp τ hτ) ⋙
        Functor.sheafPullbackConstruction.sheafPullback F AddCommGrpCat.{t}
          (associatedTopology B S hS p τ) (associatedTopology B S hS q τ)
```

**`AlgebraicGeometry.Stack.exact_sheafOfModules_pullback_of_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean#L384). The attribute's comment: “part (1)”.

> **Stacks 06X2, part (1).** For a faithful 1-morphism of categories fibred in groupoids
> whose source has equalizers, lower shriek `f_!` on sheaves of modules is exact.
>
> Finite colimits are preserved because `f_!` is a left adjoint. Finite limits are preserved
> because `SheafOfModules.toSheaf` reflects them and, composed with `f_!`, is the abelian `f_!`
> of Stacks 06X1 (1) up to `lowerShriekForgetIso`, which is exact.

```lean
theorem exact_sheafOfModules_pullback_of_faithful
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) (hcomp : F ⋙ q = p)
    (hτ : τ ≤ B.topology) [F.Faithful] [HasEqualizers 𝒳]
    (hPresheaf :
      letI : p.IsFibered := hp.isFibered
      letI : q.IsFibered := hq.isFibered
      letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
        (τ.over (B.obj hS))).1
      (PresheafOfModules.pushforward.{t}
        (ringStructureSheafCoreHom B S hS p q F τ hp hq hcomp hτ).hom).IsRightAdjoint)
    [∀ G : 𝒳ᵒᵖ ⥤ AddCommGrpCat.{t}, F.op.HasPointwiseLeftKanExtension G]
    [HasSheafify (associatedTopology B S hS q τ) AddCommGrpCat.{t}]
    [(associatedTopology B S hS q τ).WEqualsLocallyBijective AddCommGrpCat.{t}] :
    letI : p.IsFibered := hp.isFibered
    letI : q.IsFibered := hq.isFibered
    letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
      (τ.over (B.obj hS))).1
    letI : (PresheafOfModules.pushforward.{t}
      (ringStructureSheafCoreHom B S hS p q F τ hp hq hcomp hτ).hom).IsRightAdjoint := hPresheaf
    letI : (SheafOfModules.pushforward.{t}
      (ringStructureSheafCoreHom B S hS p q F τ hp hq hcomp hτ)).IsRightAdjoint :=
      SheafOfModules.instIsRightAdjointPushforward _
    exactFunctor _ _
      (SheafOfModules.pullback.{t}
        (ringStructureSheafCoreHom B S hS p q F τ hp hq hcomp hτ))
```

**`AlgebraicGeometry.Stack.injective_sheafOfModules_pushforward_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean#L441). The attribute's comment: “part (2)”.

> **Stacks 06X2, part (2).** The inverse image of an injective sheaf of modules is
> injective, when the 1-morphism is faithful and its source has equalizers.
>
> The inverse image of modules is right adjoint to the exact functor `f_!` of part (1), which
> therefore preserves monomorphisms.

```lean
theorem injective_sheafOfModules_pushforward_obj
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) (hcomp : F ⋙ q = p)
    (hτ : τ ≤ B.topology) [F.Faithful] [HasEqualizers 𝒳]
    (hPresheaf :
      letI : p.IsFibered := hp.isFibered
      letI : q.IsFibered := hq.isFibered
      letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
        (τ.over (B.obj hS))).1
      (PresheafOfModules.pushforward.{t}
        (ringStructureSheafCoreHom B S hS p q F τ hp hq hcomp hτ).hom).IsRightAdjoint)
    [∀ G : 𝒳ᵒᵖ ⥤ AddCommGrpCat.{t}, F.op.HasPointwiseLeftKanExtension G]
    [HasSheafify (associatedTopology B S hS q τ) AddCommGrpCat.{t}]
    [(associatedTopology B S hS q τ).WEqualsLocallyBijective AddCommGrpCat.{t}]
    (I : SheafOfModules.{t} (ringStructureSheafCore B S hS q hq τ hτ)) [Injective I] :
    letI : p.IsFibered := hp.isFibered
    letI : q.IsFibered := hq.isFibered
    letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
      (τ.over (B.obj hS))).1
    Injective ((SheafOfModules.pushforward.{t}
      (ringStructureSheafCoreHom B S hS p q F τ hp hq hcomp hτ)).obj I)
```

**`AlgebraicGeometry.Stack.isRightAdjoint_sheafOfModules_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/ModuleLowerShriek.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/ModuleLowerShriek.lean#L93). The attribute's comment: “f^* on sheaves of modules has a left adjoint f_!”.

> **Stacks 06X2, existence of `f_!`.** Inverse image of sheaves of modules along a
> 1-morphism of categories fibred in groupoids over the big fppf category of a scheme has a left
> adjoint `f_!`.

```lean
theorem isRightAdjoint_sheafOfModules_pushforward
    [EssentiallySmall.{t} 𝒳] [EssentiallySmall.{t} 𝒴] [UnivLE.{u, t}]
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) (hcomp : F ⋙ q = p)
    (hτ : τ ≤ B.topology) :
    letI : p.IsFibered := hp.isFibered
    letI : q.IsFibered := hq.isFibered
    letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
      (τ.over (B.obj hS))).1
    (SheafOfModules.pushforward.{t}
      (ringStructureSheafCoreHom B S hS p q F τ hp hq hcomp hτ)).IsRightAdjoint
```

**`AlgebraicGeometry.Stack.lowerShriekModulesForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/ModuleLowerShriek.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/ModuleLowerShriek.lean#L129). The attribute's comment: “f_! on sheaves of modules agrees with f_! on abelian sheaves”.

> **Stacks 06X2, comparison with abelian sheaves.** The lower shriek `f_!` of sheaves of
> modules along a 1-morphism of categories fibred in groupoids agrees, on underlying abelian
> sheaves, with the lower shriek of abelian sheaves of Stacks 06X1.

```lean
noncomputable def lowerShriekModulesForgetIso
    [EssentiallySmall.{t} 𝒳] [EssentiallySmall.{t} 𝒴] [UnivLE.{u, t}]
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) (hcomp : F ⋙ q = p)
    (hτ : τ ≤ B.topology) :
    letI : p.IsFibered := hp.isFibered
    letI : q.IsFibered := hq.isFibered
    letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
      (τ.over (B.obj hS))).1
    letI := isRightAdjoint_sheafOfModules_pushforward.{u, v₁, v₂, w₁, w₂, t}
      B S hS p q F τ hp hq hcomp hτ
    letI := fun G : 𝒳ᵒᵖ ⥤ AddCommGrpCat.{t} ↦
      Functor.hasPointwiseLeftKanExtension_of_essentiallySmall_of_locallySmall.{t} F.op G
    letI := hasSheafify_associatedTopology_of_essentiallySmall.{u, v₂, w₂, t} B S hS q τ
    SheafOfModules.pullback.{t} (ringStructureSheafCoreHom B S hS p q F τ hp hq hcomp hτ) ⋙
        SheafOfModules.toSheaf.{t} (ringStructureSheafCore B S hS q hq τ hτ) ≅
      SheafOfModules.toSheaf.{t} (ringStructureSheafCore B S hS p hp τ hτ) ⋙
        Functor.sheafPullbackConstruction.sheafPullback F AddCommGrpCat.{t}
          (associatedTopology B S hS p τ) (associatedTopology B S hS q τ)
```

**`AlgebraicGeometry.Stack.exactFunctor_sheafOfModules_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/ModuleLowerShriek.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/ModuleLowerShriek.lean#L157). The attribute's comment: “part (1)”.

> **Stacks 06X2, part (1).** For a faithful 1-morphism of categories fibred in groupoids
> whose source has equalizers, the lower shriek `f_!` of sheaves of modules is exact.

```lean
theorem exactFunctor_sheafOfModules_pullback
    [EssentiallySmall.{t} 𝒳] [EssentiallySmall.{t} 𝒴] [UnivLE.{u, t}]
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) (hcomp : F ⋙ q = p)
    (hτ : τ ≤ B.topology) [F.Faithful] [HasEqualizers 𝒳] :
    letI : p.IsFibered := hp.isFibered
    letI : q.IsFibered := hq.isFibered
    letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
      (τ.over (B.obj hS))).1
    letI := isRightAdjoint_sheafOfModules_pushforward.{u, v₁, v₂, w₁, w₂, t}
      B S hS p q F τ hp hq hcomp hτ
    exactFunctor _ _
      (SheafOfModules.pullback.{t}
        (ringStructureSheafCoreHom B S hS p q F τ hp hq hcomp hτ))
```

**`AlgebraicGeometry.Stack.injective_sheafOfModules_pushforward_obj_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/ModuleLowerShriek.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/ModuleLowerShriek.lean#L178). The attribute's comment: “part (2)”.

> **Stacks 06X2, part (2).** For a faithful 1-morphism of categories fibred in groupoids
> whose source has equalizers, the inverse image of an injective sheaf of modules is an injective
> sheaf of modules.

```lean
theorem injective_sheafOfModules_pushforward_obj_of_injective
    [EssentiallySmall.{t} 𝒳] [EssentiallySmall.{t} 𝒴] [UnivLE.{u, t}]
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) (hcomp : F ⋙ q = p)
    (hτ : τ ≤ B.topology) [F.Faithful] [HasEqualizers 𝒳]
    (I : SheafOfModules.{t} (ringStructureSheafCore B S hS q hq τ hτ)) [Injective I] :
    letI : p.IsFibered := hp.isFibered
    letI : q.IsFibered := hq.isFibered
    letI := ((hq.isFibredOneMorphism hcomp).isContinuous_and_isCocontinuous_inheritedTopology
      (τ.over (B.obj hS))).1
    Injective ((SheafOfModules.pushforward.{t}
      (ringStructureSheafCoreHom B S hS p q F τ hp hq hcomp hτ)).obj I)
```

Declarations registered for the tag:

- [`SheafOfModules.instIsRightAdjointPushforward`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.instIsRightAdjointPushforward#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Injectives.lean#L306) (StacksFrontier): “the adjunction f_! ⊣ f^* on modules”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.17, Tag 06WW](https://stacks.math.columbia.edu/tag/06WW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
