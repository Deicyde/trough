---
declaration: section
origin: cited
lean: AlgebraicGeometry.quasicoherentIntegralTransformData, AlgebraicGeometry.quasicoherentIntegralTransform_additive, AlgebraicGeometry.quasicoherentIntegralTransform_isLinearOverBase, AlgebraicGeometry.quasicoherentIntegralTransform_preservesDirectSums, AlgebraicGeometry.quasiCompact_of_compactSpace, AlgebraicGeometry.quasiCompact_isStableUnderBaseChange, AlgebraicGeometry.QuasiSeparated.of_quasiSeparatedSpace, AlgebraicGeometry.quasiSeparated_isStableUnderBaseChange
statement: formalized
proof: formalized
---

# 56.5 Functors between categories of quasi-coherent modules

Section 56.5 of the Stacks Project, [Tag 0FZA](https://stacks.math.columbia.edu/tag/0FZA). 11 tags here are carried by 22 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FZB, an example

[Tag 0FZB](https://stacks.math.columbia.edu/tag/0FZB) in the Stacks Project.

**`AlgebraicGeometry.quasicoherentIntegralTransformData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean#L153). The attribute's comment: “the functor”.

> **Stacks Project, Tag 0FZB (the functor).** A quasi-coherent kernel on `X ×_R Y`
> defines the pullback--tensor--pushforward functor from quasi-coherent modules on `X` to
> quasi-coherent modules on `Y`.

```lean
noncomputable def quasicoherentIntegralTransformData
    (R : Type u) [CommRing R] (X Y : Over (Spec (.of R)))
    [CompactSpace X.left] [QuasiSeparatedSpace X.left]
    (K : (SheafOfModules.isQuasicoherent
      (pullback X.hom Y.hom).ringCatSheaf).FullSubcategory) :
    IntegralTransformData R X Y K
```

**`AlgebraicGeometry.quasicoherentIntegralTransform_additive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean#L425). The attribute's comment: “additivity”.

> The integral transform is additive on morphisms.

```lean
theorem quasicoherentIntegralTransform_additive
    (R : Type u) [CommRing R] (X Y : Over (Spec (.of R)))
    [CompactSpace X.left] [QuasiSeparatedSpace X.left]
    (K : (SheafOfModules.isQuasicoherent
      (pullback X.hom Y.hom).ringCatSheaf).FullSubcategory) :
    (quasicoherentIntegralTransform R X Y K).Additive
```

**`AlgebraicGeometry.quasicoherentIntegralTransform_isLinearOverBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean, line 480](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean#L480). The attribute's comment: “R-linearity”.

> **Stacks Project, Tag 0FZB (linearity).** The integral transform associated to a
> quasi-coherent kernel is linear over the base ring.

```lean
theorem quasicoherentIntegralTransform_isLinearOverBase
    (R : Type u) [CommRing R] (X Y : Over (Spec (.of R)))
    [CompactSpace X.left] [QuasiSeparatedSpace X.left]
    (K : (SheafOfModules.isQuasicoherent
      (pullback X.hom Y.hom).ringCatSheaf).FullSubcategory) :
    letI : Linear R (SheafOfModules.{u} X.left.ringCatSheaf) := modulesLinear R X
    letI : Linear R (SheafOfModules.{u} Y.left.ringCatSheaf) := modulesLinear R Y
    (quasicoherentIntegralTransform R X Y K).Linear R
```

**`AlgebraicGeometry.quasicoherentIntegralTransform_preservesDirectSums`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean, line 598](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean#L598). The attribute's comment: “arbitrary direct sums”.

> **Stacks Project, Tag 0FZB (direct sums).** The integral transform associated to a
> quasi-coherent kernel commutes with arbitrary direct sums.

```lean
theorem quasicoherentIntegralTransform_preservesDirectSums
    (R : Type u) [CommRing R] (X Y : Over (Spec (.of R)))
    [CompactSpace X.left] [QuasiSeparatedSpace X.left]
    (K : (SheafOfModules.isQuasicoherent
      (pullback X.hom Y.hom).ringCatSheaf).FullSubcategory) (I : Type u) :
    PreservesColimitsOfShape (Discrete I)
      (quasicoherentIntegralTransform R X Y K)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.quasiCompact_of_compactSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiCompact_of_compactSpace#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean#L82) (StacksFrontier): “quasi-compactness: source criterion”. References: EGA IV (1.2.4), “Case Z = Spec ℤ”; SGA 3 VIB (11.1), “special case”; SGA 3 VIB (12.9), “special case”; SGA 4 VI (1.14), “(i), special case”; SGA 4 VI (1.8), “(iv), special case”; SGA 4 VI (1.9.1), “(iv), special case”.
- [`AlgebraicGeometry.quasiCompact_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiCompact_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean#L90) (StacksFrontier): “quasi-compactness: base change”. References: EGA I (6.3.4), “clause (iv)”; EGA I (6.6.4); EGA III (6.9.1), “partial”; EGA III (6.9.4), “more general”; EGA III (7.7.2), “quasi-compactness of f'”; EGA IV (1.1.2); EGA IV (2.3.7), “(i)”; EGA IV (2.6.4), “necessity in (v)”; SGA 1 VIII (3.3), “quasi-compact clause”; SGA 4 VI (1.8), “(ii), special case”; SGA 4 VI (1.9.1), “(ii), special case”; SGA 4 VIII (5.1), “partial”; SGA 7 VII (1.3.8), “partial”.
- [`AlgebraicGeometry.QuasiSeparated.of_quasiSeparatedSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiSeparated.of_quasiSeparatedSpace#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean#L107) (StacksFrontier): “quasi-separatedness: source criterion”. References: EGA IV (1.2.2), “(v), special case”; EGA IV (1.2.3); EGA IV (1.2.6), “partial”.
- [`AlgebraicGeometry.quasiSeparated_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiSeparated_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Basic.lean#L112) (StacksFrontier): “quasi-separatedness: base change”. References: EGA IV (1.2.2); EGA IV (2.7.1), “(ii)”; SGA 4 VI (1.8), “(ii), special case”; SGA 4 VI (1.9.1), “(ii), special case”; SGA 4 VIII (5.1), “partial”; SGA 7 VII (1.3.8), “partial”.

## Tag 0FZD, a lemma

[Tag 0FZD](https://stacks.math.columbia.edu/tag/0FZD) in the Stacks Project.

**`AlgebraicGeometry.integralTransformQcohFunctorLift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Equivalence.lean, line 1967](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Equivalence.lean#L1967). The attribute's comment: “the functor from quasi-coherent kernels to right exact linear functors”.

> **Stacks Project, Tag 0FZD.** For `X` affine, the integral transform of a quasi-coherent
> kernel on `X ×_R Y`, as a functor of the kernel, with codomain the `R`-linear right exact
> functors from quasi-coherent modules on `X` to quasi-coherent modules on `Y` which commute with
> arbitrary direct sums.

```lean
noncomputable def integralTransformQcohFunctorLift
    (R : Type u) [CommRing R] (X Y : Over (Spec (.of R))) [IsAffine X.left] :
    (SheafOfModules.isQuasicoherent
      (pullback X.hom Y.hom).ringCatSheaf).FullSubcategory ⥤
      (rightExactLinearCoproductFunctor R X Y).FullSubcategory
```

**`AlgebraicGeometry.integralTransformQcohFunctorLift_obj_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Equivalence.lean, line 1979](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Equivalence.lean#L1979). The attribute's comment: “the functor sends a kernel to its integral transform”.

> **Stacks Project, Tag 0FZD.** For `X` affine, the integral transform of a quasi-coherent
> kernel on `X ×_R Y` is, on objects, the functor `F ↦ pr_{2,*}(pr_1^* F ⊗ K)` of Tag 0FZB.

```lean
theorem integralTransformQcohFunctorLift_obj_obj
    (R : Type u) [CommRing R] (X Y : Over (Spec (.of R))) [IsAffine X.left]
    (K : (SheafOfModules.isQuasicoherent
      (pullback X.hom Y.hom).ringCatSheaf).FullSubcategory) :
    ((integralTransformQcohFunctorLift R X Y).obj K).obj =
      quasicoherentIntegralTransform R X Y K
```

**`AlgebraicGeometry.faithful_integralTransformQcohFunctorLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Equivalence.lean, line 1989](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Equivalence.lean#L1989). The attribute's comment: “the functor is faithful”.

> **Stacks Project, Tag 0FZD.** For `X` affine, the functor sending a quasi-coherent kernel
> on `X ×_R Y` to its integral transform is faithful.

```lean
theorem faithful_integralTransformQcohFunctorLift
    (R : Type u) [CommRing R] (X Y : Over (Spec (.of R))) [IsAffine X.left] :
    (integralTransformQcohFunctorLift R X Y).Faithful
```

**`AlgebraicGeometry.full_integralTransformQcohFunctorLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Equivalence.lean, line 2010](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Equivalence.lean#L2010). The attribute's comment: “the functor is full”.

> **Stacks Project, Tag 0FZD.** For `X` affine, the functor sending a quasi-coherent kernel
> on `X ×_R Y` to its integral transform is full.

```lean
theorem full_integralTransformQcohFunctorLift
    (R : Type u) [CommRing R] (X Y : Over (Spec (.of R))) [IsAffine X.left] :
    (integralTransformQcohFunctorLift R X Y).Full
```

**`AlgebraicGeometry.essSurj_integralTransformQcohFunctorLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Equivalence.lean, line 2032](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Equivalence.lean#L2032). The attribute's comment: “the functor is essentially surjective”.

> **Stacks Project, Tag 0FZD.** For `X` affine, every `R`-linear right exact functor from
> quasi-coherent modules on `X` to quasi-coherent modules on `Y` which commutes with arbitrary
> direct sums is the integral transform of a quasi-coherent kernel on `X ×_R Y`.

```lean
theorem essSurj_integralTransformQcohFunctorLift
    (R : Type u) [CommRing R] (X Y : Over (Spec (.of R))) [IsAffine X.left] :
    (integralTransformQcohFunctorLift R X Y).EssSurj
```

**`AlgebraicGeometry.integralTransformQcohEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Equivalence.lean, line 2044](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Equivalence.lean#L2044). The attribute's comment: “the equivalence of categories”.

> **Stacks Project, Tag 0FZD.** For `X` affine, the integral transform of a quasi-coherent
> kernel is an equivalence from the quasi-coherent modules on `X ×_R Y` to the `R`-linear right
> exact functors from quasi-coherent modules on `X` to quasi-coherent modules on `Y` which
> commute with arbitrary direct sums.

```lean
noncomputable def integralTransformQcohEquivalence
    (R : Type u) [CommRing R] (X Y : Over (Spec (.of R))) [IsAffine X.left] :
    (SheafOfModules.isQuasicoherent (pullback X.hom Y.hom).ringCatSheaf).FullSubcategory ≌
      (rightExactLinearCoproductFunctor R X Y).FullSubcategory
```

**`AlgebraicGeometry.integralTransformQcohEquivalence_functor_obj_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Equivalence.lean, line 2057](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Equivalence.lean#L2057). The attribute's comment: “the equivalence sends a kernel to its integral transform”.

> **Stacks Project, Tag 0FZD.** The equivalence sends a quasi-coherent kernel on `X ×_R Y`
> to its integral transform `F ↦ pr_{2,*}(pr_1^* F ⊗ K)`.

```lean
theorem integralTransformQcohEquivalence_functor_obj_obj
    (R : Type u) [CommRing R] (X Y : Over (Spec (.of R))) [IsAffine X.left]
    (K : (SheafOfModules.isQuasicoherent
      (pullback X.hom Y.hom).ringCatSheaf).FullSubcategory) :
    ((integralTransformQcohEquivalence R X Y).functor.obj K).obj =
      quasicoherentIntegralTransform R X Y K
```

## Tag 0FZE, a remark

[Tag 0FZE](https://stacks.math.columbia.edu/tag/0FZE) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjectionFormula.isIso_projectionFormulaMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProjectionFormulaLocal.lean, line 470](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProjectionFormulaLocal.lean#L470). The attribute's comment: “the canonical map h\_*G ⊗ H ⟶ h\_*(G ⊗ h^*H) is an isomorphism for affine h and quasi-coherent G, H”.

> Let `h : T ⟶ S` be an affine morphism of schemes, `G` a quasi-coherent `𝒪_T`-module and `H` a
> quasi-coherent `𝒪_S`-module. Then the canonical projection-formula morphism
>
> `h_*G ⊗_{𝒪_S} H ⟶ h_*(G ⊗_{𝒪_T} h^*H)`
>
> is invertible.

```lean
theorem isIso_projectionFormulaMap [IsAffineHom h] (hG : G.IsQuasicoherent)
    (hH : H.IsQuasicoherent) : IsIso (projectionFormulaMap h G H)
```

## Tag 0FZF, a lemma

[Tag 0FZF](https://stacks.math.columbia.edu/tag/0FZF) in the Stacks Project.

**`AlgebraicGeometry.quasicoherentIntegralTransformSourceChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/ChangeOfSpaces.lean, line 321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/ChangeOfSpaces.lean#L321). The attribute's comment: “affine source change”.

> Let `X` be an affine scheme over `R`, let `f : X' ⟶ X` be an affine morphism of schemes over
> `R` and let `K` be a quasi-coherent module on `X ×_R Y`.  Then the integral transform of `K`
> precomposed with the direct image along `f` is the integral transform of `(f × id_Y)^*K`.

```lean
def quasicoherentIntegralTransformSourceChangeIso (R : Type u) [CommRing R]
    (X X' Y : Over (Spec (.of R))) [IsAffine X.left] (f : X' ⟶ X) [IsAffineHom f.left]
    (K : Scheme.QuasicoherentModules (pullback X.hom Y.hom)) :
    letI : IsAffine X'.left := isAffine_of_isAffineHom f.left
    quasicoherentPushforward f.left ⋙ quasicoherentIntegralTransform R X Y K ≅
      quasicoherentIntegralTransform R X' Y (sourceChangeKernel R X X' Y f K)
```

**`AlgebraicGeometry.quasicoherentIntegralTransformTargetChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/ChangeOfSpaces.lean, line 420](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/ChangeOfSpaces.lean#L420). The attribute's comment: “flat target change”.

> Let `X` be an affine scheme over `R`, let `g : Y' ⟶ Y` be a flat morphism of schemes over `R`
> and let `K` be a quasi-coherent module on `X ×_R Y`.  Then the integral transform of `K` followed
> by the inverse image along `g` is the integral transform of `(id_X × g)^*K`.

```lean
def quasicoherentIntegralTransformTargetChangeIso (R : Type u) [CommRing R]
    (X Y Y' : Over (Spec (.of R))) [IsAffine X.left] (g : Y' ⟶ Y) [Flat g.left]
    (K : Scheme.QuasicoherentModules (pullback X.hom Y.hom)) :
    quasicoherentIntegralTransform R X Y K ⋙ quasicoherentPullback g.left ≅
      quasicoherentIntegralTransform R X Y' (targetChangeKernel R X Y Y' g K)
```

**`AlgebraicGeometry.quasicoherentIntegralTransformOpenTargetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/ChangeOfSpaces.lean, line 472](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/ChangeOfSpaces.lean#L472). The attribute's comment: “open target restriction”.

> Let `X` be an affine scheme over `R`, let `j : V ⟶ Y` be an open immersion of schemes and let
> `K` be a quasi-coherent module on `X ×_R Y`.  Then the integral transform of `K` followed by
> restriction to `V` is the integral transform of the restriction of `K` to `X ×_R V`.

```lean
def quasicoherentIntegralTransformOpenTargetIso (R : Type u) [CommRing R]
    (X Y : Over (Spec (.of R))) [IsAffine X.left] {V : Scheme.{u}} (j : V ⟶ Y.left)
    [IsOpenImmersion j] (K : Scheme.QuasicoherentModules (pullback X.hom Y.hom)) :
    quasicoherentIntegralTransform R X Y K ⋙ quasicoherentRestriction j ≅
      quasicoherentIntegralTransform R X (Over.mk (j ≫ Y.hom))
        (openTargetKernel R X Y j K)
```

## Tag 0GPA, a lemma

[Tag 0GPA](https://stacks.math.columbia.edu/tag/0GPA) in the Stacks Project.

**`AlgebraicGeometry.exists_kernel_natTrans_isIso_whiskerLeft_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/KernelOfFunctor.lean, line 958](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/KernelOfFunctor.lean#L958).

> **Tag 0GPA.**  Let `R` be a ring, let `X` and `Y` be schemes over `R` with `X` quasi-compact
> with affine diagonal, and let `F : QCoh(𝒪_X) ⥤ QCoh(𝒪_Y)` be `R`-linear, right exact and
> commute with arbitrary direct sums.  Then there are a quasi-coherent module `K` on `X ×_R Y` and a
> natural transformation `t : F ⟶ F_K` such that `t ∘ f_* : F ∘ f_* ⟶ F_K ∘ f_*` is an
> isomorphism for every morphism `f : X' ⟶ X` whose source is an affine scheme.
>
> The kernel is `AlgebraicGeometry.AffineChartKernels.glued` of
> `AlgebraicGeometry.openKernelSystem`, glued from the kernels of `F ∘ j_{U,*}` over the affine
> opens `U` of `X`, and `t` is `AlgebraicGeometry.kernelTransform`.

```lean
theorem exists_kernel_natTrans_isIso_whiskerLeft_pushforward [CompactSpace X.left]
    [IsAffineHom (pullback.diagonal (terminal.from X.left))]
    (hF : rightExactLinearCoproductFunctor R X Y F) :
    ∃ (K : Scheme.QuasicoherentModules (pullback X.hom Y.hom))
      (t : F ⟶ quasicoherentIntegralTransform R X Y K),
      ∀ (X' : Scheme.{u}) [IsAffine X'] (f : X' ⟶ X.left),
        letI : IsAffineHom f :=
          Stacks.AlgebraicGeometry.RelativeCechComplex.isAffineHom_of_isAffine_source f
        IsIso (Functor.whiskerLeft (quasicoherentPushforward f) t)
```

## Tag 0FZG, a lemma

[Tag 0FZG](https://stacks.math.columbia.edu/tag/0FZG) in the Stacks Project.

**`AlgebraicGeometry.isFlatOver_kernel_of_exactFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/KernelFlatnessGlued.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/KernelFlatnessGlued.lean#L160). The attribute's comment: “the kernel corresponding to an exact functor is flat over X, both for X affine and for X quasi-compact with affine diagonal”.

> **The kernel of an exact functor is flat.** In the situation of Tag 0FZD or of Tag 0GPA, if
> `F` is an exact functor, then the corresponding object `K` of `QCoh(𝒪_{X ×_R Y})` is flat over
> `X`.
>
> The four conjuncts are:
> 1. the situation of Tag 0FZD (`X` affine, `Y` arbitrary), for every kernel `K` whose integral
>    transform is isomorphic to `F`;
> 2. the same, for the kernel attached to `F` by the inverse of the equivalence of Tag 0FZD;
> 3. the situation of Tag 0GPA (`X` quasi-compact with affine diagonal), for every kernel `K` with
>    a natural transformation `t : F ⟶ F_K` such that `t ∘ f_*` is an isomorphism for every
>    morphism `f : X' ⟶ X` with `X'` affine;
> 4. the same, for the glued kernel constructed in Tag 0GPA from an `R`-linear right exact functor
>    commuting with arbitrary direct sums.

```lean
theorem isFlatOver_kernel_of_exactFunctor (R : Type u) [CommRing R] :
    (∀ (X Y : Over (Spec (.of R))) [IsAffine X.left]
      (K : Scheme.QuasicoherentModules (pullback X.hom Y.hom))
      (F : Scheme.QuasicoherentModules X.left ⥤ Scheme.QuasicoherentModules Y.left),
      (F ≅ quasicoherentIntegralTransform R X Y K) → exactFunctor _ _ F →
        IsFlatOver (pullback.fst X.hom Y.hom).toLRSHom.toShHom K.obj) ∧
    (∀ (X Y : Over (Spec (.of R))) [IsAffine X.left]
      (F : (rightExactLinearCoproductFunctor R X Y).FullSubcategory),
      exactFunctor _ _ F.obj →
        IsFlatOver (pullback.fst X.hom Y.hom).toLRSHom.toShHom
          ((integralTransformQcohEquivalence R X Y).inverse.obj F).obj) ∧
    (∀ (X Y : Over (Spec (.of R))) [CompactSpace X.left]
      [IsAffineHom (pullback.diagonal (terminal.from X.left))]
      (F : Scheme.QuasicoherentModules X.left ⥤ Scheme.QuasicoherentModules Y.left)
      (K : Scheme.QuasicoherentModules (pullback X.hom Y.hom))
      (t : F ⟶ quasicoherentIntegralTransform R X Y K),
      (∀ (X' : Scheme.{u}) [IsAffine X'] (f : X' ⟶ X.left),
        letI : IsAffineHom f :=
          Stacks.AlgebraicGeometry.RelativeCechComplex.isAffineHom_of_isAffine_source f
        IsIso (Functor.whiskerLeft (quasicoherentPushforward f) t)) →
      exactFunctor _ _ F →
        IsFlatOver (pullback.fst X.hom Y.hom).toLRSHom.toShHom K.obj) ∧
    (∀ (X Y : Over (Spec (.of R))) [CompactSpace X.left]
      [IsAffineHom (pullback.diagonal (terminal.from X.left))]
      (F : Scheme.QuasicoherentModules X.left ⥤ Scheme.QuasicoherentModules Y.left)
      (hF : rightExactLinearCoproductFunctor R X Y F),
      exactFunctor _ _ F →
        IsFlatOver (pullback.fst X.hom Y.hom).toLRSHom.toShHom
          (openKernelSystem R X Y F
            (affineOpenRightExactLinearCoproductFunctor_of_rightExact R X Y F hF)).glued.obj)
```

## Tag 0FZH, a lemma

[Tag 0FZH](https://stacks.math.columbia.edu/tag/0FZH) in the Stacks Project.

**`AlgebraicGeometry.isEquivalence_integralTransformExactKernelFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/ExactKernelEquivalence.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/ExactKernelEquivalence.lean#L74). The attribute's comment: “the functor sending a kernel K on X ×\_R Y to its integral transform is an equivalence from the kernels flat over X with vanishing higher direct images of pr\_1^*F ⊗ K onto the R-linear exact functors QCoh(X) ⥤ QCoh(Y) commuting with arbitrary direct sums”.

> Let `R` be a ring and let `X` and `Y` be schemes over `R` with `X` quasi-compact and with
> affine diagonal. The functor sending a quasi-coherent kernel `K` on `X ×_R Y` to its integral
> transform `F ↦ pr_{2,*}(pr_1^*F ⊗ K)` is an equivalence of categories between
>
> 1. the full subcategory of `QCoh(𝒪_{X ×_R Y})` of the kernels `K` which are flat over `X` and
>    satisfy `R^q pr_{2,*}(pr_1^*F ⊗ K) = 0` for all quasi-coherent `F` on `X` and all `q > 0`
>    (`AlgebraicGeometry.integralTransformExactKernel`), and
> 2. the category of `R`-linear exact functors `QCoh(𝒪_X) ⥤ QCoh(𝒪_Y)` which commute with
>    arbitrary direct sums (`AlgebraicGeometry.exactLinearCoproductFunctor`).

```lean
theorem isEquivalence_integralTransformExactKernelFunctor :
    (integralTransformExactKernelFunctor R X Y).IsEquivalence
```

## Tag 0GPB, a remark

[Tag 0GPB](https://stacks.math.columbia.edu/tag/0GPB) in the Stacks Project.

**`AlgebraicGeometry.nonempty_iso_quasicoherentIntegralTransform_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Characterization.lean, line 853](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Characterization.lean#L853).

> **Stacks Project, Tag 0GPB.**  Let `R` be a ring and let `X` and `Y` be schemes over `R`,
> with `X` quasi-compact with affine diagonal.  A functor `F : QCoh(𝒪_X) ⥤ QCoh(𝒪_Y)` is
> isomorphic to the integral transform `F_K = pr_{2,*}(pr_1^*(−) ⊗ K)` of a quasi-coherent module
> `K` on `X ×_R Y` if and only if
>
> 1. `F` is `R`-linear (in particular additive) and commutes with arbitrary direct sums,
> 2. `F ∘ j_*` is right exact for the inclusion `j : U ⟶ X` of every affine open `U`
>    (`AlgebraicGeometry.PreservesFiniteColimitsAfterAffineOpens`), and
> 3. `0 ⟶ F(F) ⟶ F(G) ⟶ F(H)` is exact for every short exact sequence
>    `0 ⟶ F ⟶ G ⟶ H ⟶ 0` of quasi-coherent modules whose sequences of stalks are split short
>    exact sequences of `𝒪_{X,x}`-modules (`AlgebraicGeometry.IsStalkwiseSplitLeftExact`).

```lean
theorem nonempty_iso_quasicoherentIntegralTransform_iff
    (F : Scheme.QuasicoherentModules X.left ⥤ Scheme.QuasicoherentModules Y.left) :
    letI : Linear R (SheafOfModules.{u} X.left.ringCatSheaf) := modulesLinear R X
    letI : Linear R (SheafOfModules.{u} Y.left.ringCatSheaf) := modulesLinear R Y
    (∃ K : Scheme.QuasicoherentModules (pullback X.hom Y.hom),
        Nonempty (F ≅ quasicoherentIntegralTransform R X Y K)) ↔
      ∃ _ : F.Additive, F.Linear R ∧ (∀ I : Type u, PreservesColimitsOfShape (Discrete I) F) ∧
        PreservesFiniteColimitsAfterAffineOpens R X F ∧ IsStalkwiseSplitLeftExact F
```

## Tag 0GPC, a lemma

[Tag 0GPC](https://stacks.math.columbia.edu/tag/0GPC) in the Stacks Project.

**`AlgebraicGeometry.quasicoherentIntegralTransformConvolutionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Convolution.lean, line 567](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/Convolution.lean#L567). The attribute's comment: “the composition formula F\_L ∘ F\_K ≅ F\_\{pr13,*(pr12^*K ⊗ pr23^*L)} as a natural isomorphism of functors QCoh(O\_X) to QCoh(O\_Z), for L a kernel of category (2) of 0FZH (so F\_L is R-linear, exact and commutes with direct sums), K arbitrary, X quasi-compact with affine diagonal and Y quasi-compact and quasi-separated”.

> **Stacks Project, Tag 0GPC.**  Let `R` be a ring and let `X`, `Y`, `Z` be schemes over `R`,
> with `X` quasi-compact with affine diagonal and `Y` quasi-compact and quasi-separated.  Let `K`
> be a quasi-coherent kernel on `X ×_R Y` and `L` a quasi-coherent kernel on `Y ×_R Z` in
> category (2) of Tag 0FZH, that is, flat over `Y` with vanishing higher direct images, so that its
> integral transform `F_L : QCoh(𝒪_Y) ⥤ QCoh(𝒪_Z)` is `R`-linear, exact and commutes with direct
> sums.  Then
>
> `F_L ∘ F_K ≅ F_{pr_{13,*}(pr_{12}^*K ⊗ pr_{23}^*L)}`
>
> as functors `QCoh(𝒪_X) ⥤ QCoh(𝒪_Z)`.
>
> This is the source's statement for exact functors `F` and `G` with kernels `K` and `L`
> (`G ∘ F ≅ F_L ∘ F_K`), in greater generality: nothing is assumed of `K`, and of `Y` only
> quasi-compactness and quasi-separatedness.  That, when `K` is of category (2) as well, the
> convolution is up to isomorphism the kernel of category (2) which Tag 0FZH attaches to `G ∘ F` is
> `AlgebraicGeometry.exists_integralTransformExactKernel_iso_convolutionKernel`.
>
> Exactness of `F_L` cannot be dropped.  Let `E` be an elliptic curve over a field `k` with origin
> `o`, let `C = E ∖ {e}` for a point `e ≠ o`, `R = Γ(C, 𝒪_C)`, `X = E ×_k C` over `R`, `Y = Spec R`,
> `Z = Spec k` the point `o` of `C`, `L = 𝒪_Z` on `Y ×_R Z = Z`, and `K = 𝒪(Δ - {o} × C)` on
> `X ×_R Y = X`, with `Δ` the graph of `C ⊆ E`.  The fibre of `K` over `c ∈ C` is `𝒪_E(c - o)`,
> nontrivial of degree zero for `c ≠ o`, so `Γ(X, K)`, a torsion-free `R`-module with zero generic
> fibre, vanishes and `F_L(F_K(𝒪_X)) = 0`.  But `X ×_R Y ×_R Z = E`, the convolution kernel is
> `K|_{E × {o}} ≅ 𝒪_E`, and `F_{K * L}(𝒪_X) = Γ(E, 𝒪_E) = k`.  Here `F_L = - ⊗_R k` is not left
> exact.

```lean
def quasicoherentIntegralTransformConvolutionIso (hL : integralTransformExactKernel R Y Z L) :
    quasicoherentIntegralTransform R X Y K ⋙ quasicoherentIntegralTransform R Y Z L ≅
      quasicoherentIntegralTransform R X Z (convolutionKernel R X Y Z K L)
```

## Tag 0FZI, a lemma

[Tag 0FZI](https://stacks.math.columbia.edu/tag/0FZI) in the Stacks Project.

**`AlgebraicGeometry.isZero_rightDerived_pushforward_baseChangeKernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/BaseChangeAcyclicity.lean, line 536](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/BaseChangeAcyclicity.lean#L536). The attribute's comment: “the positive higher direct images of pr\_12^*F ⊗ pr\_23^*K along pr\_13 vanish”.

> **Higher direct images of an integral-transform kernel after base change.**  Let `R` be a
> ring, let `X` and `Y` be schemes over `R` with the structure morphism of `X` quasi-compact and
> quasi-separated, and let `K` be a quasi-coherent kernel on `X ×_R Y` satisfying the two
> conditions of Tag 0FZH part (2).  Then for every scheme `T` over `R`,
> `R ^q pr_{13,*}(pr_{12}^*F ⊗ pr_{23}^*K) = 0` for every quasi-coherent `F` on `T ×_R X` and
> every `q > 0`.

```lean
theorem isZero_rightDerived_pushforward_baseChangeKernel (T X Y : Over (Spec (.of R)))
    [QuasiCompact X.hom] [QuasiSeparated X.hom]
    (K : Scheme.QuasicoherentModules (pullback X.hom Y.hom))
    (hK : integralTransformExactKernel R X Y K)
    (F : Scheme.QuasicoherentModules (baseChangeSourceOver R T X).left) (q : ℕ) (hq : 0 < q) :
    IsZero (((Scheme.Modules.pushforward (baseChangeTargetMap R T X Y)).rightDerived q).obj
      ((integralTransformIntegrand R (baseChangeSourceOver R T X) Y
        (baseChangeKernel R T X Y K)).obj F))
```

## Tag 0FZJ, a lemma

[Tag 0FZJ](https://stacks.math.columbia.edu/tag/0FZJ) in the Stacks Project.

**`AlgebraicGeometry.exists_epi_externalTensorProduct_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/DiagonalSurjection.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/IntegralTransformQcoh/DiagonalSurjection.lean#L485). The attribute's comment: “the surjection O\_X ⊠ F(O\_X) ⟶ K”.

> **Stacks Project, Tag 0FZJ.**  Let `R` be a ring, let `X` and `Y` be schemes over `R` with
> `X` quasi-compact, separated and flat over `R`, and let `K` be a quasi-coherent kernel on
> `X ×_R Y` satisfying the two conditions of [Stacks, Tag 0FZH] part (2).  Then there is a
> surjection `𝒪_X ⊠ F_K(𝒪_X) ⟶ K`, where `F_K` is the integral transform of `K`.
>
> The diagonal short exact sequence `0 → I → 𝒪_{X ×_R X} → 𝒪_Δ → 0` is sent by the exact
> integrand `pr_{12}^*(-) ⊗ pr_{23}^*K` to a short exact sequence on `X ×_R X ×_R Y`, and
> [Stacks, Tag 0FZI] makes its direct image along `pr_{13}` short exact again;  the surjection it
> exhibits is the one asserted, once flat base change identifies its source with
> `pr_2^*pr_{2,*}K = 𝒪_X ⊠ F_K(𝒪_X)` and the projection formula identifies its target with
> `K`.

```lean
theorem exists_epi_externalTensorProduct_unit (X Y : Over (Spec (.of R)))
    [CompactSpace X.left] [IsSeparated X.hom] [Flat X.hom]
    (K : Scheme.QuasicoherentModules (pullback X.hom Y.hom))
    (hK : integralTransformExactKernel R X Y K) :
    ∃ e : externalTensorProduct X.hom Y.hom (SheafOfModules.unit X.left.ringCatSheaf)
        ((quasicoherentIntegralTransform R X Y K).obj
          ⟨SheafOfModules.unit X.left.ringCatSheaf,
            Stacks.AlgebraicGeometry.AffineQcohPushforward.isQuasicoherent_unit
              X.left⟩).obj ⟶ K.obj, Epi e
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 56.5, Tag 0FZA](https://stacks.math.columbia.edu/tag/0FZA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
