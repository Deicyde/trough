---
declaration: section
origin: cited
lean: AlgebraicGeometry.InjectiveModuloMaximalIdealSituation, AlgebraicGeometry.universallyInjective_of_isNoetherianRing, AlgebraicGeometry.flat_of_isNoetherianRing, Module.finitePresentation_of_finite, AlgebraicGeometry.universallyInjective_of_localizedPolynomial_cases, AlgebraicGeometry.finitePresentation_of_localizedPolynomial_cases, AlgebraicGeometry.flat_of_localizedPolynomial_cases, AlgebraicGeometry.injectiveModuloMaximalIdealConclusion_of_henselianLocalRing
statement: formalized
proof: formalized
---

# 38.25 Variants of a lemma

Section 38.25 of the Stacks Project, [Tag 0ASZ](https://stacks.math.columbia.edu/tag/0ASZ). 14 tags here are carried by 21 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AT0, a situation

[Tag 0AT0](https://stacks.math.columbia.edu/tag/0AT0) in the Stacks Project.

**`AlgebraicGeometry.InjectiveModuloMaximalIdealSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/MaximalIdealInjectivity.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/MaximalIdealInjectivity.lean#L60).

> The standing data and hypotheses of Stacks Project, Tag 0AT0: a local homomorphism
> `A → B` of local rings which is essentially of finite type, a flat `A`-module `M`, a finite
> `B`-module `N`, and an `A`-linear map `N → M` which is injective modulo the maximal ideal
> of `A`.

```lean
structure InjectiveModuloMaximalIdealSituation
```

## Tag 0AT1, a lemma

[Tag 0AT1](https://stacks.math.columbia.edu/tag/0AT1) in the Stacks Project.

**`AlgebraicGeometry.universallyInjective_of_isNoetherianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/MaximalIdealInjectivity.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/MaximalIdealInjectivity.lean#L152). The attribute's comment: “universal injectivity”.

> **Stacks Project, Tag 0AT1.** In Situation 0AT0 over a Noetherian base, the given map is
> universally injective over the base ring.

```lean
theorem universallyInjective_of_isNoetherianRing
    (S : InjectiveModuloMaximalIdealSituation.{u₁, u₂, u₃, u₄})
    [IsNoetherianRing S.A] : UniversallyInjectivePoly S.u
```

**`AlgebraicGeometry.flat_of_isNoetherianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/MaximalIdealInjectivity.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/MaximalIdealInjectivity.lean#L161). The attribute's comment: “flatness”.

> **Stacks Project, Tag 0AT1.** In Situation 0AT0 over a Noetherian base, the source module
> is flat over the base ring.

```lean
theorem flat_of_isNoetherianRing
    (S : InjectiveModuloMaximalIdealSituation.{u₁, u₂, u₃, u₄})
    [IsNoetherianRing S.A] : Module.Flat S.A S.N
```

Declarations registered for the tag:

- [`Module.finitePresentation_of_finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.finitePresentation_of_finite#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/MaximalIdealInjectivity.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/MaximalIdealInjectivity.lean#L124) (StacksFrontier): “finite presentation”. References: EGA 0 (1.0.5), “more general”; EGA 0 (1.3.5), “more general”.

## Tag 0AT2, a lemma

[Tag 0AT2](https://stacks.math.columbia.edu/tag/0AT2) in the Stacks Project.

**`AlgebraicGeometry.universallyInjective_of_localizedPolynomial_cases`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/PolynomialLocalizationReduction.lean, line 546](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/PolynomialLocalizationReduction.lean#L546). The attribute's comment: “universal injectivity”.

> Universal injectivity in Situation 0AT0 reduces to the case of a localization of a finite
> polynomial algebra with finitely presented source module.

```lean
theorem universallyInjective_of_localizedPolynomial_cases
    (S : InjectiveModuloMaximalIdealSituation.{u₁, u₂, u₃, u₄})
    (h : ∀ (T : InjectiveModuloMaximalIdealSituation.{u₁, max u₁ u₂, u₃, max u₁ u₂ u₄}),
      SameBaseLocalRing S T → PolynomialLocalizationPresentation T.A T.B →
        Module.FinitePresentation T.B T.N →
          InjectiveModuloMaximalIdealConclusion.{max u₁ u₅} T) :
    UniversallyInjectivePoly.{_, u₅} S.u
```

**`AlgebraicGeometry.finitePresentation_of_localizedPolynomial_cases`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/PolynomialLocalizationReduction.lean, line 558](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/PolynomialLocalizationReduction.lean#L558). The attribute's comment: “finite presentation”.

> Finite presentation in Situation 0AT0 reduces to the case of a localization of a finite
> polynomial algebra with finitely presented source module.

```lean
theorem finitePresentation_of_localizedPolynomial_cases
    (S : InjectiveModuloMaximalIdealSituation.{u₁, u₂, u₃, u₄})
    (h : ∀ (T : InjectiveModuloMaximalIdealSituation.{u₁, max u₁ u₂, u₃, max u₁ u₂ u₄}),
      SameBaseLocalRing S T → PolynomialLocalizationPresentation T.A T.B →
        Module.FinitePresentation T.B T.N →
          InjectiveModuloMaximalIdealConclusion.{max u₁ u₅} T) :
    Module.FinitePresentation S.B S.N
```

**`AlgebraicGeometry.flat_of_localizedPolynomial_cases`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/PolynomialLocalizationReduction.lean, line 570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/PolynomialLocalizationReduction.lean#L570). The attribute's comment: “flatness”.

> Flatness in Situation 0AT0 reduces to the case of a localization of a finite polynomial
> algebra with finitely presented source module.

```lean
theorem flat_of_localizedPolynomial_cases
    (S : InjectiveModuloMaximalIdealSituation.{u₁, u₂, u₃, u₄})
    (h : ∀ (T : InjectiveModuloMaximalIdealSituation.{u₁, max u₁ u₂, u₃, max u₁ u₂ u₄}),
      SameBaseLocalRing S T → PolynomialLocalizationPresentation T.A T.B →
        Module.FinitePresentation T.B T.N →
          InjectiveModuloMaximalIdealConclusion.{max u₁ u₅} T) :
    Module.Flat S.A S.N
```

## Tag 0AT3, a lemma

[Tag 0AT3](https://stacks.math.columbia.edu/tag/0AT3) in the Stacks Project.

**`AlgebraicGeometry.injectiveModuloMaximalIdealConclusion_of_henselianLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/HenselianBase.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/HenselianBase.lean#L273).

> **Stacks Project, Tag 0AT3.** In Situation 0AT0 with `A` henselian the lemma holds: if
> `A → B` is a local homomorphism of local rings essentially of finite type, `M` is a flat
> `A`-module, `N` is a finite `B`-module and `u : N → M` is an `A`-linear map whose reduction
> `N/𝔪_A N → M/𝔪_A M` is injective, then `u` is `A`-universally injective, `N` is of finite
> presentation over `B`, and `N` is flat over `A`.

```lean
theorem injectiveModuloMaximalIdealConclusion_of_henselianLocalRing
    (S : InjectiveModuloMaximalIdealSituation.{u₁, u₂, u₃, u₄}) [HenselianLocalRing S.A] :
    InjectiveModuloMaximalIdealConclusion.{u₅} S
```

## Tag 0AT4, a lemma

[Tag 0AT4](https://stacks.math.columbia.edu/tag/0AT4) in the Stacks Project.

**`AlgebraicGeometry.universallyInjective_and_finitePresentation_and_flat_of_linearMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/HenselizationReduction.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/HenselizationReduction.lean#L322). The attribute's comment: “`N/𝔪_A N → M/𝔪_A M` is the `Submodule.mapQ` of `u` for `𝔪_A • ⊤`, and `A`-universal injectivity is `UniversallyInjectivePoly` of `u` with scalars restricted to `A`.”.

> **Stacks Project, Tag 0AT4.** Let `A → B` be a local homomorphism of local rings which is
> essentially of finite type and let `u : N → M` be a `B`-linear map. If `N` is a finite
> `B`-module, `M` is flat over `A`, and the induced map `N/𝔪_A N → M/𝔪_A M` is injective, then
> `u` is universally injective over `A`, `N` is finitely presented over `B`, and `N` is flat over
> `A`.
>
> This is `HenselizationReduction.conclusions_of_henselian_cases` applied to the henselian case
> Stacks 0AT3, `injectiveModuloMaximalIdealConclusion_of_henselianLocalRing`.

```lean
theorem universallyInjective_and_finitePresentation_and_flat_of_linearMap
    {A : Type u₁} {B : Type u₂} {M : Type u₃} {N : Type u₄}
    [CommRing A] [IsLocalRing A] [CommRing B] [IsLocalRing B] [Algebra A B]
    [IsLocalHom (algebraMap A B)] [Algebra.EssFiniteType A B]
    [AddCommGroup M] [Module A M] [Module B M] [IsScalarTower A B M] [Module.Flat A M]
    [AddCommGroup N] [Module A N] [Module B N] [IsScalarTower A B N] [Module.Finite B N]
    (u : N →ₗ[B] M)
    (hu : Function.Injective (Submodule.mapQ (maximalIdeal A • (⊤ : Submodule A N))
      (maximalIdeal A • (⊤ : Submodule A M)) (u.restrictScalars A)
      (Submodule.smul_top_le_comap_smul_top (maximalIdeal A) (u.restrictScalars A)))) :
    UniversallyInjectivePoly.{_, w} (u.restrictScalars A) ∧ Module.FinitePresentation B N ∧
      Module.Flat A N
```

## Tag 0AT5, a lemma

[Tag 0AT5](https://stacks.math.columbia.edu/tag/0AT5) in the Stacks Project.

**`AlgebraicGeometry.flat_of_valuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ValuationRingBase.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ValuationRingBase.lean#L241). The attribute's comment: “the flatness assertion of `the lemma' for Situation 0AT0: in Situation 0AT0 with `A` a valuation ring, `N` is flat over `A`. Proved from 0AT0's own hypotheses together with `ValuationRing A`.”.

> **Stacks Project, Tag 0AT5 (flatness).** In Situation 0AT0 with the base ring `A` a
> valuation ring, the finite `B`-module `N` is flat over `A`.

```lean
theorem flat_of_valuationRing
    (S : InjectiveModuloMaximalIdealSituation.{u₁, u₂, u₃, u₄})
    [IsDomain S.A] [ValuationRing S.A] : Module.Flat S.A S.N
```

**`AlgebraicGeometry.finitePresentation_of_valuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ValuationRingBase.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ValuationRingBase.lean#L252). The attribute's comment: “the finite-presentation assertion of `the lemma' for Situation 0AT0: in Situation 0AT0 with `A` a valuation ring, `N` is of finite presentation over `B`. Proved from 0AT0's own hypotheses together with `ValuationRing A`.”.

> **Stacks Project, Tag 0AT5 (finite presentation).** In Situation 0AT0 with the base ring
> `A` a valuation ring, the finite `B`-module `N` is of finite presentation over `B`.

```lean
theorem finitePresentation_of_valuationRing
    (S : InjectiveModuloMaximalIdealSituation.{u₁, u₂, u₃, u₄})
    [IsDomain S.A] [ValuationRing S.A] : Module.FinitePresentation S.B S.N
```

## Tag 0AT6, an equation

[Tag 0AT6](https://stacks.math.columbia.edu/tag/0AT6) in the Stacks Project.

**`AlgebraicGeometry.FinitelyPresentedLocalizedModuleSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/LocalizedModuleSpreadout.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/LocalizedModuleSpreadout.lean#L60).

> **Stacks Project, Tag 0AT6.** The standing situation of a finitely presented algebra `B`
> over `A`, a multiplicative subset `S ⊆ B`, and a finitely presented module over a
> localization of `B` at `S`.

```lean
structure FinitelyPresentedLocalizedModuleSituation
```

## Tag 0AT7, a lemma

[Tag 0AT7](https://stacks.math.columbia.edu/tag/0AT7) in the Stacks Project.

**`AlgebraicGeometry.exists_isContentIdeal_of_pureSpreadout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ContentIdeals.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ContentIdeals.lean#L125). The attribute's comment: “content_ideals”.

> **Stacks Project, Tag 0AT7.** If a pure spreadout exists, every element of the localized
> module has a content ideal over the base ring.

```lean
theorem exists_isContentIdeal_of_pureSpreadout
    (X : FinitelyPresentedLocalizedModuleSituation.{u₁, u₂, u₃, u₄})
    (hspread : Nonempty (PureSpreadout.{u₁, u₂, u₃, u₄, u₁} X)) (x : X.N) :
    ∃ I : Ideal X.A, IsContentIdeal x I
```

**`AlgebraicGeometry.universallyInjective_of_injective_mod_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/UniversalInjectivity.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/UniversalInjectivity.lean#L312). The attribute's comment: “universal_injectivity”.

> **Stacks Project, Tag 0AT7 (universal injectivity).** A map into a flat
> module which is injective modulo each maximal ideal is universally injective,
> provided the distinguished localized module admits a pure spreadout.

```lean
theorem universallyInjective_of_injective_mod_maximalIdeal
    (X : FinitelyPresentedLocalizedModuleSituation.{u₁, u₂, u₃, u₄})
    (hspread : Nonempty (PureSpreadout.{u₁, u₂, u₃, u₄, u₄} X))
    {M : Type u₄} [AddCommGroup M] [Module X.A M] [Module.Flat X.A M]
    (u : X.N →ₗ[X.A] M)
    (hu : ∀ (m : Ideal X.A) [m.IsMaximal],
      Function.Injective
        (Submodule.mapQ (m • (⊤ : Submodule X.A X.N))
          (m • (⊤ : Submodule X.A M)) u
          (Submodule.smul_top_le_comap_smul_top m u))) :
    UniversallyInjective u
```

## Tag 0AT8, a lemma

[Tag 0AT8](https://stacks.math.columbia.edu/tag/0AT8) in the Stacks Project.

**`AlgebraicGeometry.FinitelyPresentedLocalizedModuleSituation.exists_fg_ideal_localQuotientBaseChange_pureSpreadout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/PureSpreadoutQuotient.lean, line 495](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/PureSpreadoutQuotient.lean#L495).

> **Stacks Project, Tag 0AT8.** In the standing situation of Stacks 0AT6, for every prime `𝔭` of
> the base ring there is a finitely generated ideal `I` of the local ring `A_𝔭`, contained in the
> extension of `𝔭`, such that the base change of the situation to `A_𝔭 ⧸ I` carries a pure spreadout.
>
> The test-module universe of the universal injectivity packaged in the pure spreadout is left free,
> so the statement instantiates at any test universe.

```lean
theorem exists_fg_ideal_localQuotientBaseChange_pureSpreadout (p : Ideal X.A) [p.IsPrime] :
    ∃ I : Ideal (Localization.AtPrime p), I.FG ∧
      I ≤ p.map (algebraMap X.A (Localization.AtPrime p)) ∧
      ∃ Y : FinitelyPresentedLocalizedModuleSituation.{u₁, max u₁ u₂, max u₁ u₃,
          max u₁ (max u₃ u₄)},
        Nonempty (LocalQuotientBaseChange X Y p I) ∧
          Nonempty (PureSpreadout.{u₁, max u₁ u₂, max u₁ u₃, max u₁ (max u₃ u₄), u₅} Y)
```

## Tag 0AT9, a lemma

[Tag 0AT9](https://stacks.math.columbia.edu/tag/0AT9) in the Stacks Project.

**`AlgebraicGeometry.universallyInjective_of_rTensor_residueField_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/PureSpreadoutQuotient.lean, line 531](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/PureSpreadoutQuotient.lean#L531).

> **Stacks Project, Tag 0AT9**, unconditionally. In the finitely presented localized-module
> situation, a linear map between flat modules which is injective on every residue-field fibre is
> universally injective.
>
> This is `AlgebraicGeometry.universallyInjective_of_rTensor_residueField_injective_of_pureSpreadout`
> with its `hAT8` hypothesis discharged by Stacks 0AT8, instantiated at the test-module universe that
> binder pins.

```lean
theorem universallyInjective_of_rTensor_residueField_injective
    (X : FinitelyPresentedLocalizedModuleSituation.{u₁, u₂, u₃, u₄})
    {M : Type u₄} [AddCommGroup M] [Module X.A M]
    [Module.Flat X.A X.N] [Module.Flat X.A M]
    (u : X.N →ₗ[X.A] M)
    (hu : ∀ (p : Ideal X.A) [p.IsPrime],
      Function.Injective (u.rTensor p.ResidueField)) :
    UniversallyInjective u
```

## Tag 0ATA, a lemma

[Tag 0ATA](https://stacks.math.columbia.edu/tag/0ATA) in the Stacks Project.

**`PrimeSpectrum.sInf_eq_bot_of_iUnion_zeroLocus_eq_compl_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ZeroLocusOnLocalSpectrum.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ZeroLocusOnLocalSpectrum.lean#L61).

> **Stacks Project, Tag 0ATA.** A multiplicatively closed collection of finitely generated
> ideals whose zero loci cover every non-generic point of the spectrum of a local domain has
> zero intersection.

```lean
theorem sInf_eq_bot_of_iUnion_zeroLocus_eq_compl_genericPoint
    {A : Type u} [CommRing A] [IsDomain A] [IsLocalRing A]
    (hA : ¬ IsField A) (S : Set (Ideal A))
    (hSfg : ∀ I ∈ S, I.FG)
    (hSmul : ∀ I ∈ S, ∀ J ∈ S, I * J ∈ S)
    (hcover : (⋃ I ∈ S, PrimeSpectrum.zeroLocus (I : Set A)) =
      {p : PrimeSpectrum A | p.asIdeal ≠ ⊥}) :
    sInf S = ⊥
```

## Tag 0ATB, a lemma

[Tag 0ATB](https://stacks.math.columbia.edu/tag/0ATB) in the Stacks Project.

**`PrimeSpectrum.closedPoints_compl_zeroLocus_subset_zeroLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ZeroLocusOnLocalSpectrum.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ZeroLocusOnLocalSpectrum.lean#L155).

> **Stacks Project, Tag 0ATB.** If `J` is a proper finitely generated ideal of a local ring
> and `I` is contained in every positive power of `J`, then `V(I)` contains every closed point
> of `Spec(A) \ V(J)`.

```lean
theorem closedPoints_compl_zeroLocus_subset_zeroLocus
    {A : Type u} [CommRing A] [IsLocalRing A] (I J : Ideal A)
    (hJ : J ≠ ⊤) (hJfg : J.FG)
    (hIJ : ∀ n : ℕ, 0 < n → I ≤ J ^ n) :
    Subtype.val '' closedPoints
        ((PrimeSpectrum.zeroLocus (J : Set A))ᶜ : Set (PrimeSpectrum A)) ⊆
      PrimeSpectrum.zeroLocus (I : Set A)
```

## Tag 0ATC, a lemma

[Tag 0ATC](https://stacks.math.columbia.edu/tag/0ATC) in the Stacks Project.

**`AlgebraicGeometry.smallerFlatnessIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/FlatnessIdeal.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/FlatnessIdeal.lean#L67). The attribute's comment: “the ideal I₂”.

> The ideal `I₂ = Ker (I → Γ(U, (I/I²)~))` of `A`, for an ideal `I` of `A` and an open
> `U ⊆ Spec A`: the image in `A` of the kernel of the composite of `I → I/I²` with the map
> taking a global conormal class to its sections over `U`.

```lean
def smallerFlatnessIdeal {A : Type u} [CommRing A]
    (I : Ideal A) (U : (Spec (.of A)).Opens) : Ideal A
```

**`AlgebraicGeometry.flat_quotient_smallerFlatnessIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/FlatnessIdeal.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowingUp/FlatnessIdeal.lean#L330). The attribute's comment: “flatness modulo I₂”.

> **Stacks Project, Tag 0ATC.** Let `I` be an ideal of a commutative ring `A` and let
> `U ⊆ Spec A` be a quasi-compact open. If `M/IM` is flat over `A/I` and `M~` is flat on `U`,
> then `M/I₂M` is flat over `A/I₂`, where `I₂ = Ker (I → Γ(U, (I/I²)~))`.
>
> The source assumes `A` local; locality is not used.

```lean
theorem flat_quotient_smallerFlatnessIdeal
    {A : Type u} [CommRing A]
    {M : Type u} [AddCommGroup M] [Module A M]
    (I : Ideal A) (U : (Spec (.of A)).Opens)
    (hU : IsCompact U.1)
    (hquot : Module.Flat (A ⧸ I) (M ⧸ I • (⊤ : Submodule A M)))
    (hflat : SheafOfModules.IsFlat.{u, u, u, u} (O := (U : Scheme).sheaf)
      (show (U : Scheme).Modules from
        (tilde (ModuleCat.of A M)).restrict U.ι)) :
    Module.Flat (A ⧸ smallerFlatnessIdeal I U)
      (M ⧸ smallerFlatnessIdeal I U • (⊤ : Submodule A M))
```

**`Stacks.flat_quotient_sectionsKernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FlatteningSectionsKernel.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FlatteningSectionsKernel.lean#L132).

> Let `I ⊆ A` be an ideal, `M` an `A`-module and `U = ⋃ i, D(f i)` a quasi-compact open of
> `Spec A`. If `M/IM` is flat over `A/I` and `M` is flat over `U`, that is `M_{f i}` is flat over
> `A_{f i}` for each `i`, then `M/I₂M` is flat over `A/I₂`, where `I₂ = Ker (I → Γ(U, I/I²))` is
> `sectionsKernel I f`.

```lean
theorem flat_quotient_sectionsKernel (I : Ideal A) {ι : Type w} [Finite ι] (f : ι → A)
    (hI : Module.Flat (A ⧸ I) (M ⧸ I • (⊤ : Submodule A M)))
    (hU : ∀ i, Module.Flat (Localization.Away (f i)) (Localization.Away (f i) ⊗[A] M)) :
    Module.Flat (A ⧸ sectionsKernel I f)
      (M ⧸ sectionsKernel I f • (⊤ : Submodule A M))
```

## Tag 05U9, a proposition

[Tag 05U9](https://stacks.math.columbia.edu/tag/05U9) in the Stacks Project.

**`AlgebraicGeometry.conclusion_of_injectiveModuloMaximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/NilpotentFlatteningClaimOneIndex.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/NilpotentFlatteningClaimOneIndex.lean#L283). The attribute's comment: “universal injectivity, finite presentation and flatness”.

> **Stacks Project, Tag 05U9.** Let `A → B` be a local homomorphism of local rings which is
> essentially of finite type, let `M` be a flat `A`-module, let `N` be a finite `B`-module and let
> `u : N → M` be an `A`-linear map whose reduction `ū : N ⧸ 𝔪_AN → M ⧸ 𝔪_AM` is injective. Then
>
> 1. `u` is `A`-universally injective,
> 2. `N` is of finite presentation over `B`, and
> 3. `N` is flat over `A`.
>
> The hypotheses are the data of Situation 0AT0
> (`AlgebraicGeometry.InjectiveModuloMaximalIdealSituation`) and the three conclusions are
> `AlgebraicGeometry.InjectiveModuloMaximalIdealConclusion`.
>
> Stacks 0AT2 reduces all three to the case where `B` is a localization at a prime of a
> polynomial algebra over `A` in finitely many variables and `N` is of finite presentation over
> `B`, and `AlgebraicGeometry.conclusion_of_presentation` settles that case through Claim 1 of the
> source's proof.

```lean
theorem conclusion_of_injectiveModuloMaximalIdeal
    (S : InjectiveModuloMaximalIdealSituation.{u₁, u₂, u₃, u₄}) :
    InjectiveModuloMaximalIdealConclusion.{u₅} S
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.25, Tag 0ASZ](https://stacks.math.columbia.edu/tag/0ASZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
