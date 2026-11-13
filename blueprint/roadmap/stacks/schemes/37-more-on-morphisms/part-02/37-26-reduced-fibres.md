---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_open_forall_not_isReduced_fiber, AlgebraicGeometry.geometricallyReduced_fiber_set_eq_preimage_of_isPullback, AlgebraicGeometry.exists_open_forall_not_geometricallyReduced_fiber, AlgebraicGeometry.exists_opens_nonempty_geometricallyReduced_morphismRestrict_of_finiteType, AlgebraicGeometry.isLocallyConstructible_geometricallyReduced_fiber_of_isAffine, AlgebraicGeometry.isLocallyConstructible_geometricallyReduced_fiber, AlgebraicGeometry.isReduced_of_isProper_over_dvr_of_isReduced_specialFiber, AlgebraicGeometry.isReduced_genericFiber_of_isProper_over_dvr_of_isReduced_specialFiber
statement: formalized
proof: formalized
---

# 37.26 Reduced fibres

Section 37.26 of the Stacks Project, [Tag 0574](https://stacks.math.columbia.edu/tag/0574). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0575, a lemma

[Tag 0575](https://stacks.math.columbia.edu/tag/0575) in the Stacks Project.

**`AlgebraicGeometry.exists_open_forall_not_isReduced_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/Reduced.lean, line 614](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/Reduced.lean#L614). References: EGA IV (9.7.2), “more general”.

> **Stacks Project, Tag 0575.** If the generic fibre of a finite type morphism to an
> irreducible scheme is nonreduced, then every fibre over a suitable nonempty open subset of
> the target is nonreduced.

```lean
theorem exists_open_forall_not_isReduced_fiber
    {X Y : AlgebraicGeometry.Scheme.{u}} (f : X ⟶ Y)
    [IrreducibleSpace Y] [AlgebraicGeometry.LocallyOfFiniteType f]
    [AlgebraicGeometry.QuasiCompact f] (η : Y) (hη : IsGenericPoint η Set.univ)
    (h : ¬ AlgebraicGeometry.IsReduced (f.fiber η)) :
    ∃ V : Set Y, IsOpen V ∧ V.Nonempty ∧
      ∀ y ∈ V, ¬ AlgebraicGeometry.IsReduced (f.fiber y)
```

## Tag 0576, a lemma

[Tag 0576](https://stacks.math.columbia.edu/tag/0576) in the Stacks Project.

**`AlgebraicGeometry.geometricallyReduced_fiber_set_eq_preimage_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/Reduced.lean, line 641](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/Reduced.lean#L641).

> The locus of geometrically reduced fibres commutes with arbitrary base change.

```lean
theorem geometricallyReduced_fiber_set_eq_preimage_of_isPullback
    {X Y X' Y' : Scheme.{u}} (f : X ⟶ Y) (f' : X' ⟶ Y') (i : X' ⟶ X) (g : Y' ⟶ Y)
    (h : IsPullback i f' f g) :
    {y' : Y' | GeometricallyReduced (f'.fiberToSpecResidueField y')} =
      g ⁻¹' {y : Y | GeometricallyReduced (f.fiberToSpecResidueField y)}
```

## Tag 0577, a lemma

[Tag 0577](https://stacks.math.columbia.edu/tag/0577) in the Stacks Project.

**`AlgebraicGeometry.exists_open_forall_not_geometricallyReduced_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/NonReducedGenericFibre.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/NonReducedGenericFibre.lean#L43).

> If the generic fibre of a finite type morphism to an irreducible scheme is not geometrically
> reduced, then every fibre over a suitable nonempty open subset of the target is not geometrically
> reduced.

```lean
theorem exists_open_forall_not_geometricallyReduced_fiber
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IrreducibleSpace Y] [LocallyOfFiniteType f]
    [QuasiCompact f] (η : Y) (hη : IsGenericPoint η Set.univ)
    (h : ¬ GeometricallyReduced (f.fiberToSpecResidueField η)) :
    ∃ V : Set Y, IsOpen V ∧ V.Nonempty ∧
      ∀ y ∈ V, ¬ GeometricallyReduced (f.fiberToSpecResidueField y)
```

## Tag 0578, a lemma

[Tag 0578](https://stacks.math.columbia.edu/tag/0578) in the Stacks Project.

**`AlgebraicGeometry.exists_opens_nonempty_geometricallyReduced_morphismRestrict_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibre/OpenLocus.lean, line 707](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibre/OpenLocus.lean#L707).

> **Stacks Project, Tag 0578.** Let `f : X ⟶ Y` be a morphism of finite type onto an
> irreducible scheme with generic point `η`. If the fibre of `f` over `η` is geometrically reduced,
> then there is a nonempty open subscheme `V ⊆ Y` such that `X_V ⟶ V` has geometrically reduced
> fibres.
>
> Finite presentation is reached by the source's own bridge, Stacks 052A. The base is replaced by
> its reduction `r : Y_red ⟶ Y`, which is a universal homeomorphism, so it carries opens and
> generic points across and, by Stacks 0576, carries the geometrically reduced fibre locus of the
> base change back to that of `f`. Over the reduced base generic flatness
> `AlgebraicGeometry.exists_dense_open_flat_finitePresentation_structureSheaf` supplies a dense
> open `U ⊆ Y_red` over which the base change is of finite presentation; the generic point lies in
> `U` because `U` is dense, so the finite presentation case applies over `U` and produces an open
> subset of `U` inside the locus and containing the generic point. Its image in `Y` under the open
> immersion of `U` followed by the homeomorphism `r` is open, nonempty and inside the locus of
> `f`.

```lean
theorem exists_opens_nonempty_geometricallyReduced_morphismRestrict_of_finiteType
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IrreducibleSpace Y]
    [LocallyOfFiniteType f] [QuasiCompact f] (η : Y)
    (hη : IsGenericPoint η (Set.univ : Set Y))
    [GeometricallyReduced (f.fiberToSpecResidueField η)] :
    ∃ V : Y.Opens, Nonempty V ∧ GeometricallyReduced (f ∣_ V)
```

## Tag 0579, a lemma

[Tag 0579](https://stacks.math.columbia.edu/tag/0579) in the Stacks Project.

**`AlgebraicGeometry.isLocallyConstructible_geometricallyReduced_fiber_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Fibres/ReducedFibreLocus.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Fibres/ReducedFibreLocus.lean#L164). The attribute's comment: “affine Noetherian case: `X` and `S` affine with `S` locally Noetherian. The source states the lemma for an arbitrary quasi-compact morphism locally of finite presentation.”. References: EGA IV (9.9.3), “affine Noeth., reduced”; EGA IV (9.9.5), “reduced fibres, affine”; EGA IV (9.7.7), “(iii), affine Noeth.”.

> **The affine Noetherian case of Stacks 0579.** For a morphism `g : X ⟶ S` of finite
> presentation between affine schemes with `S` locally Noetherian, the set of points of `S` whose
> fibre is geometrically reduced is locally constructible.
>
> Comparing `g` with `Spec Γ(X, ⊤) ⟶ Spec Γ(S, ⊤)` gives a cartesian square with isomorphisms along
> the top and bottom, so Stacks 0576 identifies the locus with the inverse image of the locus of the
> latter; that locus is `Algebra.geometricallyReducedFibreLocus Γ(S, ⊤) Γ(X, ⊤)` by
> `AlgebraicGeometry.geometricallyReduced_fiberToSpecResidueField_specMap_iff`, which is
> constructible by `Algebra.isConstructible_geometricallyReducedFibreLocus'`; and Stacks 054I takes
> local constructibility back along the isomorphism.

```lean
theorem isLocallyConstructible_geometricallyReduced_fiber_of_isAffine {X S : Scheme.{u}}
    (g : X ⟶ S) [IsAffine X] [IsAffine S] [IsLocallyNoetherian S] (hg : FinitePresentation g) :
    IsLocallyConstructible {y : S | GeometricallyReduced (g.fiberToSpecResidueField y)}
```

**`AlgebraicGeometry.isLocallyConstructible_geometricallyReduced_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibre/OpenLocus.lean, line 610](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibre/OpenLocus.lean#L610). References: EGA IV (9.7.7), “more general”.

> **Stacks Project, Tag 0579.** Let `f : X ⟶ Y` be a quasi-compact morphism of schemes which
> is locally of finite presentation. Then the set of points of `Y` whose fibre is geometrically
> reduced is locally constructible in `Y`.
>
> Local constructibility is tested on the affine opens of `Y`
> (`AlgebraicGeometry.isLocallyConstructible_iff_forall_affineOpens`). Over an affine open `U` the
> restriction `f ∣_ U` is again quasi-compact and locally of finite presentation, and its
> geometrically reduced fibre locus is the inverse image of that of `f` by Stacks 0576, so
> `AlgebraicGeometry.isConstructible_geometricallyReduced_fiber_of_isAffine_target` applies.

```lean
theorem isLocallyConstructible_geometricallyReduced_fiber {X Y : Scheme.{u}} (f : X ⟶ Y)
    [QuasiCompact f] [LocallyOfFinitePresentation f] :
    IsLocallyConstructible {y : Y | GeometricallyReduced (f.fiberToSpecResidueField y)}
```

## Tag 0C0D, a lemma

[Tag 0C0D](https://stacks.math.columbia.edu/tag/0C0D) in the Stacks Project.

**`AlgebraicGeometry.isReduced_of_isProper_over_dvr_of_isReduced_specialFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibre/ProperOverDvr.lean, line 572](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibre/ProperOverDvr.lean#L572). The attribute's comment: “total space”.

> **Stacks Project, Tag 0C0D (total space).** A proper scheme over a discrete valuation
> ring is reduced if every irreducible component dominates the base and the special fibre is
> reduced.

```lean
theorem isReduced_of_isProper_over_dvr_of_isReduced_specialFiber
    {R : Type u} [CommRing R] [IsDomain R] [IsDiscreteValuationRing R]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of R)) [IsProper f]
    (hcomponents : ∀ Z ∈ irreducibleComponents X, Dense (f '' Z))
    [IsReduced (f.fiber (IsLocalRing.closedPoint (CommRingCat.of R)))] :
    IsReduced X
```

**`AlgebraicGeometry.isReduced_genericFiber_of_isProper_over_dvr_of_isReduced_specialFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibre/ProperOverDvr.lean, line 592](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibre/ProperOverDvr.lean#L592). The attribute's comment: “generic fibre”.

> **Stacks Project, Tag 0C0D (generic fibre).** A proper scheme over a discrete valuation
> ring has reduced generic fibre if every irreducible component dominates the base and the
> special fibre is reduced.

```lean
theorem isReduced_genericFiber_of_isProper_over_dvr_of_isReduced_specialFiber
    {R : Type u} [CommRing R] [IsDomain R] [IsDiscreteValuationRing R]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of R)) [IsProper f]
    (hcomponents : ∀ Z ∈ irreducibleComponents X, Dense (f '' Z))
    [IsReduced (f.fiber (IsLocalRing.closedPoint (CommRingCat.of R)))] :
    IsReduced (f.fiber (⟨⊥, inferInstance⟩ : PrimeSpectrum R))
```

## Tag 0C0E, a lemma

[Tag 0C0E](https://stacks.math.columbia.edu/tag/0C0E) in the Stacks Project.

**`AlgebraicGeometry.isOpen_geometricallyReduced_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibre/OpenLocus.lean, line 527](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ReducedFibre/OpenLocus.lean#L527).

> **Stacks Project, Tag 0C0E.** The geometrically reduced fibres of a flat, proper, finitely
> presented morphism form an open locus in the base.

```lean
theorem isOpen_geometricallyReduced_fiber
    {X Y : Scheme.{u}} (f : X ⟶ Y) [Flat f] [IsProper f]
    (hfp : FinitePresentation f) :
    IsOpen {y : Y | GeometricallyReduced (f.fiberToSpecResidueField y)}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.26, Tag 0574](https://stacks.math.columbia.edu/tag/0574)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
