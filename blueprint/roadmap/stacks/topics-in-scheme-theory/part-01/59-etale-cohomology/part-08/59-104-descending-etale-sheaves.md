---
declaration: section
origin: cited
lean: AlgebraicGeometry.smallEtaleSheafDescentFunctor_isEquivalence_of_section, AlgebraicGeometry.smallEtaleSheafDescentFunctor_isEquivalence_of_surjective_integral_unconditional, AlgebraicGeometry.smallEtaleSheafDescentFunctor_isEquivalence_of_isProper_of_surjective, AlgebraicGeometry.smallEtaleSheafDescentFunctor_isEquivalence_of_baseChange, AlgebraicGeometry.smallEtaleSheafDescentFunctor_isEquivalence_of_baseChange_id, AlgebraicGeometry.smallEtaleSheafDescentFunctor_isEquivalence_of_baseChange_of_surjective, AlgebraicGeometry.smallEtaleSheafDescentFunctor_isEquivalence_of_fppf_unconditional, AlgebraicGeometry.smallEtaleSheafFamilyDescentFunctor_isEquivalence_of_fppfCovering_unconditional
statement: formalized
proof: formalized
---

# 59.104 Descending étale sheaves

Section 59.104 of the Stacks Project, [Tag 0GEX](https://stacks.math.columbia.edu/tag/0GEX). 8 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GEY, a lemma

[Tag 0GEY](https://stacks.math.columbia.edu/tag/0GEY) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleSheafDescentFunctor_isEquivalence_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescent.lean, line 434](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescent.lean#L434).

> **Stacks 0GEY.** The canonical small étale sheaf descent functor for a morphism of schemes
> admitting a section is an equivalence.

```lean
public theorem smallEtaleSheafDescentFunctor_isEquivalence_of_section
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    (s : Y ⟶ X) (hs : s ≫ f = 𝟙 Y) :
    (smallEtaleSheafDescentFunctor B f).IsEquivalence
```

## Tag 0GEZ, a lemma

[Tag 0GEZ](https://stacks.math.columbia.edu/tag/0GEZ) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleSheafDescentFunctor_isEquivalence_of_surjective_integral_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescentIntegralSurjectiveGeneral.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescentIntegralSurjectiveGeneral.lean#L55). The attribute's comment: “The functor is the canonical descent functor `AlgebraicGeometry.smallEtaleSheafDescentFunctorGeneral`, sending a sheaf on `Y_etale` to its inverse image on `X_etale` with the canonical descent isomorphism. Sheaves take values in `Type (u + 1)`, the universe of the big étale site. Proved from the base-change isomorphism for small étale sheaves along integral morphisms [Stacks, Tag 0EYP], applied to `X ×_Y X ⟶ X` and to `X ×_Y X ×_Y X ⟶ X ×_Y X`.”.

> Let `f : X ⟶ Y` be a surjective integral morphism of a big étale site. The functor from sheaves
> of sets on the small étale site of `Y` to descent data for `{X ⟶ Y}` is an equivalence of
> categories.

```lean
public theorem smallEtaleSheafDescentFunctor_isEquivalence_of_surjective_integral_unconditional
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [Surjective (B.inclusion.map f)] [IsIntegralHom (B.inclusion.map f)] :
    (smallEtaleSheafDescentFunctorGeneral B f).IsEquivalence
```

## Tag 0GF0, a lemma

[Tag 0GF0](https://stacks.math.columbia.edu/tag/0GF0) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleSheafDescentFunctor_isEquivalence_of_isProper_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescentProperSurjectiveUnconditional.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescentProperSurjectiveUnconditional.lean#L115). The attribute's comment: “The schemes are the objects of a big étale site `B`, and the functor is the library's canonical descent functor `smallEtaleSheafDescentFunctor`, whose pseudofunctor is shown equal to the explicit inverse-image pseudofunctor of small étale sheaves.”. References: SGA 4 VIII (9.4).

> **Effective descent of small étale sheaves along a proper surjection.** For a surjective
> proper morphism `f : X ⟶ Y` of a big étale site, the functor sending a sheaf of sets on the small
> étale site of `Y` to its canonical descent datum for `{X ⟶ Y}` is an equivalence of
> categories.

```lean
public theorem smallEtaleSheafDescentFunctor_isEquivalence_of_isProper_of_surjective
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [Surjective (B.inclusion.map f)] [IsProper (B.inclusion.map f)] :
    (smallEtaleSheafDescentFunctor B f).IsEquivalence
```

## Tag 0GF1, a lemma

[Tag 0GF1](https://stacks.math.columbia.edu/tag/0GF1) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleSheafDescentFunctor_isEquivalence_of_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescentBaseChange.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescentBaseChange.lean#L110). The attribute's comment: “only the case of a `g` admitting a section, and with the two hypotheses of the source -- effectivity over `Z` and over `Z ×_Y Z` -- replaced by effectivity of descent along the base change `X ×_Y Z` read along its structure morphism to `Y` rather than along its projection to `Z`. The surjective integral and the surjective proper cases, where the content of the source lemma lies (these are the cases in which 0GEZ resp. 0GF0 supplies effective descent along `g`), are NOT proved here; neither is the passage from effectivity over `Z` and over `Z ×_Y Z` to effectivity over `Y` of the base change.”.

> Descent of small étale sheaves along `f : X ⟶ Y` is effective as soon as it is effective
> along the structure morphism `X ×_Y Z ⟶ Y` of the base change of `f` along a morphism
> `g : Z ⟶ Y` admitting a section.

```lean
public theorem smallEtaleSheafDescentFunctor_isEquivalence_of_baseChange
    (B : BigEtaleSite.{u}) {X Y Z : B.Scheme} (f : X ⟶ Y) (g : Z ⟶ Y) (s : Y ⟶ Z)
    (hs : s ≫ g = 𝟙 Y)
    (hXZ : (smallEtaleSheafDescentFunctor B (pullback.fst f g ≫ f)).IsEquivalence) :
    (smallEtaleSheafDescentFunctor B f).IsEquivalence
```

**`AlgebraicGeometry.smallEtaleSheafDescentFunctor_isEquivalence_of_baseChange_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescentBaseChange.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescentBaseChange.lean#L123). The attribute's comment: “the case `Z = Y`, `g = 𝟙 Y` of the source statement, with the hypothesis in the shape the source gives it, namely effectivity along the projection `X ×_Y Z ⟶ Z`. The hypothesis over `Z ×_Y Z` is not needed in this case. No other case of the source statement is proved.”.

> Descent of small étale sheaves along `f : X ⟶ Y` is effective as soon as it is effective
> along the projection `X ×_Y Y ⟶ Y`.

```lean
public theorem smallEtaleSheafDescentFunctor_isEquivalence_of_baseChange_id
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    (hZ : (smallEtaleSheafDescentFunctor B (pullback.snd f (𝟙 Y))).IsEquivalence) :
    (smallEtaleSheafDescentFunctor B f).IsEquivalence
```

**`AlgebraicGeometry.smallEtaleSheafDescentFunctor_isEquivalence_of_baseChange_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescentOfCoverBaseChange.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescentOfCoverBaseChange.lean#L120).

> **Descent of small étale sheaves, tested after a surjective integral or proper base
> change.** Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of a big étale site, with `g` surjective
> and either integral or proper. If the functors from sheaves on the small étale sites of `Z` and
> of `Z ×_Y Z` to descent data for `{X ×_Y Z ⟶ Z}` and for `{X ×_Y (Z ×_Y Z) ⟶ Z ×_Y Z}` are
> equivalences of categories, then so is the functor from sheaves on the small étale site of `Y`
> to descent data for `{X ⟶ Y}`.

```lean
public theorem smallEtaleSheafDescentFunctor_isEquivalence_of_baseChange_of_surjective
    (B : BigEtaleSite.{u}) {X Y Z : B.Scheme} (f : X ⟶ Y) (g : Z ⟶ Y)
    [Surjective (B.inclusion.map g)]
    (hg : IsIntegralHom (B.inclusion.map g) ∨ IsProper (B.inclusion.map g))
    (hZ : (smallEtaleSheafDescentFunctor B (pullback.snd f g)).IsEquivalence)
    (hZZ : (smallEtaleSheafDescentFunctor B
      (pullback.snd f (pullback.fst g g ≫ g))).IsEquivalence) :
    (smallEtaleSheafDescentFunctor B f).IsEquivalence
```

## Tag 0GF2, a lemma

[Tag 0GF2](https://stacks.math.columbia.edu/tag/0GF2) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleSheafDescentFunctor_isEquivalence_of_fppf_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescentFppfCoveringUnconditional.lean, line 406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescentFppfCoveringUnconditional.lean#L406).

> **[Stacks, Tag 0GF2].** Let `f : X ⟶ Y` be a morphism of a big étale site which is
> surjective, flat and locally of finite presentation. Then the canonical functor from sheaves on
> the small étale site of `Y` to descent data for `{X ⟶ Y}` is an equivalence of categories.
>
> This is [Stacks, Tag 0GF3] for the one-member fppf covering `{f}`,
> `smallEtaleSheafFamilyDescentFunctor_isEquivalence_of_fppfCovering_unconditional`, whose
> proof is the source's proof of this lemma: the problem is local on `Y`, which reduces it to a
> quasi-compact quasi-separated base; there [Stacks, Tag 0CP0] supplies a finite surjective
> `Z ⟶ Y` with an open covering of `Z` factoring through `X`, the dévissage of [Stacks, Tag 0GF1]
> replaces `Y` by `Z` and `Z ×_Y Z`, and over those `f` has sections Zariski locally, which is
> [Stacks, Tag 0GEY] after localizing once more.

```lean
public theorem smallEtaleSheafDescentFunctor_isEquivalence_of_fppf_unconditional
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y) [Surjective (B.inclusion.map f)]
    [Flat (B.inclusion.map f)] [LocallyOfFinitePresentation (B.inclusion.map f)] :
    (smallEtaleSheafDescentFunctorGeneral B f).IsEquivalence
```

## Tag 0GF3, a lemma

[Tag 0GF3](https://stacks.math.columbia.edu/tag/0GF3) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleSheafFamilyDescentFunctor_isEquivalence_of_fppfCovering_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescentFppfCoveringUnconditional.lean, line 368](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafDescentFppfCoveringUnconditional.lean#L368).

> **[Stacks, Tag 0GF3].** Let `{f i : X i ⟶ Y}` be a family of morphisms of a big étale site
> whose underlying family of morphisms of schemes is an fppf covering. Then the canonical functor
> from sheaves on the small étale site of `Y` to descent data for small étale sheaves with respect
> to the covering is an equivalence of categories.
>
> The base is covered by affine opens `V k`; each `V k ×_Y V l` and each `V k ×_Y V l ×_Y V m` is
> an open subscheme of the affine `V k`, hence quasi-separated, so the quasi-separated case
> `smallEtaleSheafFamilyDescentFunctor_isEquivalence_of_fppfCovering_of_quasiSeparated`
> applies to the base change of the covering to each of them, and descent is local on the base
> (`AlgebraicGeometry.isEquivalence_toDescentData_smallEtaleSheafPullbackSystem_of_openCover`).
> The quasi-separated case is reduced in the same way to the quasi-compact quasi-separated case,
> which is the source's argument for [Stacks, Tag 0GF2] run for a family: [Stacks, Tag 0CP0], the
> integral branch of [Stacks, Tag 0GF1], and sections Zariski locally. The source instead applies
> [Stacks, Tag 0GF2] to the single morphism `∐ X i ⟶ Y`; the family is treated directly here.

```lean
public theorem smallEtaleSheafFamilyDescentFunctor_isEquivalence_of_fppfCovering_unconditional
    (B : BigEtaleSite.{u}) {I : Type t} {X : I → B.Scheme} {Y : B.Scheme} (f : ∀ i, X i ⟶ Y)
    (hf : Presieve.ofArrows (fun i ↦ B.inclusion.obj (X i)) (fun i ↦ B.inclusion.map (f i)) ∈
      Scheme.fppfPrecoverage (B.inclusion.obj Y)) :
    (smallEtaleSheafFamilyDescentFunctorGeneral B f).IsEquivalence
```

## Tag 0GF4, a lemma

[Tag 0GF4](https://stacks.math.columbia.edu/tag/0GF4) in the Stacks Project.

**`Stacks.EtaleCohomology.isEquivalence_smallEtaleSheafToCategoricalPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BlowUpSquare/SetSheafEquivalence.lean, line 479](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BlowUpSquare/SetSheafEquivalence.lean#L479).

> **Stacks Project, Tag 0GF4.** Let `f : X' ⟶ X` be a proper morphism of schemes, `i : Z ⟶ X`
> a closed immersion and `E = Z ×_X X'` with projections `j : E ⟶ X'` and `g : E ⟶ Z`. If `f` is
> an isomorphism over the open complement `U` of `Z`, the functor
> `Sh(X_étale) ⥤ Sh(X'_étale) ×_{Sh(E_étale)} Sh(Z_étale)`, `F ↦ (f⁻¹ F, i⁻¹ F, c)` with `c` the
> canonical isomorphism `j⁻¹ f⁻¹ F ≅ g⁻¹ i⁻¹ F`, is an equivalence of categories.

```lean
theorem isEquivalence_smallEtaleSheafToCategoricalPullback (U : X.Opens)
    (hU : (U : Set X) = (Set.range i.base)ᶜ) [IsIso (f ∣_ U)] :
    (smallEtaleSheafToCategoricalPullback.{u, 0} f i j g sq.w).IsEquivalence
```

## Tag 0GF5, a lemma

[Tag 0GF5](https://stacks.math.columbia.edu/tag/0GF5) in the Stacks Project.

**`AlgebraicGeometry.BigHOver.isStackInGroupoids_etaleSheafGroupoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafHStack.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SheafHStack.lean#L228).

> **Stacks 0GF5.** The category fibred in groupoids over the big h site `(Sch/S)_h` whose fibre
> over `U` is the category of sheaves on the small étale site of `U` is a stack in groupoids.

```lean
public theorem isStackInGroupoids_etaleSheafGroupoid :
    (etaleSheafGroupoidProjection B E hBE S hS).IsStackInGroupoids.{w}
      (BigHOver.topology B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.104, Tag 0GEX](https://stacks.math.columbia.edu/tag/0GEX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
