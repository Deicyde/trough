---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isFinite_normalization_and_exists_isDenseOpenSubspace_isRegular, AlgebraicGeometry.Space.exists_isRegularRing_localizationAway_of_regular_spaceAlteration, AlgebraicGeometry.Space.module_finite_integralClosure_of_regular_spaceAlteration, AlgebraicGeometry.Space.isNormalRing_adicCompletion_integralClosure_of_regular_spaceAlteration, AlgebraicGeometry.Space.isRegularRing_genericFormalFibre_of_regular_spaceAlteration, AlgebraicGeometry.Space.exists_isRegularRing_localizationAway_of_isAlteration_of_isRegular, AlgebraicGeometry.Space.module_finite_integralClosure_of_isAlteration_of_isRegular, AlgebraicGeometry.Space.isNormalRing_adicCompletion_integralClosure_of_isAlteration_of_isRegular
statement: formalized
proof: formalized
---

# 89.7 Implied properties

Section 89.7 of the Stacks Project, [Tag 0BHS](https://stacks.math.columbia.edu/tag/0BHS). 2 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BHT, a lemma

[Tag 0BHT](https://stacks.math.columbia.edu/tag/0BHT) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinite_normalization_and_exists_isDenseOpenSubspace_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianRegularAlteration.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianRegularAlteration.lean#L67). The attribute's comment: “both assertions: finiteness of the normalization and the existence of a regular dense open. The source's Step 1, etale localization to a Noetherian domain, does not apply to algebraic spaces (etale charts of an integral space need not be irreducible); finiteness is proved instead through Chow's lemma for spaces over an affine chart”.

> **Stacks 0BHT.** Let `Y` be a Noetherian integral algebraic space over `S`, and suppose there
> is an alteration `f : X ⟶ Y` with `X` regular. Then the normalization `Y^ν ⟶ Y` of `Y` is a
> finite morphism of algebraic spaces, and `Y` has a dense open subspace which is regular.
>
> Integrality of `Y` is part of `AlgebraicGeometry.Space.IsAlteration`. Noetherianity is
> Stacks 03EA, `AlgebraicGeometry.Space.IsNoetherian`; its local Noetherianity makes the étale
> scheme charts of `Y` satisfy the finiteness condition of Stacks 0BB1, so that
> `AlgebraicGeometry.Space.normalizationData` is the normalization of `Y`, unique up to a unique
> isomorphism over `Y` by `AlgebraicGeometry.Space.NormalizationData.existsUnique_iso_hom`.
>
> The first assertion is `AlgebraicGeometry.Space.isFinite_normalization_of_regular_alteration`
> and the second is
> `AlgebraicGeometry.Space.exists_isDenseOpenSubspace_hasEtaleLocalProperty_isRegular`. The source
> proves finiteness by étale localization to the spectrum of a Noetherian domain followed by
> Stacks 08AR; that reduction is not valid for algebraic spaces, whose étale charts need not be
> irreducible, and the proof used here goes instead through Chow's lemma (Stacks 089J) over an
> affine chart, as the module docstring of
> `StacksFrontier.AlgebraicGeometry.Spaces.NormalizationFiniteRegularAlteration` explains.

```lean
theorem isFinite_normalization_and_exists_isDenseOpenSubspace_isRegular
    (hZ : B.Contains (⊤_ Scheme.{u})) (hYnoeth : IsNoetherian B S hS hZ Y)
    (f : X ⟶ Y) (hf : IsAlteration B S hS f)
    (hXreg : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsRegular T)) :
    IsFinite B S hS (normalizationData B S hS hf.1
        (hasLocallyFiniteIrreducibleComponents_of_isLocallyNoetherian B S hS Y hf.1
          hYnoeth.2.2)).hom ∧
      ∃ V : Subfunctor Y, IsDenseOpenSubspace B S hS hf.1 V ∧
        HasEtaleLocalProperty B S hS V.toFunctor (fun T : Scheme.{u} => IsRegular T)
```

## Tag 0BHU, a lemma

[Tag 0BHU](https://stacks.math.columbia.edu/tag/0BHU) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isRegularRing_localizationAway_of_regular_spaceAlteration`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean#L164). The attribute's comment: “clause (1), regular after inverting one element”.

> **A Noetherian local domain admitting an alteration by a regular algebraic space is regular
> after inverting one nonzero element.** The dense regular open of [Stacks, Tag 0BHT] at the
> representable target `Spec A` contains a nonempty basic open `D(a)` of `Spec A`, and
> `Γ(D(a)) = A_a`.

```lean
public alias exists_isRegularRing_localizationAway_of_regular_spaceAlteration
```

**`AlgebraicGeometry.Space.module_finite_integralClosure_of_regular_spaceAlteration`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean#L172). The attribute's comment: “clause (2), finite integral closure”.

> **The integral closure of a Noetherian local domain admitting an alteration by a regular
> algebraic space is a finite module over it.** The normalization of `Spec A` is finite by
> [Stacks, Tag 0BHT], and it is the spectrum of the integral closure of `A` in `Frac(A)`
> ([Stacks, Tag 035P]).

```lean
public alias module_finite_integralClosure_of_regular_spaceAlteration
```

**`AlgebraicGeometry.Space.isNormalRing_adicCompletion_integralClosure_of_regular_spaceAlteration`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean#L182). The attribute's comment: “clause (3), normal completion of the integral closure”.

> **The completion of the integral closure is normal.** With `C = Γ(X, 𝒪_X)` and `B` the
> integral closure of `A` in `Frac(A)`, the inclusion `B ⊆ C` is a map of finite `A`-algebras and
> `B` is a normal domain, so [Stacks, Tag 0BGH] reduces normality of `Bˆ` to normality of
> `Cˆ = Aˆ ⊗_A C`, which is the global functions of the regular base change `X ×_{Spec A} Spec Aˆ`
> ([Stacks, Tag 073K], [Stacks, Tag 0BHQ]). Normality here is `IsNormalRing`, which for a finite
> algebra over a Noetherian local ring is normality of the completions at the maximal ideals.

```lean
public alias isNormalRing_adicCompletion_integralClosure_of_regular_spaceAlteration
```

**`AlgebraicGeometry.Space.isRegularRing_genericFormalFibre_of_regular_spaceAlteration`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/LocalDomainSpaceAlteration.lean#L191). The attribute's comment: “clause (4), regular generic formal fibre”.

> **The generic formal fibre of a Noetherian local domain admitting an alteration by a regular
> algebraic space is regular.** For an affine étale chart `V` of `X` through the generic point the
> ring `Aˆ ⊗_A Γ(V, 𝒪_V)` is regular by [Stacks, Tag 0BHQ], and the generic formal fibre is
> recovered by inverting `A ∖ {0}` and descending along the faithfully flat `Frac(A)`-algebra
> `Frac(A) ⊗_A Γ(V, 𝒪_V)` by [Stacks, Tag 07NG].

```lean
public alias isRegularRing_genericFormalFibre_of_regular_spaceAlteration
```

**`AlgebraicGeometry.Space.exists_isRegularRing_localizationAway_of_isAlteration_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean#L473). The attribute's comment: “part (1)”.

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

**`AlgebraicGeometry.Space.module_finite_integralClosure_of_isAlteration_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean, line 505](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean#L505). The attribute's comment: “part (2)”.

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

**`AlgebraicGeometry.Space.isNormalRing_adicCompletion_integralClosure_of_isAlteration_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean, line 647](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean#L647). The attribute's comment: “part (3)”.

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

**`AlgebraicGeometry.Space.isRegularRing_genericFormalFibre_of_isAlteration_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean, line 694](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ImpliedProperties/RegularSpaceAlterationLocalDomain.lean#L694). The attribute's comment: “part (4)”. References: EGA IV (7.9.3), “special case”.

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
