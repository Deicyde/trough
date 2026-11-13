---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.changeOfBaseFibreProduct, AlgebraicGeometry.Stack.changeOfBaseFibreProductProjection, AlgebraicGeometry.Stack.changeOfBaseFibreProductPair, AlgebraicGeometry.Stack.changeOfBaseFibreProductOverBase, AlgebraicGeometry.Stack.algebraicStackConstructionObjEquiv_changeOfBaseFibreProductOverBase, AlgebraicGeometry.Stack.changeOfBaseFibreProductOverBase_p, AlgebraicGeometry.Stack.changeBaseAlgebraicStack, AlgebraicGeometry.Stack.exists_comp_p_eq_map_of_changeBase
statement: formalized
proof: formalized
---

# 94.19 Change of base scheme

Section 94.19 of the Stacks Project, [Tag 04X4](https://stacks.math.columbia.edu/tag/04X4). 4 tags here are carried by 40 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04X4, the section

[Tag 04X4](https://stacks.math.columbia.edu/tag/04X4) in the Stacks Project.

**`AlgebraicGeometry.Stack.changeOfBaseFibreProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseSection.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseSection.lean#L92). The attribute's comment: “the 2-fibre product X'\_S = (Sch/S)\_fppf ×\_\{(Sch/S')\_fppf} X', which is an algebraic stack over S' according to Lemma 04T2”.

> **The 2-fibre product `𝒳'_S = (Sch/S)_fppf ×_{(Sch/S')_fppf} 𝒳'` of Section 04X4.** For an
> algebraic stack `𝒳'` over `S'`, the apex of the canonical 2-fibre product square of the cospan
> formed by the structure 1-morphisms of the stack represented by `S/S'` (that is, `(Sch/S)_fppf`
> over `S'`) and of `𝒳'` to the final object `(Sch/S')_fppf`. It is an object of the 2-category of
> algebraic stacks over `S'`, which is the source's appeal to Lemma 04T2.

```lean
def changeOfBaseFibreProduct (𝒳' : AlgebraicStacks.{u, w} B S' hS') :
    AlgebraicStacks.{u, w} B S' hS'
```

**`AlgebraicGeometry.Stack.changeOfBaseFibreProductProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseSection.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseSection.lean#L102). The attribute's comment: “the natural 1-morphism p : X'\_S → (Sch/S)\_fppf”.

> **The natural 1-morphism `p : 𝒳'_S ⟶ (Sch/S)_fppf` of Section 04X4**: the projection of the
> 2-fibre product `AlgebraicGeometry.Stack.changeOfBaseFibreProduct` to its first factor, the
> stack represented by `S/S'`.

```lean
def changeOfBaseFibreProductProjection (𝒳' : AlgebraicStacks.{u, w} B S' hS') :
    changeOfBaseFibreProduct B S S' hS hS' g 𝒳' ⟶ schemeStack.{u, w} B S' hS' (Over.mk g)
```

**`AlgebraicGeometry.Stack.changeOfBaseFibreProductPair`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseSection.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseSection.lean#L113). The attribute's comment: “the pair (X'\_S, p), an algebraic stack over S' with a 1-morphism to (Sch/S)\_fppf, i.e. an object of the right-hand side of Lemma 04X5”.

> **The pair `(𝒳'_S, p)` of Section 04X4**, as an object of the right-hand 2-category of
> Lemma 04X5: an algebraic stack over `S'` with a 1-morphism to the stack represented by
> `S/S'`.

```lean
def changeOfBaseFibreProductPair (𝒳' : AlgebraicStacks.{u, w} B S' hS') :
    AlgebraicStackPair.{u, w} B S S' hS hS' g
```

**`AlgebraicGeometry.Stack.changeOfBaseFibreProductOverBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseSection.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseSection.lean#L123). The attribute's comment: “by Lemma 04X5 the pair (X'\_S, p) corresponds in a canonical way to an algebraic stack over S”.

> **The algebraic stack over `S` that `(𝒳'_S, p)` corresponds to (Section 04X4).** The image of
> the pair `AlgebraicGeometry.Stack.changeOfBaseFibreProductPair` under the inverse of the
> bijection on objects of Lemma 04X5, that is, under Construction B.

```lean
def changeOfBaseFibreProductOverBase (𝒳' : AlgebraicStacks.{u, w} B S' hS') :
    AlgebraicStacks.{u, w} B S hS
```

**`AlgebraicGeometry.Stack.algebraicStackConstructionObjEquiv_changeOfBaseFibreProductOverBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseSection.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseSection.lean#L134). The attribute's comment: “the algebraic stack over S corresponds to (X'\_S, p) under Lemma 04X5: Construction A returns X'\_S over S' together with p”.

> **The correspondence of Lemma 04X5 carries the algebraic stack over `S` of Section 04X4 back
> to `(𝒳'_S, p)`.** Construction A applied to
> `AlgebraicGeometry.Stack.changeOfBaseFibreProductOverBase` returns the 2-fibre product `𝒳'_S`
> over `S'` together with its natural 1-morphism `p`.

```lean
theorem algebraicStackConstructionObjEquiv_changeOfBaseFibreProductOverBase
    (𝒳' : AlgebraicStacks.{u, w} B S' hS') :
    algebraicStackConstructionObjEquiv.{u, w} B S S' hS hS' g
        (changeOfBaseFibreProductOverBase B S S' hS hS' g 𝒳') =
      changeOfBaseFibreProductPair B S S' hS hS' g 𝒳'
```

**`AlgebraicGeometry.Stack.changeOfBaseFibreProductOverBase_p`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseSection.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseSection.lean#L145). The attribute's comment: “the structure functor of that algebraic stack over S is p”.

> The structure functor over `S` of the algebraic stack of Section 04X4 is the natural
> 1-morphism `p : 𝒳'_S ⟶ (Sch/S)_fppf`, read through the identification of the big fppf site of `S`
> with the localization of the big fppf site of `S'` at `S/S'`.

```lean
lemma changeOfBaseFibreProductOverBase_p (𝒳' : AlgebraicStacks.{u, w} B S' hS') :
    (changeOfBaseFibreProductOverBase B S S' hS hS' g 𝒳').val.val.p =
      (changeOfBaseFibreProductProjection B S S' hS hS' g 𝒳').hom.hom.toFunctor ⋙
        (Over.iteratedSliceEquiv (Over.mk g)).functor
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Stack.changeBaseAlgebraicStack`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean#L1178), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseSection.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseSection.lean#L77) (StacksFrontier): “the introduction's upshot: given a morphism S → S' of base schemes, any algebraic stack over S can be viewed as an algebraic stack over S' (Construction A on objects of the 2-category of algebraic stacks)”.

## Tag 04X5, a lemma

[Tag 04X5](https://stacks.math.columbia.edu/tag/04X5) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_comp_p_eq_map_of_changeBase`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean#L355). The attribute's comment: “the scheme-valued points of Construction A”.

> **The scheme-valued points of Construction A are those of the original category.** Every
> scheme-valued point of `changeBase 𝒳` over the big fppf site of `S'` is a scheme-valued point of
> `𝒳` over the big fppf site of `S`, on the same scheme, lying over a morphism to `S` whose
> composite with `g` is the structure morphism of the point's base.
>
> This is the content of the source's remark that the statement of Stacks 04X5 makes sense because
> `j : (Sch/S)_{fppf} ⟶ (Sch/S')_{fppf}` is the localization functor at `S/S'`: no information about
> the base is lost by Construction A. Together with
> `AlgebraicGeometry.Stack.comp_changeBase_p_eq_map` it matches up the quantifications over
> scheme-valued points in the two sides of the algebraicity criterion.

```lean
lemma exists_comp_p_eq_map_of_changeBase (𝒳 : BasedCategory.{v, t} (BigFppfOver B S hS))
    (V' : BigFppfOver B S' hS') (y : BigFppfOver B V'.left.1 V'.left.2 ⥤ 𝒳.obj)
    (hy : y ⋙ (changeBase B S S' hS hS' g 𝒳).p = Over.map V'.hom) :
    ∃ h : V'.left ⟶ B.obj hS, y ⋙ 𝒳.p = Over.map h ∧ h ≫ g = V'.hom
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_changeBaseFunctor_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean#L394). The attribute's comment: “representability by algebraic spaces is unchanged by Construction A”.

> **Stacks 02ZW is unchanged by Construction A.** A 1-morphism of categories over the big fppf
> site of `S` is representable by algebraic spaces exactly when the 1-morphism over the big fppf
> site of `S'` produced by Construction A is.
>
> This is the second of the four clauses of Stacks 026O, in the form in which the clause is used:
> the clause itself is this statement for the diagonal. The proof is the two halves of the source's
> remark that `j : (Sch/S)_{fppf} ⟶ (Sch/S')_{fppf}` is the localization functor at `S/S'`. On
> points it is `AlgebraicGeometry.Stack.comp_changeBase_p_eq_map` and
> `AlgebraicGeometry.Stack.exists_comp_p_eq_map_of_changeBase`, which match up the quantifications
> over scheme-valued points of the target. On 2-fibre products it is
> `CategoryTheory.TwoFibreProductOver.fstEquivalenceOver`, which says that relocalizing the base
> does not change the 2-fibre product of a point with the 1-morphism, as an equivalence over the
> big fppf site of the point's scheme; so the representing algebraic space is literally the same on
> both sides, and no transport of algebraicity along a comparison is needed.

```lean
theorem isRepresentableByAlgebraicSpaces_changeBaseFunctor_iff
    {𝒳 : BasedCategory.{v, t} (BigFppfOver B S hS)}
    {𝒴 : BasedCategory.{v₂, t₂} (BigFppfOver B S hS)} (f : 𝒳 ⥤ᵇ 𝒴) :
    IsRepresentableByAlgebraicSpaces B S' hS' (changeBaseFunctor B S S' hS hS' g f) ↔
      IsRepresentableByAlgebraicSpaces B S hS f
```

**`AlgebraicGeometry.Stack.hasRelativeProperty_surjective_changeBaseHom_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean, line 504](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean#L504). The attribute's comment: “surjectivity of the presentation is unchanged by Construction A”.

> **Relative surjectivity is unchanged by Construction A.** A 1-morphism of categories fibred
> in groupoids over the big fppf site of `S` which is representable by algebraic spaces has the
> relative property of Stacks 03YK for surjectivity of morphisms of algebraic spaces exactly when
> the 1-morphism over the big fppf site of `S'` produced by Construction A has it.
>
> This is the *surjectivity half of the presentation clause* of Stacks 026O, which is what Stacks
> 04X5 needs of it: that clause tests surjectivity and smoothness of the structural morphism of
> every algebraic space representing a base change of the presentation along a scheme-valued point
> of the stack, and for surjectivity that test is exactly
> `AlgebraicGeometry.Stack.HasRelativeProperty` at
> `AlgebraicGeometry.Space.surjectiveMorphismProperty`.
>
> No statement about the lower-shriek extension of Stacks 03I5 part (2) is needed. Stacks 06D7
> replaces the relative test by surjectivity on objects, Stacks 06D4, which
> `AlgebraicGeometry.Stack.isSurjectiveOnObjects_changeBaseHom_iff` transfers directly.

```lean
theorem hasRelativeProperty_surjective_changeBaseHom_iff
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom) :
    HasRelativeProperty.{u, v, w, vP} B S' hS' (Space.surjectiveMorphismProperty B S' hS')
        (changeBaseHom B S S' hS hS' g f)
        ((isRepresentableByAlgebraicSpaces_changeBaseFunctor_iff B S S' hS hS' g f.hom).2 hf) ↔
      HasRelativeProperty.{u, v, w, vP} B S hS (Space.surjectiveMorphismProperty B S hS) f hf
```

**`AlgebraicGeometry.Stack.hasRelativeProperty_smooth_changeBaseHom_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean, line 558](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean#L558). The attribute's comment: “smoothness of the presentation is unchanged by Construction A”.

> **A relative property tested on étale charts is unchanged by Construction A.** Let `Q` be a
> property of morphisms of schemes. A 1-morphism of categories fibred in groupoids over the big
> fppf site of `S` which is representable by algebraic spaces has the relative property of
> Stacks 03YK at the every-étale-chart condition of Stacks 03MJ for `Q` exactly when the 1-morphism
> over the big fppf site of `S'` produced by Construction A has it.
>
> At `Q = AlgebraicGeometry.Smooth` this is the *smoothness half of the presentation clause* of
> Stacks 026O, the other half being
> `AlgebraicGeometry.Stack.hasRelativeProperty_surjective_changeBaseHom_iff`; that case is recovered
> by applying this statement to `@AlgebraicGeometry.Smooth`, since
> `AlgebraicGeometry.Space.smoothMorphismProperty` *is* the every-étale-chart condition at
> `AlgebraicGeometry.Smooth`. It is stated at a general `Q` because that is what the separation
> axioms of Stacks 04YW need of it: for instance
> `AlgebraicGeometry.Space.IsLocallyQuasiFinite` is the every-étale-chart condition at
> `AlgebraicGeometry.LocallyOfFiniteType ⊓ AlgebraicGeometry.LocallyQuasiFinite`, and nothing in the
> argument is about smoothness.
>
> The relative property is written out as the quantifier of
> `AlgebraicGeometry.Stack.HasRelativeProperty` rather than through that abbreviation, exactly as
> `AlgebraicGeometry.Stack.relativeProperty_baseChange` and
> `AlgebraicGeometry.Stack.relativeProperty_of_equivalences` do: the abbreviation carries
> `[P.IsStableUnderBaseChange]` and `[P.IsLocalAtTarget (Space.Topology.fppf.precoverage B S hS)]`
> as instance arguments and neither is available for a general `Q`, while its body uses neither, so
> the quantifier is the same proposition carrying no hypothesis on the property.
>
> Unlike surjectivity this really is a statement about the lower-shriek extension of Stacks 03I5
> part (2), since smoothness has no objects-level criterion. The two quantifications match up by
> `AlgebraicGeometry.Stack.comp_changeBase_p_eq_map` and
> `AlgebraicGeometry.Stack.exists_comp_p_eq_map_of_changeBase` on scheme-valued points and by
> `CategoryTheory.TwoFibreProductOver.fstEquivalenceOver` on 2-fibre products, exactly as in
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_changeBaseFunctor_iff`; so the
> representing algebraic space is the same object on both sides, living over the same scheme over
> `S`, and what is left is that its structural morphism has `Q` on every étale chart over `S`
> exactly when it does over `S'`. That is
> `AlgebraicGeometry.Space.holdsOnEveryEtaleChart_spacesOverSmallerBaseFunctor_iff`: the
> every-étale-chart condition of Stacks 03MJ for the structural morphism of the image of Stacks
> 04SG's forward functor does not depend on the base at all.

```lean
theorem hasRelativeProperty_smooth_changeBaseHom_iff (Q : MorphismProperty Scheme.{u})
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (f : 𝒳 ⟶ 𝒴)
    (_hf : IsRepresentableByAlgebraicSpaces B S hS f.hom) :
    (∀ (U : BigFppfOver B S' hS')
        (y : BigFppfOver B U.left.1 U.left.2 ⥤
          (changeBaseFiberedInGroupoids B S S' hS hS' g 𝒴).val.obj)
        (_hy : y ⋙ (changeBaseFiberedInGroupoids B S S' hS hS' g 𝒴).val.p = Over.map U.hom)
        (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom)
            (changeBaseFiberedInGroupoids B S S' hS hS' g 𝒳).val.p
            (changeBaseFiberedInGroupoids B S S' hS hS' g 𝒴).val.p y
            (CatFiberedInGroupoids.homFunctor (changeBaseHom B S S' hS hS' g f)))
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        Space.HoldsOnEveryEtaleChart B S' hS' Q
          (algebraicSpaceMap B S' hS' U
            ((spacesOverSmallerBaseFunctor B U.left.1 S' U.left.2 hS' U.hom).obj
              ⟨F, hF⟩)).hom) ↔
      (∀ (U : BigFppfOver B S hS)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.obj)
        (_hy : y ⋙ 𝒴.val.p = Over.map U.hom)
        (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.p 𝒴.val.p y
            (CatFiberedInGroupoids.homFunctor f))
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        Space.HoldsOnEveryEtaleChart B S hS Q
          (algebraicSpaceMap B S hS U
            ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj
              ⟨F, hF⟩)).hom)
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_diagonalBasedFunctor_changeBase_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean, line 784](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean#L784). The attribute's comment: “representability of the diagonal is unchanged by Construction A”.

> **The diagonal clause of Stacks 026O is unchanged by Construction A.** The diagonal of a
> category fibred in groupoids over the big fppf site of `S` is representable by algebraic spaces
> exactly when the diagonal of the category over the big fppf site of `S'` produced by Construction
> A is.
>
> The two diagonals are *not* comparable directly: the self-product of `changeBase 𝒳` over the big
> fppf site of `S'` has the strictly larger object set of pairs lying over a common `S'`-scheme by
> two different morphisms to `S`, so there is no equivalence to transport along. The route taken
> instead is Stacks 045G: by its conditions (1), (2) and (3) the clause is equivalent to
> `AlgebraicGeometry.Stack.IsRepresentableFromSchemes`, which does transfer
> (`AlgebraicGeometry.Stack.isRepresentableFromSchemes_changeBase_iff`), because a 1-morphism out
> of a scheme-valued point sees only one morphism to `S` at a time. The equalizer of the two
> morphisms, which a direct comparison of the self-products would have to form, is absorbed into the
> already-proved equivalence of conditions (2) and (3).

```lean
theorem isRepresentableByAlgebraicSpaces_diagonalBasedFunctor_changeBase_iff
    (𝒳 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)) :
    IsRepresentableByAlgebraicSpaces B S' hS'
        (diagonalBasedFunctor B S' hS' (changeBaseFiberedInGroupoids B S S' hS hS' g 𝒳)) ↔
      IsRepresentableByAlgebraicSpaces B S hS (diagonalBasedFunctor B S hS 𝒳)
```

**`AlgebraicGeometry.Stack.exists_factorization_of_isCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean, line 830](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean#L830). The attribute's comment: “the descent input of the stack clause of Construction A”.

> **A point of the big fppf site of `S'` covered by points coming from the site of `S` comes
> from the site of `S` itself.** If the structure morphism of every member of a covering family of
> `U'` factors through `g`, and the factorizations agree on every pair of morphisms into two
> members agreeing over `U'`, then the structure morphism of `U'` factors through `g`, compatibly
> with the given factorizations, and the factorization is unique by
> `AlgebraicGeometry.Stack.eq_of_isCovering`.
>
> This is the descent input of the stack-in-groupoids clause of Stacks 026O for Construction A: an
> object of the total category of `changeBase 𝒳` lying over `U'` lies over an object of the big
> fppf site of `S`, so gluing objects along a covering family of `U'` is only possible when
> `U'.hom` itself factors through `g`, and nothing short of the sheaf condition for the
> representable presheaf of `S` on the big fppf site produces that factorization.

```lean
theorem exists_factorization_of_isCovering {U' : BigFppfOver B S' hS'} {I : Type w}
    (Z : I → BigFppfOver B S' hS') (f : ∀ i, Z i ⟶ U')
    (hf : Sieve.ofArrows Z f ∈ BigFppfOver.topology B S' hS' U')
    (a : ∀ i, (Z i).left ⟶ B.obj hS) (ha : ∀ i, a i ≫ g = (Z i).hom)
    (hcompat : ∀ (i j : I) (Y : B.Schemes) (u : Y ⟶ (Z i).left) (v : Y ⟶ (Z j).left),
      u ≫ (f i).left = v ≫ (f j).left → u ≫ a i = v ≫ a j) :
    ∃ h : U'.left ⟶ B.obj hS, h ≫ g = U'.hom ∧ ∀ i, (f i).left ≫ h = a i
```

**`AlgebraicGeometry.Stack.isStackInGroupoids_of_changeBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean, line 862](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean#L862). The attribute's comment: “the stack clause transfers back along Construction A”.

> **The stack-in-groupoids clause of Stacks 026O transfers back along Construction A.** If the
> category over the big fppf site of `S'` produced by Construction A is a stack in groupoids for
> the fppf topology there, then the original category over the big fppf site of `S` is a stack in
> groupoids for the fppf topology of that site.
>
> This is one of the two implications of the third of the four clauses of Stacks 026O. Every piece
> of data over the site of `S` is read over the site of `S'` — covering families by
> `CategoryTheory.Over.mem_over_map_iff`, the fibre-product overlaps by
> `CategoryTheory.Over.isPullback_map_iff`, restrictions by
> `CategoryTheory.Functor.Restriction.overMap`, and descent data field by field — the hypothesis is
> applied there, and the conclusion is read back. The one step that is not formal is the object of
> the site of `S` that a glued object lies over: the hypothesis produces an object lying over the
> image of `U`, which determines its structure morphism only after composition with every member of
> the covering family, so `AlgebraicGeometry.Stack.eq_of_isCovering` is used to identify it
> with `U`.
>
> The converse implication is
> `AlgebraicGeometry.Stack.isStackInGroupoids_changeBase`, and the two together are
> `AlgebraicGeometry.Stack.isStackInGroupoids_changeBase_iff`.

```lean
theorem isStackInGroupoids_of_changeBase (𝒳 : BasedCategory.{v, t} (BigFppfOver B S hS))
    (h : (changeBase B S S' hS hS' g 𝒳).p.IsStackInGroupoids.{w}
      (BigFppfOver.topology B S' hS')) :
    𝒳.p.IsStackInGroupoids.{w} (BigFppfOver.topology B S hS)
```

**`AlgebraicGeometry.Stack.isStackInGroupoids_changeBase_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean, line 903](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean#L903). The attribute's comment: “the stack clause of Stacks 026O is unchanged by Construction A”.

> **The stack-in-groupoids clause of Stacks 026O is unchanged by Construction A.** A category
> over the big fppf site of `S` is a stack in groupoids for the fppf topology there exactly when
> the category over the big fppf site of `S'` produced by Construction A is a stack in groupoids
> for the fppf topology of that site.
>
> This is the third of the four clauses of Stacks 026O, in full. The clause is read entirely in the
> two localized fppf topologies: a covering family of the site of `S` is one of the site of `S'`
> and conversely (`CategoryTheory.Over.mem_over_map_iff` and
> `CategoryTheory.Over.mem_over_mk`), and the fibre-product overlaps, the restrictions, the fibre
> isomorphisms and the descent data all match. The one non-formal ingredient is subcanonicity of
> the fppf topology, `AlgebraicGeometry.BigFppfSite.subcanonical_topology`, which is what pins
> down the morphism to `S` carried by an object of the site of `S'`.

```lean
theorem isStackInGroupoids_changeBase_iff (𝒳 : BasedCategory.{v, t} (BigFppfOver B S hS)) :
    (changeBase B S S' hS hS' g 𝒳).p.IsStackInGroupoids.{w}
        (BigFppfOver.topology B S' hS') ↔
      𝒳.p.IsStackInGroupoids.{w} (BigFppfOver.topology B S hS)
```

**`AlgebraicGeometry.Stack.isStack_changeBase_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean, line 930](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean#L930). The attribute's comment: “the sieve-indexed stack clause of Stacks 026O is unchanged by Construction A”.

> **The sieve-indexed stack clause of Stacks 026F is unchanged by Construction A.** A category
> over the big fppf site of `S` is a stack in the sense of Stacks 026F for the fppf topology there
> exactly when the category over the big fppf site of `S'` produced by Construction A is one for
> the fppf topology of that site.
>
> Unlike the family-indexed condition this needs no transfer of covering families and descent data
> at all: both sides are read through the single statement that the composite of the structure
> functor with the localization functor of the big fppf site of `S` is a stack over the whole big
> fppf site, by Constructions A and B of Stacks 04WV
> (`CategoryTheory.Over.isStack_map_iff`). Subcanonicity of the fppf topology
> (`AlgebraicGeometry.BigFppfSite.subcanonical_topology`) supplies the sheaf hypothesis of those two
> constructions for the representable presheaves of `S` and of `S'`.
>
> The universes are those of Stacks 04X5 itself: Construction B relates two categories over the
> same site in the *same* universes, so the total category is taken in the object universe one
> above the scheme universe, which is what `AlgebraicGeometry.Stack.IsAlgebraicStack` is applied
> at.

```lean
theorem isStack_changeBase_iff (𝒳 : BasedCategory.{u, u + 1} (BigFppfOver B S hS)) :
    (changeBase B S S' hS hS' g 𝒳).p.IsStack (BigFppfOver.topology B S' hS') ↔
      𝒳.p.IsStack (BigFppfOver.topology B S hS)
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_changeBase_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean, line 1159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBase.lean#L1159). The attribute's comment: “algebraicity criterion”.

> **The algebraicity criterion of Stacks 04X5.** A category over the big fppf site of `S` is an
> algebraic stack over `S` exactly when the category over the big fppf site of `S'` produced by
> Construction A is an algebraic stack over `S'`. Together with the object, 1-morphism and
> 2-morphism equivalences of Stacks 04WV this is what restricts that isomorphism of 2-categories to
> algebraic stacks.
>
> `AlgebraicGeometry.Stack.IsAlgebraicStack` is not a conjunction of the four clauses of Stacks
> 026O: the fibred-in-groupoids clause is existentially quantified ahead of the others, which are
> stated for the bundled category fibred in groupoids it produces. So the witness is transported
> first, by `AlgebraicGeometry.Stack.isFiberedInGroupoids_changeBase_iff`, and the bundled object on
> the `S'` side is then `AlgebraicGeometry.Stack.changeBaseFiberedInGroupoids` of the bundled object
> on the `S` side — the same underlying category over the site, paired with a proof of a
> proposition, so the two agree definitionally and the remaining clauses can be transported one by
> one:
>
> * the stack clause is `AlgebraicGeometry.Stack.isStack_changeBase_iff` in its sieve-indexed half
>   and `AlgebraicGeometry.Stack.isStackInGroupoids_changeBase_iff` in its family-indexed half;
> * the diagonal clause is
>   `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_diagonalBasedFunctor_changeBase_iff`;
> * the presentation clause is the pair
>   `AlgebraicGeometry.Stack.hasRelativeProperty_surjective_changeBaseHom_iff` and
>   `AlgebraicGeometry.Stack.hasRelativeProperty_smooth_changeBaseHom_iff`, read through
>   `AlgebraicGeometry.Stack.forall_isSurjective_and_isSmooth_iff_hasRelativeProperty`.
>
> The presentation clause is the only one whose quantifiers move. A presentation of the stack over
> `S'` is a 1-morphism out of the category represented by an object `U'` of the site of `S'`, and
> its mere existence forces `U'.hom` to factor through `g`, by the rigidity of relocalization
> (`CategoryTheory.Over.exists_eq_map_of_comp_map`); the slice of the site of `S'` over `U'` is then
> identified with the slice of the site of `S` over that factorization by
> `AlgebraicGeometry.Stack.factorSliceFunctor`, and in the other direction a presentation by `U`
> over `S` becomes one by `(Over.map g).obj U` over `S'` through
> `AlgebraicGeometry.Stack.factorSliceInverse`. Neither identification is an equality of
> categories, so the relative properties of Stacks 03YK have to be moved across it; that is
> `AlgebraicGeometry.Stack.hasRelativeProperty_iff_of_equivalence_source`.
>
> The universes are those of Stacks 04X5: the total category is taken with object universe one
> above the scheme universe, which is where Construction B of Stacks 04WV — the one ingredient
> whose universes are pinned — applies.

```lean
theorem isAlgebraicStack_changeBase_iff (𝒳 : BasedCategory.{u, u + 1} (BigFppfOver B S hS)) :
    IsAlgebraicStack.{u, w} B S' hS' (changeBase B S S' hS hS' g 𝒳) ↔
      IsAlgebraicStack.{u, w} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_of_changeBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseAlgebraicStack.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseAlgebraicStack.lean#L196). The attribute's comment: “algebraicity transfers back along Construction A”.

> **Stacks 04X5, the algebraic-stack clause in the direction Construction A reflects.** Let
> `g : S ⟶ S'` be a morphism of a big fppf site and let `𝒳` be a category fibred in groupoids over
> the big fppf site of `S`. If the category over the big fppf site of `S'` produced by Construction
> A out of `𝒳` is an algebraic stack, then `𝒳` is an algebraic stack over `S`.
>
> All four clauses of Stacks 026O are carried back: see the implementation notes. The descent
> universe of the conclusion is free, because the sieve-indexed conjunct of the stack clause does
> not depend on it.

```lean
theorem isAlgebraicStack_of_changeBase
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h : IsAlgebraicStack.{u, w'} B S' hS' (changeBase B S S' hS hS' g 𝒳.val)) :
    IsAlgebraicStack.{u, w} B S hS 𝒳.val
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_changeBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseAlgebraicStack.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseAlgebraicStack.lean#L315). The attribute's comment: “algebraicity transfers along Construction A”.

> **Stacks 04X5, the algebraic-stack clause in the direction Construction A produces.** Let
> `g : S ⟶ S'` be a morphism of a big fppf site and let `𝒳` be a category fibred in groupoids over
> the big fppf site of `S`. If `𝒳` is an algebraic stack over `S`, then the category over the big
> fppf site of `S'` produced by Construction A out of `𝒳` is an algebraic stack over `S'`.
>
> This is the converse of `AlgebraicGeometry.Stack.isAlgebraicStack_of_changeBase`, and it is the
> statement that makes **Stacks 04X6** a definition of an algebraic stack rather than merely of a
> category over the big fppf site of `S'`.
>
> Three of the four clauses of Stacks 026O are the already-available biconditionals of
> `StacksFrontier.AlgebraicGeometry.Stacks.ChangeOfBase`, read in the forward direction: being fibred
> in groupoids is `AlgebraicGeometry.Stack.isFiberedInGroupoids_changeBase_iff`, the stack clause is
> `AlgebraicGeometry.Stack.isStack_changeBase` together with
> `AlgebraicGeometry.Stack.isStackInGroupoids_changeBase_of_isStack`, and the diagonal clause is
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_diagonalBasedFunctor_changeBase_iff`.
> The descent universe of the conclusion is free, because the sieve-indexed conjunct of the stack
> clause does not depend on it and the family-indexed one is derived from it at any universe.
>
> The presentation clause is easier in this direction than in the reflecting one, and this is the
> asymmetry of Construction A working in our favour. Reflection has to *discover* the presenting
> object of the site of `S` inside a presentation by an object of the site of `S'`, which is what
> forces `CategoryTheory.Over.exists_eq_map_of_comp_map` there. Here the presenting object is
> simply pushed forward: a presentation of `𝒳` by `U` becomes a presentation of `changeBase 𝒳` by
> `(CategoryTheory.Over.map g).obj U`, the two slices are identified by
> `AlgebraicGeometry.Stack.factorSliceInverse` — which is exactly
> `AlgebraicGeometry.Stack.factorSliceFunctor` taken in the direction that makes the comparison
> isomorphism of Stacks 0457 the identity — and representability and the two relative properties
> cross by `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_changeBaseFunctor_iff`,
> `AlgebraicGeometry.Stack.hasRelativeProperty_surjective_changeBaseHom_iff` and
> `AlgebraicGeometry.Stack.hasRelativeProperty_smooth_changeBaseHom_iff`, followed by Stacks 0457
> and 0459 in the source variable along that identification.

```lean
theorem isAlgebraicStack_changeBase
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h : IsAlgebraicStack.{u, w} B S hS 𝒳.val) :
    IsAlgebraicStack.{u, w'} B S' hS' (changeBase B S S' hS hS' g 𝒳.val)
```

**`AlgebraicGeometry.Stack.changeBaseStructureHom_toFunctor`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean#L222). The attribute's comment: “Construction A on 1-morphisms, as a functor”.

> The underlying functor of `AlgebraicGeometry.Stack.changeBaseStructureHom` is the structure
> functor of `𝒳`, read through the inverse of the iterated-slice equivalence. This is the
> `object_structure` clause of the correspondence of Stacks 04X5.

```lean
lemma changeBaseStructureHom_toFunctor (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    (changeBaseStructureHom B S S' hS hS' g 𝒳).hom.toFunctor =
      𝒳.val.val.p ⋙ (Over.iteratedSliceEquiv (Over.mk g)).inverse
```

**`AlgebraicGeometry.Stack.algebraicStackConstructionA_val_val`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean#L239). The attribute's comment: “Construction A on objects, on the underlying fibred category”.

> The algebraic stack over `S'` underlying Construction A is Construction A of the underlying
> category over the big fppf site of `S`. This is the `object_underlying` clause of the
> correspondence of Stacks 04X5.

```lean
lemma algebraicStackConstructionA_val_val (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    (algebraicStackConstructionA B S S' hS hS' g 𝒳).1.val.val =
      changeBase B S S' hS hS' g 𝒳.val.val
```

**`AlgebraicGeometry.Stack.algebraicStackConstructionB_p`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean#L295). The attribute's comment: “Construction B on objects, on the projection”.

> The structure functor produced by Construction B is the pair's 1-morphism to the stack
> represented by `S/S'`, read through the iterated-slice equivalence.

```lean
lemma algebraicStackConstructionB_p (X : AlgebraicStackPair.{u, w} B S S' hS hS' g) :
    (algebraicStackConstructionB B S S' hS hS' g X).val.val.p =
      X.2.hom.toFunctor ⋙ (Over.iteratedSliceEquiv (Over.mk g)).functor
```

**`AlgebraicGeometry.Stack.algebraicStackConstructionObjEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean#L330). The attribute's comment: “the bijection on objects”.

> **Constructions A and B of Stacks 04X5 are mutually inverse on objects.** An algebraic stack
> over `S` is the same thing as an algebraic stack over `S'` together with a 1-morphism to the stack
> represented by `S/S'`.
>
> Both round trips are strict. In one direction nothing has to be done: the pair carries no
> information beyond its 1-morphism, and the iterated-slice equivalence composed the other way is
> the identity on the nose. In the other the structure functor of the pair's first component has to
> be recognized as the 1-morphism followed by the localization functor of `S/S'`, which is what
> being a 1-morphism over `S'` says. The two algebraicity conditions agree by
> `AlgebraicGeometry.Stack.isAlgebraicStack_changeBase_iff`.

```lean
def algebraicStackConstructionObjEquiv :
    AlgebraicStacks.{u, w} B S hS ≃ AlgebraicStackPair.{u, w} B S S' hS hS' g
```

**`AlgebraicGeometry.Stack.algebraicStackConstructionHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean, line 347](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean#L347). The attribute's comment: “the bijection on 1-morphisms”.

> **Constructions A and B of Stacks 04X5 are bijective on 1-morphisms**, and both are the
> identity on the underlying functor. In one direction the commutation with the structure functors
> is composed with the relocalization functor and with the inverse iterated-slice equivalence; in
> the other it is recovered by composing the pair condition with the iterated-slice equivalence,
> which cancels on the nose.

```lean
def algebraicStackConstructionHomEquiv (𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS) :
    (𝒳 ⟶ 𝒴) ≃ AlgebraicStackPairHom B S S' hS hS' g
      (algebraicStackConstructionA B S S' hS hS' g 𝒳)
      (algebraicStackConstructionA B S S' hS hS' g 𝒴)
```

**`AlgebraicGeometry.Stack.algebraicStackConstructionHomEquiv_val_hom_toFunctor`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean#L369). The attribute's comment: “that bijection, on the underlying functor”.

> The bijection on 1-morphisms is the identity on the underlying functor. This is the
> `hom_underlying` clause of the correspondence of Stacks 04X5; no heterogeneous equality is needed,
> the two functors having the same type.

```lean
lemma algebraicStackConstructionHomEquiv_val_hom_toFunctor
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (φ : 𝒳 ⟶ 𝒴) :
    (algebraicStackConstructionHomEquiv B S S' hS hS' g 𝒳 𝒴 φ).val.hom.toFunctor =
      φ.hom.hom.toFunctor
```

**`AlgebraicGeometry.Stack.algebraicStackConstructionHomEquiv_id`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean, line 377](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean#L377). The attribute's comment: “that bijection carries the identity to the identity”.

> Construction A preserves the identity 1-morphism.

```lean
lemma algebraicStackConstructionHomEquiv_id (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    algebraicStackConstructionHomEquiv B S S' hS hS' g 𝒳 𝒳 (𝟙 𝒳) =
      AlgebraicStackPairHom.id B S S' hS hS' g
        (algebraicStackConstructionA B S S' hS hS' g 𝒳)
```

**`AlgebraicGeometry.Stack.algebraicStackConstructionHomEquiv_comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean, line 385](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean#L385). The attribute's comment: “that bijection is compatible with composition”.

> Construction A preserves composition of 1-morphisms.

```lean
lemma algebraicStackConstructionHomEquiv_comp {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS}
    (φ : 𝒳 ⟶ 𝒴) (ψ : 𝒴 ⟶ 𝒵) :
    algebraicStackConstructionHomEquiv B S S' hS hS' g 𝒳 𝒵 (φ ≫ ψ) =
      AlgebraicStackPairHom.comp B S S' hS hS' g
        (algebraicStackConstructionHomEquiv B S S' hS hS' g 𝒳 𝒴 φ)
        (algebraicStackConstructionHomEquiv B S S' hS hS' g 𝒴 𝒵 ψ)
```

**`AlgebraicGeometry.Stack.algebraicStackConstructionHom₂Equiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean#L398). The attribute's comment: “the bijection on 2-morphisms”.

> **Constructions A and B of Stacks 04X5 are bijective on 2-morphisms**, and both are the
> identity on the underlying morphism of functors. The only thing to transfer is the condition that
> a component lie over an identity, and that is unchanged by the relocalization functor by
> `CategoryTheory.Functor.isHomLift_overMap_iff`.

```lean
def algebraicStackConstructionHom₂Equiv {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (φ ψ : 𝒳 ⟶ 𝒴) :
    (φ ⟶ ψ) ≃ AlgebraicStackPairHom₂ B S S' hS hS' g
      (algebraicStackConstructionHomEquiv B S S' hS hS' g 𝒳 𝒴 φ)
      (algebraicStackConstructionHomEquiv B S S' hS hS' g 𝒳 𝒴 ψ)
```

**`AlgebraicGeometry.Stack.algebraicStackConstructionHom₂Equiv_hom_toNatTrans`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean, line 420](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean#L420). The attribute's comment: “the 2-morphism bijection, on the underlying natural transformation”.

> The bijection on 2-morphisms is the identity on the underlying morphism of functors. This is
> the `twoHom_underlying` clause of the correspondence of Stacks 04X5.

```lean
lemma algebraicStackConstructionHom₂Equiv_hom_toNatTrans
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} {φ ψ : 𝒳 ⟶ 𝒴} (η : φ ⟶ ψ) :
    (algebraicStackConstructionHom₂Equiv B S S' hS hS' g φ ψ η).hom.toNatTrans =
      η.hom.hom.toNatTrans
```

**`AlgebraicGeometry.Stack.algebraicStackConstructionHom₂Equiv_id`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean, line 428](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean#L428). The attribute's comment: “the 2-morphism bijection carries the identity to the identity”.

> Construction A preserves identity 2-morphisms.

```lean
lemma algebraicStackConstructionHom₂Equiv_id {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS}
    (φ : 𝒳 ⟶ 𝒴) :
    algebraicStackConstructionHom₂Equiv B S S' hS hS' g φ φ (𝟙 φ) = 𝟙 _
```

**`AlgebraicGeometry.Stack.algebraicStackConstructionHom₂Equiv_comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean#L435). The attribute's comment: “the 2-morphism bijection is compatible with vertical composition”.

> Construction A preserves vertical composition of 2-morphisms.

```lean
lemma algebraicStackConstructionHom₂Equiv_comp {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS}
    {φ ψ χ : 𝒳 ⟶ 𝒴} (η : φ ⟶ ψ) (θ : ψ ⟶ χ) :
    algebraicStackConstructionHom₂Equiv B S S' hS hS' g φ χ (η ≫ θ) =
      algebraicStackConstructionHom₂Equiv B S S' hS hS' g φ ψ η ≫
        algebraicStackConstructionHom₂Equiv B S S' hS hS' g ψ χ θ
```

**`AlgebraicGeometry.Stack.algebraicStackConstructionHom₂Equiv_whiskerLeft`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean, line 444](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean#L444). The attribute's comment: “the 2-morphism bijection is compatible with left whiskering”.

> Construction A preserves left whiskering.

```lean
lemma algebraicStackConstructionHom₂Equiv_whiskerLeft
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} (a : 𝒳 ⟶ 𝒴) {φ ψ : 𝒴 ⟶ 𝒵} (η : φ ⟶ ψ) :
    algebraicStackConstructionHom₂Equiv B S S' hS hS' g (a ≫ φ) (a ≫ ψ)
        (Bicategory.whiskerLeft a η) =
      Bicategory.whiskerLeft (algebraicStackConstructionHomEquiv B S S' hS hS' g 𝒳 𝒴 a).val
        (algebraicStackConstructionHom₂Equiv B S S' hS hS' g φ ψ η)
```

**`AlgebraicGeometry.Stack.algebraicStackConstructionHom₂Equiv_whiskerRight`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean, line 454](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean#L454). The attribute's comment: “the 2-morphism bijection is compatible with right whiskering”.

> Construction A preserves right whiskering.

```lean
lemma algebraicStackConstructionHom₂Equiv_whiskerRight
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} {φ ψ : 𝒳 ⟶ 𝒴} (η : φ ⟶ ψ) (a : 𝒴 ⟶ 𝒵) :
    algebraicStackConstructionHom₂Equiv B S S' hS hS' g (φ ≫ a) (ψ ≫ a)
        (Bicategory.whiskerRight η a) =
      Bicategory.whiskerRight (algebraicStackConstructionHom₂Equiv B S S' hS hS' g φ ψ η)
        (algebraicStackConstructionHomEquiv B S S' hS hS' g 𝒴 𝒵 a).val
```

**`AlgebraicGeometry.Stack.categoryOfAlgebraicStacksOverSmallerBaseScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean, line 534](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean#L534). The attribute's comment: “the resulting equivalence of 2-categories”.

> **Constructions A and B restrict to mutually inverse isomorphisms on objects, 1-morphisms and
> 2-morphisms of algebraic stacks.** This is the whole of the correspondence of Stacks 04X5 as a
> single object, assembled from the components proved above; the algebraicity criterion
> `AlgebraicGeometry.Stack.isAlgebraicStack_changeBase_iff` is what makes its object map well
> defined in both directions.

```lean
noncomputable def categoryOfAlgebraicStacksOverSmallerBaseScheme :
    AlgebraicStackCorrespondence.{u, w} B S S' hS hS' g
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_schemeFibredCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeStack.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeStack.lean#L195). The attribute's comment: “the stack of a scheme of the big fppf site is algebraic”.

> **Stacks 026O for the big fppf site of a scheme over `S`.** The big fppf site of a scheme
> `X` over `S`, read as a category fibred in groupoids over the big fppf site of `S`, is an
> algebraic stack.
>
> It is representable by the algebraic space `yoneda.obj X` by Stacks 04SV, so it is a stack in
> groupoids and its diagonal is representable by algebraic spaces; the identity 1-morphism
> presents it, being representable by algebraic spaces by Stacks 02ZZ and surjective and smooth
> by `AlgebraicGeometry.Stack.prop_identityPresentation`.
>
> Taken at `X = S/S'` for a morphism `g : S ⟶ S'` of the site, this is the clause of the
> 2-categorical correspondence of Stacks 04X5 asserting that the base of the right-hand
> 2-category is itself an algebraic stack over `S'`; the rest of that correspondence is in
> `StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseCorrespondence.lean`.

```lean
theorem isAlgebraicStack_schemeFibredCategory (X : BigFppfOver B S hS) :
    IsAlgebraicStack.{u, w} B S hS (schemeFibredCategory B S hS X).val
```

## Tag 04X6, a definition

[Tag 04X6](https://stacks.math.columbia.edu/tag/04X6) in the Stacks Project.

**`AlgebraicGeometry.Stack.changeBaseAlgebraicStacks`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseAlgebraicStack.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseAlgebraicStack.lean#L381).

> **Stacks 04X6.** An algebraic stack `𝒳` over `S`, *viewed as an algebraic stack over `S'`*
> along a morphism `g : S ⟶ S'` of the big fppf site: the algebraic stack over `S'` obtained by
> applying Construction A of **Stacks 04X5** to `𝒳`.
>
> The underlying category and its structure functor are `AlgebraicGeometry.Stack.changeBase`, which
> composes the structure functor of `𝒳` with `CategoryTheory.Over.map g`; the content of the
> definition is that the result is again an algebraic stack, which is
> `AlgebraicGeometry.Stack.isAlgebraicStack_changeBase`.

```lean
def changeBaseAlgebraicStacks (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    AlgebraicStacks.{u, w'} B S' hS'
```

## Tag 04X7, a definition

[Tag 04X7](https://stacks.math.columbia.edu/tag/04X7) in the Stacks Project.

**`AlgebraicGeometry.Stack.baseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeAlgebraicStack.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeAlgebraicStack.lean#L177). The attribute's comment: “the construction”.

> **Stacks 04X7, the construction.** The *change of base* of a category `𝒳'` over the big fppf
> site of `S'` along `g : S ⟶ S'`: the strict pullback of its structure functor along the
> relocalization functor of `g`, as a category over the big fppf site of `S`. An object is an object
> `U` of the big fppf site of `S` together with an object of `𝒳'` lying over `U/S'`, and the
> structure functor is the first projection.

```lean
def baseChange : BasedCategory.{u, u + 1} (BigFppfOver B S hS)
```

**`AlgebraicGeometry.Stack.baseChangeProductEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeAlgebraicStack.lean, line 361](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeAlgebraicStack.lean#L361). The attribute's comment: “the change of base is the two-fibre product over the base”.

> **The image of the change of base under Construction A is the 2-fibre product
> `𝒳' ×_{S'} S`.** The identification is strict in one composite: an object of the strict pullback
> is carried to the triple consisting of its object of `𝒳'`, its object of the big fppf site of `S`
> read in the slice at `S/S'`, and the defining equation of the strict pullback as the comparison
> 2-cell, and recovering the strict pullback from that triple returns it unchanged. In the other
> composite the object of the slice at `S/S'` is only recovered up to the unit of
> `CategoryTheory.Over.iteratedSliceEquiv`.

```lean
noncomputable def baseChangeProductEquivalence :
    BasedCategory.Equivalence (changeBase B S S' hS hS' g (baseChange B S S' hS hS' g 𝒳'))
      (baseChangeProduct B S S' hS hS' g 𝒳')
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeAlgebraicStack.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeAlgebraicStack.lean#L396). The attribute's comment: “the change of base is an algebraic stack”.

> **Stacks 04X7.** The change of base of an algebraic stack over `S'` along `g : S ⟶ S'` is an
> algebraic stack over `S`.
>
> Its image under Construction A is the 2-fibre product `𝒳' ×_{S'} S`, hence an algebraic stack
> over `S'` by Stacks 04TF; algebraicity is then carried back along Construction A by the direction
> of Stacks 04X5 proved in
> `AlgebraicGeometry.Stack.isAlgebraicStack_of_changeBase`.

```lean
theorem isAlgebraicStack_baseChange (h𝒳' : IsAlgebraicStack.{u, u + 1} B S' hS' 𝒳') :
    IsAlgebraicStack.{u, w} B S hS (baseChange B S S' hS hS' g 𝒳')
```

**`AlgebraicGeometry.Stack.changeOfBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseStack.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseStack.lean#L332).

> The change of base of an algebraic stack `𝒳'` over `S'` along a morphism `S ⟶ S'` of the big
> fppf site: the algebraic stack over `S` whose total category is the strict pullback of the
> structure functor of `𝒳'` along the relocalization functor of `g`.

```lean
def changeOfBase (𝒳' : AlgebraicStacks.{u, w} B S' hS') :
    AlgebraicStacks.{u, w} B S hS
```

**`AlgebraicGeometry.Stack.changeOfBase_twoFibreProductWitness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseStack.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ChangeOfBaseStack.lean#L425). The attribute's comment: “canonical two-fibre-product characterization”.

> Under the canonical 2-categorical correspondence of Stacks 04X5 between algebraic stacks over
> `S` and algebraic stacks over `S'` equipped with a 1-morphism to the stack represented by `S/S'`,
> the change of base of `𝒳'` is the 2-fibre product of `𝒳'` and the stack represented by `S/S'`
> over the stack represented by the final object `S'/S'`.
>
> The two 1-morphisms to the base are the structure functor of `𝒳'` and the forgetful functor of
> `S/S'` read through the iterated-slice equivalence, the apex is the correspondence's image of the
> change of base, the second projection is the correspondence's structural 1-morphism and the first
> is the projection of the strict pullback.

```lean
theorem changeOfBase_twoFibreProductWitness (𝒳' : AlgebraicStacks.{u, w} B S' hS') :
    Nonempty (ChangeOfBaseTwoFibreProductWitness B S S' hS hS' g 𝒳')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 94.19, Tag 04X4](https://stacks.math.columbia.edu/tag/04X4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
