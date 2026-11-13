---
declaration: section
origin: cited
lean: Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_of_completionFullyFaithfulOnFiniteLocallyFree, Stacks.FundamentalGroup.finiteEtaleBaseChange_isEquivalence_of_completionEquivalence, Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_of_completionFullyFaithfulComplete, Stacks.FundamentalGroup.restriction_isEquivalence_of_completionEquivalence, Stacks.FundamentalGroup.faithful_finiteEtaleRestriction_of_components_meet, Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_of_sectionsComplete_of_or, Stacks.FundamentalGroup.bijective_map_finiteEtaleBaseChange_of_sectionsComplete_of_or, Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_of_neighbourhoodSectionsComplete
statement: formalized
proof: formalized
---

# 58.17 Restriction to a closed subscheme

Section 58.17 of the Stacks Project, [Tag 0EJW](https://stacks.math.columbia.edu/tag/0EJW). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EL8, a lemma

[Tag 0EL8](https://stacks.math.columbia.edu/tag/0EL8) in the Stacks Project.

**`Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_of_completionFullyFaithfulOnFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionToClosedSubscheme.lean, line 1052](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionToClosedSubscheme.lean#L1052). The attribute's comment: “proved from full faithfulness of completion on the finite locally free coherent modules alone”.

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

**`Stacks.FundamentalGroup.finiteEtaleBaseChange_isEquivalence_of_completionEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionEquivalenceOfCompletion.lean, line 2984](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionEquivalenceOfCompletion.lean#L2984). The attribute's comment: “completion an equivalence on finite locally free objects implies restriction FEt\_X to FEt\_Y an equivalence”.

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

**`Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_of_completionFullyFaithfulComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SectionsExtendFromCompletion.lean, line 636](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SectionsExtendFromCompletion.lean#L636). The attribute's comment: “the full statement: full faithfulness of completion on the finite locally free objects of the neighbourhood colimit gives full faithfulness of restriction of finite étale covers”.

> **[Stacks, Tag 0ELA].** Let `X` be a Noetherian scheme and let `Y ⊆ X` be a closed subscheme
> with ideal sheaf `I`. Let `𝒱` be the set of open subschemes `V ⊆ X` containing `Y`, ordered by
> reverse inclusion. Assume the completion functor `colim_𝒱 Coh(𝒪_V) ⟶ Coh(X, I)`, `ℱ ↦ ℱ^∧`, is
> fully faithful on the full subcategory of finite locally free objects. Then the restriction
> functor `colim_𝒱 FÉt_V ⟶ FÉt_Y` is fully faithful.
>
> The completion condition is the source's, condition (4) of [Stacks, Tag 0EK2],
> `Stacks.Algebraization.NeighbourhoodCompletion.CompletionFullyFaithfulComplete`, at the closed
> immersion of `Y`: for every neighbourhood `V` and all finite locally free `𝒪_V`-modules `𝒢`, `ℱ`,
> the map `colim_{W ⊆ V} Hom(𝒢|_W, ℱ|_W) ⟶ lim_n Hom(𝒢|_{Y_n}, ℱ|_{Y_n})` is bijective, which is
> full faithfulness of `ℱ ↦ ℱ^∧` on these objects since a morphism of `Coh(X, I)` between
> completions is a compatible family of morphisms on the `Y_n`. The conclusion is
> `Stacks.FundamentalGroup.FiniteEtaleColimitFullyFaithful`,
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

**`Stacks.FundamentalGroup.restriction_isEquivalence_of_completionEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionColimitEquivalenceOfCompletion.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionColimitEquivalenceOfCompletion.lean#L99). The attribute's comment: “the colimit functor is an equivalence: fully faithful, and every finite étale cover of Y extends to a neighbourhood, assuming as in the tag that completion is an equivalence on finite locally free modules”.

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

**`Stacks.FundamentalGroup.faithful_finiteEtaleRestriction_of_components_meet`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleMorphisms/Restriction.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleMorphisms/Restriction.lean#L102).

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

**`Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_of_sectionsComplete_of_or`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionSectionwiseComplete.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionSectionwiseComplete.lean#L80).

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

**`Stacks.FundamentalGroup.bijective_map_finiteEtaleBaseChange_of_sectionsComplete_of_or`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionSectionwiseComplete.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionSectionwiseComplete.lean#L105). The attribute's comment: “restated as bijectivity on hom sets”. References: SGA 2 X (2.5), “special case”.

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

**`Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_of_neighbourhoodSectionsComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionColimitFullyFaithful.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionColimitFullyFaithful.lean#L82). The attribute's comment: “the full tag, unconditionally: X Noetherian, Y a closed subscheme, and any one of conditions (1), (2), (3) imply that colim\_V FEt\_V -> FEt\_Y is fully faithful; full faithfulness spelled through the directed-colimit description of the hom sets of colim\_V FEt\_V (as in Stacks 04AX)”.

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
