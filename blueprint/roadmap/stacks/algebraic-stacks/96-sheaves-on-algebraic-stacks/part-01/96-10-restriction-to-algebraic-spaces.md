---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.projectionRingedToposHom, AlgebraicGeometry.Space.projectionRingedToposHom_pushforward, AlgebraicGeometry.Space.restrictionFunctor_isContinuous, AlgebraicGeometry.Space.restrictionFunctor_isCocontinuous, AlgebraicGeometry.Space.restrictionToposHom, AlgebraicGeometry.Space.restrictionToposHom_inverseImage, AlgebraicGeometry.Space.inverseImage_structureSheaf_eq, AlgebraicGeometry.Space.restrictionRingedToposHom
statement: formalized
proof: formalized
---

# 96.10 Restriction to algebraic spaces

Section 96.10 of the Stacks Project, [Tag 076P](https://stacks.math.columbia.edu/tag/076P). 7 tags here are carried by 28 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 073M, a lemma

[Tag 073M](https://stacks.math.columbia.edu/tag/073M) in the Stacks Project.

**`AlgebraicGeometry.Space.projectionRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionProjection.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionProjection.lean#L275). The attribute's comment: “the morphism of ringed topoi pi\_F”.

> **Stacks 073M.** The morphism of ringed topoi
> `π_F : (Sh(𝒳_étale), 𝒪_𝒳) ⟶ (Sh(F_étale), 𝒪_F)`: its direct image is restriction along the
> functor `F_étale ⥤ 𝒳`, its inverse image is the left adjoint `g_!` of that restriction, which is
> left exact, and its structure map is the identification of the restricted structure sheaf of
> `𝒳` with the structure sheaf of `F`.

```lean
noncomputable def projectionRingedToposHom (hp : p.IsFiberedInGroupoids)
    (hF : IsAlgebraicSpace B S hS F)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    RingedToposHom (FibredSite.associatedRingedTopos B S hS p hp .etale)
      (smallEtaleRingedTopos B S hS ⟨F, hF⟩)
```

**`AlgebraicGeometry.Space.projectionRingedToposHom_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionProjection.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionProjection.lean#L314). The attribute's comment: “the direct image of pi\_F is restriction along the functor”.

> **Stacks 073M, equation 075K.** The direct image of `π_F` is restriction along the functor
> `F_étale ⥤ 𝒳`, that is, `π_{F,*}ℱ(U) = ℱ(u(U))`.
>
> This is the right-hand identification `ℱ|_{F_étale} = π_{F, *}ℱ` of equation 075K: the
> right-hand side here is the term that `AlgebraicGeometry.Space.restrictionSheafFunctor` names
> `ℱ|_{F_étale}`. The left-hand identification `ℱ|_{F_étale} = i_F^{-1}ℱ` is
> `AlgebraicGeometry.Space.restrictionToposHom_inverseImage`; together they give the chain.

```lean
theorem projectionRingedToposHom_pushforward (hp : p.IsFiberedInGroupoids)
    (hF : IsAlgebraicSpace B S hS F)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    letI := restrictionFunctor_isContinuous B S hS F p hp e
    (projectionRingedToposHom B S hS F p hp hF e).toToposHom.pushforward =
      (restrictionFunctor B S hS F p e).sheafPushforwardContinuous (Type u)
        (SmallEtale.topology B S hS F)
        (BigFppfOver.associatedTopology B S hS p .etale)
```

**`AlgebraicGeometry.Space.restrictionFunctor_isContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean#L213). The attribute's comment: “continuity of the functor from the small étale site of the space”.

> **Stacks 073M.** The functor `F_étale ⥤ 𝒳` is continuous for the étale topology on `𝒳`: it
> preserves fibre products and carries a covering family of étale charts to a covering family of
> the inherited étale topology, the images of its members being strongly cartesian.

```lean
theorem restrictionFunctor_isContinuous (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    (restrictionFunctor B S hS F p e).IsContinuous
      (SmallEtale.topology B S hS F)
      (BigFppfOver.associatedTopology B S hS p .etale)
```

**`AlgebraicGeometry.Space.restrictionFunctor_isCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean, line 333](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean#L333). The attribute's comment: “cocontinuity of the functor from the small étale site of the space”.

> **Stacks 073M.** The functor `F_étale ⥤ 𝒳` is cocontinuous for the étale topology on `𝒳`: a
> covering sieve of the image of a chart pulls back to a covering sieve of that chart, because its
> image under the structure functor already does and the members of a covering sieve of the
> inherited topology are strongly cartesian.

```lean
theorem restrictionFunctor_isCocontinuous (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    (restrictionFunctor B S hS F p e).IsCocontinuous
      (SmallEtale.topology B S hS F)
      (BigFppfOver.associatedTopology B S hS p .etale)
```

**`AlgebraicGeometry.Space.restrictionToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean, line 474](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean#L474). The attribute's comment: “the morphism of topoi i\_F”.

> **Stacks 073M.** The morphism of topoi `i_F : Sh(F_étale) ⟶ Sh(𝒳_étale)` induced by the
> continuous and cocontinuous functor `F_étale ⥤ 𝒳`: its inverse image is restriction along that
> functor and its direct image is the right Kan extension along it.

```lean
noncomputable def restrictionToposHom (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    MorphismOfTopoi (Sheaf (SmallEtale.topology B S hS F) (Type u))
      (Sheaf (BigFppfOver.associatedTopology B S hS p .etale) (Type u))
```

**`AlgebraicGeometry.Space.restrictionToposHom_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean, line 496](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean#L496). The attribute's comment: “the inverse image of i\_F is restriction along the functor”.

> **Stacks 073M, equation 075K.** The inverse image of `i_F` is restriction along the functor
> `F_étale ⥤ 𝒳`. This is the source's `π_{F,*} = i_F^{-1}`: both send a sheaf `ℱ` to
> `U ↦ ℱ(u(U))`.
>
> It is also the left-hand identification `ℱ|_{F_étale} = i_F^{-1}ℱ` of equation 075K, the
> right-hand side of this statement being the term that
> `AlgebraicGeometry.Space.restrictionSheafFunctor` names `ℱ|_{F_étale}`. The right-hand
> identification `ℱ|_{F_étale} = π_{F, *}ℱ` is
> `AlgebraicGeometry.Space.projectionRingedToposHom_pushforward`.

```lean
theorem restrictionToposHom_inverseImage (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    letI := restrictionFunctor_isContinuous B S hS F p hp e
    (restrictionToposHom B S hS F p hp e).inverseImage =
      (restrictionFunctor B S hS F p e).sheafPushforwardContinuous (Type u)
        (SmallEtale.topology B S hS F)
        (BigFppfOver.associatedTopology B S hS p .etale)
```

**`AlgebraicGeometry.Space.inverseImage_structureSheaf_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean, line 535](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean#L535). The attribute's comment: “the restricted structure sheaf of the category is that of the space”.

> **Stacks 073M.** Restriction along the functor `F_étale ⥤ 𝒳` carries the structure sheaf of
> `𝒳` to the structure sheaf of the small étale site of `F`, on the nose: both send a chart to the
> ring of global functions on its underlying scheme.

```lean
theorem inverseImage_structureSheaf_eq (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p)
    (hF : IsAlgebraicSpace B S hS F) :
    letI := restrictionFunctor_isContinuous B S hS F p hp e
    ((restrictionFunctor B S hS F p e).sheafPushforwardContinuous CommRingCat.{u}
      (SmallEtale.topology B S hS F)
      (BigFppfOver.associatedTopology B S hS p .etale)).obj
        (FibredSite.structureSheaf B S hS p hp .etale) = structureSheaf B S hS F hF
```

**`AlgebraicGeometry.Space.restrictionRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean, line 556](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean#L556). The attribute's comment: “the morphism of ringed topoi i\_F”.

> **Stacks 073M.** The morphism of ringed topoi
> `i_F : (Sh(F_étale), 𝒪_F) ⟶ (Sh(𝒳_étale), 𝒪_𝒳)`: the morphism of topoi `i_F` together with the
> identification of the restricted structure sheaf of `𝒳` with the structure sheaf of `F`.

```lean
noncomputable def restrictionRingedToposHom (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p)
    (hF : IsAlgebraicSpace B S hS F) :
    RingedToposHom (smallEtaleRingedTopos B S hS ⟨F, hF⟩)
      (FibredSite.associatedRingedTopos B S hS p hp .etale)
```

**`AlgebraicGeometry.Space.lowerShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean, line 773](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean#L773). The attribute's comment: “the inverse image i\_F! of the morphism of sites”.

> **Stacks 073M.** The inverse image `π_F^{-1} = i_{F,!}` of the source: lower shriek along the
> functor `F_étale ⥤ 𝒳`, the sheafification of the left Kan extension of a sheaf of sets on the
> small étale site of `F`. It is the left adjoint of restriction `i_F^{-1}`.

```lean
noncomputable def lowerShriek (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    Sheaf (SmallEtale.topology B S hS F) (Type u) ⥤
      Sheaf (BigFppfOver.associatedTopology B S hS p .etale) (Type u)
```

**`AlgebraicGeometry.Space.lowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean, line 792](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean#L792). The attribute's comment: “the direct image of the morphism of sites is the inverse image of i\_F”.

> **Stacks 073M.** `π_{F,*} = i_F^{-1}` is right adjoint to `π_F^{-1} = i_{F,!}`.
>
> This is the source's "Moreover `π_{F,*} = i_F^{-1}`": the direct image of `π_F` is restriction
> along the functor `F_étale ⥤ 𝒳`, which is exactly the inverse image of `i_F` recorded by
> `AlgebraicGeometry.Space.restrictionToposHom_inverseImage`.

```lean
noncomputable def lowerShriekAdjunction (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    letI := restrictionFunctor_isContinuous B S hS F p hp e
    lowerShriek B S hS F p hp e ⊣
      (restrictionFunctor B S hS F p e).sheafPushforwardContinuous (Type u)
        (SmallEtale.topology B S hS F)
        (BigFppfOver.associatedTopology B S hS p .etale)
```

**`AlgebraicGeometry.Space.lowerShriek_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean, line 814](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean#L814). The attribute's comment: “left exactness of i\_F! on sheaves of sets”.

> **Stacks 073M.** `i_{F,!}` is left exact on sheaves of sets.
>
> This is the claim the source proves in order to define `π_F`: the small étale site of `F` has
> binary products and fibre products, which the functor `F_étale ⥤ 𝒳` preserves, so the left Kan
> extension is a pointwise filtered colimit and commutes with fibre products; and the images of the
> étale charts cover the final object, which gives `i_{F,!}* = *`.

```lean
theorem lowerShriek_preservesFiniteLimits (hF : IsAlgebraicSpace B S hS F)
    (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    PreservesFiniteLimits (lowerShriek B S hS F p hp e)
```

**`AlgebraicGeometry.Space.lowerShriek_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean, line 832](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean#L832). The attribute's comment: “right exactness of i\_F! on sheaves of sets”.

> **Stacks 073M.** `i_{F,!}` is right exact on sheaves of sets, being a left adjoint.

```lean
theorem lowerShriek_preservesFiniteColimits (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    PreservesFiniteColimits (lowerShriek B S hS F p hp e)
```

**`AlgebraicGeometry.Space.restrictionFunctor_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean, line 844](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean#L844). The attribute's comment: “the functor from the small etale site defines a morphism of sites”.

> **Stacks 073M.** The functor `F_étale ⥤ 𝒳` defines a morphism of sites
> `π_F : 𝒳_étale ⟶ F_étale`: restriction along it has a left exact left adjoint, namely
> `i_{F,!}`.

```lean
theorem restrictionFunctor_isMorphismOfSites (hF : IsAlgebraicSpace B S hS F)
    (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    IsMorphismOfSites.{u} (restrictionFunctor B S hS F p e)
      (SmallEtale.topology B S hS F)
      (BigFppfOver.associatedTopology B S hS p .etale)
```

**`AlgebraicGeometry.Space.lowerShriekAdjunction_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean, line 863](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean#L863). The attribute's comment: “the unit of i\_F! ⊣ i\_F^\{-1} is an isomorphism, so π\_F ∘ i\_F = id”.

> **Stacks 073M.** `π_F ∘ i_F = id`.
>
> The inverse image of the composite is `i_F^{-1} ∘ π_F^{-1} = i_F^{-1} ∘ i_{F,!}`, so the
> composite is the identity exactly when the unit `ℱ ⟶ i_F^{-1} i_{F,!} ℱ` of `i_{F,!} ⊣ i_F^{-1}`
> is an isomorphism. That holds because the functor `F_étale ⥤ 𝒳` is continuous, cocontinuous and
> fully faithful, which presents the small étale topos of `F` as a subtopos of that of `𝒳`.

```lean
theorem lowerShriekAdjunction_unit_isIso (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    letI := restrictionFunctor_isContinuous B S hS F p hp e
    IsIso (lowerShriekAdjunction B S hS F p hp e).unit
```

## Tag 0GQA, a remark

[Tag 0GQA](https://stacks.math.columbia.edu/tag/0GQA) in the Stacks Project.

**`AlgebraicGeometry.Space.etaleLocalizationRingedSquares`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionEtaleLocalization.lean, line 480](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionEtaleLocalization.lean#L480). The attribute's comment: “both squares of the diagram formed by i\_F, i\_G, pi\_F, pi\_G, f and f\_small commute as diagrams of ringed topoi, for an etale induced morphism f : F -> G”.

> **Stacks 0GQA.** Let `f : 𝒳 ⥤ 𝒴` be a morphism of categories fibred in groupoids over
> `(Sch/S)_{fppf}`, with `𝒳` and `𝒴` representable by algebraic spaces `F` and `G` through the
> chosen equivalences `eF` and `eG`, such that the induced morphism of algebraic spaces
> `f : F ⟶ G` (`AlgebraicGeometry.Space.inducedSpacesHom`) is étale, and let `f_small` be the
> corresponding morphism of small étale ringed topoi
> (`AlgebraicGeometry.Space.smallEtaleRingedToposHom`). Then the diagram
> ```
> (Sh(F_étale), 𝒪_F) --f_small--> (Sh(G_étale), 𝒪_G)
>        |                              |
>       i_F                            i_G
>        v                              v
> (Sh(𝒳_étale), 𝒪_𝒳) -----f-----> (Sh(𝒴_étale), 𝒪_𝒴)
>        |                              |
>       π_F                            π_G
>        v                              v
> (Sh(F_étale), 𝒪_F) --f_small--> (Sh(G_étale), 𝒪_G)
> ```
> is a commutative diagram of ringed topoi: the first component is a 2-isomorphism (Stacks 04IC)
> `f ∘ i_F ≅ i_G ∘ f_small` of morphisms of ringed topoi, the second a 2-isomorphism
> `π_G ∘ f ≅ f_small ∘ π_F`. Here `i_F`, `i_G` are
> `AlgebraicGeometry.Space.restrictionRingedToposHom` and `π_F`, `π_G` are
> `AlgebraicGeometry.Space.projectionRingedToposHom` (Stacks 073M), and the middle arrow is
> `AlgebraicGeometry.FibredSite.ringedToposMorphism` (Stacks 06TW), whose direct image exists by
> `AlgebraicGeometry.Space.hasPointwiseRightKanExtension_op_of_equivalenceOver`.

```lean
noncomputable def etaleLocalizationRingedSquares
    (hg : IsEtale B S hS
      (inducedSpacesHom B S hS (X := ⟨F, hF⟩) (Y := ⟨G, hG⟩) p q eF eG f hf.comp_eq).hom) :
    letI : ∀ P : 𝒳ᵒᵖ ⥤ Type u, f.op.HasPointwiseRightKanExtension P :=
      hasPointwiseRightKanExtension_op_of_equivalenceOver B S hS F p G q eF eG f
    RingedToposHom.TwoIso (A := smallEtaleRingedTopos B S hS ⟨F, hF⟩)
        (B := FibredSite.associatedRingedTopos B S hS q hq .etale)
        (etaleSquareFibredLeg B S hS F p q hp hq hF eF f hf)
        (etaleSquareSpaceLeg B S hS F G p q hq hF hG eF eG f hf) ×
      RingedToposHom.TwoIso (A := FibredSite.associatedRingedTopos B S hS p hp .etale)
        (B := smallEtaleRingedTopos B S hS ⟨G, hG⟩)
        (restrictionSquareFibredLeg B S hS G p q hp hq hG eG f hf)
        (restrictionSquareSpaceLeg B S hS F G p hp hF hG eF
          (inducedSpacesHom B S hS (X := ⟨F, hF⟩) (Y := ⟨G, hG⟩) p q eF eG f hf.comp_eq))
```

## Tag 075K, an equation

[Tag 075K](https://stacks.math.columbia.edu/tag/075K) in the Stacks Project.

**`AlgebraicGeometry.Space.moduleRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionAlgebraicSpace.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionAlgebraicSpace.lean#L184). The attribute's comment: “the restriction of a module to the small étale site of the representing space”.

> The restriction `ℱ|_{X_étale} = i_X^*ℱ = π_{X,*}ℱ` of an `𝒪_𝒳`-module on the inherited étale
> site of a category fibred in groupoids representable by the algebraic space `X`, as an
> `𝒪_X`-module on the small étale site of `X`: the pushforward along the continuous functor
> `u_X : X_étale ⥤ 𝒳` of Stacks 073M, with coefficient homomorphism
> `AlgebraicGeometry.Space.restrictionStructureHom`.

```lean
noncomputable def moduleRestriction :
    SheafOfModules.{m} (FibredSite.ringStructureSheafCore B S hS p hp .etale) ⥤
      Modules.{u, m} B S hS X.1 X.2
```

**`AlgebraicGeometry.Space.projectionRingedToposHom_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionProjection.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionProjection.lean#L314). The attribute's comment: “the identification `ℱ|_{F_étale} = π_{F, *}ℱ`”.

> **Stacks 073M, equation 075K.** The direct image of `π_F` is restriction along the functor
> `F_étale ⥤ 𝒳`, that is, `π_{F,*}ℱ(U) = ℱ(u(U))`.
>
> This is the right-hand identification `ℱ|_{F_étale} = π_{F, *}ℱ` of equation 075K: the
> right-hand side here is the term that `AlgebraicGeometry.Space.restrictionSheafFunctor` names
> `ℱ|_{F_étale}`. The left-hand identification `ℱ|_{F_étale} = i_F^{-1}ℱ` is
> `AlgebraicGeometry.Space.restrictionToposHom_inverseImage`; together they give the chain.

```lean
theorem projectionRingedToposHom_pushforward (hp : p.IsFiberedInGroupoids)
    (hF : IsAlgebraicSpace B S hS F)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    letI := restrictionFunctor_isContinuous B S hS F p hp e
    (projectionRingedToposHom B S hS F p hp hF e).toToposHom.pushforward =
      (restrictionFunctor B S hS F p e).sheafPushforwardContinuous (Type u)
        (SmallEtale.topology B S hS F)
        (BigFppfOver.associatedTopology B S hS p .etale)
```

**`AlgebraicGeometry.Space.restrictionToposHom_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean, line 496](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean#L496). The attribute's comment: “the identification `ℱ|_{F_étale} = i_F^{-1}ℱ`”.

> **Stacks 073M, equation 075K.** The inverse image of `i_F` is restriction along the functor
> `F_étale ⥤ 𝒳`. This is the source's `π_{F,*} = i_F^{-1}`: both send a sheaf `ℱ` to
> `U ↦ ℱ(u(U))`.
>
> It is also the left-hand identification `ℱ|_{F_étale} = i_F^{-1}ℱ` of equation 075K, the
> right-hand side of this statement being the term that
> `AlgebraicGeometry.Space.restrictionSheafFunctor` names `ℱ|_{F_étale}`. The right-hand
> identification `ℱ|_{F_étale} = π_{F, *}ℱ` is
> `AlgebraicGeometry.Space.projectionRingedToposHom_pushforward`.

```lean
theorem restrictionToposHom_inverseImage (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    letI := restrictionFunctor_isContinuous B S hS F p hp e
    (restrictionToposHom B S hS F p hp e).inverseImage =
      (restrictionFunctor B S hS F p e).sheafPushforwardContinuous (Type u)
        (SmallEtale.topology B S hS F)
        (BigFppfOver.associatedTopology B S hS p .etale)
```

**`AlgebraicGeometry.Space.restrictionSheafFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean, line 509](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean#L509).

> **Stacks 073M, equation 075K.** The restriction `ℱ|_{F_étale} = i_F^{-1}ℱ` of a sheaf on the
> inherited étale site of `𝒳` to the small étale site of the algebraic space `F`.

```lean
noncomputable abbrev restrictionSheafFunctor (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    letI := restrictionFunctor_isContinuous B S hS F p hp e
    Sheaf (BigFppfOver.associatedTopology B S hS p .etale) (Type u) ⥤
      Sheaf (SmallEtale.topology B S hS F) (Type u)
```

**`AlgebraicGeometry.Space.restrictionSheafFunctor_obj_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean, line 522](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionToAlgebraicSpace.lean#L522). The attribute's comment: “sections of a restriction”.

> **Stacks 073M, equation 075K.** The sections of a restriction are the sections of the
> original sheaf on the image of the chart: `ℱ|_{F_étale}(U) = ℱ(u(U))`.

```lean
theorem restrictionSheafFunctor_obj_obj (hp : p.IsFiberedInGroupoids)
    (e : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (F ⋙ typeToCat)).p)
    (𝓕 : Sheaf (BigFppfOver.associatedTopology B S hS p .etale) (Type u))
    (U : SmallEtale B S hS F) :
    ((restrictionSheafFunctor B S hS F p hp e).obj 𝓕).obj.obj (Opposite.op U) =
      𝓕.obj.obj (Opposite.op ((restrictionFunctor B S hS F p e).obj U))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.projectionPushforward`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionProjection.lean#L327), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionTags.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionTags.lean#L52) (StacksFrontier): “the direct image pi\_\{F,*}”.
- [`AlgebraicGeometry.Space.restrictionSheafFunctor_eq_projectionPushforward`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionProjection.lean#L338), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionTags.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionTags.lean#L54) (StacksFrontier): “the restriction is the direct image along pi\_F”.
- [`AlgebraicGeometry.Space.restrictionSheafFunctor_eq_restrictionToposHom_inverseImage`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionProjection.lean#L352), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionTags.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionTags.lean#L57) (StacksFrontier): “the restriction is the inverse image along i\_F”.
- [`AlgebraicGeometry.Space.projectionPushforward_obj_obj`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionProjection.lean#L364), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionTags.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentRestrictionTags.lean#L60) (StacksFrontier): “sections of the direct image along pi\_F”.

## Tag 073N, a lemma

[Tag 073N](https://stacks.math.columbia.edu/tag/073N) in the Stacks Project.

**`AlgebraicGeometry.Space.restrictionRingedSquareTwoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionRingedSquareCommutes.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionRingedSquareCommutes.lean#L104). The attribute's comment: “the square of ringed topoi formed by pi\_F, pi\_G, the morphism induced by f and f\_small commutes: its two composites are 2-isomorphic morphisms of ringed topoi”.

> Let `f : 𝒳 ⥤ 𝒴` be a morphism of categories fibred in groupoids over `(Sch/S)_{fppf}`,
> with `𝒳` and `𝒴` representable by algebraic spaces `F` and `G` through the chosen equivalences
> `eF` and `eG`. Write `f : F ⟶ G` for the induced morphism of algebraic spaces
> (`AlgebraicGeometry.Space.inducedSpacesHom`) and `f_small` for the corresponding morphism of
> small étale ringed topoi (`AlgebraicGeometry.Space.smallEtaleRingedToposHom`). Then the square
> ```
> (Sh(𝒳_étale), 𝒪_𝒳) ---f---> (Sh(𝒴_étale), 𝒪_𝒴)
>        |                            |
>       π_F                          π_G
>        v                            v
> (Sh(F_étale), 𝒪_F) --f_small--> (Sh(G_étale), 𝒪_G)
> ```
> is a commutative diagram of ringed topoi: this is a 2-isomorphism of morphisms of ringed topoi
> (Stacks 04IC) between its two composites `π_G ∘ f`
> (`AlgebraicGeometry.Space.restrictionSquareFibredLeg`) and `f_small ∘ π_F`
> (`AlgebraicGeometry.Space.restrictionSquareSpaceLeg`), where `π_F` and `π_G` are the morphisms of
> ringed topoi of Stacks 073M and the upper arrow is the morphism of ringed topoi of Stacks 06TW.
>
> Its underlying isomorphism `π_{G,*}f_* ≅ f_{small,*}π_{F,*}` is the canonical comparison map of
> equation 075M, which is invertible by
> `AlgebraicGeometry.Space.isIso_restrictedDirectImageComparison`, and its compatibility with the
> structure sheaves is
> `AlgebraicGeometry.Space.restrictedDirectImageComparison_structureSheafCompatible`. The direct
> image `f_*` exists with no size hypothesis, by
> `AlgebraicGeometry.Space.hasPointwiseRightKanExtension_op_of_equivalenceOver`.

```lean
noncomputable def restrictionRingedSquareTwoIso :
    letI : ∀ P : 𝒳ᵒᵖ ⥤ Type u, f.op.HasPointwiseRightKanExtension P :=
      hasPointwiseRightKanExtension_op_of_equivalenceOver B S hS F p G q eF eG f
    RingedToposHom.TwoIso
      (A := FibredSite.associatedRingedTopos B S hS p hp .etale)
      (B := smallEtaleRingedTopos B S hS ⟨G, hG⟩)
      (restrictionSquareFibredLeg B S hS G p q hp hq hG eG f hf)
      (restrictionSquareSpaceLeg B S hS F G p hp hF hG eF
        (inducedSpacesHom B S hS (X := ⟨F, hF⟩) (Y := ⟨G, hG⟩) p q eF eG f hf.comp_eq))
```

## Tag 075M, an equation

[Tag 075M](https://stacks.math.columbia.edu/tag/075M) in the Stacks Project.

**`AlgebraicGeometry.Space.restrictedDirectImageChartEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionDirectImage.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionDirectImage.lean#L204). The attribute's comment: “the left-hand side, as sections over the 2-fibre product at a chart”.

> **Equation 075M, left-hand side.** The sections of the restriction `(f_*ℱ)|_{G_étale}` of a
> direct image to the small étale site of the algebraic space `G` representing `𝒴`, at a chart `V`
> of `G`, are the global sections of the pullback of `ℱ` to the 2-fibre product
> `(Sch/V)_{fppf} ×_{u_G V, 𝒴} 𝒳`.
>
> This is the opening display of the source's proof of Stacks 073N, from which equation 075M is
> drawn: `π_{G,*}f_*ℱ(V) = f_*ℱ(V/G) = Γ((Sch/V)_{fppf} ×_𝒴 𝒳, pr^{-1}ℱ)`. The first step is
> equation 075K, that restriction is evaluation at `u_G V`; the second is Stacks 06W6.
>
> Only the left-hand side of 075M is covered. Identifying these sections with those of
> `f_{small,*}(ℱ|_{F_étale})` is the content of Stacks 073N, which is not proved in this library;
> the implementation notes of this file say which input to the identification is still
> missing.
> Accordingly `𝒳` is an arbitrary category fibred in groupoids here, with no representability
> assumed of it.

```lean
noncomputable def restrictedDirectImageChartEquiv (hp : p.IsFiberedInGroupoids)
    (hq : q.IsFiberedInGroupoids)
    (eG : StacksRepresentableCFG.EquivalenceOver q (presheafOfCategories (G ⋙ typeToCat)).p)
    (f : 𝒳 ⥤ 𝒴) (hf : p.IsFibredOneMorphism q f) (c : q.ChoiceOfPullbacks)
    [∀ H : 𝒳ᵒᵖ ⥤ Type u, f.op.HasPointwiseRightKanExtension H]
    (ℱ : Sheaf (BigFppfOver.associatedTopology B S hS p .etale) (Type u))
    (V : SmallEtale B S hS G) :
    ((restrictionSheafFunctor B S hS G q hq eG).obj
        ((etaleDirectImage B S hS p q hp f hf).obj ℱ)).obj.obj (op V) ≃
      Presheaf.globalSections
        ((TwoFibreProductOver.snd (Over.forget ((SmallEtale.toOver B S hS G).obj V)) p q
          (c.sliceFunctor (chartFiberObj B S hS G q eG V)) f).op ⋙ ℱ.obj)
```

**`AlgebraicGeometry.Space.restrictedDirectImageComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionDirectImageComparison.lean, line 585](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionDirectImageComparison.lean#L585). The attribute's comment: “the comparison map between the two sides, natural in the sheaf: both sides of the equation are present -- the left-hand side `(f_*F)|_{G_etale}` as the direct image of `restrictionSquareFibredLeg` and the right-hand side `f_{small,*}(F|_{F_etale})` as that of `restrictionSquareSpaceLeg` -- together with the canonical map from the first to the second and its naturality in the sheaf. That this map is an ISOMORPHISM, which is what the displayed equality asserts, is `isIso_restrictedDirectImageComparison` of StacksFrontier/AlgebraicGeometry/Stacks/RestrictionDirectImageComparisonIso.lean, which reduces it by `isIso_restrictedDirectImageComparison_of_bijective` to a bijection on sections over one etale scheme chart of G at a time. The compatibility `ha` of the 1-morphism f with the morphism fSpace of algebraic spaces through the two chosen presentations is a hypothesis; it is realized for every fSpace by `exists_comparisonChartFunctorIso`”.

> **Equation 075M.** The comparison of the two direct images around the square of
> Stacks 073N: the canonical map `π_{G,*}f_*ℱ ⟶ f_{small,*}(ℱ|_{F_étale})`, natural in `ℱ`, whose
> source is the left-hand side `(f_*ℱ)|_{G_étale}` of equation 075M and whose target is its
> right-hand side.
>
> Its value on sections over a diagram of étale scheme charts is
> `AlgebraicGeometry.Space.restrictedDirectImageComparisonSections`. That it is an isomorphism,
> which is what the displayed equality of the source asserts, is
> `AlgebraicGeometry.Space.isIso_restrictedDirectImageComparison` of
> `StacksFrontier/AlgebraicGeometry/Stacks/RestrictionDirectImageComparisonIso.lean`.

```lean
noncomputable def restrictedDirectImageComparison :
    (restrictionSquareFibredLeg B S hS G p q hp hq hG eG f hf).toToposHom.pushforward ⟶
      (restrictionSquareSpaceLeg B S hS F G p hp hF hG eF fSpace).toToposHom.pushforward
```

**`AlgebraicGeometry.Space.exists_restrictedDirectImageComparisonTarget_equalizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionDirectImageComparison.lean, line 615](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionDirectImageComparison.lean#L615). The attribute's comment: “the right-hand side f\_\{small,*}(F|\_\{F\_etale}), as an equalizer of sections of F|\_\{F\_etale} over two etale scheme charts of F, at a chart V of G”.

> **The right-hand side of equation 075M at a chart, as an equalizer.**  The target of the
> comparison map is `f_{small,*}(ℱ|_{F_étale})`; its sections over an étale scheme chart `V` of
> `G` are the equalizer of the sections of `ℱ|_{F_étale}` over an étale scheme chart `W` of `F`
> covering `F ×_G V` and over a chart `W'` presenting the self-fibre product of `W` over
> `F ×_G V`.
>
> This is `AlgebraicGeometry.Space.exists_smallEtaleDirectImageChartEqualizerEquiv` — Tag 03H7 for
> the direct image on the small étale sites — specialized at the chart of equation 075M.  The
> target of the comparison is that direct image on the nose: the direct image of the geometric
> morphism underlying `AlgebraicGeometry.Space.smallEtaleRingedToposHom` is the spaces-étale
> direct image of Stacks 03G2 conjugated by the comparison equivalences of Stacks 03G1, which is
> how `AlgebraicGeometry.Space.smallEtaleDirectImage` is defined.

```lean
theorem exists_restrictedDirectImageComparisonTarget_equalizer
    (ℱ : Sheaf (BigFppfOver.associatedTopology B S hS p .etale) (Type u))
    (V : SmallEtale B S hS G) :
    ∃ (W W' : SmallEtale B S hS F) (a b : W' ⟶ W),
      Nonempty (((smallEtaleRingedToposHom B S hS fSpace).toToposHom.pushforward.obj
            ((restrictionSheafFunctor B S hS F p hp eF).obj ℱ)).obj.obj (op V) ≃
        {y : ((restrictionSheafFunctor B S hS F p hp eF).obj ℱ).obj.obj (op W) //
          ((restrictionSheafFunctor B S hS F p hp eF).obj ℱ).obj.map a.op y =
            ((restrictionSheafFunctor B S hS F p hp eF).obj ℱ).obj.map b.op y})
```

**`AlgebraicGeometry.Space.isIso_restrictedDirectImageComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionDirectImageComparisonIso.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionDirectImageComparisonIso.lean#L399). The attribute's comment: “the displayed equality itself: the canonical comparison map between the two sides is an isomorphism”.

> **Equation 075M.** The canonical comparison map of equation 075M,
> `AlgebraicGeometry.Space.restrictedDirectImageComparison`, is an **isomorphism**: the two sides
> of the equation,
> ```
> (f_*ℱ)|_{G_étale} = f_{small,*}(ℱ|_{F_étale}),
> ```
> agree, naturally in the sheaf, through that canonical map.
>
> Invertibility is reduced to a bijection on sections over each étale scheme chart `V` of `G` by
> `AlgebraicGeometry.Space.isIso_restrictedDirectImageComparison_of_bijective`, and there:
>
> * **injectivity** is
>   `AlgebraicGeometry.Space.injective_restrictedDirectImageComparisonHom_app`. A section of
>   `f_*ℱ` over `u_G V` is determined by its values at the pairs `(Z, κ : f(Z) ⟶ u_G V)` (Stacks
>   06W6), the chart correspondence of Stacks 03G8 determines those values at the morphisms out of
>   the image of an étale chart of `F`, and the factorization lemma together with the sheaf
>   condition on `ℱ` carries that to all of them.
> * **surjectivity** is
>   `AlgebraicGeometry.Space.surjective_restrictedDirectImageComparisonHom_app`. The canonical
>   restrictions of a section of the right-hand side to the diagrams of étale scheme charts over
>   `V` form a family which the refinement of two chart diagrams shows compatible, the sheaf
>   condition on `ℱ` glues that family to a value at every pair `(Z, κ)`, and those values are the
>   components of a global section over the 2-fibre product `(Sch/V)_{fppf} ×_𝒴 𝒳` — a section of
>   the left-hand side. It is carried to the given section because a section of the right-hand side
>   is determined by its restriction to one diagram whose chart covers the cartesian base change
>   `F ×_G V`, which is Properties of Spaces 03H7.
>
> The choice of pullbacks that the pushforward formula of Stacks 06W6 needs is not a hypothesis: a
> category fibred in groupoids admits one.

```lean
theorem isIso_restrictedDirectImageComparison :
    IsIso (restrictedDirectImageComparison B S hS F G p q hp hq hF hG eF eG f hf fSpace ha)
```

**`AlgebraicGeometry.Space.exists_restrictedDirectImageComparisonSource_equalizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionDirectImageLeftEqualizer.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionDirectImageLeftEqualizer.lean#L363). The attribute's comment: “the left-hand side (f\_*F)|\_\{G\_etale}, as an equalizer of sections of F over two objects of the 2-fibre product (Sch/V)\_fppf x\_Y X, at a chart V of G. This is the counterpart of exists\_restrictedDirectImageComparisonTarget\_equalizer, which is the right-hand side at the same chart; with both sides presented the comparison map is a map of equalizer diagrams. The representability of the 2-fibre product by an algebraic space over S -- the identification of (Sch/V)\_fppf x\_Y X with the split category fibred in groupoids of V x\_G F that the source's proof of Tag 073N makes -- is supplied by exists\_isAlgebraicSpace\_twoFibreProductStructureFunctor from the presentations of X and Y alone”.

> **Equation 075M, the left-hand side at a chart, as an equalizer.** The sections of
> `(f_*ℱ)|_{G_étale}` over an étale scheme chart `V` of `G` are the equalizer of the sections of `ℱ`
> over two objects of the 2-fibre product `(Sch/V)_{fppf} ×_𝒴 𝒳`, namely an object `A` coming from
> an étale scheme chart of an algebraic space representing that 2-fibre product and the object
> presenting the self-product of `A`.
>
> This is the counterpart of
> `AlgebraicGeometry.Space.exists_restrictedDirectImageComparisonTarget_equalizer`, which presents
> the *right*-hand side at the same chart as an equalizer of sections of `ℱ|_{F_étale}` over two
> étale scheme charts of `F`. With both sides presented, the comparison map of equation 075M is a map
> between two equalizer diagrams, which is the shape in which the source proves it invertible.
>
> The hypotheses are those of equation 075M itself: `𝒳` and `𝒴` are presented by the algebraic
> spaces `F` and `G` and `f` is a 1-morphism of fibred categories between them. The
> representability of the 2-fibre product that the equalizer presentation needs — the identification
> the source makes in its proof of Stacks 073N — is supplied by
> `AlgebraicGeometry.Space.exists_isAlgebraicSpace_twoFibreProductStructureFunctor`, and the
> equalizer itself by `exists_restrictedDirectImageComparisonSource_equalizer_of_equivalenceOver`.

```lean
theorem exists_restrictedDirectImageComparisonSource_equalizer
    (Fpsh : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hFpsh : IsAlgebraicSpace B S hS Fpsh)
    (eFpsh : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (Fpsh ⋙ typeToCat)).p)
    (hG : IsAlgebraicSpace B S hS G) (hf : p.IsFibredOneMorphism q f)
    [∀ H : 𝒳ᵒᵖ ⥤ Type u, f.op.HasPointwiseRightKanExtension H]
    (ℱ : Sheaf (BigFppfOver.associatedTopology B S hS p .etale) (Type u))
    (V : SmallEtale B S hS G) :
    ∃ (A A' : TwoFibreProductOver (Over.forget ((SmallEtale.toOver B S hS G).obj V)) p q
          (c.sliceFunctor (chartFiberObj B S hS G q eG V)) f) (a b : A' ⟶ A),
      Nonempty (((restrictionSheafFunctor B S hS G q hq eG).obj
            ((etaleDirectImage B S hS p q hp f hf).obj ℱ)).obj.obj (op V) ≃
        {y : ℱ.obj.obj (op ((twoFibreProductSnd B S hS G p q eG f c V).obj A)) //
          ℱ.obj.map ((twoFibreProductSnd B S hS G p q eG f c V).map a).op y =
            ℱ.obj.map ((twoFibreProductSnd B S hS G p q eG f c V).map b).op y})
```

## Tag 076Q, an equation

[Tag 076Q](https://stacks.math.columbia.edu/tag/076Q) in the Stacks Project.

**`AlgebraicGeometry.Space.comparisonAlgebraicSpaces`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionComparisonAlgebraicSpace.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionComparisonAlgebraicSpace.lean#L425). The attribute's comment: “the comparison map of a 2-commutative triangle, on sheaves of sets”.

> The comparison map
>
> ```
> c_φ : a_small⁻¹(g⁻¹ℱ|_{V_étale}) ⟶ f⁻¹ℱ|_{U_étale}
> ```
>
> of a 2-commutative triangle `φ : a ⋙ g ≅ f` of 1-morphisms of categories fibred in groupoids
> over `(Sch/S)_{fppf}` whose two source categories `𝒰`, `𝒱` are representable by algebraic spaces
> `U`, `V`, for a sheaf `ℱ` on the inherited étale site of `𝒳`.
>
> Here `a_small` is the morphism of small étale topoi attached to the morphism `aSpace : U ⟶ V`
> of algebraic spaces corresponding to `a`, and `c_φ` is the adjoint, under
> `a_small⁻¹ ⊣ a_{small,*}`, of `AlgebraicGeometry.Space.comparisonPushforwardHom`.

```lean
noncomputable def comparisonAlgebraicSpaces
    (ℱ : Sheaf (BigFppfOver.associatedTopology B S hS r .etale) (Type u)) :
    (smallToposMorphismTypeU B S hS aSpace).inverseImage.obj
        (etaleRestrictedInverseImage B S hS q r hq eV g hg ℱ) ⟶
      etaleRestrictedInverseImage B S hS p r hp eU f hf ℱ
```

## Tag 076R, an equation

[Tag 076R](https://stacks.math.columbia.edu/tag/076R) in the Stacks Project.

**`AlgebraicGeometry.Space.comparisonAlgebraicSpacesModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RestrictionComparisonAlgebraicSpace.lean, line 605](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RestrictionComparisonAlgebraicSpace.lean#L605). The attribute's comment: “the comparison map of a 2-commutative triangle, on modules”.

> The comparison map
>
> ```
> c_φ : a_small^*(g^*ℱ|_{V_étale}) ⟶ f^*ℱ|_{U_étale}
> ```
>
> of a 2-commutative triangle `φ : a ⋙ g ≅ f` of 1-morphisms of categories fibred in groupoids
> over `(Sch/S)_{fppf}` whose two source categories `𝒰`, `𝒱` are representable by algebraic
> spaces `U`, `V`, for an `𝒪_𝒳`-module `ℱ` on the inherited étale site of `𝒳`.
>
> Here `a_small^*` is the inverse image of modules (`AlgebraicGeometry.Space.modulePullback`)
> for the morphism `aSpace : U ⟶ V` of algebraic spaces corresponding to `a`, and `c_φ` is the
> adjoint, under `a_small^* ⊣ a_{small,*}`, of
> `AlgebraicGeometry.Space.moduleComparisonPushforwardHom`.

```lean
noncomputable def comparisonAlgebraicSpacesModules
    (ℱ : inheritedEtaleModules B S hS r hr) :
    (modulePullback B S hS aSpace).obj
        (etaleRestrictedModuleInverseImage B S hS q r hq hr eV g hg ℱ) ⟶
      etaleRestrictedModuleInverseImage B S hS p r hp hr eU f hf ℱ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.10, Tag 076P](https://stacks.math.columbia.edu/tag/076P)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
