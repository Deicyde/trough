---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isGeometricallyReducedFibre_tfae, AlgebraicGeometry.Space.IsGeometricallyReducedFibreAt, AlgebraicGeometry.Space.geometricallyReducedFibreLocus_pullback, AlgebraicGeometry.Space.isEtaleLocallyConstructible_geometricallyReducedFibreLocus, AlgebraicGeometry.Space.isReduced_of_isReduced_specialFiber, AlgebraicGeometry.Space.isReduced_genericFiber_of_isReduced_specialFiber, AlgebraicGeometry.Space.isOpen_geometricallyReducedFibreLocus
statement: formalized
proof: formalized
---

# 76.29 Reduced fibres

Section 76.29 of the Stacks Project, [Tag 0E06](https://stacks.math.columbia.edu/tag/0E06). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E07, a lemma

[Tag 0E07](https://stacks.math.columbia.edu/tag/0E07) in the Stacks Project.

**`AlgebraicGeometry.Space.isGeometricallyReducedFibre_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricallyReduced.lean, line 442](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricallyReduced.lean#L442).

> **Stacks 0E07.** For a morphism `f : X ⟶ Y` of algebraic spaces over `S` and a point `y`
> of `|Y|` the following are equivalent: (1) the fibre `X_k` is geometrically reduced over `k`
> for *some* morphism `Spec k ⟶ Y` in the equivalence class of `y`; (2) the same for *every*
> such morphism; (3) the fibre `X_k` is reduced for every such morphism.
>
> Conditions (1) and (2) agree because geometric reducedness of the fibre only depends on the
> point of `|Y|` represented by the field-valued point, two representatives of one point having
> a common extension. Condition (3) implies (2) because every representative is dominated by
> one whose field of definition is algebraically closed, hence perfect, where reducedness of
> the fibre already gives geometric reducedness.

```lean
theorem isGeometricallyReducedFibre_tfae (f : X ⟶ Y) (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (y : points B S hS Y) :
    List.TFAE
      [ ∃ p : FieldValuedPoint B S hS Y, p.class B S hS Y = y ∧
          IsGeometricallyReducedFibre B S hS f hX hY p,
        ∀ p : FieldValuedPoint B S hS Y, p.class B S hS Y = y →
          IsGeometricallyReducedFibre B S hS f hX hY p,
        ∀ p : FieldValuedPoint B S hS Y, p.class B S hS Y = y →
          HasEtaleLocalProperty B (Spec (.of p.carrier)) p.contained
            (fibreOverFieldValuedPoint B S hS f p) (fun T : Scheme.{u} => IsReduced T) ]
```

## Tag 0E08, a definition

[Tag 0E08](https://stacks.math.columbia.edu/tag/0E08) in the Stacks Project.

**`AlgebraicGeometry.Space.IsGeometricallyReducedFibreAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricallyReduced.lean, line 372](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricallyReduced.lean#L372).

> **Stacks 0E08.** The fibre of `f : X ⟶ Y` at a point `y` of `|Y|` is *geometrically reduced*
> when the equivalent conditions of Stacks 0E07 hold: the fibre over some — equivalently, every —
> field-valued representative of `y` is geometrically reduced over the field of that
> representative.

```lean
abbrev IsGeometricallyReducedFibreAt (y : points B S hS Y) : Prop
```

## Tag 0E09, a lemma

[Tag 0E09](https://stacks.math.columbia.edu/tag/0E09) in the Stacks Project.

**`AlgebraicGeometry.Space.geometricallyReducedFibreLocus_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricallyReduced.lean, line 389](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricallyReduced.lean#L389).

> **Stacks 0E09.** The locus of points with geometrically reduced fibre commutes with base
> change: the fibre of the base change `X ×_Y Y' ⟶ Y'` over a point of `|Y'|` is geometrically
> reduced exactly when the fibre of `f` over the image of that point in `|Y|` is.

```lean
theorem geometricallyReducedFibreLocus_pullback {Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) (g : Y' ⟶ Y) (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hY' : IsAlgebraicSpace B S hS Y') :
    geometricallyReducedFibreLocus B S hS (pullback.snd f g)
        (isAlgebraicSpace_pullback B S hS f g hX hY' hY) hY' =
      pointsMap B S hS Y' g ⁻¹' geometricallyReducedFibreLocus B S hS f hX hY
```

## Tag 0E0A, a lemma

[Tag 0E0A](https://stacks.math.columbia.edu/tag/0E0A) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtaleLocallyConstructible_geometricallyReducedFibreLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricallyReducedLocus.lean, line 428](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricallyReducedLocus.lean#L428). References: EGA IV (9.7.7), “more general”.

> **Stacks 0E0A.** For a quasi-compact morphism of algebraic spaces over `S` which is
> locally of finite presentation, the set of points of `|Y|` whose fibre is geometrically reduced
> is étale locally constructible.
>
> Constructibility is tested on an affine étale chart `h_V ⟶ Y`. There the locus is, by
> Stacks 0E09, the locus of the base change `X ×_Y h_V ⟶ h_V`, which is a quasi-compact algebraic
> space and so has an affine surjective étale chart `h_A ⟶ X ×_Y h_V`. The induced morphism of
> affine schemes `A ⟶ V` is of finite presentation, its scheme-theoretic fibres are surjective
> étale charts of the fibres of the base change, and so the locus is the geometrically reduced
> fibre locus of `A ⟶ V`; that set is locally constructible by Stacks 0579.

```lean
theorem isEtaleLocallyConstructible_geometricallyReducedFibreLocus
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsQuasiCompact B S hS f) (hfp : IsLocallyOfFinitePresentation B S hS f) :
    IsEtaleLocallyConstructible B S hS Y (geometricallyReducedFibreLocus B S hS f hX hY)
```

## Tag 0E0B, a lemma

[Tag 0E0B](https://stacks.math.columbia.edu/tag/0E0B) in the Stacks Project.

**`AlgebraicGeometry.Space.isReduced_of_isReduced_specialFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/Reduced.lean, line 824](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/Reduced.lean#L824). The attribute's comment: “total space”.

> **Stacks 0E0B.** A proper flat algebraic space over a discrete valuation ring is reduced
> when its special fibre is reduced.

```lean
public theorem isReduced_of_isReduced_specialFiber
    (R : Type u) [CommRing R] [IsDomain R] [IsDiscreteValuationRing R]
    (B : BigFppfSite.{u})
    (hR : B.Contains (Spec (.of R)))
    (hk : B.Contains (Spec (.of (IsLocalRing.ResidueField R))))
    (X : (BigFppfOver B (Spec (.of R)) hR)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of R)) hR X)
    (f : X ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hR))))
    (hproper : IsProper B (Spec (.of R)) hR f)
    (hflat : IsFlat B (Spec (.of R)) hR f)
    (hspecial :
      let g : B.obj hk ⟶ B.obj hR :=
        B.inclusion.preimage
          (Spec.map (CommRingCat.ofHom (IsLocalRing.residue R)))
      HasEtaleLocalProperty B
        (Spec (.of (IsLocalRing.ResidueField R))) hk
        ((OverShriek.relocalizeRestrict g).obj X)
        (fun T : Scheme.{u} => IsReduced T)) :
    HasEtaleLocalProperty B (Spec (.of R)) hR X
      (fun T : Scheme.{u} => IsReduced T)
```

**`AlgebraicGeometry.Space.isReduced_genericFiber_of_isReduced_specialFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/Reduced.lean, line 968](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/Reduced.lean#L968). The attribute's comment: “generic fibre”.

> **Stacks 0E0B.** The generic fibre of a proper flat algebraic space over a discrete
> valuation ring with reduced special fibre is reduced.

```lean
public theorem isReduced_genericFiber_of_isReduced_specialFiber
    (R : Type u) [CommRing R] [IsDomain R] [IsDiscreteValuationRing R]
    (B : BigFppfSite.{u})
    (hR : B.Contains (Spec (.of R)))
    (hk : B.Contains (Spec (.of (IsLocalRing.ResidueField R))))
    (hK : B.Contains (Spec (.of (FractionRing R))))
    (X : (BigFppfOver B (Spec (.of R)) hR)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of R)) hR X)
    (f : X ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hR))))
    (hproper : IsProper B (Spec (.of R)) hR f)
    (hflat : IsFlat B (Spec (.of R)) hR f)
    (hspecial :
      let g : B.obj hk ⟶ B.obj hR :=
        B.inclusion.preimage
          (Spec.map (CommRingCat.ofHom (IsLocalRing.residue R)))
      HasEtaleLocalProperty B
        (Spec (.of (IsLocalRing.ResidueField R))) hk
        ((OverShriek.relocalizeRestrict g).obj X)
        (fun T : Scheme.{u} => IsReduced T)) :
    let g : B.obj hK ⟶ B.obj hR :=
      B.inclusion.preimage
        (Spec.map (CommRingCat.ofHom (algebraMap R (FractionRing R))))
    HasEtaleLocalProperty B (Spec (.of (FractionRing R))) hK
      ((OverShriek.relocalizeRestrict g).obj X)
      (fun T : Scheme.{u} => IsReduced T)
```

## Tag 0E0C, a lemma

[Tag 0E0C](https://stacks.math.columbia.edu/tag/0E0C) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpen_geometricallyReducedFibreLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricallyReducedOpenLocus.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/GeometricallyReducedOpenLocus.lean#L304). References: EGA IV (12.2.4), “more general”.

> **Stacks 0E0C.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is flat,
> proper and of finite presentation. Then the set of points of `|Y|` at which the fibre of `f` is
> geometrically reduced is open in `|Y|`.
>
> The locus is étale locally constructible, Stacks 0E0A, and on every étale scheme chart its
> inverse image is stable under generalization,
> `AlgebraicGeometry.Space.stableUnderGeneralization_preimage_geometricallyReducedFibreLocus`;
> so `AlgebraicGeometry.Space.isOpen_geometricallyReducedFibreLocus_of_chart_generalization`
> applies.

```lean
theorem isOpen_geometricallyReducedFibreLocus
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hflat : IsFlat B S hS f) (hproper : IsProper B S hS f)
    (hfp : IsFinitePresentation B S hS f) :
    IsOpen (geometricallyReducedFibreLocus B S hS f hX hY)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.29, Tag 0E06](https://stacks.math.columbia.edu/tag/0E06)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
