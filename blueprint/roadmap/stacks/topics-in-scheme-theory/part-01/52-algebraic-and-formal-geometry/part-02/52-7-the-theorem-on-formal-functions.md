---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.isIso_derivedCompletionPushforwardComparison_idealSheafData_inverseImageIdealSheaf, Stacks.Algebraization.adicCompletion_homology_derivedSections_iso_derivedCompletion, Stacks.Algebraization.homology_derivedCompletion_derivedSections_iso_adicCompletion, Stacks.Algebraization.exists_iso_homology_derivedSections_derivedCompletion_whole, Stacks.Algebraization.isDerivedLimit_single_limit_powerQuotients, Stacks.Algebraization.isZero_cohomology_limit_powerQuotients_of_isAffineOpen, Stacks.Algebraization.nonempty_iso_homology_derivedCompletion_limit_adicQuotientSystem, Stacks.Algebraization.isIso_comparisonDerivedCompletionLimitAdicQuotient
statement: formalized
proof: formalized
---

# 52.7 The theorem on formal functions

Section 52.7 of the Stacks Project, [Tag 0A0H](https://stacks.math.columbia.edu/tag/0A0H). 5 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A0I, an equation

[Tag 0A0I](https://stacks.math.columbia.edu/tag/0A0I) in the Stacks Project.

**`AlgebraicGeometry.Scheme.isIso_derivedCompletionPushforwardComparison_idealSheafData_inverseImageIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionFiniteType.lean, line 487](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionFiniteType.lean#L487). The attribute's comment: “Equation 52.7.0.1 in the display's own setting and at Section 52.7's own data, for an **arbitrary** object, as an invertibility of the **canonical** comparison map `(Rf_*ℱ)^∧ ⟶ Rf_*(ℱ^∧)`: a morphism of **schemes** `f : X ⟶ S`, a **quasi-coherent** sheaf of ideals `ℐ ⊆ 𝒪_S` **of finite type** — an `AlgebraicGeometry.Scheme.IdealSheafData` read on the small Zariski ringed site — and the completion on `X` taken along the sheaf of ideals `f^{-1}ℐ · 𝒪_X` built out of `ℐ`, the image of `f^*ℐ ⟶ 𝒪_X`. No restriction on `ℱ`: every object of `D(𝒪_X)`, in particular every quasi-coherent `ℱ`. That `f^♯(f^{-1}ℐ) ⊆ f^{-1}ℐ · 𝒪_X` and that this sheaf of ideals is of finite type, so that [Stacks, Tag 099F] produces the derived completion along it, are theorems about the construction, not hypotheses”.

> **Equation 52.7.0.1 of [Stacks, Tag 0A0I] at Section 52.7's own data, for an arbitrary
> object — and so the analogue for complexes of quasi-coherent modules of [Stacks, Tag 0AKL].** Let
> `f : X ⟶ S` be a morphism of schemes, let `ℐ ⊆ 𝒪_S` be a quasi-coherent sheaf of ideals of finite
> type and let `ℐ' = f^{-1}ℐ · 𝒪_X` be the sheaf of ideals Section 52.7 builds out of it. Then the
> canonical comparison map
>
> `(Rf_*K)^∧ ⟶ Rf_*(K^∧)`
>
> is invertible for **every** object `K` of `D(𝒪_X)`, the completion on `S` being taken along `ℐ`
> and the one on `X` along `ℐ'`. In particular it is invertible for every complex of
> quasi-coherent `𝒪_X`-modules, with no derived-completeness or nilpotence restriction.
>
> `ℐ` is an `AlgebraicGeometry.Scheme.IdealSheafData`, read on the small Zariski ringed site by
> `Stacks.Algebraization.idealSheafSiteSubmodule`, and "of finite type" is
> `SheafOfModules.IsFiniteType` (automatic on a locally Noetherian scheme, by
> `Stacks.Algebraization.isFiniteType_idealSheafSiteSubmodule`). The sheaf of ideals `ℐ'` is
> `AlgebraicGeometry.RingedSite.inverseImageIdealSheaf`, the image of `f^*ℐ ⟶ 𝒪_X`; that `f^♯`
> carries `f^{-1}ℐ` into it is
> `AlgebraicGeometry.RingedSite.pushforwardIdealCompatible_inverseImageIdealSheaf`, and that it is of
> finite type — so that the derived completion along it exists, by [Stacks, Tag 099F] — is
> `AlgebraicGeometry.RingedSite.isFiniteType_inverseImageIdealSheaf`. Neither is a hypothesis.
>
> This is
> `RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType`,
> the ringed-sites case of [Stacks, Tag 0A0G], at the morphism of ringed sites
> `AlgebraicGeometry.Scheme.toRingedSiteHom f` underlying `f`.

```lean
theorem isIso_derivedCompletionPushforwardComparison_idealSheafData_inverseImageIdealSheaf
    [(idealSheafSiteSubmodule I).toSheafOfModules.IsFiniteType]
    (K : DerivedCategory (_root_.SheafOfModules.{u}
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (Stacks.RingedSpace.toRingedSite X.toRingedSpace).O)))) :
    IsIso ((RingedSite.derivedCompletionPushforwardComparison (toRingedSiteHom f)
      (idealSheafSiteSubmodule I)
      (RingedSite.inverseImageIdealSheaf.{u} (toRingedSiteHom f) (idealSheafSiteSubmodule I))
      (RingedSite.pushforwardIdealCompatible_inverseImageIdealSheaf.{u} (toRingedSiteHom f)
        (idealSheafSiteSubmodule I))).app K)
```

## Tag 0A0L, a lemma

[Tag 0A0L](https://stacks.math.columbia.edu/tag/0A0L) in the Stacks Project.

**`Stacks.Algebraization.adicCompletion_homology_derivedSections_iso_derivedCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/FormalFunctionsPseudoCoherent.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/FormalFunctionsPseudoCoherent.lean#L152). The attribute's comment: “the second equality `lim H^p(U, K)/IⁿH^p(U, K) = H^p(U, K)^∧`, the right hand completion being the derived completion of the module `H^p(U, K)` along `I = 𝓘(U)`; the first equality is `homology_derivedSections_derivedCompletion_iso_adicCompletion`”.

> **Stacks Project, Tag 0A0L, the second equality.** Let `X` be a locally Noetherian scheme,
> `𝓘 ⊂ 𝒪_X` a quasi-coherent sheaf of ideals and `K` a pseudo-coherent object of `D(𝒪_X)`. For an
> affine open `U`, with `A = Γ(X, U)` and `I = 𝓘(U)`, and any left adjoint `C` to the inclusion of
> the derived-complete objects of `D(A)`, the `I`-adic completion `lim H^p(U, K)/IⁿH^p(U, K)` of
> `H^p(U, K)` is the derived `I`-adic completion of the `A`-module `H^p(U, K)`, read in degree zero.
>
> This is [Stacks, Tag 0A06] for the complex `H^p(U, K)[0]`, which is legitimate because
> `H^p(U, K)` is a finite module.

```lean
public theorem adicCompletion_homology_derivedSections_iso_derivedCompletion
    (X : Scheme.{u}) [IsLocallyNoetherian X] (𝓘 : X.IdealSheafData)
    (K : DerivedCategory X.Modules)
    (hK : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) K)
    (U : X.affineOpens)
    (C : DerivedCategory (ModuleCat.{u} Γ(X, U.1)) ⥤
      (show ObjectProperty (DerivedCategory (ModuleCat.{u} Γ(X, U.1))) from
        fun L ↦ IsDerivedComplete (𝓘.ideal U) L).FullSubcategory)
    (adj : C ⊣ (show ObjectProperty (DerivedCategory (ModuleCat.{u} Γ(X, U.1))) from
      fun L ↦ IsDerivedComplete (𝓘.ideal U) L).ι)
    (p : ℤ) :
    Nonempty
      (ModuleCat.of Γ(X, U.1) (AdicCompletion (𝓘.ideal U)
          ((DerivedCategory.homologyFunctor (ModuleCat.{u} Γ(X, U.1)) p).obj
            ((derivedSections (structureSheafRing X.toRingedSpace) U.1).obj K))) ≅
        (DerivedCategory.homologyFunctor (ModuleCat.{u} Γ(X, U.1)) 0).obj
          ((C ⋙ (show ObjectProperty (DerivedCategory (ModuleCat.{u} Γ(X, U.1))) from
              fun L ↦ IsDerivedComplete (𝓘.ideal U) L).ι).obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} Γ(X, U.1)) 0).obj
              ((DerivedCategory.homologyFunctor (ModuleCat.{u} Γ(X, U.1)) p).obj
                ((derivedSections (structureSheafRing X.toRingedSpace) U.1).obj K)))))
```

**`Stacks.Algebraization.homology_derivedCompletion_derivedSections_iso_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/FormalFunctionsPseudoCoherentModuleSide.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/FormalFunctionsPseudoCoherentModuleSide.lean#L157). The attribute's comment: “the first equality `H^p(RΓ(U, K)^∧) = lim H^p(U, K)/IⁿH^p(U, K)` on the module side: its left hand side read at the derived completion in `D(A)` of the derived sections `RΓ(U, K)`, for `A = Γ(X, U)` and `I = 𝓘(U)`, which is [Stacks, Tag 0A06] applied to `RΓ(U, K)` together with the finiteness of the `H^n(U, K)`; the second equality is `exists_adjunction_and_adicCompletion_homology_derivedSections_iso_derivedCompletion`”.

> **Stacks Project, Tag 0A0L, the first equality, read on the module side.** Let `X` be a
> locally Noetherian scheme, `𝓘 ⊂ 𝒪_X` a quasi-coherent sheaf of ideals and `K` a pseudo-coherent
> object of `D(𝒪_X)`. For an affine open `U`, with `A = Γ(X, U)` and `I = 𝓘(U)`, the degree-`p`
> cohomology of the derived completion in `D(A)` of `RΓ(U, K)` is the `I`-adic completion
> `lim H^p(U, K)/IⁿH^p(U, K)` of `H^p(U, K)`.
>
> Everything the source's first equality needs beyond the identification `RΓ(U, K^∧)
> = RΓ(U, K)^∧`: `A` is Noetherian and `H^n(U, K)` is a finite `A`-module in every degree
> (`Stacks.Algebraization.finite_homology_derivedSections_of_isPseudoCoherent`, which is where
> pseudo-coherence and the locally Noetherian hypothesis of the tag are used), so [Stacks,
> Tag 0A06] applies to `RΓ(U, K)` along `I = 𝓘(U)`.
>
> The derived completion of `A`-modules is produced, not assumed: the first conjunct exhibits a
> left adjoint `C` to the inclusion of the derived-complete objects of `D(A)`, by
> `Stacks.Algebraization.exists_derivedCompletionAdjunction`, and the second conjunct holds for
> every such `C`, so no choice of reflector enters.
>
> The left hand side is the cohomology of `C(RΓ(U, K))`, not of `RΓ(U, K^∧)`; passing between the
> two is [Stacks, Tag 0CQI], which
> `exists_adjunction_and_homology_derivedSections_derivedCompletion_iso_adicCompletion` below takes
> as an input and
> `Stacks.Algebraization.exists_iso_homology_derivedSections_derivedCompletion_whole` of
> `Completion/FormalFunctionsPseudoCoherentWhole.lean` discharges.

```lean
public theorem homology_derivedCompletion_derivedSections_iso_adicCompletion
    (X : Scheme.{u}) [IsLocallyNoetherian X] (𝓘 : X.IdealSheafData)
    (K : DerivedCategory X.Modules)
    (hK : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) K)
    (U : X.affineOpens) (p : ℤ) :
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} Γ(X, U.1))) :=
      fun L ↦ IsDerivedComplete (𝓘.ideal U) L
    (∃ C : DerivedCategory (ModuleCat.{u} Γ(X, U.1)) ⥤ P.FullSubcategory,
        Nonempty (C ⊣ P.ι)) ∧
      ∀ C : DerivedCategory (ModuleCat.{u} Γ(X, U.1)) ⥤ P.FullSubcategory, (C ⊣ P.ι) →
        Nonempty
          ((DerivedCategory.homologyFunctor (ModuleCat.{u} Γ(X, U.1)) p).obj
              ((C ⋙ P.ι).obj
                ((derivedSections (structureSheafRing X.toRingedSpace) U.1).obj K)) ≅
            ModuleCat.of Γ(X, U.1) (AdicCompletion (𝓘.ideal U)
              ((DerivedCategory.homologyFunctor (ModuleCat.{u} Γ(X, U.1)) p).obj
                ((derivedSections (structureSheafRing X.toRingedSpace) U.1).obj K))))
```

**`Stacks.Algebraization.exists_iso_homology_derivedSections_derivedCompletion_whole`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/FormalFunctionsPseudoCoherentWhole.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/FormalFunctionsPseudoCoherentWhole.lean#L223). The attribute's comment: “the whole lemma, at the source's own hypotheses — `X` a locally Noetherian scheme, `𝓘 ⊂ 𝒪_X` a quasi-coherent sheaf of ideals and `K` a pseudo-coherent object of `D(𝒪_X)`: for every affine open `U`, with `A = Γ(X, U)` and `I = 𝓘(U)`, and every `p`, both equalities `H^p(U, K^∧) = lim H^p(U, K)/IⁿH^p(U, K) = H^p(U, K)^∧`, the right hand completion being the derived completion of the A-module H^p(U,K) along I read in degree zero. The left hand side is read at the derived completion `K^∧` on `D(𝒪_X)` along `𝓘` itself, which exists because a quasi-coherent sheaf of ideals of a locally Noetherian scheme is of finite type, so [Stacks, Tag 099F] applies; the passage `RΓ(U, K^∧) = RΓ(U, K)^∧` is [Stacks, Tag 0CQI] at an affine open, where the chosen generating family spans `𝓘(U)` itself. The reflector onto the derived-complete objects of D(A) is produced out of [Stacks, Tag 0920] and the conclusion quantifies over it”.

> **Stacks Project, Tag 0A0L.** Let `X` be a locally Noetherian scheme, `ℐ ⊂ 𝒪_X` a
> quasi-coherent sheaf of ideals and `K` a pseudo-coherent object of `D(𝒪_X)` with derived
> completion `K^∧`. Then for every affine open `U ⊂ X`, with `A = Γ(X, U)` and `I = ℐ(U)`, and
> every `p`,
>
> `H^p(U, K^∧) = lim H^p(U, K)/IⁿH^p(U, K) = H^p(U, K)^∧`,
>
> the completion on the right being the derived completion of the `A`-module `H^p(U, K)` along `I`,
> read in degree zero.
>
> Both equalities, at the source's own hypotheses. The first is
> `exists_adjunction_and_homology_derivedSections_derivedCompletion_iso_adicCompletion`
> with its input — the identification `RΓ(U, K^∧) = RΓ(U, K)^∧` of [Stacks, Tag 0CQI] — discharged by
> `Stacks.Algebraization.nonempty_iso_derivedSections_derivedCompletion_affine`; the second is
> `Stacks.Algebraization.adicCompletion_homology_derivedSections_iso_derivedCompletion`, which is
> [Stacks, Tag 0A06] for the finite module `H^p(U, K)` placed in degree zero. Pseudo-coherence and
> the locally Noetherian hypothesis enter through the finiteness of `H^n(U, K)`, which is
> `Stacks.Algebraization.finite_homology_derivedSections_of_isPseudoCoherent`.
>
> Derived completion of `A`-modules is produced, not assumed: the first conjunct exhibits a left
> adjoint `C` to the inclusion of the derived-complete objects of `D(A)`, by
> `Stacks.Algebraization.exists_derivedCompletionAdjunction`, and the second holds for every such
> `C`, so no choice of reflector enters. The derived completion `K^∧` on `D(𝒪_X)` is produced too:
> `ℐ` is of finite type on a locally Noetherian scheme
> (`Stacks.Algebraization.isFiniteType_idealSheafSiteSubmodule`), so the reflector of [Stacks,
> Tag 099F] exists along the tag's own ideal sheaf.

```lean
theorem exists_iso_homology_derivedSections_derivedCompletion_whole
    (hK : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) K) (p : ℤ) :
    let P : ObjectProperty (DerivedCategory (ModuleCat.{u} Γ(X, U.1))) :=
      fun L ↦ IsDerivedComplete (𝓘.ideal U) L
    let Hp := fun (L : DerivedCategory X.Modules) ↦
      (DerivedCategory.homologyFunctor (ModuleCat.{u} Γ(X, U.1)) p).obj
        ((derivedSections (structureSheafRing X.toRingedSpace) U.1).obj L)
    (∃ C : DerivedCategory (ModuleCat.{u} Γ(X, U.1)) ⥤ P.FullSubcategory,
        Nonempty (C ⊣ P.ι)) ∧
      ∀ (C : DerivedCategory (ModuleCat.{u} Γ(X, U.1)) ⥤ P.FullSubcategory) (_ : C ⊣ P.ι),
        Nonempty
          (Hp ((AlgebraicGeometry.RingedSite.derivedCompletion (opensRingedSite X.sheaf)
              (idealSheafSiteSubmodule 𝓘)).obj K) ≅
            ModuleCat.of Γ(X, U.1) (AdicCompletion (𝓘.ideal U) (Hp K))) ∧
        Nonempty
          (ModuleCat.of Γ(X, U.1) (AdicCompletion (𝓘.ideal U) (Hp K)) ≅
            (DerivedCategory.homologyFunctor (ModuleCat.{u} Γ(X, U.1)) 0).obj
              ((C ⋙ P.ι).obj
                ((DerivedCategory.singleFunctor (ModuleCat.{u} Γ(X, U.1)) 0).obj (Hp K))))
```

## Tag 0A0K, a lemma

[Tag 0A0K](https://stacks.math.columbia.edu/tag/0A0K) in the Stacks Project.

**`Stacks.Algebraization.isDerivedLimit_single_limit_powerQuotients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/AdicQuotientDerivedLimit.lean, line 391](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/AdicQuotientDerivedLimit.lean#L391). The attribute's comment: “part (4), `lim ℱ/𝓘ⁿℱ = R lim ℱ/𝓘ⁿℱ`: for a coherent module `ℱ` on a locally Noetherian scheme and an arbitrary quasi-coherent sheaf of ideals `𝓘`, the **ordinary** inverse limit of the adic quotient tower, placed in degree zero, is a **derived** inverse limit of that tower, with nothing assumed. The terms of the tower are quasi-coherent, hence acyclic on the affine opens, and its transitions are surjective on affine sections, hence Mittag-Leffler, and those are the two hypotheses [Stacks, Tag 0BKS] consumes. Existence of the product the derived limit is written with is part of the conclusion rather than a hypothesis”.

> **Stacks Project, Tag 0A0K, part (4).** The ordinary inverse limit of the coherent adic
> quotient tower, placed in degree zero, is its derived inverse limit.

```lean
public theorem isDerivedLimit_single_limit_powerQuotients
    {X : Scheme.{u}} [IsLocallyNoetherian X]
    (I : X.IdealSheafData) (F : X.Modules) [F.IsCoherent] :
    let S := (powerQuotientSystem I F
      (isQuasicoherent_of_isCoherent F)).system
    ∃ h : HasProduct (fun n : ℕ =>
        (S ⋙ DerivedCategory.singleFunctor X.Modules 0).obj ⟨n⟩),
      @IsDerivedLimit (DerivedCategory X.Modules) _ _ _ _ _ _
        (S ⋙ DerivedCategory.singleFunctor X.Modules 0) h
        ((DerivedCategory.singleFunctor X.Modules 0).obj (limit S))
```

**`Stacks.Algebraization.isZero_cohomology_limit_powerQuotients_of_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/AdicQuotientDerivedLimit.lean, line 432](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/AdicQuotientDerivedLimit.lean#L432). The attribute's comment: “part (5), `H^p(U, ℱ^∧) = 0` for `p ≠ 0` and `U ⊂ X` affine open, read on the ordinary limit `lim ℱ/ℐⁿℱ` — the object [Stacks, Tag 0A0K] part (3) names `ℱ^∧` — for a coherent module `ℱ` on a locally Noetherian scheme and an arbitrary quasi-coherent sheaf of ideals `ℐ`, with nothing assumed: the terms of the adic quotient tower are quasi-coherent, hence acyclic on the affine opens, and its transitions are surjective on affine sections, hence Mittag-Leffler, and those are the two hypotheses [Stacks, Tag 0BKS] consumes”.

> **Stacks Project, Tag 0A0K, part (5).** On a locally Noetherian scheme the ordinary inverse
> limit `lim ℱ/ℐⁿℱ` of the adic quotient tower of a coherent module has no cohomology in positive
> degree over an affine open.
>
> The terms of the tower are quasi-coherent, so Serre vanishing gives their acyclicity on the
> affine opens, and the transition maps are epimorphisms of quasi-coherent modules, hence
> surjective on affine sections, so Mittag-Leffler gives the vanishing of `R¹ lim` of the sections
> there. Those are exactly the two hypotheses of
> `Stacks.Cohomology.SpaceInverseLimits.isZero_cohomology_limit_of_isBasis` on the basis of affine
> opens.
>
> The object is the ordinary limit `lim ℱ/ℐⁿℱ`, which is what the source's own argument for this
> part is about: parts (4) and (5) are both read off [Stacks, Tag 0A0J] for the quotient tower,
> and it is the tag's part (3) that then names that limit `ℱ^∧`. In this library part (3) at the
> tag's own hypotheses is
> `Stacks.Algebraization.isIso_comparisonDerivedCompletionLimitAdicQuotient` of
> `Completion/AdicQuotientSliceTowerKoszul.lean`, and part (5) stated on the derived completion `ℱ^∧`
> itself, in every degree `p ≠ 0` of either sign, is
> `Stacks.Algebraization.isZero_homology_derivedSections_derivedCompletion_of_isAffineOpen` of
> `Completion/CoherentCompletionAffineVanishing.lean`, which is derived from this statement through
> that isomorphism.

```lean
public theorem isZero_cohomology_limit_powerQuotients_of_isAffineOpen
    {X : Scheme.{u}} [IsLocallyNoetherian X]
    (I : X.IdealSheafData) (F : X.Modules) [F.IsCoherent]
    (U : X.affineOpens) (p : ℕ) (hp : 0 < p) :
    IsZero (Hgroup X.ringCatSheaf U.1 p
      (show X.Modules from limit (adicQuotientSystem I F)))
```

**`Stacks.Algebraization.nonempty_iso_homology_derivedCompletion_limit_adicQuotientSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/AdicQuotientLimitSheafIso.lean, line 512](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/AdicQuotientLimitSheafIso.lean#L512). The attribute's comment: “part (2), `H^q(K^∧) = lim H^q(K)/𝓘ⁿ H^q(K)`: for a **pseudo-coherent** object `K` of `D(𝒪_X)` on a locally Noetherian scheme `X` and an **arbitrary** quasi-coherent sheaf of ideals `𝓘`, the degree-`q` cohomology sheaf of the derived completion `K^∧` is isomorphic to the inverse limit of the adic quotient tower of the coherent module `H^q(K)`, with nothing further assumed — no quasi-compactness of `X`, no generation of `𝓘` by global sections, no Mittag-Leffler hypothesis and no appeal to part (1) of the tag. The limit is the same object parts (3), (4) and (5) are registered over, `Stacks.Algebraization.adicQuotientSystem`, read at the coherent module the tag's own footnote names. The isomorphism is non-canonical in the statement only because the source's canonical maps go the other way; it is produced by gluing the canonical affine comparisons, which are unique”.

> **Part (2) of [Stacks, Tag 0A0K].** For a pseudo-coherent object `K` of `D(𝒪_X)` on a locally
> Noetherian scheme `X` and an arbitrary quasi-coherent sheaf of ideals `𝓘`,
>
> `H^q(K^∧) ≅ lim_n H^q(K)/𝓘ⁿ H^q(K)`.
>
> The isomorphism is `Stacks.BasisRestriction.moduleSheafIsoOfBasisSectionsIso` applied to the
> affine comparisons `Stacks.Algebraization.adicQuotientLimitSectionsComparison`, which are
> bijective and compatible with restriction, against the unit of sheafification on the degree-`q`
> hypercohomology presheaf of `K^∧`; the sheafification of that presheaf is the cohomology sheaf by
> [Stacks, Tag 0BKV].

```lean
theorem nonempty_iso_homology_derivedCompletion_limit_adicQuotientSystem :
    Nonempty ((DerivedCategory.homologyFunctor X.Modules q).obj
          ((AlgebraicGeometry.RingedSite.derivedCompletion (opensRingedSite X.sheaf)
            (idealSheafSiteSubmodule 𝓘)).obj K) ≅
        limit (C := X.Modules)
          (adicQuotientSystem 𝓘 (homologyCoherentModule K hK q).obj))
```

**`Stacks.Algebraization.isIso_comparisonDerivedCompletionLimitAdicQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/AdicQuotientSliceTowerKoszul.lean, line 498](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/AdicQuotientSliceTowerKoszul.lean#L498). The attribute's comment: “part (3), `ℱ^∧ = lim ℱ/𝓘ⁿℱ` with an ordinary limit, at the source's own hypotheses: for a coherent module `ℱ` on a locally Noetherian scheme `X`, which is **not** assumed quasi-compact, and an **arbitrary** quasi-coherent sheaf of ideals `𝓘` — with no global generating family — the canonical comparison `c : ℱ^∧ ⟶ (lim ℱ/𝓘ⁿℱ)[0]` from the derived completion of `ℱ` along `𝓘` to the ordinary inverse limit of the adic quotients `ℱ/𝓘ⁿℱ`, placed in degree zero, is an isomorphism. The comparison is the unique map compatible with the completion unit and the limit lift, so the statement identifies a named map rather than asserting an abstract isomorphism. The source's `=` is also read as such an abstract isomorphism by `nonempty_iso_completion_limit_adicQuotientSystem`, which buys quasi-compactness of the scheme and a global generating family for the ideal sheaf”.

> **Part (3) of [Stacks, Tag 0A0K]: `ℱ^∧ = lim ℱ/𝓘ⁿℱ` with an ordinary inverse limit.** Let `X`
> be a locally Noetherian scheme — **not** assumed quasi-compact — let `𝓘 ⊂ 𝒪_X` be an arbitrary
> quasi-coherent sheaf of ideals and let `ℱ` be a coherent `𝒪_X`-module. Then the canonical
> comparison
>
> `c : ℱ^∧ ⟶ (lim ℱ/𝓘ⁿℱ)[0]`
>
> from the derived completion of `ℱ` along `𝓘` to the ordinary inverse limit of the adic quotients,
> placed in degree zero, is an isomorphism.
>
> The comparison is the unique map compatible with the completion unit of `ℱ` and the limit lift
> `ℱ ⟶ lim ℱ/𝓘ⁿℱ` (`Stacks.Algebraization`
> `.existsUnique_comparison_derivedCompletion_limit_adicQuotientSystem`), so the statement is about
> a named map and not merely the existence of an isomorphism — which is what makes it provable at
> these hypotheses at all, invertibility of a named map being local on the site
> (`Stacks.SheafOfModules.isIso_of_coversTop_mapDerivedCategory`).
>
> `Stacks.Algebraization.isIso_comparison_of_affineOpens_sliceTower` reduces it to the per-affine-
> slice presentation `Stacks.Algebraization`
> `.exists_isDerivedLimitWithProjections_completionToAdicQuotientSliceTower`, which is the Koszul
> chain of `DerivedCompletionRinged/` run on the slice over an affine open, where the restricted
> ideal sheaf is generated by finitely many sections and the Artin–Rees level is computed once over
> a single Noetherian model.
>
> `Stacks.Algebraization.nonempty_iso_completion_limit_adicQuotientSystem` of
> `Completion/KoszulAdicCompletionLimit.lean` is the other registration of this part: it runs the
> same chain on `X` itself, which costs `[CompactSpace X]` and a global generating family for `𝓘`
> and delivers the non-canonical isomorphism of [Stacks, Tag 0H9L] in place of the invertibility of
> `c`.

```lean
theorem isIso_comparisonDerivedCompletionLimitAdicQuotient :
    IsIso (comparisonDerivedCompletionLimitAdicQuotient I ℱ)
```

**`Stacks.Algebraization.isDerivedLimit_adicReductionTower_derivedCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/AdicReductionTowerDerivedLimit.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/AdicReductionTowerDerivedLimit.lean#L95). The attribute's comment: “part (1), `K^∧ = R lim (K ⊗^𝐋_𝒪 𝒪/𝓘ⁿ)`, at the source's own hypotheses: on a locally Noetherian scheme `Y`, for an **arbitrary** quasi-coherent sheaf of ideals `𝓘` and an **arbitrary** object `K` of `D(𝒪_Y)`, the derived completion `K^∧` along `𝓘` (the reflector of Tag 099F) is a derived limit of the tower `n ↦ K ⊗^𝐋_{𝒪_Y} 𝒪_Y/𝓘ⁿ⁺¹`. No quasi-compactness of `Y` and no generation of `𝓘` by global sections is assumed. `R lim` is a predicate rather than a functor, so the source's equality is read as `K^∧` being a derived limit of that tower, the same reading as the tag's part (4); the tower over the positive powers `𝓘ⁿ⁺¹` is cofinal in the one over all powers”.

> **Part (1) of [Stacks, Tag 0A0K].** On a locally Noetherian scheme `Y`, for an arbitrary
> quasi-coherent sheaf of ideals `𝓘` and an arbitrary object `K` of `D(𝒪_Y)`, the derived
> completion `K^∧` along `𝓘` is a derived limit of the tower `n ↦ K ⊗^𝐋_{𝒪_Y} 𝒪_Y/𝓘ⁿ⁺¹`.
>
> See the module documentation for the proof.

```lean
theorem isDerivedLimit_adicReductionTower_derivedCompletion
    (K : DerivedCategory (_root_.SheafOfModules.{u}
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (Stacks.SheafOfModules.opensRingedSite Y.sheaf).O)))) :
    IsDerivedLimit
      (adicReductionTower (Stacks.SheafOfModules.opensRingedSite Y.sheaf)
        (idealSheafSiteSubmodule 𝓘) K)
      ((derivedCompletion (Stacks.SheafOfModules.opensRingedSite Y.sheaf)
        (idealSheafSiteSubmodule 𝓘)).obj K)
```

**`Stacks.Algebraization.isZero_homology_derivedSections_derivedCompletion_of_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/CoherentCompletionAffineVanishing.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/CoherentCompletionAffineVanishing.lean#L84). The attribute's comment: “part (5), `H^p(U, ℱ^∧) = 0` for `p ≠ 0` and `U ⊂ X` affine open, on the derived completion itself: for a coherent module `ℱ` on a locally Noetherian scheme `X`, which is not required to be quasi-compact, and an arbitrary quasi-coherent sheaf of ideals `𝓘`, the degree-`p` hypercohomology over an affine open `U` of the derived completion `ℱ^∧` of `ℱ` along `𝓘`, an object of `D(𝒪_X)`, vanishes for every integer `p ≠ 0`, negative degrees included. The proof reads `ℱ^∧` as `lim ℱ/𝓘ⁿℱ` in degree zero by part (3) and applies the vanishing on that limit”.

> **Part (5) of [Stacks, Tag 0A0K]: `H^p(U, ℱ^∧) = 0` for `p ≠ 0` and `U ⊂ X` affine open.** Let
> `X` be a locally Noetherian scheme — not assumed quasi-compact — let `𝓘 ⊂ 𝒪_X` be an arbitrary
> quasi-coherent sheaf of ideals and let `ℱ` be a coherent `𝒪_X`-module. Then for every affine open
> `U ⊂ X` and every integer `p ≠ 0` the degree-`p` hypercohomology over `U` of the derived
> completion `ℱ^∧` of `ℱ` along `𝓘`, an object of `D(𝒪_X)`, vanishes.
>
> Part (3) (`Stacks.Algebraization.isIso_comparisonDerivedCompletionLimitAdicQuotient`) identifies
> `ℱ^∧` with `(lim ℱ/𝓘ⁿℱ)[0]`; below degree zero the vanishing is left t-exactness of `RΓ(U, -)`,
> and above it is the vanishing of the higher cohomology of `lim ℱ/𝓘ⁿℱ` over an affine open,
> `Stacks.Algebraization.isZero_cohomology_limit_powerQuotients_of_isAffineOpen`.

```lean
theorem isZero_homology_derivedSections_derivedCompletion_of_isAffineOpen
    {X : Scheme.{u}} [IsLocallyNoetherian X] (I : X.IdealSheafData) (ℱ : X.Modules)
    [ℱ.IsCoherent] (U : X.affineOpens) (p : ℤ) (hp : p ≠ 0) :
    IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} Γ(X, U.1)) p).obj
      ((derivedSections (structureSheafRing X.toRingedSpace) U.1).obj
        ((AlgebraicGeometry.RingedSite.derivedCompletion (opensRingedSite X.sheaf)
            (idealSheafSiteSubmodule I)).obj
          ((DerivedCategory.singleFunctor X.Modules 0).obj ℱ))))
```

**`Stacks.Algebraization.nonempty_iso_completion_limit_adicQuotientSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/KoszulAdicCompletionLimit.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/KoszulAdicCompletionLimit.lean#L308). The attribute's comment: “part (3), `ℱ^∧ = lim ℱ/𝓘ⁿℱ` with an ordinary limit: for a coherent module `ℱ` on a quasi-compact locally Noetherian scheme `Y` and the quasi-coherent sheaf of ideals `𝓘` generated by global sections `f_1, …, f_r` of `𝒪_Y`, the derived completion `ℱ^∧` along `𝓘` is isomorphic in `D(𝒪_Y)` to the ordinary inverse limit of the adic quotients `ℱ/𝓘ⁿℱ`, placed in degree zero. The ideal sheaf is the extension to `Y` of the ideal those global sections span, so its generation by them is a definition and not a hypothesis, and every ideal sheaf so generated equals it. The isomorphism is non-canonical because a derived limit is, which is the form [Stacks, Tag 0H9L] takes”.

> **Stacks Project, Tag 0A0K, part (3).** Let `Y` be a quasi-compact locally Noetherian scheme,
> let `ℐ ⊂ 𝒪_Y` be a quasi-coherent sheaf of ideals generated by the global sections
> `f_1, …, f_r`, and let `ℱ` be a coherent `𝒪_Y`-module. Then the derived completion `ℱ^∧` of `ℱ`
> along `ℐ` is isomorphic, in `D(𝒪_Y)`, to the **ordinary** inverse limit `lim ℱ/ℐⁿℱ` of the adic
> quotients, placed in degree zero.
>
> `R lim` is a predicate rather than a functor here, and a derived limit is unique only up to a
> non-canonical isomorphism, which is why the conclusion is `Nonempty` of an isomorphism — exactly as
> in [Stacks, Tag 0H9L], `_root_.Rlim.Pro.nonempty_iso_of_isDerivedLimit_of_pro_isomorphism`, which
> is the last step of the proof.
>
> The ideal sheaf is not a parameter with a generation hypothesis: it is
> `Stacks.Algebraization.koszulIdealSheafData`, the extension to `Y` of the ideal of global
> functions spanned by `f_1, …, f_r`, whose affine components are computed by
> `Stacks.Algebraization.koszulIdealSheafData_ideal`. Nothing is lost by fixing it, because an
> `IdealSheafData` is determined by its affine components and so every ideal sheaf generated by
> those sections equals this one, which is
> `Stacks.Algebraization.eq_koszulIdealSheafData`.
>
> `[CompactSpace Y]` is a genuine hypothesis and not an artefact: the Artin–Rees level behind the
> pro-vanishing of the Koszul cohomology sheaves below the top degree is produced one per member of
> an affine cover, and the proof takes the maximum over a *finite* cover. See the section "The
> hypotheses, and what they are for" of this file. The source asks neither for quasi-compactness
> nor for `ℐ` to be globally generated; the module documentation of
> `Completion/AdicQuotientDerivedLimit.lean` records what a proof at the source's own hypotheses
> would take, namely a canonical comparison, which is what this route does not produce.

```lean
theorem nonempty_iso_completion_limit_adicQuotientSystem :
    Nonempty
      ((RingedSite.completionFunctor (Stacks.SheafOfModules.opensRingedSite Y.sheaf) f).obj
          (DerivedCategory.Q.obj (RingedSite.singleSheafComplex
            (Stacks.SheafOfModules.opensRingedSite Y.sheaf) ℱ)) ≅
        (DerivedCategory.singleFunctor Y.Modules 0).obj
          (limit (adicQuotientSystem (koszulIdealSheafData Y f) ℱ)))
```

**`Stacks.Algebraization.isDerivedLimit_derivedTensor_adicQuotientSystem_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/KoszulAdicDerivedTensorLimit.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/KoszulAdicDerivedTensorLimit.lean#L216). The attribute's comment: “part (1), `K^∧ = R lim (K ⊗^𝐋_𝒪 𝒪/𝓘ⁿ)`: for an **arbitrary** object `K` of `D(𝒪_Y)` on a quasi-compact locally Noetherian scheme `Y` and the quasi-coherent sheaf of ideals `𝓘` generated by global sections `f_1, …, f_r` of `𝒪_Y`, the derived completion `K^∧` along `𝓘` is a derived limit of the tower `n ↦ K ⊗^𝐋_{𝒪_Y} 𝒪_Y/𝓘ⁿ`. `R lim` is a predicate rather than a functor, so the source's equality is read as `K^∧` being a derived limit of that tower, which is the same reading the tag's part (4) is registered with. The ideal sheaf is the extension to `Y` of the ideal those global sections span, so its generation by them is a definition and not a hypothesis, and every ideal sheaf so generated equals it. The object `K` carries no hypothesis”.

> **Stacks Project, Tag 0A0K, part (1).** Let `Y` be a quasi-compact locally Noetherian scheme,
> let `ℐ ⊂ 𝒪_Y` be the quasi-coherent sheaf of ideals generated by the global sections
> `f_1, …, f_r`, and let `K` be an arbitrary object of `D(𝒪_Y)`. Then the derived completion `K^∧`
> of `K` along `ℐ` is a derived limit of the tower `n ↦ K ⊗^𝐋_{𝒪_Y} 𝒪_Y/ℐⁿ`:
>
> `K^∧ = R lim (K ⊗^𝐋_{𝒪_Y} 𝒪_Y/ℐⁿ)`.
>
> `R lim` is a predicate rather than a functor here, exactly as in the tag's part (4)
> `Stacks.Algebraization.isDerivedLimit_single_limit_powerQuotients`, so the source's equality is
> read as the object `K^∧` being a derived limit of the tower; no comparison map has to be
> produced, and nothing is weakened by that reading.
>
> The proof is [Stacks, Tag 0A0E] — `K^∧` is a derived limit of `n ↦ K ⊗^𝐋 (K^n)^∨` — together
> with the pro-isomorphism of the dual Koszul tower with `n ↦ 𝒪/ℐⁿ`, whiskered by `K ⊗^𝐋 -`. The
> coefficient object enters both towers as that same whiskering functor, so the two meet with no
> constraint of the derived tensor product used.
>
> `[CompactSpace Y]` is a genuine hypothesis of this route and not an artefact: the Artin–Rees
> level behind the pro-vanishing of the Koszul cohomology sheaves below the top degree is produced
> one per member of an affine cover and the proof maximises over a *finite* cover. See the section
> "The hypotheses, and what they are for" of this file. The source asks neither for
> quasi-compactness nor for `ℐ` to be globally generated; `Completion/AdicQuotientDerivedLimit.lean`
> records what a proof at the source's own hypotheses would take.

```lean
theorem isDerivedLimit_derivedTensor_adicQuotientSystem_completion
    (K : DerivedCategory Y.Modules) :
    IsDerivedLimit
      ((adicQuotientSystem (koszulIdealSheafData Y f)
            (SheafOfModules.unit
              (Stacks.SheafOfModules.Tensor.ringSheaf
                (Stacks.SheafOfModules.opensRingedSite Y.sheaf).O)) ⋙
          DerivedCategory.singleFunctor Y.Modules 0) ⋙
        (Stacks.SheafOfModules.canonicalDerivedTensorProduct
          (Stacks.SheafOfModules.opensRingedSite Y.sheaf)).tensor.obj K)
      ((RingedSite.completionFunctor
        (Stacks.SheafOfModules.opensRingedSite Y.sheaf) f).obj K)
```

## Tag 0A0M, a lemma

[Tag 0A0M](https://stacks.math.columbia.edu/tag/0A0M) in the Stacks Project.

**`Stacks.Algebraization.exists_shortExact_adicCompletion_cohomology_whole`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/GeneralCohomologyAdicCompletion.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/GeneralCohomologyAdicCompletion.lean#L301). The attribute's comment: “the whole lemma, at the source's own hypotheses — `A` Noetherian, `I ⊆ A` an ideal, `f : X ⟶ Spec A` a Noetherian scheme over `A` and `ℱ` a coherent `𝒪_X`-module with every `H^p(X, ℱ)` finite over `A`: for every `p` the short exact sequence of `A`-modules `0 → R¹lim H^{p-1}(X, ℱ/𝓘ⁿℱ) → H^p(X,ℱ)^∧ → lim H^p(X, ℱ/𝓘ⁿℱ) → 0` whose middle term is the I-adic completion of the A-module H^p(X,ℱ), together with the vanishing of the R¹lim term for a proper f. The ideal is arbitrary: the identification of the middle term is the identity `RΓ(X,ℱ)^∧ = RΓ(X, lim ℱ/𝓘ⁿℱ)` of [Stacks, Tag 0BLX], got from the Koszul identity of that tag at the ideal sheaf generated by the images of a generating family of I — which a Noetherian A provides — and part (3) of [Stacks, Tag 0A0K]. The properness clause is the Mittag-Leffler condition of [Stacks, Tag 02OB], discharged from [Stacks, Tag 02O8]. The reflector onto the derived-complete objects of D(A) is produced in the proof out of [Stacks, Tag 0920]”.

> **Stacks Project, Tag 0A0M.** Let `A` be a Noetherian ring, `I ⊆ A` an ideal,
> `f : X ⟶ Spec A` a Noetherian scheme over `A` and `ℱ` a coherent `𝒪_X`-module whose cohomology
> modules `H^p(X, ℱ)` are finite over `A` — the hypotheses of the source, and nothing else. Write
> `𝓘 = I · 𝒪_X`. Then for every `p`:
>
> * the `I`-adic completion of the `A`-module `H^p(X, ℱ)` sits in a short exact sequence of
>   `A`-modules
>
>   `0 ⟶ R¹lim H^{p-1}(X, ℱ/𝓘ⁿℱ) ⟶ H^p(X, ℱ)^∧ ⟶ lim H^p(X, ℱ/𝓘ⁿℱ) ⟶ 0`,
>
>   whose left term is the cokernel of `1 - shift` on the product of the degree-`(p-1)` cohomology
>   tower and whose right term is the inverse limit of the degree-`p` cohomology tower; and
> * **if `f` is proper the `R¹lim` term is zero**.
>
> Both are the source's own assertions, at the source's own hypotheses, with nothing assumed. The
> sequence is `Stacks.Algebraization.exists_shortExact_adicCompletion_cohomology`, whose single
> input — the identification `RΓ(X, ℱ)^∧ ≅ RΓ(X, lim ℱ/𝓘ⁿℱ)` of [Stacks, Tag 0BLX] — is supplied
> by `Stacks.Algebraization.hBLX_baseIdealSheaf`: `A` being Noetherian, `I = (a_1, …, a_r)`, and
> `I · 𝒪_X` is then the ideal sheaf generated by the global sections `ρ a_i`, where the Koszul
> identity of [Stacks, Tag 0BLX] and part (3) of [Stacks, Tag 0A0K] are both available. The
> properness clause is
> `Stacks.Algebraization.isZero_firstDerivedLimit_cohomology_adicQuotients_of_isProper_int`, which
> rests on the Mittag-Leffler condition of [Stacks, Tag 02OB] and through it on the proper mapping
> theorem [Stacks, Tag 02O5].
>
> Derived `I`-adic completion is never introduced as data: a reflector onto the derived-complete
> objects of `D(A)` exists by [Stacks, Tag 0920] and is produced inside the proof.

```lean
theorem exists_shortExact_adicCompletion_cohomology_whole
    [IsNoetherianRing A] (I : Ideal A) [IsNoetherian X] (F : X.Modules) [F.IsCoherent]
    (hfinite : ∀ p : ℤ, Module.Finite A
      ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) p).obj
        ((derivedGlobalSectionsOver f).obj
          ((DerivedCategory.singleFunctor X.Modules 0).obj F))))
    (p : ℤ) :
    let T : ℕᵒᵖ ⥤ DerivedCategory (ModuleCat.{u} A) :=
      adicQuotientSystem (baseIdealSheaf A I f) F ⋙
        DerivedCategory.singleFunctor X.Modules 0 ⋙ derivedGlobalSectionsOver f
    let H : ℤ → DerivedCategory (ModuleCat.{u} A) ⥤ ModuleCat.{u} A := fun q ↦
      DerivedCategory.homologyFunctor (ModuleCat.{u} A) q
    (∃ (i : CompletionSequences.firstDerivedLimit A (T ⋙ H (p - 1)) ⟶
        ModuleCat.of A (AdicCompletion I
          ((H p).obj ((derivedGlobalSectionsOver f).obj
            ((DerivedCategory.singleFunctor X.Modules 0).obj F)))))
      (q : ModuleCat.of A (AdicCompletion I
          ((H p).obj ((derivedGlobalSectionsOver f).obj
            ((DerivedCategory.singleFunctor X.Modules 0).obj F)))) ⟶
        limit (T ⋙ H p))
      (w : i ≫ q = 0),
      (ShortComplex.mk i q w).ShortExact) ∧
    (AlgebraicGeometry.IsProper f →
      IsZero (CompletionSequences.firstDerivedLimit A (T ⋙ H (p - 1))))
```

## Tag 0AKL, a remark

[Tag 0AKL](https://stacks.math.columbia.edu/tag/0AKL) in the Stacks Project.

**`AlgebraicGeometry.Stack.isIso_derivedCompletionPushforwardComparison_of_isAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionAlgebraicStacks.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionAlgebraicStacks.lean#L194). The attribute's comment: “the mathematical content of Remark 52.7.4, which is its fifth and last sentence: the analogue of Equation 52.7.0.1 of [Stacks, Tag 0A0I] for complexes of quasi-coherent modules, [HL-P, Theorem 6.5], here for a 1-morphism `f : 𝒳 ⟶ 𝒴` of **algebraic stacks** over `S`. For the morphism of ringed topoi `(Sh(𝒳_τ), 𝒪_𝒳) ⟶ (Sh(𝒴_τ), 𝒪_𝒴)` that `f` induces, at any topology `τ` coarser than the fppf one, a sheaf of ideals `ℐ ⊂ 𝒪_𝒴` of finite type and `ℐ' = f^{-1}ℐ · 𝒪_𝒳`, the canonical comparison map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` is invertible for **every** object `K` of `D(𝒪_𝒳)`, so in particular for every complex of quasi-coherent modules, and every quasi-coherent sheaf of ideals of finite type is an admissible `ℐ`. The proof is [Stacks, Tag 0A0G] for an arbitrary morphism of ringed topoi, `AlgebraicGeometry.RingedToposHom.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType`, at the morphism of ringed topoi of [Stacks, Tag 06TW], `AlgebraicGeometry.Stack.fullRingedToposHom`; it holds for every 1-morphism of categories fibred in groupoids over the big fppf site, `AlgebraicGeometry.Stack.isIso_derivedCompletionPushforwardComparison_fullRingedToposHom`. The stacks have objects and morphisms in `Type (u + 1)` and the structure sheaves sections in `Type (u + 1)`, the seating at which the library's derived completion on a ringed topos is defined. The remark's first four sentences are bibliography — pointers to [lurie-thesis, Theorem 6.3.1] for a derived formal functions theorem for proper maps, to [dag12, Chapter 4] with the cross-reference to More on Algebra, Section 091N for the affine story, and to [G-R, Section 2.9] for proper base change and derived completion via (ind) coherent modules — and carry no formalizable statement. [HL-P, Theorem 6.5] is also stated for morphisms of **derived** algebraic stacks; derived algebraic stacks are not defined in this library, so that part of the reference's setting is outside it”.

> **The analogue of [Stacks, Tag 0A0I] for morphisms of algebraic stacks, [HL-P, Theorem 6.5],
> which is the content of the last sentence of [Stacks, Tag 0AKL].** Let `f : 𝒳 ⟶ 𝒴` be a
> 1-morphism of algebraic stacks over `S`, let `τ` be a topology coarser than the fppf one (any of
> the Zariski, étale, smooth, syntomic and fppf topologies), and consider the morphism of ringed
> topoi `(Sh(𝒳_τ), 𝒪_𝒳) ⟶ (Sh(𝒴_τ), 𝒪_𝒴)` that `f` induces (Stacks 06TW). Let `ℐ ⊂ 𝒪_𝒴` be a sheaf
> of ideals of finite type and let `ℐ' = f^{-1}ℐ · 𝒪_𝒳`. Then the canonical comparison map
>
> `(Rf_*K)^∧ ⟶ Rf_*(K^∧)`
>
> is invertible for every object `K` of `D(𝒪_𝒳)`, the completion on `𝒴` being taken along `ℐ` and
> the one on `𝒳` along `ℐ'`. In particular `Rf_*(ℱ^∧) = (Rf_*ℱ)^∧` for every complex of
> quasi-coherent `𝒪_𝒳`-modules `ℱ`, which is the form in which the remark states it, and every
> quasi-coherent sheaf of ideals of finite type is an admissible `ℐ`.
>
> The ideal `ℐ'` is `AlgebraicGeometry.RingedToposHom.inverseImageIdealSheaf`, the sheaf of ideals
> generated by `f^♯(f^{-1}ℐ)`; the relation between `ℐ` and `ℐ'` that the comparison map needs, and
> finite type of `ℐ'`, are theorems about that construction. The two algebraic stacks are taken
> with objects and morphisms in `Type (u + 1)` and the structure sheaves with sections in
> `Type (u + 1)`; see the module documentation for why.
>
> It is `AlgebraicGeometry.Stack.isIso_derivedCompletionPushforwardComparison_fullRingedToposHom`,
> which needs only that `𝒳` and `𝒴` are fibred in groupoids — the first clause of
> `AlgebraicGeometry.Stack.IsAlgebraicStack`.

```lean
theorem isIso_derivedCompletionPushforwardComparison_of_isAlgebraicStack
    {𝒳 𝒴 : BasedCategory.{u + 1, u + 1} (BigFppfOver B S hS)}
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳) (h𝒴 : IsAlgebraicStack.{u, w} B S hS 𝒴)
    (f : 𝒳 ⥤ᵇ 𝒴)
    (I : SheafOfModules.Submodule (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf
      (fullRingedTopos.{u, u + 1, u + 1} B S hS 𝒴.p τ
        (liftedStructureSheaf.{u, u + 1, u + 1} B S hS 𝒴.p τ h𝒴.fst hτ)).toRingedSite.O)))
    [I.toSheafOfModules.IsFiniteType]
    (K : letI := HasDerivedCategory.standard; DerivedCategory (SheafOfModules.{u + 1}
      (Stacks.SheafOfModules.Tensor.ringSheaf
        (fullRingedTopos.{u, u + 1, u + 1} B S hS 𝒳.p τ
          (liftedStructureSheaf.{u, u + 1, u + 1} B S hS 𝒳.p τ h𝒳.fst hτ)).toRingedSite.O))) :
    IsIso ((RingedToposHom.derivedCompletionPushforwardComparison
      (fullRingedToposHom B S hS 𝒳.p 𝒴.p f.toFunctor h𝒳.fst h𝒴.fst τ hτ
        (.of_isFiberedInGroupoids h𝒴.fst f.w)) I
      (RingedToposHom.inverseImageIdealSheaf.{u + 1}
        (fullRingedToposHom B S hS 𝒳.p 𝒴.p f.toFunctor h𝒳.fst h𝒴.fst τ hτ
          (.of_isFiberedInGroupoids h𝒴.fst f.w)) I)
      (RingedToposHom.idealCompatible_inverseImageIdealSheaf.{u + 1}
        (fullRingedToposHom B S hS 𝒳.p 𝒴.p f.toFunctor h𝒳.fst h𝒴.fst τ hτ
          (.of_isFiberedInGroupoids h𝒴.fst f.w)) I)).app K)
```

**`AlgebraicGeometry.Scheme.isIso_derivedCompletionPushforwardComparison_of_isFiniteType_of_isDerivedComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionFiniteType.lean, line 333](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionFiniteType.lean#L333). The attribute's comment: “the mathematical content of Remark 52.7.4, which is its fifth and last sentence: the analogue of Equation 52.7.0.1 for complexes of quasi-coherent modules, [HL-P, Theorem 6.5]. What is proved here is that analogue at a morphism of **schemes**, at the source's own data — two sheaves of ideals of finite type, `ℐ ⊆ 𝒪_S` and `ℐ' ⊆ 𝒪_X` with `f^♯(f^{-1}ℐ) ⊆ ℐ'` — for every object of `D(𝒪_X)` derived complete along `ℐ'`, hence for every complex of quasi-coherent modules derived complete along `ℐ'`, with both derived completion functors produced from the finite-type hypotheses by [Stacks, Tag 099F]. The remark's first four sentences are bibliography — pointers to [lurie-thesis, Theorem 6.3.1] for a derived formal functions theorem for proper maps, to [dag12, Chapter 4] with the cross-reference to More on Algebra, Section 091N for the affine story, and to [G-R, Section 2.9] for proper base change and derived completion via (ind) coherent modules — and carry no formalizable statement. At a morphism of algebraic stacks the analogue is `AlgebraicGeometry.Stack.isIso_derivedCompletionPushforwardComparison_of_isAlgebraicStack`; derived algebraic stacks, the other half of the setting of [HL-P, Theorem 6.5], are not defined in this library”.

> **Equation 52.7.0.1 of [Stacks, Tag 0A0I] in the display's own setting and at the source's
> own data, for a derived-complete object.** Let `f : X ⟶ S` be a morphism of schemes, let
> `ℐ ⊆ 𝒪_S` be a sheaf of ideals of finite type and let `ℐ' ⊆ 𝒪_X` be a sheaf of ideals of finite
> type with `f^♯(f^{-1}ℐ) ⊆ ℐ'` — which the display's `f^{-1}ℐ · 𝒪_X` is. Then
> `(Rf_*ℱ)^∧ ⟶ Rf_*(ℱ^∧)` is invertible for every `ℱ ∈ D(𝒪_X)` derived complete along `ℐ'`.
>
> This is the display at the hypotheses Section 52.7 writes it under. The source asks `ℐ` to be a
> quasi-coherent sheaf of ideals of finite type and `ℱ` to be quasi-coherent, and uses those
> hypotheses only through [Stacks, Tag 099F], to know the two derived completion functors exist;
> here finite type alone produces them, by
> `Stacks.RingedSpace.isRightAdjoint_ι_isDerivedComplete_of_isFiniteType`, so quasi-coherence is
> not needed and the statement applies in particular to every quasi-coherent `ℐ` of finite type
> and every complex of quasi-coherent modules derived complete along `ℐ'`.
>
> Because `ℱ` ranges over all the objects of `D(𝒪_X)` derived complete along `ℐ'`, this is also
> the analogue of the display *for complexes of quasi-coherent modules* that the fifth and last
> sentence of [Stacks, Tag 0AKL] attributes to [HL-P, Theorem 6.5], at a morphism of schemes. At
> a morphism of algebraic stacks, for an arbitrary object, that analogue is
> `AlgebraicGeometry.Stack.isIso_derivedCompletionPushforwardComparison_of_isAlgebraicStack` of
> `PushforwardCommutesCompletionAlgebraicStacks.lean`; derived algebraic stacks, the other half of
> the setting of that reference, are not defined in this library.
>
> The restriction to a derived-complete `ℱ` is on the object, not on the data: the invertibility
> for an arbitrary `ℱ` is the assertion of [Stacks, Tag 0A0G], and it is proved — at a morphism of
> ringed *sites* and at the constructed `ℐ' = f^{-1}ℐ · 𝒪_X` rather than at an independent
> parameter `ℐ'` — by
> `RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType`,
> and at a morphism of schemes and a quasi-coherent `ℐ` of finite type by
> `Scheme.isIso_derivedCompletionPushforwardComparison_idealSheafData_inverseImageIdealSheaf`.

```lean
theorem isIso_derivedCompletionPushforwardComparison_of_isFiniteType_of_isDerivedComplete
    [I.toSheafOfModules.IsFiniteType] [I'.toSheafOfModules.IsFiniteType]
    {K : DerivedCategory (_root_.SheafOfModules.{u}
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (Stacks.RingedSpace.toRingedSite X.toRingedSpace).O)))}
    (hK : RingedSite.IsDerivedComplete.{u, u, u, u}
      (Stacks.RingedSpace.toRingedSite X.toRingedSpace) I' K) :
    IsIso ((RingedSite.derivedCompletionPushforwardComparison
      (toRingedSiteHom f) I I' hI).app K)
```

**`AlgebraicGeometry.Scheme.isIso_derivedCompletionPushforwardComparison_idealSheafData_of_isDerivedComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionFiniteType.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionFiniteType.lean#L424). The attribute's comment: “the mathematical content of Remark 52.7.4, which is its fifth and last sentence: the analogue of Equation 52.7.0.1 for complexes of quasi-coherent modules, [HL-P, Theorem 6.5]. What is proved here is that analogue at a morphism of **schemes** and at Section 52.7's own data — two **quasi-coherent** sheaves of ideals **of finite type**, `ℐ ⊆ 𝒪_S` and `ℐ' ⊆ 𝒪_X` with `f^♯(f^{-1}ℐ) ⊆ ℐ'` — for every object of `D(𝒪_X)` derived complete along `ℐ'`, hence for every complex of quasi-coherent modules derived complete along `ℐ'`. Both derived completion functors are produced from the finite-type hypothesis by [Stacks, Tag 099F]. The remark's first four sentences are bibliography — pointers to [lurie-thesis, Theorem 6.3.1] for a derived formal functions theorem for proper maps, to [dag12, Chapter 4] with the cross-reference to More on Algebra, Section 091N for the affine story, and to [G-R, Section 2.9] for proper base change and derived completion via (ind) coherent modules — and carry no formalizable statement. At a morphism of algebraic stacks the analogue is `AlgebraicGeometry.Stack.isIso_derivedCompletionPushforwardComparison_of_isAlgebraicStack`; derived algebraic stacks, the other half of the setting of [HL-P, Theorem 6.5], are not defined in this library”.

> **Equation 52.7.0.1 of [Stacks, Tag 0A0I] at Section 52.7's own data, for a derived-complete
> object.** Let `f : X ⟶ S` be a morphism of schemes, let `ℐ ⊆ 𝒪_S` be a quasi-coherent sheaf of
> ideals of finite type and let `ℐ' ⊆ 𝒪_X` be a quasi-coherent sheaf of ideals of finite type with
> `f^♯(f^{-1}ℐ) ⊆ ℐ'` — which the display's `f^{-1}ℐ · 𝒪_X` is. Then `(Rf_*ℱ)^∧ ⟶ Rf_*(ℱ^∧)` is
> invertible for every `ℱ ∈ D(𝒪_X)` derived complete along `ℐ'`, in particular for every such
> complex of quasi-coherent modules.
>
> This is the display written at the hypotheses Section 52.7 states it under, in the library's own
> scheme-theoretic vocabulary: `ℐ` and `ℐ'` are `AlgebraicGeometry.Scheme.IdealSheafData`, so
> quasi-coherent, and the finite-type hypothesis is `SheafOfModules.IsFiniteType` — locally
> generated by finitely many sections. It is
> `isIso_derivedCompletionPushforwardComparison_of_isFiniteType_of_isDerivedComplete` above at
> those sheaves of ideals, and the only thing the hypotheses are used for is [Stacks, Tag 099F],
> which is what produces the two derived completion functors.
>
> Because `ℱ` ranges over the objects of `D(𝒪_X)` derived complete along `ℐ'` and not over
> quasi-coherent sheaves alone, this is also the analogue of the display *for complexes of
> quasi-coherent modules* that the fifth and last sentence of [Stacks, Tag 0AKL] attributes to
> [HL-P, Theorem 6.5], at a morphism of schemes.
>
> The restriction to a derived-complete `ℱ` is on the object, not on the data: the invertibility
> for an arbitrary `ℱ` is the assertion of [Stacks, Tag 0A0G], and it is proved — at a morphism of
> ringed *sites* and at the constructed `ℐ' = f^{-1}ℐ · 𝒪_X` rather than at an independent
> parameter `ℐ'` — by
> `RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType`,
> and at a morphism of schemes and a quasi-coherent `ℐ` of finite type by
> `Scheme.isIso_derivedCompletionPushforwardComparison_idealSheafData_inverseImageIdealSheaf`.

```lean
theorem isIso_derivedCompletionPushforwardComparison_idealSheafData_of_isDerivedComplete
    [(idealSheafSiteSubmodule I).toSheafOfModules.IsFiniteType]
    [(idealSheafSiteSubmodule I').toSheafOfModules.IsFiniteType]
    {K : DerivedCategory (_root_.SheafOfModules.{u}
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (Stacks.RingedSpace.toRingedSite X.toRingedSpace).O)))}
    (hK : RingedSite.IsDerivedComplete.{u, u, u, u}
      (Stacks.RingedSpace.toRingedSite X.toRingedSpace) (idealSheafSiteSubmodule I') K) :
    IsIso ((RingedSite.derivedCompletionPushforwardComparison
      (toRingedSiteHom f) (idealSheafSiteSubmodule I) (idealSheafSiteSubmodule I') hI).app K)
```

**`AlgebraicGeometry.Scheme.isIso_derivedCompletionPushforwardComparison_idealSheafData_inverseImageIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionFiniteType.lean, line 487](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionFiniteType.lean#L487). The attribute's comment: “the mathematical content of Remark 52.7.4, which is its fifth and last sentence: the analogue of Equation 52.7.0.1 for complexes of quasi-coherent modules, [HL-P, Theorem 6.5]. Proved here at a morphism of **schemes** `f : X ⟶ S` and at Section 52.7's own data — a **quasi-coherent** sheaf of ideals `ℐ ⊆ 𝒪_S` **of finite type** and the sheaf of ideals `ℐ' = f^{-1}ℐ · 𝒪_X` built out of it — for an **arbitrary** object of `D(𝒪_X)`, hence for every complex of quasi-coherent modules, with no derived-completeness or nilpotence restriction: the canonical comparison map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` is invertible. That `f^♯(f^{-1}ℐ) ⊆ ℐ'` and that `ℐ'` is of finite type are theorems about the construction, not hypotheses. The remark's first four sentences are bibliography — pointers to [lurie-thesis, Theorem 6.3.1] for a derived formal functions theorem for proper maps, to [dag12, Chapter 4] with the cross-reference to More on Algebra, Section 091N for the affine story, and to [G-R, Section 2.9] for proper base change and derived completion via (ind) coherent modules — and carry no formalizable statement. At a morphism of algebraic stacks the analogue is `AlgebraicGeometry.Stack.isIso_derivedCompletionPushforwardComparison_of_isAlgebraicStack`; derived algebraic stacks, the other half of the setting of [HL-P, Theorem 6.5], are not defined in this library”.

> **Equation 52.7.0.1 of [Stacks, Tag 0A0I] at Section 52.7's own data, for an arbitrary
> object — and so the analogue for complexes of quasi-coherent modules of [Stacks, Tag 0AKL].** Let
> `f : X ⟶ S` be a morphism of schemes, let `ℐ ⊆ 𝒪_S` be a quasi-coherent sheaf of ideals of finite
> type and let `ℐ' = f^{-1}ℐ · 𝒪_X` be the sheaf of ideals Section 52.7 builds out of it. Then the
> canonical comparison map
>
> `(Rf_*K)^∧ ⟶ Rf_*(K^∧)`
>
> is invertible for **every** object `K` of `D(𝒪_X)`, the completion on `S` being taken along `ℐ`
> and the one on `X` along `ℐ'`. In particular it is invertible for every complex of
> quasi-coherent `𝒪_X`-modules, with no derived-completeness or nilpotence restriction.
>
> `ℐ` is an `AlgebraicGeometry.Scheme.IdealSheafData`, read on the small Zariski ringed site by
> `Stacks.Algebraization.idealSheafSiteSubmodule`, and "of finite type" is
> `SheafOfModules.IsFiniteType` (automatic on a locally Noetherian scheme, by
> `Stacks.Algebraization.isFiniteType_idealSheafSiteSubmodule`). The sheaf of ideals `ℐ'` is
> `AlgebraicGeometry.RingedSite.inverseImageIdealSheaf`, the image of `f^*ℐ ⟶ 𝒪_X`; that `f^♯`
> carries `f^{-1}ℐ` into it is
> `AlgebraicGeometry.RingedSite.pushforwardIdealCompatible_inverseImageIdealSheaf`, and that it is of
> finite type — so that the derived completion along it exists, by [Stacks, Tag 099F] — is
> `AlgebraicGeometry.RingedSite.isFiniteType_inverseImageIdealSheaf`. Neither is a hypothesis.
>
> This is
> `RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType`,
> the ringed-sites case of [Stacks, Tag 0A0G], at the morphism of ringed sites
> `AlgebraicGeometry.Scheme.toRingedSiteHom f` underlying `f`.

```lean
theorem isIso_derivedCompletionPushforwardComparison_idealSheafData_inverseImageIdealSheaf
    [(idealSheafSiteSubmodule I).toSheafOfModules.IsFiniteType]
    (K : DerivedCategory (_root_.SheafOfModules.{u}
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (Stacks.RingedSpace.toRingedSite X.toRingedSpace).O)))) :
    IsIso ((RingedSite.derivedCompletionPushforwardComparison (toRingedSiteHom f)
      (idealSheafSiteSubmodule I)
      (RingedSite.inverseImageIdealSheaf.{u} (toRingedSiteHom f) (idealSheafSiteSubmodule I))
      (RingedSite.pushforwardIdealCompatible_inverseImageIdealSheaf.{u} (toRingedSiteHom f)
        (idealSheafSiteSubmodule I))).app K)
```

**`AlgebraicGeometry.Scheme.isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf_of_isDerivedComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionGenerated.lean, line 430](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionGenerated.lean#L430). The attribute's comment: “the mathematical content of Remark 52.7.4 — its fifth and last sentence, the analogue of Equation 52.7.0.1 for complexes of quasi-coherent modules, [HL-P, Theorem 6.5] — in the second of the two regimes this library reaches for it. Proved here: that analogue at a morphism of **schemes**, for an object of `D(𝒪_X)` that is **derived complete** along `ℐ'`, with `ℐ` and `ℐ'` generated by finitely many global sections of the two structure sheaves, out of which both derived completion functors are built. The objects covered are therefore the derived-complete complexes of quasi-coherent modules, at ideal sheaves on which the only demand is those generators. The same analogue at two sheaves of ideals of finite type, which is the source's own hypothesis on the data, is `AlgebraicGeometry.Scheme``.isIso_derivedCompletionPushforwardComparison_of_isFiniteType_of_isDerivedComplete` of `PushforwardCommutesCompletionFiniteType.lean`, and for an arbitrary complex, at a quasi-coherent `ℐ` of finite type and `ℐ' = f^{-1}ℐ · 𝒪_X`, it is `AlgebraicGeometry.Scheme``.isIso_derivedCompletionPushforwardComparison_idealSheafData_inverseImageIdealSheaf` of the same file. At a morphism of algebraic stacks the analogue is `AlgebraicGeometry.Stack.isIso_derivedCompletionPushforwardComparison_of_isAlgebraicStack` of `PushforwardCommutesCompletionAlgebraicStacks.lean`; derived algebraic stacks, the other half of the setting of [HL-P, Theorem 6.5], are not defined in this library. The remark's first four sentences are bibliography — pointers to [lurie-thesis, Theorem 6.3.1] for a derived formal functions theorem for proper maps, to [dag12, Chapter 4] with the cross-reference to More on Algebra, Section 091N for the affine story, and to [G-R, Section 2.9] for proper base change and derived completion via (ind) coherent modules — and carry no formalizable statement. A further registration, which takes an **arbitrary** object in the regime where the local sections of both ideal sheaves are nilpotent, is in `PushforwardCommutesCompletionSpaces.lean`”.

> **[Stacks, Tag 0A0I] in the display's own setting, for a derived-complete object, with
> nothing assumed.** Let `f : X ⟶ S` be a morphism of schemes, let `ℐ = (t_1, …, t_s) ⊆ 𝒪_S` and
> `ℐ' = (g_1, …, g_r) ⊆ 𝒪_X` be the sheaves of ideals generated by finitely many global sections
> of the two structure sheaves, with `f^♯(f^{-1}ℐ) ⊆ ℐ'` — which the display's `f^{-1}ℐ · 𝒪_X`
> satisfies. Then `(Rf_*ℱ)^∧ ⟶ Rf_*(ℱ^∧)` is invertible for every `ℱ ∈ D(𝒪_X)` derived complete
> along `ℐ'`.
>
> Both derived completion functors are produced from the generators, by
> `AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete_generatedIdealSheaf`, so
> [Stacks, Tag 099F] is nowhere a hypothesis; neither quasi-coherence nor finite type nor
> quasi-coherence of `ℱ` is assumed either, those entering the source only through that tag. The
> restriction to a derived-complete `ℱ` is the tag's own content and remains; the invertibility
> for an arbitrary `ℱ` is the assertion of [Stacks, Tag 0A0G]. The descent from a globally
> generated `ℐ` to a finite-type one is carried out in
> `PushforwardCommutesCompletionFiniteType.lean`, where the derived completion functors come from
> [Stacks, Tag 099F] at a sheaf of ideals of finite type; this statement is the case of
> `AlgebraicGeometry.Scheme`
> `.isIso_derivedCompletionPushforwardComparison_of_isFiniteType_of_isDerivedComplete` there in
> which the two sheaves of ideals are generated by global sections.
>
> Because `ℱ` ranges over the derived-complete objects of `D(𝒪_X)` and not over quasi-coherent
> sheaves alone, this is also the analogue of the display *for complexes of quasi-coherent
> modules* that the fifth and last sentence of [Stacks, Tag 0AKL] attributes to
> [HL-P, Theorem 6.5]; related statements are
> `isIso_derivedCompletionPushforwardComparison_of_isFiniteType_of_isDerivedComplete` of
> `PushforwardCommutesCompletionFiniteType.lean`, the same statement at two sheaves of ideals of
> finite type, and
> `AlgebraicGeometry.Scheme.isIso_derivedCompletionPushforwardComparison_of_forall_isNilpotent` of
> `PushforwardCommutesCompletionSpaces.lean`, which takes an arbitrary object in the nilpotent
> regime and whose module documentation accounts for the remark sentence by sentence.

```lean
theorem isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf_of_isDerivedComplete
    {K : DerivedCategory (_root_.SheafOfModules.{u}
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (Stacks.RingedSpace.toRingedSite X.toRingedSpace).O)))}
    (hK : RingedSite.IsDerivedComplete.{u, u, u, u}
      (Stacks.RingedSpace.toRingedSite X.toRingedSpace) (generatedIdealSheaf g) K) :
    IsIso ((RingedSite.derivedCompletionPushforwardComparison (toRingedSiteHom f)
      (generatedIdealSheaf t) (generatedIdealSheaf g) hI).app K)
```

**`AlgebraicGeometry.Scheme.isIso_derivedCompletionPushforwardComparison_of_forall_isNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionSpaces.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionSpaces.lean#L394). The attribute's comment: “the mathematical content of Remark 52.7.4, which is its fifth and last sentence: the analogue of Equation 52.7.0.1 for complexes of quasi-coherent modules, [HL-P, Theorem 6.5]. What is proved here is that analogue at a morphism of **schemes** for an **arbitrary** object of `D(𝒪_X)`, hence for an arbitrary complex of quasi-coherent modules, in the regime where the local sections of both sheaves of ideals are nilpotent — the regime in which this library builds the two derived completion functors out of the data, which is why this statement has no instance argument. The same analogue at the source's own data, two sheaves of ideals of finite type, is `AlgebraicGeometry.Scheme` `.isIso_derivedCompletionPushforwardComparison_of_isFiniteType_of_isDerivedComplete` of `PushforwardCommutesCompletionFiniteType.lean`, for a complex derived complete along `ℐ'`. An arbitrary complex at a quasi-coherent sheaf of ideals of finite type and `ℐ' = f^{-1}ℐ · 𝒪_X` is `AlgebraicGeometry.Scheme` `.isIso_derivedCompletionPushforwardComparison_idealSheafData_inverseImageIdealSheaf` of `PushforwardCommutesCompletionFiniteType.lean`. At a morphism of algebraic stacks it is `AlgebraicGeometry.Stack.isIso_derivedCompletionPushforwardComparison_of_isAlgebraicStack` of `PushforwardCommutesCompletionAlgebraicStacks.lean`; derived algebraic stacks, the other half of the setting of [HL-P, Theorem 6.5], are not defined in this library. The remark's first four sentences are bibliography — pointers to [lurie-thesis, Theorem 6.3.1] for a derived formal functions theorem for proper maps, to [dag12, Chapter 4] with the cross-reference to More on Algebra, Section 091N for the affine story, and to [G-R, Section 2.9] for proper base change and derived completion via (ind) coherent modules — and carry no formalizable statement. A third registration, at a derived-complete object and ideal sheaves generated by finitely many global sections, is in `PushforwardCommutesCompletionGenerated.lean`”.

> **Equation 52.7.0.1 of [Stacks, Tag 0A0I] in the display's own setting, for an arbitrary
> object**, when the local sections of `ℐ` and of `ℐ'` are nilpotent: the comparison
> `(Rf_*ℱ)^∧ ⟶ Rf_*(ℱ^∧)` is invertible for every `ℱ ∈ D(𝒪_X)`, in particular for every
> quasi-coherent `ℱ`, with no hypothesis on `ℱ`.
>
> The restriction is on the two sheaves of ideals, not on `ℱ`, and it *discharges* the conclusion
> of [Stacks, Tag 099F] on `X` and on `S` rather than assuming it: this statement has no instance
> hypothesis. It is not the general case of the display — nilpotence is not the source's
> hypothesis, and in that regime both derived completion functors are the identity. The display at
> the source's own data, two sheaves of ideals of finite type, is `AlgebraicGeometry.Scheme`
> `.isIso_derivedCompletionPushforwardComparison_of_isFiniteType_of_isDerivedComplete` of
> `PushforwardCommutesCompletionFiniteType.lean`, for an object derived complete along `ℐ'`.
> An arbitrary object, at a quasi-coherent sheaf of ideals `ℐ` of finite type and
> `ℐ' = f^{-1}ℐ · 𝒪_X`, is
> `Scheme.isIso_derivedCompletionPushforwardComparison_idealSheafData_inverseImageIdealSheaf` of
> the same file.
>
> Because `ℱ` ranges over all of `D(𝒪_X)`, this is also the analogue of the display *for complexes
> of quasi-coherent modules* that the fifth and last sentence of [Stacks, Tag 0AKL] attributes to
> [HL-P, Theorem 6.5], in the nilpotent regime. The derived-complete case of that remark is, at two
> sheaves of ideals of finite type, `AlgebraicGeometry.Scheme`
> `.isIso_derivedCompletionPushforwardComparison_of_isFiniteType_of_isDerivedComplete` of
> `PushforwardCommutesCompletionFiniteType.lean`, and at ideal sheaves generated by finitely many
> global sections, `AlgebraicGeometry.Scheme`
> `.isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf_of_isDerivedComplete` of
> `PushforwardCommutesCompletionGenerated.lean`.

```lean
theorem isIso_derivedCompletionPushforwardComparison_of_forall_isNilpotent
    (hnil : ∀ (V : TopologicalSpace.Opens X.toRingedSpace.carrier)
      (g : ((Stacks.SheafOfModules.Tensor.ringSheaf
        (Stacks.RingedSpace.toRingedSite X.toRingedSpace).O)).obj.obj (op V)),
      g ∈ I'.toSubmodule.obj (op V) → IsNilpotent g)
    (hnil' : ∀ (W : TopologicalSpace.Opens S.toRingedSpace.carrier)
      (s : ((Stacks.SheafOfModules.Tensor.ringSheaf
        (Stacks.RingedSpace.toRingedSite S.toRingedSpace).O)).obj.obj (op W)),
      s ∈ I.toSubmodule.obj (op W) → IsNilpotent s)
    (K : DerivedCategory (_root_.SheafOfModules.{u}
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (Stacks.RingedSpace.toRingedSite X.toRingedSpace).O)))) :
    letI : (ObjectProperty.ι (RingedSite.IsDerivedComplete.{u, u, u, u}
        (Stacks.RingedSpace.toRingedSite X.toRingedSpace) I')).IsRightAdjoint :=
      RingedSite.isRightAdjoint_ι_isDerivedComplete_of_forall_isNilpotent
        (Stacks.RingedSpace.toRingedSite X.toRingedSpace) I' hnil
    letI : (ObjectProperty.ι (RingedSite.IsDerivedComplete.{u, u, u, u}
        (Stacks.RingedSpace.toRingedSite S.toRingedSpace) I)).IsRightAdjoint :=
      RingedSite.isRightAdjoint_ι_isDerivedComplete_of_forall_isNilpotent
        (Stacks.RingedSpace.toRingedSite S.toRingedSpace) I hnil'
    IsIso ((RingedSite.derivedCompletionPushforwardComparison
      (toRingedSiteHom f) I I' hI).app K)
```

**`AlgebraicGeometry.RingedSite.isDerivedComplete_derivedPushforward_derivedSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCompletionComplete.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCompletionComplete.lean#L113). The attribute's comment: “the mathematical content of the remark, which is its fifth and last sentence: the analogue of the displayed equation (0A0I) for complexes of quasi-coherent modules, [HL-P, Theorem 6.5]. The first four sentences are bibliography and carry no mathematical statement — a pointer to [lurie-thesis, Theorem 6.3.1] for a derived formal functions theorem for proper maps, one to [dag12, Chapter 4] together with the cross-reference to More on Algebra, Section 091N for the affine story, and one to [G-R, Section 2.9] for proper base change and derived completion via (ind) coherent modules. Covered here and in `isDerivedComplete_derivedSheafHom_derivedPushforward`: that both sides of (0A0I) are derived complete, for an arbitrary coefficient object of the derived category of modules, which subsumes the complexes of quasi-coherent modules the sentence speaks of. This is the step of the proof of Tag 0A0G that makes the comparison between the two sides canonical. NOT covered: the comparison isomorphism itself, which cannot be stated while Tag 099B and Tag 099F leave the derived completion without the universal property that pins the map down, nor proved while Tag 0944 and Tag 0A0E are unavailable; and not the setting of (derived) algebraic stacks in which [HL-P, Theorem 6.5] is stated. See the module documentation.”.

> **The pushed-forward completion is derived complete.** Let `f : (Sh(𝒟), 𝒪') ⟶ (Sh(𝒞), 𝒪)` be
> a morphism of ringed sites and let `ℐ ⊂ 𝒪`, `ℐ' ⊂ 𝒪'` be sheaves of ideals such that `f^♯` sends
> `f^{-1}ℐ` into `ℐ'`. If `K` in `D(𝒪')` is derived complete along `ℐ'`, then for every `M` in
> `D(𝒪')` the object `Rf_*(R𝑆heafHom_{𝒪'}(M, K))` is derived complete along `ℐ`.
>
> Taking `M` to be the extended alternating Čech complex of a finite family of global sections
> generating `ℐ'`, so that `R𝑆heafHom_{𝒪'}(M, K)` is the derived completion `K^∧` of
> [Stacks, Tag 099B], this says that the left-hand side `Rf_*(K^∧)` of the displayed equation of
> [Stacks, Tag 0A0I] is derived complete.
>
> [Stacks, Tag 099A] puts `R𝑆heafHom_{𝒪'}(M, K)` in `D_comp(𝒪', ℐ')`, and [Stacks, Tag 099J]
> carries it from there into `D_comp(𝒪, ℐ)`.

```lean
theorem isDerivedComplete_derivedPushforward_derivedSheafHom
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf Y.O))))
    (I' : SheafOfModules.Submodule
      (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hI : ∀ (W : Y.C) (s : ((Stacks.SheafOfModules.Tensor.ringSheaf Y.O)).obj.obj (op W)),
      s ∈ I.toSubmodule.obj (op W) →
        fSharpSection f W s ∈ I'.toSubmodule.obj (op (f.u.obj W)))
    (M K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hK : IsDerivedComplete.{u, u, u, u} X I' K) :
    IsDerivedComplete.{u, u, u, u} Y I
      ((derivedPushforward.{u} f.toRingedToposSiteHom).obj
        (((derivedSheafHomBifunctor X).obj (op M)).obj K))
```

**`AlgebraicGeometry.RingedSite.isDerivedComplete_derivedSheafHom_derivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCompletionComplete.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCompletionComplete.lean#L142). The attribute's comment: “the second half of the covered statement; see `isDerivedComplete_derivedPushforward_derivedSheafHom` for the full accounting of which sentences of the remark carry mathematical content and of what is and is not covered.”.

> **The completion of a pushforward is derived complete.** In the situation of
> `isDerivedComplete_derivedPushforward_derivedSheafHom`, for every `N` in `D(𝒪)` the object
> `R𝑆heafHom_𝒪(N, Rf_*K)` is derived complete along `ℐ`.
>
> Taking `N` to be the extended alternating Čech complex of a finite family of global sections
> generating `ℐ`, this says that the right-hand side `(Rf_*K)^∧` of the displayed equation of
> [Stacks, Tag 0A0I] is derived complete.
>
> The two inputs are used in the opposite order to the companion result: [Stacks, Tag 099J] puts
> `Rf_*K` in `D_comp(𝒪, ℐ)` and [Stacks, Tag 099A] keeps the derived internal Hom into it there.

```lean
theorem isDerivedComplete_derivedSheafHom_derivedPushforward
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf Y.O))))
    (I' : SheafOfModules.Submodule
      (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hI : ∀ (W : Y.C) (s : ((Stacks.SheafOfModules.Tensor.ringSheaf Y.O)).obj.obj (op W)),
      s ∈ I.toSubmodule.obj (op W) →
        fSharpSection f W s ∈ I'.toSubmodule.obj (op (f.u.obj W)))
    (N : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf Y.O))))
    (K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hK : IsDerivedComplete.{u, u, u, u} X I' K) :
    IsDerivedComplete.{u, u, u, u} Y I
      (((derivedSheafHomBifunctor Y).obj (op N)).obj
        ((derivedPushforward.{u} f.toRingedToposSiteHom).obj K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.7, Tag 0A0H](https://stacks.math.columbia.edu/tag/0A0H)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
