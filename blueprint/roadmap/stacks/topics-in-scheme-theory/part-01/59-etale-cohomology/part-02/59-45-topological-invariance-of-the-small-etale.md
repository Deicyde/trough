---
declaration: section
origin: cited
lean: Stacks.Etale.bijective_baseChange_hom_of_universalHomeomorphism, Stacks.EtaleCohomology.smallEtaleBaseChange_full_of_universalHomeomorphism, Stacks.Etale.bijective_pullbackHom_of_universalHomeomorphism, AlgebraicGeometry.etaleDescentDataForget, Stacks.Etale.isEquivalence_etalePullback_of_integral_universallyInjective_surjective, Stacks.Etale.etalePullback_isEquivalence, Stacks.Etale.etalePullback_isEquivalence_of_integral_universallyInjective_surjective, Stacks.Etale.affineEtalePullback_fullyFaithful
statement: formalized
proof: formalized
---

# 59.45 Topological invariance of the small étale site

Section 59.45 of the Stacks Project, [Tag 04DY](https://stacks.math.columbia.edu/tag/04DY). 6 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BTY, a theorem

[Tag 0BTY](https://stacks.math.columbia.edu/tag/0BTY) in the Stacks Project.

**`Stacks.Etale.bijective_baseChange_hom_of_universalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance.lean#L209). References: EGA IV (18.1.3), “more general”; SGA 3 X (2.0), “full faithfulness”.

> **Stacks Project, Tag 0BTY.** Let `g : S' ⟶ S` be a universal homeomorphism and let `X` be
> a scheme étale over `S`. For every scheme `Y` over `S`, base change along `g` is a bijection
> from the `S`-morphisms `Y ⟶ X` to the `S'`-morphisms between the base changes of `Y` and `X`.

```lean
theorem bijective_baseChange_hom_of_universalHomeomorphism
    {S S' : Scheme.{u}} (g : S' ⟶ S) [UniversalHomeomorphism g] (X Y : Over S) [Etale X.hom] :
    Function.Bijective (fun f : Y ⟶ X => (Over.pullback g).map f)
```

**`Stacks.EtaleCohomology.smallEtaleBaseChange_full_of_universalHomeomorphism`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/Fullness.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/Fullness.lean#L78). The attribute's comment: “fullness of base change on the small étale site”.

> **Base change along a universal homeomorphism is full on small étale sites.** For `V` and
> `W` étale over `Y`, every morphism `X ×_Y V ⟶ X ×_Y W` over `X` is the base change of a
> morphism `V ⟶ W` over `Y`.
>
> This is Stacks Project, Tag 0BTY read on the small étale site; the content is
> `Stacks.Etale.bijective_pullbackHom_of_universalHomeomorphism`.

```lean
instance smallEtaleBaseChange_full_of_universalHomeomorphism (f : X ⟶ Y)
    [UniversalHomeomorphism f] : (smallEtaleBaseChange f).Full
```

**`Stacks.Etale.bijective_pullbackHom_of_universalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/MorphismDescent.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/MorphismDescent.lean#L256). References: EGA IV (18.1.3), “more general”; EGA IV (2.2.16), “special case”; SGA 1 IX (3.1), “special case”; SGA 1 IX (4.10), “full faithfulness”; SGA 3 X (2.0), “full faithfulness”.

> **Stacks Project, Tag 0BTY.** Let `f : X ⟶ Y` be a universal homeomorphism and let `A` be a
> scheme étale over `Y`. For every scheme `B` over `Y`, base change along `f` is a bijection from
> the `Y`-morphisms `B ⟶ A` to the `X`-morphisms between the base changes.
>
> Injectivity holds for any surjective `f`, by
> `Stacks.Etale.injective_baseChange_hom_of_universalHomeomorphism`; surjectivity is
> `Stacks.Etale.exists_hom_of_pullbackHom_of_universalHomeomorphism`.

```lean
theorem bijective_pullbackHom_of_universalHomeomorphism {X Y : Scheme.{u}} (f : X ⟶ Y)
    [UniversalHomeomorphism f] (A B : Over Y) [Etale A.hom] :
    Function.Bijective (fun h : B ⟶ A => (Over.pullback f).map h)
```

## Tag 0BTZ, an equation

[Tag 0BTZ](https://stacks.math.columbia.edu/tag/0BTZ) in the Stacks Project.

**`AlgebraicGeometry.etaleDescentDataForget`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Descent.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/Descent.lean#L79).

> The functor forgetting the descent isomorphism of an étale descent datum relative to
> `S' ⟶ S`, retaining its underlying étale scheme over `S'`.

```lean
def etaleDescentDataForget {S S' : Scheme.{u}} (g : S' ⟶ S)
    [UniversalHomeomorphism g] : EtaleDescentData g ⥤ EtaleOver S'
```

## Tag 04DZ, a theorem

[Tag 04DZ](https://stacks.math.columbia.edu/tag/04DZ) in the Stacks Project.

**`Stacks.Etale.isEquivalence_etalePullback_of_integral_universallyInjective_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/AffineEtaleDescentStep.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/AffineEtaleDescentStep.lean#L427). The attribute's comment: “base change `V ↦ X ×_Y V` along an integral, universally injective and surjective morphism `f : X ⟶ Y` is an equivalence `Y_étale ⥤ X_étale`: full faithfulness is Tag 0BTY, and essential surjectivity is glued, by Schemes 01JA and 01JC, from the affine case, the induction `Stacks.Etale.essSurjAffineEtalePullback_of_etaleDescent` of the source's second proof on a bound for the degree of the fibres, descending at each step by Tag 0245 as `Stacks.Etale.etaleDescentAlongAffineEtaleSurjection`.”. References: EGA IV (18.1.2), “more general”; SGA 1 IX (4.10); SGA 4 VIII (1.1), “partial”.

> **Topological invariance of the small étale site, Stacks Project, Tag 04DZ.** Let
> `f : X ⟶ Y` be integral, universally injective and surjective. Then `V ↦ X ×_Y V` is an
> equivalence from the category of schemes étale over `Y` to the category of schemes étale over
> `X`.
>
> The reduction to the affine case,
> `Stacks.Etale.exists_etale_pullback_iso_of_essSurjAffine`, is
> supplied with that affine case (Stacks Project, Tag 04E0), obtained here from
> `Stacks.Etale.essSurjAffineEtalePullback_of_etaleDescent` and the descent step
> `Stacks.Etale.etaleDescentAlongAffineEtaleSurjection`.

```lean
theorem isEquivalence_etalePullback_of_integral_universallyInjective_surjective
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsIntegralHom f] [UniversallyInjective f] [Surjective f] :
    letI : MorphismProperty.HasPullbacksAlong
        (@Etale : MorphismProperty Scheme.{u}) f := ⟨fun _ _ ↦ inferInstance⟩
    letI : MorphismProperty.IsStableUnderBaseChangeAlong
        (@Etale : MorphismProperty Scheme.{u}) f :=
      ⟨fun pb hg ↦ MorphismProperty.IsStableUnderBaseChange.of_isPullback pb hg⟩
    (show Y.Etale ⥤ X.Etale from
      MorphismProperty.Over.pullback
        (@Etale : MorphismProperty Scheme.{u}) ⊤ f).IsEquivalence
```

**`Stacks.Etale.etalePullback_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/DescentEffective.lean, line 546](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/DescentEffective.lean#L546). The attribute's comment: “the equivalence, unconditionally. Full faithfulness is Tag 0BTY; essential surjectivity is the affine case `Stacks.Etale.essSurjAffineEtalePullback` glued over an affine cover by `Stacks.Etale.exists_etale_pullback_iso_of_essSurjAffine`. The name `Stacks.Etale.etalePullback_isEquivalence_of_integral_universallyInjective_surjective` is an alias of this declaration and keeps the tag as well.”. References: EGA IV (18.1.2), “more general”; SGA 1 IX (4.10); SGA 4 VIII (1.1), “partial”.

> **Topological invariance of the small étale site.** Let `f : X ⟶ Y` be integral, universally
> injective and surjective. Then `V ↦ X ×_Y V` is an equivalence from the category of schemes étale
> over `Y` to the category of schemes étale over `X`.
>
> Essential surjectivity is `Stacks.Etale.exists_etale_pullback_iso_of_essSurjAffine` with its
> hypothesis discharged by `Stacks.Etale.essSurjAffineEtalePullback`.

```lean
theorem etalePullback_isEquivalence (f : X ⟶ Y) [IsIntegralHom f]
    [UniversallyInjective f] [Surjective f] :
    letI : MorphismProperty.HasPullbacksAlong
        (@Etale : MorphismProperty Scheme.{u}) f := ⟨fun _ _ ↦ inferInstance⟩
    letI : MorphismProperty.IsStableUnderBaseChangeAlong
        (@Etale : MorphismProperty Scheme.{u}) f :=
      ⟨fun pb hg ↦ MorphismProperty.IsStableUnderBaseChange.of_isPullback pb hg⟩
    (show Y.Etale ⥤ X.Etale from
      MorphismProperty.Over.pullback
        (@Etale : MorphismProperty Scheme.{u}) ⊤ f).IsEquivalence
```

**`Stacks.Etale.etalePullback_isEquivalence_of_integral_universallyInjective_surjective`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/DescentEffective.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/DescentEffective.lean#L574). The attribute's comment: “Full faithfulness is unconditional, from Tag 0BTY. A scheme etale over `X` is covered by affine opens lying over affine opens of `Y`, and the glueing of Schemes 01JA and 01JC -- in this library `exists_etale_pullback_iso_of_descendedOpens_cover` -- assembles the local descents into a global one. Essential surjectivity is thereby reduced to the affine case, the essential surjectivity of the correspondence displayed as Tag 04E0, which is proved unconditionally as `Stacks.Etale.essSurjAffineEtalePullback` by the source's induction on a bound for the degree of the fibres of an etale morphism of affine schemes. This name is an alias of `Stacks.Etale.etalePullback_isEquivalence`. The source's hypotheses are stated in their own form, as integrality, universal injectivity and surjectivity, and converted by Tag 04DF.”.

> **Topological invariance of the small étale site.** Let `f : X ⟶ Y` be integral, universally
> injective and surjective. Then `V ↦ X ×_Y V` is an equivalence from the category of schemes
> étale over `Y` to the category of schemes étale over `X`.

```lean
alias etalePullback_isEquivalence_of_integral_universallyInjective_surjective
```

## Tag 04E0, an equation

[Tag 04E0](https://stacks.math.columbia.edu/tag/04E0) in the Stacks Project.

**`Stacks.Etale.affineEtalePullback_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/AffineCase.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/AffineCase.lean#L234). The attribute's comment: “Full faithfulness of the displayed correspondence and the preservation of affineness only, both unconditional: full faithfulness is Tag 0BTY read on the affine objects, and base change carries an affine etale `Y`-scheme to an affine etale `X`-scheme because a universal homeomorphism is an affine morphism (Tag 04DF). Essential surjectivity, which is the content the source proves about this correspondence, is NOT delivered here. The source obtains it by induction on a bound for the degree of the fibres of an etale morphism of affine schemes, descending at each step by effectivity of affine descent, Tag 0245; that induction is not formalized in this library, although Tag 0245 itself is carried, by `AlgebraicGeometry.DescentData.isFamilyEffective_of_isAffineHom`, as are the other tags it cites (04DW, 03WS, 03JA, 03WU, 02VN). The alternative route, through effectivity of etale descent along a surjective integral morphism (Tag 0BTP), has only its fully faithful half carried, by `AlgebraicGeometry.fullyFaithful_quasiCompactSeparatedEtaleDescentFunctor_of_isIntegralHom`. Given essential surjectivity, this restricted functor is an equivalence, by `affineEtalePullback_isEquivalence_of_essSurjAffine`.”.

> **The affine correspondence of Stacks Project, Tag 04E0: its unconditional half.** Let
> `f : X ⟶ Y` be a universal homeomorphism of affine schemes. Base change along `f` carries an
> affine scheme étale over `Y` to an affine scheme étale over `X`, and the induced functor between
> the affine objects of the two small étale sites is full and faithful.

```lean
theorem affineEtalePullback_fullyFaithful (f : X ⟶ Y) [UniversalHomeomorphism f]
    [IsAffine X] [IsAffine Y] :
    letI : MorphismProperty.HasPullbacksAlong
        (@Etale : MorphismProperty Scheme.{u}) f := ⟨fun _ _ ↦ inferInstance⟩
    letI : MorphismProperty.IsStableUnderBaseChangeAlong
        (@Etale : MorphismProperty Scheme.{u}) f :=
      ⟨fun pb hg ↦ MorphismProperty.IsStableUnderBaseChange.of_isPullback pb hg⟩
    let F : Y.Etale ⥤ X.Etale :=
      MorphismProperty.Over.pullback (@Etale : MorphismProperty Scheme.{u}) ⊤ f
    let PY : ObjectProperty Y.Etale := fun V ↦ IsAffine V.left
    let PX : ObjectProperty X.Etale := fun U ↦ IsAffine U.left
    ∃ h : ∀ V : PY.FullSubcategory, PX (F.obj V.obj),
      (PX.lift (PY.ι ⋙ F) h).Full ∧ (PX.lift (PY.ι ⋙ F) h).Faithful
```

**`Stacks.Etale.affineEtalePullback_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/DescentEffective.lean, line 517](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/DescentEffective.lean#L517). The attribute's comment: “the displayed correspondence, in full and unconditionally. Its three clauses are covered as follows. Preservation of affineness and full faithfulness are `Stacks.Etale.affineEtalePullback_fullyFaithful`, which carries the tag too. Essential surjectivity -- the content the source proves, by induction on a bound for the degree of the fibres of an etale morphism of affine schemes, descending at each step by effectivity of descent -- is `Stacks.Etale.essSurjAffineEtalePullback`. This declaration is the equivalence the three together give, assembled by `Stacks.Etale.affineEtalePullback_isEquivalence_of_essSurjAffine`. The source's induction runs through `Stacks.Etale.essSurjAffineEtalePullback_of_inductiveStep_surjective`, whose step is `Stacks.Etale.exists_affine_etale_pullback_iso_of_surjective`; its one descent along an etale covering of the target is `Stacks.Etale.exists_affine_etale_pullback_iso_of_descentIso`, where effectivity enters as Tag 02W8 rather than as the source's Tag 0245.”.

> **The affine correspondence of Stacks Project, Tag 04E0.** Let `f : X ⟶ Y` be a universal
> homeomorphism of affine schemes. Base change along `f` carries an affine scheme étale over `Y` to
> an affine scheme étale over `X`, and the induced functor between the affine objects of the two
> small étale sites is an equivalence.
>
> This is `Stacks.Etale.affineEtalePullback_isEquivalence_of_essSurjAffine` with its hypothesis
> discharged by `Stacks.Etale.essSurjAffineEtalePullback`.

```lean
theorem affineEtalePullback_isEquivalence (f : X ⟶ Y) [UniversalHomeomorphism f]
    [IsAffine X] [IsAffine Y] :
    letI : MorphismProperty.HasPullbacksAlong
        (@Etale : MorphismProperty Scheme.{u}) f := ⟨fun _ _ ↦ inferInstance⟩
    letI : MorphismProperty.IsStableUnderBaseChangeAlong
        (@Etale : MorphismProperty Scheme.{u}) f :=
      ⟨fun pb hg ↦ MorphismProperty.IsStableUnderBaseChange.of_isPullback pb hg⟩
    let F : Y.Etale ⥤ X.Etale :=
      MorphismProperty.Over.pullback (@Etale : MorphismProperty Scheme.{u}) ⊤ f
    let PY : ObjectProperty Y.Etale := fun V ↦ IsAffine V.left
    let PX : ObjectProperty X.Etale := fun U ↦ IsAffine U.left
    ∃ h : ∀ V : PY.FullSubcategory, PX (F.obj V.obj),
      (PX.lift (PY.ι ⋙ F) h).IsEquivalence
```

## Tag 05YX, a remark

[Tag 05YX](https://stacks.math.columbia.edu/tag/05YX) in the Stacks Project.

**`Stacks.Etale.affineEtalePullback_isEquivalence_of_essSurj_of_h09YZ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvarianceAffine.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvarianceAffine.lean#L81). The attribute's comment: “assuming essential surjectivity of etale pullback (the content of Stacks 04DZ) and Stacks 09YZ over a qcqs base”.

> **Topological invariance of the étale site on affine objects.** Base change along a universal
> homeomorphism `f : X ⟶ Y` restricts to an equivalence between the full subcategory of affine
> objects of the small étale site of `Y` and the full subcategory of affine objects of the small
> étale site of `X`.
>
> The hypothesis `hessSurj` is essential surjectivity of base change on the whole small étale
> site, part of Stacks Project, Tag 04DZ, and `h09YZ` is Stacks Project, Tag 09YZ over a
> quasi-compact quasi-separated base, the input of Stacks Project, Tag 05YU.

```lean
theorem affineEtalePullback_isEquivalence_of_essSurj_of_h09YZ
    {X Y : Scheme.{u}} (f : X ⟶ Y) [UniversalHomeomorphism f]
    (hessSurj :
      letI : MorphismProperty.HasPullbacksAlong
          (@Etale : MorphismProperty Scheme.{u}) f := ⟨fun _ _ ↦ inferInstance⟩
      letI : MorphismProperty.IsStableUnderBaseChangeAlong
          (@Etale : MorphismProperty Scheme.{u}) f :=
        ⟨fun pb hg ↦ MorphismProperty.IsStableUnderBaseChange.of_isPullback pb hg⟩
      (show Y.Etale ⥤ X.Etale from
        MorphismProperty.Over.pullback
          (@Etale : MorphismProperty Scheme.{u}) ⊤ f).EssSurj)
    (h09YZ : IntegralHasFinitePresentationLimit.{u}) :
    letI : MorphismProperty.HasPullbacksAlong
        (@Etale : MorphismProperty Scheme.{u}) f :=
      ⟨fun _ _ ↦ inferInstance⟩
    letI : MorphismProperty.IsStableUnderBaseChangeAlong
        (@Etale : MorphismProperty Scheme.{u}) f :=
      ⟨fun pb hg ↦
        MorphismProperty.IsStableUnderBaseChange.of_isPullback pb hg⟩
    let F : Y.Etale ⥤ X.Etale :=
      MorphismProperty.Over.pullback
        (@Etale : MorphismProperty Scheme.{u}) ⊤ f
    let PY : ObjectProperty Y.Etale := fun V ↦ IsAffine V.left
    let PX : ObjectProperty X.Etale := fun U ↦ IsAffine U.left
    ∃ (h : ∀ V : PY.FullSubcategory, PX (F.obj V.obj)),
      (PX.lift (PY.ι ⋙ F) h).IsEquivalence
```

**`Stacks.Etale.affineEtalePullback_isEquivalence_of_universalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvarianceAffineEquivalence.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvarianceAffineEquivalence.lean#L46). The attribute's comment: “base change along a universal homeomorphism restricts to an equivalence between the affine schemes etale over the target and the affine schemes etale over the source”. References: SGA 4½ Th finitude (2.7), “partial”.

> **Topological invariance of the étale site on affine objects.** Let `f : X ⟶ Y` be a universal
> homeomorphism. Base change `V ↦ X ×_Y V` along `f` carries an affine scheme étale over `Y` to an
> affine scheme étale over `X`, and the induced functor from the full subcategory of affine objects
> of the small étale site of `Y` to the full subcategory of affine objects of the small étale site
> of `X` is an equivalence.

```lean
theorem affineEtalePullback_isEquivalence_of_universalHomeomorphism
    {X Y : Scheme.{u}} (f : X ⟶ Y) [UniversalHomeomorphism f] :
    letI : MorphismProperty.HasPullbacksAlong
        (@Etale : MorphismProperty Scheme.{u}) f :=
      ⟨fun _ _ ↦ inferInstance⟩
    letI : MorphismProperty.IsStableUnderBaseChangeAlong
        (@Etale : MorphismProperty Scheme.{u}) f :=
      ⟨fun pb hg ↦
        MorphismProperty.IsStableUnderBaseChange.of_isPullback pb hg⟩
    let F : Y.Etale ⥤ X.Etale :=
      MorphismProperty.Over.pullback
        (@Etale : MorphismProperty Scheme.{u}) ⊤ f
    let PY : ObjectProperty Y.Etale := fun V ↦ IsAffine V.left
    let PX : ObjectProperty X.Etale := fun U ↦ IsAffine U.left
    ∃ (h : ∀ V : PY.FullSubcategory, PX (F.obj V.obj)),
      (PX.lift (PY.ι ⋙ F) h).IsEquivalence
```

## Tag 03SI, a proposition

[Tag 03SI](https://stacks.math.columbia.edu/tag/03SI) in the Stacks Project.

**`Stacks.EtaleCohomology.smallEtaleSite_iso_of_universalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/SiteIsomorphism.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvariance/SiteIsomorphism.lean#L88). The attribute's comment: “part (1): the isomorphism of sites, as the equivalence of the small etale categories induced by base change together with the correspondence of covering sieves. The source's hypothesis is a universal homeomorphism, which is this statement's hypothesis as well.”. References: SGA 1 IX (1.7), “more general”; SGA 1 IX (4.10); SGA 4 XIV (1.11), “more general”; SGA 4½ Th finitude (2.7), “more general”.

> **Part (1) of Stacks Project, Tag 03SI: the small étale sites of a universal homeomorphism
> are isomorphic.** Let `f : X ⟶ Y` be a universal homeomorphism. Base change along `f` is an
> equivalence from the small étale category of `Y` to that of `X`, and a sieve on a scheme étale
> over `Y` is covering exactly when its image under base change is covering.
>
> The equivalence of categories is Stacks Project, Tag 04DZ; the correspondence of coverings holds
> for any surjection.

```lean
theorem smallEtaleSite_iso_of_universalHomeomorphism (f : X ⟶ Y) [UniversalHomeomorphism f] :
    (smallEtaleBaseChange f).IsEquivalence ∧
      ∀ (V : Y.Etale) (S : Sieve V),
        S.functorPushforward (smallEtaleBaseChange f) ∈
            smallEtaleTopology X ((smallEtaleBaseChange f).obj V) ↔
          S ∈ smallEtaleTopology Y V
```

**`Stacks.EtaleCohomology.smallEtaleInverseImage_isEquivalence_of_universalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvarianceCohomology.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvarianceCohomology.lean#L65). The attribute's comment: “part (2), equivalence of the small étale topoi”.

> **Stacks 03SI, part (2).** For a universal homeomorphism `f : X ⟶ Y` the small étale topoi of
> `X` and `Y` are equivalent: the canonical inverse-image functor on sheaves of types is an
> equivalence of categories.

```lean
theorem smallEtaleInverseImage_isEquivalence_of_universalHomeomorphism :
    (smallEtaleInverseImage.{u, v} f).IsEquivalence
```

**`Stacks.EtaleCohomology.etaleCohomologyRestrictionMap_bijective_of_universalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvarianceCohomology.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TopologicalInvarianceCohomology.lean#L82). The attribute's comment: “part (3), agreement of étale cohomology”.

> **Stacks 03SI, part (3).** For a universal homeomorphism `f : X ⟶ Y` étale cohomology agrees
> in every degree: restriction along `f` is bijective on `H^q` of every abelian sheaf on the small
> étale site of `Y`.

```lean
theorem etaleCohomologyRestrictionMap_bijective_of_universalHomeomorphism
    [HasSheafify X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}]
    [HasSheafify Y.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}]
    [HasExt.{w} (Sheaf Y.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})]
    [HasExt.{w} (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})]
    (F : Sheaf Y.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) (q : ℕ) :
    Function.Bijective (etaleCohomologyRestrictionMap.{u, v, w} f F q)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.45, Tag 04DY](https://stacks.math.columbia.edu/tag/04DY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
