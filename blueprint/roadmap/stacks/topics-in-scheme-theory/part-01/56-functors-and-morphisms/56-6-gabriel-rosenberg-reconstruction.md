---
declaration: section
origin: cited
lean: AlgebraicGeometry.isFinitelyPresentable_iff_isFinitePresentation, AlgebraicGeometry.exists_nonzero_hom_of_supp_subset, AlgebraicGeometry.supportContained_eq_serreCoproductClosure, AlgebraicGeometry.quasicoherentSupportedOn_isSerreClass, AlgebraicGeometry.quasicoherentRestriction_isLocalization, AlgebraicGeometry.quasicoherentSupportedQuotientEquivalence, AlgebraicGeometry.quasicoherentSupportedQuotientEquivalenceFunctorIso, AlgebraicGeometry.AffineOfModuleCategory.isAffine_of_quasicoherentModules_equivalent_moduleCat
statement: formalized
proof: formalized
---

# 56.6 Gabriel-Rosenberg reconstruction

Section 56.6 of the Stacks Project, [Tag 0GPD](https://stacks.math.columbia.edu/tag/0GPD). 6 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GPE, a lemma

[Tag 0GPE](https://stacks.math.columbia.edu/tag/0GPE) in the Stacks Project.

**`AlgebraicGeometry.isFinitelyPresentable_iff_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/CompactObjects.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/CompactObjects.lean#L152).

> **Stacks Project, Tag 0GPE.**  A quasi-coherent module on a quasi-compact and quasi-separated
> scheme is a categorically compact object of the category of quasi-coherent modules if and only if
> it is of finite presentation.

```lean
theorem isFinitelyPresentable_iff_isFinitePresentation
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X]
    (F : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory) :
    IsFinitelyPresentable.{u} F ↔ F.obj.IsFinitePresentation
```

## Tag 0GPF, a lemma

[Tag 0GPF](https://stacks.math.columbia.edu/tag/0GPF) in the Stacks Project.

**`AlgebraicGeometry.exists_nonzero_hom_of_supp_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedNonzeroHom.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedNonzeroHom.lean#L358). References: SGA 2 VII (1.3), “affine case”.

> **Stacks Project, Tag 0GPF.** If the support of a nonzero quasi-coherent module on an
> affine scheme is contained in that of a finitely presented module, then there is a nonzero
> morphism from the latter to the former.

```lean
theorem exists_nonzero_hom_of_supp_subset
    (X : Scheme.{u}) [IsAffine X]
    (F E : X.Modules) [F.IsFinitePresentation] [E.IsQuasicoherent]
    (hE : ¬ IsZero E)
    (hsupp : SheafOfModules.supp E ⊆ SheafOfModules.supp F) :
    ∃ f : F ⟶ E, f ≠ 0
```

## Tag 0GPG, a lemma

[Tag 0GPG](https://stacks.math.columbia.edu/tag/0GPG) in the Stacks Project.

**`AlgebraicGeometry.supportContained_eq_serreCoproductClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreSubcategory.lean, line 780](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreSubcategory.lean#L780).

> **Stacks Project, Tag 0GPG.** On a quasi-compact and quasi-separated scheme, the
> quasi-coherent modules supported on the support of a finitely presented module are exactly
> the smallest Serre subcategory containing it and closed under arbitrary direct sums.

```lean
theorem supportContained_eq_serreCoproductClosure (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (F : X.Modules)
    [SheafOfModules.IsFinitePresentation (R := X.ringCatSheaf) F] :
    (fun E : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory ↦
        IsSupportedOn E.obj F) =
      serreCoproductClosure
          (C := (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory)
        ⟨F, by
        constructor
        exact ⟨(SheafOfModules.IsFinitePresentation.exists_quasicoherentData F).choose⟩⟩
```

## Tag 0GPH, a lemma

[Tag 0GPH](https://stacks.math.columbia.edu/tag/0GPH) in the Stacks Project.

**`AlgebraicGeometry.quasicoherentSupportedOn_isSerreClass`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean#L229). The attribute's comment: “the full subcategory of modules supported on `Z` is a Serre subcategory”.

> Quasi-coherent modules supported on a fixed subset of a scheme form a Serre subcategory of
> the category of all quasi-coherent modules.

```lean
public instance quasicoherentSupportedOn_isSerreClass (X : Scheme.{u}) (Z : Set X) :
    (quasicoherentSupportedOn X Z).IsSerreClass
```

**`AlgebraicGeometry.quasicoherentRestriction_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean#L307). The attribute's comment: “restriction is the localization at the supported Serre subcategory”.

> **[Stacks, Tag 0GPH].** Let `X` be a quasi-compact and quasi-separated scheme and let `U` be
> a quasi-compact open whose complement is the closed subset `Z`.  Restriction along `U ↪ X`
> exhibits `QCoh(𝒪_U)` as the localization of `QCoh(𝒪_X)` at the morphisms whose kernel and
> cokernel are supported on `Z`, that is, as the Serre quotient of `QCoh(𝒪_X)` by the full
> subcategory of quasi-coherent modules supported on `Z`.

```lean
public theorem quasicoherentRestriction_isLocalization (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (Z : Set X) (U : X.Opens) (hUZ : (U : Set X) = Zᶜ)
    (hU : IsCompact (U : Set X)) :
    (quasicoherentRestriction U.ι).IsLocalization
      (quasicoherentSupportedOn X Z).isoModSerre
```

**`AlgebraicGeometry.quasicoherentSupportedQuotientEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean#L378). The attribute's comment: “the induced equivalence from the quotient category”.

> **[Stacks, Tag 0GPH].** The equivalence `QCoh(𝒪_X)/𝒜 ≌ QCoh(𝒪_U)` induced by restriction,
> where `𝒜` is the Serre subcategory of quasi-coherent modules supported on the closed complement
> `Z` of the quasi-compact open `U`, and `QCoh(𝒪_X)/𝒜` is the Serre quotient, that is the
> localization of `QCoh(𝒪_X)` at the morphisms that are isomorphisms modulo `𝒜`.

```lean
public noncomputable def quasicoherentSupportedQuotientEquivalence (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X] (Z : Set X) (U : X.Opens)
    (hUZ : (U : Set X) = Zᶜ) (hU : IsCompact (U : Set X)) :
    (quasicoherentSupportedOn X Z).isoModSerre.Localization ≌
      (SheafOfModules.isQuasicoherent U.toScheme.ringCatSheaf).FullSubcategory
```

**`AlgebraicGeometry.quasicoherentSupportedQuotientEquivalenceFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean#L390). The attribute's comment: “the equivalence is induced by the restriction functor”.

> The equivalence `QCoh(𝒪_X)/𝒜 ≌ QCoh(𝒪_U)` of [Stacks, Tag 0GPH] is the one induced by the
> restriction functor: composing it with the quotient functor gives back restriction.

```lean
public noncomputable def quasicoherentSupportedQuotientEquivalenceFunctorIso (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X] (Z : Set X) (U : X.Opens)
    (hUZ : (U : Set X) = Zᶜ) (hU : IsCompact (U : Set X)) :
    (quasicoherentSupportedOn X Z).isoModSerre.Q ⋙
        (quasicoherentSupportedQuotientEquivalence X Z U hUZ hU).functor ≅
      quasicoherentRestriction U.ι
```

## Tag 0GPI, a lemma

[Tag 0GPI](https://stacks.math.columbia.edu/tag/0GPI) in the Stacks Project.

**`AlgebraicGeometry.AffineOfModuleCategory.isAffine_of_quasicoherentModules_equivalent_moduleCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/AffineOfModuleCategory.lean, line 1141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/AffineOfModuleCategory.lean#L1141). The attribute's comment: “`[CommRing R]` reads the tag's `a ring`: the rank-one step needs `End P` commutative. For noncommutative `R` the conclusion still holds by Morita equivalence (`Mod (M₂ k) ≌ Mod k`), but that rank-one step fails outright.”.

> **Stacks Project, Tag 0GPI.** A quasi-compact and quasi-separated scheme whose category
> of quasi-coherent modules is equivalent to the category of modules over a commutative ring
> is affine.
>
> The commutativity of `R` is a reading of the tag's `a ring`. It is used through the separator
> `P`, whose endomorphism ring must be commutative for the rank of `P` to be forced to be `1`.

```lean
public theorem isAffine_of_quasicoherentModules_equivalent_moduleCat
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X]
    (R : Type v) [CommRing R]
    (e : ModuleCat.{u} R ≌
      (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory) :
    IsAffine X
```

**`AlgebraicGeometry.AffineOfModuleCategory.isAffine_of_quasicoherentModules_equivalence_moduleCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/AffineOfModuleCategory.lean, line 1164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/AffineOfModuleCategory.lean#L1164). The attribute's comment: “the hypothesis in the orientation of the source, `QCoh(𝒪_X) ≌ Mod R`; `[CommRing R]` reads the tag's `a ring`, exactly as for the mirror form `isAffine_of_quasicoherentModules_equivalent_moduleCat`”.

> **Stacks Project, Tag 0GPI**, with the equivalence written in the orientation of the source:
> a quasi-compact and quasi-separated scheme whose category of quasi-coherent modules is equivalent
> to the category of modules over a commutative ring is affine.
>
> As for the mirror form, the commutativity of `R` is a reading of the tag's `a ring`.

```lean
public theorem isAffine_of_quasicoherentModules_equivalence_moduleCat
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X]
    (R : Type v) [CommRing R]
    (e : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory ≌
      ModuleCat.{u} R) :
    IsAffine X
```

## Tag 0GPJ, a proposition

[Tag 0GPJ](https://stacks.math.columbia.edu/tag/0GPJ) in the Stacks Project.

**`AlgebraicGeometry.exists_schemeIso_invertible_of_quasicoherentEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/AffineReconstruction.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/AffineReconstruction.lean#L185). The attribute's comment: “affine case: for `X` and `Y` affine, with the tensoring by the invertible module read on `ModuleCat Γ(Y, ⊤)` through the affine comparison `AlgebraicGeometry.affineQuasicoherentModulesEquiv` rather than as the tensor product of sheaves of `𝒪_Y`-modules. This is the form in which the Tag 0GP0 argument produces the conclusion; the source's own sheaf-level form is `AlgebraicGeometry.exists_schemeIso_invertibleSheaf_of_quasicoherentEquivalence`, proved from this one in the same file. What is NOT proved here is the general quasi-compact quasi-separated case; its local form, steps 3 to 8 of the source's argument, is `AlgebraicGeometry.exists_isAffineOpen_schemeIso_invertibleSheaf_of_isFinitePresentation`, and what remains beyond that is step 2 and the gluing step 9 that the source itself omits”.

> If `X` and `Y` are affine schemes and
> `F : QCoh(𝒪_X) ⥤ QCoh(𝒪_Y)` is an equivalence, then there are an isomorphism of schemes
> `f : Y ≅ X` and an invertible `Γ(Y, ⊤)`-module `L` such that `F` is inverse image along `f`
> followed by tensoring with `L`.

```lean
theorem exists_schemeIso_invertible_of_quasicoherentEquivalence
    (F : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory ⥤
      (SheafOfModules.isQuasicoherent Y.ringCatSheaf).FullSubcategory) [F.IsEquivalence] :
    ∃ (f : Y ≅ X) (L : ModuleCat.{u} Γ(Y, ⊤)), Module.Invertible Γ(Y, ⊤) L ∧
      Nonempty (F ≅ (quasicoherentModulesEquivOfSchemeIso f).symm.functor ⋙
        affineTensorFunctor Y L)
```

**`AlgebraicGeometry.exists_schemeIso_invertibleSheaf_of_quasicoherentEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/AffineReconstruction.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/AffineReconstruction.lean#L438). The attribute's comment: “affine case: for `X` and `Y` affine. The invertible object is a sheaf of `𝒪_Y`-modules, invertible in the sense of Tag 01CS (`Stacks.SheafOfModules.IsInvertible`), and the tensoring is `- ⊗_{𝒪_Y} L`. Two deviations from the source statement. First, the general quasi-compact quasi-separated case is not proved; its local form, steps 3 to 8 of the source's argument, is `AlgebraicGeometry.exists_isAffineOpen_schemeIso_invertibleSheaf_of_isFinitePresentation`, which quotes this theorem for its affine input, and what remains beyond that is step 2 (the existence of a finitely presented module supported on the complement of a given affine open) and the gluing step 9 that the source itself omits. Second, the comparison of functors is stated after forgetting quasi-coherence, i.e. between functors into all `𝒪_Y`-modules, so that the statement does not depend on quasi-coherence being stable under inverse image and tensor product; since the inclusion of the quasi-coherent modules is fully faithful and quasi-coherence is invariant under isomorphism, nothing of the source's content is lost”.

> If `X` and `Y` are affine schemes and `F : QCoh(𝒪_X) ⥤ QCoh(𝒪_Y)` is an equivalence, then there
> are an isomorphism of schemes `f : Y ≅ X` and an invertible sheaf `L` of `𝒪_Y`-modules such
> that `F` is inverse image along `f` followed by `- ⊗_{𝒪_Y} L`.

```lean
theorem exists_schemeIso_invertibleSheaf_of_quasicoherentEquivalence
    (F : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory ⥤
      (SheafOfModules.isQuasicoherent Y.ringCatSheaf).FullSubcategory) [F.IsEquivalence] :
    ∃ (f : Y ≅ X) (L : SheafOfModules.{u} Y.ringCatSheaf),
      Stacks.SheafOfModules.IsInvertible Y.presheaf Y.ringCatSheaf.2 L ∧
        Nonempty (F ⋙ ObjectProperty.ι (SheafOfModules.isQuasicoherent Y.ringCatSheaf) ≅
          pullbackTensorFunctor f.hom L)
```

**`AlgebraicGeometry.exists_natIso_pullbackTensorFunctor_of_quasicoherentEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionGlobalComparison.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionGlobalComparison.lean#L89). The attribute's comment: “the tag IN FULL, for `X` and `Y` quasi-compact and quasi-separated: an equivalence of the categories of quasi-coherent modules gives an isomorphism of schemes `g : Y ≅ X`, an invertible `𝒪_Y`-module `M`, and a NATURAL isomorphism `e(𝓕) ≅ g^*𝓕 ⊗ M`. No cover, no affineness and no further hypothesis of any kind beyond qcqs. The scheme half is `exists_schemeIso_of_quasicoherentEquivalence` and the module half `isInvertible_map_quasicoherentUnit_of_quasicoherentEquivalence`, both already unconditional; what is new is the comparison of functors, which the Stacks source dismisses with "We omit the details". It is glued from the per-chart comparisons `chartComparisonIso` by `exists_natIso_of_chartComparison`, whose agreement hypothesis is discharged by the rigidity `natIso_eq_of_app_unit_eq_of_iso` once the comparisons are normalised at `𝒪_X`; the normalisation is `chartComparisonIso_hom_app_quasicoherentUnit` and it is automatic, because the module is `e(𝒪_X)` and the identification of its restriction with the chart's `L` is `restrictMapUnitIsoOfChartIso`, built from the same `α` and `β`. As in the affine case the comparison is stated after forgetting quasi-coherence, between functors into all `𝒪_Y`-modules”.

> **Stacks Project, Tag 0GPJ.**  Let `X` and `Y` be quasi-compact and quasi-separated schemes
> and let `e : QCoh(𝒪_X) ≌ QCoh(𝒪_Y)` be an equivalence of their categories of quasi-coherent
> modules.  Then there are an isomorphism of schemes `g : Y ≅ X` and an invertible `𝒪_Y`-module
> `M` with `e(𝓕) ≅ g^*𝓕 ⊗ M`, naturally in the quasi-coherent `𝒪_X`-module `𝓕`.
>
> The module is `e(𝒪_X)`; the isomorphism is the one glued from the reconstruction charts.  As in
> the affine case the comparison of functors is stated after forgetting quasi-coherence, between
> functors into all `𝒪_Y`-modules, which loses nothing because the inclusion of the quasi-coherent
> modules is fully faithful and quasi-coherence is invariant under isomorphism.
>
> Nothing is assumed beyond the equivalence and quasi-compactness and quasi-separatedness of the
> two schemes.

```lean
theorem exists_natIso_pullbackTensorFunctor_of_quasicoherentEquivalence {X Y : Scheme.{u}}
    [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y] [QuasiSeparatedSpace Y]
    (e : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory ≌
      (SheafOfModules.isQuasicoherent Y.ringCatSheaf).FullSubcategory) :
    ∃ (g : Y ≅ X) (M : Y.Modules),
      Stacks.SheafOfModules.IsInvertible Y.presheaf Y.ringCatSheaf.2 M ∧
        Nonempty (e.functor ⋙ ObjectProperty.ι
            (SheafOfModules.isQuasicoherent Y.ringCatSheaf) ≅
          pullbackTensorFunctor g.hom M)
```

**`AlgebraicGeometry.exists_isOpenCover_schemeIso_invertibleSheaf_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionGlobalForm.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionGlobalForm.lean#L169). The attribute's comment: “the GLOBAL form — `X` and `Y` quasi-compact and quasi-separated, no affineness and no restriction to a single open `U`. Steps 3 to 8 together with the covering assertion of step 9, which is PROVED here and no longer hypothesised: `AlgebraicGeometry.isOpenCover_of_supportedCorrespondence` shows the opens `V_U` cover `Y`, and `AlgebraicGeometry.exists_gluedQuasicoherentFunctor_restrictIso` runs the functor-level gluing with that hypothesis discharged. The module `G` of step 2 is a hypothesis here, one per member of the cover; it need not be, and `AlgebraicGeometry.exists_isOpenCover_schemeIso_invertibleSheaf_of_isAffineOpenCover` below is this statement with `G` and `hG` deleted, the module produced instead as `𝒪_X/I` for the Tag 01PH ideal. The per-chart data IS glued downstream: the `f_U` into one isomorphism `Y ≅ X` by `exists_schemeIso_of_quasicoherentEquivalence` (`ReconstructionGlobalSchemeIso.lean`) and the `L_U` into one invertible `𝒪_Y`-module by `exists_isOpenCover_invertibleModule_restrictIso_of_isAffineOpenCover` (`ReconstructionGlobalModule.lean`). The single natural isomorphism `e(F) ≅ g^*F ⊗ M` comparing `e` with that glued pair — the stated conclusion of 0GPJ, which the source dismisses with "We omit the details" — is `exists_natIso_pullbackTensorFunctor_of_quasicoherentEquivalence` (`ReconstructionGlobalComparison.lean`). As in the affine case the comparison of functors is stated after forgetting quasi-coherence, between functors into all `𝒪_V`-modules”.

> **Stacks Project, Tag 0GPJ in its global form.**  Let `X` and `Y` be quasi-compact and
> quasi-separated schemes and let `e : QCoh(𝒪_X) ≌ QCoh(𝒪_Y)` be an equivalence.  Let `U i` be an
> affine open cover of `X` and let `G i` be a finitely presented quasi-coherent `𝒪_X`-module whose
> support is the complement of `U i`.  Then there are opens `V i ⊆ Y` which **cover `Y`** and are
> each affine and quasi-compact, and for each `i` an equivalence `F_i : QCoh(𝒪_{U i}) ≌
> QCoh(𝒪_{V i})` compatible with `e` and the two restrictions, an isomorphism of schemes
> `f_i : V i ≅ U i` and an invertible sheaf `L_i` of `𝒪_{V i}`-modules such that `F_i` is inverse
> image along `f_i` followed by `- ⊗_{𝒪_{V i}} L_i`.
>
> The chart `V i` is the complement of the support of `e.functor.obj (G i)`, as in
> `AlgebraicGeometry.exists_isAffineOpen_schemeIso_invertibleSheaf_of_isFinitePresentation`; what
> is new here is that these opens cover `Y`, which is
> `AlgebraicGeometry.isOpenCover_of_supportedCorrespondence`.

```lean
theorem exists_isOpenCover_schemeIso_invertibleSheaf_of_isFinitePresentation {ι : Type u}
    (U : ι → X.Opens) (hUaff : ∀ i, IsAffineOpen (U i)) (hUcover : IsOpenCover U)
    (G : ι → (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory)
    [∀ i, SheafOfModules.IsFinitePresentation (R := X.ringCatSheaf) (G i).obj]
    (hG : ∀ i, supportSet (G i).obj = (U i : Set X)ᶜ) :
    ∃ V : ι → Y.Opens, IsOpenCover V ∧
      ∀ i, IsAffineOpen (V i) ∧ IsCompact (V i : Set Y) ∧
        ∃ (F : (SheafOfModules.isQuasicoherent (U i).toScheme.ringCatSheaf).FullSubcategory ⥤
            (SheafOfModules.isQuasicoherent (V i).toScheme.ringCatSheaf).FullSubcategory)
          (f : (V i).toScheme ≅ (U i).toScheme)
          (L : SheafOfModules.{u} (V i).toScheme.ringCatSheaf),
          F.IsEquivalence ∧
            Stacks.SheafOfModules.IsInvertible (V i).toScheme.presheaf
              (V i).toScheme.ringCatSheaf.2 L ∧
            Nonempty (e.functor ⋙ quasicoherentRestriction (V i).ι ≅
              quasicoherentRestriction (U i).ι ⋙ F) ∧
            Nonempty (F ⋙ ObjectProperty.ι
                (SheafOfModules.isQuasicoherent (V i).toScheme.ringCatSheaf) ≅
              pullbackTensorFunctor f.hom L)
```

**`AlgebraicGeometry.exists_isOpenCover_schemeIso_invertibleSheaf_of_isAffineOpenCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionGlobalForm.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionGlobalForm.lean#L265). The attribute's comment: “the GLOBAL form with step 2 DISCHARGED — `X` and `Y` quasi-compact and quasi-separated, an affine open cover `U i` of `X`, and no module hypothesised. The `G i` is `𝒪_X/I i` for the finite type ideal sheaf `I i` of Tag 01PH, finitely presented by `Stacks.AlgebraicGeometry.IdealSheafQuotient.isFinitePresentation_structureQuotient` and with support `V(I i)` by `Stacks.AlgebraicGeometry.IdealSheafQuotient.supp_structureQuotient`. Steps 2 to 8 and the covering assertion of step 9 are therefore all proved. The per-chart data IS glued downstream: the `f_i` into one isomorphism `Y ≅ X` by `exists_schemeIso_of_quasicoherentEquivalence` (`ReconstructionGlobalSchemeIso.lean`) and the `L_i` into one invertible `𝒪_Y`-module by `exists_isOpenCover_invertibleModule_restrictIso_of_isAffineOpenCover` (`ReconstructionGlobalModule.lean`). The single natural isomorphism `e(F) ≅ g^*F ⊗ M` comparing `e` with that glued pair — the stated conclusion of 0GPJ, which the Stacks source dismisses with "We omit the details" — is `exists_natIso_pullbackTensorFunctor_of_quasicoherentEquivalence` (`ReconstructionGlobalComparison.lean`). As in the affine case the comparison of functors is stated after forgetting quasi-coherence, between functors into all `𝒪_V`-modules”.

> **Stacks Project, Tag 0GPJ in its global form, with step 2 discharged.**  Let `X` and `Y` be
> quasi-compact and quasi-separated schemes, let `e : QCoh(𝒪_X) ≌ QCoh(𝒪_Y)` be an equivalence and
> let `U i` be an affine open cover of `X`.  Then there are opens `V i ⊆ Y` which **cover `Y`** and
> are each affine and quasi-compact, and for each `i` an equivalence
> `F_i : QCoh(𝒪_{U i}) ≌ QCoh(𝒪_{V i})` compatible with `e` and the two restrictions, an
> isomorphism of schemes `f_i : V i ≅ U i` and an invertible sheaf `L_i` of `𝒪_{V i}`-modules such
> that `F_i` is inverse image along `f_i` followed by `- ⊗_{𝒪_{V i}} L_i`.
>
> This is
> `AlgebraicGeometry.exists_isOpenCover_schemeIso_invertibleSheaf_of_isFinitePresentation` with its
> hypotheses `G` and `hG` *deleted*: the modules are produced by
> `AlgebraicGeometry.exists_isFinitePresentation_supportSet_eq_compl`.  Only the affine open cover
> of `X` is given.
>
> The module family is kept opaque, by `choose` against the single-index statement above, for the
> reason recorded in the implementation notes: handing over an explicit composite instead makes
> the conclusion unfold definitionally once per index and per conjunct.

```lean
theorem exists_isOpenCover_schemeIso_invertibleSheaf_of_isAffineOpenCover {ι : Type u}
    (U : ι → X.Opens) (hUaff : ∀ i, IsAffineOpen (U i)) (hUcover : IsOpenCover U) :
    ∃ V : ι → Y.Opens, IsOpenCover V ∧
      ∀ i, IsAffineOpen (V i) ∧ IsCompact (V i : Set Y) ∧
        ∃ (F : (SheafOfModules.isQuasicoherent (U i).toScheme.ringCatSheaf).FullSubcategory ⥤
            (SheafOfModules.isQuasicoherent (V i).toScheme.ringCatSheaf).FullSubcategory)
          (f : (V i).toScheme ≅ (U i).toScheme)
          (L : SheafOfModules.{u} (V i).toScheme.ringCatSheaf),
          F.IsEquivalence ∧
            Stacks.SheafOfModules.IsInvertible (V i).toScheme.presheaf
              (V i).toScheme.ringCatSheaf.2 L ∧
            Nonempty (e.functor ⋙ quasicoherentRestriction (V i).ι ≅
              quasicoherentRestriction (U i).ι ⋙ F) ∧
            Nonempty (F ⋙ ObjectProperty.ι
                (SheafOfModules.isQuasicoherent (V i).toScheme.ringCatSheaf) ≅
              pullbackTensorFunctor f.hom L)
```

**`AlgebraicGeometry.isInvertible_map_quasicoherentUnit_of_quasicoherentEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionGlobalModule.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionGlobalModule.lean#L240). The attribute's comment: “the MODULE half of the tag's conclusion, unconditionally: `X` and `Y` quasi-compact and quasi-separated and an equivalence `e` of their categories of quasi-coherent modules make `e(𝒪_X)` an invertible `𝒪_Y`-module. No cover, no affineness and no further hypothesis of any kind beyond qcqs. This identifies WHICH module the tag's `L` is and proves it invertible: were the tag's comparison `e(F) ≅ f^*F ⊗ L` available, `F = 𝒪_X` would give `L ≅ f^*𝒪_X ⊗ L ≅ e(𝒪_X)`, so no other module can serve. The statement is not an existential — `∃ L, IsInvertible L` is satisfied by `𝒪_Y` and would say nothing — it names the module. The per-chart invertible sheaves `L i` of the reconstruction are its restrictions (`restrictMapUnitIsoOfChartIso`), which is also what supplies the transition data the gluing of `ReconstructionGluedModule.lean:197` asks for; that gluing run on the reconstruction's own charts is `exists_isOpenCover_invertibleModule_restrictIso_of_isAffineOpenCover` below. The SCHEME half is `exists_schemeIso_of_quasicoherentEquivalence` (`ReconstructionGlobalSchemeIso.lean:324`). The comparison of functors — 0GPJ also asserts `e(F) ≅ f^*F ⊗ L` naturally in `F` — is NOT produced here: it is `exists_natIso_pullbackTensorFunctor_of_quasicoherentEquivalence` (`ReconstructionGlobalComparison.lean`), glued from the per-chart `chartComparisonIso` (`ReconstructionGlobalNatIso.lean`) by `exists_natIso_of_chartComparison` (`ReconstructionChartGlue.lean`), the two comparisons over a common affine open being made equal by the rigidity `natIso_eq_of_app_unit_eq_of_iso` (`ReconstructionChartRigidity.lean`) once they are normalised at `𝒪_X` (`chartComparisonIso_hom_app_quasicoherentUnit`). Nothing below assumes any of it”.

> **The image of the structure sheaf under an equivalence of categories of quasi-coherent
> modules is invertible.**  Let `X` and `Y` be quasi-compact and quasi-separated schemes and let
> `e : QCoh(𝒪_X) ≌ QCoh(𝒪_Y)` be an equivalence.  Then `e(𝒪_X)` is an invertible `𝒪_Y`-module.
>
> Invertibility of a module on a scheme is local on the base
> (`Stacks.Modules.isInvertible_of_isInvertible_restrict_isOpenCover`), the opens `V i` of the
> reconstruction cover `Y`, and over each of them `e(𝒪_X)` is the invertible sheaf `L i` of that
> chart by `AlgebraicGeometry.restrictMapUnitIsoOfChartIso`.

```lean
theorem isInvertible_map_quasicoherentUnit_of_quasicoherentEquivalence :
    Stacks.SheafOfModules.IsInvertible Y.presheaf Y.ringCatSheaf.2
      (e.functor.obj (quasicoherentUnit X)).obj
```

**`AlgebraicGeometry.exists_isOpenCover_invertibleModule_restrictIso_of_isAffineOpenCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionGlobalModule.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionGlobalModule.lean#L288). The attribute's comment: “the GLOBAL form with the per-chart invertible sheaves GLUED into one invertible `𝒪_Y`-module: `X` and `Y` quasi-compact and quasi-separated, an affine open cover `U i` of `X`, and no further hypothesis. The chart data is `exists_isOpenCover_schemeIso_invertibleSheaf_of_isAffineOpenCover` (`ReconstructionGlobalForm.lean:236`) with the families pulled out of the per-index existential; what is new is the last conjunct, a SINGLE invertible `𝒪_Y`-module restricting to every `L i`. It is `exists_invertibleModule_of_isOpenCover_of_overlapCompatible` (`ReconstructionGluedModule.lean:197`) run on these charts, its transition data being `transOfRestrictIso` for the module `e(𝒪_X)`, which restricts to each `L i` by `restrictMapUnitIsoOfChartIso`. The SCHEME half of the tag is `exists_schemeIso_of_quasicoherentEquivalence` (`ReconstructionGlobalSchemeIso.lean:324`). The comparison of functors `e(F) ≅ f^*F ⊗ M`, naturally in `F`, is NOT produced here: it is `exists_natIso_pullbackTensorFunctor_of_quasicoherentEquivalence` (`ReconstructionGlobalComparison.lean`), and it is stated for the module `e(𝒪_X)` rather than for the `M` glued here — taking `e(𝒪_X)` is what makes the per-chart comparisons agree at `𝒪_X`, because then the identification of its restriction with `L i` is `restrictMapUnitIsoOfChartIso`, built from the same `α i` and `β i`. Nothing in this statement assumes it”.

> **The global form of [Stacks, Tag 0GPJ] with the per-chart invertible sheaves glued into one
> invertible module.**  Let `X` and `Y` be quasi-compact and quasi-separated schemes, let
> `e : QCoh(𝒪_X) ≌ QCoh(𝒪_Y)` be an equivalence and let `U i` be an affine open cover of `X`.
> Then there are opens `V i` covering `Y`, each affine, and for each `i` an equivalence
> `F i : QCoh(𝒪_{U i}) ≌ QCoh(𝒪_{V i})` compatible with `e` and the two restrictions, an
> isomorphism of schemes `f i : V i ≅ U i` and an invertible sheaf `L i` of `𝒪_{V i}`-modules with
> `F i` inverse image along `f i` followed by `- ⊗ L i` — **and a single invertible `𝒪_Y`-module
> `M` whose restriction to each `V i` is `L i`**.
>
> This is
> `AlgebraicGeometry.exists_isOpenCover_schemeIso_invertibleSheaf_of_isAffineOpenCover` with the
> families pulled out of the per-index existential, together with
> `AlgebraicGeometry.exists_invertibleModule_of_isOpenCover_of_overlapCompatible` run on those
> charts.  The three transition hypotheses of the gluing are
> `AlgebraicGeometry.transOfRestrictIso`, `AlgebraicGeometry.transOfRestrictIso_resLE` and
> `AlgebraicGeometry.transOfRestrictIso_trans` for the module `e(𝒪_X)`, which restricts to each
> `L i` by `AlgebraicGeometry.restrictMapUnitIsoOfChartIso`.

```lean
theorem exists_isOpenCover_invertibleModule_restrictIso_of_isAffineOpenCover {κ : Type u}
    (U : κ → X.Opens) (hUaff : ∀ i, IsAffineOpen (U i)) (hUcover : IsOpenCover U) :
    ∃ (V : κ → Y.Opens)
      (F : ∀ i, (SheafOfModules.isQuasicoherent (U i).toScheme.ringCatSheaf).FullSubcategory ⥤
        (SheafOfModules.isQuasicoherent (V i).toScheme.ringCatSheaf).FullSubcategory)
      (f : ∀ i, (V i).toScheme ≅ (U i).toScheme)
      (L : ∀ i, SheafOfModules.{u} (V i).toScheme.ringCatSheaf) (M : Y.Modules),
      IsOpenCover V ∧ (∀ i, IsAffineOpen (V i)) ∧ (∀ i, (F i).IsEquivalence) ∧
        (∀ i, Stacks.SheafOfModules.IsInvertible (V i).toScheme.presheaf
          (V i).toScheme.ringCatSheaf.2 (L i)) ∧
        (∀ i, Nonempty (e.functor ⋙ quasicoherentRestriction (V i).ι ≅
          quasicoherentRestriction (U i).ι ⋙ F i)) ∧
        (∀ i, Nonempty (F i ⋙ ObjectProperty.ι
            (SheafOfModules.isQuasicoherent (V i).toScheme.ringCatSheaf) ≅
          pullbackTensorFunctor (f i).hom (L i))) ∧
        Stacks.SheafOfModules.IsInvertible Y.presheaf Y.ringCatSheaf.2 M ∧
        ∀ i, Nonempty (Scheme.Modules.restrict M (V i).ι ≅ L i)
```

**`AlgebraicGeometry.exists_schemeIso_of_quasicoherentEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionGlobalSchemeIso.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionGlobalSchemeIso.lean#L369). The attribute's comment: “the SCHEME HALF of the tag's conclusion, unconditionally: `X` and `Y` quasi-compact and quasi-separated and an equivalence of their categories of quasi-coherent modules give an isomorphism of schemes `Y ≅ X`. No cover, no affineness, no invertible module and no further hypothesis of any kind beyond qcqs. This is the step the Stacks source dismisses with "We omit the details", carried out: the charts are matched (`ReconstructionGlobalForm.lean`), they cover `Y` (`ReconstructionCover.lean:164`), they agree on overlaps in both directions (`ReconstructionOverlapCompatible.lean:256`, `ReconstructionGlobalSchemeIso.lean:223`) because the matched pair is rigid (`ReconstructionRigidity.lean:141`), and they glue (`ReconstructionGluedIso.lean:113`). The MODULE half — 0GPJ also asserts a single invertible `𝒪_Y`-module `L` with `e(F) ≅ f^*F ⊗ L` — is NOT produced here: it is `isInvertible_map_quasicoherentUnit_of_quasicoherentEquivalence` (`ReconstructionGlobalModule.lean`), the module being `e(𝒪_X)`, and the comparison of functors is `exists_natIso_pullbackTensorFunctor_of_quasicoherentEquivalence` (`ReconstructionGlobalComparison.lean`). Nothing in this statement assumes either”.

> **The scheme half of [Stacks, Tag 0GPJ] with no cover hypothesised.**  Two quasi-compact
> quasi-separated schemes with equivalent categories of quasi-coherent modules are isomorphic.
>
> This is the statement above with the affine open cover of `X` deleted: `X` is covered by its own
> affine opens, `AlgebraicGeometry.iSup_affineOpens_eq_top`, and that family is indexed by
> `AlgebraicGeometry.Scheme.affineOpens`, a type in the same universe.

```lean
theorem exists_schemeIso_of_quasicoherentEquivalence {X Y : Scheme.{u}} [CompactSpace X]
    [QuasiSeparatedSpace X] [CompactSpace Y] [QuasiSeparatedSpace Y]
    (e : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory ≌
      (SheafOfModules.isQuasicoherent Y.ringCatSheaf).FullSubcategory) :
    Nonempty (Y ≅ X)
```

**`AlgebraicGeometry.exists_isAffineOpen_schemeIso_invertibleSheaf_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionLocalForm.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionLocalForm.lean#L78). The attribute's comment: “steps 3 to 8 only: the statement LOCALIZED at one affine open `U ⊆ X`, with the module `G` of step 2 given as a hypothesis. This is the per-chart building block; the statement over a whole cover is `AlgebraicGeometry.exists_isOpenCover_schemeIso_invertibleSheaf_of_isAffineOpenCover`, where the covering of `Y` is proved (`AlgebraicGeometry.isOpenCover_of_supportedCorrespondence`) and `G` is produced rather than hypothesised, so nothing in this clause is left open by this file alone. Step 9's descent datum is available too: `AlgebraicGeometry.restrictionSquareFunctor` makes `F_U` explicit with `rfl` section formulas (the localization lift has no formula on sections, which is why it is rebuilt), and `AlgebraicGeometry.ReconstructionGlue.glueData` is a complete `FunctorGlueData`, all five fields, its covering hypothesis discharged by `AlgebraicGeometry.exists_gluedQuasicoherentFunctor_restrictIso`. What remains open for 0GPJ as a whole is the gluing of the per-chart `f_U` and `L_U` into a single isomorphism `Y ≅ X` and a single invertible `𝒪_Y`-module, which the source dismisses with "We omit the details". As in the affine case the comparison of functors is stated after forgetting quasi-coherence, between functors into all `𝒪_V`-modules”.

> **Stacks Project, Tag 0GPJ, steps 3 to 8: the local form of the proposition.**  Let `X` and
> `Y` be quasi-compact and quasi-separated schemes and let `e : QCoh(𝒪_X) ≌ QCoh(𝒪_Y)` be an
> equivalence.  Let `U ⊆ X` be an affine open and let `G` be a finitely presented quasi-coherent
> `𝒪_X`-module whose support is the complement of `U`.  Then there is a quasi-compact open
> `V ⊆ Y` — namely the complement of the support of `e.functor.obj G` — which is affine, and there
> are an equivalence `F_U : QCoh(𝒪_U) ≌ QCoh(𝒪_V)` compatible with `e` and the two restrictions, an
> isomorphism of schemes `f_U : V ≅ U` and an invertible sheaf `L_U` of `𝒪_V`-modules such that
> `F_U` is inverse image along `f_U` followed by `- ⊗_{𝒪_V} L_U`.

```lean
theorem exists_isAffineOpen_schemeIso_invertibleSheaf_of_isFinitePresentation (U : X.Opens)
    (hUaff : IsAffineOpen U)
    (G : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory)
    [SheafOfModules.IsFinitePresentation (R := X.ringCatSheaf) G.obj]
    (hG : supportSet G.obj = (U : Set X)ᶜ) :
    ∃ V : Y.Opens, IsAffineOpen V ∧ IsCompact (V : Set Y) ∧
      ∃ (F : (SheafOfModules.isQuasicoherent U.toScheme.ringCatSheaf).FullSubcategory ⥤
          (SheafOfModules.isQuasicoherent V.toScheme.ringCatSheaf).FullSubcategory)
        (f : V.toScheme ≅ U.toScheme) (L : SheafOfModules.{u} V.toScheme.ringCatSheaf),
        F.IsEquivalence ∧
          Stacks.SheafOfModules.IsInvertible V.toScheme.presheaf V.toScheme.ringCatSheaf.2 L ∧
          Nonempty (e.functor ⋙ quasicoherentRestriction V.ι ≅
            quasicoherentRestriction U.ι ⋙ F) ∧
          Nonempty (F ⋙ ObjectProperty.ι
              (SheafOfModules.isQuasicoherent V.toScheme.ringCatSheaf) ≅
            pullbackTensorFunctor f.hom L)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 56.6, Tag 0GPD](https://stacks.math.columbia.edu/tag/0GPD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
