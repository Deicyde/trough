---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.preservesCoproducts_rightAdjoint_quasicoherentDerivedPushforward_of_isProper, AlgebraicGeometry.Space.isIso_quasicoherentDerivedCompareWithPullback_app_of_isProper, AlgebraicGeometry.Space.isLE_derivedModulePushforward_affineRightAdjoint, AlgebraicGeometry.Space.isPerfectRelativeToCanonical_affineRightAdjoint, AlgebraicGeometry.Space.isIso_smallEtaleDerivedHomothety_affineRightAdjoint
statement: formalized
proof: formalized
---

# 86.8 Right adjoint of pushforward for proper flat morphisms

Section 86.8 of the Stacks Project, [Tag 0E5S](https://stacks.math.columbia.edu/tag/0E5S). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E5T, a lemma

[Tag 0E5T](https://stacks.math.columbia.edu/tag/0E5T) in the Stacks Project.

**`AlgebraicGeometry.Space.preservesCoproducts_rightAdjoint_quasicoherentDerivedPushforward_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityRightAdjointDirectSums.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityRightAdjointDirectSums.lean#L75).

> Let `Y` be a quasi-compact and quasi-separated algebraic space and
> `f : X ⟶ Y` a proper, flat morphism of finite presentation. Then the right adjoint `a` of
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` (Stacks 0E55) commutes with direct sums.

```lean
theorem preservesCoproducts_rightAdjoint_quasicoherentDerivedPushforward_of_isProper
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hYqc : IsQuasiCompactSpace B S hS Y.1)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y.1) (hf : IsProper B S hS f.hom)
    (hfl : IsFlat B S hS f.hom) (hfp : IsFinitePresentation B S hS f.hom) :
    haveI := isLeftAdjoint_quasicoherentDerivedPushforward hZ f
      (isQuasiCompactSpace_of_isQuasiCompact B S hS Y.2 hYqc f.hom hfp.2.1)
      (isAbsolutelyQuasiSeparated_of_isQuasiSeparated B S hS hZ X.2 hYqs hfp.2.2) hYqs
    ∀ I : Type u, PreservesColimitsOfShape (Discrete I)
      (quasicoherentDerivedPushforward B S hS f hfp.2.1 hfp.2.2).rightAdjoint
```

## Tag 0E5U, a lemma

[Tag 0E5U](https://stacks.math.columbia.edu/tag/0E5U) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_quasicoherentDerivedCompareWithPullback_app_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparisonProperFlat.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityPullbackComparisonProperFlat.lean#L43).

> Let `Y` be a quasi-compact and quasi-separated algebraic space and `f : X ⟶ Y` a proper,
> flat morphism of finite presentation, with right adjoint `a` of
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` (Stacks 0E55). The map `Lf^*K ⊗^L a(𝒪_Y) ⟶ a(K)` of
> Stacks 0E5P is an isomorphism for every `K ∈ D_QCoh(𝒪_Y)`.

```lean
theorem isIso_quasicoherentDerivedCompareWithPullback_app_of_isProper
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hYqc : IsQuasiCompactSpace B S hS Y.1)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y.1) (hf : IsProper B S hS f.hom)
    (hfl : IsFlat B S hS f.hom) (hfp : IsFinitePresentation B S hS f.hom)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS Y.1 Y.2) :
    IsIso ((quasicoherentDerivedCompareWithPullback hZ f
      (isQuasiCompactSpace_of_isQuasiCompact B S hS Y.2 hYqc f.hom hfp.2.1)
      (isAbsolutelyQuasiSeparated_of_isQuasiSeparated B S hS hZ X.2 hYqs hfp.2.2) hYqs).app K)
```

## Tag 0E5V, a lemma

[Tag 0E5V](https://stacks.math.columbia.edu/tag/0E5V) in the Stacks Project.

**`AlgebraicGeometry.Space.isLE_derivedModulePushforward_affineRightAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DualityRelativeDualizingAffineBounds.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DualityRelativeDualizingAffineBounds.lean#L50). The attribute's comment: “(2)”.

> **Stacks 0E5V (2).** For `Y` affine and `f : X ⟶ Y` proper, flat and of finite
> presentation, `Rf_* a(𝒪_Y)` has vanishing cohomology sheaves in positive degrees.

```lean
theorem isLE_derivedModulePushforward_affineRightAdjoint (hf : IsProper B S hS f.hom)
    (hfl : IsFlat B S hS f.hom) (hfp : IsFinitePresentation B S hS f.hom)
    (hY : IsAffineSpace B S hS Y.1) :
    ((derivedModulePushforward B S hS f).obj
      ((affineRightAdjoint hZ f hfp hY).obj
        (derivedStructureSheaf B S hS Y.1 Y.2)).obj).IsLE 0
```

**`AlgebraicGeometry.Space.isPerfectRelativeToCanonical_affineRightAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplexAffinePerfect.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplexAffinePerfect.lean#L61). The attribute's comment: “(1)”.

> **Stacks 0E5V (1).** For `Y` affine and `f : X ⟶ Y` proper, flat and of finite
> presentation, with `a` the right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`, the object
> `a(𝒪_Y)` of `D(𝒪_X)` is `Y`-perfect.

```lean
theorem isPerfectRelativeToCanonical_affineRightAdjoint {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsProper B S hS f.hom) (hfl : IsFlat B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom) (hY : IsAffineSpace B S hS Y.1) :
    IsPerfectRelativeToCanonical.{u, u + 1, u + 1} B S hS f hfl hfp.1
      ((affineRightAdjoint hZ f hfp hY).obj (derivedStructureSheaf B S hS Y.1 Y.2)).obj
```

**`AlgebraicGeometry.Space.isIso_smallEtaleDerivedHomothety_affineRightAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplexAffinePerfect.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDualizingComplexAffinePerfect.lean#L114). The attribute's comment: “(3)”.

> **Stacks 0E5V (3).** For `Y` affine and `f : X ⟶ Y` proper, flat and of finite
> presentation, with `a` the right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`, the map
> `𝒪_X ⟶ R𝓗om(a(𝒪_Y), a(𝒪_Y))` is an isomorphism.

```lean
theorem isIso_smallEtaleDerivedHomothety_affineRightAdjoint {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsProper B S hS f.hom) (hfl : IsFlat B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom) (hY : IsAffineSpace B S hS Y.1) :
    IsIso (smallEtaleDerivedHomothety B S hS X
      ((affineRightAdjoint hZ f hfp hY).obj (derivedStructureSheaf B S hS Y.1 Y.2)).obj)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 86.8, Tag 0E5S](https://stacks.math.columbia.edu/tag/0E5S)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
