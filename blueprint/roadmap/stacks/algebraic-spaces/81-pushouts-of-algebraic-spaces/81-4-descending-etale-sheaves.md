---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.SpacesEtale.isEquivalence_toDescentData_smallEtaleSheafSystem_of_isEtaleCovering, AlgebraicGeometry.Space.SpacesEtale.isEquivalence_toDescentData_spacesEtalePseudofunctor_of_isEtaleCovering, AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_isEtaleCovering, AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_surjective_integral, AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_surjective_proper, AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_surjective_flat_locallyOfFinitePresentation, AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_relativelyRepresentable, AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_representable_comp
statement: formalized
proof: formalized
---

# 81.4 Descending étale sheaves

Section 81.4 of the Stacks Project, [Tag 0GFR](https://stacks.math.columbia.edu/tag/0GFR). 7 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GFS, a lemma

[Tag 0GFS](https://stacks.math.columbia.edu/tag/0GFS) in the Stacks Project.

**`AlgebraicGeometry.Space.SpacesEtale.isEquivalence_toDescentData_smallEtaleSheafSystem_of_isEtaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleSheafDescent.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleSheafDescent.lean#L196).

> **Stacks 0GFS.** Let `X` be an algebraic space over a scheme `S` and let
> `{g i : Y i ⟶ X}` be an étale covering of algebraic spaces. Then sheaves of sets on the small
> étale site of `X` are equivalent, via the functor taking a sheaf to its canonical descent
> datum, to descent data for étale sheaves with respect to that covering: a sheaf on the small
> étale site of each `Y i`, together with transition isomorphisms over the overlaps satisfying
> the cocycle condition.

```lean
theorem isEquivalence_toDescentData_smallEtaleSheafSystem_of_isEtaleCovering
    [∀ (U : SpacesEtale B S hS X) (Z : _),
      HasLimitsOfShape
        (StructuredArrow Z (Space.comparisonFunctor B S hS U.obj.left).op) (Type (u + 1))]
    {I : Type t} (Y : I → AlgebraicSpaces B S hS) (g : ∀ i, Y i ⟶ X)
    (hg : IsEtaleCovering B S hS (fun i => (Y i).1) (fun i => (g i).hom)) :
    ((smallEtaleSheafSystem B S hS (X := X)).toDescentData
      (fun i => toFinal B S hS (etaleObject B S hS (g i) (hg.etale i)))).IsEquivalence
```

**`AlgebraicGeometry.Space.SpacesEtale.isEquivalence_toDescentData_spacesEtalePseudofunctor_of_isEtaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleGlobalDescent.lean, line 555](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleGlobalDescent.lean#L555). The attribute's comment: “for the pseudofunctor of spaces-étale inverse images”.

> **Stacks 0GFS for the pseudofunctor of spaces-étale inverse images.** Let `X` be an
> algebraic space over a scheme `S` and let `{g i : Y i ⟶ X}` be an étale covering of algebraic
> spaces. Then sheaves of sets on the spaces-étale site of `X` are equivalent, via the functor
> taking a sheaf to its canonical descent datum, to descent data for that covering: a
> spaces-étale sheaf on each `Y i`, together with transition isomorphisms over the overlaps
> satisfying the cocycle condition.

```lean
theorem isEquivalence_toDescentData_spacesEtalePseudofunctor_of_isEtaleCovering
    {I : Type t} (Y : I → AlgebraicSpaces B S hS) (g : ∀ i, Y i ⟶ X)
    (hg : IsEtaleCovering B S hS (fun i => (Y i).1) (fun i => (g i).hom)) :
    ((spacesEtalePseudofunctor B S hS).toDescentData g).IsEquivalence
```

## Tag 0GFT, a lemma

[Tag 0GFT](https://stacks.math.columbia.edu/tag/0GFT) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_isEtaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentEtaleLocal.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentEtaleLocal.lean#L374). The attribute's comment: “for the pseudofunctor of spaces-étale inverse images”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` and let `{g i : Y i ⟶ Y}` be an
> étale covering. If
> spaces-étale sheaves on `Y i` are equivalent, via the canonical descent datum, to descent data
> for the base change `X ×_Y Y i ⟶ Y i` of `f`, and likewise over each pairwise overlap
> `Y i ×_Y Y j`, then spaces-étale sheaves on `Y` are equivalent to descent data for `f`
> itself.

```lean
theorem isEquivalence_toDescentData_singleton_of_isEtaleCovering
    (hY : ∀ i, ((spacesEtalePseudofunctor B S hS).toDescentData
      (fun _ : Unit => (spacesChosenPullback B S hS f (g i)).p₂)).IsEquivalence)
    (hYY : ∀ i j, ((spacesEtalePseudofunctor B S hS).toDescentData
      (fun _ : Unit => (spacesChosenPullback B S hS f
        (spacesChosenPullback B S hS (g i) (g j)).p).p₂)).IsEquivalence) :
    ((spacesEtalePseudofunctor B S hS).toDescentData
      (fun _ : Unit => f)).IsEquivalence
```

## Tag 0GFU, a lemma

[Tag 0GFU](https://stacks.math.columbia.edu/tag/0GFU) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_surjective_integral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentRepresentableCover.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentRepresentableCover.lean#L193). The attribute's comment: “the surjective integral case, for the pseudofunctor of spaces-étale inverse images, granted the case of a representable target as the hypothesis `hsch`. Proved here: the étale-local reduction of the source, that is, that the conclusion for an arbitrary algebraic space `Y` follows from the case in which the target is a scheme -- a scheme atlas of `Y` is a one-member étale covering (Tag 025Y), the two base changes of `f` named by Tag 0GFT have representable target, and the representable surjective integral morphisms are stable under base change (Tag 02WE). NOT proved, and carried by `hsch`: the case of a scheme target, which the source deduces from Etale Cohomology Tag 0GEZ; that lemma is not in this library and rests in turn on the devissage of Tag 0GF1 and on the base-change theorem of Tag 0EYP. The other two cases of the source statement are separate declarations with their own hypothesis.”.

> **Stacks 0GFU, the surjective integral case.** Let `f : X ⟶ Y` be a morphism of algebraic
> spaces over `S` which is representable by schemes, surjective and integral. Then spaces-étale
> sheaves on `Y` are equivalent, via the canonical descent datum, to descent data for the covering
> `{X ⟶ Y}`, granted the same assertion for a morphism with representable target.

```lean
theorem isEquivalence_toDescentData_singleton_of_surjective_integral
    (hsch : SpacesEtaleDescentOverRepresentable B S hS
      (MorphismProperty.inverseImage
        (@AlgebraicGeometry.Surjective.{u} ⊓ @AlgebraicGeometry.IsIntegralHom.{u})
        (BigFppfOver.toScheme B S hS)).presheaf)
    (f : X ⟶ Y)
    (hsurj : (MorphismProperty.inverseImage (@AlgebraicGeometry.Surjective.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f.hom)
    (hint : (MorphismProperty.inverseImage (@AlgebraicGeometry.IsIntegralHom.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f.hom) :
    ((spacesEtalePseudofunctor B S hS).toDescentData (fun _ : Unit => f)).IsEquivalence
```

**`AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_surjective_proper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentRepresentableCover.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentRepresentableCover.lean#L221). The attribute's comment: “the surjective proper case, for the pseudofunctor of spaces-étale inverse images, granted the case of a representable target as the hypothesis `hsch`. Proved here: the étale-local reduction of the source, that is, that the conclusion for an arbitrary algebraic space `Y` follows from the case in which the target is a scheme -- a scheme atlas of `Y` is a one-member étale covering (Tag 025Y), the two base changes of `f` named by Tag 0GFT have representable target, and the representable surjective proper morphisms are stable under base change (Tag 02WE). NOT proved, and carried by `hsch`: the case of a scheme target, which the source deduces from Etale Cohomology Tag 0GF0; that lemma is not in this library and rests in turn on the devissage of Tag 0GF1 and on the proper base-change theorem of Tag 0A3U. The other two cases of the source statement are separate declarations with their own hypothesis.”.

> **Stacks 0GFU, the surjective proper case.** Let `f : X ⟶ Y` be a morphism of algebraic
> spaces over `S` which is representable by schemes, surjective and proper. Then spaces-étale
> sheaves on `Y` are equivalent, via the canonical descent datum, to descent data for the covering
> `{X ⟶ Y}`, granted the same assertion for a morphism with representable target.

```lean
theorem isEquivalence_toDescentData_singleton_of_surjective_proper
    (hsch : SpacesEtaleDescentOverRepresentable B S hS
      (MorphismProperty.inverseImage
        (@AlgebraicGeometry.Surjective.{u} ⊓ @AlgebraicGeometry.IsProper.{u})
        (BigFppfOver.toScheme B S hS)).presheaf)
    (f : X ⟶ Y)
    (hsurj : (MorphismProperty.inverseImage (@AlgebraicGeometry.Surjective.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f.hom)
    (hproper : (MorphismProperty.inverseImage (@AlgebraicGeometry.IsProper.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f.hom) :
    ((spacesEtalePseudofunctor B S hS).toDescentData (fun _ : Unit => f)).IsEquivalence
```

**`AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_surjective_flat_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentRepresentableCover.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentRepresentableCover.lean#L251). The attribute's comment: “the surjective flat locally-of-finite-presentation case, for the pseudofunctor of spaces-étale inverse images, granted the case of a representable target as the hypothesis `hsch`. Proved here: the étale-local reduction of the source, that is, that the conclusion for an arbitrary algebraic space `Y` follows from the case in which the target is a scheme -- a scheme atlas of `Y` is a one-member étale covering (Tag 025Y), the two base changes of `f` named by Tag 0GFT have representable target, and the representable surjective flat morphisms locally of finite presentation are stable under base change (Tag 02WE). NOT proved, and carried by `hsch`: the case of a scheme target, which the source deduces from Etale Cohomology Tag 0GF2; that lemma is not in this library and rests in turn on the devissage of Tag 0GF1 and on the finite domination of an fppf covering of Tag 0CP0. The other two cases of the source statement are separate declarations with their own hypothesis.”.

> **Stacks 0GFU, the surjective flat locally finitely presented case.** Let `f : X ⟶ Y` be a
> morphism of algebraic spaces over `S` which is representable by schemes, surjective, flat and
> locally of finite presentation. Then spaces-étale sheaves on `Y` are equivalent, via the
> canonical descent datum, to descent data for the covering `{X ⟶ Y}`, granted the same assertion
> for a morphism with representable target.

```lean
theorem isEquivalence_toDescentData_singleton_of_surjective_flat_locallyOfFinitePresentation
    (hsch : SpacesEtaleDescentOverRepresentable B S hS
      (MorphismProperty.inverseImage
        (@AlgebraicGeometry.Surjective.{u} ⊓ @AlgebraicGeometry.Flat.{u} ⊓
          @AlgebraicGeometry.LocallyOfFinitePresentation.{u})
        (BigFppfOver.toScheme B S hS)).presheaf)
    (f : X ⟶ Y)
    (hsurj : (MorphismProperty.inverseImage (@AlgebraicGeometry.Surjective.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f.hom)
    (hflat : (MorphismProperty.inverseImage (@AlgebraicGeometry.Flat.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f.hom)
    (hlfp : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.LocallyOfFinitePresentation.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f.hom) :
    ((spacesEtalePseudofunctor B S hS).toDescentData (fun _ : Unit => f)).IsEquivalence
```

**`AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_relativelyRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentSchemeTarget.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentSchemeTarget.lean#L187).

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is representable (by
> schemes) and is surjective and integral, or surjective and proper, or surjective, flat and locally
> of finite presentation. Then the functor from sheaves on the spaces-étale site of `Y` (that is,
> `Sh(Y_étale)`, Stacks 03G1) to descent data for étale sheaves with respect to `{X ⟶ Y}` is an
> equivalence of categories.

```lean
theorem isEquivalence_toDescentData_singleton_of_relativelyRepresentable
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hrep : yoneda.relativelyRepresentable f.hom)
    (hf : IsSurjectiveIntegralProperOrFlatLfp B S hS f) :
    ((spacesEtalePseudofunctor B S hS).toDescentData (fun _ : Unit => f)).IsEquivalence
```

## Tag 0GFV, a lemma

[Tag 0GFV](https://stacks.math.columbia.edu/tag/0GFV) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_representable_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentRepresentableRefinement.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentRepresentableRefinement.lean#L235). The attribute's comment: “granted `h0GFU`, the conclusion of Stacks 0GFU: that for EVERY morphism of algebraic spaces over `S` which is representable by schemes and is surjective and integral, surjective and proper, or surjective and flat and locally of finite presentation, spaces-étale sheaves on its target are equivalent to descent data for the singleton family it generates. That is the special case `π = 𝟙 X` of this statement, in which the morphism carrying the hypotheses is the morphism of the descent problem itself, so it is NOT the universally quantified form of this conclusion: this conclusion asks for descent along `f` while the hypotheses are carried by `π ≫ f`, and `f` itself is neither representable nor surjective in any instance of the grant. The implication runs one way only — the grant is an instance of this conclusion, and getting this conclusion back out of the grant is exactly the refinement step. That step, Stacks 0GEA, is proved and not granted: `CategoryTheory.Pseudofunctor.isEquivalence_toDescentData_of_homOver` of this file restates the library's `CategoryTheory.Functor.isEquivalence_toFamilyDescentDatum_of_homOver` at an arbitrary pseudofunctor, and its fibre-product and base-change obligations are discharged here”.

> **Stacks 0GFV for the pseudofunctor of spaces-étale inverse images.** Let `f : X ⟶ Y` be a
> morphism of algebraic spaces over `S` and let `π : X' ⟶ X` be a morphism of algebraic spaces.
> If the composite `π ≫ f` is representable by schemes and is surjective and integral, surjective
> and proper, or surjective and flat and locally of finite presentation, then spaces-étale sheaves
> on `Y` are equivalent, via the canonical descent datum, to descent data for the singleton family
> `{X ⟶ Y}`. No hypothesis is placed on `f` itself.
>
> The conclusion of Stacks 0GFU is granted as `h0GFU`; see the implementation notes of the file.

```lean
theorem isEquivalence_toDescentData_singleton_of_representable_comp
    (h0GFU : ∀ {X₀ Y₀ : AlgebraicSpaces B S hS} (f₀ : X₀ ⟶ Y₀),
      yoneda.relativelyRepresentable f₀.hom →
      IsSurjectiveIntegralProperOrFlatLfp B S hS f₀ →
      ((spacesEtalePseudofunctor B S hS).toDescentData
        (fun _ : Unit => f₀)).IsEquivalence)
    {X' X Y : AlgebraicSpaces B S hS} (π : X' ⟶ X) (f : X ⟶ Y)
    (hrep : yoneda.relativelyRepresentable (π ≫ f).hom)
    (hcov : IsSurjectiveIntegralProperOrFlatLfp B S hS (π ≫ f)) :
    ((spacesEtalePseudofunctor B S hS).toDescentData
      (fun _ : Unit => f)).IsEquivalence
```

**`AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_relativelyRepresentable_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentSchemeTarget.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentSchemeTarget.lean#L218).

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` and let `π : X' ⟶ X` be a
> morphism of algebraic spaces. Assume that `π ≫ f` is representable (by schemes) and is surjective
> and integral, or surjective and proper, or surjective, flat and locally of finite presentation.
> Then the functor from sheaves on the spaces-étale site of `Y` to descent data for étale sheaves
> with respect to `{X ⟶ Y}` is an equivalence of categories.

```lean
theorem isEquivalence_toDescentData_singleton_of_relativelyRepresentable_comp
    {X' X Y : AlgebraicSpaces B S hS} (π : X' ⟶ X) (f : X ⟶ Y)
    (hrep : yoneda.relativelyRepresentable (π ≫ f).hom)
    (hcov : IsSurjectiveIntegralProperOrFlatLfp B S hS (π ≫ f)) :
    ((spacesEtalePseudofunctor B S hS).toDescentData (fun _ : Unit => f)).IsEquivalence
```

## Tag 0GFW, a lemma

[Tag 0GFW](https://stacks.math.columbia.edu/tag/0GFW) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_isSurjectiveIntegralProperOrFlatLfp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentProperSurjective.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentProperSurjective.lean#L201).

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is surjective and integral, or
> surjective and proper, or surjective, flat and locally of finite presentation. Then the functor
> from sheaves on the spaces-étale site of `Y` to descent data for étale sheaves with respect to
> `{X ⟶ Y}` is an equivalence of categories.

```lean
theorem isEquivalence_toDescentData_singleton_of_isSurjectiveIntegralProperOrFlatLfp
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : IsSurjectiveIntegralProperOrFlatLfp B S hS f) :
    ((spacesEtalePseudofunctor B S hS).toDescentData (fun _ : Unit => f)).IsEquivalence
```

**`AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_isSurjectiveDescentMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentSurjective.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentSurjective.lean#L197). The attribute's comment: “all three cases stated; the integral and flat cases are proved from Stacks 0GFV, carried as a hypothesis, and the proper case is carried whole as a hypothesis”.

> **Stacks 0GFW for the pseudofunctor of spaces-étale inverse images.** Let `f : X ⟶ Y` be a
> morphism of algebraic spaces over `S` which is surjective and integral, or surjective and
> proper, or surjective and flat and locally of finite presentation. Then sheaves on the
> spaces-étale site of `Y` are equivalent, through the canonical descent datum, to descent data
> for the one-member family `{f}`.
>
> All three cases are stated. The integral and the flat case are proved from `hGFV`, which is
> Stacks 0GFV; the proper case is the hypothesis `hproper`, carried whole.

```lean
theorem isEquivalence_toDescentData_singleton_of_isSurjectiveDescentMorphism
    (hGFV : DescentEffectiveAlongRepresentablePrecomposition B S hS)
    (hproper : DescentEffectiveAlongProperSurjective B S hS)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : IsSurjectiveDescentMorphism B S hS f.hom) :
    ((spacesEtalePseudofunctor B S hS).toDescentData (fun _ : Unit => f)).IsEquivalence
```

## Tag 0GFX, a lemma

[Tag 0GFX](https://stacks.math.columbia.edu/tag/0GFX) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_toDescentData_of_isFppfCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentFppfCovering.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentFppfCovering.lean#L112).

> Let `S` be a scheme and let `{f i : X i ⟶ Y}` be an fppf covering of algebraic spaces over
> `S`. Then the functor from sheaves on the spaces-étale site of `Y` (that is, `Sh(Y_étale)`) to
> descent data for étale sheaves with respect to `{f i : X i ⟶ Y}` is an equivalence of
> categories.

```lean
theorem isEquivalence_toDescentData_of_isFppfCovering {I : Type v}
    {X : I → AlgebraicSpaces B S hS} {Y : AlgebraicSpaces B S hS} (f : ∀ i, X i ⟶ Y)
    (hf : IsFppfCovering B S hS (fun i => (X i).1) (fun i => (f i).hom)) :
    ((spacesEtalePseudofunctor B S hS).toDescentData f).IsEquivalence
```

## Tag 0GFY, a lemma

[Tag 0GFY](https://stacks.math.columbia.edu/tag/0GFY) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_spacesModificationRestriction_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleModificationProper.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleModificationProper.lean#L68).

> **[Stacks, Tag 0GFY].** Let `S` be a scheme, let `f : Y ⟶ X` be a proper morphism of
> algebraic spaces over `S`, let `i : Z ⟶ X` be a closed immersion, and let `E = Z ×_X Y` with
> projections `j : E ⟶ Y` and `g : E ⟶ Z`. Suppose `f` is an isomorphism over the open complement
> `u : X ∖ Z ⟶ X` of `Z`: the projection `fU : V ⟶ X ∖ Z` of a fibre product
> `V = (X ∖ Z) ×_X Y` is an isomorphism. Then the functor
> `Sh(X_étale) ⥤ Sh(Y_étale) ×_{Sh(E_étale)} Sh(Z_étale)`, `F ↦ (f⁻¹F, i⁻¹F)`, is an equivalence
> of categories.

```lean
theorem isEquivalence_spacesModificationRestriction_of_isProper
    (hf : IsProper B S hS f.hom) (hi : IsClosedImmersion B S hS i.hom)
    (sq : IsPullback j g f i)
    {V : AlgebraicSpaces B S hS} (w' : V ⟶ Y)
    (fU : V ⟶ closedImmersionComplement B S hS i hi) [IsIso fU]
    (sqU : IsPullback w' fU f (closedImmersionComplementHom B S hS i hi)) :
    (spacesModificationRestriction B S hS f i j g sq.w).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 81.4, Tag 0GFR](https://stacks.math.columbia.edu/tag/0GFR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
