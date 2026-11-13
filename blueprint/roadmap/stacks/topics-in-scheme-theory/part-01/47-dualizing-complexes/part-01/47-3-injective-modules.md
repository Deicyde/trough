---
declaration: section
origin: cited
lean: Module.Injective.pi, Module.Injective.restrictScalars_of_flat', Module.Injective.of_isEpi, Dualizing.injective_coextendScalars_obj, Module.injective_iff_eq_of_essential_extension, Module.injective_iff_isIso_essentialMono, Module.bijective_hom_localizationAtPrime, Module.injective_localizationAtPrime_of_minimal
statement: formalized
proof: formalized
---

# 47.3 Injective modules

Section 47.3 of the Stacks Project, [Tag 08XN](https://stacks.math.columbia.edu/tag/08XN). 10 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08XP, a lemma

[Tag 08XP](https://stacks.math.columbia.edu/tag/08XP) in the Stacks Project.

Declarations registered for the tag:

- [`Module.Injective.pi`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Injective.pi#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch47.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch47.lean#L19) (StacksFrontier).

## Tag 08XQ, a lemma

[Tag 08XQ](https://stacks.math.columbia.edu/tag/08XQ) in the Stacks Project.

**`Module.Injective.restrictScalars_of_flat'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Injective/ChangeOfRings.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Injective/ChangeOfRings.lean#L63).

> **Stacks 08XQ.** Let `R → S` be a flat ring map. If `E` is an injective `S`-module, then
> `E` is injective as an `R`-module.

```lean
theorem restrictScalars_of_flat' (R : Type*) {S E : Type v} [CommRing R] [CommRing S]
    [Algebra R S] [Module.Flat R S] [AddCommGroup E] [Module R E] [Module S E]
    [IsScalarTower R S E] (h : Module.Injective S E) : Module.Injective R E
```

## Tag 08YV, a lemma

[Tag 08YV](https://stacks.math.columbia.edu/tag/08YV) in the Stacks Project.

**`Module.Injective.of_isEpi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/Ring/Epi/RestrictionOfScalars.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/Ring/Epi/RestrictionOfScalars.lean#L94).

> Let `R → S` be an epimorphism of rings and let `E` be an `S`-module. If `E` is injective as
> an `R`-module, then `E` is an injective `S`-module.
>
> An `S`-linear map into `E` out of an `S`-module is in particular `R`-linear, so it extends
> `R`-linearly along an injective `S`-linear map, and that extension is `S`-linear because
> `R → S` is an epimorphism.

```lean
theorem Module.Injective.of_isEpi (R : Type*) {S E : Type*} [CommRing R] [CommRing S]
    [Algebra R S] [Algebra.IsEpi R S] [AddCommGroup E] [Module R E] [Module S E]
    [IsScalarTower R S E] (h : Module.Injective R E) : Module.Injective S E
```

## Tag 08XR, a lemma

[Tag 08XR](https://stacks.math.columbia.edu/tag/08XR) in the Stacks Project.

**`Dualizing.injective_coextendScalars_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DerivedHomFinite.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/DerivedHomFinite.lean#L86).

> **Stacks 08XR.** For a ring map `f : A →+* B` and an injective `A`-module `M`, the
> `B`-module `Hom_A(B, M)` is injective. Indeed coextension of scalars is right adjoint to
> restriction of scalars, which is exact and in particular preserves monomorphisms.

```lean
theorem injective_coextendScalars_obj (f : A →+* B) (M : ModuleCat.{max v u} A) [Injective M] :
    Injective ((ModuleCat.coextendScalars.{u, u, max v u} f).obj M)
```

## Tag 08XS, a lemma

[Tag 08XS](https://stacks.math.columbia.edu/tag/08XS) in the Stacks Project.

**`Module.injective_iff_eq_of_essential_extension`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean, line 608](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean#L608). The attribute's comment: “characterization inside an injective module”.

> A submodule of an injective module is injective if and only if it has no
> proper essential extension inside the ambient module.

```lean
lemma injective_iff_eq_of_essential_extension
    (R : Type u) [Ring R] (I : Type v) [AddCommGroup I] [Module R I]
    [Module.Injective R I] (E : Submodule R I) :
    Module.Injective R E ↔
      ∀ (E' : Submodule R I) (h : E ≤ E'),
        let i := ModuleCat.ofHom (Submodule.inclusion h)
        letI : Mono i := (ModuleCat.mono_iff_injective i).mpr
          (Submodule.inclusion_injective h)
        IsEssentialMono i → E = E'
```

**`Module.injective_iff_isIso_essentialMono`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean, line 721](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/InjectiveHull/Basic/Existence.lean#L721). The attribute's comment: “intrinsic characterization”.

> A module is injective if and only if every essential monomorphism from it is an isomorphism.

```lean
lemma injective_iff_isIso_essentialMono
    (R : Type u) [Ring R] (Q : Type v) [AddCommGroup Q] [Module R Q] :
    Module.Injective R Q ↔
      ∀ (E' : ModuleCat.{v} R) (i : ModuleCat.of R Q ⟶ E') [Mono i],
        IsEssentialMono i → IsIso i
```

## Tag 08XT, an example

[Tag 08XT](https://stacks.math.columbia.edu/tag/08XT) in the Stacks Project.

**`Module.bijective_hom_localizationAtPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Injective.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/InjectiveHull/Injective.lean#L156). The attribute's comment: “canonical identification of Hom modules”.

> For any module, maps into the localization at a prime are exactly the
> maps from its localized module, via canonical precomposition.

```lean
theorem bijective_hom_localizationAtPrime
    {R : Type u} [CommRing R] (p : Ideal R) [p.IsPrime]
    (M : Type v) [AddCommGroup M] [Module R M] :
    Function.Bijective
      (fun f : LocalizedModule.AtPrime p M →ₗ[Localization.AtPrime p]
          Localization.AtPrime p =>
        (f.restrictScalars R).comp (LocalizedModule.mkLinearMap p.primeCompl M))
```

**`Module.injective_localizationAtPrime_of_minimal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Injective.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/InjectiveHull/Injective.lean#L186). The attribute's comment: “injectivity at a minimal prime”.

> The localization of a reduced ring at a minimal prime is injective as
> an `R`-module.

```lean
theorem injective_localizationAtPrime_of_minimal
    {R : Type u} [CommRing R] [IsReduced R] (p : Ideal R)
    [p.IsPrime] (hp : p ∈ minimalPrimes R) :
    Module.Injective R (Localization.AtPrime p)
```

## Tag 08XV, a lemma

[Tag 08XV](https://stacks.math.columbia.edu/tag/08XV) in the Stacks Project.

**`Module.directSum_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Injective.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/InjectiveHull/Injective.lean#L381).

> An arbitrary direct sum of injective modules over a Noetherian ring is
> injective.

```lean
theorem directSum_injective
    (R : Type u) [CommRing R] [IsNoetherianRing R]
    {ι : Type v} (M : ι → Type (max v w)) [∀ i, AddCommGroup (M i)]
    [∀ i, Module R (M i)] [∀ i, Module.Injective R (M i)]
    : Module.Injective R (⨁ i, M i)
```

## Tag 0A6I, a lemma

[Tag 0A6I](https://stacks.math.columbia.edu/tag/0A6I) in the Stacks Project.

**`AlgebraicGeometry.AffineExt.hasInjectiveAmplitude_extD_locMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineExt/InjectiveAmplitude.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineExt/InjectiveAmplitude.lean#L52). The attribute's comment: “injective amplitude is preserved by localization”.

> **Injective amplitude is preserved by localization.** Over a Noetherian ring `R`, if `L` in
> `D(R)` has injective amplitude in `[a, b]`, then `L ⊗_R R_f` has injective amplitude in `[a, b]`
> over `R_f`.
>
> A bounded complex of injective `R`-modules representing `L` is carried degreewise, and in the
> same degrees, to a bounded complex of injective `R_f`-modules representing `L ⊗_R R_f`: the
> terms stay injective by [Stacks, Tag 0A6I], the bounds are preserved because an additive functor
> carries zero objects to zero objects, and the complex still represents the localization because
> extension of scalars along a localization is exact.

```lean
theorem hasInjectiveAmplitude_extD_locMap (R : CommRingCat.{u}) [IsNoetherianRing R]
    (L : DerivedCategory (ModuleCat.{u} R)) (a b : ℤ) (f : R)
    (hL : StacksDraft.InjectiveDimension.HasInjectiveAmplitude L a b) :
    StacksDraft.InjectiveDimension.HasInjectiveAmplitude ((extD (locMap R f)).obj L) a b
```

Declarations registered for the tag:

- [`Module.injective_of_isLocalizedModule`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.injective_of_isLocalizedModule#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/InjectiveHull/Localization.lean, line 14](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/InjectiveHull/Localization.lean#L14) (StacksFrontier).

## Tag 08XW, a lemma

[Tag 08XW](https://stacks.math.columbia.edu/tag/08XW) in the Stacks Project.

**`Module.injective_iSup_torsionBy_pow`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean, line 634](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean#L634). The attribute's comment: “part (1)”. References: SGA 2 IV (2.2), “principal ideal case”.

> The submodule of an injective module consisting of the elements annihilated by some power
> of `f` is injective. This is part (1) of Stacks Project, Tag 08XW.

```lean
lemma injective_iSup_torsionBy_pow (f : R) :
    Module.Injective R (⨆ n : ℕ, Submodule.torsionBy R I (f ^ n) : Submodule R I)
```

**`Module.injective_primaryComponent`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean, line 727](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/InjectiveHull/Basic/IndecomposableInjective.lean#L727). The attribute's comment: “part (2)”. References: SGA 2 IV (2.2).

> The submodule of an injective module consisting of the elements annihilated by some power
> of `J` is injective. This is part (2) of Stacks Project, Tag 08XW.

```lean
lemma injective_primaryComponent (J : Ideal R) :
    Module.Injective R (Ideal.primaryComponent I J)
```

## Tag 0A6J, a lemma

[Tag 0A6J](https://stacks.math.columbia.edu/tag/0A6J) in the Stacks Project.

**`Module.tensorProduct_polynomial_hasInjectiveDimensionLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/InjectiveHull/Injective.lean, line 877](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/InjectiveHull/Injective.lean#L877).

> **Stacks Project, Tag 0A6J.** Extending an injective module over a Noetherian ring to the
> one-variable polynomial ring gives a module of injective dimension at most one.

```lean
theorem tensorProduct_polynomial_hasInjectiveDimensionLE
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (E : Type v) [AddCommGroup E] [Module A E] [Module.Injective A E] :
    HasInjectiveDimensionLE
      (ModuleCat.of (Polynomial A) (TensorProduct A (Polynomial A) E)) 1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.3, Tag 08XN](https://stacks.math.columbia.edu/tag/08XN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
