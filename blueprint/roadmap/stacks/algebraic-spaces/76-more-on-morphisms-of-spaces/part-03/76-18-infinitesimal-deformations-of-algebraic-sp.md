---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isIso_conormalMap_firstOrderThickening_of_isFlat, AlgebraicGeometry.Space.isFlat_and_isPullback_iff_isIso_conormalMap, AlgebraicGeometry.Space.isFlat_and_isPullback_iff_isIso_conormalMapOfImmersions, AlgebraicGeometry.Space.isFlat_of_isFlat_restriction, AlgebraicGeometry.Space.isFlatAt_base_of_isFlat_restriction, AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isFiniteLocallyFree_iff, AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isFiniteLocallyFreeOfRank_iff, AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isFlat_iff
statement: formalized
proof: formalized
---

# 76.18 Infinitesimal deformations of algebraic spaces

Section 76.18 of the Stacks Project, [Tag 06BG](https://stacks.math.columbia.edu/tag/06BG). 5 tags here are carried by 53 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06BH, a lemma

[Tag 06BH](https://stacks.math.columbia.edu/tag/06BH) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_conormalMap_firstOrderThickening_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleFirstOrderThickening.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleFirstOrderThickening.lean#L81). The attribute's comment: “(1) implies (2), with f' flat as a morphism of small etale ringed topoi”.

> Let `(f, f') : (X ⊆ X') → (Y ⊆ Y')` be a morphism of first-order thickenings of algebraic
> spaces in which `X = Y ×_{Y'} X'`, that is in which the upper closed subspace is the inverse image
> `g⁻¹(Y)` of the lower one along `g = f'` and `f` is the projection. If `f'` is flat, as a morphism
> of small étale ringed topoi, then the canonical map of conormal modules `f^*𝒞_{Y/Y'} ⟶ 𝒞_{X/X'}`
> is an isomorphism. The first-order thickening conditions on `Y ⊆ Y'` and on `g⁻¹(Y) ⊆ X'` are
> taken as hypotheses.

```lean
theorem isIso_conormalMap_firstOrderThickening_of_isFlat
    (_hY : IsFirstOrderThickening B S hS Y' Y.1)
    (_hX : IsFirstOrderThickening B S hS X' (preimageSubspace B S hS g Y).1)
    (hg : (smallEtaleRingedToposHom B S hS g).IsFlat) :
    IsIso (conormalMap B S hS (preimageSubspace B S hS g Y) Y g
      (preimageProjection B S hS g Y)
      (conormalEtaleRestrictionSquare B S hS g Y))
```

**`AlgebraicGeometry.Space.isFlat_and_isPullback_iff_isIso_conormalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleFlatDeformation.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleFlatDeformation.lean#L338).

> **[Stacks Project, Tag 06BH].**  Let `(f, f') : (X ⊆ X') → (Y ⊆ Y')` be a morphism of
> first-order thickenings of algebraic spaces over `S` — `X ⊆ X'` and `Y ⊆ Y'` first-order
> thickenings, `f' = g : X' ⟶ Y'` and `f : X ⟶ Y` with commuting square of inclusions — and let
> `f` be flat.  Then the following are equivalent:
>
> 1. `f'` is flat and `X = Y ×_{Y'} X'`;
> 2. the canonical map `f^*𝒞_{Y/Y'} ⟶ 𝒞_{X/X'}` of [Stacks Project, Tag 04CP] is an
>    isomorphism.
>
> Both flatness conditions are `AlgebraicGeometry.Space.IsFlat` of [Stacks Project, Tag 03ML],
> `X = Y ×_{Y'} X'` is cartesianness of the square of inclusions, and the canonical map is
> `AlgebraicGeometry.Space.conormalMap`.  The first-order thickening hypotheses are used only in
> (2) ⟹ (1), and so is the flatness of `f`.

```lean
theorem isFlat_and_isPullback_iff_isIso_conormalMap
    (hX : IsFirstOrderThickening B S hS X' X.1) (hY : IsFirstOrderThickening B S hS Y' Y.1)
    (hf : IsFlat B S hS f.hom) :
    (IsFlat B S hS g.hom ∧
        IsPullback (subspaceInclusion B S hS X' X) f g (subspaceInclusion B S hS Y' Y)) ↔
      IsIso (conormalMap B S hS X Y g f hsq)
```

**`AlgebraicGeometry.Space.isFlat_and_isPullback_iff_isIso_conormalMapOfImmersions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FirstOrderThickeningFlatConormal.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FirstOrderThickeningFlatConormal.lean#L265).

> **[Stacks Project, Tag 06BH].**  Let `(f, g) : (X ⊆ X') → (Y ⊆ Y')` be a morphism of
> first-order thickenings of algebraic spaces over `S` (a commutative square of inclusions of
> closed subspaces which are first-order thickenings, [Stacks Project, Tag 05ZK]), and assume
> that `f` is flat.  Then the following are equivalent:
>
> 1. `g` is flat and `X = Y ×_{Y'} X'`;
> 2. the canonical map `f^*𝒞_{Y/Y'} ⟶ 𝒞_{X/X'}` of [Stacks Project, Tag 04CP] is an isomorphism.
>
> Flatness is that of [Stacks Project, Tag 03ML], the equality `X = Y ×_{Y'} X'` is the square
> being cartesian, and the canonical map is that of the two inclusions read as immersions.

```lean
theorem isFlat_and_isPullback_iff_isIso_conormalMapOfImmersions
    (hsq : subspaceInclusion B S hS X' X ≫ g = f ≫ subspaceInclusion B S hS Y' Y)
    (hX : IsFirstOrderThickening B S hS X' X.1) (hY : IsFirstOrderThickening B S hS Y' Y.1)
    (hf : IsFlat B S hS f.hom) :
    (IsFlat B S hS g.hom ∧
        IsPullback (subspaceInclusion B S hS X' X) f g (subspaceInclusion B S hS Y' Y)) ↔
      IsIso (conormalMapOfImmersions B S hS (subspaceInclusion B S hS X' X)
        (subspaceInclusion B S hS Y' Y) f g (isImmersion_subspaceInclusion B S hS X' X)
        (isImmersion_subspaceInclusion B S hS Y' Y) hsq)
```

## Tag 0CG5, a lemma

[Tag 0CG5](https://stacks.math.columbia.edu/tag/0CG5) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_of_isFlat_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Flat.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Flat.lean#L306). The attribute's comment: “flatness of the upper morphism”.

> **Stacks 0CG5, flatness of the ambient morphism.** In a commuting diagram of thickenings
> of algebraic spaces over `S` with the base thickening of finite order, the ambient source flat
> over the ambient base and both unprimed spaces the base changes of their primed counterparts,
> flatness of the morphism of special fibres implies flatness of its ambient deformation.
>
> This is the forward implication of part 0CG8 of Tag 0CG6, which is
> `AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isFlat_iff`.

```lean
theorem isFlat_of_isFlat_restriction
    (hiX : IsThickening B S hS X' X) (hiY : IsThickening B S hS Y' Y)
    (hiB : IsFiniteOrderThickening B S hS B' B₀)
    (hcartX : IsPullback X.ι pX pX' B₀.ι) (hcartY : IsPullback Y.ι pY pY' B₀.ι)
    (hinner : f ≫ pY = pX) (houter : f' ≫ pY' = pX')
    (hrestrict : X.ι ≫ f' = f ≫ Y.ι)
    (hXflat : IsFlat B S hS pX') (hfflat : IsFlat B S hS f) :
    IsFlat B S hS f'
```

**`AlgebraicGeometry.Space.isFlatAt_base_of_isFlat_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Flat.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Flat.lean#L322). The attribute's comment: “flatness of the upper target at image points”.

> **Stacks 0CG5, flatness of the ambient target along the image.** In the situation of
> `AlgebraicGeometry.Space.isFlat_of_isFlat_restriction` the ambient target is flat over the
> ambient base at every point in the image of the ambient morphism.

```lean
theorem isFlatAt_base_of_isFlat_restriction
    (hiX : IsThickening B S hS X' X) (hiY : IsThickening B S hS Y' Y)
    (hiB : IsFiniteOrderThickening B S hS B' B₀)
    (hcartX : IsPullback X.ι pX pX' B₀.ι) (hcartY : IsPullback Y.ι pY pY' B₀.ι)
    (hinner : f ≫ pY = pX) (houter : f' ≫ pY' = pX')
    (hrestrict : X.ι ≫ f' = f ≫ Y.ι)
    (hXflat : IsFlat B S hS pX') (hfflat : IsFlat B S hS f)
    (x' : points B S hS X'.1) :
    IsFlatAt B S hS pY' (pointsMap B S hS X'.1 f' x')
```

## Tag 0CG6, a lemma

[Tag 0CG6](https://stacks.math.columbia.edu/tag/0CG6) in the Stacks Project.

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isFiniteLocallyFree_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FiniteLocallyFreeProperty.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FiniteLocallyFreeProperty.lean#L145). The attribute's comment: “0CGV: finite locally free”.

> **Stacks 0CG6, part 0CGV.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is finite locally free if and only if its ambient deformation is.

```lean
theorem isFiniteLocallyFree_iff :
    IsFiniteLocallyFree T S hS D.smallHom ↔ IsFiniteLocallyFree T S hS D.ambientHom
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isFiniteLocallyFreeOfRank_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FiniteLocallyFreeProperty.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FiniteLocallyFreeProperty.lean#L159). The attribute's comment: “0CGV: finite locally free of rank d”.

> **Stacks 0CG6, part 0CGV, with the rank.** In a cartesian finite-order deformation of
> algebraic spaces the morphism of special fibres is finite locally free of rank `d` if and only
> if its ambient deformation is.

```lean
theorem isFiniteLocallyFreeOfRank_iff (d : ℕ) :
    IsFiniteLocallyFreeOfRank T S hS D.smallHom d ↔
      IsFiniteLocallyFreeOfRank T S hS D.ambientHom d
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isFlat_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean#L109). The attribute's comment: “0CG8: flat”.

> **Stacks 0CG6, part 0CG8.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is flat if and only if its ambient deformation is.

```lean
theorem isFlat_iff : IsFlat T S hS D.f ↔ IsFlat T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isSurjective_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean#L116). The attribute's comment: “0CGF: surjective”.

> **Stacks 0CG6, part 0CGF.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is surjective if and only if its ambient deformation is.

```lean
theorem isSurjective_iff : IsSurjective T S hS D.f ↔ IsSurjective T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isLocallyOfFiniteType_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean#L124). The attribute's comment: “0CGI: locally of finite type”.

> **Stacks 0CG6, part 0CGI.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is locally of finite type if and only if its ambient deformation
> is.

```lean
theorem isLocallyOfFiniteType_iff :
    IsLocallyOfFiniteType T S hS D.f ↔ IsLocallyOfFiniteType T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isLocallyQuasiFinite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean#L134). The attribute's comment: “0CGJ: locally quasi-finite”.

> **Stacks 0CG6, part 0CGJ.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is locally quasi-finite if and only if its ambient deformation
> is.

```lean
theorem isLocallyQuasiFinite_iff :
    IsLocallyQuasiFinite T S hS D.f ↔ IsLocallyQuasiFinite T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isLocallyOfFinitePresentation_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean#L144). The attribute's comment: “0CGK: locally of finite presentation”.

> **Stacks 0CG6, part 0CGK.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is locally of finite presentation if and only if its ambient
> deformation is.

```lean
theorem isLocallyOfFinitePresentation_iff :
    IsLocallyOfFinitePresentation T S hS D.f ↔ IsLocallyOfFinitePresentation T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isSyntomic_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean#L153). The attribute's comment: “0CGN: syntomic”.

> **Stacks 0CG6, part 0CGN.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is syntomic if and only if its ambient deformation is.

```lean
theorem isSyntomic_iff : IsSyntomic T S hS D.f ↔ IsSyntomic T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isSmooth_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean#L160). The attribute's comment: “0CGP: smooth”.

> **Stacks 0CG6, part 0CGP.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is smooth if and only if its ambient deformation is.

```lean
theorem isSmooth_iff : IsSmooth T S hS D.f ↔ IsSmooth T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isUnramified_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean#L167). The attribute's comment: “0CGQ: unramified”.

> **Stacks 0CG6, part 0CGQ.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is unramified if and only if its ambient deformation is.

```lean
theorem isUnramified_iff : IsUnramified T S hS D.f ↔ IsUnramified T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isEtale_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Properties.lean#L174). The attribute's comment: “0CGR: étale”.

> **Stacks 0CG6, part 0CGR.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is étale if and only if its ambient deformation is.

```lean
theorem isEtale_iff : IsEtale T S hS D.f ↔ IsEtale T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isRelativelyRepresentable_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean#L150). The attribute's comment: “0CG7: representable”.

> **Stacks 0CG6, part 0CG7.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is representable if and only if its ambient deformation is.

```lean
theorem isRelativelyRepresentable_iff :
    yoneda.relativelyRepresentable D.f ↔ yoneda.relativelyRepresentable D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isQuasiCompact_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean#L158). The attribute's comment: “0CGB: quasi-compact”.

> **Stacks 0CG6, part 0CGB.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is quasi-compact if and only if its ambient deformation is.

```lean
theorem isQuasiCompact_iff : IsQuasiCompact T S hS D.f ↔ IsQuasiCompact T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.universallyClosed_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean#L165). The attribute's comment: “0CGC: universally closed”.

> **Stacks 0CG6, part 0CGC.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is universally closed if and only if its ambient deformation is.

```lean
theorem universallyClosed_iff : UniversallyClosed T S hS D.f ↔ UniversallyClosed T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isSeparated_iff_and_isQuasiSeparated_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean#L173). The attribute's comment: “0CGD: separated, and quasi-separated”.

> **Stacks 0CG6, part 0CGD.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is separated if and only if its ambient deformation is, and it is
> quasi-separated if and only if its ambient deformation is.

```lean
theorem isSeparated_iff_and_isQuasiSeparated_iff :
    (IsSeparated T S hS D.f ↔ IsSeparated T S hS D.f') ∧
      (IsQuasiSeparated T S hS D.f ↔ IsQuasiSeparated T S hS D.f')
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.universallyInjective_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean#L183). The attribute's comment: “0CGG: universally injective”.

> **Stacks 0CG6, part 0CGG.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is universally injective if and only if its ambient deformation
> is.

```lean
theorem universallyInjective_iff :
    UniversallyInjective T S hS D.f ↔ UniversallyInjective T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isAffineHom_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean#L191). The attribute's comment: “0CGH: affine”.

> **Stacks 0CG6, part 0CGH.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is affine if and only if its ambient deformation is.

```lean
theorem isAffineHom_iff : IsAffineHom T S hS D.f ↔ IsAffineHom T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.universallyOpen_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean#L198). The attribute's comment: “0CGM: universally open”.

> **Stacks 0CG6, part 0CGM.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is universally open if and only if its ambient deformation is.

```lean
theorem universallyOpen_iff : UniversallyOpen T S hS D.f ↔ UniversallyOpen T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isIntegralHom_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean#L205). The attribute's comment: “0CGT: integral”.

> **Stacks 0CG6, part 0CGT.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is integral if and only if its ambient deformation is.

```lean
theorem isIntegralHom_iff : IsIntegralHom T S hS D.f ↔ IsIntegralHom T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.mono_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean#L214). The attribute's comment: “0CGE: monomorphism”.

> **Stacks 0CG6, part 0CGE.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is a monomorphism if and only if its ambient deformation is.

```lean
theorem mono_iff : Mono D.f ↔ Mono D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isLocallyOfFiniteType_and_hasRelativeDimension_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean#L221). The attribute's comment: “0CGL: locally of finite type of relative dimension d”.

> **Stacks 0CG6, part 0CGL.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is locally of finite type of relative dimension `d` if and only if
> its ambient deformation is.

```lean
theorem isLocallyOfFiniteType_and_hasRelativeDimension_iff (d : ℕ) :
    (IsLocallyOfFiniteType T S hS D.f ∧ HasRelativeDimension d T S hS D.f) ↔
      (IsLocallyOfFiniteType T S hS D.f' ∧ HasRelativeDimension d T S hS D.f')
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isProper_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean#L230). The attribute's comment: “0CGS: proper”.

> **Stacks 0CG6, part 0CGS.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is proper if and only if its ambient deformation is.

```lean
theorem isProper_iff : IsProper T S hS D.f ↔ IsProper T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isFinite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean#L236). The attribute's comment: “0CGU: finite”.

> **Stacks 0CG6, part 0CGU.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is finite if and only if its ambient deformation is.

```lean
theorem isFinite_iff : IsFinite T S hS D.f ↔ IsFinite T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isOpenImmersion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean#L266). The attribute's comment: “0CGA: open immersion”.

> **Stacks 0CG6, part 0CGA.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is an open immersion if and only if its ambient deformation is.

```lean
theorem isOpenImmersion_iff : IsOpenImmersion T S hS D.f ↔ IsOpenImmersion T S hS D.f'
```

**`AlgebraicGeometry.Space.CartesianFiniteOrderDeformation.isIso_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/ThickeningProperties.lean#L279). The attribute's comment: “0CG9: isomorphism”.

> **Stacks 0CG6, part 0CG9.** In a cartesian finite-order deformation of algebraic spaces the
> morphism of special fibres is an isomorphism if and only if its ambient deformation is.

```lean
theorem isIso_iff : IsIso D.f ↔ IsIso D.f'
```

## Tag 0CGW, a lemma

[Tag 0CGW](https://stacks.math.columbia.edu/tag/0CGW) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Flatness.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Flatness.lean#L48). The attribute's comment: “flatness of the ambient morphism”.

> In a flat deformation diagram of algebraic spaces, flatness of the morphism of special fibres
> implies flatness of its ambient deformation.

```lean
theorem isFlat_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS)
    (hf : IsFlat B S hS D.f.hom) : IsFlat B S hS D.f'.hom
```

**`AlgebraicGeometry.Space.isFlatAt_target_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Flatness.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/Flatness.lean#L56). The attribute's comment: “flatness of the ambient target over the ambient base along the image”.

> In a flat deformation diagram of algebraic spaces whose morphism of special fibres is flat,
> the ambient target is flat over the ambient base at every point in the image of the ambient
> morphism.

```lean
theorem isFlatAt_target_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS)
    (hf : IsFlat B S hS D.f.hom) (x' : points B S hS D.X'.1) :
    IsFlatAt B S hS D.g'.hom (pointsMap B S hS D.X'.1 D.f'.hom x')
```

## Tag 0CGX, a lemma

[Tag 0CGX](https://stacks.math.columbia.edu/tag/0CGX) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean#L155). The attribute's comment: “part (2): flat”.

> **Stacks 0CGX, part (2).** Flatness of a morphism of algebraic spaces is invariant under a
> flat deformation.

```lean
theorem isFlat_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    IsFlat B S hS D.f.hom ↔ IsFlat B S hS D.f'.hom
```

**`AlgebraicGeometry.Space.isSurjective_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean#L198). The attribute's comment: “part (9): surjective”.

> **Stacks 0CGX, part (9).** Surjectivity of a morphism of algebraic spaces is invariant under
> a flat deformation.

```lean
theorem isSurjective_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    IsSurjective B S hS D.f.hom ↔ IsSurjective B S hS D.f'.hom
```

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean#L210). The attribute's comment: “part (12): locally quasi-finite”.

> **Stacks 0CGX, part (12).** Local quasi-finiteness of a morphism of algebraic spaces is
> invariant under a flat deformation.

```lean
theorem isLocallyQuasiFinite_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    IsLocallyQuasiFinite B S hS D.f.hom ↔ IsLocallyQuasiFinite B S hS D.f'.hom
```

**`AlgebraicGeometry.Space.isSyntomic_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean#L219). The attribute's comment: “part (15): syntomic”.

> **Stacks 0CGX, part (15).** Syntomicity of a morphism of algebraic spaces is invariant under
> a flat deformation.

```lean
theorem isSyntomic_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    IsSyntomic B S hS D.f.hom ↔ IsSyntomic B S hS D.f'.hom
```

**`AlgebraicGeometry.Space.isSmooth_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean#L227). The attribute's comment: “part (16): smooth”.

> **Stacks 0CGX, part (16).** Smoothness of a morphism of algebraic spaces is invariant under a
> flat deformation.

```lean
theorem isSmooth_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    IsSmooth B S hS D.f.hom ↔ IsSmooth B S hS D.f'.hom
```

**`AlgebraicGeometry.Space.isUnramified_iff_isUnramified_deformation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean#L235). The attribute's comment: “part (17): unramified”.

> **Stacks 0CGX, part (17).** Unramifiedness of a morphism of algebraic spaces is invariant
> under a flat deformation.

```lean
theorem isUnramified_iff_isUnramified_deformation (D : FlatDeformationDiagram B S hS) :
    IsUnramified B S hS D.f.hom ↔ IsUnramified B S hS D.f'.hom
```

**`AlgebraicGeometry.Space.isEtale_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean#L243). The attribute's comment: “part (18): étale”.

> **Stacks 0CGX, part (18).** Étaleness of a morphism of algebraic spaces is invariant under a
> flat deformation.

```lean
theorem isEtale_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    IsEtale B S hS D.f.hom ↔ IsEtale B S hS D.f'.hom
```

**`AlgebraicGeometry.Space.universallyInjective_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean#L334). The attribute's comment: “part (10): universally injective”.

> **Stacks 0CGX, part (10).** Universal injectivity of a morphism of algebraic spaces is
> invariant under a flat deformation.

```lean
theorem universallyInjective_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    UniversallyInjective B S hS D.f.hom ↔ UniversallyInjective B S hS D.f'.hom
```

**`AlgebraicGeometry.Space.isIso_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformation.lean#L350). The attribute's comment: “part (3): isomorphism”.

> **Stacks 0CGX, part (3).** Being an isomorphism is invariant under a flat deformation of
> algebraic spaces.

```lean
theorem isIso_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    IsIso D.f.hom ↔ IsIso D.f'.hom
```

**`AlgebraicGeometry.Space.isFiniteLocallyFree_iff_and_isFiniteLocallyFreeOfRank_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationFiniteLocallyFree.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationFiniteLocallyFree.lean#L161). The attribute's comment: “part (21): finite locally free, and finite locally free of rank d”.

> **Stacks 0CGX, part (21).** Being finite locally free, and being finite locally free of a
> given rank `d`, in the sense of Stacks 03ZV — affine, with `f_*𝒪_X` a finite locally free
> `𝒪_Y`-module (of rank `d`) — are each invariant under a flat deformation of algebraic spaces.

```lean
theorem isFiniteLocallyFree_iff_and_isFiniteLocallyFreeOfRank_iff_of_flatDeformationDiagram
    (D : FlatDeformationDiagram B S hS) :
    (IsFiniteLocallyFree B S hS D.f ↔ IsFiniteLocallyFree B S hS D.f') ∧
      ∀ d : ℕ,
        IsFiniteLocallyFreeOfRank B S hS D.f d ↔ IsFiniteLocallyFreeOfRank B S hS D.f' d
```

**`AlgebraicGeometry.Space.relativelyRepresentable_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean#L115). The attribute's comment: “part (1): representable”.

> Representability of a morphism of algebraic spaces is invariant under a flat deformation.

```lean
theorem relativelyRepresentable_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    yoneda.relativelyRepresentable D.f.hom ↔ yoneda.relativelyRepresentable D.f'.hom
```

**`AlgebraicGeometry.Space.isQuasiCompact_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean#L123). The attribute's comment: “part (5): quasi-compact”.

> Quasi-compactness of a morphism of algebraic spaces is invariant under a flat deformation.

```lean
theorem isQuasiCompact_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    IsQuasiCompact B S hS D.f.hom ↔ IsQuasiCompact B S hS D.f'.hom
```

**`AlgebraicGeometry.Space.universallyClosed_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean#L132). The attribute's comment: “part (6): universally closed”.

> Universal closedness of a morphism of algebraic spaces is invariant under a flat
> deformation.

```lean
theorem universallyClosed_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    UniversallyClosed B S hS D.f.hom ↔ UniversallyClosed B S hS D.f'.hom
```

**`AlgebraicGeometry.Space.isSeparated_iff_and_isQuasiSeparated_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean#L141). The attribute's comment: “part (7): separated, and quasi-separated”.

> Separatedness, and quasi-separatedness, of a morphism of algebraic spaces are each invariant
> under a flat deformation.

```lean
theorem isSeparated_iff_and_isQuasiSeparated_iff_of_flatDeformationDiagram
    (D : FlatDeformationDiagram B S hS) :
    (IsSeparated B S hS D.f.hom ↔ IsSeparated B S hS D.f'.hom) ∧
      (IsQuasiSeparated B S hS D.f.hom ↔ IsQuasiSeparated B S hS D.f'.hom)
```

**`AlgebraicGeometry.Space.isAffineHom_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean#L156). The attribute's comment: “part (11): affine”.

> Affineness of a morphism of algebraic spaces is invariant under a flat deformation.

```lean
theorem isAffineHom_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    IsAffineHom B S hS D.f.hom ↔ IsAffineHom B S hS D.f'.hom
```

**`AlgebraicGeometry.Space.universallyOpen_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean#L164). The attribute's comment: “part (14): universally open”.

> Universal openness of a morphism of algebraic spaces is invariant under a flat deformation.

```lean
theorem universallyOpen_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    UniversallyOpen B S hS D.f.hom ↔ UniversallyOpen B S hS D.f'.hom
```

**`AlgebraicGeometry.Space.mono_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean#L181). The attribute's comment: “part (8): monomorphism”.

> Being a monomorphism is invariant under a flat deformation of algebraic spaces.

```lean
theorem mono_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    Mono D.f.hom ↔ Mono D.f'.hom
```

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_and_hasRelativeDimension_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean#L196). The attribute's comment: “part (13): locally of finite type of relative dimension d”.

> Being locally of finite type of relative dimension `d` is invariant under a flat deformation of
> algebraic spaces: the morphism under study is locally of finite type of relative dimension `d`
> exactly when its ambient deformation is.

```lean
theorem isLocallyOfFiniteType_and_hasRelativeDimension_iff_of_flatDeformationDiagram
    (D : FlatDeformationDiagram B S hS) (d : ℕ) :
    (IsLocallyOfFiniteType B S hS D.f.hom ∧ HasRelativeDimension d B S hS D.f.hom) ↔
      (IsLocallyOfFiniteType B S hS D.f'.hom ∧ HasRelativeDimension d B S hS D.f'.hom)
```

**`AlgebraicGeometry.Space.isProper_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean#L212). The attribute's comment: “part (19): proper”.

> Properness of a morphism of algebraic spaces is invariant under a flat deformation.

```lean
theorem isProper_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    IsProper B S hS D.f.hom ↔ IsProper B S hS D.f'.hom
```

**`AlgebraicGeometry.Space.isFinite_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationMorphismClasses.lean#L221). The attribute's comment: “part (20): finite”.

> Finiteness of a morphism of algebraic spaces is invariant under a flat deformation.

```lean
theorem isFinite_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    IsFinite B S hS D.f.hom ↔ IsFinite B S hS D.f'.hom
```

**`AlgebraicGeometry.Space.isOpenImmersion_iff_of_flatDeformationDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationOpenImmersion.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Deformations/FlatDeformationOpenImmersion.lean#L41). The attribute's comment: “part (4): open immersion”.

> Being an open immersion is invariant under a flat deformation of algebraic spaces: `f` is an
> open immersion if and only if `f'` is.

```lean
theorem isOpenImmersion_iff_of_flatDeformationDiagram (D : FlatDeformationDiagram B S hS) :
    IsOpenImmersion B S hS D.f.hom ↔ IsOpenImmersion B S hS D.f'.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.18, Tag 06BG](https://stacks.math.columbia.edu/tag/06BG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
