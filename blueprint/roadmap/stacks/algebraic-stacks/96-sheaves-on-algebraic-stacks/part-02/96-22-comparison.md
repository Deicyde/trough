---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.injective_restrictionAbSheafFunctor_obj, AlgebraicGeometry.Space.isKInjective_restrictionAbSheafFunctor_obj, AlgebraicGeometry.Space.injective_restrictionAbSheafFunctor_obj_univ, AlgebraicGeometry.Space.isKInjective_restrictionAbSheafFunctor_obj_univ, AlgebraicGeometry.Space.restriction_modules_not_preserves_injectives, AlgebraicGeometry.Space.restrictedTotalDerivedDirectImageIsoClauses, AlgebraicGeometry.Stack.inducedSquareSpacesHom, AlgebraicGeometry.Stack.RepresentableBaseChangeSquare.exists_isAlgebraicSpace_apex
statement: formalized
proof: formalized
---

# 96.22 Comparison

Section 96.22 of the Stacks Project, [Tag 073L](https://stacks.math.columbia.edu/tag/073L). 3 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 075L, a lemma

[Tag 075L](https://stacks.math.columbia.edu/tag/075L) in the Stacks Project.

**`AlgebraicGeometry.Space.injective_restrictionAbSheafFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpaceInjectives.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpaceInjectives.lean#L208). The attribute's comment: “part (1), injective abelian sheaves”.

> **Stacks Project, Tag 075L, part (1).** Let `𝒳` be a category fibred in groupoids over the
> big fppf site of `S` representable by the algebraic space `F`. If `I` is injective in
> `Ab(𝒳_étale)`, then `I|_{F_étale}` is injective in `Ab(F_étale)`.

```lean
theorem injective_restrictionAbSheafFunctor_obj (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p)
    [HasSheafify (BigFppfOver.associatedTopology B S hS p .etale) Ab.{t}]
    [HasSheafify (SmallEtale.topology B S hS F) Ab.{t}]
    [∀ G : (SmallEtale B S hS F)ᵒᵖ ⥤ Ab.{t},
      (restrictionFunctor B S hS F p e).op.HasPointwiseLeftKanExtension G]
    (I : Sheaf (BigFppfOver.associatedTopology B S hS p .etale) Ab.{t}) [Injective I] :
    Injective ((restrictionAbSheafFunctor B S hS F p hp e).obj I)
```

**`AlgebraicGeometry.Space.isKInjective_restrictionAbSheafFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpaceInjectives.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpaceInjectives.lean#L226). The attribute's comment: “part (2), K-injective complexes”.

> **Stacks Project, Tag 075L, part (2).** Let `𝒳` be a category fibred in groupoids over the
> big fppf site of `S` representable by the algebraic space `F`. If `I` is a K-injective complex
> in `Ab(𝒳_étale)`, then `I|_{F_étale}` is a K-injective complex in `Ab(F_étale)`.

```lean
theorem isKInjective_restrictionAbSheafFunctor_obj (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p)
    [HasSheafify (BigFppfOver.associatedTopology B S hS p .etale) Ab.{t}]
    [HasSheafify (SmallEtale.topology B S hS F) Ab.{t}]
    [∀ G : (SmallEtale B S hS F)ᵒᵖ ⥤ Ab.{t},
      (restrictionFunctor B S hS F p e).op.HasPointwiseLeftKanExtension G]
    (I : CochainComplex
      (Sheaf (BigFppfOver.associatedTopology B S hS p .etale) Ab.{t}) ℤ) [I.IsKInjective] :
    CochainComplex.IsKInjective
      (((restrictionAbSheafFunctor B S hS F p hp e).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj I)
```

**`AlgebraicGeometry.Space.injective_restrictionAbSheafFunctor_obj_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpaceModules.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpaceModules.lean#L121). The attribute's comment: “part (1), injective abelian sheaves, with no size hypothesis”.

> **Stacks 075L, part (1), with no size hypothesis.** For abelian sheaves with values in the
> universe of the schemes, the sheafifications and Kan extensions that
> `AlgebraicGeometry.Space.injective_restrictionAbSheafFunctor_obj` asks for exist: `𝒳` is
> essentially small, being equivalent to the scheme charts of `F`, and so is the small étale site
> of `F`. So the restriction of an injective abelian sheaf on `𝒳_étale` to `F_étale` is injective,
> with no hypothesis beyond the source's.

```lean
theorem injective_restrictionAbSheafFunctor_obj_univ (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p)
    (I : Sheaf (BigFppfOver.associatedTopology B S hS p .etale) Ab.{u}) [Injective I] :
    Injective ((restrictionAbSheafFunctor.{u} B S hS F p hp e).obj I)
```

**`AlgebraicGeometry.Space.isKInjective_restrictionAbSheafFunctor_obj_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpaceModules.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpaceModules.lean#L144). The attribute's comment: “part (2), K-injective complexes, with no size hypothesis”.

> **Stacks 075L, part (2), with no size hypothesis.** The degreewise restriction of a
> K-injective complex of abelian sheaves on `𝒳_étale` to `F_étale` is K-injective, for sheaves with
> values in the universe of the schemes. The abelian structures on the two categories of sheaves
> are the ones given by sheafification, which exists on both sites because both are essentially
> small (`AlgebraicGeometry.Space.essentiallySmall_of_equivalenceOver` for `𝒳`); the statement
> introduces it from the presentation `e`.

```lean
theorem isKInjective_restrictionAbSheafFunctor_obj_univ (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    letI := essentiallySmall_of_equivalenceOver B S hS F p e
    letI : HasSheafify (BigFppfOver.associatedTopology B S hS p .etale) Ab.{u} :=
      GrothendieckTopology.hasSheafify_addCommGrpCat_of_essentiallySmall.{u} _
    letI : HasSheafify (SmallEtale.topology B S hS F) Ab.{u} :=
      GrothendieckTopology.hasSheafify_addCommGrpCat_of_essentiallySmall.{u} _
    ∀ (I : CochainComplex
      (Sheaf (BigFppfOver.associatedTopology B S hS p .etale) Ab.{u}) ℤ) [I.IsKInjective],
    CochainComplex.IsKInjective
      (((restrictionAbSheafFunctor.{u} B S hS F p hp e).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj I)
```

**`AlgebraicGeometry.Space.restriction_modules_not_preserves_injectives`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpaceModules.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpaceModules.lean#L369). The attribute's comment: “the final sentence: the same does not hold for modules, for neither part”.

> **Stacks 075L, the failure for modules.** Restriction of abelian sheaves from an algebraic
> stack representable by an algebraic space `F` to `F_étale` preserves injectives and K-injective
> complexes (parts (1) and (2), `AlgebraicGeometry.Space.injective_restrictionAbSheafFunctor_obj`
> and `AlgebraicGeometry.Space.isKInjective_restrictionAbSheafFunctor_obj`), but **the same does
> not hold for modules**: on every big fppf site, the algebraic stack `Spec ℤ`, represented by the
> algebraic space `h_{Spec ℤ}`, carries an injective `𝒪`-module `I` with `I|_{F_étale}` not an
> injective `𝒪_F`-module, and a K-injective complex of `𝒪`-modules whose restriction is not
> K-injective.

```lean
theorem restriction_modules_not_preserves_injectives (B : BigFppfSite.{u}) :
    (∃ I : SheafOfModules.{u} (specIntEtaleRingSheaf B),
      Injective I ∧ ¬ Injective ((specIntModuleRestriction B).obj I)) ∧
    ∃ I : CochainComplex (SheafOfModules.{u} (specIntEtaleRingSheaf B)) ℤ,
      I.IsKInjective ∧ ¬ CochainComplex.IsKInjective
        (((specIntModuleRestriction B).mapHomologicalComplex (ComplexShape.up ℤ)).obj I)
```

## Tag 075N, a lemma

[Tag 075N](https://stacks.math.columbia.edu/tag/075N) in the Stacks Project.

**`AlgebraicGeometry.Space.restrictedTotalDerivedDirectImageIsoClauses`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RestrictionTotalDerivedDirectImage.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RestrictionTotalDerivedDirectImage.lean#L370). The attribute's comment: “Both clauses, with the four derived direct images constructed: (1) for abelian sheaves (Rf\_*F)|\_\{G\_etale} = Rf\_\{small,*}(F|\_\{F\_etale}) in D(G\_etale), (2) the same identity in D(O\_G) for sheaves of modules. Rf\_* and Rf\_\{small,*} are the total right derived functors of degreewise direct image, which exist by K-injective resolutions (Tag 079P) on the four essentially small sites; the inputs are S, the 1-morphism and the two presentations.”.

> **Stacks 075N.** Let `S` be a scheme in a big fppf site, let `f : 𝒳 ⥤ 𝒴` be a 1-morphism of
> categories fibred in groupoids over `(Sch/S)_{fppf}` with `𝒳` presented by an algebraic space `F`
> and `𝒴` by an algebraic space `G`, and let `f : F ⟶ G` be the induced morphism of algebraic
> spaces. Then
>
> 1. for an abelian sheaf `ℱ` on `𝒳_étale`, `(Rf_*ℱ)|_{G_étale} = Rf_{small,*}(ℱ|_{F_étale})` in
>    `D(G_étale)`;
> 2. for a complex `ℱ` of `𝒪_𝒳`-modules, the same identity in `D(𝒪_G)`.
>
> Here `Rf_*` and `Rf_{small,*}` are the total right derived direct images
> `derivedAbelianDirectImageFibred`, `derivedAbelianDirectImageSpace`, `derivedDirectImageFibred`
> and `derivedDirectImageSpace`, which exist because the four sites are essentially small — `𝒳`
> and `𝒴` by their presentations — so that K-injective resolutions exist (Stacks 079P). The
> restrictions `(-)|_{F_étale}`, `(-)|_{G_étale}` are exact and appear underived, as in the source.
> Each component is the canonical comparison of the two derived composites around the square of
> Stacks 073N, shown invertible.

```lean
def restrictedTotalDerivedDirectImageIsoClauses
    [HasDerivedCategory.{dF} (Sheaf (smallEtaleRingedTopos B S hS ⟨F, hF⟩).J AddCommGrpCat.{u})]
    [HasDerivedCategory.{dG} (Sheaf (smallEtaleRingedTopos B S hS ⟨G, hG⟩).J AddCommGrpCat.{u})]
    [HasDerivedCategory.{mF} (smallEtaleRingedTopos B S hS ⟨F, hF⟩).Modules]
    [HasDerivedCategory.{mG} (smallEtaleRingedTopos B S hS ⟨G, hG⟩).Modules]
    [letI : EssentiallySmall.{u} 𝒳 := essentiallySmall_of_equivalenceOver B S hS F p eF;
      letI : EssentiallySmall.{u} 𝒴 := essentiallySmall_of_equivalenceOver B S hS G q eG;
      HasDerivedCategory.{dX}
        (Sheaf (FibredSite.associatedRingedTopos B S hS p hp .etale).J AddCommGrpCat.{u})]
    [letI : EssentiallySmall.{u} 𝒳 := essentiallySmall_of_equivalenceOver B S hS F p eF;
      letI : EssentiallySmall.{u} 𝒴 := essentiallySmall_of_equivalenceOver B S hS G q eG;
      HasDerivedCategory.{dY}
        (Sheaf (FibredSite.associatedRingedTopos B S hS q hq .etale).J AddCommGrpCat.{u})]
    [letI : EssentiallySmall.{u} 𝒳 := essentiallySmall_of_equivalenceOver B S hS F p eF;
      letI : EssentiallySmall.{u} 𝒴 := essentiallySmall_of_equivalenceOver B S hS G q eG;
      HasDerivedCategory.{mX} (FibredSite.associatedRingedTopos B S hS p hp .etale).Modules]
    [letI : EssentiallySmall.{u} 𝒳 := essentiallySmall_of_equivalenceOver B S hS F p eF;
      letI : EssentiallySmall.{u} 𝒴 := essentiallySmall_of_equivalenceOver B S hS G q eG;
      HasDerivedCategory.{mY} (FibredSite.associatedRingedTopos B S hS q hq .etale).Modules] :
    letI : EssentiallySmall.{u} 𝒳 := essentiallySmall_of_equivalenceOver B S hS F p eF
    letI : EssentiallySmall.{u} 𝒴 := essentiallySmall_of_equivalenceOver B S hS G q eG
    (derivedAbelianDirectImageFibred B S hS p q hp hq fStack hfStack ⋙
        (abelianRestrictionFunctor B S hS G q hq hG eG).mapDerivedCategory ≅
      (abelianRestrictionFunctor B S hS F p hp hF eF).mapDerivedCategory ⋙
        derivedAbelianDirectImageSpace B S hS F G p q hF hG eF eG fStack hfStack) ×
      (derivedDirectImageFibred B S hS p q hp hq fStack hfStack ⋙
          derivedModuleRestriction B S hS q hq G hG eG ≅
        derivedModuleRestriction B S hS p hp F hF eF ⋙
          derivedDirectImageSpace B S hS F G p q hF hG eF eG fStack hfStack)
```

## Tag 075P, a lemma

[Tag 075P](https://stacks.math.columbia.edu/tag/075P) in the Stacks Project.

**`AlgebraicGeometry.Stack.inducedSquareSpacesHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableBaseChangeSquare.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableBaseChangeSquare.lean#L140). The attribute's comment: “the induced morphism of algebraic spaces f' : F' ⟶ G' named in the conclusion, through chosen equivalences of the apex with F' and of Y' with G'. The displayed base change identity of this tag is NOT proved”.

> **The morphism of algebraic spaces `f' : F' ⟶ G'` of Stacks 075P.**  For a 2-fibre product
> square over the cospan `(g, f)`, with the apex represented by an algebraic space `F'` and the
> base `𝒴'` of `g` represented by an algebraic space `G'`, the left-hand leg `f'` of the square
> induces a morphism `F' ⟶ G'` of algebraic spaces: an element of `F'` over `U` is an object of
> the apex over `U`, whose image under `f'` is an object of `𝒴'` over `U`, hence an element of
> `G'` over `U`.
>
> This is the construction of **Stacks 0GQA**, `AlgebraicGeometry.Space.inducedSpacesHom`, read
> at the left-hand leg of the square.  Only the two chosen equivalences and the verticality of
> the leg over the site enter; representability of the apex, which **Stacks 0300** supplies, is
> what makes such an equivalence available in the first place.
>
> The displayed identity of **Stacks 075P**, which is the direct image along this morphism of a
> restricted derived direct image, is not proved; see the implementation notes of this module.

```lean
noncomputable def inducedSquareSpacesHom
    {𝒳 𝒴 𝒴' : CatFiberedInGroupoids.{u, max u v, u + 1, max (max (u + 1) w) v}
      (BigFppfOver B S hS)}
    {f : 𝒳 ⟶ 𝒴} {g : 𝒴' ⟶ 𝒴} (P : Bicategory.TwoCommSq g f)
    {F' G' : AlgebraicSpaces B S hS}
    (eF' : StacksRepresentableCFG.EquivalenceOver P.pt.val.p
      (presheafOfCategories (F'.1 ⋙ typeToCat)).p)
    (eG' : StacksRepresentableCFG.EquivalenceOver 𝒴'.val.p
      (presheafOfCategories (G'.1 ⋙ typeToCat)).p) :
    F' ⟶ G'
```

**`AlgebraicGeometry.Stack.RepresentableBaseChangeSquare.exists_isAlgebraicSpace_apex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableBaseChangeSquareDerived.lean, line 305](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableBaseChangeSquareDerived.lean#L305). The attribute's comment: “The first assertion: the apex X' of the 2-fibre product square is representable by an algebraic space F', given that f is representable by algebraic spaces and that Y' is representable by an algebraic space.”.

> **The apex of the square is representable by an algebraic space**, when `f` is
> representable by algebraic spaces and `𝒴'` is representable by an algebraic space. This is
> Stacks 0300, `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_twoFibreProduct`, for the
> 2-fibre product with the factors in the order of the source's square, read through the exchange
> of the two factors `CategoryTheory.TwoFibreProductOver.swapEquivalenceOver`.

```lean
theorem exists_isAlgebraicSpace_apex (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (h𝒴' : IsRepresentableByAlgebraicSpace B S hS 𝒴'.val) :
    ∃ F' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u, IsAlgebraicSpace B S hS F' ∧
      Nonempty (StacksRepresentableCFG.EquivalenceOver (apexP B S hS f g)
        (presheafOfCategories (F' ⋙ typeToCat)).p)
```

**`AlgebraicGeometry.Stack.RepresentableBaseChangeSquare.restrictedDerivedBaseChangeIsoClauses`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableBaseChangeSquareDerived.lean, line 1125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableBaseChangeSquareDerived.lean#L1125). The attribute's comment: “The displayed identity, both clauses, as isomorphisms of functors on the unbounded derived categories: (1) g^\{-1}(Rf\_*F)|\_\{G'\_etale} = Rf'\_\{small,*}((g')^\{-1}F|\_\{F'\_etale}) for F in D(X\_etale), (2) the same identity for F in D(O\_X), for any presentations of Y' and of the apex X' by algebraic spaces G' and F'.”.

> **Stacks 075P.** Let `S` be a scheme and let
>
> ```
> 𝒴' ×_𝒴 𝒳 --g'--> 𝒳
>     |            |
>     f'           f
>     v            v
>     𝒴' ---g--->  𝒴
> ```
>
> be the 2-fibre product square of algebraic stacks over `S`. If `𝒴'` is represented by an
> algebraic space `G'` and the apex by an algebraic space `F'` — which is the case as soon as `f`
> is representable by algebraic spaces, by `exists_isAlgebraicSpace_apex` — and `f' : F' ⟶ G'` is
> the induced morphism of algebraic spaces, then
>
> `g⁻¹(Rf_*ℱ)|_{G'_étale} = Rf'_{small,*}((g')⁻¹ℱ|_{F'_étale})`
>
> 1. for `ℱ` in `D(𝒳_étale)`, in particular for an abelian sheaf on `𝒳_étale`, and
> 2. for `ℱ` in `D(𝒪_𝒳)`, in particular for a sheaf of `𝒪_𝒳`-modules,
>
> as isomorphisms of functors. The derived direct images are the total right derived functors of
> Stacks 075N, `AlgebraicGeometry.Space.derivedAbelianDirectImageFibred`,
> `AlgebraicGeometry.Space.derivedAbelianDirectImageSpace`,
> `AlgebraicGeometry.Space.derivedDirectImageFibred` and
> `AlgebraicGeometry.Space.derivedDirectImageSpace`.

```lean
def restrictedDerivedBaseChangeIsoClauses :
    (Space.derivedAbelianDirectImageFibred B S hS 𝒳.val.val.p 𝒴.val.val.p
        (𝒳.val.isFiberedInGroupoids) (𝒴.val.isFiberedInGroupoids) f.hom.hom.toFunctor
        ((𝒴.val.isFiberedInGroupoids).isFibredOneMorphism f.hom.hom.w) ⋙
        (inverseImageAb B S hS g).mapDerivedCategory ⋙
          (restrictionG'Ab B S hS G' hG' eG').mapDerivedCategory ≅
      (fstInverseImageAb B S hS f g).mapDerivedCategory ⋙
        (restrictionF'Ab B S hS f g F' hF' eF').mapDerivedCategory ⋙
          Space.derivedAbelianDirectImageSpace B S hS F' G' (apexP B S hS f g) 𝒴'.val.val.p hF'
            hG' eF' eG' (TwoFibreProductOver.snd _ _ _ f.hom.hom.toFunctor g.hom.hom.toFunctor)
            (snd_isFibredOneMorphism B S hS f g)) ×
    (Space.derivedDirectImageFibred B S hS 𝒳.val.val.p 𝒴.val.val.p
        (𝒳.val.isFiberedInGroupoids) (𝒴.val.isFiberedInGroupoids) f.hom.hom.toFunctor
        ((𝒴.val.isFiberedInGroupoids).isFibredOneMorphism f.hom.hom.w) ⋙
        (inverseImageMod B S hS g).mapDerivedCategory ⋙
          (Space.projectionRingedToposHom B S hS G' 𝒴'.val.val.p (𝒴'.val.isFiberedInGroupoids)
            hG' eG').derivedPushforwardOfExact ≅
      (fstInverseImageMod B S hS f g).mapDerivedCategory ⋙
        (Space.projectionRingedToposHom B S hS F' (apexP B S hS f g)
          (apexP_isFiberedInGroupoids B S hS f g) hF' eF').derivedPushforwardOfExact ⋙
          Space.derivedDirectImageSpace B S hS F' G' (apexP B S hS f g) 𝒴'.val.val.p hF'
            hG' eF' eG' (TwoFibreProductOver.snd _ _ _ f.hom.hom.toFunctor g.hom.hom.toFunctor)
            (snd_isFibredOneMorphism B S hS f g))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_of_isTwoFibreProduct`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeRepresentableBySpace.lean#L172), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableBaseChangeSquare.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableBaseChangeSquare.lean#L111) (StacksFrontier): “the first assertion of the conclusion: the apex X' of the 2-fibre product square is representable by an algebraic space F', given that f is representable by algebraic spaces and that Y' is representable by an algebraic space. This is Tag 0300, at hypotheses weaker than the source's. The displayed base change identity of this tag is NOT proved; see the implementation notes of StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableBaseChangeSquare.lean”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.22, Tag 073L](https://stacks.math.columbia.edu/tag/073L)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
