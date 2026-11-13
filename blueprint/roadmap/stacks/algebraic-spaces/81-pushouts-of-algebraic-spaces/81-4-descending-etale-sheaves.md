---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.SpacesEtale.isEquivalence_toDescentData_smallEtaleSheafSystem_of_isEtaleCovering, AlgebraicGeometry.Space.SpacesEtale.isEquivalence_toDescentData_spacesEtalePseudofunctor_of_isEtaleCovering, AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_isEtaleCovering, AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_relativelyRepresentable, AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_relativelyRepresentable_comp, AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_isSurjectiveIntegralProperOrFlatLfp, AlgebraicGeometry.Space.isEquivalence_toDescentData_of_isFppfCovering, AlgebraicGeometry.Space.isEquivalence_spacesModificationRestriction_of_isProper
statement: formalized
proof: formalized
---

# 81.4 Descending étale sheaves

Section 81.4 of the Stacks Project, [Tag 0GFR](https://stacks.math.columbia.edu/tag/0GFR). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GFS, a lemma

[Tag 0GFS](https://stacks.math.columbia.edu/tag/0GFS) in the Stacks Project.

**`AlgebraicGeometry.Space.SpacesEtale.isEquivalence_toDescentData_smallEtaleSheafSystem_of_isEtaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleSheafDescent.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleSheafDescent.lean#L196).

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

**`AlgebraicGeometry.Space.SpacesEtale.isEquivalence_toDescentData_spacesEtalePseudofunctor_of_isEtaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleGlobalDescent.lean, line 555](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleGlobalDescent.lean#L555). The attribute's comment: “for the pseudofunctor of spaces-étale inverse images”.

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

**`AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_isEtaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentEtaleLocal.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentEtaleLocal.lean#L375). The attribute's comment: “for the pseudofunctor of spaces-étale inverse images”.

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

**`AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_relativelyRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentSchemeTarget.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentSchemeTarget.lean#L208).

> **Stacks 0GFU.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is
> representable (by schemes) and is surjective and integral, or surjective and proper, or
> surjective, flat and locally of finite presentation. Then the functor from sheaves on the
> spaces-étale site of `Y` (that is, `Sh(Y_étale)`, Stacks 03G1) to descent data for étale sheaves
> with respect to `{X ⟶ Y}` is an equivalence of categories.
>
> Nothing is assumed beyond the source's hypotheses: the case over a scheme base, which the three
> cases `isEquivalence_toDescentData_singleton_of_surjective_integral`, `…_of_surjective_proper`
> and `…_of_surjective_flat_locallyOfFinitePresentation` take as their hypothesis `hsch`, is
> discharged here by `spacesEtaleDescentOverRepresentable_of_smallEtale`.

```lean
theorem isEquivalence_toDescentData_singleton_of_relativelyRepresentable
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hrep : yoneda.relativelyRepresentable f.hom)
    (hf : IsSurjectiveIntegralProperOrFlatLfp B S hS f) :
    ((spacesEtalePseudofunctor B S hS).toDescentData (fun _ : Unit => f)).IsEquivalence
```

## Tag 0GFV, a lemma

[Tag 0GFV](https://stacks.math.columbia.edu/tag/0GFV) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_relativelyRepresentable_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentSchemeTarget.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentSchemeTarget.lean#L243). The attribute's comment: “Sh(Y\_étale) is the category of sheaves on the spaces-étale site of `Y`, equivalent to the small étale topos by Stacks 03G1; descent data for `{X ⟶ Y}` are those of the spaces-étale pseudofunctor along the singleton family. The proof combines Stacks 0GFU (`isEquivalence_toDescentData_singleton_of_relativelyRepresentable`) with the refinement principle Stacks 0GEA, via `isEquivalence_toDescentData_singleton_of_representable_comp`.”.

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

**`AlgebraicGeometry.Space.isEquivalence_toDescentData_singleton_of_isSurjectiveIntegralProperOrFlatLfp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentProperSurjective.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentProperSurjective.lean#L206).

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is surjective and integral, or
> surjective and proper, or surjective, flat and locally of finite presentation. Then the functor
> from sheaves on the spaces-étale site of `Y` to descent data for étale sheaves with respect to
> `{X ⟶ Y}` is an equivalence of categories.
>
> The proof applies the three-case analysis
> `Space.isEquivalence_toDescentData_singleton_of_isSurjectiveDescentMorphism`, which is untagged,
> to Stacks 0GFV (`Space.isEquivalence_toDescentData_singleton_of_relativelyRepresentable_comp`)
> and to the proper case (`Space.descentEffectiveAlongProperSurjective`).

```lean
theorem isEquivalence_toDescentData_singleton_of_isSurjectiveIntegralProperOrFlatLfp
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : IsSurjectiveIntegralProperOrFlatLfp B S hS f) :
    ((spacesEtalePseudofunctor B S hS).toDescentData (fun _ : Unit => f)).IsEquivalence
```

## Tag 0GFX, a lemma

[Tag 0GFX](https://stacks.math.columbia.edu/tag/0GFX) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_toDescentData_of_isFppfCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentFppfCovering.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleDescentFppfCovering.lean#L112).

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

**`AlgebraicGeometry.Space.isEquivalence_spacesModificationRestriction_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleModificationProper.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleModificationProper.lean#L68).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
