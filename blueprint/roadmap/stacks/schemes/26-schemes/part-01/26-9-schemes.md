---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme, AlgebraicGeometry.Scheme.Hom, AlgebraicGeometry.Scheme.instCategory, AlgebraicGeometry.PresheafedSpace.IsOpenImmersion.toScheme, AlgebraicGeometry.Scheme.Opens.toScheme, AlgebraicGeometry.PuncturedAffinePlane.xOpen_sup_yOpen, AlgebraicGeometry.PuncturedAffinePlane.isAffineOpen_xOpen, AlgebraicGeometry.PuncturedAffinePlane.isAffineOpen_yOpen
statement: formalized
proof: formalized
---

# 26.9 Schemes

Section 26.9 of the Stacks Project, [Tag 01II](https://stacks.math.columbia.edu/tag/01II). 3 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01IJ, a definition

[Tag 01IJ](https://stacks.math.columbia.edu/tag/01IJ) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L159) (StacksFrontier): “a scheme: a locally ringed space locally isomorphic to an affine scheme”. References: EGA I (2.1.2); EGA I (10.4.2), “special case”; SGA 2 XIV (1.0); SGA 3 IV (4.7); SGA 4 VII (1.1); SGA 4 XVII (0.7); SGA 6 II (3.0).
- [`AlgebraicGeometry.Scheme.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L161) (StacksFrontier): “a morphism of schemes: a morphism of locally ringed spaces”. References: EGA I (2.2.1); EGA I (2.2.2); EGA I (10.4.5), “special case”.
- [`AlgebraicGeometry.Scheme.instCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.instCategory#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L163) (StacksFrontier): “the category of schemes”. References: EGA I (2.2.2); SGA 4 VII (1.1).

## Tag 01IK, a lemma

[Tag 01IK](https://stacks.math.columbia.edu/tag/01IK) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.PresheafedSpace.IsOpenImmersion.toScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.PresheafedSpace.IsOpenImmersion.toScheme#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L165) (StacksFrontier): “the source of an open immersion into a scheme is a scheme”.
- [`AlgebraicGeometry.Scheme.Opens.toScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Opens.toScheme#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L167) (StacksFrontier): “an open subspace of a scheme is a scheme”. References: EGA I (10.4.4), “special case”; EGA I (2.1.7); EGA I (2.2.10); EGA I (2.2.3); EGA I (4.1.3), “special case”; EGA IV (4.5.3), “partial”; EGA IV (4.9.6), “partial”; EGA IV (9.6.7); EGA IV (9.7.11), “more general”; SGA 2 XII (4.1).

## Tag 01IL, an example

[Tag 01IL](https://stacks.math.columbia.edu/tag/01IL) in the Stacks Project.

**`AlgebraicGeometry.PuncturedAffinePlane.xOpen_sup_yOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlane.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlane.lean#L229). The attribute's comment: “affine\_open\_cover”.

> The two coordinate standard opens cover the punctured affine plane.

```lean
theorem xOpen_sup_yOpen : xOpen S ⊔ yOpen S = ⊤
```

**`AlgebraicGeometry.PuncturedAffinePlane.isAffineOpen_xOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlane.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlane.lean#L251). The attribute's comment: “affine\_open\_cover”.

> The first-coordinate member of the standard cover is affine.

```lean
theorem isAffineOpen_xOpen : IsAffineOpen (xOpen S)
```

**`AlgebraicGeometry.PuncturedAffinePlane.isAffineOpen_yOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlane.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlane.lean#L256). The attribute's comment: “affine\_open\_cover”.

> The second-coordinate member of the standard cover is affine.

```lean
theorem isAffineOpen_yOpen : IsAffineOpen (yOpen S)
```

**`AlgebraicGeometry.PuncturedAffinePlane.xOpen_inf_yOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlane.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlane.lean#L261). The attribute's comment: “affine\_open\_cover”.

> The intersection of the two members of the cover is the product standard open.

```lean
theorem xOpen_inf_yOpen : xOpen S ⊓ yOpen S = xyOpen S
```

**`AlgebraicGeometry.PuncturedAffinePlane.toScheme_iso_specAway_x`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlane.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlane.lean#L267). The attribute's comment: “affine\_open\_cover”.

> The first-coordinate standard open has coordinate ring `k[x,y,1/x]`.

```lean
theorem toScheme_iso_specAway_x :
    Nonempty ((xOpen S).toScheme ≅
      Spec (.of (Localization.Away (MvPolynomial.X (0 : Fin 2) : S.R))))
```

**`AlgebraicGeometry.PuncturedAffinePlane.toScheme_iso_specAway_y`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlane.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlane.lean#L274). The attribute's comment: “affine\_open\_cover”.

> The second-coordinate standard open has coordinate ring `k[x,y,1/y]`.

```lean
theorem toScheme_iso_specAway_y :
    Nonempty ((yOpen S).toScheme ≅
      Spec (.of (Localization.Away (MvPolynomial.X (1 : Fin 2) : S.R))))
```

**`AlgebraicGeometry.PuncturedAffinePlane.toScheme_iso_specAway_xy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlane.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlane.lean#L281). The attribute's comment: “affine\_open\_cover”.

> The intersection standard open has coordinate ring `k[x,y,1/(xy)]`.

```lean
theorem toScheme_iso_specAway_xy :
    Nonempty ((xyOpen S).toScheme ≅ Spec (.of (Localization.Away
      (MvPolynomial.X (0 : Fin 2) * MvPolynomial.X (1 : Fin 2) : S.R))))
```

**`AlgebraicGeometry.not_isAffine_puncturedScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlaneNotAffine.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlaneNotAffine.lean#L40). The attribute's comment: “punctured\_plane\_not\_affine”.

> The affine plane with its origin removed is not affine.

```lean
theorem not_isAffine_puncturedScheme (S : PuncturedAffinePlane.{u}) :
    ¬ IsAffine S.puncturedScheme
```

**`AlgebraicGeometry.restrictionPair_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlaneSections.lean, line 344](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlaneSections.lean#L344). The attribute's comment: “sections\_exact\_sequence”.

> **Stacks Project, Tag 01IL, sections exact sequence.** Restriction of global
> sections to the two standard affine opens is injective.

```lean
theorem restrictionPair_injective (S : PuncturedAffinePlane.{u}) :
    Function.Injective (restrictionPair S)
```

**`AlgebraicGeometry.restrictionPair_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlaneSections.lean, line 431](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlaneSections.lean#L431). The attribute's comment: “sections\_exact\_sequence”.

> **Stacks Project, Tag 01IL, sections exact sequence.** The image of global
> sections in the product of the two localizations is the kernel of the
> difference of restrictions to the intersection.

```lean
theorem restrictionPair_exact (S : PuncturedAffinePlane.{u}) :
    Function.Exact (restrictionPair S) (localizationDifference S)
```

**`AlgebraicGeometry.isIso_coordinateRingToGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlaneSections.lean, line 564](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Affine/PuncturedPlaneSections.lean#L564). The attribute's comment: “punctured\_plane\_global\_sections”.

> The canonical homomorphism from the coordinate ring of the affine plane to the global
> sections of the punctured affine plane is an isomorphism.

```lean
theorem isIso_coordinateRingToGlobalSections (S : PuncturedAffinePlane.{u}) :
    IsIso ((Scheme.ΓSpecIso (.of S.R)).inv ≫ S.openImmersion.appTop)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.9, Tag 01II](https://stacks.math.columbia.edu/tag/01II)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
