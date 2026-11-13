---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.presheaf_universalHomeomorphism_iff, AlgebraicGeometry.Space.UniversalHomeomorphism, AlgebraicGeometry.AffineLineInvolution.nonSeparatedUniversalHomeomorphism_squaringMap, AlgebraicGeometry.Space.universallyClosed_toQuotientSheaf_comp_squaringMap, AlgebraicGeometry.Space.universalHomeomorphism_squaringMap, AlgebraicGeometry.Space.universalHomeomorphism_pullback, AlgebraicGeometry.Space.universalHomeomorphism_of_isPullback, AlgebraicGeometry.Space.universalHomeomorphism_comp
statement: formalized
proof: formalized
---

# 67.53 Universal homeomorphisms

Section 67.53 of the Stacks Project, [Tag 05Z3](https://stacks.math.columbia.edu/tag/05Z3). 7 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05Z4, a lemma

[Tag 05Z4](https://stacks.math.columbia.edu/tag/05Z4) in the Stacks Project.

**`AlgebraicGeometry.Space.presheaf_universalHomeomorphism_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalHomeomorphismRepresentable.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/UniversalHomeomorphismRepresentable.lean#L320).

> A representable morphism of algebraic spaces over `S` has universal
> homeomorphy of every one of its represented base changes, which is what being a universal
> homeomorphism means for a representable morphism, exactly when it is a universal homeomorphism in
> the sense of Stacks 05Z5: every base change of it by an algebraic space over `S` induces a
> homeomorphism on the spaces of points.

```lean
theorem presheaf_universalHomeomorphism_iff
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hf : yoneda.relativelyRepresentable f) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.UniversalHomeomorphism.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f ↔ UniversalHomeomorphism B S hS f
```

## Tag 05Z5, a definition

[Tag 05Z5](https://stacks.math.columbia.edu/tag/05Z5) in the Stacks Project.

**`AlgebraicGeometry.Space.UniversalHomeomorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversalHomeomorphism.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversalHomeomorphism.lean#L180).

> **Stacks 05Z5.** A morphism of algebraic spaces over `S` is a *universal homeomorphism*
> when its base change along every morphism to its target from an algebraic space over `S`
> induces a homeomorphism on the spaces of points.

```lean
abbrev UniversalHomeomorphism (f : F ⟶ G) : Prop
```

## Tag 05Z6, an example

[Tag 05Z6](https://stacks.math.columbia.edu/tag/05Z6) in the Stacks Project.

**`AlgebraicGeometry.AffineLineInvolution.nonSeparatedUniversalHomeomorphism_squaringMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionExample.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionExample.lean#L139).

> **Stacks 05Z6.**  Let `k` be a field in which `2` is invertible, let `B` be a big fppf site
> containing `Spec k`, and let `X = 𝐀¹_k/\{x ∼ -x ∣ x ≠ 0\}` be the quotient of the affine line
> by the punctured graph of negation.  Then `X` is an algebraic space over `k`, and of the two
> morphisms
> `𝐀¹_k ⟶ X ⟶ 𝐀¹_k`,
> the projection onto the quotient and the morphism descended from squaring the coordinate:
>
> 1. the first is surjective and étale;
> 2. the second is universally injective;
> 3. their composition is the map `x ↦ x²`;
> 4. hence that composition is universally closed;
> 5. therefore the second morphism is a universal homeomorphism;
> 6. but the second morphism is not separated.
>
> The projection is surjective and étale because the relation is an étale equivalence relation
> whose morphism into the self-product of the affine line is affine, which makes the presentation
> of Stacks 0265 unconditional here.  Squaring is injective on field-valued points up to the
> relation and integral on the affine line, which gives (2) and (4); a universally injective,
> universally closed and surjective morphism of algebraic spaces is a universal homeomorphism,
> which gives (5).  For (6) the relation is a represented base change of the relative diagonal of
> the squaring map and is not a closed immersion, its restriction to the punctured summand
> factoring through the split section of the fibre square with components the identity and
> negation.

```lean
theorem nonSeparatedUniversalHomeomorphism_squaringMap (hchar : (2 : k) ≠ 0) :
    IsAlgebraicSpace B (Spec (.of k)) hk (involutionQuotient k B hk).obj ∧
      (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B (Spec (.of k)) hk)).presheaf
          (Stacks.Groupoids.toQuotientSheaf (BigFppfOver.topology B (Spec (.of k)) hk)
            (Over.post (X := B.obj hk) B.inclusion) (involutionRelation k)) ∧
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B (Spec (.of k)) hk)).presheaf
          (Stacks.Groupoids.toQuotientSheaf (BigFppfOver.topology B (Spec (.of k)) hk)
            (Over.post (X := B.obj hk) B.inclusion) (involutionRelation k)) ∧
      Space.UniversallyInjective B (Spec (.of k)) hk (squaringMap k B hk) ∧
      Stacks.Groupoids.toQuotientSheaf (BigFppfOver.topology B (Spec (.of k)) hk)
            (Over.post (X := B.obj hk) B.inclusion) (involutionRelation k) ≫
          squaringMap k B hk =
        (Over.post (X := B.obj hk) B.inclusion).op.whiskerLeft
          (yoneda.map (affineLineSquare k)) ∧
      Space.UniversallyClosed B (Spec (.of k)) hk
          (Stacks.Groupoids.toQuotientSheaf (BigFppfOver.topology B (Spec (.of k)) hk)
              (Over.post (X := B.obj hk) B.inclusion) (involutionRelation k) ≫
            squaringMap k B hk) ∧
      Space.UniversalHomeomorphism B (Spec (.of k)) hk (squaringMap k B hk) ∧
      ¬ Space.IsSeparated B (Spec (.of k)) hk (squaringMap k B hk)
```

**`AlgebraicGeometry.Space.universallyClosed_toQuotientSheaf_comp_squaringMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversalHomeomorphism.lean, line 671](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversalHomeomorphism.lean#L671). The attribute's comment: “closed\_squaring”.

> **Stacks 05Z6.** The composite of the projection onto the quotient of the affine line by
> the punctured involution relation with the descended squaring map of Stacks 05VS is
> universally closed.
>
> The composite is, through
> `AlgebraicGeometry.Space.toQuotientSheaf_comp_squaringMap_eq_conj`, the morphism of
> represented presheaves induced by squaring of the coordinate. Squaring is an integral morphism
> of schemes, hence a universally closed one, so the induced morphism of presheaves is
> universally closed after every represented base change, and Stacks 03XD turns that into
> universal closedness in the sense of Stacks 03HI. No assumption on the characteristic is
> needed.

```lean
theorem universallyClosed_toQuotientSheaf_comp_squaringMap (hk : B.Contains (Spec (.of k)))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hk) (Type u)] :
    UniversallyClosed B (Spec (.of k)) hk
      (Stacks.Groupoids.toQuotientSheaf (BigFppfOver.topology B (Spec (.of k)) hk)
          (Over.post (X := B.obj hk) B.inclusion) (involutionRelation k) ≫
        squaringMap k B hk)
```

**`AlgebraicGeometry.Space.universalHomeomorphism_squaringMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversalHomeomorphism.lean, line 772](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversalHomeomorphism.lean#L772). The attribute's comment: “universal\_homeomorphism: the map X ⟶ 𝐀¹\_k is a universal homeomorphism”.

> **Stacks 05ZI, the last sentence: there is a universal homeomorphism `X ⟶ 𝐀¹_k`, exhibited
> directly by `t ↦ t ^ 2` on affine space.**
>
> Here `X` is the quotient of the affine line by the relation identifying `t` with `-t` away from
> the origin, the algebraic space of Stacks 05Z6, and the morphism is the one Stacks 05VS
> descends from squaring the coordinate. It is universally closed by
> `AlgebraicGeometry.Space.universallyClosed_squaringMap`, universally injective by Stacks 05VS
> part (4), and surjective after every base change by
> `AlgebraicGeometry.Space.isSurjective_pullback_fst_squaringMap`; the criterion is
> `AlgebraicGeometry.Space.universalHomeomorphism_of_universallyClosed_of_universallyInjective`.
>
> Stacks 05Z6 and Stacks 05ZI state this over an algebraically closed field of characteristic
> zero. Only `2 ≠ 0` in `k` is used, and only for universal injectivity.

```lean
theorem universalHomeomorphism_squaringMap (hchar : (2 : k) ≠ 0)
    (hk : B.Contains (Spec (.of k)))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hk) (Type u)] :
    UniversalHomeomorphism B (Spec (.of k)) hk (squaringMap k B hk)
```

## Tag 0CFT, a lemma

[Tag 0CFT](https://stacks.math.columbia.edu/tag/0CFT) in the Stacks Project.

**`AlgebraicGeometry.Space.universalHomeomorphism_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversalHomeomorphism.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversalHomeomorphism.lean#L238).

> **Stacks 0CFT.** A base change of a universal homeomorphism of algebraic spaces over `S` is
> a universal homeomorphism.
>
> Nothing is needed beyond unwinding the definition: a base change of `Z ×_Y X ⟶ Z` along
> `k : W ⟶ Z` is a base change of `X ⟶ Y` along `k ≫ g`.

```lean
theorem universalHomeomorphism_pullback (f : X ⟶ Y) (g : Z ⟶ Y)
    (hf : UniversalHomeomorphism B S hS f) :
    UniversalHomeomorphism B S hS (pullback.fst g f)
```

**`AlgebraicGeometry.Space.universalHomeomorphism_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversalHomeomorphism.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversalHomeomorphism.lean#L294).

> **Stacks 0CFT** for an arbitrary cartesian square: if `IsPullback a b g f` and `f` is a
> universal homeomorphism, then so is `a`.
>
> This is `AlgebraicGeometry.Space.universalHomeomorphism_pullback` composed with the
> identification of the given square with the canonical fibre product.

```lean
theorem universalHomeomorphism_of_isPullback (hC : IsAlgebraicSpace B S hS C)
    (hZ : IsAlgebraicSpace B S hS Z) (hT : IsAlgebraicSpace B S hS T) (f : C ⟶ T) (g : Z ⟶ T)
    (hf : UniversalHomeomorphism B S hS f) {a : A ⟶ Z} {b : A ⟶ C}
    (hpb : IsPullback a b g f) : UniversalHomeomorphism B S hS a
```

## Tag 0CFU, a lemma

[Tag 0CFU](https://stacks.math.columbia.edu/tag/0CFU) in the Stacks Project.

**`AlgebraicGeometry.Space.universalHomeomorphism_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversalHomeomorphism.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversalHomeomorphism.lean#L268).

> **Stacks 0CFU.** A composition of universal homeomorphisms of algebraic spaces over `S` is
> a universal homeomorphism.
>
> The base change `W ×_Z X ⟶ W` of the composite along `k : W ⟶ Z` is identified by the pasting
> isomorphism `W ×_Z X ≅ (W ×_Z Y) ×_Y X` with the composition of a base change of `X ⟶ Y` and a
> base change of `Y ⟶ Z`.

```lean
theorem universalHomeomorphism_comp (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : UniversalHomeomorphism B S hS f) (hg : UniversalHomeomorphism B S hS g) :
    UniversalHomeomorphism B S hS (f ≫ g)
```

## Tag 08AK, a lemma

[Tag 08AK](https://stacks.math.columbia.edu/tag/08AK) in the Stacks Project.

**`AlgebraicGeometry.Space.universalHomeomorphism_ι_reducedClosedSubspace_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Reduction.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Reduction.lean#L265). References: EGA IV (2.4.8), “(ii) univ. homeo”.

> **Stacks 08AK.** The canonical morphism from the reduction of an algebraic space over `S` —
> the reduced closed subspace supported on all of its points — to the space itself is a universal
> homeomorphism.
>
> The four clauses are independent of one another: continuity is clause (2) of Stacks 03BX,
> injectivity is Stacks 06RV applied to the base change of a subfunctor inclusion, surjectivity is
> Stacks 03H4 together with the computation of the point set of the reduction, and openness is
> `AlgebraicGeometry.Space.universallyOpen_ι_reducedClosedSubspace_univ`. None of them needs the
> inclusion to be representable, so no effective descent hypothesis appears.

```lean
theorem universalHomeomorphism_ι_reducedClosedSubspace_univ (hX : IsAlgebraicSpace B S hS X) :
    UniversalHomeomorphism B S hS
      (reducedClosedSubspace B S hS X hX Set.univ isClosed_univ).ι
```

## Tag 0AEH, a lemma

[Tag 0AEH](https://stacks.math.columbia.edu/tag/0AEH) in the Stacks Project.

**`AlgebraicGeometry.Space.supportOfSheaf_subset_of_essImage_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralPushforwardSupport.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralPushforwardSupport.lean#L172). The attribute's comment: “part (2), the inclusion only: a sheaf in the essential image of f\_\{small,*} is supported on f(|Y|), for an integral morphism and with no universal injectivity needed. The converse inclusion, and with it the full iff of part (2), is AlgebraicGeometry.Space.smallEtalePushforwardAb\_essImage\_iff\_of\_integral\_universallyInjective; part (1) is ...smallEtalePushforward\_essImage\_iff\_of\_integral\_universallyInjective. Both are proved at the source's own hypotheses”.

> **Stacks 0AEH, part (2), one inclusion of the essential image.** An abelian sheaf on the
> small étale site of `X` isomorphic to a small étale direct image along an integral morphism
> `f : Y ⟶ X` of algebraic spaces over `S` is supported on the image of the point set of `Y`.
>
> An isomorphism of abelian sheaves is locally surjective, so by part (5) of Stacks 04KB it does
> not enlarge the support, and the support of the direct image is bounded by
> `AlgebraicGeometry.Space.supportOfSheaf_smallEtaleAbelianPushforward_subset_of_isIntegralHom`.
>
> Universal injectivity of `f`, which Stacks 0AEH also assumes, is not used: this inclusion holds
> for every integral morphism. It is one inclusion of the clause and carries no tag; the clause
> itself is
> `AlgebraicGeometry.Space.smallEtalePushforwardAb_essImage_iff_of_integral_universallyInjective`.

```lean
theorem supportOfSheaf_subset_of_essImage_of_isIntegralHom (f : Y ⟶ X)
    (hf : IsIntegralHom B S hS f.hom) (F : abelianSheaves.{w} B S hS X)
    (hF : (smallEtaleAbelianPushforward B S hS f
      ((isIntegralHom_iff_representable B S hS f.hom Y.property X.property).mp hf).1).essImage
        F) :
    supportOfSheaf B S hS X.1 F ⊆ Set.range (pointsMap B S hS Y.1 f.hom)
```

**`AlgebraicGeometry.Space.smallEtalePushforwardAb_essImage_iff_of_integral_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveEssentialImage.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveEssentialImage.lean#L354). The attribute's comment: “part (2): the essential image, for an integral and universally injective morphism of algebraic spaces”.

> **Stacks 0AEH, part (2), the essential image.** For an integral and universally injective
> morphism `f : Y ⟶ X` of algebraic spaces over a scheme `S`, an abelian sheaf on the small étale
> site of `X` lies in the essential image of the direct image along `f` exactly when its support
> is contained in the image of the point set of `Y`.
>
> The forward inclusion is
> `AlgebraicGeometry.Space.supportOfSheaf_subset_of_essImage_of_isIntegralHom`, resting on Étale
> Cohomology 04FX for algebraic spaces, and the converse is
> `AlgebraicGeometry.Space.isIso_unit_app_of_supportOfSheaf_subset_of_isIntegralHom` together with
> the characterization of the essential image of a fully faithful right adjoint by invertibility
> of the unit.

```lean
theorem smallEtalePushforwardAb_essImage_iff_of_integral_universallyInjective (f : Y ⟶ X)
    (hf : IsIntegralHom B S hS f.hom) (hui : UniversallyInjective B S hS f.hom)
    (F : Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1}) :
    (smallEtaleAbelianPushforward.{u + 1} B S hS f
        (relativelyRepresentable_of_isIntegralHom B S hS f hf)).essImage F ↔
      supportOfSheaf B S hS X.1 F ⊆ Set.range (pointsMap B S hS Y.1 f.hom)
```

**`AlgebraicGeometry.Space.smallEtalePushforward_essImage_iff_of_integral_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSetEssentialImage.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSetEssentialImage.lean#L362). The attribute's comment: “part (1): the essential image, for an integral and universally injective morphism of algebraic spaces”.

> **Stacks 0AEH, part (1), the essential image.** For an integral and universally injective
> morphism `f : Y ⟶ X` of algebraic spaces over a scheme `S`, a sheaf of sets on the small étale
> site of `X` lies in the essential image of the direct image along `f` exactly when its
> restriction to the open complement of the image of the point set of `Y` is the singleton sheaf.
>
> One direction is Étale Cohomology 04FX for sheaves of sets,
> `AlgebraicGeometry.Space.isTerminal_inverseImage_pushforward_integralComplement`. For the other,
> the direct image is fully faithful, so membership of the essential image is invertibility of the
> unit `F ⟶ f_*f^{-1}F`; the unit becomes invertible under `f^{-1}` by the triangle identity and
> under restriction to the complement because both sides are then the singleton sheaf, and a map
> of sheaves of sets invertible on both is invertible, every geometric point of `X` lying either
> on the image of `f` or on its complement.

```lean
theorem smallEtalePushforward_essImage_iff_of_integral_universallyInjective (f : Y ⟶ X)
    (hf : IsIntegralHom B S hS f.hom) (hui : UniversallyInjective B S hS f.hom)
    (F : Sheaf (SmallEtale.topology B S hS X.1) (Type (u + 1))) :
    (smallToposMorphism B S hS f).pushforward.essImage F ↔
      Nonempty (IsTerminal ((smallToposMorphism B S hS
        (integralComplementHom B S hS f hf)).inverseImage.obj F))
```

**`AlgebraicGeometry.Space.fullyFaithfulSmallEtaleSetPushforwardOfIntegralUniversallyInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean#L130). The attribute's comment: “part (1): full faithfulness of the direct image on sheaves of sets”.

> **Stacks 0AEH, part (1), full faithfulness.** For an integral and universally injective
> morphism `f : Y ⟶ X` of algebraic spaces over a scheme `S`, the direct image of sheaves of sets
> along `f` — restriction along the chart base-change morphism of small étale sites of
> Stacks 03G2, part (4) — is fully faithful, at any coefficient universe.

```lean
def fullyFaithfulSmallEtaleSetPushforwardOfIntegralUniversallyInjective (f : Y ⟶ X)
    (hf : IsIntegralHom B S hS f.hom) (hui : UniversallyInjective B S hS f.hom) :
    letI := (smallBaseChange_isMorphismOfSites B S hS f
      (relativelyRepresentable_of_isIntegralHom B S hS f hf)).toIsContinuous
    ((smallBaseChange B S hS f
      (relativelyRepresentable_of_isIntegralHom B S hS f hf)).sheafPushforwardContinuous
        (Type w) (SmallEtale.topology B S hS X.1)
        (SmallEtale.topology B S hS Y.1)).FullyFaithful
```

**`AlgebraicGeometry.Space.fullyFaithfulSmallEtalePushforwardOfIntegralUniversallyInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean#L148). The attribute's comment: “part (1): the direct image of the morphism of small étale topoi is fully faithful”.

> **Stacks 0AEH, part (1), full faithfulness, through the morphism of small étale topoi.**
> For an integral and universally injective morphism `f : Y ⟶ X` of algebraic spaces over a
> scheme `S`, the direct image of sheaves of sets along the morphism of small étale topoi of
> Stacks 03G2, part (3) is fully faithful.
>
> By Stacks 03G8 that direct image is restriction along chart base change, so this is the
> previous statement read through an identification and not a new proof.

```lean
def fullyFaithfulSmallEtalePushforwardOfIntegralUniversallyInjective (f : Y ⟶ X)
    (hf : IsIntegralHom B S hS f.hom) (hui : UniversallyInjective B S hS f.hom) :
    (smallToposMorphismTypeU B S hS f).pushforward.FullyFaithful
```

**`AlgebraicGeometry.Space.smallEtaleAdjunctionCounitIsIsoOfIntegralUniversallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean#L166). The attribute's comment: “trailing clause for sheaves of sets: the inverse image is a left inverse”.

> **Stacks 0AEH, the trailing clause, for sheaves of sets.** For an integral and universally
> injective morphism `f : Y ⟶ X` of algebraic spaces over a scheme `S` the counit
> `f^{-1}f_*\mathcal{G} ⟶ \mathcal{G}` of the inverse-image/direct-image adjunction on sheaves of
> sets is an isomorphism: the inverse image is a left inverse of the direct image.
>
> The counit of an adjunction is an isomorphism exactly when the right adjoint is fully
> faithful.

```lean
theorem smallEtaleAdjunctionCounitIsIsoOfIntegralUniversallyInjective (f : Y ⟶ X)
    (hf : IsIntegralHom B S hS f.hom) (hui : UniversallyInjective B S hS f.hom)
    (G : Sheaf (SmallEtale.topology B S hS Y.1) (Type (max (u + 1) v))) :
    letI := (smallBaseChange_isMorphismOfSites B S hS f
      (relativelyRepresentable_of_isIntegralHom B S hS f hf)).toIsContinuous
    IsIso (((smallBaseChange B S hS f
      (relativelyRepresentable_of_isIntegralHom B S hS f hf)).sheafAdjunctionContinuous
        (Type (max (u + 1) v)) (SmallEtale.topology B S hS X.1)
        (SmallEtale.topology B S hS Y.1)).counit.app G)
```

**`AlgebraicGeometry.Space.smallEtalePullbackPushforwardCounitIsoOfIntegralUniversallyInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean#L185). The attribute's comment: “trailing clause for sheaves of sets, as a natural isomorphism f\_* f^\{-1} ≅ 1”.

> **Stacks 0AEH, the trailing clause, for sheaves of sets, as a natural isomorphism.** For an
> integral and universally injective morphism `f : Y ⟶ X` of algebraic spaces over a scheme `S`
> the counit of the adjunction of the morphism of small étale topoi of Stacks 03G2, part (3) is a
> natural isomorphism `f_* ⋙ f^{-1} ≅ 𝟭`.

```lean
def smallEtalePullbackPushforwardCounitIsoOfIntegralUniversallyInjective (f : Y ⟶ X)
    (hf : IsIntegralHom B S hS f.hom) (hui : UniversallyInjective B S hS f.hom) :
    (smallToposMorphismTypeU B S hS f).pushforward ⋙
        (smallToposMorphismTypeU B S hS f).inverseImage ≅
      𝟭 (Sheaf (SmallEtale.topology B S hS Y.1) (Type u))
```

**`AlgebraicGeometry.Space.fullyFaithfulSmallEtaleAbelianPushforwardOfIntegralUniversallyInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean#L207). The attribute's comment: “part (2): full faithfulness of the direct image on abelian sheaves”.

> **Stacks 0AEH, part (2), full faithfulness.** For an integral and universally injective
> morphism `f : Y ⟶ X` of algebraic spaces over a scheme `S`, the direct image of sheaves of
> *abelian groups* along `f` is fully faithful.
>
> Full faithfulness of restriction along a cover-dense, locally full, continuous functor does not
> depend on the category of coefficients, so this is
> `AlgebraicGeometry.Space.fullyFaithfulSmallEtaleRestrictionOfIntegralUniversallyInjective` at
> the category of abelian groups.

```lean
def fullyFaithfulSmallEtaleAbelianPushforwardOfIntegralUniversallyInjective (f : Y ⟶ X)
    (hf : IsIntegralHom B S hS f.hom) (hui : UniversallyInjective B S hS f.hom) :
    letI := (smallBaseChange_isMorphismOfSites B S hS f
      (relativelyRepresentable_of_isIntegralHom B S hS f hf)).toIsContinuous
    ((smallBaseChange B S hS f
      (relativelyRepresentable_of_isIntegralHom B S hS f hf)).sheafPushforwardContinuous
        AddCommGrpCat.{w} (SmallEtale.topology B S hS X.1)
        (SmallEtale.topology B S hS Y.1)).FullyFaithful
```

**`AlgebraicGeometry.Space.smallEtalePushforwardAbIsRightAdjointOfIntegralUniversallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean#L224). The attribute's comment: “part (2): the direct image of abelian sheaves has the inverse image as left adjoint”.

> **Stacks 0AEH, part (2), existence of the inverse image.** For an integral morphism
> `f : Y ⟶ X` of algebraic spaces over a scheme `S`, the direct image of abelian sheaves along
> `f` is a right adjoint, so that the inverse image of part (2) exists.
>
> Universal injectivity is not used: representability is all this needs.

```lean
theorem smallEtalePushforwardAbIsRightAdjointOfIntegralUniversallyInjective (f : Y ⟶ X)
    (hf : IsIntegralHom B S hS f.hom) :
    letI := (smallBaseChange_isMorphismOfSites B S hS f
      (relativelyRepresentable_of_isIntegralHom B S hS f hf)).toIsContinuous
    Nonempty (((smallBaseChange B S hS f
      (relativelyRepresentable_of_isIntegralHom B S hS f hf)).sheafPushforwardContinuous
        AddCommGrpCat.{max (u + 1) v} (SmallEtale.topology B S hS X.1)
        (SmallEtale.topology B S hS Y.1)).IsRightAdjoint)
```

**`AlgebraicGeometry.Space.smallEtaleAdjunctionCounitIsIsoAbelianOfIntegralUniversallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean#L244). The attribute's comment: “trailing clause for abelian sheaves: the inverse image is a left inverse”.

> **Stacks 0AEH, the trailing clause, for abelian sheaves.** For an integral and universally
> injective morphism `f : Y ⟶ X` of algebraic spaces over a scheme `S` the counit of the
> inverse-image/direct-image adjunction on abelian sheaves is an isomorphism: the inverse image is
> a left inverse of the direct image.
>
> The adjunction is the one whose existence is
> `AlgebraicGeometry.Space.smallEtalePushforwardAbIsRightAdjointOfIntegralUniversallyInjective`,
> as in the source, where part (2) presupposes it.

```lean
theorem smallEtaleAdjunctionCounitIsIsoAbelianOfIntegralUniversallyInjective (f : Y ⟶ X)
    (hf : IsIntegralHom B S hS f.hom) (hui : UniversallyInjective B S hS f.hom)
    (G : Sheaf (SmallEtale.topology B S hS Y.1) AddCommGrpCat.{max (u + 1) v}) :
    letI := (smallBaseChange_isMorphismOfSites B S hS f
      (relativelyRepresentable_of_isIntegralHom B S hS f hf)).toIsContinuous
    letI := Classical.choice (smallEtalePushforwardAb_isRightAdjoint.{v} B S hS f
      (relativelyRepresentable_of_isIntegralHom B S hS f hf))
    IsIso (((smallBaseChange B S hS f
      (relativelyRepresentable_of_isIntegralHom B S hS f hf)).sheafAdjunctionContinuous
        AddCommGrpCat.{max (u + 1) v} (SmallEtale.topology B S hS X.1)
        (SmallEtale.topology B S hS Y.1)).counit.app G)
```

**`AlgebraicGeometry.Space.smallEtaleAbelianPullbackPushforwardCounitIsoOfIntegralUniversallyInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralUniversallyInjectiveSmallEtale.lean#L265). The attribute's comment: “trailing clause for abelian sheaves, as a natural isomorphism f\_* f^\{-1} ≅ 1”.

> **Stacks 0AEH, the trailing clause, for abelian sheaves, as a natural isomorphism.** For an
> integral and universally injective morphism `f : Y ⟶ X` of algebraic spaces over a scheme `S`
> the counit of the adjunction of `CategoryTheory.Functor.sheafAdjunctionContinuous` for chart
> base change is a natural isomorphism `f_* ⋙ f^{-1} ≅ 𝟭`.

```lean
def smallEtaleAbelianPullbackPushforwardCounitIsoOfIntegralUniversallyInjective (f : Y ⟶ X)
    (hf : IsIntegralHom B S hS f.hom) (hui : UniversallyInjective B S hS f.hom) :
    letI := (smallBaseChange_isMorphismOfSites B S hS f
      (relativelyRepresentable_of_isIntegralHom B S hS f hf)).toIsContinuous
    letI := Classical.choice (smallEtalePushforwardAb_isRightAdjoint.{v} B S hS f
      (relativelyRepresentable_of_isIntegralHom B S hS f hf))
    (smallBaseChange B S hS f
        (relativelyRepresentable_of_isIntegralHom B S hS f hf)).sheafPushforwardContinuous
          AddCommGrpCat.{max (u + 1) v} (SmallEtale.topology B S hS X.1)
          (SmallEtale.topology B S hS Y.1) ⋙
      (smallBaseChange B S hS f
        (relativelyRepresentable_of_isIntegralHom B S hS f hf)).sheafPullback
          AddCommGrpCat.{max (u + 1) v} (SmallEtale.topology B S hS X.1)
          (SmallEtale.topology B S hS Y.1) ≅
      𝟭 (Sheaf (SmallEtale.topology B S hS Y.1) AddCommGrpCat.{max (u + 1) v})
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.53, Tag 05Z3](https://stacks.math.columbia.edu/tag/05Z3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
