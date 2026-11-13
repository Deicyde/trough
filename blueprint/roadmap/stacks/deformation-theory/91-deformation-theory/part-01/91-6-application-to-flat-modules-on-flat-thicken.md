---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSpaceThickening.FlatModuleDeformation.nonempty_flatLift_iff_flatDeformationObstruction_eq_zero, AlgebraicGeometry.RingedSpaceThickening.FlatModuleDeformation.flatLiftClassDifferenceBase_isPrincipalHomogeneous, AlgebraicGeometry.RingedSpaceThickening.FlatModuleDeformation.exists_identityLiftAut_equiv_ext_zero, AlgebraicGeometry.RingedSpaceThickening.FlatShortExactThickeningDiagram, AlgebraicGeometry.RingedSpaceThickening.boundary_flatLiftClassDifferenceBase_eq_flatDeformationObstruction, AlgebraicGeometry.RingedSpaceThickening.FlatShortExactThickeningDiagram.boundary_difference_trivialLift_pulledLift_eq_flatDeformationObstruction
statement: formalized
proof: formalized
---

# 91.6 Application to flat modules on flat thickenings of ringed spaces

Section 91.6 of the Stacks Project, [Tag 08VQ](https://stacks.math.columbia.edu/tag/08VQ). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08VR, a lemma

[Tag 08VR](https://stacks.math.columbia.edu/tag/08VR) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.FlatModuleDeformation.nonempty_flatLift_iff_flatDeformationObstruction_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/FlatModuleDeformation.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RingedSpaceThickening/FlatModuleDeformation.lean#L257). The attribute's comment: “clause (1)”.

> **Stacks Project, Tag 08VR**, clause (1). Let `(f, f')` be a strict morphism of first order
> thickenings of ringed spaces with `f'` flat, and let `ℱ` be an `𝒪_X`-module flat over `S`. There
> is an `𝒪_{X'}`-module `ℱ'` flat over `S'` with `i^* ℱ' ≅ ℱ` if and only if the class
> `o(ℱ, f^* 𝒥 ⊗_{𝒪_X} ℱ, 1)` of **Stacks 08L8** vanishes.
>
> This is **Stacks 08LN** read through the identification `ℐ = f^* 𝒥`
> (`isIso_baseToSourceIdeal_of_isFlat`), which makes its first condition automatic.

```lean
theorem nonempty_flatLift_iff_flatDeformationObstruction_eq_zero
    (hi : IsFirstOrderThickening D.i) (ht : IsFirstOrderThickening D.t) (hs : D.IsStrict)
    (hf' : AlgebraicGeometry.IsFlat D.f') (F : SheafOfModules.{u} (structureSheafRing D.X))
    (hF : AlgebraicGeometry.IsFlatOver D.f F) :
    Nonempty (FlatLift D F) ↔
      flatDeformationObstruction D hi (isIso_baseToSourceIdeal_of_isFlat D hs hf') F = 0
```

**`AlgebraicGeometry.RingedSpaceThickening.FlatModuleDeformation.flatLiftClassDifferenceBase_isPrincipalHomogeneous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/FlatModuleDeformation.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RingedSpaceThickening/FlatModuleDeformation.lean#L307). The attribute's comment: “clause (2)”.

> **Stacks Project, Tag 08VR**, clause (2). Let `(f, f')` be a strict morphism of first order
> thickenings of ringed spaces with `f'` flat, and let `ℱ` be an `𝒪_X`-module flat over `S`. The
> isomorphism classes of lifts of `ℱ` to `𝒪_{X'}`-modules flat over `S'` form a principal
> homogeneous space under `Ext¹_{𝒪_X}(ℱ, f^* 𝒥 ⊗_{𝒪_X} ℱ)`: the difference
> `flatLiftClassDifferenceBase` is additive, and for every class `b` the map `a ↦ d(a, b)` is a
> bijection onto `Ext¹_{𝒪_X}(ℱ, f^* 𝒥 ⊗_{𝒪_X} ℱ)`. When no lift exists both conditions hold
> vacuously.
>
> This is **Stacks 08LM** read through the identification `ℐ = f^* 𝒥`.

```lean
theorem flatLiftClassDifferenceBase_isPrincipalHomogeneous (hi : IsFirstOrderThickening D.i)
    (ht : IsFirstOrderThickening D.t) (hs : D.IsStrict) (hf' : AlgebraicGeometry.IsFlat D.f')
    {F : SheafOfModules.{u} (structureSheafRing D.X)} (hF : AlgebraicGeometry.IsFlatOver D.f F) :
    (∀ a b c : FlatLiftClass D F,
      flatLiftClassDifferenceBase D hi hs (isIso_baseToSourceIdeal_of_isFlat D hs hf') F a b +
          flatLiftClassDifferenceBase D hi hs (isIso_baseToSourceIdeal_of_isFlat D hs hf') F b c =
        flatLiftClassDifferenceBase D hi hs (isIso_baseToSourceIdeal_of_isFlat D hs hf') F a c) ∧
      ∀ b : FlatLiftClass D F, Function.Bijective fun a : FlatLiftClass D F =>
        flatLiftClassDifferenceBase D hi hs (isIso_baseToSourceIdeal_of_isFlat D hs hf') F a b
```

**`AlgebraicGeometry.RingedSpaceThickening.FlatModuleDeformation.exists_identityLiftAut_equiv_ext_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/FlatModuleDeformation.lean, line 460](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RingedSpaceThickening/FlatModuleDeformation.lean#L460). The attribute's comment: “clause (3)”.

> **Stacks Project, Tag 08VR**, clause (3). Given a lift `ℱ'` of `ℱ` to an `𝒪_{X'}`-module
> flat over `S'`, the set of automorphisms of `ℱ'` which pull back to the identity of `ℱ` is
> canonically isomorphic to `Ext⁰_{𝒪_X}(ℱ, f^* 𝒥 ⊗_{𝒪_X} ℱ)`: the class `ξ` corresponds to the
> automorphism `1 + ε_ξ`, where `ε_ξ` is `ξ ∈ Hom_{𝒪_X}(ℱ, f^* 𝒥 ⊗_{𝒪_X} ℱ)` read through
> **Stacks 08LJ** as an endomorphism `ℱ' ⟶ ℐℱ' ⟶ ℱ'`.

```lean
theorem exists_identityLiftAut_equiv_ext_zero [CategoryTheory.HasExt.{w}
      (SheafOfModules.{u} (structureSheafRing D.X))]
    (hi : IsFirstOrderThickening D.i) (hs : D.IsStrict)
    {F : SheafOfModules.{u} (structureSheafRing D.X)} (A : FlatLift D F) :
    ∃ e : { φ : A.module' ≅ A.module' //
          (modulePullback D.i).map φ.hom = 𝟙 ((modulePullback D.i).obj A.module') } ≃
        CategoryTheory.Abelian.Ext.{w} F (baseIdealTensor D F) 0,
      ∀ φ, φ.1.hom = 𝟙 A.module' +
        liftInfinitesimalEndo D hi hs A (CategoryTheory.Abelian.Ext.homEquiv₀ (e φ))
```

## Tag 08VS, a situation

[Tag 08VS](https://stacks.math.columbia.edu/tag/08VS) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.FlatShortExactThickeningDiagram`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/FlatThickeningSituation.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RingedSpaceThickening/FlatThickeningSituation.lean#L46). The attribute's comment: “the situation”.

> Two short exact sequences of first order thickenings, one over the other, with strict and flat
> vertical arrows, together with a module on the middle upper space which is flat over the middle
> lower space.

```lean
structure FlatShortExactThickeningDiagram
```

## Tag 08VT, a lemma

[Tag 08VT](https://stacks.math.columbia.edu/tag/08VT) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.boundary_flatLiftClassDifferenceBase_eq_flatDeformationObstruction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/FlatThickeningBoundary.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RingedSpaceThickening/FlatThickeningBoundary.lean#L250). The attribute's comment: “the boundary of the difference of `π^* ℱ` and `h^* ℱ'₂` is the obstruction to lifting `ℱ` to an `𝒪'₃`-module flat over `S'₃`, difference in the order `(h^* ℱ'₂, π^* ℱ)`; inputs of the source are hypotheses -- the 08VQ identifications `ℐᵢ = f^* 𝒥ᵢ`, as 08VR already carries them, the short exactness of the tensored ideal sequence, and 08LF's own `hrestrict` -- each named in the Scope section of the module docstring”.

> In the situation of **Stacks 08VS** the two `𝒪'₁`-modules
> `π^* ℱ` and `h^* ℱ'₂` are flat over `S'₁` and restrict to `ℱ` on `X`, so **Stacks 08VR**
> clause (2) attaches to them a difference `θ ∈ Ext¹_{𝒪_X}(ℱ, f^* 𝒥₁ ⊗_{𝒪_X} ℱ)`. The boundary of
> `θ` along `0 ⟶ f^* 𝒥₃ ⊗ ℱ ⟶ f^* 𝒥₂ ⊗ ℱ ⟶ f^* 𝒥₁ ⊗ ℱ ⟶ 0` is the obstruction of **Stacks 08VR**
> clause (1) to lifting `ℱ` to an `𝒪'₃`-module flat over `S'₃`.
>
> The difference is taken in the order `(h^* ℱ'₂, π^* ℱ)`; the other order negates both it and its
> boundary. The hypotheses carrying inputs of the source are described in the Scope section of the
> module docstring.

```lean
theorem boundary_flatLiftClassDifferenceBase_eq_flatDeformationObstruction
    (D : FlatShortExactThickeningDiagram.{u})
    [CategoryTheory.HasExt.{w} (SheafOfModules.{u} (structureSheafRing D.upper.X))]
    [CategoryTheory.HasExt.{w} (SheafOfModules.{u} (structureSheafRing D.upper.X₁))]
    [HasDerivedCategory.{w'} (SheafOfModules.{u} (structureSheafRing D.upper.X))]
    (hI₁ : IsIso D.morphism₁.baseToSourceIdeal)
    (hI₂ : IsIso D.morphism₂.baseToSourceIdeal)
    (hI₃ : IsIso D.morphism₃.baseToSourceIdeal)
    (k₃₂ : baseIdealTensor D.morphism₃ D.restriction ⟶
      baseIdealTensor D.morphism₂ D.restriction)
    (k₂₁ : baseIdealTensor D.morphism₂ D.restriction ⟶
      baseIdealTensor D.morphism₁ D.restriction)
    (hk : k₃₂ ≫ k₂₁ = 0) (hK : (ShortComplex.mk k₃₂ k₂₁ hk).ShortExact)
    (hk₃₂ : (baseIdealTensorIso D.morphism₃ hI₃ D.restriction).inv ≫ k₃₂ =
      D.idealTensorTransition₃₂ ≫ (baseIdealTensorIso D.morphism₂ hI₂ D.restriction).inv)
    (hk₂₁ : (baseIdealTensorIso D.morphism₂ hI₂ D.restriction).inv ≫ k₂₁ =
      D.idealTensorTransition₂₁ ≫ (baseIdealTensorIso D.morphism₁ hI₁ D.restriction).inv)
    (Aπ Bh : FlatLift D.morphism₁ D.restriction)
    (hAπ : underlyingExtensionClass D.upper.i₁ D.trivialization D.upper.firstOrder₁.1.1
      D.restriction (idealTensor D.morphism₁ D.restriction)
      (Aπ.kernelExtension D.upper.firstOrder₁ D.isStrict₁) = 0)
    (w : PushedExtension D.upper.i₁ D.upper.i₂ D.upper.f₁₂ D.upper.comm₁₂ D.restriction
      (idealTensor D.morphism₁ D.restriction) (idealTensor D.morphism₂ D.restriction)
      D.idealTensorTransition₂₁
      (D.liftOfModule₂.kernelExtension D.upper.firstOrder₂ D.isStrict₂)
      (Bh.kernelExtension D.upper.firstOrder₁ D.isStrict₁))
    (hw : IsPushout (D.liftOfModule₂.kernelExtension D.upper.firstOrder₂ D.isStrict₂).f
      ((modulePushforward D.upper.i₂).map D.idealTensorTransition₂₁ ≫
        (thickeningPushforwardComp D.upper.i₁ D.upper.i₂ D.upper.f₁₂ D.upper.comm₁₂).inv.app
          (idealTensor D.morphism₁ D.restriction))
      w.hom ((modulePushforward D.upper.f₁₂).map
        (Bh.kernelExtension D.upper.firstOrder₁ D.isStrict₁).f))
    (hrestrict : (firstOrderExtensionAction D.upper.i₃ D.restriction
        (idealTensor D.morphism₂ D.restriction) D.upper.firstOrder₃
        (sequenceRestrictedExtension D.upper D.restriction
          (idealTensor D.morphism₂ D.restriction)
          (D.liftOfModule₂.kernelExtension D.upper.firstOrder₂ D.isStrict₂))).val =
      D.idealTensorTransition₃₂) :
    (flatLiftClassDifferenceBase D.morphism₁ D.upper.firstOrder₁ D.isStrict₁ hI₁ D.restriction
          (Quotient.mk (flatLiftSetoid D.morphism₁ D.restriction) Bh)
          (Quotient.mk (flatLiftSetoid D.morphism₁ D.restriction) Aπ)).comp
        hK.extClass (by decide) =
      flatDeformationObstruction D.morphism₃ D.upper.firstOrder₃ hI₃ D.restriction
```

**`AlgebraicGeometry.RingedSpaceThickening.FlatShortExactThickeningDiagram.boundary_difference_trivialLift_pulledLift_eq_flatDeformationObstruction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/FlatThickeningBoundaryUnconditional.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RingedSpaceThickening/FlatThickeningBoundaryUnconditional.lean#L100).

> In Situation **Stacks 08VS** — a commutative diagram of short exact sequences of first order
> thickenings `X'₁ ⟶ X'₂ ⟶ X'₃` of `X` over `S'₁ ⟶ S'₂ ⟶ S'₃` of `S`, with every
> `(f, f'ᵢ)` strict and every `f'ᵢ` flat, and an `𝒪'₂`-module `ℱ'₂` flat over `S'₂` with
> `ℱ = ℱ'₂|_X` — let `π : X'₁ ⟶ X` be the canonical splitting of **Stacks 08LE**.
> Then `π^* ℱ` and `h^* ℱ'₂` are `𝒪'₁`-modules flat over `S'₁` (the first two conjuncts); they
> restrict to `ℱ` on `X` through `i₁^* π^* ℱ ≅ (i₁ ≫ π)^* ℱ = ℱ` and
> `i₁^* h^* ℱ'₂ ≅ (i₁ ≫ h)^* ℱ'₂ = ℱ`, which makes them the flat lifts `trivialLift` and
> `pulledLift`. Their difference `θ ∈ Ext¹_{𝒪_X}(ℱ, f^* 𝒥₁ ⊗_{𝒪_X} ℱ)`, the difference of
> **Stacks 08VR** (2) of the two isomorphism classes, has for boundary along
> `0 ⟶ f^* 𝒥₃ ⊗ ℱ ⟶ f^* 𝒥₂ ⊗ ℱ ⟶ f^* 𝒥₁ ⊗ ℱ ⟶ 0` — the sequence induced by the lower row, short
> exact by `baseTransition_shortExact` — the obstruction of **Stacks 08VR** (1) to lifting `ℱ` to an
> `𝒪'₃`-module flat over `S'₃`.
>
> The difference is taken in the order `(h^* ℱ'₂, π^* ℱ)`.

```lean
theorem boundary_difference_trivialLift_pulledLift_eq_flatDeformationObstruction
    [CategoryTheory.HasExt.{w} (SheafOfModules.{u} (structureSheafRing D.upper.X))]
    [CategoryTheory.HasExt.{w} (SheafOfModules.{u} (structureSheafRing D.upper.X₁))]
    [HasDerivedCategory.{w'} (SheafOfModules.{u} (structureSheafRing D.upper.X))] :
    AlgebraicGeometry.IsFlatOver D.f₁
        ((modulePullback D.trivialization.retraction).obj D.restriction) ∧
      AlgebraicGeometry.IsFlatOver D.f₁ ((modulePullback D.upper.f₁₂).obj D.module₂) ∧
      (flatLiftClassDifferenceBase D.morphism₁ D.upper.firstOrder₁ D.isStrict₁
          D.isIso_baseToSourceIdeal₁ D.restriction
          (Quotient.mk (flatLiftSetoid D.morphism₁ D.restriction) D.pulledLift)
          (Quotient.mk (flatLiftSetoid D.morphism₁ D.restriction) D.trivialLift)).comp
          D.baseTransition_shortExact.extClass (by decide) =
        flatDeformationObstruction D.morphism₃ D.upper.firstOrder₃ D.isIso_baseToSourceIdeal₃
          D.restriction
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 91.6, Tag 08VQ](https://stacks.math.columbia.edu/tag/08VQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
