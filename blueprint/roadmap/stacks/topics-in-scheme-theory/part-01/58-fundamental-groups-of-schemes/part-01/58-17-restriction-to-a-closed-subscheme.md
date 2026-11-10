---
declaration: section
origin: cited
lean: Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_of_completionFullyFaithfulOnFiniteLocallyFree, Stacks.FundamentalGroup.finiteEtaleBaseChange_isEquivalence_of_completionEquivalence, Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_of_sectionsExtendNearSubscheme, Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_of_completionFullyFaithfulComplete, Stacks.FundamentalGroup.isEquivalence_restrictionFunctor_of_fullyFaithful_of_essentialImage, Stacks.FundamentalGroup.restriction_isEquivalence_of_completionEquivalence, Stacks.FundamentalGroup.faithful_finiteEtaleRestriction_of_components_meet, Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_of_sectionsComplete_of_or
statement: formalized
proof: formalized
---

# 58.17 Restriction to a closed subscheme

Section 58.17 of the Stacks Project, [Tag 0EJW](https://stacks.math.columbia.edu/tag/0EJW). 7 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EL8, a lemma

[Tag 0EL8](https://stacks.math.columbia.edu/tag/0EL8) in the Stacks Project.

**`Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_of_completionFullyFaithfulOnFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionToClosedSubscheme.lean, line 1052](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionToClosedSubscheme.lean#L1052). The attribute's comment: “proved from full faithfulness of completion on the finite locally free coherent modules alone”.

> Let `X` be a Noetherian scheme and `Y ⊆ X` a closed subscheme with ideal sheaf `I`. If the
> completion functor `Coh(𝒪_X) ⟶ Coh(X, I)` is fully faithful on the full subcategory of finite
> locally free objects, then the restriction functor `FÉt_X ⟶ FÉt_Y` is fully faithful.

```lean
public theorem fullyFaithful_finiteEtaleBaseChange_of_completionFullyFaithfulOnFiniteLocallyFree
    {X Y : Scheme.{u}} (i : Y ⟶ X) [IsNoetherian X] [IsClosedImmersion i]
    (hcompletion : Stacks.Algebraization.CompletionFullyFaithfulOnFiniteLocallyFree X i.ker) :
    Nonempty (finiteEtaleBaseChange i).FullyFaithful
```

## Tag 0EL9, a lemma

[Tag 0EL9](https://stacks.math.columbia.edu/tag/0EL9) in the Stacks Project.

**`Stacks.FundamentalGroup.finiteEtaleBaseChange_isEquivalence_of_completionEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionEquivalenceOfCompletion.lean, line 2994](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionEquivalenceOfCompletion.lean#L2994). The attribute's comment: “completion an equivalence on finite locally free objects implies restriction FEt_X to FEt_Y an equivalence”.

> **[Stacks, Tag 0EL9].** Let `X` be a Noetherian scheme and `Y ⊆ X` a closed subscheme with
> ideal sheaf `I`. If the completion functor `Coh(𝒪_X) ⥤ Coh(X, I)`, `ℱ ↦ ℱ^∧`, is an equivalence
> on the full subcategories of finite locally free objects, then the restriction functor
> `FÉt_X ⥤ FÉt_Y`, `U ↦ U ×_X Y`, is an equivalence.
>
> The closed subscheme is given by a closed immersion `i : Y ⟶ X` with ideal sheaf `I = ker i`.
> Restriction factors as restriction to the closed subscheme cut out by `I` followed by base change
> along the isomorphism from `Y` onto it, and the second is an equivalence because an isomorphism is
> a thickening ([Stacks, Tag 0BQB]); the first is
> `Stacks.FundamentalGroup.finiteEtaleBaseChange_isEquivalence_of_completion`.

```lean
public theorem finiteEtaleBaseChange_isEquivalence_of_completionEquivalence
    {X Y : Scheme.{u}} (i : Y ⟶ X) [IsNoetherian X] [IsClosedImmersion i]
    [(finiteLocallyFreeCompletion X i.ker).IsEquivalence] :
    (AlgebraicGeometry.finiteEtaleBaseChange i).IsEquivalence
```

## Tag 0ELA, a lemma

[Tag 0ELA](https://stacks.math.columbia.edu/tag/0ELA) in the Stacks Project.

**`Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_of_sectionsExtendNearSubscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionFromNeighborhoods.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionFromNeighborhoods.lean#L366). The attribute's comment: “granted SectionsExtendNearSubscheme: the shrinking form of Tag 0EL8”.

> **[Stacks, Tag 0ELA], granted the section-extension input.** Let `X` be a scheme, let
> `Y ⊆ X` be the closed subscheme cut out by the ideal sheaf `Y`, and let `𝒱` be the open
> subschemes of `X` containing it, ordered by reverse inclusion. If sections of a finite étale
> cover of a neighbourhood extend to a smaller neighbourhood and are determined there after
> further shrinking, then the restriction functor `colim_𝒱 FÉt_V ⟶ FÉt_Y` is fully faithful.
>
> This is the first paragraph of the source's proof, which is the only part of it that is about
> finite étale covers: the category of finite étale coverings has an internal hom
> ([Stacks, Tag 0BL7]), and a section of the internal hom `Hom_V(A, B)` over a base is exactly a
> morphism `A ⟶ B` after that base change, so a morphism between the restrictions to the closed
> subscheme is a section of the internal hom over the closed subscheme and full faithfulness over
> the colimit is the extension property for sections of one finite étale cover.
>
> **What is granted and what is not.** The hypothesis of the tag — full faithfulness of the
> completion functor `colim_𝒱 Coh(𝒪_V) ⟶ Coh(X, I)` on the finite locally free objects — is
> **not** used here at all: the section-extension property
> `Stacks.FundamentalGroup.SectionsExtendNearSubscheme` is assumed in its place. That property is
> the shrinking form of the conclusion of [Stacks, Tag 0EL8], and deducing it from the completion
> hypothesis is the rest of the source's proof: lift the section over the closed subscheme to the
> infinitesimal neighbourhoods ([Stacks, Tag 0BQB]), algebraize the resulting compatible system of
> module maps out of the finite locally free module `f _* 𝒪_U` over some smaller neighbourhood by
> fullness of completion, and shrink once more to make the algebraized map multiplicative by
> faithfulness of completion. That half is carried in this library only in its non-shrinking form,
> on the nose at a single scheme, as
> `Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_of_completionFullyFaithful`; the
> shrinking form would need the restriction of a direct image algebra to an open subscheme and the
> comparison of the infinitesimal neighbourhoods of the closed subscheme taken inside `X` and
> inside a neighbourhood, neither of which has a carrier here.
>
> It is **not** enough to assume the pointwise analogue of the hypothesis at each individual
> neighbourhood, which would make the statement a formal consequence of Tag 0EL8 applied one
> neighbourhood at a time. The quantifiers over smaller neighbourhoods in both
> `SectionsExtendNearSubscheme` and `FiniteEtaleColimitFullyFaithful` are the content.

```lean
theorem finiteEtaleColimitFullyFaithful_of_sectionsExtendNearSubscheme
    (h : SectionsExtendNearSubscheme X Y) : FiniteEtaleColimitFullyFaithful X Y
```

**`Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_of_completionFullyFaithfulComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SectionsExtendFromCompletion.lean, line 632](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SectionsExtendFromCompletion.lean#L632). The attribute's comment: “proved from full faithfulness of completion on the finite locally free objects of the neighbourhood colimit, the tag's own hypothesis”.

> **[Stacks, Tag 0ELA].** Let `X` be a Noetherian scheme and let `Y ⊆ X` be a closed subscheme
> with ideal sheaf `I`. Let `𝒱` be the set of open subschemes `V ⊆ X` containing `Y`, ordered by
> reverse inclusion. Assume the completion functor `colim_𝒱 Coh(𝒪_V) ⟶ Coh(X, I)`, `ℱ ↦ ℱ^∧`, is
> fully faithful on the full subcategory of finite locally free objects. Then the restriction
> functor `colim_𝒱 FÉt_V ⟶ FÉt_Y` is fully faithful.
>
> The hypothesis is condition (4) of [Stacks, Tag 0EK2],
> `Stacks.Algebraization.NeighbourhoodCompletion.CompletionFullyFaithfulComplete`, at the closed
> immersion of `Y`; the conclusion is `Stacks.FundamentalGroup.FiniteEtaleColimitFullyFaithful`,
> full faithfulness spelled through the directed-colimit description of the hom sets of
> `colim_𝒱 FÉt_V`. The proof is the source's: the internal hom reduces the statement to the
> extension of sections of one finite étale cover
> (`finiteEtaleColimitFullyFaithful_of_sectionsExtendNearSubscheme`), and that extension is
> `sectionsExtendNearSubscheme_of_completionFullyFaithfulComplete`.

```lean
theorem finiteEtaleColimitFullyFaithful_of_completionFullyFaithfulComplete [IsNoetherian X]
    (h : NeighbourhoodCompletion.CompletionFullyFaithfulComplete Y.subschemeι) :
    FiniteEtaleColimitFullyFaithful X Y
```

## Tag 0EK1, a lemma

[Tag 0EK1](https://stacks.math.columbia.edu/tag/0EK1) in the Stacks Project.

**`Stacks.FundamentalGroup.isEquivalence_restrictionFunctor_of_fullyFaithful_of_essentialImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionColimitEquivalence.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionColimitEquivalence.lean#L288). The attribute's comment: “granted Stacks 0ELA for full faithfulness and the essential image of restriction”.

> **[Stacks, Tag 0EK1].** Let `X` be a Noetherian scheme, `Y ⊆ X` a closed subscheme with ideal
> sheaf `I`, and `𝒱` the open subschemes of `X` containing `Y`, ordered by reverse inclusion. If the
> completion functor `colim_𝒱 Coh(𝒪_V) ⟶ Coh(X, I)`, `ℱ ↦ ℱ^∧`, is an equivalence of the full
> subcategories of finite locally free objects, then the restriction functor
> `colim_𝒱 FÉt_V ⟶ FÉt_Y` is an equivalence.
>
> The hypothesis is carried through the two consequences the source draws from it, because it
> cannot be stated here: the finite locally free objects of `Coh(X, I)` and the comparison of
> `Coh(X, I)` with `Coh(V, I|_V)` for a neighbourhood `V` are both absent from this library. The
> first consequence, `h0ELA`, is full faithfulness of the restriction functor, which the source
> obtains from the fully faithful half of the hypothesis by [Stacks, Tag 0ELA]. The second,
> `hessImage`, is that every finite étale cover of `Y` is the restriction of a finite étale cover of
> some neighbourhood; the source obtains it by algebraizing the tower `π_{n, *}𝒪_{U_n}` of pushed
> forward structure sheaves of the covers of the infinitesimal neighbourhoods, which is a finite
> locally free object of `Coh(X, I)`, transporting the algebra structure along the equivalence, and
> taking the relative spectrum, which is étale near `Y` by More on Morphisms, Tag 0A43. What is
> proved here is that the second consequence gives essential surjectivity of the functor out of the
> colimit.

```lean
public theorem isEquivalence_restrictionFunctor_of_fullyFaithful_of_essentialImage
    {X : Scheme.{u}} [IsNoetherian X] (Y : X.IdealSheafData)
    (P : FiniteEtaleColimitPresentation X Y) [HasColimit P.diagram]
    (h0ELA : Nonempty P.restrictionFunctor.FullyFaithful)
    (hessImage : ∀ A : FiniteEtaleOver Y.subscheme, ∃ (W : Neighborhood X Y)
      (U : FiniteEtaleOver (Neighborhood.open X Y W).toScheme),
      Nonempty ((finiteEtaleBaseChange (Neighborhood.toSchemeHom X Y W)).obj U ≅ A)) :
    P.restrictionFunctor.IsEquivalence
```

**`Stacks.FundamentalGroup.restriction_isEquivalence_of_completionEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionColimitEquivalenceOfCompletion.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionColimitEquivalenceOfCompletion.lean#L98). The attribute's comment: “the colimit functor is an equivalence: fully faithful, and every finite étale cover of Y extends to a neighbourhood”.

> **[Stacks, Tag 0EK1].** Let `X` be a Noetherian scheme, `Y ⊆ X` a closed subscheme with ideal
> sheaf `I`, and `𝒱` the open subschemes of `X` containing `Y`, ordered by reverse inclusion. If the
> completion functor `colim_𝒱 Coh(𝒪_V) ⟶ Coh(X, I)` defines an equivalence of the full
> subcategories of finite locally free objects, then the restriction functor
> `colim_𝒱 FÉt_V ⟶ FÉt_Y` is an equivalence: it is fully faithful in the directed-colimit sense of
> `FiniteEtaleColimitFullyFaithful`, and every finite étale cover of `Y` is the restriction of a
> finite étale cover of some `V ∈ 𝒱`.

```lean
public theorem restriction_isEquivalence_of_completionEquivalence [IsNoetherian X]
    (h : CompletionEquivalenceFiniteLocallyFree X Y) :
    FiniteEtaleColimitFullyFaithful X Y ∧
      ∀ A : FiniteEtaleOver Y.subscheme, ∃ (W : Neighborhood X Y)
        (U : FiniteEtaleOver (Neighborhood.open X Y W).toScheme),
        Nonempty ((finiteEtaleBaseChange (Neighborhood.toSchemeHom X Y W)).obj U ≅ A)
```

## Tag 0EJX, a lemma

[Tag 0EJX](https://stacks.math.columbia.edu/tag/0EJX) in the Stacks Project.

**`Stacks.FundamentalGroup.faithful_finiteEtaleRestriction_of_components_meet`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleMorphisms/Restriction.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleMorphisms/Restriction.lean#L102).

> **Stacks Project, Tag 0EJX.** Restriction of finite étale schemes to a closed subscheme
> meeting every connected component is faithful.

```lean
public lemma faithful_finiteEtaleRestriction_of_components_meet
    {X Y : Scheme.{u}} (f : Y ⟶ X) [IsClosedImmersion f]
    (h : ∀ c : ConnectedComponents X,
      ∃ y : Y, ConnectedComponents.mk (f.base y) = c) :
    (MorphismProperty.Over.pullback
      ((@IsFinite ⊓ @Etale) : MorphismProperty Scheme.{u}) ⊤ f).Faithful
```

## Tag 0EJZ, a lemma

[Tag 0EJZ](https://stacks.math.columbia.edu/tag/0EJZ) in the Stacks Project.

**`Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_of_sectionsComplete_of_or`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionSectionwiseComplete.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionSectionwiseComplete.lean#L80).

> **[Stacks, Tag 0EJZ].** Let `X` be a Noetherian scheme and `Y ⊆ X` a closed subscheme, with
> infinitesimal neighbourhoods `Y_n ⊆ X`. Assume one of the following holds:
>
> 1. `X` is quasi-affine and `Γ(X, 𝒪_X) → lim Γ(Y_n, 𝒪_{Y_n})` is an isomorphism, or
> 2. `X` has an ample invertible module `L` and `Γ(X, L^{⊗ m}) → lim Γ(Y_n, L^{⊗ m}|_{Y_n})` is an
>    isomorphism for all `m ≫ 0`, or
> 3. for every finite locally free `𝒪_X`-module `ℰ` the map `Γ(X, ℰ) → lim Γ(Y_n, ℰ|_{Y_n})` is an
>    isomorphism.
>
> Then the restriction functor `FÉt_X ⟶ FÉt_Y` is fully faithful.
>
> As in the source, cases (1) and (2) are reduced to case (3) by the implications `(1) ⇒ (2) ⇒ (3)`
> of [Stacks, Tag 0EKP], case (3) gives full faithfulness of completion on finite locally free
> modules by `(3) ⇒ (4)` of the same tag, and [Stacks, Tag 0EL8] concludes.

```lean
public theorem fullyFaithful_finiteEtaleBaseChange_of_sectionsComplete_of_or
    {X Y : Scheme.{u}} (i : Y ⟶ X) [IsNoetherian X] [IsClosedImmersion i]
    (h : SectionsCompleteQuasiAffine i ∨ SectionsCompleteAmplePowers i ∨
      SectionsCompleteFiniteLocallyFree i) :
    Nonempty (finiteEtaleBaseChange i).FullyFaithful
```

**`Stacks.FundamentalGroup.bijective_map_finiteEtaleBaseChange_of_sectionsComplete_of_or`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionSectionwiseComplete.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionSectionwiseComplete.lean#L105). The attribute's comment: “restated as bijectivity on hom sets”. References: SGA 2 X (2.5), “special case”.

> **[Stacks, Tag 0EJZ], restated as bijectivity on hom sets.** Under any one of the three
> conditions of
> `Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_of_sectionsComplete_of_or`,
> restriction of finite étale covers of `X` to the closed subscheme `Y` is bijective on every hom
> set.
>
> `CategoryTheory.Functor.FullyFaithful` carries the inverse map on hom sets as data, so full
> faithfulness is recorded as `Nonempty _.FullyFaithful`;
> `CategoryTheory.Functor.FullyFaithful.nonempty_iff_map_bijective` turns it into bijectivity on hom
> sets.

```lean
public theorem bijective_map_finiteEtaleBaseChange_of_sectionsComplete_of_or
    {X Y : Scheme.{u}} (i : Y ⟶ X) [IsNoetherian X] [IsClosedImmersion i]
    (h : SectionsCompleteQuasiAffine i ∨ SectionsCompleteAmplePowers i ∨
      SectionsCompleteFiniteLocallyFree i)
    (A B : FiniteEtaleOver X) :
    Function.Bijective (fun φ : A ⟶ B => (finiteEtaleBaseChange i).map φ)
```

## Tag 0EK0, a lemma

[Tag 0EK0](https://stacks.math.columbia.edu/tag/0EK0) in the Stacks Project.

**`Stacks.FundamentalGroup.fullyFaithful_restrictionFunctor_of_neighbourhoodSectionsComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionColimitEquivalence.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionColimitEquivalence.lean#L248). The attribute's comment: “granted Stacks 0EK2 (2)⇒(3), and Stacks 0EK2 (3)⇒(4) together with Stacks 0ELA”.

> **[Stacks, Tag 0EK0].** Let `X` be a Noetherian scheme, `Y ⊆ X` a closed subscheme with
> infinitesimal neighbourhoods `Y_n ⊆ X`, and `𝒱` the open subschemes of `X` containing `Y`,
> ordered by reverse inclusion. If one of
>
> 1. `X` is quasi-affine and `colim_𝒱 Γ(V, 𝒪_V) → lim Γ(Y_n, 𝒪_{Y_n})` is an isomorphism,
> 2. `X` has an ample invertible module `L` and
>    `colim_𝒱 Γ(V, L^{⊗ m}) → lim Γ(Y_n, L^{⊗ m}|_{Y_n})` is an isomorphism for all `m ≫ 0`,
> 3. `colim_{V' ≥ V} Γ(V', ℰ|_{V'}) → lim Γ(Y_n, ℰ|_{Y_n})` is an isomorphism for every `V ∈ 𝒱` and
>    every finite locally free `𝒪_V`-module `ℰ`,
>
> holds, then the restriction functor `colim_𝒱 FÉt_V ⟶ FÉt_Y` is fully faithful.
>
> The source's proof is to combine [Stacks, Tag 0ELA] with [Stacks, Tag 0EK2]. Of that chain this
> library carries the implication `(1) ⇒ (2)` of Tag 0EK2 and no more, so condition (1) is
> converted to condition (2) here by the library's proof of that implication and the remaining steps are the two
> hypotheses `h0EK2` and `h0ELA`; see
> `Stacks.FundamentalGroup.AmplePowersImpliesFiniteLocallyFree` and
> `Stacks.FundamentalGroup.FullyFaithfulRestrictionOfSectionsComplete`.

```lean
public theorem fullyFaithful_restrictionFunctor_of_neighbourhoodSectionsComplete
    {X : Scheme.{u}} [IsNoetherian X] (Y : X.IdealSheafData)
    (P : FiniteEtaleColimitPresentation X Y) [HasColimit P.diagram]
    (h : NeighbourhoodSectionsCompleteQuasiAffine Y ∨
      NeighbourhoodSectionsCompleteAmplePowers Y ∨
      NeighbourhoodSectionsCompleteFiniteLocallyFree Y)
    (h0EK2 : AmplePowersImpliesFiniteLocallyFree.{u})
    (h0ELA : FullyFaithfulRestrictionOfSectionsComplete.{u}) :
    Nonempty P.restrictionFunctor.FullyFaithful
```

**`Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_of_neighbourhoodSectionsComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionColimitFullyFaithful.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionColimitFullyFaithful.lean#L80). The attribute's comment: “all three cases, under the tag's own hypotheses; full faithfulness spelled through the directed-colimit description of the hom sets of colim_V FEt_V”.

> **[Stacks, Tag 0EK0].** Let `X` be a Noetherian scheme, `Y ⊆ X` a closed subscheme with
> infinitesimal neighbourhoods `Y_n ⊆ X`, and `𝒱` the open subschemes of `X` containing `Y`,
> ordered by reverse inclusion. Assume one of the following holds:
>
> 1. `X` is quasi-affine and `colim_𝒱 Γ(V, 𝒪_V) → lim Γ(Y_n, 𝒪_{Y_n})` is an isomorphism;
> 2. `X` has an ample invertible module `L` and
>    `colim_𝒱 Γ(V, L^{⊗ m}) → lim Γ(Y_n, L^{⊗ m}|_{Y_n})` is an isomorphism for all `m ≫ 0`;
> 3. for every `V ∈ 𝒱` and every finite locally free `𝒪_V`-module `ℰ` the map
>    `colim_{V' ≥ V} Γ(V', ℰ|_{V'}) → lim Γ(Y_n, ℰ|_{Y_n})` is an isomorphism.
>
> Then the restriction functor `colim_𝒱 FÉt_V ⟶ FÉt_Y` is fully faithful. The conclusion is in the
> form `FiniteEtaleColimitFullyFaithful`, which describes the hom sets of the directed colimit.
>
> The proof follows the source. By [Stacks, Tag 0EK2], condition (1) gives (2), (2) gives (3), and
> (3) gives full faithfulness of completion on the finite locally free objects. [Stacks, Tag 0ELA]
> then gives full faithfulness of restriction.

```lean
public theorem finiteEtaleColimitFullyFaithful_of_neighbourhoodSectionsComplete
    {X : Scheme.{u}} [IsNoetherian X] (Y : X.IdealSheafData)
    (h : NeighbourhoodSectionsCompleteQuasiAffine Y ∨
      NeighbourhoodSectionsCompleteAmplePowers Y ∨
      FiniteLocallyFreeComplete Y.subschemeι) :
    FiniteEtaleColimitFullyFaithful X Y
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.17, Tag 0EJW](https://stacks.math.columbia.edu/tag/0EJW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
