---
declaration: section
origin: cited
lean: AlgebraicGeometry.CoherentModuleFunctors.FilteredColimitExtension.preservesCoproducts, AlgebraicGeometry.CoherentModuleFunctors.FilteredColimitExtension.preservesFiniteLimits, AlgebraicGeometry.CoherentModuleFunctors.FilteredColimitExtension.preservesFiniteColimits, AlgebraicGeometry.CoherentModuleFunctors.FilteredColimitExtension.exactFunctor, AlgebraicGeometry.CoherentModuleFunctors.filteredColimitExtension, AlgebraicGeometry.CoherentModuleFunctors.FilteredColimitExtension.existsUnique_iso, AlgebraicGeometry.CoherentModuleFunctors.exists_iso_pullbackTensor, AlgebraicGeometry.CoherentModuleFunctors.exists_iso_pullbackTensor_over_base
statement: formalized
proof: formalized
---

# 56.7 Functors between categories of coherent modules

Section 56.7 of the Stacks Project, [Tag 0FZK](https://stacks.math.columbia.edu/tag/0FZK). 8 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FZL, a lemma

[Tag 0FZL](https://stacks.math.columbia.edu/tag/0FZL) in the Stacks Project.

**`AlgebraicGeometry.CoherentModuleFunctors.FilteredColimitExtension.preservesCoproducts`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/DirectSums.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/DirectSums.lean#L269). The attribute's comment: “direct\_sums”.

> **Stacks Project, Tag 0FZL.** An extension of an additive functor on coherent modules
> commutes with arbitrary direct sums of quasi-coherent modules.

```lean
lemma FilteredColimitExtension.preservesCoproducts (E : FilteredColimitExtension X Y F)
    (J : Type u) : PreservesColimitsOfShape (Discrete J) E.functor
```

**`AlgebraicGeometry.CoherentModuleFunctors.FilteredColimitExtension.preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/Exactness.lean, line 554](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/Exactness.lean#L554). The attribute's comment: “left\_exactness”.

> **Stacks Project, Tag 0FZL.** The extension of a left exact functor on the coherent modules
> of a Noetherian scheme is left exact.

```lean
theorem FilteredColimitExtension.preservesFiniteLimits {X Y : Scheme.{u}}
    [IsNoetherian X] [IsNoetherian Y]
    {F : CoherentModules X.ringCatSheaf ⥤ CoherentModules Y.ringCatSheaf}
    (E : FilteredColimitExtension X Y F) [PreservesFiniteLimits F] :
    PreservesFiniteLimits E.functor
```

**`AlgebraicGeometry.CoherentModuleFunctors.FilteredColimitExtension.preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/Exactness.lean, line 567](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/Exactness.lean#L567). The attribute's comment: “right\_exactness”.

> **Stacks Project, Tag 0FZL.** The extension of a right exact functor on the coherent modules
> of a Noetherian scheme is right exact.

```lean
theorem FilteredColimitExtension.preservesFiniteColimits {X Y : Scheme.{u}}
    [IsNoetherian X] [IsNoetherian Y]
    {F : CoherentModules X.ringCatSheaf ⥤ CoherentModules Y.ringCatSheaf}
    (E : FilteredColimitExtension X Y F) [PreservesFiniteColimits F] :
    PreservesFiniteColimits E.functor
```

**`AlgebraicGeometry.CoherentModuleFunctors.FilteredColimitExtension.exactFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/Exactness.lean, line 580](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/Exactness.lean#L580). The attribute's comment: “exactness”.

> **Stacks Project, Tag 0FZL.** The extension of an exact functor on the coherent modules of a
> Noetherian scheme is exact.

```lean
theorem FilteredColimitExtension.exactFunctor {X Y : Scheme.{u}}
    [IsNoetherian X] [IsNoetherian Y]
    {F : CoherentModules X.ringCatSheaf ⥤ CoherentModules Y.ringCatSheaf}
    (E : FilteredColimitExtension X Y F)
    (hF : exactFunctor (CoherentModules X.ringCatSheaf) (CoherentModules Y.ringCatSheaf) F) :
    exactFunctor (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory
      (SheafOfModules.isQuasicoherent Y.ringCatSheaf).FullSubcategory E.functor
```

**`AlgebraicGeometry.CoherentModuleFunctors.filteredColimitExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/Extension.lean, line 389](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/Extension.lean#L389). The attribute's comment: “extension”.

> **Stacks Project, Tag 0FZL.** A functor from the coherent modules on a Noetherian scheme to
> the coherent modules on a scheme extends to a functor on quasi-coherent modules which commutes
> with filtered colimits.

```lean
noncomputable def filteredColimitExtension (X Y : Scheme.{u}) [IsNoetherian X]
    (F : CoherentModules X.ringCatSheaf ⥤
      CoherentModules Y.ringCatSheaf) :
    FilteredColimitExtension X Y F
```

**`AlgebraicGeometry.CoherentModuleFunctors.FilteredColimitExtension.existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/Extension.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/Extension.lean#L416). The attribute's comment: “extension”.

> **Stacks Project, Tag 0FZL.** Two filtered-colimit-preserving extensions are related by a
> unique natural isomorphism compatible with their specified identifications on the coherent
> modules.

```lean
theorem FilteredColimitExtension.existsUnique_iso {X Y : Scheme.{u}} [IsNoetherian X]
    {F : CoherentModules X.ringCatSheaf ⥤
      CoherentModules Y.ringCatSheaf}
    (E₁ E₂ : FilteredColimitExtension X Y F) :
    ∃! e : E₁.functor ≅ E₂.functor,
      Functor.whiskerLeft (coherentToQuasicoherent X) e.hom =
        (E₁.iso.trans E₂.iso.symm).hom
```

## Tag 0GPK, a lemma

[Tag 0GPK](https://stacks.math.columbia.edu/tag/0GPK) in the Stacks Project.

**`AlgebraicGeometry.CoherentModuleFunctors.exists_iso_pullbackTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/EquivalenceReconstruction.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/EquivalenceReconstruction.lean#L193).

> **Stacks Project, Tag 0GPK.** Let `X` and `Y` be Noetherian schemes and let
> `F : Coh(𝒪_X) ⥤ Coh(𝒪_Y)` be an equivalence of categories. Then there are an isomorphism of
> schemes `f : Y ⟶ X` and an invertible `𝒪_Y`-module `ℒ` with `F(𝓕) = f^*𝓕 ⊗ ℒ`, naturally in the
> coherent `𝒪_X`-module `𝓕`. The corresponding description of an equivalence of the categories of
> quasi-coherent modules is Tag 0GPJ, available here as
> `exists_iso_pullbackTensor_quasicoherent`; the coherent case follows from it by extending `F` to
> the quasi-coherent modules. Nothing is hypothesised.

```lean
theorem exists_iso_pullbackTensor {X Y : Scheme.{u}} [IsNoetherian X] [IsNoetherian Y]
    (F : CoherentModules X.ringCatSheaf ⥤ CoherentModules Y.ringCatSheaf) [F.IsEquivalence] :
    ∃ (f : Y ≅ X) (L : Y.Modules),
      Stacks.SheafOfModules.IsInvertible Y.presheaf Y.ringCatSheaf.2 L ∧
      Nonempty (coherentToModules X ⋙ pullbackTensor f.hom L ≅ F ⋙ coherentToModules Y)
```

## Tag 0GPL, a remark

[Tag 0GPL](https://stacks.math.columbia.edu/tag/0GPL) in the Stacks Project.

**`AlgebraicGeometry.CoherentModuleFunctors.exists_iso_pullbackTensor_over_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/EquivalenceOverBase.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/EquivalenceOverBase.lean#L281).

> **Stacks Project, Tag 0GPL.** Let `R` be a commutative ring, let `X` and `Y` be Noetherian
> schemes over `R`, and let `F : Coh(𝒪_X) ⥤ Coh(𝒪_Y)` be an equivalence of categories which is
> linear over `R`. Then the isomorphism of schemes `f : Y ≅ X` and the invertible `𝒪_Y`-module
> `ℒ` of Tag 0GPK with `F(𝓕) = f^*𝓕 ⊗ ℒ` may be chosen with `f` a morphism of schemes over `R`,
> that is with `f ≫ (X → Spec R) = (Y → Spec R)`.
>
> Nothing is hypothesised. Tag 0GPK is unconditional, so the content here is only the refinement
> over `R`: `R`-linearity of `F` forces `f` to be a morphism over `R`.

```lean
theorem exists_iso_pullbackTensor_over_base (X Y : Over (Spec (.of R)))
    [IsNoetherian X.left] [IsNoetherian Y.left]
    (F : CoherentModules X.left.ringCatSheaf ⥤ CoherentModules Y.left.ringCatSheaf)
    [F.IsEquivalence] :
    letI : Linear R (SheafOfModules.{u} X.left.ringCatSheaf) := modulesLinear R X
    letI : Linear R (SheafOfModules.{u} Y.left.ringCatSheaf) := modulesLinear R Y
    F.Linear R →
      ∃ (f : Y.left ≅ X.left) (L : Y.left.Modules),
        Stacks.SheafOfModules.IsInvertible Y.left.presheaf Y.left.ringCatSheaf.2 L ∧
        Nonempty (coherentToModules X.left ⋙ pullbackTensor f.hom L ≅
          F ⋙ coherentToModules Y.left) ∧
        f.hom ≫ X.hom = Y.hom
```

## Tag 0FZM, a lemma

[Tag 0FZM](https://stacks.math.columbia.edu/tag/0FZM) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CoherentModuleFunctors.isFinite_of_isCoherent_pushforward_of_isZero_higherDirectImages`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/FinitenessCriterion.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/FinitenessCriterion.lean#L369).

> **A finiteness criterion.** Let `f : V ⟶ X` be a quasi-finite separated morphism of
> Noetherian schemes. If there is a coherent `𝒪_V`-module `𝒦` whose support is all of `V` such
> that `f_*𝒦` is coherent and `R^q f_*𝒦 = 0` for every `q > 0`, then `f` is finite.
>
> Quasi-finiteness is [Stacks, Tag 02NG] — locally quasi-finite and of finite type — which in
> Mathlib's vocabulary is `AlgebraicGeometry.LocallyQuasiFinite`,
> `AlgebraicGeometry.LocallyOfFiniteType` and `AlgebraicGeometry.QuasiCompact` together. The
> existential over `𝒦` of the source is taken as an explicit hypothesis.
>
> Finiteness is Zariski-local on the target, and every hypothesis restricts to an affine open `U`
> of `X`: coherence and the support condition because they are local, and the vanishing of the
> higher direct images by the comparison `R^q(f|_U)_*(𝒦|_{f^{-1}U}) ≅ (R^q f_*𝒦)|_U` of
> [Stacks, Tag 01E5]. Over an affine target the statement is
> `isFinite_of_isAffine_target`.

```lean
public theorem isFinite_of_isCoherent_pushforward_of_isZero_higherDirectImages
    {V X : Scheme.{u}} (f : V ⟶ X) [IsNoetherian V] [IsNoetherian X]
    [LocallyOfFiniteType f] [LocallyQuasiFinite f] [QuasiCompact f] [IsSeparated f]
    (K : V.Modules) [K.IsCoherent] (hsupp : SheafOfModules.supp K = Set.univ)
    (hpush : ((Scheme.Modules.pushforward f).obj K).IsCoherent)
    (hvanish : ∀ q : ℤ, 0 < q →
      IsZero (((Scheme.Modules.pushforward f).rightDerivedPlus q).obj K)) :
    IsFinite f
```

## Tag 0FZN, a lemma

[Tag 0FZN](https://stacks.math.columbia.edu/tag/0FZN) in the Stacks Project.

**`AlgebraicGeometry.CoherentKernels.isEquivalence_coherentIntegralTransformFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentKernels/Equivalence.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentKernels/Equivalence.lean#L216). The attribute's comment: “sending a coherent kernel flat over X with support finite over Y to the restriction to Coh of its integral transform is an equivalence onto the k-linear exact functors Coh(O\_X) to Coh(O\_Y)”.

> **Stacks Project, Tag 0FZN.** Let `k` be a field and let `X` and `Y` be schemes of finite
> type over `k` with `X` separated. Sending a coherent `𝒪_{X ×_k Y}`-module `𝒦`, flat over `X` and
> with support finite over `Y`, to the restriction to `Coh(𝒪_X)` of its integral transform
> `𝓕 ↦ pr_{2,*}(pr_1^*𝓕 ⊗ 𝒦)` is an equivalence of categories onto the `k`-linear exact functors
> `Coh(𝒪_X) ⥤ Coh(𝒪_Y)`.
>
> Finite type over `k` is `LocallyOfFiniteType` together with `QuasiCompact`; `X ×_k Y` is the
> fibre product over `Spec k`. The functor is `coherentIntegralTransformFunctor`, whose value at
> `𝒦` is by definition the restriction of `quasicoherentIntegralTransform k X Y 𝒦`
> (`coherentIntegralTransformFunctor_obj_obj_comp`), the pullback--tensor--pushforward formula
> `integralTransformFormula` after forgetting quasi-coherence.

```lean
theorem isEquivalence_coherentIntegralTransformFunctor :
    (coherentIntegralTransformFunctor k X Y).IsEquivalence
```

## Tag 0FZP, a lemma

[Tag 0FZP](https://stacks.math.columbia.edu/tag/0FZP) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.exists_section_iso_pushforward_of_invertible_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/InvertiblePushforwardSection.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/InvertiblePushforwardSection.lean#L373).

> Let `f : X ⟶ Y` be a separated morphism of finite type and let `F` be a quasi-coherent
> `𝒪_X`-module of finite type whose scheme-theoretic support is finite over `Y`. If the direct
> image `f_* F` is invertible, then `f` admits a section `s`, and `F` is the direct image along `s`
> of `f_* F`.

```lean
public theorem exists_section_iso_pushforward_of_invertible_pushforward
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    [IsFinite ((Scheme.Modules.annihilatorIdeal F).subschemeι ≫ f)]
    [AlgebraicGeometry.SheafOfModules.IsInvertible Y.presheaf Y.ringCatSheaf.property
      ((Scheme.Modules.pushforward f).obj F)] :
    ∃ s : Y ⟶ X, s ≫ f = 𝟙 Y ∧
      Nonempty (F ≅ (Scheme.Modules.pushforward s).obj
        ((Scheme.Modules.pushforward f).obj F))
```

## Tag 0FZQ, a lemma

[Tag 0FZQ](https://stacks.math.columbia.edu/tag/0FZQ) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.iso_pushforward_section_of_invertible_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/InvertiblePushforwardSection.lean, line 655](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/InvertiblePushforwardSection.lean#L655).

> Let `f : X ⟶ Y` be a separated morphism of finite type with a section `s`, and let `Y` be
> reduced. A quasi-coherent `𝒪_X`-module `F` of finite type supported on the image of `s` and with
> invertible direct image `f_* F` is the direct image along `s` of `f_* F`.

```lean
public theorem iso_pushforward_section_of_invertible_pushforward
    {X Y : Scheme.{u}} (f : X ⟶ Y) (s : Y ⟶ X)
    [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f]
    (hs : s ≫ f = 𝟙 Y) [IsReduced Y]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (hsupp : SheafOfModules.supp F ⊆ Set.range s.base)
    [AlgebraicGeometry.SheafOfModules.IsInvertible Y.presheaf Y.ringCatSheaf.property
      ((Scheme.Modules.pushforward f).obj F)] :
    Nonempty (F ≅ (Scheme.Modules.pushforward s).obj
      ((Scheme.Modules.pushforward f).obj F))
```

## Tag 0FZR, a lemma

[Tag 0FZR](https://stacks.math.columbia.edu/tag/0FZR) in the Stacks Project.

**`AlgebraicGeometry.CoherentModuleFunctors.exists_iso_pullbackTensor_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/EquivalenceOverField.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/CoherentModuleFunctors/EquivalenceOverField.lean#L107). The attribute's comment: “with `X` SEPARATED and `Y` REDUCED deleted: the source uses those two hypotheses in its second proof only, and the deduction carried out here — from Tag 0GPL, with finite type over the field giving Noetherian by `isNoetherian_of_finiteType_over_field` — does not need them, so the statement is more general than the source's and implies it. Finite type is `LocallyOfFiniteType` together with `QuasiCompact`. As in Tags 0GPK and 0GPL the prescribed form of the functor is stated after the fully faithful inclusions of the coherent modules into all `𝒪`-modules, where the inverse image and the tensor product live”.

> **Stacks Project, Tag 0FZR.** Let `k` be a field, let `X` and `Y` be schemes of finite type
> over `k`, and let `F : Coh(𝒪_X) ⥤ Coh(𝒪_Y)` be an equivalence of categories which is `k`-linear.
> Then there are an isomorphism of schemes `f : Y ≅ X` over `k`, that is with
> `f ≫ (X → Spec k) = (Y → Spec k)`, and an invertible `𝒪_Y`-module `ℒ` with
> `F(𝓕) = f^*𝓕 ⊗ ℒ`, naturally in the coherent `𝒪_X`-module `𝓕`.
>
> Finite type is `LocallyOfFiniteType X.hom` together with `QuasiCompact X.hom`; this makes `X`
> and `Y` Noetherian by `isNoetherian_of_finiteType_over_field`, which is what Tag 0GPL needs, and
> `k`-linearity is what makes its `f` a morphism over `k`.
>
> Nothing is hypothesised: Tag 0GPL is unconditional, so the content here is only the passage
> from Noetherian to finite type over `k`.
>
> The source states the lemma with `X` separated and `Y` reduced. Those hypotheses are used by its
> second proof only; the deduction from Tag 0GPK and Tag 0GPL carried out here does not need them,
> so they are absent and the statement is correspondingly more general.

```lean
theorem exists_iso_pullbackTensor_over_field (k : Type u) [Field k]
    (X Y : Over (Spec (.of k)))
    [LocallyOfFiniteType X.hom] [QuasiCompact X.hom]
    [LocallyOfFiniteType Y.hom] [QuasiCompact Y.hom]
    (F : CoherentModules X.left.ringCatSheaf ⥤ CoherentModules Y.left.ringCatSheaf)
    [F.IsEquivalence] :
    letI : Linear k (SheafOfModules.{u} X.left.ringCatSheaf) := modulesLinear k X
    letI : Linear k (SheafOfModules.{u} Y.left.ringCatSheaf) := modulesLinear k Y
    F.Linear k →
      ∃ (f : Y.left ≅ X.left) (L : Y.left.Modules),
        Stacks.SheafOfModules.IsInvertible Y.left.presheaf Y.left.ringCatSheaf.2 L ∧
        Nonempty (coherentToModules X.left ⋙ pullbackTensor f.hom L ≅
          F ⋙ coherentToModules Y.left) ∧
        f.hom ≫ X.hom = Y.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 56.7, Tag 0FZK](https://stacks.math.columbia.edu/tag/0FZK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
