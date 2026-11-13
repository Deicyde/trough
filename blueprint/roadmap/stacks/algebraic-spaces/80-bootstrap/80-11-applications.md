---
declaration: section
origin: cited
lean: AlgebraicGeometry.isAlgebraicSpace_of_isCovering, AlgebraicGeometry.isAlgebraicSpace_of_isCovering_of_isFiniteType, AlgebraicGeometry.Space.Descent.DescentData.isEffective_of_countable, AlgebraicGeometry.Space.Descent.DescentData.isEffective_of_isFiniteType, AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_of_comp_of_flat_surjective_unconditional, AlgebraicGeometry.Stack.isAlgebraicSpace_isomPresheaf, AlgebraicGeometry.Space.isSurjective_toQuotientSheaf, AlgebraicGeometry.Space.isFlat_toQuotientSheaf
statement: formalized
proof: formalized
---

# 80.11 Applications

Section 80.11 of the Stacks Project, [Tag 04SJ](https://stacks.math.columbia.edu/tag/04SJ). 8 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04SK, a lemma

[Tag 04SK](https://stacks.math.columbia.edu/tag/04SK) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicSpace_of_isCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringRestrictionCoproduct.lean, line 777](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoveringRestrictionCoproduct.lean#L777).

> **Stacks 04SK**.
>
> Let `F` be a presheaf of sets on the big fppf site of `S` and let `{S i → S}` be a covering
> family of the base. Assume
>
> 1. `F` is a sheaf (`hF`);
> 2. each restriction `F_i = h_{S i} × F` is an algebraic space (`hFi`);
> 3. the coproduct `∐ F_i` is an algebraic space: `G`, presented by the colimit cofan `hcoprod`
>    with legs `ι`, is a coproduct of the `F_i` in sheaves, and it is an algebraic space (`hG`).
>
> Then `F` is an algebraic space.
>
> The coproduct in (3) is given as data because the index type of the covering is of the next
> universe, so a coproduct of the `F_i` need not exist in sheaves of `Type u`; any two coproducts
> are isomorphic, so this is the source's hypothesis.
>
> The source's proof applies Stacks 04S6 to `∐ F_i ⟶ F`, the base change of `∐ S_i ⟶ S`. Inside
> the site this chart is built from a refinement of the covering of size bounded by `S`, which is
> `AlgebraicGeometry.isAlgebraicSpace_of_isCovering_of_atlas_size_le`; what that lemma asks for is
> a bounded étale atlas of the restriction of each `F_i` to an affine open `W` of `S_i`, and
> hypothesis (3) is exactly what supplies it. An étale atlas `U` of `∐ F_i` splits along the
> coproduct into étale atlases `U_i` of the `F_i`, which are open in `U`
> (`AlgebraicGeometry.Sheaf.exists_clopen_decomposition_of_isColimit_cofan`). The restriction of
> `F_i` to `W` is the base change of `F_i` along `W ⟶ S_i`, so `W ×_{S_i} U_i` is an étale atlas
> of it, of size at most `max (size S) (size U)`.
>
> The last step is Stacks 04S6, condition (3), for a chart representable by objects of the site:
> a sheaf which receives a representable, surjective, flat, locally finitely presented morphism
> from an algebraic space is an algebraic space.

```lean
theorem isAlgebraicSpace_of_isCovering
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : Presheaf.IsSheaf (BigFppfOver.topology B S hS) F)
    (E : PreZeroHypercover.{u + 1} (Over.mk (𝟙 (B.obj hS))))
    (hE : BigFppfOver.IsCovering B S hS ⟨Over.mk (𝟙 (B.obj hS)), E⟩)
    (hFi : ∀ i : E.I₀, IsAlgebraicSpace B S hS (yoneda.obj (E.X i) ⨯ F))
    {G : Sheaf (BigFppfOver.topology B S hS) (Type u)}
    (ι : ∀ i : E.I₀, (⟨yoneda.obj (E.X i) ⨯ F, (hFi i).isSheaf⟩ :
      Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ G)
    (hcoprod : IsColimit (Cofan.mk G ι))
    (hG : IsAlgebraicSpace B S hS G.obj) :
    IsAlgebraicSpace B S hS F
```

## Tag 04U0, a lemma

[Tag 04U0](https://stacks.math.columbia.edu/tag/04U0) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicSpace_of_isCovering_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringRestrictionFiniteType.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoveringRestrictionFiniteType.lean#L135).

> Let `F` be a presheaf of sets on the big fppf site of `S` and let `{S i → S}` be a covering
> family of the base, and assume
>
> 1. `F` is a sheaf (`hF`);
> 2. each restriction `h_{S i} × F` is an algebraic space (`hFi`);
> 3. each restriction is of finite type over its member (`hft`).
>
> Then `F` is an algebraic space.
>
> The refinement of the covering by affines over the points of `S`, Stacks 02WQ and the final
> appeal to Stacks 04S6 are `AlgebraicGeometry.isAlgebraicSpace_of_isCovering_of_atlas_size_le`.
> What this proof adds is the bounded atlas it asks for: the restriction of `h_{S i} × F` to an
> affine open `W` of `S i` is of finite type over `W`, hence quasi-compact, hence has an affine
> étale atlas (Stacks 03H6), which is locally of finite type over `S` and so of size at most
> `size (S)` (Stacks 04T7).

```lean
theorem isAlgebraicSpace_of_isCovering_of_isFiniteType
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : Presheaf.IsSheaf (BigFppfOver.topology B S hS) F)
    (E : PreZeroHypercover.{u + 1} (Over.mk (𝟙 (B.obj hS))))
    (hE : BigFppfOver.IsCovering B S hS ⟨Over.mk (𝟙 (B.obj hS)), E⟩)
    (hFi : ∀ i : E.I₀, IsAlgebraicSpace B S hS (yoneda.obj (E.X i) ⨯ F))
    (hft : ∀ i : E.I₀, Space.IsFiniteType B S hS
      (prod.fst : yoneda.obj (E.X i) ⨯ F ⟶ yoneda.obj (E.X i))) :
    IsAlgebraicSpace B S hS F
```

## Tag 0ADV, a lemma

[Tag 0ADV](https://stacks.math.columbia.edu/tag/0ADV) in the Stacks Project.

**`AlgebraicGeometry.Space.Descent.DescentData.isEffective_of_countable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/EffectiveCountableCovering.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/EffectiveCountableCovering.lean#L207). The attribute's comment: “part (1): countable index set”.

> **Stacks 0ADV, part (1).** Let `{f i : X i ⟶ T}` be an fppf covering of algebraic spaces
> over `S` whose index type is countable. Then every descent datum for algebraic spaces relative
> to it is effective.

```lean
theorem isEffective_of_countable (hcov : IsFppfCovering B S hS X f) : D.IsEffective
```

**`AlgebraicGeometry.Space.Descent.DescentData.isEffective_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/EffectiveFiniteTypeCovering.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/SpacesOverSpaces/EffectiveFiniteTypeCovering.lean#L325). The attribute's comment: “part (2): finite type, index set of any size”.

> **Stacks 0ADV, part (2).** Let `{f i : X i ⟶ T}` be an fppf covering of algebraic spaces
> over `S`, indexed by a type of any size. Then every descent datum `(Y i, φ i j)` relative to it
> with each `Y i ⟶ X i` of finite type is effective.
>
> The proof is the source's. The sheaf `F` of Stacks 0ADT the datum descends to has
> `X i ×_T F = Y i`. Refine the covering by an fppf covering `{R k ⟶ T}` by affine objects of
> the site, with the index type and the sizes of the members bounded by the size `μ` of an atlas
> of `T`
> (`AlgebraicGeometry.Space.exists_affine_refinement_of_isFppfCovering`, which uses Stacks 042T).
> If `R k ⟶ T` factors through `X i`, then `R k ×_T F = R k ×_{X i} Y i` is of finite type over
> the affine `R k`. So it has an atlas of size at most `size (R k) ≤ μ` by Stacks 04T7
> (`AlgebraicGeometry.Space.exists_atlas_size_le_of_isFiniteType`). This is the size bound the
> source draws from Stacks 04U0. Stacks 02WQ then makes the coproducts `∐ R k` and
> `∐ (R k ×_T F)` algebraic spaces, and Stacks 04S6 makes `F` an algebraic space.

```lean
theorem isEffective_of_isFiniteType (hcov : IsFppfCovering B S hS X f)
    (hft : ∀ i, IsFiniteType B S hS (D.obj i).hom) : D.IsEffective
```

## Tag 0AMP, a lemma

[Tag 0AMP](https://stacks.math.columbia.edu/tag/0AMP) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_of_comp_of_flat_surjective_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrap.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrap.lean#L155).

> **Stacks 0AMP.** Let `a : F ⟶ G` and `b : G ⟶ H` be morphisms of presheaves on the big fppf
> site of `S`, with `G` and `H` sheaves.  If `a` is representable by algebraic spaces, surjective,
> flat and locally of finite presentation and the composite `a ≫ b` is representable by algebraic
> spaces, then `b` is representable by algebraic spaces.
>
> At a scheme-valued point `ξ` of `H` the fibre product `U ×_H F` is an algebraic space, being a
> base change of `a ≫ b`, and `U ×_H G` is a sheaf.  The morphism `U ×_H F ⟶ U ×_H G` is the base
> change of `a` along `U ×_H G ⟶ G`, so Stacks 046F gives it the three properties of `a`, and
> Stacks 04S6 condition (3) makes `U ×_H G` an algebraic space; that deduction is
> `AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_of_comp_of_flat_surjective`, whose
> bootstrap input is discharged here by
> `AlgebraicGeometry.Space.isBootstrapAlgebraicSpaceAlongFlatSurjection`.
>
> Sheafness of `F` is assumed in the source and is not needed here: representability of `a ≫ b`
> already makes the base changes of `F` that the argument uses algebraic spaces.
>
> This is the complete statement of Stacks 0AMP and its only registration; nothing is assumed.

```lean
theorem isRepresentableByAlgebraicSpaces_of_comp_of_flat_surjective_unconditional
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G) (b : G ⟶ H)
    (hG : Presheaf.IsSheaf (BigFppfOver.topology B S hS) G)
    (hH : Presheaf.IsSheaf (BigFppfOver.topology B S hS) H)
    (haRep : IsRepresentableByAlgebraicSpaces B S hS a)
    (haSurj : HasProperty B S hS (surjectiveMorphismProperty B S hS) a haRep)
    (haFlat : HasProperty B S hS (flatProperty B S hS) a haRep)
    (haLfp : HasProperty B S hS (locallyOfFinitePresentationProperty B S hS) a haRep)
    (hcomp : IsRepresentableByAlgebraicSpaces B S hS (a ≫ b)) :
    IsRepresentableByAlgebraicSpaces B S hS b
```

## Tag 04TB, a lemma

[Tag 04TB](https://stacks.math.columbia.edu/tag/04TB) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicSpace_isomPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/IsomorphismSheafAlgebraic.lean, line 1199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/IsomorphismSheafAlgebraic.lean#L1199).

> The sheaf `Isom(x, y)` of isomorphisms between two objects of the quotient stack of a groupoid
> in algebraic spaces, read on the big fppf site of the scheme the test object lies over, is an
> algebraic space over that scheme.
>
> Algebraicity is expressed by a pointwise bijection, natural in the test object, with a presheaf
> of `Type u` which is an algebraic space: the hom sets of the stackification are not small, so
> `Isom(x, y)` itself takes values one universe up.

```lean
theorem isAlgebraicSpace_isomPresheaf
    (C : BigFppfSite.{u}) (S : Scheme.{u}) (hS : C.Contains S)
    (B : AlgebraicSpaces C S hS)
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (T : BigFppfOver C S hS)
    (x y : (quotientStack G).p.Fiber T) :
    let I := (Over.iteratedSliceBackward T).op ⋙ (quotientStack G).p.isomPresheaf x y
    ∃ F : (BigFppfOver C T.left.1 T.left.2)ᵒᵖ ⥤ Type u,
      IsAlgebraicSpace C T.left.1 T.left.2 F ∧
        ∃ e : ∀ U, I.obj U ≃ F.obj U,
          ∀ ⦃U V⦄ (f : U ⟶ V) (z : I.obj U), e V (I.map f z) = F.map f (e U z)
```

## Tag 06PG, a lemma

[Tag 06PG](https://stacks.math.columbia.edu/tag/06PG) in the Stacks Project.

**`AlgebraicGeometry.Space.isSurjective_toQuotientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CoveringMap.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CoveringMap.lean#L169). The attribute's comment: “surjectivity”.

> **Stacks 06PG.** The object presheaf of a pre-relation surjects onto its quotient sheaf.
>
> A point of the quotient is represented by a section over the spectrum of a field in the site;
> the quotient map is a surjection of fppf sheaves, so that section lifts to `U` on a covering,
> and the spectrum of a residue field of a member of the covering is again an object of the
> site and gives a field-valued point of `U` dominating the original one.
>
> This also discharges the surjectivity clause of **Stacks 06PH**, that `X ⟶ X/G` is surjective
> for a free action of a group algebraic space: the quotient `X/G` of [Stacks, Tag 044J] is the
> quotient sheaf of the pre-relation of the action, so that clause is this lemma at that
> pre-relation. It is stated here for an arbitrary pre-relation, which is more general and uses
> neither freeness of the action nor flatness of `G ⟶ B`; the remaining clauses of Stacks 06PH —
> algebraicity of `X/G`, flatness and local finite presentation of `X ⟶ X/G`, and the fppf
> torsor property — are not proved here and nothing in this file assumes them.

```lean
theorem isSurjective_toQuotientSheaf (j : PreRelation R U) :
    IsSurjective site S hS (toQuotientSheaf j)
```

**`AlgebraicGeometry.Space.isFlat_toQuotientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CoveringMap.lean, line 459](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CoveringMap.lean#L459). The attribute's comment: “flatness”.

> **Stacks 06PG.** The object space of a groupoid in algebraic spaces is flat over its
> sheaf quotient, as soon as that quotient is an algebraic space, the relation cut out by the
> groupoid is an equivalence relation and the target map of the groupoid is flat.

```lean
theorem isFlat_toQuotientSheaf
    (hrel : CategoryTheory.IsEquivalenceRelation
      (groupoidPreRelation G).target (groupoidPreRelation G).source)
    (hF : IsAlgebraicSpace site S hS (quotientSheaf (groupoidPreRelation G)).obj)
    (ht : IsFlat site S hS G.target.hom) :
    IsFlat site S hS (toQuotientSheaf (groupoidPreRelation G))
```

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_toQuotientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CoveringMap.lean, line 479](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CoveringMap.lean#L479). The attribute's comment: “local finite presentation”.

> **Stacks 06PG.** The object space of a groupoid in algebraic spaces is locally of finite
> presentation over its sheaf quotient, as soon as that quotient is an algebraic space, the
> relation cut out by the groupoid is an equivalence relation and the target map of the groupoid
> is locally of finite presentation.

```lean
theorem isLocallyOfFinitePresentation_toQuotientSheaf
    (hrel : CategoryTheory.IsEquivalenceRelation
      (groupoidPreRelation G).target (groupoidPreRelation G).source)
    (hF : IsAlgebraicSpace site S hS (quotientSheaf (groupoidPreRelation G)).obj)
    (ht : IsLocallyOfFinitePresentation site S hS G.target.hom) :
    IsLocallyOfFinitePresentation site S hS (toQuotientSheaf (groupoidPreRelation G))
```

## Tag 06PH, a lemma

[Tag 06PH](https://stacks.math.columbia.edu/tag/06PH) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isAlgebraicSpace_arrowStabilizerQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ArrowQuotient.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ArrowQuotient.lean#L367). The attribute's comment: “R/S is an algebraic space”.

> **Stacks 06PH.** The quotient `R/S` of the arrow space by the stabilizer action is an
> algebraic space, as soon as the stabilizer is flat and locally of finite presentation over the
> object space.

```lean
theorem isAlgebraicSpace_arrowStabilizerQuotient (G : GroupoidInAlgebraicSpaces C S hS B)
    (hflat : Space.IsFlat C S hS (stabilizer G).hom)
    (hfp : Space.IsLocallyOfFinitePresentation C S hS (stabilizer G).hom) :
    IsAlgebraicSpace C S hS (arrowStabilizerQuotient G).obj
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isSurjective_toArrowStabilizerQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ArrowQuotient.lean, line 377](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ArrowQuotient.lean#L377). The attribute's comment: “surjectivity of R ⟶ R/S”.

> **Stacks 06PH.** The quotient map `π : R ⟶ R/S` is surjective.

```lean
theorem isSurjective_toArrowStabilizerQuotient (G : GroupoidInAlgebraicSpaces C S hS B) :
    Space.IsSurjective C S hS (toArrowStabilizerQuotient G)
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isFlat_toArrowStabilizerQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ArrowQuotient.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ArrowQuotient.lean#L383). The attribute's comment: “flatness of R ⟶ R/S”.

> **Stacks 06PH.** The quotient map `π : R ⟶ R/S` is flat.

```lean
theorem isFlat_toArrowStabilizerQuotient (G : GroupoidInAlgebraicSpaces C S hS B)
    (hflat : Space.IsFlat C S hS (stabilizer G).hom)
    (hfp : Space.IsLocallyOfFinitePresentation C S hS (stabilizer G).hom) :
    Space.IsFlat C S hS (toArrowStabilizerQuotient G)
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isLocallyOfFinitePresentation_toArrowStabilizerQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ArrowQuotient.lean, line 393](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ArrowQuotient.lean#L393). The attribute's comment: “local finite presentation of R ⟶ R/S”.

> **Stacks 06PH.** The quotient map `π : R ⟶ R/S` is locally of finite presentation.

```lean
theorem isLocallyOfFinitePresentation_toArrowStabilizerQuotient
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (hflat : Space.IsFlat C S hS (stabilizer G).hom)
    (hfp : Space.IsLocallyOfFinitePresentation C S hS (stabilizer G).hom) :
    Space.IsLocallyOfFinitePresentation C S hS (toArrowStabilizerQuotient G)
```

**`AlgebraicGeometry.Space.isSurjective_toQuotientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CoveringMap.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CoveringMap.lean#L169). The attribute's comment: “surjectivity of the quotient map, for an arbitrary pre-relation”.

> **Stacks 06PG.** The object presheaf of a pre-relation surjects onto its quotient sheaf.
>
> A point of the quotient is represented by a section over the spectrum of a field in the site;
> the quotient map is a surjection of fppf sheaves, so that section lifts to `U` on a covering,
> and the spectrum of a residue field of a member of the covering is again an object of the
> site and gives a field-valued point of `U` dominating the original one.
>
> This also discharges the surjectivity clause of **Stacks 06PH**, that `X ⟶ X/G` is surjective
> for a free action of a group algebraic space: the quotient `X/G` of [Stacks, Tag 044J] is the
> quotient sheaf of the pre-relation of the action, so that clause is this lemma at that
> pre-relation. It is stated here for an arbitrary pre-relation, which is more general and uses
> neither freeness of the action nor flatness of `G ⟶ B`; the remaining clauses of Stacks 06PH —
> algebraicity of `X/G`, flatness and local finite presentation of `X ⟶ X/G`, and the fppf
> torsor property — are not proved here and nothing in this file assumes them.

```lean
theorem isSurjective_toQuotientSheaf (j : PreRelation R U) :
    IsSurjective site S hS (toQuotientSheaf j)
```

**`AlgebraicGeometry.Space.isSurjective_toActionQuotientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GroupActionQuotient.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GroupActionQuotient.lean#L351). The attribute's comment: “surjectivity of X ⟶ X/G”.

> **Stacks 06PH.** The quotient morphism `X ⟶ X/G` is surjective.
>
> This holds for the quotient sheaf of any pre-relation, by Stacks 06PG, so neither freeness
> nor any property of `G ⟶ B` is needed.

```lean
theorem isSurjective_toActionQuotientSheaf (G X : Over B) [GrpObj G] [ModObj G X] :
    IsSurjective site S hS (toQuotientSheaf (actionPreRelation G X))
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_actionQuotientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GroupActionQuotientAlgebraic.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GroupActionQuotientAlgebraic.lean#L82). The attribute's comment: “X/G is an algebraic space”.

> **Stacks 06PH.** The quotient `X/G` of an algebraic space by a free action of a group
> algebraic space which is flat and locally of finite presentation over the base is an
> algebraic space.

```lean
theorem isAlgebraicSpace_actionQuotientSheaf
    (hB : IsAlgebraicSpace site S hS B) (G X : Over B) [GrpObj G] [ModObj G X]
    (hG : IsAlgebraicSpace site S hS G.left) (hX : IsAlgebraicSpace site S hS X.left)
    (hfree : IsFreeAction site S hS B G X) (hflat : IsFlat site S hS G.hom)
    (hfp : IsLocallyOfFinitePresentation site S hS G.hom) :
    IsAlgebraicSpace site S hS (actionQuotientSheaf G X).obj
```

**`AlgebraicGeometry.Space.isFlat_toActionQuotientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GroupActionQuotientAlgebraic.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GroupActionQuotientAlgebraic.lean#L94). The attribute's comment: “flatness of X ⟶ X/G”.

> **Stacks 06PH.** The quotient morphism `X ⟶ X/G` of a free action of a group algebraic
> space which is flat and locally of finite presentation over the base is flat.

```lean
theorem isFlat_toActionQuotientSheaf
    (hB : IsAlgebraicSpace site S hS B) (G X : Over B) [GrpObj G] [ModObj G X]
    (hG : IsAlgebraicSpace site S hS G.left) (hX : IsAlgebraicSpace site S hS X.left)
    (hfree : IsFreeAction site S hS B G X) (hflat : IsFlat site S hS G.hom)
    (hfp : IsLocallyOfFinitePresentation site S hS G.hom) :
    IsFlat site S hS (toQuotientSheaf (actionPreRelation G X))
```

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_toActionQuotientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GroupActionQuotientAlgebraic.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GroupActionQuotientAlgebraic.lean#L107). The attribute's comment: “local finite presentation of X ⟶ X/G”.

> **Stacks 06PH.** The quotient morphism `X ⟶ X/G` of a free action of a group algebraic
> space which is flat and locally of finite presentation over the base is locally of finite
> presentation.

```lean
theorem isLocallyOfFinitePresentation_toActionQuotientSheaf
    (hB : IsAlgebraicSpace site S hS B) (G X : Over B) [GrpObj G] [ModObj G X]
    (hG : IsAlgebraicSpace site S hS G.left) (hX : IsAlgebraicSpace site S hS X.left)
    (hfree : IsFreeAction site S hS B G X) (hflat : IsFlat site S hS G.hom)
    (hfp : IsLocallyOfFinitePresentation site S hS G.hom) :
    IsLocallyOfFinitePresentation site S hS (toQuotientSheaf (actionPreRelation G X))
```

**`AlgebraicGeometry.Space.isFppfTorsor_actionQuotientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GroupActionQuotientAlgebraic.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/GroupActionQuotientAlgebraic.lean#L120). The attribute's comment: “X is an fppf G-torsor over X/G”.

> **Stacks 06PH.** For a free action of a group algebraic space which is flat and locally of
> finite presentation over the base, `X` is an fppf torsor over `X/G` under the group `G` pulled
> back to `X/G`.

```lean
theorem isFppfTorsor_actionQuotientSheaf
    (hB : IsAlgebraicSpace site S hS B) (G X : Over B) [GrpObj G] [ModObj G X]
    (hG : IsAlgebraicSpace site S hS G.left) (hX : IsAlgebraicSpace site S hS X.left)
    (hfree : IsFreeAction site S hS B G X) (hflat : IsFlat site S hS G.hom)
    (hfp : IsLocallyOfFinitePresentation site S hS G.hom) :
    IsFppfTorsor site S hS (actionQuotientPresheaf G X)
      (isAlgebraicSpace_actionQuotientSheaf hB G X hG hX hfree hflat hfp)
      (groupOverQuotient hB.isSheaf G X) (sourceOverQuotient G X)
      (isAlgebraicSpace_pullback site S hS G.hom (actionQuotientToBase hB.isSheaf G X) hG
        (isAlgebraicSpace_actionQuotientSheaf hB G X hG hX hfree hflat hfp) hB)
      hX
```

## Tag 04U1, a lemma

[Tag 04U1](https://stacks.math.columbia.edu/tag/04U1) in the Stacks Project.

**`AlgebraicGeometry.Space.isFppfTorsor_of_isFppfCovering_of_modIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/TorsorDescent/GlueingTorsors.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/TorsorDescent/GlueingTorsors.lean#L181). The attribute's comment: “the glued object is an fppf torsor; not its existence from the descent datum”.

> **The glued object of Stacks 04U1 is an fppf torsor.**
>
> Let `{Bᵢ ⟶ B}` be an fppf covering of an algebraic space `B` over `S`, let `G` be a group
> algebraic space over `B`, and suppose given for each `i` an fppf torsor `Xᵢ` over `Bᵢ` under the
> base change of `G`. If `X` is an algebraic space over `B` carrying an action of `G` together
> with, for each `i`, an isomorphism `e i` of the base change of `X` to `Bᵢ` with `Xᵢ` which is
> equivariant for the base change of `G`, then `X` is an fppf `G`-torsor over `B`.
>
> The base changes of the action on `X` are fppf torsors by transport along the `e i`
> (`AlgebraicGeometry.Space.isFppfTorsor_of_modIso` applied to the inverse isomorphisms), and the
> two conditions are fppf local on the base by
> `AlgebraicGeometry.Space.isFppfTorsor_of_isFppfCovering`.
>
> The existence of `X` from the transition isomorphisms of a descent datum, and so the whole of
> Stacks 04U1, is `AlgebraicGeometry.Space.exists_isFppfTorsor_of_descentDatum`.

```lean
theorem isFppfTorsor_of_isFppfCovering_of_modIso (hB : IsAlgebraicSpace 𝒞 S hS B)
    (G : Over B) [GrpObj G] (hG : IsAlgebraicSpace 𝒞 S hS G.left)
    (X : Over B) [ModObj G X] (hX : IsAlgebraicSpace 𝒞 S hS X.left)
    {I : Type (u + 1)} (Bᵢ : I → (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u) (f : ∀ i, Bᵢ i ⟶ B)
    (hBᵢ : ∀ i, IsAlgebraicSpace 𝒞 S hS (Bᵢ i)) (hcov : IsFppfCovering 𝒞 S hS Bᵢ f)
    (Xᵢ : ∀ i, Over (Bᵢ i)) [∀ i, ModObj ((Over.pullback (f i)).obj G) (Xᵢ i)]
    (hXᵢ : ∀ i, IsAlgebraicSpace 𝒞 S hS (Xᵢ i).left)
    (e : ∀ i, (Over.pullback (f i)).obj X ≅ Xᵢ i)
    (he : ∀ i, IsModHom ((Over.pullback (f i)).obj G) (e i).hom)
    (htors : ∀ i, IsFppfTorsor 𝒞 S hS (Bᵢ i) (hBᵢ i) ((Over.pullback (f i)).obj G) (Xᵢ i)
      (isAlgebraicSpace_pullback 𝒞 S hS G.hom (f i) hG (hBᵢ i) hB) (hXᵢ i)) :
    IsFppfTorsor 𝒞 S hS B hB G X hG hX
```

**`AlgebraicGeometry.Space.exists_isFppfTorsor_of_descentDatum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/TorsorDescent/GlueingTorsorsExistence.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/TorsorDescent/GlueingTorsorsExistence.lean#L213).

> **Stacks 04U1.** Let `{f i : Sᵢ ⟶ S}` be a covering family of the big fppf site of `S` and let
> `G` be a group algebraic space over `S`. A descent datum `D` of fppf torsors along that family —
> for each `i` an fppf torsor `D.x i` over `Sᵢ` under the base change `Gᵢ` of `G`, and for each
> `i, j` an equivariant isomorphism `D.φ i j` between the restrictions of `D.x i` and of `D.x j`
> to `Sᵢ ×_S Sⱼ`, satisfying the cocycle condition over every `Sᵢ ×_S Sⱼ ×_S Sₖ` — is effective:
> there is an fppf `G`-torsor `X` over `S` whose restriction to each `Sᵢ` is isomorphic to `D.x i`,
> compatibly with the `D.φ i j`.
>
> The bootstrap theorem Stacks 04S6, condition (3), is used only to see that the glued torsor of
> sheaves is an algebraic space; the glueing is Stacks 04UM and the torsor conditions are carried
> along by it.

```lean
theorem exists_isFppfTorsor_of_descentDatum
    (G : GroupAlgebraicSpace 𝒞 S hS (baseYoneda 𝒞 S hS)
      (isAlgebraicSpace_yoneda 𝒞 S hS (Over.mk (𝟙 (𝒞.obj hS)))))
    {I : Type w} (V : I → BigFppfOver 𝒞 S hS) (f : ∀ i, V i ⟶ Over.mk (𝟙 (𝒞.obj hS)))
    (hf : Sieve.ofArrows V f ∈ BigFppfOver.topology 𝒞 S hS (Over.mk (𝟙 (𝒞.obj hS))))
    (Vij : I → I → BigFppfOver 𝒞 S hS)
    (pr₁ : ∀ i j, Vij i j ⟶ V i) (pr₂ : ∀ i j, Vij i j ⟶ V j)
    (hVij : ∀ i j, IsPullback (pr₁ i j) (pr₂ i j) (f i) (f j))
    (Vijk : I → I → I → BigFppfOver 𝒞 S hS)
    (s₁₂ : ∀ i j k, Vijk i j k ⟶ Vij i j) (s₂₃ : ∀ i j k, Vijk i j k ⟶ Vij j k)
    (hVijk : ∀ i j k, IsPullback (s₁₂ i j k) (s₂₃ i j k) (pr₂ i j) (pr₁ j k))
    (q₁ : ∀ i j k, Vijk i j k ⟶ V i) (q₂ : ∀ i j k, Vijk i j k ⟶ V j)
    (q₃ : ∀ i j k, Vijk i j k ⟶ V k)
    (hq₁ : ∀ i j k, q₁ i j k = s₁₂ i j k ≫ pr₁ i j)
    (hq₂ : ∀ i j k, q₂ i j k = s₁₂ i j k ≫ pr₂ i j)
    (hq₃ : ∀ i j k, q₃ i j k = s₂₃ i j k ≫ pr₂ j k)
    (D : Functor.DescentDatum
      (FppfTorsors.projection (isAlgebraicSpace_yoneda 𝒞 S hS (Over.mk (𝟙 (𝒞.obj hS)))) G)
      V f Vij pr₁ pr₂ hVij Vijk s₁₂ s₂₃ hVijk q₁ q₂ q₃ hq₁ hq₂ hq₃) :
    D.IsEffective
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 80.11, Tag 04SJ](https://stacks.math.columbia.edu/tag/04SJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
