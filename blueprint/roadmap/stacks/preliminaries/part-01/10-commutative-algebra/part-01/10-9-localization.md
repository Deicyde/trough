---
declaration: section
origin: cited
lean: Submonoid, Localization, IsLocalization, IsLocalization.lift, IsLocalization.subsingleton_iff, ModuleCat.invertibleSMulEquivalentLocalizationModuleCat, LocalizedModule, IsLocalizedModule.lift_unique
statement: formalized
proof: formalized
---

# 10.9 Localization

Section 10.9 of the Stacks Project, [Tag 00CM](https://stacks.math.columbia.edu/tag/00CM). 16 tags here are carried by 6 declarations of the repository (all in StacksCore) and 16 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00CN, a definition

[Tag 00CN](https://stacks.math.columbia.edu/tag/00CN) in the Stacks Project.

Declarations registered for the tag:

- [`Submonoid`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Submonoid#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Group/Submonoid/Defs.lean, line 7](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Group/Submonoid/Defs.lean#L7) (StacksCore). References: EGA 0 (1.2.1).

## Tag 00CO, a definition

[Tag 00CO](https://stacks.math.columbia.edu/tag/00CO) in the Stacks Project.

Declarations registered for the tag:

- [`Localization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Localization#doc) registered with `add_to_stacks` in [StacksCore/GroupTheory/MonoidLocalization/Basic.lean, line 7](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/GroupTheory/MonoidLocalization/Basic.lean#L7) (StacksCore). References: EGA 0 (10.3.1.1); EGA 0 (1.2.2); SGA 7 XXI (5.0), “more general”.
- [`IsLocalization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/Defs.lean, line 7](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Localization/Defs.lean#L7) (StacksCore). References: EGA I (1.3.1), “more general”.

## Tag 00CP, a proposition

[Tag 00CP](https://stacks.math.columbia.edu/tag/00CP) in the Stacks Project.

Declarations registered for the tag:

- [`IsLocalization.lift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.lift#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/Defs.lean, line 8](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Localization/Defs.lean#L8) (StacksCore). References: EGA 0 (1.2.4); EGA 0 (7.6.6).

## Tag 00CQ, a lemma

[Tag 00CQ](https://stacks.math.columbia.edu/tag/00CQ) in the Stacks Project.

Declarations registered for the tag:

- [`IsLocalization.subsingleton_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.subsingleton_iff#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/Defs.lean, line 9](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Localization/Defs.lean#L9) (StacksCore). References: EGA 0 (7.6.4), “Discrete topology on A”.

## Tag 07JY, a lemma

[Tag 07JY](https://stacks.math.columbia.edu/tag/07JY) in the Stacks Project.

**`ModuleCat.invertibleSMulEquivalentLocalizationModuleCat`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Category/ModuleCat/Localization.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Category/ModuleCat/Localization.lean#L283).

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

- [`LocalizedModule`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocalizedModule#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Module/LocalizedModule/Basic.lean, line 7](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Module/LocalizedModule/Basic.lean#L7) (StacksCore). References: EGA 0 (1.2.2); EGA I (1.1.1), “more general”; EGA I (1.3.1), “more general”.

## Tag 07K0, a lemma

[Tag 07K0](https://stacks.math.columbia.edu/tag/07K0) in the Stacks Project.

Declarations registered for the tag:

- [`IsLocalizedModule.lift_unique`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalizedModule.lift_unique#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Module/LocalizedModule/Basic.lean, line 8](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Module/LocalizedModule/Basic.lean#L8) (StacksCore). References: EGA 0 (1.2.4), “uniqueness of v*”.

## Tag 02C5, an example

[Tag 02C5](https://stacks.math.columbia.edu/tag/02C5) in the Stacks Project.

Declarations registered for the tag:

- [`Localization.Away`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Localization.Away#doc) registered with `add_to_stacks` in [StacksCore/GroupTheory/MonoidLocalization/Away.lean, line 7](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/GroupTheory/MonoidLocalization/Away.lean#L7) (StacksCore): “2”. References: EGA 0 (1.2.3); EGA 0 (7.6.15), “special case”; EGA I (1.3.1); EGA IV (10.4.4).
- [`Localization.AtPrime`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Localization.AtPrime#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/AtPrime/Basic.lean, line 7](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Localization/AtPrime/Basic.lean#L7) (StacksCore): “1”. References: EGA 0 (10.3.1.1); EGA 0 (10.3.1.4); EGA 0 (16.3.1); EGA 0 (1.2.3); EGA 0 (1.2.7); EGA 0 (19.8.3); EGA I (1.1.1); EGA III (4.4.7); EGA IV (5.6.11); EGA IV (7.2.4); EGA IV (1.3.10); SGA 1 III (1.4).
- [`FractionRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FractionRing#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/FractionRing.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Localization/FractionRing.lean#L16) (StacksCore): “3”. References: EGA 0 (10.3.1.1); EGA 0 (1.2.2), “special case”; EGA 0 (21.8.8); EGA II (7.1.5); EGA IV (18.11.12).
- [`FractionRing.field`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FractionRing.field#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/FractionRing.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Localization/FractionRing.lean#L17) (StacksCore): “4”.

## Tag 00CR, a lemma

[Tag 00CR](https://stacks.math.columbia.edu/tag/00CR) in the Stacks Project.

**`LocalizedModule.equivAwayColimit`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Module/LocalizedModule/Colimit.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Module/LocalizedModule/Colimit.lean#L208).

> **Stacks 00CR.** `S⁻¹M = colim_{f ∈ S} M_f`: the localization of `M` at `S` is the
> directed colimit of the away-localizations `M_f` over `f ∈ S` with the divisibility
> preorder, with transition maps `M_f → M_g` for `f ∣ g` induced by the universal
> property.

```lean
noncomputable def equivAwayColimit : LocalizedModule S M ≃ₗ[R] AwayColimit S M
```

## Tag 02C6, a proposition

[Tag 02C6](https://stacks.math.columbia.edu/tag/02C6) in the Stacks Project.

Declarations registered for the tag:

- [`IsLocalization.localization_localization_isLocalization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.localization_localization_isLocalization#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/LocalizationLocalization.lean, line 8](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Localization/LocalizationLocalization.lean#L8) (StacksCore). References: EGA 0 (1.4.6), “special case”; EGA 0 (7.6.8), “partial”.

## Tag 02C7, a proposition

[Tag 02C7](https://stacks.math.columbia.edu/tag/02C7) in the Stacks Project.

**`LocalizedModule.equivLocalizedModuleLocalizedModule`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Module/LocalizedModule/LocalizationLocalization.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Module/LocalizedModule/LocalizationLocalization.lean#L67).

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

- [`LocalizedModule.map_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocalizedModule.map_exact#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Module/LocalizedModule/Exact.lean, line 7](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Module/LocalizedModule/Exact.lean#L7) (StacksCore). References: EGA 0 (1.3.2), “more general”; EGA 0 (6.3.1), “more general”.

## Tag 02C8, a lemma

[Tag 02C8](https://stacks.math.columbia.edu/tag/02C8) in the Stacks Project.

Declarations registered for the tag:

- [`localizedQuotientEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=localizedQuotientEquiv#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Module/LocalizedModule/Submodule.lean, line 7](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Module/LocalizedModule/Submodule.lean#L7) (StacksCore).

## Tag 00CT, a proposition

[Tag 00CT](https://stacks.math.columbia.edu/tag/00CT) in the Stacks Project.

**`IsLocalization.quotientEquiv`**, a def in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Localization/Ideal.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Localization/Ideal.lean#L30). The attribute's comment: “(2)”.

> Localization commutes with quotients: for any localization
> `Q` of `A/I` at the image `S̄` of `S`, there is a canonical algebra (in particular ring)
> isomorphism `S̄⁻¹(A/I) ≅ S⁻¹A/S⁻¹I`.

```lean
noncomputable def quotientEquiv : Q ≃ₐ[A ⧸ I] A_S ⧸ I.map (algebraMap A A_S)
```

Declarations registered for the tag:

- [`Ideal.localized'_eq_map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.localized'_eq_map#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/Ideal.lean, line 12](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Localization/Ideal.lean#L12) (StacksCore): “(1)”. References: EGA 0 (1.2.6), “partial”.

## Tag 00CU, a lemma

[Tag 00CU](https://stacks.math.columbia.edu/tag/00CU) in the Stacks Project.

**`Submodule.localized'_comap_restrictScalars`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Module/LocalizedModule/Submodule.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Module/LocalizedModule/Submodule.lean#L19). References: SGA 6 0 (2.11), “affine step”.

```lean
theorem localized'_comap_restrictScalars (N' : Submodule S N) :
    ((N'.restrictScalars R).comap f).localized' S p f = N'
```

**`Submodule.localized'_surjective`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Module/LocalizedModule/Submodule.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Module/LocalizedModule/Submodule.lean#L24). The attribute's comment: “existence form”.

```lean
theorem localized'_surjective : Function.Surjective (localized' S p f)
```

## Tag 02C9, a lemma

[Tag 02C9](https://stacks.math.columbia.edu/tag/02C9) in the Stacks Project.

Declarations registered for the tag:

- [`IsLocalization.map_under`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.map_under#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/Ideal.lean, line 13](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Localization/Ideal.lean#L13) (StacksCore). References: EGA 0 (1.2.6), “partial”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.9, Tag 00CM](https://stacks.math.columbia.edu/tag/00CM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
