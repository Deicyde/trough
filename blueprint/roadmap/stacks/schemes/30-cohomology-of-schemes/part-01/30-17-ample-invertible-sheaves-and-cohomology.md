---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Modules.hasEventualTwistCohomologyVanishing_of_isAmple, AlgebraicGeometry.Scheme.Modules.hasIdealTwistH1Vanishing_of_eventualTwistVanishing, AlgebraicGeometry.Scheme.Modules.isAmple_of_hasIdealTwistH1Vanishing, AlgebraicGeometry.Scheme.Modules.isAmple_of_eventualTwistVanishing, AlgebraicGeometry.Scheme.Modules.tfae_isAmple_twistCohomologyVanishing, Stacks.AmpleFiniteSurjective.isAmple_modulePullback_of_isFinite_surjective, Stacks.AmpleFiniteSurjective.isAmple_iff_isAmple_modulePullback, Stacks.Cohomology.TwistedLocalizationMap.bijective_canonicalMap_of_le_nonvanishingOpen
statement: formalized
proof: formalized
---

# 30.17 Ample invertible sheaves and cohomology

Section 30.17 of the Stacks Project, [Tag 01XO](https://stacks.math.columbia.edu/tag/01XO). 8 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B5U, a lemma

[Tag 0B5U](https://stacks.math.columbia.edu/tag/0B5U) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.hasEventualTwistCohomologyVanishing_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/CohomologicalCriterion.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/CohomologicalCriterion.lean#L148). The attribute's comment: “the implication (1) ⟹ (2)”.

> **The implication (1) ⟹ (2) of [Stacks, Tag 0B5U]**, at the tag's own hypotheses: `R`
> Noetherian, `f : X ⟶ Spec R` proper, `𝓛` ample.
>
> This is clause (4) of [Stacks, Tag 0B5T],
> `Stacks.AlgebraicGeometry.ProperAmpleCohomology.exists_isZero_Hgroup_tensorPowTwist`,
> read through the two comparisons of the implementation notes: ampleness is carried across by
> `Stacks.PowerFamilyBridge.isAmple_of_modulesIsAmple` and the conclusion by
> `isZero_rightDerived_moduleGlobalSections_of_isZero_Hgroup`.

```lean
public theorem hasEventualTwistCohomologyVanishing_of_isAmple {R : Type u} [CommRing R]
    [IsNoetherianRing R] (f : X ⟶ Spec (.of R)) [IsProper f] (hL : IsAmple X L) :
    HasEventualTwistCohomologyVanishing L
```

**`AlgebraicGeometry.Scheme.Modules.hasIdealTwistH1Vanishing_of_eventualTwistVanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/CohomologicalCriterion.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/CohomologicalCriterion.lean#L166). The attribute's comment: “the implication (2) ⟹ (3)”.

> **The implication (2) ⟹ (3) of [Stacks, Tag 0B5U]**, on a locally Noetherian scheme and with
> none of the tag's remaining hypotheses.
>
> A quasi-coherent sheaf of ideals is a quasi-coherent submodule of the structure sheaf, which on a
> locally Noetherian scheme is coherent ([Stacks, Tag 01Y1], the structure sheaf itself being
> coherent); condition (2) then applies to it, and is read at `p = 1` and at an exponent at least
> one.

```lean
public theorem hasIdealTwistH1Vanishing_of_eventualTwistVanishing [IsLocallyNoetherian X]
    (h : HasEventualTwistCohomologyVanishing L) : HasIdealTwistH1Vanishing L
```

**`AlgebraicGeometry.Scheme.Modules.isAmple_of_hasIdealTwistH1Vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/CohomologicalCriterion.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/CohomologicalCriterion.lean#L181). The attribute's comment: “the implication (3) ⟹ (1)”.

> **The implication (3) ⟹ (1) of [Stacks, Tag 0B5U]**, on a quasi-compact scheme and with none
> of the tag's remaining hypotheses. This is [Stacks, Tag 0B5P].

```lean
public theorem isAmple_of_hasIdealTwistH1Vanishing [CompactSpace X]
    (h : HasIdealTwistH1Vanishing L) : IsAmple X L
```

**`AlgebraicGeometry.Scheme.Modules.isAmple_of_eventualTwistVanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/CohomologicalCriterion.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/CohomologicalCriterion.lean#L195). The attribute's comment: “the implication (2) ⟹ (1)”.

> **The implication (2) ⟹ (1) of [Stacks, Tag 0B5U]**, at the tag's own hypotheses: `R`
> Noetherian, `f : X ⟶ Spec R` proper. Both steps are unconditional; properness and the Noetherian
> base enter only through `IsLocallyNoetherian X` and `CompactSpace X`.

```lean
public theorem isAmple_of_eventualTwistVanishing {R : Type u} [CommRing R] [IsNoetherianRing R]
    (f : X ⟶ Spec (.of R)) [IsProper f] (h : HasEventualTwistCohomologyVanishing L) :
    IsAmple X L
```

**`AlgebraicGeometry.Scheme.Modules.tfae_isAmple_twistCohomologyVanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/CohomologicalCriterion.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleDegreeCriterion/CohomologicalCriterion.lean#L212). The attribute's comment: “the three equivalent conditions”. References: EGA III (5.2.3), “(ii), special case”.

> **[Stacks, Tag 0B5U].** For `R` Noetherian, `f : X ⟶ Spec R` proper and `𝓛` an invertible
> `𝒪_X`-module, the three conditions
>
> 1. `𝓛` is ample;
> 2. the higher cohomology of `ℱ ⊗ 𝓛^{⊗ n}` vanishes for every coherent `ℱ` and all large `n`;
> 3. `H¹(X, ℐ ⊗ 𝓛^{⊗ n}) = 0` for some `n ≥ 1`, for every quasi-coherent sheaf of ideals `ℐ`
>
> are equivalent. The implication (1) ⟹ (2) is clause (4) of [Stacks, Tag 0B5T]; the other two are
> proved with none of the tag's hypotheses.

```lean
public theorem tfae_isAmple_twistCohomologyVanishing {R : Type u} [CommRing R]
    [IsNoetherianRing R] (f : X ⟶ Spec (.of R)) [IsProper f] :
    List.TFAE
      [IsAmple X L, HasEventualTwistCohomologyVanishing L, HasIdealTwistH1Vanishing L]
```

## Tag 0B5V, a lemma

[Tag 0B5V](https://stacks.math.columbia.edu/tag/0B5V) in the Stacks Project.

**`Stacks.AmpleFiniteSurjective.isAmple_modulePullback_of_isFinite_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleFiniteSurjective/Basic.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleFiniteSurjective/Basic.lean#L278). The attribute's comment: “the implication `L` ample ⟹ `f^* L` ample”.

> **The forward half of [Stacks, Tag 0B5V]**, at the source's hypothesis list: `X` proper over a
> Noetherian ring `R`, `f` finite and surjective. The hypotheses other than finiteness are inert;
> `Stacks.AmpleFiniteSurjective.isAmple_modulePullback_of_isFinite` is the same statement without
> them.

```lean
theorem isAmple_modulePullback_of_isFinite_surjective (R : Type u) [CommRing R]
    [IsNoetherianRing R] (p : X ⟶ Spec (.of R)) [IsProper p] [IsFinite f] [Surjective f]
    (hL : IsAmple X L) :
    IsAmple Y ((modulePullback f.toLRSHom.toShHom).obj L)
```

**`Stacks.AmpleFiniteSurjective.isAmple_iff_isAmple_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleFiniteSurjective/Basic.lean, line 663](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleFiniteSurjective/Basic.lean#L663).

> **[Stacks, Tag 0B5V].** Let `R` be a Noetherian ring, let `f : Y ⟶ X` be a morphism of schemes
> proper over `R` — `X` through `p` and `Y` through `f ≫ p`, which is automatic since a finite
> morphism is proper and properness composes — and let `L` be an invertible `𝒪_X`-module. If `f` is
> finite and surjective, then `L` is ample if and only if `f^* L` is ample.
>
> Every binder is the source's: the Noetherian ring, properness over it, finiteness and
> surjectivity of `f`, and invertibility of `L`. `⟹` is `isAmple_modulePullback_of_isFinite`, which
> needs only finiteness; `⟸` is `isAmple_of_isAmple_modulePullback`, the source's cohomological
> argument.

```lean
theorem isAmple_iff_isAmple_modulePullback (R : Type u) [CommRing R] [IsNoetherianRing R]
    (p : X ⟶ Spec (.of R)) [IsProper p] [IsFinite f] [Surjective f] :
    IsAmple X L ↔ IsAmple Y ((modulePullback f.toLRSHom.toShHom).obj L)
```

## Tag 09MR, a lemma

[Tag 09MR](https://stacks.math.columbia.edu/tag/09MR) in the Stacks Project.

**`Stacks.Cohomology.TwistedLocalizationMap.bijective_canonicalMap_of_le_nonvanishingOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwistedCohomologyLocalization/CanonicalMap.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TwistedCohomologyLocalization/CanonicalMap.lean#L391). The attribute's comment: “for an open U inside the nonvanishing locus X_s: the canonical map H^p_*(U,L,F)_(s) to H^p(U ∩ X_s,F), xi/s^n to s^(-n) xi, is bijective, on an arbitrary scheme, for an arbitrary module and in every degree. The quasi-compact quasi-separated case of the tag is bijective_canonicalMap_of_isCompact, and neither case subsumes the other.”.

> **The comparison map is bijective on an open contained in the nonvanishing open of `s`.** Let
> `X` be a scheme, `ℒ` an invertible `𝒪_X`-module, `s` a global section of `ℒ`, `ℱ` an arbitrary
> `𝒪_X`-module, `p` a cohomological degree and `U ⊆ X_s` an open contained in the nonvanishing
> locus of `s`. Then the canonical map
>
> `H^p_*(U, ℒ, ℱ)₍s₎ ⟶ H^p(U ∩ X_s, ℱ)`,  `ξ / sⁿ ↦ s^{-n} ξ`
>
> of `Stacks.Cohomology.TwistedLocalizationMap.canonicalMap` is **bijective**.
>
> Neither quasi-compactness nor quasi-separatedness of `U`, nor quasi-coherence of `ℱ`, nor
> positivity of `p` is assumed, and this is **not** a both-sides-vanish statement: taking
> `U = X_s` it reads `H^p_*(X_s, ℒ, ℱ)₍s₎ ≅ H^p(X_s, ℱ)` on an arbitrary scheme, with neither side
> forced to be zero.

```lean
theorem bijective_canonicalMap_of_le_nonvanishingOpen (hU : U ≤ nonvanishingOpen L s) :
    Function.Bijective (canonicalMap X L s F p U)
```

**`Stacks.Cohomology.TwistedLocalizationMap.bijective_canonicalMap_of_isCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwistedCohomologyLocalization/MayerVietorisStep.lean, line 981](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TwistedCohomologyLocalization/MayerVietorisStep.lean#L981).

> **[Stacks, Tag 09MR] over a quasi-compact open of a quasi-separated scheme.** For a
> quasi-compact open `S` of a quasi-separated scheme `X`, an invertible `𝒪_X`-module `ℒ`, a global
> section `s` of `ℒ`, a quasi-coherent `𝒪_X`-module `ℱ` and any degree `p`, the comparison map
>
> `H^p_*(S, ℒ, ℱ)₍s₎ ⟶ H^p(S ∩ X_s, ℱ)`,  `ξ / sⁿ ↦ s^{-n} ξ`
>
> is bijective.

```lean
theorem bijective_canonicalMap_of_isCompact [QuasiSeparatedSpace X]
    (S : X.Opens) (hS : IsCompact (S : Set X)) (p : ℕ) :
    Function.Bijective (canonicalMap X L s F p S)
```

**`Stacks.Cohomology.TwistedLocalizationMap.bijective_canonicalMap_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TwistedCohomologyLocalization/MayerVietorisStep.lean, line 990](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TwistedCohomologyLocalization/MayerVietorisStep.lean#L990).

> **[Stacks, Tag 09MR] on a quasi-compact quasi-separated scheme.**

```lean
theorem bijective_canonicalMap_top [QuasiSeparatedSpace X] [CompactSpace X] (p : ℕ) :
    Function.Bijective (canonicalMap X L s F p ⊤)
```

## Tag 01XR, a lemma

[Tag 01XR](https://stacks.math.columbia.edu/tag/01XR) in the Stacks Project.

**`Stacks.SheafOfModules.exists_sectionPowerAction_eq_zero_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionPowerCohomology/Basic.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionPowerCohomology/Basic.lean#L123). The attribute's comment: “the case of an affine ambient scheme”.

> **The conclusion of [Stacks, Tag 01XR] for an affine ambient scheme.** On an affine scheme the
> positive-degree cohomology of a quasi-coherent module vanishes, so every class is annihilated
> already by the zeroth power of a global section of an invertible module.

```lean
theorem exists_sectionPowerAction_eq_zero_of_isAffine [IsAffine X] (s : L.sections)
    [CompactSpace X] [QuasiSeparatedSpace X] (_hU : IsAffineOpen (nonvanishingOpen L s))
    (F : X.Modules) [F.IsQuasicoherent] (p : ℕ) (hp : 0 < p)
    (ξ : Hgroup X.ringCatSheaf ⊤ p F) :
    ∃ (n : ℕ) (t : SheafOfModules.unit X.ringCatSheaf ⟶
        TensorPower.tensorPower X.toRingedSpace.presheaf
          (structureSheafRing X.toRingedSpace).property L n),
      IsSectionPowerHom X.toRingedSpace.presheaf
          (structureSheafRing X.toRingedSpace).property L s n t ∧
        (Hfunctor X.ringCatSheaf ⊤ p).map
          (sectionPowerAction X.toRingedSpace.presheaf
            (structureSheafRing X.toRingedSpace).property L F n t) ξ = 0
```

**`Stacks.SheafOfModules.exists_sectionPowerAction_eq_zero_of_finite_affine_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionPowerCohomology/Basic.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionPowerCohomology/Basic.lean#L144). The attribute's comment: “the degrees at least the size of a finite affine cover”.

> **The conclusion of [Stacks, Tag 01XR] above the size of a finite affine cover.** On a scheme
> with affine diagonal covered by `t` affine opens the cohomology of a quasi-coherent module
> vanishes in every degree at least `t`, so in those degrees every class is annihilated already by
> the zeroth power of a global section of an invertible module.

```lean
theorem exists_sectionPowerAction_eq_zero_of_finite_affine_cover
    [IsAffineHom (pullback.diagonal (terminal.from X))] (s : L.sections)
    [CompactSpace X] [QuasiSeparatedSpace X] (_hU : IsAffineOpen (nonvanishingOpen L s))
    {t : ℕ} (U : Fin t → X.Opens) (hUaff : ∀ i, IsAffineOpen (U i)) (hUcover : ⨆ i, U i = ⊤)
    (F : X.Modules) [F.IsQuasicoherent] (p : ℕ) (_hp : 0 < p) (ht : t ≤ p)
    (ξ : Hgroup X.ringCatSheaf ⊤ p F) :
    ∃ (n : ℕ) (t' : SheafOfModules.unit X.ringCatSheaf ⟶
        TensorPower.tensorPower X.toRingedSpace.presheaf
          (structureSheafRing X.toRingedSpace).property L n),
      IsSectionPowerHom X.toRingedSpace.presheaf
          (structureSheafRing X.toRingedSpace).property L s n t' ∧
        (Hfunctor X.ringCatSheaf ⊤ p).map
          (sectionPowerAction X.toRingedSpace.presheaf
            (structureSheafRing X.toRingedSpace).property L F n t') ξ = 0
```

**`Stacks.SheafOfModules.exists_sectionPowerAction_eq_zero_of_isAffineOpen_nonvanishingOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionPowerCohomology/Localization.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionPowerCohomology/Localization.lean#L152).

> **[Stacks, Tag 01XR].** Let `X` be a quasi-compact quasi-separated scheme, `ℒ` an invertible
> `𝒪_X`-module and `s ∈ Γ(X, ℒ)` a global section whose nonvanishing open `X_s` is affine. Then
> every cohomology class of a quasi-coherent `𝒪_X`-module in a positive degree is annihilated by
> some power of `s`.
>
> This is the general case; `./Basic.lean` has the two cases in which the cohomology group itself
> vanishes. The conclusion quantifies over the morphisms `𝒪_X ⟶ ℒ^{⊗ k}` representing `s^k`, as
> those statements do, and is witnessed by the canonical representative
> `Stacks.SheafOfModules.sectionPowerHom`.

```lean
theorem exists_sectionPowerAction_eq_zero_of_isAffineOpen_nonvanishingOpen [CompactSpace X]
    [QuasiSeparatedSpace X] (hU : IsAffineOpen (nonvanishingOpen L s)) (p : ℕ) (hp : 0 < p)
    (ξ : (Hgroup X.ringCatSheaf ⊤ p F : Type u)) :
    ∃ (n : ℕ) (t : SheafOfModules.unit X.ringCatSheaf ⟶
        TensorPower.tensorPower X.toRingedSpace.presheaf
          (structureSheafRing X.toRingedSpace).property L n),
      IsSectionPowerHom X.toRingedSpace.presheaf
          (structureSheafRing X.toRingedSpace).property L s n t ∧
        (Hfunctor X.ringCatSheaf ⊤ p).map
          (sectionPowerAction X.toRingedSpace.presheaf
            (structureSheafRing X.toRingedSpace).property L F n t) ξ = 0
```

**`Stacks.SheafOfModules.exists_sectionPowerAction_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SectionPowerCohomology/QuasiCompact.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SectionPowerCohomology/QuasiCompact.lean#L141).

> **[Stacks, Tag 01XR].** Let `X` be a scheme, `ℒ` an invertible `𝒪_X`-module and
> `s ∈ Γ(X, ℒ)` a global section. If `X` is quasi-compact and quasi-separated and
> `X_s` is affine, then for every quasi-coherent `𝒪_X`-module `ℱ`, every `p > 0` and every
> `ξ ∈ Hᵖ(X, ℱ)` there is `n ≥ 0` with `sⁿ ξ = 0` in `Hᵖ(X, ℱ ⊗ ℒ^{⊗ n})`.
>
> Multiplication by `sⁿ` is `Stacks.SheafOfModules.sectionPowerAction` along the morphism
> `t : 𝒪_X ⟶ ℒ^{⊗ n}` representing `sⁿ` (`Stacks.SheafOfModules.IsSectionPowerHom`; such a `t` is
> unique, by `Stacks.SheafOfModules.IsSectionPowerHom.unique`, and exists, by
> `Stacks.SheafOfModules.isSectionPowerHom_sectionPowerHom`).

```lean
theorem exists_sectionPowerAction_eq_zero (X : Scheme.{u})
    (L : SheafOfModules.{u} (structureSheafRing X.toRingedSpace))
    [IsInvertible X.toRingedSpace.presheaf (structureSheafRing X.toRingedSpace).property L]
    [CompactSpace X] [QuasiSeparatedSpace X] (s : L.sections)
    (hU : IsAffineOpen (nonvanishingOpen L s)) (F : X.Modules) [F.IsQuasicoherent] (p : ℕ)
    (hp : 0 < p) (ξ : Hgroup X.ringCatSheaf ⊤ p F) :
    ∃ n : ℕ, ∀ (t : SheafOfModules.unit X.ringCatSheaf ⟶
        TensorPower.tensorPower X.toRingedSpace.presheaf
          (structureSheafRing X.toRingedSpace).property L n),
      IsSectionPowerHom X.toRingedSpace.presheaf
          (structureSheafRing X.toRingedSpace).property L s n t →
        (Hfunctor X.ringCatSheaf ⊤ p).map
          (sectionPowerAction X.toRingedSpace.presheaf
            (structureSheafRing X.toRingedSpace).property L F n t) ξ = 0
```

## Tag 09MS, a lemma

[Tag 09MS](https://stacks.math.columbia.edu/tag/09MS) in the Stacks Project.

**`Stacks.AmpleSurjectiveThickening.isAmple_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleSurjectiveThickening/Basic.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleSurjectiveThickening/Basic.lean#L107). The attribute's comment: “the implication `L` ample ⟹ `i^* L` ample”.

> **`L` ample `⟹` `i^* L` ample.** For a closed immersion `i : Z ⟶ X` of Noetherian schemes
> inducing a homeomorphism of underlying spaces, ampleness of an invertible `𝒪_X`-module `L` gives
> ampleness of `i^* L` ([Stacks, Tag 0892]). The proof is
> `Stacks.AmpleClosedImmersion.isAmple_modulePullback_of_surjective_isClosedImmersion`.

```lean
theorem isAmple_modulePullback [IsClosedImmersion i] [Surjective i] [IsNoetherian X]
    (hL : IsAmple X L) :
    IsAmple Z ((modulePullback i.toLRSHom.toShHom).obj L)
```

**`Stacks.AmpleSurjectiveThickening.isAmple_modulePullback_iff_isAmple_of_isHomeomorph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleSurjectiveThickening/Basic.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleSurjectiveThickening/Basic.lean#L254).

> **[Stacks, Tag 09MS].** Let `i : Z ⟶ X` be a closed immersion of Noetherian schemes inducing a
> homeomorphism of underlying topological spaces, and let `L` be an invertible `𝒪_X`-module. Then
> `i^* L` is ample on `Z` if and only if `L` is ample on `X`. Noetherianness of `Z` follows from that
> of `X`, since `i` is a closed immersion, and is not assumed.

```lean
theorem isAmple_modulePullback_iff_isAmple_of_isHomeomorph [IsClosedImmersion i] [IsNoetherian X]
    (hi : IsHomeomorph i.base) :
    IsAmple Z ((modulePullback i.toLRSHom.toShHom).obj L) ↔ IsAmple X L
```

## Tag 0B7K, a lemma

[Tag 0B7K](https://stacks.math.columbia.edu/tag/0B7K) in the Stacks Project.

**`Stacks.AmpleSurjectiveThickening.isQuasiAffine_iff_isQuasiAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleSurjectiveThickening/QuasiAffine.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleSurjectiveThickening/QuasiAffine.lean#L145).

> **[Stacks, Tag 0B7K].** Let `i : Z ⟶ X` be a closed immersion of Noetherian schemes inducing a
> homeomorphism of underlying topological spaces — that is, a closed immersion surjective on
> points. Then `X` is quasi-affine if and only if `Z` is quasi-affine.

```lean
theorem isQuasiAffine_iff_isQuasiAffine [IsClosedImmersion i] [Surjective i] [IsNoetherian X] :
    X.IsQuasiAffine ↔ Z.IsQuasiAffine
```

**`Stacks.Thickenings.isQuasiAffine_iff_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/QuasiAffineAscent.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/QuasiAffineAscent.lean#L550). References: EGA II (5.1.10), “(vi), special case”.

> **[Stacks Project, Tag 0B7K].** For a closed immersion `i : Z ⟶ X` of Noetherian schemes
> inducing a homeomorphism of underlying spaces — equivalently, a surjective closed immersion — the
> ambient scheme is quasi-affine if and only if the closed subscheme is.
>
> Both implications are unconditional. *Ambient `⟹` closed subscheme* is the elementary one, a
> closed immersion being affine (`Stacks.Thickenings.isQuasiAffine_of_isQuasiAffine_ambient`).
> *Closed subscheme `⟹` ambient* is
> `Stacks.Thickenings.isQuasiAffine_of_isThickening_of_isLocallyNoetherian`: over a Noetherian
> scheme a thickening is of finite order, and along a finite-order thickening an affine basic open
> lifts, by the square-zero computation of
> `Stacks.Thickenings.affineBasicOpenLifts_of_isFirstOrderThickening_of_isQuasiAffine` along the
> filtration by the powers of the ideal sheaf. Neither the ampleness criterion
> [Stacks Project, Tag 01QE] nor [Stacks Project, Tag 09MS] nor any cohomology group enters, so the
> hypothesis `Stacks.AmpleClosedImmersion.SectionsLiftAfterPower` carried by
> `Stacks.AmpleSurjectiveThickening.isQuasiAffine_iff_of_sectionsLiftAfterPower` is discharged.
>
> Noetherianness of the closed subscheme is not used, and of the ambient scheme only local
> Noetherianness together with quasi-compactness; both are carried because the source assumes
> them.

```lean
theorem isQuasiAffine_iff_of_isNoetherian {Z X : Scheme.{u}} (i : Z ⟶ X) [IsClosedImmersion i]
    [Surjective i] [IsNoetherian Z] [IsNoetherian X] :
    X.IsQuasiAffine ↔ Z.IsQuasiAffine
```

## Tag 0EBD, a lemma

[Tag 0EBD](https://stacks.math.columbia.edu/tag/0EBD) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CohomologyColimitReduction.isAffine_of_isZero_cohomology_negative_tensorPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CohomologyColimitReduction/Basic.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CohomologyColimitReduction/Basic.lean#L258).

> **[Stacks, Tag 0EBD].** Let `L` be an ample invertible module on a scheme `X` and let `n₀` be
> an integer such that `Hᵖ(X, L^{⊗ -n}) = 0` for every `n ≥ n₀` and every `p > 0`. Then `X` is
> affine.
>
> Everything the dévissage of the tag needs beyond this hypothesis comes from ampleness itself:
> quasi-compactness is part of ampleness and quasi-separatedness follows from it
> ([Stacks, Tag 01PV]), which makes the colimit reduction ([Stacks, Tag 01PG] with
> [Stacks, Tag 01FF]) available and supplies a degree beyond which the cohomology of every
> quasi-coherent module vanishes ([Stacks, Tag 071L], in the form
> `AlgebraicGeometry.exists_isZero_hgroup_top`); the dévissage sequence presenting a quasi-coherent
> module of finite type as a quotient of a finite direct sum of negative twists of `L` is clause
> (8) of [Stacks, Tag 01Q3]; and the vanishing of `Hᵖ` on all quasi-coherent modules in all
> positive degrees gives affineness by Serre's criterion ([Stacks, Tag 01XF]).

```lean
theorem isAffine_of_isZero_cohomology_negative_tensorPower (L : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L] (hL : Stacks.Ample.IsAmple X L) (n₀ : ℤ)
    (hvan : ∀ (n : ℤ) (p : ℕ), n₀ ≤ n → 0 < p →
      IsZero (Hgroup X.ringCatSheaf ⊤ p (Stacks.Ample.tensorPowModule X L (-n)))) :
    IsAffine X
```

## Tag 0EBE, a lemma

[Tag 0EBE](https://stacks.math.columbia.edu/tag/0EBE) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CohomologyColimitReduction.isAffine_of_isZero_hgroup_unitModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CohomologyColimitReduction/QuasiAffine.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CohomologyColimitReduction/QuasiAffine.lean#L102).

> **[Stacks, Tag 0EBE].** Let `X` be a quasi-affine scheme.  If `Hᵖ(X, 𝒪_X) = 0` for every
> `p > 0`, then `X` is affine.
>
> The source's argument verbatim: `𝒪_X` is an ample invertible module on a quasi-affine scheme
> ([Stacks, Tag 01QE], `Stacks.Ample.isAmple_unitModule_of_isQuasiAffine`), so affineness follows
> from the vanishing of the higher cohomology of the negative twists of an ample module
> ([Stacks, Tag 0EBD], `isAffine_of_isZero_cohomology_negative_tensorPower`).  Tag 0EBD's family of
> hypotheses collapses to this single one because the twists of `𝒪_X` are all `𝒪_X`, by
> `isZero_hgroup_tensorPowModule_unitModule`; the threshold `n₀` is taken to be `0` and is
> immaterial.

```lean
theorem isAffine_of_isZero_hgroup_unitModule (X : Scheme.{u}) [X.IsQuasiAffine]
    (hvan : ∀ p : ℕ, 0 < p →
      IsZero (Hgroup X.ringCatSheaf ⊤ p (SheafOfModules.unit X.ringCatSheaf))) :
    IsAffine X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.17, Tag 01XO](https://stacks.math.columbia.edu/tag/01XO)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
