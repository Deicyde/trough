---
declaration: section
origin: cited
lean: Submonoid, Localization, IsLocalization, Stacks.Localization.existsUnique_ringHom_comp_algebraMap_eq, IsLocalization.lift, IsLocalization.subsingleton_iff, ModuleCat.invertibleSMulEquivalentLocalizationModuleCat, LocalizedModule
statement: formalized
proof: formalized
---

# 10.9 Localization

Section 10.9 of the Stacks Project, [Tag 00CM](https://stacks.math.columbia.edu/tag/00CM). 16 tags here are carried by 10 declarations of the repository (6 in StacksCore and 4 in StacksFrontier) and 17 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00CN, a definition

[Tag 00CN](https://stacks.math.columbia.edu/tag/00CN) in the Stacks Project.

Declarations registered for the tag:

- [`Submonoid`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Submonoid#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Group/Submonoid/Defs.lean, line 7](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Group/Submonoid/Defs.lean#L7) (StacksCore). References: EGA 0 (1.2.1).

## Tag 00CO, a definition

[Tag 00CO](https://stacks.math.columbia.edu/tag/00CO) in the Stacks Project.

Declarations registered for the tag:

- [`Localization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Localization#doc) registered with `add_to_stacks` in [StacksCore/GroupTheory/MonoidLocalization/Basic.lean, line 7](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/GroupTheory/MonoidLocalization/Basic.lean#L7) (StacksCore). References: EGA 0 (10.3.1.1); EGA 0 (1.2.2); SGA 7 XXI (5.0), “more general”.
- [`IsLocalization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/Defs.lean, line 7](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/Defs.lean#L7) (StacksCore). References: EGA I (1.3.1), “more general”.

## Tag 00CP, a proposition

[Tag 00CP](https://stacks.math.columbia.edu/tag/00CP) in the Stacks Project.

**`Stacks.Localization.existsUnique_ringHom_comp_algebraMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/UniversalProperty.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Localization/UniversalProperty.lean#L24). The attribute's comment: “Stated for any localization `S` of `R` at `M`, in particular `Localization M`.”.

> The universal property of localization: if a ring map `f : R →+* P` sends every element of
> `M` to a unit of `P`, there is a unique ring map `g : S →+* P` out of the localization
> `S = M⁻¹R` with `g ∘ (R → S) = f`.

```lean
theorem existsUnique_ringHom_comp_algebraMap_eq {f : R →+* P} (hf : ∀ y : M, IsUnit (f y)) :
    ∃! g : S →+* P, g.comp (algebraMap R S) = f
```

Declarations registered for the tag:

- [`IsLocalization.lift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.lift#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/Defs.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/Defs.lean#L8) (StacksCore). References: EGA 0 (1.2.4); EGA 0 (7.6.6).

## Tag 00CQ, a lemma

[Tag 00CQ](https://stacks.math.columbia.edu/tag/00CQ) in the Stacks Project.

Declarations registered for the tag:

- [`IsLocalization.subsingleton_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.subsingleton_iff#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/Defs.lean, line 9](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/Defs.lean#L9) (StacksCore). References: EGA 0 (7.6.4), “Discrete topology on A”.

## Tag 07JY, a lemma

[Tag 07JY](https://stacks.math.columbia.edu/tag/07JY) in the Stacks Project.

**`ModuleCat.invertibleSMulEquivalentLocalizationModuleCat`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Category/ModuleCat/Localization.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Category/ModuleCat/Localization.lean#L283).

> **Stacks 07JY.** The category of `Localization S`-modules is equivalent to the full
> subcategory of `R`-modules on which every `s ∈ S` acts invertibly. The functor is
> `ModuleCat.localizedModuleFunctor` restricted to the subcategory; the quasi-inverse is
> restriction of scalars along `algebraMap R (Localization S)`.

```lean
noncomputable def invertibleSMulEquivalentLocalizationModuleCat [Small.{v, u} R] :
    (invertibleSMul S).FullSubcategory ≌ ModuleCat.{v} (Localization S)
```

## Tag 07JZ, a definition

[Tag 07JZ](https://stacks.math.columbia.edu/tag/07JZ) in the Stacks Project.

Declarations registered for the tag:

- [`LocalizedModule`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocalizedModule#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Module/LocalizedModule/Basic.lean, line 7](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Module/LocalizedModule/Basic.lean#L7) (StacksCore). References: EGA 0 (1.2.2); EGA I (1.1.1), “more general”; EGA I (1.3.1), “more general”.

## Tag 07K0, a lemma

[Tag 07K0](https://stacks.math.columbia.edu/tag/07K0) in the Stacks Project.

**`IsLocalizedModule.bijective_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/LocalizedModule/Basic.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/LocalizedModule/Basic.lean#L24). The attribute's comment: “The full lemma: the canonical map `Hom_R(S⁻¹M, N) → Hom_R(M, N)` induced by the localization map is bijective, stated for any localization `f : M →ₗ[R] M'` of `M` at `S`. It supersedes the registration of `IsLocalizedModule.lift_unique`, which is only injectivity.”.

> Let `S ⊆ R` be a multiplicative subset and `f : M → M'` a localization of `M` at `S`
> (e.g. `M' = S⁻¹M`). If every element of `S` acts invertibly on `N`, then the canonical
> map `Hom_R(M', N) → Hom_R(M, N)`, `l ↦ l ∘ₗ f`, is bijective; as it is `R`-linear, it is an
> isomorphism of `R`-modules. Injectivity is `IsLocalizedModule.lift_unique` and surjectivity is
> `IsLocalizedModule.lift_comp`. This is the full statement of Lemma 10.9.7, so it supersedes the
> registration of `IsLocalizedModule.lift_unique` (only injectivity) for that tag.

```lean
theorem IsLocalizedModule.bijective_comp {R : Type*} [CommSemiring R] (S : Submonoid R)
    {M M' N : Type*} [AddCommMonoid M] [Module R M] [AddCommMonoid M'] [Module R M']
    [AddCommMonoid N] [Module R N] (f : M →ₗ[R] M') [IsLocalizedModule S f]
    (h : ∀ s : S, IsUnit (algebraMap R (Module.End R N) s)) :
    Function.Bijective fun l : M' →ₗ[R] N ↦ l ∘ₗ f
```

Declarations registered for the tag:

- [`IsLocalizedModule.lift_unique`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalizedModule.lift_unique#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Module/LocalizedModule/Basic.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Module/LocalizedModule/Basic.lean#L8) (StacksCore). References: EGA 0 (1.2.4), “uniqueness of v*”.

## Tag 02C5, an example

[Tag 02C5](https://stacks.math.columbia.edu/tag/02C5) in the Stacks Project.

**`IsLocalization.Away.subsingleton_iff_isNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Away/Basic.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Localization/Away/Basic.lean#L40). The attribute's comment: “Item 2: `A_f = 0` if and only if `f` is nilpotent in `A`, for every localization `A_f` of `A` with respect to `f`.”.

> A localization `R_f` of `R` away from `f` is the zero ring if and only if `f` is nilpotent
> in `R`.

```lean
theorem subsingleton_iff_isNilpotent [IsLocalization.Away f S] :
    Subsingleton S ↔ IsNilpotent f
```

Declarations registered for the tag:

- [`Localization.Away`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Localization.Away#doc) registered with `add_to_stacks` in [StacksCore/GroupTheory/MonoidLocalization/Away.lean, line 7](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/GroupTheory/MonoidLocalization/Away.lean#L7) (StacksCore): “2”. References: EGA 0 (1.2.3); EGA 0 (7.6.15), “special case”; EGA I (1.3.1); EGA IV (10.4.4).
- [`Localization.AtPrime`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Localization.AtPrime#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/AtPrime/Basic.lean, line 7](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/AtPrime/Basic.lean#L7) (StacksCore): “1”. References: EGA 0 (10.3.1.1); EGA 0 (10.3.1.4); EGA 0 (16.3.1); EGA 0 (1.2.3); EGA 0 (1.2.7); EGA 0 (19.8.3); EGA I (1.1.1); EGA III (4.4.7); EGA IV (5.6.11); EGA IV (7.2.4); EGA IV (1.3.10); SGA 1 III (1.4).
- [`FractionRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FractionRing#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/FractionRing.lean, line 16](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/FractionRing.lean#L16) (StacksCore): “3”. References: EGA 0 (10.3.1.1); EGA 0 (1.2.2), “special case”; EGA 0 (21.8.8); EGA II (7.1.5); EGA IV (18.11.12).
- [`FractionRing.field`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FractionRing.field#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/FractionRing.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/FractionRing.lean#L17) (StacksCore): “4”.
- [`LocalizedModule`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocalizedModule#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Localization/Away/Basic.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Localization/Away/Basic.lean#L28) (StacksFrontier): “Items 1 and 2: for an `A`-module `M`, the localization `M_𝔭` at a prime `𝔭` is `LocalizedModule 𝔭.primeCompl M`, and the localization `M_f` with respect to `f ∈ A` is `LocalizedModule (Submonoid.powers f) M`.”. References: EGA 0 (1.2.2); EGA I (1.1.1), “more general”; EGA I (1.3.1), “more general”.

## Tag 00CR, a lemma

[Tag 00CR](https://stacks.math.columbia.edu/tag/00CR) in the Stacks Project.

**`LocalizedModule.equivAwayColimit`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Module/LocalizedModule/Colimit.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Module/LocalizedModule/Colimit.lean#L208).

> **Stacks 00CR.** `S⁻¹M = colim_{f ∈ S} M_f`: the localization of `M` at `S` is the
> directed colimit of the away-localizations `M_f` over `f ∈ S` with the divisibility
> preorder, with transition maps `M_f → M_g` for `f ∣ g` induced by the universal
> property.

```lean
noncomputable def equivAwayColimit : LocalizedModule S M ≃ₗ[R] AwayColimit S M
```

## Tag 02C6, a proposition

[Tag 02C6](https://stacks.math.columbia.edu/tag/02C6) in the Stacks Project.

**`IsLocalization.isLocalization_sup_of_isLocalization_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/LocalizationLocalization.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Localization/LocalizationLocalization.lean#L40). The attribute's comment: “Stated as `IsLocalization (S ⊔ S') T`: in a commutative monoid `S ⊔ S'` is the set of products `s * s'`, which is Stacks' `SS'`; the isomorphism itself is `IsLocalization.algEquivSupOfIsLocalizationMap`.”.

> **Localization in two stages.** If `B` is the localization of `A` at `S'` and `T` is the
> localization of `B` at the image `S̄` of `S`, then `T` is the localization of `A` at the
> product submonoid `S ⊔ S' = SS'`.

```lean
theorem isLocalization_sup_of_isLocalization_map [IsLocalization S' B]
    [IsLocalization (S.map (algebraMap A B)) T] : IsLocalization (S ⊔ S') T
```

Declarations registered for the tag:

- [`IsLocalization.localization_localization_isLocalization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.localization_localization_isLocalization#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/LocalizationLocalization.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/LocalizationLocalization.lean#L8) (StacksCore). References: EGA 0 (1.4.6), “special case”; EGA 0 (7.6.8), “partial”.

## Tag 02C7, a proposition

[Tag 02C7](https://stacks.math.columbia.edu/tag/02C7) in the Stacks Project.

**`LocalizedModule.equivLocalizedModuleLocalizedModule`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Module/LocalizedModule/LocalizationLocalization.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Module/LocalizedModule/LocalizationLocalization.lean#L67).

> **Stacks 02C7.**  Iterated localization of modules: for multiplicative subsets
> `S, S' ⊆ R` and an `R`-module `M`, the localization of `M` at the multiplicative set
> `SS' = S ⊔ S'` is the localization at `S` of the `R`-module `S'⁻¹M`.

```lean
noncomputable def equivLocalizedModuleLocalizedModule :
    LocalizedModule (S ⊔ S') M ≃ₗ[R] LocalizedModule S (LocalizedModule S' M)
```

## Tag 00CS, a proposition

[Tag 00CS](https://stacks.math.columbia.edu/tag/00CS) in the Stacks Project.

Declarations registered for the tag:

- [`LocalizedModule.map_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocalizedModule.map_exact#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Module/LocalizedModule/Exact.lean, line 7](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Module/LocalizedModule/Exact.lean#L7) (StacksCore). References: EGA 0 (1.3.2), “more general”; EGA 0 (6.3.1), “more general”.

## Tag 02C8, a lemma

[Tag 02C8](https://stacks.math.columbia.edu/tag/02C8) in the Stacks Project.

Declarations registered for the tag:

- [`localizedQuotientEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=localizedQuotientEquiv#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Module/LocalizedModule/Submodule.lean, line 7](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Module/LocalizedModule/Submodule.lean#L7) (StacksCore).

## Tag 00CT, a proposition

[Tag 00CT](https://stacks.math.columbia.edu/tag/00CT) in the Stacks Project.

**`IsLocalization.quotientEquiv`**, a def in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Localization/Ideal.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/Ideal.lean#L30). The attribute's comment: “(2)”.

> Localization commutes with quotients: for any localization
> `Q` of `A/I` at the image `S̄` of `S`, there is a canonical algebra (in particular ring)
> isomorphism `S̄⁻¹(A/I) ≅ S⁻¹A/S⁻¹I`.

```lean
noncomputable def quotientEquiv : Q ≃ₐ[A ⧸ I] A_S ⧸ I.map (algebraMap A A_S)
```

Declarations registered for the tag:

- [`Ideal.localized'_eq_map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.localized'_eq_map#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/Ideal.lean, line 12](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/Ideal.lean#L12) (StacksCore): “(1)”. References: EGA 0 (1.2.6), “partial”.

## Tag 00CU, a lemma

[Tag 00CU](https://stacks.math.columbia.edu/tag/00CU) in the Stacks Project.

**`Submodule.localized'_comap_restrictScalars`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Module/LocalizedModule/Submodule.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Module/LocalizedModule/Submodule.lean#L19). References: SGA 6 0 (2.11), “affine step”.

```lean
theorem localized'_comap_restrictScalars (N' : Submodule S N) :
    ((N'.restrictScalars R).comap f).localized' S p f = N'
```

**`Submodule.localized'_surjective`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Module/LocalizedModule/Submodule.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Module/LocalizedModule/Submodule.lean#L24). The attribute's comment: “existence form”.

```lean
theorem localized'_surjective : Function.Surjective (localized' S p f)
```

## Tag 02C9, a lemma

[Tag 02C9](https://stacks.math.columbia.edu/tag/02C9) in the Stacks Project.

Declarations registered for the tag:

- [`IsLocalization.map_under`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.map_under#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/Ideal.lean, line 13](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/Ideal.lean#L13) (StacksCore). References: EGA 0 (1.2.6), “partial”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.9, Tag 00CM](https://stacks.math.columbia.edu/tag/00CM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
