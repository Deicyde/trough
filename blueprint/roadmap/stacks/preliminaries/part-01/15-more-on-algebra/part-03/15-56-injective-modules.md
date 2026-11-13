---
declaration: section
origin: cited
lean: Module.injective_iff_exact_linearYoneda, CategoryTheory.Abelian.comparison, CategoryTheory.Abelian.isCanonicalExtOneComparison_comparison, CategoryTheory.Abelian.eq_comparison_of_isCanonical, Module.injective_iff_subsingleton_ext_one, CategoryTheory.injective_iff_subsingleton_ext_one, ModuleCat.injective_iff_subsingleton_ext_quotient_one, ModuleCat.ext_quotient_one_subsingleton_iff
statement: formalized
proof: formalized
---

# 15.56 Injective modules

Section 15.56 of the Stacks Project, [Tag 01D8](https://stacks.math.columbia.edu/tag/01D8). 9 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AVD, a definition

[Tag 0AVD](https://stacks.math.columbia.edu/tag/0AVD) in the Stacks Project.

**`Module.injective_iff_exact_linearYoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Injective/Criteria.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Injective/Criteria.lean#L74).

> **Stacks 0AVD.** An `R`-module `J` is injective if and only if its contravariant Hom
> functor `Hom_R(-, J)` is exact.
>
> Exactness of a functor out of `(ModuleCat R)ᵒᵖ` is tested after composing with the forgetful
> functor to abelian groups, where the composite is the preadditive Yoneda functor at `J`, for
> which Mathlib already characterises injectivity.

```lean
theorem Module.injective_iff_exact_linearYoneda (R : Type u) [CommRing R]
    (J : Type v) [AddCommGroup J] [Module R J] :
    Module.Injective R J ↔
      exactFunctor _ _ ((linearYoneda R (ModuleCat.{v} R)).obj (ModuleCat.of R J))
```

## Tag 0AUL, a lemma

[Tag 0AUL](https://stacks.math.columbia.edu/tag/0AUL) in the Stacks Project.

**`CategoryTheory.Abelian.comparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/YonedaExtOne.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/YonedaExtOne.lean#L205). The attribute's comment: “the comparison itself; `isCanonicalExtOneComparison_comparison` is its defining properties and `eq_comparison_of_isCanonical` their uniqueness”.

> **The canonical comparison data.** Its equivalence is `comparisonEquiv`, and its covariant
> and contravariant maps are Yoneda composition with `Ext.mk₀` read through that equivalence.

```lean
noncomputable def comparison : ExtOneComparison (C := C)
```

**`CategoryTheory.Abelian.isCanonicalExtOneComparison_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/YonedaExtOne.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/YonedaExtOne.lean#L243). The attribute's comment: “the comparison has the announced properties: canonicity, representation of the two maps by pushout and pullback, naturality in both variables, additivity for Baer sums, and agreement with both connecting maps”. References: EGA 0 (12.3.2), “more general”; SGA 7 VII (3.4), “special case”.

> **The comparison is canonical.** `comparison` sends a short exact sequence to its derived
> extension class, represents its covariant and contravariant maps by pushout and pullback of
> short exact sequences, is natural in both variables, takes Baer sums to sums in `Ext¹`, and
> matches the boundary maps of the two long exact `Ext` sequences.

```lean
theorem isCanonicalExtOneComparison_comparison :
    IsCanonicalExtOneComparison (comparison (C := C))
```

**`CategoryTheory.Abelian.eq_comparison_of_isCanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/YonedaExtOne.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/YonedaExtOne.lean#L282). The attribute's comment: “uniqueness of the canonical comparison”.

> **The canonical comparison is unique.** Any comparison with the properties of
> `IsCanonicalExtOneComparison` is `comparison`.

```lean
theorem eq_comparison_of_isCanonical (c' : ExtOneComparison (C := C))
    (hc' : IsCanonicalExtOneComparison c') : c' = comparison
```

## Tag 0AVE, a lemma

[Tag 0AVE](https://stacks.math.columbia.edu/tag/0AVE) in the Stacks Project.

**`Module.injective_iff_subsingleton_ext_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Injective/Criteria.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Injective/Criteria.lean#L152).

> **Stacks 0AVE.** An `R`-module `J` is injective if and only if `Ext¹_R(M, J)` vanishes for
> every `R`-module `M`.
>
> Mathlib's `CategoryTheory.injective_iff_subsingleton_ext_one` is this criterion for an object of
> an abelian category with an `Ext` theory; here it is read off for modules, the quantifier running
> over `R`-modules rather than over objects of `ModuleCat R`. The two agree because every object of
> `ModuleCat.{v} R` is `ModuleCat.of R` of its own carrier.

```lean
theorem Module.injective_iff_subsingleton_ext_one (R : Type u) [Ring R] [Small.{v} R]
    (J : Type v) [AddCommGroup J] [Module R J] :
    Module.Injective R J ↔
      ∀ (M : Type v) [AddCommGroup M] [Module R M],
        Subsingleton (Abelian.Ext (ModuleCat.of R M) (ModuleCat.of R J) 1)
```

Declarations registered for the tag:

- [`CategoryTheory.injective_iff_subsingleton_ext_one`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.injective_iff_subsingleton_ext_one#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/Injective/Criteria.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Injective/Criteria.lean#L167) (StacksFrontier). References: SGA 6 I (5.7), “(ii) ⇒ (i)”.

## Tag 0AVF, a lemma

[Tag 0AVF](https://stacks.math.columbia.edu/tag/0AVF) in the Stacks Project.

Declarations registered for the tag:

- [`ModuleCat.injective_iff_subsingleton_ext_quotient_one`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ModuleCat.injective_iff_subsingleton_ext_quotient_one#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/Injective/Criteria.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Injective/Criteria.lean#L170) (StacksFrontier): “injectivity is equivalent to vanishing Ext^1 from quotients by ideals”.
- [`ModuleCat.ext_quotient_one_subsingleton_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ModuleCat.ext_quotient_one_subsingleton_iff#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/Injective/Criteria.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Injective/Criteria.lean#L173) (StacksFrontier): “vanishing Ext^1 is equivalent to extending maps from ideals”.

## Tag 01D9, a definition

[Tag 01D9](https://stacks.math.columbia.edu/tag/01D9) in the Stacks Project.

**`CharacterModule.dualFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/CharacterModule/Duality.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/CharacterModule/Duality.lean#L55). The attribute's comment: “the contravariant functor `M ↦ M^∨`”.

> The contravariant functor `M ↦ M^∨ = Hom_ℤ(M, ℚ/ℤ)` on modules over a commutative ring,
> acting on a linear map by precomposition (`CharacterModule.dual`).

```lean
noncomputable def dualFunctor (R : Type u) [CommRing R] :
    (ModuleCat.{u} R)ᵒᵖ ⥤ ModuleCat.{u} R
```

**`freeModuleCoverFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/CharacterModule/EnoughInjectives.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/CharacterModule/EnoughInjectives.lean#L108). The attribute's comment: “the free module on the underlying set of a module, with its natural surjection”.

> The functor sending an `R`-module `M` to the natural epimorphism `F(M) → M`, where `F(M)` is
> the free module on the underlying set of `M`. Landing in the full subcategory of the arrow
> category spanned by the epimorphisms retains the surjectivity of each cover.

```lean
noncomputable def freeModuleCoverFunctor (R : Type u) [CommRing R] :
    ModuleCat.{u} R ⥤ (MorphismProperty.epimorphisms (ModuleCat.{u} R)).Arrow ⊤ ⊤
```

## Tag 01DA, a lemma

[Tag 01DA](https://stacks.math.columbia.edu/tag/01DA) in the Stacks Project.

**`CharacterModule.dualFunctor_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/CharacterModule/Duality.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/CharacterModule/Duality.lean#L118).

> The contravariant character-dual functor on modules over a commutative ring is exact.

```lean
theorem dualFunctor_exact (R : Type u) [CommRing R] :
    exactFunctor (ModuleCat.{u} R)ᵒᵖ (ModuleCat.{u} R) (dualFunctor R)
```

## Tag 01DB, a lemma

[Tag 01DB](https://stacks.math.columbia.edu/tag/01DB) in the Stacks Project.

**`CharacterModule.eval_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/CharacterModule/Duality.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/CharacterModule/Duality.lean#L140).

> The canonical evaluation map from an additive commutative group into its double character
> module is injective.

```lean
theorem eval_injective (M : Type u) [AddCommGroup M] :
    Function.Injective (AddMonoidHom.eval : M →+ CharacterModule (CharacterModule M))
```

## Tag 01DC, a lemma

[Tag 01DC](https://stacks.math.columbia.edu/tag/01DC) in the Stacks Project.

**`jModule_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/CharacterModule/EnoughInjectives.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/CharacterModule/EnoughInjectives.lean#L141).

> **Stacks Tag 01DC, Lemma 15.56.8.**
> For every `R`-module `M` (with `R` commutative), the `R`-module `J(M) = (F(M^∨))^∨` is
> injective. This is `characterModule_finsupp_injective` for the index type `M^∨`.

```lean
theorem jModule_injective (R : Type*) [CommRing R] (M : Type*) [AddCommGroup M] :
    Module.Injective R (JModule R M)
```

## Tag 01DD, a lemma

[Tag 01DD](https://stacks.math.columbia.edu/tag/01DD) in the Stacks Project.

**`moduleCat_hasFunctorialInjectiveEmbeddings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/CharacterModule/EnoughInjectives.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/CharacterModule/EnoughInjectives.lean#L254).

> **Stacks Project, Tag 01DD.** The canonical maps `M → J(M) = (F(M^∨))^∨` form a covariant
> functor from `R`-modules to arrows of `R`-modules whose source projection is the identity, each
> of whose components is a monomorphism, and each of whose targets is an injective module.

```lean
theorem moduleCat_hasFunctorialInjectiveEmbeddings :
    IsFunctorialInjectiveEmbeddings₁ (ModuleCat.{max u v} R) (jModuleArrowFunctor R) ∧
      IsFunctorialInjectiveEmbeddings₂ (ModuleCat.{max u v} R) (jModuleArrowFunctor R) ∧
        IsFunctorialInjectiveEmbeddings₃ (ModuleCat.{max u v} R) (jModuleArrowFunctor R)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.56, Tag 01D8](https://stacks.math.columbia.edu/tag/01D8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
