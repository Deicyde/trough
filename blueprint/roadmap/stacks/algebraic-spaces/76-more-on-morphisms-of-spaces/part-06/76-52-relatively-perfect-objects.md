---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsPerfectRelativeTo, AlgebraicGeometry.Space.IsRelativelyPerfect, AlgebraicGeometry.Space.isRelativelyPerfect_dualNumberResidueComplex_and_not_isPerfect, AlgebraicGeometry.Space.isPerfectRelativeTo_of_isBounded_of_isPseudoCoherent, AlgebraicGeometry.Space.isBounded_and_isPseudoCoherent_iff_derivedCategoryBBounded, AlgebraicGeometry.Space.isQuasiCompactSpace_of_isFinitePresentation_fieldSpace, AlgebraicGeometry.Space.isRelativelyPerfect_iff_isBounded_and_isPseudoCoherent, AlgebraicGeometry.Space.isRelativelyPerfect_iff_derivedCategoryBBounded
statement: formalized
proof: formalized
---

# 76.52 Relatively perfect objects

Section 76.52 of the Stacks Project, [Tag 0DKM](https://stacks.math.columbia.edu/tag/0DKM). 13 tags here are carried by 31 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DKN, a definition

[Tag 0DKN](https://stacks.math.columbia.edu/tag/0DKN) in the Stacks Project.

**`AlgebraicGeometry.Space.IsPerfectRelativeTo`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/Relative.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/Relative.lean#L179). References: SGA 6 III (4.1), “spaces, flat l.f.p.”.

> For a morphism `f : X ⟶ Y` of algebraic spaces which is flat and locally of finite
> presentation, an object `E` of `D(𝒪_X)` is *perfect relative to `Y`* when `E` is
> pseudo-coherent and, read as an object of `D(f⁻¹𝒪_Y)` through restriction of scalars along
> `f⁻¹𝒪_Y ⟶ 𝒪_X`, locally has finite Tor dimension.
>
> Finite Tor dimension on the slice of the small étale site over `V` is measured against the
> derived tensor product `T V` on that slice. The hypotheses `_hflat` and `_hlfp` that `f` is flat
> and locally of finite presentation do not enter the condition.

```lean
abbrev IsPerfectRelativeTo
    (_hflat : IsFlat B S hS f.hom)
    (_hlfp : IsLocallyOfFinitePresentation B S hS f.hom)
    (T : ∀ U : (inverseImageRingedSite B S hS f).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, u, e}
        ((inverseImageRingedSite B S hS f).over U))
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) : Prop
```

**`AlgebraicGeometry.Space.IsRelativelyPerfect`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativelyPerfect.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativelyPerfect.lean#L101). The attribute's comment: “Y-perfect objects: pseudo-coherent, and locally of finite tor dimension over f⁻¹𝒪\_Y for the derived tensor product of 06YU; independent of that choice by isRelativelyPerfect\_iff\_isPerfectRelativeTo”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is flat and locally of
> finite presentation. An object `E` of `D(𝒪_X)` is *perfect relative to `Y`*, or *`Y`-perfect*,
> if `E` is pseudo-coherent and `E` locally has finite Tor dimension as an object of `D(f⁻¹𝒪_Y)`.
>
> `E` is read as an object of `D(f⁻¹𝒪_Y)` through restriction of scalars along `f⁻¹𝒪_Y ⟶ 𝒪_X`, and
> finite Tor dimension on the slice of `(X_étale, f⁻¹𝒪_Y)` over `U` is measured against the derived
> tensor product of that slice constructed by Stacks 06YU.

```lean
def IsRelativelyPerfect
    (_hflat : IsFlat B S hS f.hom)
    (_hlfp : IsLocallyOfFinitePresentation B S hS f.hom)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) : Prop
```

## Tag 0DKP, an example

[Tag 0DKP](https://stacks.math.columbia.edu/tag/0DKP) in the Stacks Project.

**`AlgebraicGeometry.Space.isRelativelyPerfect_dualNumberResidueComplex_and_not_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativelyPerfectNotFibrewise.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativelyPerfectNotFibrewise.lean#L383). The attribute's comment: “relative perfectness over a field is not perfectness on the fibres”.

> **Stacks 0DKP, the closing warning.** Over a field, relative perfectness is not perfectness
> on the fibres: on the algebraic space `Spec k[ε]` — which is of finite presentation over `k`
> (`AlgebraicGeometry.Space.isFinitePresentation_dualNumberSpaceMap`), and whose only fibre over
> `Spec k` is itself — the residue field of the dual numbers, placed in degree zero, is `k`-perfect
> and is not a perfect object of `D(𝒪_{Spec k[ε]})`.

```lean
theorem isRelativelyPerfect_dualNumberResidueComplex_and_not_isPerfect :
    IsRelativelyPerfect B S hS (dualNumberSpaceMap B S hS k hk b)
        (isFlat_toFieldSpace B S hS k hk b _)
        (isLocallyOfFinitePresentation_dualNumberSpaceMap B S hS k hk b)
        (dualNumberResidueComplex B S hS k hk b) ∧
      ¬ (smallEtaleRingedSite B S hS (dualNumberSpace B S hS k hk b).1
        (dualNumberSpace B S hS k hk b).2).IsPerfect (dualNumberResidueComplex B S hS k hk b)
```

**`AlgebraicGeometry.Space.isPerfectRelativeTo_of_isBounded_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeOverField.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeOverField.lean#L231). The attribute's comment: “bounded pseudo-coherent objects are perfect relative to a field”.

> Let `k` be a field and let `X` be an algebraic space locally of finite presentation over
> `k`. A bounded pseudo-coherent object of `D(𝒪_X)` is perfect relative to `Spec k`, the flatness
> of `X ⟶ Spec k` being `isFlat_toFieldSpace`.

```lean
theorem isPerfectRelativeTo_of_isBounded_of_isPseudoCoherent
    (hlfp : IsLocallyOfFinitePresentation B S hS f.hom)
    (T : ∀ U : (inverseImageRingedSite B S hS f).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, u, e}
        ((inverseImageRingedSite B S hS f).over U))
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hpc : (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherent E)
    (hbdd : DerivedCategoryB.IsBounded E) :
    IsPerfectRelativeTo B S hS f (isFlat_toFieldSpace B S hS k hk b f) hlfp T E
```

**`AlgebraicGeometry.Space.isBounded_and_isPseudoCoherent_iff_derivedCategoryBBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeOverFieldCharacterization.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeOverFieldCharacterization.lean#L143). The attribute's comment: “bounded pseudo-coherent objects are the objects of `D^b_Coh(X)`, by Stacks 08IK”.

> **On a locally Noetherian algebraic space the bounded pseudo-coherent objects of `D(𝒪_X)`
> are the objects of `D^b_Coh(𝒪_X)`**: an object of `D(𝒪_X)` is bounded and pseudo-coherent if
> and only if it is bounded with coherent cohomology sheaves.
>
> This is the bounded case of the final statement of Stacks 08IK, which identifies the
> pseudo-coherent objects with `D⁻_Coh(𝒪_X)`; quasi-coherence of the cohomology sheaves holds on
> both sides, on the left by Stacks 08JL.

```lean
theorem isBounded_and_isPseudoCoherent_iff_derivedCategoryBBounded
    (E : DerivedCategory (Modules.{u, u} B S hS F hF)) :
    (DerivedCategoryB.IsBounded E ∧ (smallEtaleRingedSite B S hS F hF).IsPseudoCoherent E) ↔
      DerivedCategoryB.derivedCategoryBBounded
        (fun M : Modules.{u, u} B S hS F hF => M.IsCoherentOnSite) E
```

**`AlgebraicGeometry.Space.isQuasiCompactSpace_of_isFinitePresentation_fieldSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeOverFieldCharacterization.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeOverFieldCharacterization.lean#L171). The attribute's comment: “in particular, an algebraic space of finite presentation over a field is quasi-compact”.

> **An algebraic space of finite presentation over a field is quasi-compact.**

```lean
theorem isQuasiCompactSpace_of_isFinitePresentation_fieldSpace
    (hfp : IsFinitePresentation B S hS f.hom) : IsQuasiCompactSpace B S hS X.1
```

**`AlgebraicGeometry.Space.isRelativelyPerfect_iff_isBounded_and_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeOverFieldCharacterization.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeOverFieldCharacterization.lean#L330). The attribute's comment: “`k`-perfect objects are the bounded pseudo-coherent ones”.

> **Stacks 0DKP, first equivalence.** Let `k` be a field and let `X` be an algebraic space of
> finite presentation over `k`. An object `E` of `D(𝒪_X)` is `k`-perfect (Stacks 0DKN) if and only
> if it is bounded and pseudo-coherent.

```lean
theorem isRelativelyPerfect_iff_isBounded_and_isPseudoCoherent
    (hfp : IsFinitePresentation B S hS f.hom)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) :
    IsRelativelyPerfect B S hS f (isFlat_toFieldSpace B S hS k hk b f) hfp.1 E ↔
      (DerivedCategoryB.IsBounded E ∧ (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherent E)
```

**`AlgebraicGeometry.Space.isRelativelyPerfect_iff_derivedCategoryBBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeOverFieldCharacterization.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeOverFieldCharacterization.lean#L342). The attribute's comment: “the `k`-perfect objects are exactly the objects of `D^b_Coh(X)`”.

> **Stacks 0DKP.** Let `k` be a field and let `X` be an algebraic space of finite presentation
> over `k`. An object `E` of `D(𝒪_X)` is `k`-perfect (Stacks 0DKN) if and only if it lies in
> `D^b_Coh(𝒪_X)`, that is, if and only if it is bounded with coherent cohomology sheaves.

```lean
theorem isRelativelyPerfect_iff_derivedCategoryBBounded
    (hfp : IsFinitePresentation B S hS f.hom)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) :
    IsRelativelyPerfect B S hS f (isFlat_toFieldSpace B S hS k hk b f) hfp.1 E ↔
      DerivedCategoryB.derivedCategoryBBounded
        (fun M : Modules.{u, u} B S hS X.1 X.2 => M.IsCoherentOnSite) E
```

## Tag 0DKQ, a lemma

[Tag 0DKQ](https://stacks.math.columbia.edu/tag/0DKQ) in the Stacks Project.

**`AlgebraicGeometry.Space.isPerfectRelativeToCanonical_tfae_chartDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSchemeCharts.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSchemeCharts.lean#L380).

> **Relative perfectness of algebraic spaces read on scheme charts.** Let `f : X ⟶ Y` be a
> morphism of algebraic spaces which is flat and locally of finite presentation, and let
> `E ∈ D_QCoh(𝒪_X)`. For a commutative square of étale scheme charts `U ⟶ V` over `f`, write `E_0`
> for the object `Rε_*(E|_U)` of `D_QCoh(𝒪_{U_0})` corresponding to `E|_U` (Stacks 071Q). The
> following are equivalent:
> 1. `E` is `Y`-perfect;
> 2. for every such square, `E_0` is `V_0`-perfect in the sense of schemes;
> 3. for some such square whose chart of `X` is surjective, `E_0` is `V_0`-perfect;
> 4. for every such square with `U` and `V` affine, `RΓ(U, E)` is `𝒪_Y(V)`-perfect, that is,
>    pseudo-coherent over `Γ(U, 𝒪_U)` and of finite Tor dimension over `Γ(V, 𝒪_V)`.

```lean
theorem isPerfectRelativeToCanonical_tfae_chartDiagram
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2)) (hE : QcohDerived B S hS X E) :
    List.TFAE
      [IsPerfectRelativeToCanonical.{u, u + 1, u + 1} B S hS f hfl hlfp E,
        ∀ d : ChartDiagram B S hS X.1 Y.1 f.hom,
          haveI := flat_chartDiagram_g f hfl d
          haveI := locallyOfFinitePresentation_chartDiagram_g f hlfp d
          ((BigFppfOver.toScheme B S hS).map d.g).IsPerfectRelativeTo
            (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily.{u + 1, u}
              (RingedSpace.inverseImage
                (representedSchemeRepresentedZariskiRingedToposHom B S hS
                  ((SmallEtale.toOver B S hS Y.1).obj d.V)).toRingedSpace
                ((BigFppfOver.toScheme B S hS).map d.g).base))
            (chartObject d.U E),
        ∃ d : ChartDiagram B S hS X.1 Y.1 f.hom, IsSurjective B S hS d.U.1.hom ∧
          haveI := flat_chartDiagram_g f hfl d
          haveI := locallyOfFinitePresentation_chartDiagram_g f hlfp d
          ((BigFppfOver.toScheme B S hS).map d.g).IsPerfectRelativeTo
            (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily.{u + 1, u}
              (RingedSpace.inverseImage
                (representedSchemeRepresentedZariskiRingedToposHom B S hS
                  ((SmallEtale.toOver B S hS Y.1).obj d.V)).toRingedSpace
                ((BigFppfOver.toScheme B S hS).map d.g).base))
            (chartObject d.U E),
        ∀ (d : ChartDiagram B S hS X.1 Y.1 f.hom)
          [IsAffine ((BigFppfOver.toScheme B S hS).obj ((SmallEtale.toOver B S hS X.1).obj d.U))]
          [IsAffine ((BigFppfOver.toScheme B S hS).obj ((SmallEtale.toOver B S hS Y.1).obj d.V))],
          StacksDraft.PseudoCoherence.IsPseudoCoherent
              ((representedAffineDerivedSections B S hS
                ((SmallEtale.toOver B S hS X.1).obj d.U)).obj
                ((smallEtaleDerivedModulePullback B S hS (chartToSpace B S hS X d.U)).obj E)) ∧
            StacksDraft.TorAmplitude.HasFiniteTorDimensionCanonical
              Γ((BigFppfOver.toScheme B S hS).obj ((SmallEtale.toOver B S hS Y.1).obj d.V), ⊤)
              ((ModuleCat.restrictScalars
                ((BigFppfOver.toScheme B S hS).map d.g).appTop.hom).mapDerivedCategory.obj
                ((representedAffineDerivedSections B S hS
                  ((SmallEtale.toOver B S hS X.1).obj d.U)).obj
                  ((smallEtaleDerivedModulePullback B S hS
                    (chartToSpace B S hS X d.U)).obj E)))]
```

## Tag 0DKR, a lemma

[Tag 0DKR](https://stacks.math.columbia.edu/tag/0DKR) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosedUnderIsomorphisms_isPerfectRelativeTo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean#L221). The attribute's comment: “isomorphism closure”.

> For a morphism `f : X ⟶ Y` of algebraic spaces which is flat and locally of finite
> presentation, the `Y`-perfect objects of `D(𝒪_X)` form a *strictly full* subcategory:
> relative perfectness is invariant under isomorphism in `D(𝒪_X)`.

```lean
theorem isClosedUnderIsomorphisms_isPerfectRelativeTo
    (hflat : IsFlat B S hS f.hom)
    (hlfp : IsLocallyOfFinitePresentation B S hS f.hom)
    (T : ∀ U : (inverseImageRingedSite B S hS f).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, u, e}
        ((inverseImageRingedSite B S hS f).over U)) :
    (isPerfectRelativeTo B S hS f hflat hlfp T).IsClosedUnderIsomorphisms
```

**`AlgebraicGeometry.Space.isSaturated_isPerfectRelativeTo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean#L291). The attribute's comment: “saturation”.

> For a morphism `f : X ⟶ Y` of algebraic spaces which is flat and locally of finite
> presentation, the `Y`-perfect objects of `D(𝒪_X)` form a *saturated* (thick) subcategory: both
> summands of a `Y`-perfect biproduct are `Y`-perfect.

```lean
theorem isSaturated_isPerfectRelativeTo
    (hflat : IsFlat B S hS f.hom)
    (hlfp : IsLocallyOfFinitePresentation B S hS f.hom)
    (T : ∀ U : (inverseImageRingedSite B S hS f).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, u, e}
        ((inverseImageRingedSite B S hS f).over U)) :
    (isPerfectRelativeTo B S hS f hflat hlfp T).IsSaturated
```

**`AlgebraicGeometry.Space.containsZero_isPerfectRelativeTo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean#L322). The attribute's comment: “contains a zero object”.

> For a morphism `f : X ⟶ Y` of algebraic spaces which is flat and locally of finite
> presentation, the `Y`-perfect objects of `D(𝒪_X)` contain a zero object.

```lean
theorem containsZero_isPerfectRelativeTo
    (hflat : IsFlat B S hS f.hom)
    (hlfp : IsLocallyOfFinitePresentation B S hS f.hom)
    (T : ∀ U : (inverseImageRingedSite B S hS f).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, u, e}
        ((inverseImageRingedSite B S hS f).over U)) :
    (isPerfectRelativeTo B S hS f hflat hlfp T).ContainsZero
```

**`AlgebraicGeometry.Space.isStableUnderShift_isPerfectRelativeTo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean, line 339](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean#L339). The attribute's comment: “closure under the shifts”.

> For a morphism `f : X ⟶ Y` of algebraic spaces which is flat and locally of finite
> presentation, the `Y`-perfect objects of `D(𝒪_X)` are stable under every shift `E ↦ E[n]`.

```lean
theorem isStableUnderShift_isPerfectRelativeTo
    (hflat : IsFlat B S hS f.hom)
    (hlfp : IsLocallyOfFinitePresentation B S hS f.hom)
    (T : ∀ U : (inverseImageRingedSite B S hS f).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, u, e}
        ((inverseImageRingedSite B S hS f).over U)) :
    (isPerfectRelativeTo B S hS f hflat hlfp T).IsStableUnderShift ℤ
```

**`AlgebraicGeometry.Space.isTriangulated_isPerfectRelativeTo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean#L394). The attribute's comment: “closure under cones: the Y-perfect objects form a triangulated subcategory. The zero object and the shifts are `containsZero_isPerfectRelativeTo` and `isStableUnderShift_isPerfectRelativeTo`”. References: SGA 6 I (5.8.4), “5.8.4 a), special case”.

> For a morphism `f : X ⟶ Y` of algebraic spaces which is flat and locally of finite
> presentation, the `Y`-perfect objects of `D(𝒪_X)` form a *triangulated* subcategory: the
> property contains a zero object, is stable under all shifts, and is closed under extensions,
> for a given family `T` of derived tensor products on the slices.

```lean
theorem isTriangulated_isPerfectRelativeTo
    (hflat : IsFlat B S hS f.hom)
    (hlfp : IsLocallyOfFinitePresentation B S hS f.hom)
    (T : ∀ U : (inverseImageRingedSite B S hS f).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, u, e}
        ((inverseImageRingedSite B S hS f).over U)) :
    (isPerfectRelativeTo B S hS f hflat hlfp T).IsTriangulated
```

**`AlgebraicGeometry.Space.isClosedUnderIsomorphisms_isPerfectRelativeToCanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean, line 460](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean#L460). The attribute's comment: “isomorphism closure, for an actual f”.

> For a morphism `f : X ⟶ Y` of algebraic spaces which is flat and locally of finite
> presentation, the `Y`-perfect objects of `D(𝒪_X)` form a *strictly full* subcategory.

```lean
theorem isClosedUnderIsomorphisms_isPerfectRelativeToCanonical
    (hflat : IsFlat B S hS f.hom)
    (hlfp : IsLocallyOfFinitePresentation B S hS f.hom) :
    (isPerfectRelativeToCanonical B S hS f hflat hlfp).IsClosedUnderIsomorphisms
```

**`AlgebraicGeometry.Space.isSaturated_isPerfectRelativeToCanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean#L478). The attribute's comment: “saturation, for an actual f”.

> For a morphism `f : X ⟶ Y` of algebraic spaces which is flat and locally of finite
> presentation, the `Y`-perfect objects of `D(𝒪_X)` form a *saturated* (thick) subcategory.

```lean
theorem isSaturated_isPerfectRelativeToCanonical
    (hflat : IsFlat B S hS f.hom)
    (hlfp : IsLocallyOfFinitePresentation B S hS f.hom) :
    (isPerfectRelativeToCanonical B S hS f hflat hlfp).IsSaturated
```

**`AlgebraicGeometry.Space.containsZero_isPerfectRelativeToCanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean, line 496](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean#L496). The attribute's comment: “contains a zero object, for an actual f”.

> For a morphism `f : X ⟶ Y` of algebraic spaces which is flat and locally of finite
> presentation, the `Y`-perfect objects of `D(𝒪_X)` contain a zero object.

```lean
theorem containsZero_isPerfectRelativeToCanonical
    (hflat : IsFlat B S hS f.hom)
    (hlfp : IsLocallyOfFinitePresentation B S hS f.hom) :
    (isPerfectRelativeToCanonical B S hS f hflat hlfp).ContainsZero
```

**`AlgebraicGeometry.Space.isStableUnderShift_isPerfectRelativeToCanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean, line 514](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean#L514). The attribute's comment: “closure under the shifts, for an actual f”.

> For a morphism `f : X ⟶ Y` of algebraic spaces which is flat and locally of finite
> presentation, the `Y`-perfect objects of `D(𝒪_X)` are stable under every shift.

```lean
theorem isStableUnderShift_isPerfectRelativeToCanonical
    (hflat : IsFlat B S hS f.hom)
    (hlfp : IsLocallyOfFinitePresentation B S hS f.hom) :
    (isPerfectRelativeToCanonical B S hS f hflat hlfp).IsStableUnderShift ℤ
```

**`AlgebraicGeometry.Space.isTriangulated_isPerfectRelativeToCanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean, line 528](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeSubcategory.lean#L528). The attribute's comment: “closure under cones for an actual f: the Y-perfect objects of D(O\_X) form a triangulated subcategory. The zero object and the shifts are `containsZero_isPerfectRelativeToCanonical` and `isStableUnderShift_isPerfectRelativeToCanonical`”.

> For a morphism `f : X ⟶ Y` of algebraic spaces which is flat and locally of finite
> presentation, the `Y`-perfect objects of `D(𝒪_X)` form a *triangulated* subcategory: the
> property contains a zero object, is stable under all shifts, and is closed under extensions.

```lean
theorem isTriangulated_isPerfectRelativeToCanonical
    (hflat : IsFlat B S hS f.hom)
    (hlfp : IsLocallyOfFinitePresentation B S hS f.hom) :
    (isPerfectRelativeToCanonical B S hS f hflat hlfp).IsTriangulated
```

## Tag 0DKS, a lemma

[Tag 0DKS](https://stacks.math.columbia.edu/tag/0DKS) in the Stacks Project.

**`AlgebraicGeometry.Space.isRelativelyPerfect_of_isPerfect_and_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativelyPerfectDerivedTensor.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativelyPerfectDerivedTensor.lean#L320).

> **Stacks 0DKS.** Let `S` be a scheme and let `f : X ⟶ Y` be a morphism of algebraic spaces
> over `S` which is flat and locally of finite presentation.
>
> 1. A perfect object of `D(𝒪_X)` is `Y`-perfect.
> 2. If `K, M ∈ D(𝒪_X)`, then `K ⊗^𝐋_{𝒪_X} M` is `Y`-perfect if `K` is perfect and `M` is
>    `Y`-perfect.
>
> `Y`-perfectness is Stacks 0DKN, `AlgebraicGeometry.Space.IsRelativelyPerfect`. The derived tensor
> product is any derived tensor product datum `TX` of Stacks 06YU on the small étale site of `X`,
> for instance the canonical one. The first assertion is
> `AlgebraicGeometry.Space.isRelativelyPerfect_of_isPerfect`, the second
> `AlgebraicGeometry.Space.isRelativelyPerfect_derivedTensor`.

```lean
theorem isRelativelyPerfect_of_isPerfect_and_derivedTensor
    (hflat : IsFlat B S hS f.hom)
    (hlfp : IsLocallyOfFinitePresentation B S hS f.hom)
    (TX : Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, u, d}
      (smallEtaleRingedSite B S hS X.1 X.2)) :
    (∀ E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2),
        (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect E →
          IsRelativelyPerfect B S hS f hflat hlfp E) ∧
      ∀ K M : DerivedCategory (Modules.{u, u} B S hS X.1 X.2),
        (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect K →
          IsRelativelyPerfect B S hS f hflat hlfp M →
            IsRelativelyPerfect B S hS f hflat hlfp ((TX.tensor.obj K).obj M)
```

## Tag 0DKT, a lemma

[Tag 0DKT](https://stacks.math.columbia.edu/tag/0DKT) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isPerfectRelativeToCanonical_smallEtaleDerivedModulePullback`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeBaseChange.lean#L227), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeBaseChangeTags.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeBaseChangeTags.lean#L20) (StacksFrontier).

## Tag 0DKU, a situation

[Tag 0DKU](https://stacks.math.columbia.edu/tag/0DKU) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeDescentSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativelyPerfect.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativelyPerfect.lean#L39).

> A directed inverse system of quasi-compact, quasi-separated algebraic spaces with affine
> transition morphisms, together with its limit, a flat algebraic space of finite presentation
> over one chosen stage, and the base changes of that space to every later stage and to the
> limit.

```lean
structure RelativeDescentSituation (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u})) (I : Type v) [Preorder I]
    [IsDirected I (· ≤ ·)]
```

## Tag 0DKV, a lemma

[Tag 0DKV](https://stacks.math.columbia.edu/tag/0DKV) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeDescentSituation.restrict`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativelyPerfectHomDescent.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativelyPerfectHomDescent.lean#L293). The attribute's comment: “the restriction of Situation 0DKU along a flat morphism of finite presentation, a step the tag's proof needs and which this development lacked; stated for flat plus finite presentation rather than étale, which is strictly more general. The tag's own conclusion is not proved here”.

> The restriction of a relative descent situation along a flat finitely presented morphism
> `g : U₀ ⟶ X₀`: the inverse system, its limit and the chosen stage are unchanged, `U₀` replaces
> `X₀` with structure morphism `g ≫ p₀`, and the base changes are the fibre products
> `Xᵢ ×_{X₀} U₀` and `X ×_{X₀} U₀`.

```lean
def restrict {U₀ : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hU₀ : IsAlgebraicSpace B S hS U₀)
    (g : U₀ ⟶ D.X₀) (hgflat : IsFlat B S hS g)
    (hgfp : IsFinitePresentation B S hS g) : RelativeDescentSituation B S hS hZ I
```

**`AlgebraicGeometry.Space.RelativeDescentSituation.homDescent_iff_isIso_colimitDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativelyPerfectHomDescent.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativelyPerfectHomDescent.lean#L478). The attribute's comment: “the tag's conclusion reformulated: the elementary descent statement holds exactly when the canonical colimit comparison map is invertible”.

> `HomDescent` holds exactly when the canonical map from the colimit of the system of derived
> homomorphism sets to `Hom_{D(𝒪_X)}(K, L)` is an isomorphism.

```lean
theorem homDescent_iff_isIso_colimitDesc [HasColimit (D.homFunctor P K₀ L₀)] :
    D.HomDescent P K₀ L₀ ↔
      IsIso (colimit.desc (D.homFunctor P K₀ L₀) (D.homCocone P K₀ L₀))
```

**`AlgebraicGeometry.Space.RelativeDescentSituation.isIso_colimitDesc_homCocone_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativelyPerfectHomDescentFinal.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativelyPerfectHomDescentFinal.lean#L80). The attribute's comment: “the full statement; the condition D.IsSchemeLimit on the limit cone is the meaning of Y = lim Y\_i in Situation 0DKU, the limit of algebraic spaces of Stacks 07SF, which the presheaf limit cone of RelativeDescentSituation does not record by itself (see the module documentation of RelativeDescentSchemeLimit for a situation where the presheaf limit is empty and the conclusion fails); it holds automatically for small index sets, see isIso\_colimitDesc\_homCocone\_of\_isPseudoCoherent\_of\_mk\_lt and isIso\_colimitDesc\_homCocone\_of\_isPseudoCoherent\_of\_countable”.

> **Stacks 0DKV.** In Situation 0DKU, with `Y = lim Yᵢ` the limit of algebraic spaces of
> Stacks 07SF (a limit of schemes on affine charts), let `K₀`, `L₀` be objects of `D(𝒪_{X₀})`
> with `K₀` pseudo-coherent and `L₀ ∈ D_QCoh(𝒪_{X₀})` locally of finite Tor dimension as an object
> of `D((X₀ → Y₀)⁻¹𝒪_{Y₀})`.  Then the comparison map
> `colim_{i ≥ 0} Hom_{D(𝒪_{Xᵢ})}(Lf_{i0}^*K₀, Lf_{i0}^*L₀) ⟶ Hom_{D(𝒪_X)}(Lf₀^*K₀, Lf₀^*L₀)`
> is an isomorphism.

```lean
theorem isIso_colimitDesc_homCocone_of_isPseudoCoherent
    (D : RelativeDescentSituation B S hS hZ I) (hD : D.IsSchemeLimit)
    (K₀ L₀ : derivedModules B S hS D.initialSource) (hK₀ : IsPseudoCoherentObject K₀)
    (hL₀ : IsInQuasicoherentDerived D.initialSource L₀)
    (hL₀tor : HasLocallyFiniteTorDimensionAlong D.initialStructure L₀) :
    IsIso (colimit.desc (D.homFunctor (DerivedPullbackComposition.canonical B S hS) K₀ L₀)
      (D.homCocone (DerivedPullbackComposition.canonical B S hS) K₀ L₀))
```

**`AlgebraicGeometry.Space.RelativeDescentSituation.isIso_colimitDesc_homCocone_of_isPseudoCoherent_of_mk_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativelyPerfectHomDescentFinal.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativelyPerfectHomDescentFinal.lean#L101). The attribute's comment: “the full statement for every directed index set I with #I below the cofinality of the size cutoff of the site, with no condition on the limit: the limit of presheaves of RelativeDescentSituation is then the limit of algebraic spaces of Stacks 07SF (isSchemeLimit\_of\_size)”.

> **Stacks 0DKV for a small index set.** In Situation 0DKU indexed by a directed set with
> fewer elements than the cofinality of the size cutoff of the site, let `K₀`, `L₀` be objects of
> `D(𝒪_{X₀})` with `K₀` pseudo-coherent and `L₀ ∈ D_QCoh(𝒪_{X₀})` locally of finite Tor dimension
> as an object of `D((X₀ → Y₀)⁻¹𝒪_{Y₀})`.  Then the comparison map
> `colim_{i ≥ 0} Hom_{D(𝒪_{Xᵢ})}(Lf_{i0}^*K₀, Lf_{i0}^*L₀) ⟶ Hom_{D(𝒪_X)}(Lf₀^*K₀, Lf₀^*L₀)`
> is an isomorphism.  No condition on the limit is needed: for such index sets the limit of
> presheaves is the limit of algebraic spaces of Stacks 07SF.

```lean
theorem isIso_colimitDesc_homCocone_of_isPseudoCoherent_of_mk_lt
    (D : RelativeDescentSituation B S hS hZ I) (hI : #I < B.cutoff.ord.cof)
    (K₀ L₀ : derivedModules B S hS D.initialSource) (hK₀ : IsPseudoCoherentObject K₀)
    (hL₀ : IsInQuasicoherentDerived D.initialSource L₀)
    (hL₀tor : HasLocallyFiniteTorDimensionAlong D.initialStructure L₀) :
    IsIso (colimit.desc (D.homFunctor (DerivedPullbackComposition.canonical B S hS) K₀ L₀)
      (D.homCocone (DerivedPullbackComposition.canonical B S hS) K₀ L₀))
```

**`AlgebraicGeometry.Space.RelativeDescentSituation.isIso_colimitDesc_homCocone_of_isPseudoCoherent_of_countable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativelyPerfectHomDescentFinal.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativelyPerfectHomDescentFinal.lean#L119). The attribute's comment: “the full statement for every countable directed index set, on every big fppf site, with no condition on the limit”.

> **Stacks 0DKV for a countable index set.** In Situation 0DKU indexed by a countable
> directed set, on any big fppf site, let `K₀`, `L₀` be objects of `D(𝒪_{X₀})` with `K₀`
> pseudo-coherent and `L₀ ∈ D_QCoh(𝒪_{X₀})` locally of finite Tor dimension as an object of
> `D((X₀ → Y₀)⁻¹𝒪_{Y₀})`.  Then the comparison map
> `colim_{i ≥ 0} Hom_{D(𝒪_{Xᵢ})}(Lf_{i0}^*K₀, Lf_{i0}^*L₀) ⟶ Hom_{D(𝒪_X)}(Lf₀^*K₀, Lf₀^*L₀)`
> is an isomorphism.  The size cutoff of every big fppf site has uncountable cofinality.

```lean
theorem isIso_colimitDesc_homCocone_of_isPseudoCoherent_of_countable [Countable I]
    (D : RelativeDescentSituation B S hS hZ I)
    (K₀ L₀ : derivedModules B S hS D.initialSource) (hK₀ : IsPseudoCoherentObject K₀)
    (hL₀ : IsInQuasicoherentDerived D.initialSource L₀)
    (hL₀tor : HasLocallyFiniteTorDimensionAlong D.initialStructure L₀) :
    IsIso (colimit.desc (D.homFunctor (DerivedPullbackComposition.canonical B S hS) K₀ L₀)
      (D.homCocone (DerivedPullbackComposition.canonical B S hS) K₀ L₀))
```

## Tag 0DKW, a lemma

[Tag 0DKW](https://stacks.math.columbia.edu/tag/0DKW) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeDescentSituation.relativelyPerfectColimit_proved`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RepresentedHomotopyPullbackCoherenceConsequences.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RepresentedHomotopyPullbackCoherenceConsequences.lean#L56).

> In Situation 0DKU (indexed by a directed preorder `I` in `Type u`), whose
> limit is a limit of schemes on affine charts (the standing meaning of `Y = lim Yᵢ`,
> `AlgebraicGeometry.Space.RelativeDescentSituation.IsSchemeLimit`), the category of `Y`-perfect
> objects of `D(𝒪_X)` is the colimit of the categories of `Yᵢ`-perfect objects of `D(𝒪_{Xᵢ})`, in the
> five clauses of `AlgebraicGeometry.Space.RelativeDescentSituation.RelativelyPerfectColimit`.

```lean
theorem relativelyPerfectColimit_proved (D : RelativeDescentSituation B S hS hZ I) :
    D.RelativelyPerfectColimit
```

## Tag 0DKX, a lemma

[Tag 0DKX](https://stacks.math.columbia.edu/tag/0DKX) in the Stacks Project.

**`AlgebraicGeometry.Space.isPerfect_derivedPushforward_and_isIso_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeDerivedHomDualProved.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeDerivedHomDualProved.lean#L111).

> **Stacks 0DKX.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is flat,
> proper and of finite presentation, and let `E ∈ D(𝒪_X)` be `Y`-perfect (Stacks 0DKN). Then
> `Rf_*E` is a perfect object of `D(𝒪_Y)`, and its formation commutes with arbitrary base change:
> for every cartesian square
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
> the base change map `Lg^*Rf_*E ⟶ Rf'_*L(g')^*E` (Stacks 07A7) is an isomorphism.

```lean
theorem isPerfect_derivedPushforward_and_isIso_baseChange
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hproper : IsProper B S hS f.hom)
    (hflat : IsFlat B S hS f.hom) (hfp : IsFinitePresentation B S hS f.hom)
    (E : derivedModules B S hS X) (hE : IsPerfectRelativeToCanonical B S hS f hflat hfp.1 E) :
    (smallEtaleRingedSite B S hS Y.1 Y.2).IsPerfect ((spaceDerivedPushforward B S hS f).obj E) ∧
      ∀ {X' Y' : AlgebraicSpaces B S hS} (g' : X' ⟶ X) (f' : X' ⟶ Y') (g : Y' ⟶ Y)
        (hpb : IsPullback g' f' f g),
        IsIso (smallEtaleDerivedModuleBaseChangeMap B S hS f g f' g' hpb.w E)
```

## Tag 0DKY, a lemma

[Tag 0DKY](https://stacks.math.columbia.edu/tag/0DKY) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isPseudoCoherent_pushforward_sheafHom_iso_dual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeDerivedHomDualProved.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeDerivedHomDualProved.lean#L153).

> **Stacks 0DKY.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`, and let `E`, `K`
> be objects of `D(𝒪_X)`. Assume that `Y` is quasi-compact and quasi-separated, that `f` is proper,
> flat and of finite presentation, that `E` is `Y`-perfect (Stacks 0DKN) and that `K` is
> pseudo-coherent. Then there is a pseudo-coherent `L ∈ D(𝒪_Y)` with
> `Rf_* R𝓗om(K, E) ≅ R𝓗om(L, 𝒪_Y)`, and the same holds after arbitrary base change: for every
> cartesian square `X' = X ×_Y Y'` with projections `g' : X' ⟶ X` and `f' : X' ⟶ Y'`,
> `Rf'_* R𝓗om(L(g')^*K, L(g')^*E) ≅ R𝓗om(Lg^*L, 𝒪_{Y'})`.
>
> (`hZ` says that the site contains `Spec ℤ`, through which quasi-separatedness of `Y` is
> expressed.)

```lean
theorem exists_isPseudoCoherent_pushforward_sheafHom_iso_dual
    (hZ : B.Contains (⊤_ Scheme.{u})) {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hqc : IsQuasiCompactSpace B S hS Y.1) (hqs : IsAbsolutelyQuasiSeparated B S hS hZ Y.1)
    (hproper : IsProper B S hS f.hom) (hflat : IsFlat B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom) (K E : derivedModules B S hS X)
    (hE : IsPerfectRelativeToCanonical B S hS f hflat hfp.1 E)
    (hK : (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherent K) :
    ∃ L : derivedModules B S hS Y, (smallEtaleRingedSite B S hS Y.1 Y.2).IsPseudoCoherent L ∧
      Nonempty ((spaceDerivedPushforward B S hS f).obj
          (((smallEtaleDerivedSheafHom B S hS X).obj (Opposite.op K)).obj E) ≅
        smallEtaleDerivedDual B S hS Y L) ∧
      ∀ {X' Y' : AlgebraicSpaces B S hS} (g' : X' ⟶ X) (f' : X' ⟶ Y') (g : Y' ⟶ Y),
        IsPullback g' f' f g →
        Nonempty ((spaceDerivedPushforward B S hS f').obj
            (((smallEtaleDerivedSheafHom B S hS X').obj
              (Opposite.op (((smallEtaleDerivedPullbackData B S hS).pull g').obj K))).obj
                (((smallEtaleDerivedPullbackData B S hS).pull g').obj E)) ≅
          smallEtaleDerivedDual B S hS Y'
            (((smallEtaleDerivedPullbackData B S hS).pull g).obj L))
```

## Tag 0GFK, a lemma

[Tag 0GFK](https://stacks.math.columbia.edu/tag/0GFK) in the Stacks Project.

**`AlgebraicGeometry.Space.isPerfectRelativeToCanonical_iff_isLocallyBoundedBelow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeFibrewiseBoundedBelow.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/RelativeFibrewiseBoundedBelow.lean#L242).

> **Stacks 0GFK.** Let `f : X ⟶ T` be a morphism from an algebraic space to a scheme which is
> flat and locally of finite presentation, and let `E ∈ D(𝒪_X)` be pseudo-coherent. Then `E` is
> `T`-perfect exactly when `E` is locally bounded below and, for every point `s ∈ T`, the derived
> pullback `L(X_s ⟶ X)^*E` to the fibre `X_s = X ×_T Spec κ(s)` is locally bounded below.

```lean
theorem isPerfectRelativeToCanonical_iff_isLocallyBoundedBelow (f : X ⟶ representedSpace T)
    (hfl : IsFlat B S hS f.hom) (hlfp : IsLocallyOfFinitePresentation B S hS f.hom)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherent E) :
    IsPerfectRelativeToCanonical.{u, u + 1, u + 1} B S hS f hfl hlfp E ↔
      IsLocallyBoundedBelow X E ∧ ∀ s : (BigFppfOver.toScheme B S hS).obj T,
        IsLocallyBoundedBelow (residueFibre f s)
          ((smallEtaleDerivedModulePullback B S hS (residueFibreι f s)).obj E)
```

## Tag 0GFL, a lemma

[Tag 0GFL](https://stacks.math.columbia.edu/tag/0GFL) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasicoherentDerivedCategory.isPerfectRelativeToCanonical_of_isPerfect_derivedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DerivedChow/RelativePerfect.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DerivedChow/RelativePerfect.lean#L304).

> Let `A` be a ring and `X` an algebraic space separated, of finite presentation and flat over
> `A`. Let `K ∈ D_QCoh(𝒪_X)`. If `RΓ(X, E ⊗^𝐋 K)` is perfect in `D(A)` for every perfect
> `E ∈ D(𝒪_X)`, then `K` is `Spec(A)`-perfect.
>
> Here `K` is an object of the full subcategory `D_QCoh(𝒪_X)` of `D(𝒪_X)` (Stacks 071X), and
> `RΓ(X, -)` with values in `D(A)` is `RΓ(Spec A, Rf_*(-))` for the structure morphism
> `f : X ⟶ Spec A`.

```lean
theorem QuasicoherentDerivedCategory.isPerfectRelativeToCanonical_of_isPerfect_derivedSections
    {X : AlgebraicSpaces B (Spec (CommRingCat.of A)) hA}
    (hsep : IsSeparated B _ hA (toBase B _ hA X).hom)
    (hfp : IsFinitePresentation B _ hA (toBase B _ hA X).hom)
    (hfl : IsFlat B _ hA (toBase B _ hA X).hom)
    (K : QuasicoherentDerivedCategory.{u, u} B _ hA X.1 X.2)
    (h : ∀ E : DerivedCategory (Modules.{u, u} B _ hA X.1 X.2),
      (smallEtaleRingedSite B _ hA X.1 X.2).IsPerfect E →
        StacksDraft.Perfect.IsPerfect
          ((representedAffineDerivedSections B _ hA (baseSiteObj B _ hA)).obj
            ((derivedModulePushforward B _ hA (toBase B _ hA X)).obj
              (((smallEtaleDerivedTensor B _ hA X).obj E).obj K.obj)))) :
    IsPerfectRelativeToCanonical.{u, u + 1, u + 1} B _ hA (toBase B _ hA X) hfl hfp.1 K.obj
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.52, Tag 0DKM](https://stacks.math.columbia.edu/tag/0DKM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
