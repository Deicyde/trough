---
declaration: section
origin: cited
lean: AlgebraicGeometry.isFinitelyPresentable_iff_isFinitePresentation, AlgebraicGeometry.exists_nonzero_hom_of_supp_subset, AlgebraicGeometry.supportContained_eq_serreCoproductClosure, AlgebraicGeometry.quasicoherentSupportedOn_isSerreClass, AlgebraicGeometry.quasicoherentRestriction_isLocalization, AlgebraicGeometry.quasicoherentSupportedQuotientEquivalence, AlgebraicGeometry.quasicoherentSupportedQuotientEquivalenceFunctorIso, AlgebraicGeometry.AffineOfModuleCategory.isAffine_of_quasicoherentModules_equivalent_moduleCat
statement: formalized
proof: formalized
---

# 56.6 Gabriel-Rosenberg reconstruction

Section 56.6 of the Stacks Project, [Tag 0GPD](https://stacks.math.columbia.edu/tag/0GPD). 6 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GPE, a lemma

[Tag 0GPE](https://stacks.math.columbia.edu/tag/0GPE) in the Stacks Project.

**`AlgebraicGeometry.isFinitelyPresentable_iff_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/CompactObjects.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/CompactObjects.lean#L152).

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

**`AlgebraicGeometry.exists_nonzero_hom_of_supp_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedNonzeroHom.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedNonzeroHom.lean#L358). References: SGA 2 VII (1.3), “affine case”.

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

**`AlgebraicGeometry.supportContained_eq_serreCoproductClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreSubcategory.lean, line 780](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreSubcategory.lean#L780).

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

**`AlgebraicGeometry.quasicoherentSupportedOn_isSerreClass`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean#L229). The attribute's comment: “the full subcategory of modules supported on `Z` is a Serre subcategory”.

> Quasi-coherent modules supported on a fixed subset of a scheme form a Serre subcategory of
> the category of all quasi-coherent modules.

```lean
public instance quasicoherentSupportedOn_isSerreClass (X : Scheme.{u}) (Z : Set X) :
    (quasicoherentSupportedOn X Z).IsSerreClass
```

**`AlgebraicGeometry.quasicoherentRestriction_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean#L307). The attribute's comment: “restriction is the localization at the supported Serre subcategory”.

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

**`AlgebraicGeometry.quasicoherentSupportedQuotientEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean#L378). The attribute's comment: “the induced equivalence from the quotient category”.

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

**`AlgebraicGeometry.quasicoherentSupportedQuotientEquivalenceFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/SupportedSerreQuotient.lean#L390). The attribute's comment: “the equivalence is induced by the restriction functor”.

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

**`AlgebraicGeometry.AffineOfModuleCategory.isAffine_of_quasicoherentModules_equivalent_moduleCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/AffineOfModuleCategory.lean, line 1142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/AffineOfModuleCategory.lean#L1142). The attribute's comment: “`[CommRing R]` reads the tag's `a ring`: the rank-one step needs `End P` commutative. For noncommutative `R` the conclusion still holds by Morita equivalence (`Mod (M₂ k) ≌ Mod k`), but that rank-one step fails outright.”.

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

**`AlgebraicGeometry.AffineOfModuleCategory.isAffine_of_quasicoherentModules_equivalence_moduleCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/AffineOfModuleCategory.lean, line 1165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/AffineOfModuleCategory.lean#L1165). The attribute's comment: “the hypothesis in the orientation of the source, `QCoh(𝒪_X) ≌ Mod R`; `[CommRing R]` reads the tag's `a ring`, exactly as for the mirror form `isAffine_of_quasicoherentModules_equivalent_moduleCat`”.

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

**`AlgebraicGeometry.exists_natIso_pullbackTensorFunctor_of_quasicoherentEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionGlobalComparison.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/ReconstructionGlobalComparison.lean#L113). The attribute's comment: “the tag IN FULL, for `X` and `Y` quasi-compact and quasi-separated: an equivalence of the categories of quasi-coherent modules gives an isomorphism of schemes `g : Y ≅ X`, an invertible `𝒪_Y`-module `M`, and a NATURAL isomorphism `e(𝓕) ≅ g^*𝓕 ⊗ M`. No cover, no affineness and no further hypothesis of any kind beyond qcqs. The scheme half is `exists_schemeIso_of_quasicoherentEquivalence` and the module half `isInvertible_map_quasicoherentUnit_of_quasicoherentEquivalence`, both already unconditional; what is new is the comparison of functors, which the Stacks source dismisses with "We omit the details". It is glued from the per-chart comparisons `chartComparisonIso` by `exists_natIso_of_chartComparison`, whose agreement hypothesis is discharged by the rigidity `natIso_eq_of_app_unit_eq_of_iso` once the comparisons are normalised at `𝒪_X`; the normalisation is `chartComparisonIso_hom_app_quasicoherentUnit` and it is automatic, because the module is `e(𝒪_X)` and the identification of its restriction with the chart's `L` is `restrictMapUnitIsoOfChartIso`, built from the same `α` and `β`. As in the affine case the comparison is stated after forgetting quasi-coherence, between functors into all `𝒪_Y`-modules”.

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

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 56.6, Tag 0GPD](https://stacks.math.columbia.edu/tag/0GPD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
