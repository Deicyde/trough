---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isFinite_normalization_of_regular_alteration, AlgebraicGeometry.Space.exists_isDenseOpenSubspace_hasEtaleLocalProperty_isRegular, AlgebraicGeometry.Space.NormalizationData.isFinite_hom_of_regular_alteration, AlgebraicGeometry.Space.exists_isRegularRing_localizationAway_of_regular_spaceAlteration, AlgebraicGeometry.Space.module_finite_integralClosure_of_regular_spaceAlteration, AlgebraicGeometry.Space.isNormalRing_adicCompletion_integralClosure_of_regular_spaceAlteration, AlgebraicGeometry.Space.isRegularRing_genericFormalFibre_of_regular_spaceAlteration, AlgebraicGeometry.Space.exists_isRegularRing_localizationAway_of_isAlteration_of_isRegular
statement: formalized
proof: formalized
---

# 89.7 Implied properties

Section 89.7 of the Stacks Project, [Tag 0BHS](https://stacks.math.columbia.edu/tag/0BHS). 2 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BHT, a lemma

[Tag 0BHT](https://stacks.math.columbia.edu/tag/0BHT) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinite_normalization_of_regular_alteration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationFiniteRegularAlteration.lean, line 486](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationFiniteRegularAlteration.lean#L486). The attribute's comment: “finiteness of the normalization. The source's Noetherian hypothesis on Y is used only as quasi-compactness of its point space and local Noetherianity of its etale charts; the quasi-separatedness that Stacks 03EA also asks for is unused, which is a strengthening. Integrality of Y is part of IsAlteration. The source's Step 1 -- etale localization to a Noetherian domain, which charts of an integral space do not permit -- and its appeal to Stacks 08AR are both replaced by Chow's lemma for spaces (Stacks 089J) over an affine chart, which reduces the finiteness to the degree-zero case of Stacks 02O6 for schemes; see the module docstring”.

> **Stacks 0BHT, finiteness of the normalization.** Let `Y` be an integral algebraic space over
> `S` which is quasi-compact and whose étale scheme charts are locally Noetherian, and suppose
> there is an alteration `f : X ⟶ Y` with `X` regular. Then **the** normalization morphism
> `Y^ν ⟶ Y` of `Y` is a finite morphism of algebraic spaces.
>
> The normalization is the constructed one, neither assumed nor existentially quantified: the
> étale scheme charts of `Y` are locally Noetherian, so they satisfy the finiteness condition of
> Stacks 0BB1 by Stacks 0GMB, and `AlgebraicGeometry.Space.normalizationData` is then the
> normalization of `Y`, unique up to a unique isomorphism over `Y` by
> `AlgebraicGeometry.Space.NormalizationData.existsUnique_iso_hom`.

```lean
theorem isFinite_normalization_of_regular_alteration
    (f : X ⟶ Y) (hf : IsAlteration B S hS f)
    (hXreg : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsRegular T))
    (hYqc : IsQuasiCompactSpace B S hS Y)
    (hYnoeth : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T)) :
    IsFinite B S hS (normalizationData B S hS hf.1
      (hasLocallyFiniteIrreducibleComponents_of_isLocallyNoetherian B S hS Y hf.1 hYnoeth)).hom
```

**`AlgebraicGeometry.Space.exists_isDenseOpenSubspace_hasEtaleLocalProperty_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularAlterationImpliedProperties.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RegularAlterationImpliedProperties.lean#L203). The attribute's comment: “the regular dense open; the source's Noetherian hypothesis on Y and the finiteness of f over a nonempty open are unused, only reducedness of Y and properness and dominance of f, which is a strengthening. The source's Stacks 07NG enters as the space-level descent Stacks 06MK, whose engine on local rings is that same statement”.

> **Stacks 0BHT, the dense regular open.** An integral algebraic space `Y` over `S` admitting
> an alteration `f : X ⟶ Y` whose source is regular has a dense open subspace which is regular.

```lean
theorem exists_isDenseOpenSubspace_hasEtaleLocalProperty_isRegular (f : X ⟶ Y)
    (hf : IsAlteration B S hS f)
    (hXreg : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsRegular T)) :
    ∃ V : Subfunctor Y, IsDenseOpenSubspace B S hS hf.1 V ∧
      HasEtaleLocalProperty B S hS V.toFunctor (fun T : Scheme.{u} => IsRegular T)
```

**`AlgebraicGeometry.Space.NormalizationData.isFinite_hom_of_regular_alteration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularAlterationImpliedProperties.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RegularAlterationImpliedProperties.lean#L320). The attribute's comment: “finiteness of the normalization, for a REPRESENTABLE AFFINE target: the source's Step 1, etale localization to a Noetherian domain, is invalid for algebraic spaces -- charts of an integral space are reduced but not irreducible, so Stacks 0BH3 does not apply over them. Conditional on h02O6, the degree-zero case of Stacks 02O6 for algebraic spaces, which this library lacks; see the module docstring”.

> **Stacks 0BHT, finiteness of the normalization**, for a target represented by an affine
> object of the site and conditional on the degree-zero case of Stacks 02O6. Let `Z` be an affine
> object of the site whose scheme is integral and locally Noetherian, let `f : X ⟶ h_Z` be an
> alteration with `X` regular, and let `D` be normalization data for `h_Z`. Then the normalization
> morphism of `D` is finite.

```lean
theorem NormalizationData.isFinite_hom_of_regular_alteration {Z : BigFppfOver B S hS}
    [IsAffine ((BigFppfOver.toScheme B S hS).obj Z)]
    [_root_.AlgebraicGeometry.IsIntegral ((BigFppfOver.toScheme B S hS).obj Z)]
    [IsLocallyNoetherian ((BigFppfOver.toScheme B S hS).obj Z)]
    (f : X ⟶ yoneda.obj Z) (hf : IsAlteration B S hS f)
    (hXreg : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsRegular T))
    (h02O6 : ∃ φ : Γ((BigFppfOver.toScheme B S hS).obj Z, ⊤) →+*
        ↥(RingCat.sectionsSubring
          (structurePresheaf B S hS X ⋙ forget₂ CommRingCat.{u} RingCat.{u})),
      Function.Injective φ ∧ φ.Finite)
    (D : NormalizationData B S hS (yoneda.obj Z)) :
    IsFinite B S hS D.hom
```

## Tag 0BHU, a lemma

[Tag 0BHU](https://stacks.math.columbia.edu/tag/0BHU) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isRegularRing_localizationAway_of_regular_spaceAlteration`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean#L164). The attribute's comment: “clause (1), regular after inverting one element”.

> **A Noetherian local domain admitting an alteration by a regular algebraic space is regular
> after inverting one nonzero element.** The dense regular open of [Stacks, Tag 0BHT] at the
> representable target `Spec A` contains a nonempty basic open `D(a)` of `Spec A`, and
> `Γ(D(a)) = A_a`.

```lean
public alias exists_isRegularRing_localizationAway_of_regular_spaceAlteration
```

**`AlgebraicGeometry.Space.module_finite_integralClosure_of_regular_spaceAlteration`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean#L172). The attribute's comment: “clause (2), finite integral closure”.

> **The integral closure of a Noetherian local domain admitting an alteration by a regular
> algebraic space is a finite module over it.** The normalization of `Spec A` is finite by
> [Stacks, Tag 0BHT], and it is the spectrum of the integral closure of `A` in `Frac(A)`
> ([Stacks, Tag 035P]).

```lean
public alias module_finite_integralClosure_of_regular_spaceAlteration
```

**`AlgebraicGeometry.Space.isNormalRing_adicCompletion_integralClosure_of_regular_spaceAlteration`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean#L182). The attribute's comment: “clause (3), normal completion of the integral closure”.

> **The completion of the integral closure is normal.** With `C = Γ(X, 𝒪_X)` and `B` the
> integral closure of `A` in `Frac(A)`, the inclusion `B ⊆ C` is a map of finite `A`-algebras and
> `B` is a normal domain, so [Stacks, Tag 0BGH] reduces normality of `Bˆ` to normality of
> `Cˆ = Aˆ ⊗_A C`, which is the global functions of the regular base change `X ×_{Spec A} Spec Aˆ`
> ([Stacks, Tag 073K], [Stacks, Tag 0BHQ]). Normality here is `IsNormalRing`, which for a finite
> algebra over a Noetherian local ring is normality of the completions at the maximal ideals.

```lean
public alias isNormalRing_adicCompletion_integralClosure_of_regular_spaceAlteration
```

**`AlgebraicGeometry.Space.isRegularRing_genericFormalFibre_of_regular_spaceAlteration`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean#L191). The attribute's comment: “clause (4), regular generic formal fibre”.

> **The generic formal fibre of a Noetherian local domain admitting an alteration by a regular
> algebraic space is regular.** For an affine étale chart `V` of `X` through the generic point the
> ring `Aˆ ⊗_A Γ(V, 𝒪_V)` is regular by [Stacks, Tag 0BHQ], and the generic formal fibre is
> recovered by inverting `A ∖ {0}` and descending along the faithfully flat `Frac(A)`-algebra
> `Frac(A) ⊗_A Γ(V, 𝒪_V)` by [Stacks, Tag 07NG].

```lean
public alias isRegularRing_genericFormalFibre_of_regular_spaceAlteration
```

**`AlgebraicGeometry.Space.exists_isRegularRing_localizationAway_of_isAlteration_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean#L473). The attribute's comment: “part (1)”.

> **A Noetherian local domain admitting an alteration by a regular algebraic space is regular
> after inverting one nonzero element.** The dense regular open of [Stacks, Tag 0BHT], read at the
> representable target `Spec A` by
> `AlgebraicGeometry.Space.denseRegularOpenOfRegularAlteration`, contains a nonempty basic open
> `D(a)` of `Spec A`, and `Γ(D(a)) = A_a`.

```lean
public theorem exists_isRegularRing_localizationAway_of_isAlteration_of_isRegular
    (A : Type u) [CommRing A] [IsDomain A] [IsNoetherianRing A] [IsLocalRing A]
    (B : BigFppfSite.{u}) (hA : B.Contains (Spec (.of A)))
    (X : (BigFppfOver B (Spec (.of A)) hA)ᵒᵖ ⥤ Type u)
    (g : X ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hA))))
    (hg : IsAlteration B (Spec (.of A)) hA g)
    (hreg : HasEtaleLocalProperty B (Spec (.of A)) hA X (fun T : Scheme.{u} => IsRegular T)) :
    ∃ a : A, a ≠ 0 ∧ IsRegularRing (Localization.Away a)
```

**`AlgebraicGeometry.Space.module_finite_integralClosure_of_isAlteration_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean#L505). The attribute's comment: “part (2)”.

> **The integral closure of a Noetherian local domain admitting an alteration by a regular
> algebraic space is a finite module over it.** This is clause (2) of [Stacks, Tag 0BHU]: `A` is
> N-1 (`IsN1`).
>
> The alteration makes `Spec A` an integral algebraic space carrying a regular alteration, so
> [Stacks, Tag 0BHT] applies to it; `Spec A` is its own affine surjective étale scheme chart, the
> identity being surjective and étale, and along that chart
> `AlgebraicGeometry.Space.NormalizationData.isFinite_normalization_chart_of_regular_alteration`
> gives that the normalization morphism of the *scheme* `Spec A` is finite. By [Stacks, Tag 035P]
> that morphism is the spectrum map of `A ⟶ integralClosure A (Frac A)`, so the integral closure is
> a finite `A`-module; that reading is
> `AlgebraicGeometry.module_finite_integralClosure_of_isFinite_normalization`, which takes the
> presenting ring of the scheme — here `A` itself — rather than its ring of global sections.
>
> The source argues instead that `C = Γ(X, 𝒪_X)` is a finite `A`-module by [Stacks, Tag 08AR] and
> integrally closed, and that the integral closure embeds into `C`; the route above replaces that
> by Chow's lemma for algebraic spaces over the chart and the degree-zero case of
> [Stacks, Tag 02O6] for *schemes*, which is how [Stacks, Tag 0BHT] is proved here.

```lean
public theorem module_finite_integralClosure_of_isAlteration_of_isRegular
    (A : Type u) [CommRing A] [IsDomain A] [IsNoetherianRing A] [IsLocalRing A]
    (B : BigFppfSite.{u}) (hA : B.Contains (Spec (.of A)))
    (X : (BigFppfOver B (Spec (.of A)) hA)ᵒᵖ ⥤ Type u)
    (g : X ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hA))))
    (hg : IsAlteration B (Spec (.of A)) hA g)
    (hreg : HasEtaleLocalProperty B (Spec (.of A)) hA X (fun T : Scheme.{u} => IsRegular T)) :
    Module.Finite A ↥(integralClosure A (FractionRing A))
```

**`AlgebraicGeometry.Space.isNormalRing_adicCompletion_integralClosure_of_isAlteration_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean, line 647](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean#L647). The attribute's comment: “part (3)”.

> **The completion of the integral closure of a Noetherian local domain admitting an
> alteration by a regular algebraic space is normal.** This is part (3) of [Stacks, Tag 0BHU]. Let
> `B` be the integral closure of `A` in `Frac(A)` and `C = Γ(X, 𝒪_X)`. Then `C` is a finite
> `A`-module and a normal domain containing `A` ([Stacks, Tag 0BH3]), so `B ⊆ C`, and `Cˆ = Aˆ ⊗_A C`
> is normal by `AlgebraicGeometry.Space.globalFunctions_of_isAlteration_of_isRegular`;
> [Stacks, Tag 0BGH] gives normality of `Bˆ`. Normality is `IsNormalRing`: every localization at a
> prime is a normal domain, which for the finite algebra `Bˆ` over the complete local `Aˆ` is
> normality of the completions of `B` at its maximal ideals.

```lean
public theorem isNormalRing_adicCompletion_integralClosure_of_isAlteration_of_isRegular
    (A : Type u) [CommRing A] [IsDomain A] [IsNoetherianRing A] [IsLocalRing A]
    (B : BigFppfSite.{u}) (hA : B.Contains (Spec (.of A)))
    (X : (BigFppfOver B (Spec (.of A)) hA)ᵒᵖ ⥤ Type u)
    (g : X ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hA))))
    (hg : IsAlteration B (Spec (.of A)) hA g)
    (hreg : HasEtaleLocalProperty B (Spec (.of A)) hA X (fun T : Scheme.{u} => IsRegular T)) :
    IsNormalRing
      (AdicCompletion
        ((IsLocalRing.maximalIdeal A).map
          (algebraMap A ↥(integralClosure A (FractionRing A))))
        ↥(integralClosure A (FractionRing A)))
```

**`AlgebraicGeometry.Space.isRegularRing_genericFormalFibre_of_isAlteration_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean, line 694](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean#L694). The attribute's comment: “part (4)”. References: EGA IV (7.9.3), “special case”.

> **The generic formal fibre of a Noetherian local domain admitting an alteration by a regular
> algebraic space is regular.** For an affine étale chart `V` of `X` through the generic point the
> ring `Aˆ ⊗_A Γ(V, 𝒪_V)` is regular, and the generic formal fibre is recovered by inverting
> `A ∖ {0}` and descending along the faithfully flat `Frac(A)`-algebra `Frac(A) ⊗_A Γ(V, 𝒪_V)`
> by [Stacks, Tag 07NG]. Regularity of the completed base change of the chart is part (3) of
> [Stacks, Tag 0BHQ], applied through
> `AlgebraicGeometry.Space.exists_injective_isRegularRing_adicCompletion_tensorProduct`.

```lean
public theorem isRegularRing_genericFormalFibre_of_isAlteration_of_isRegular
    (A : Type u) [CommRing A] [IsDomain A] [IsNoetherianRing A] [IsLocalRing A]
    (B : BigFppfSite.{u}) (hA : B.Contains (Spec (.of A)))
    (X : (BigFppfOver B (Spec (.of A)) hA)ᵒᵖ ⥤ Type u)
    (g : X ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hA))))
    (hg : IsAlteration B (Spec (.of A)) hA g)
    (hreg : HasEtaleLocalProperty B (Spec (.of A)) hA X (fun T : Scheme.{u} => IsRegular T)) :
    IsRegularRing ((AdicCompletion (IsLocalRing.maximalIdeal A) A) ⊗[A] (FractionRing A))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 89.7, Tag 0BHS](https://stacks.math.columbia.edu/tag/0BHS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
