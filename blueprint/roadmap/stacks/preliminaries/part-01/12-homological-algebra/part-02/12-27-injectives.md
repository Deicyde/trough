---
declaration: section
origin: cited
lean: CategoryTheory.Injective, injective_tfae, CategoryTheory.Injective.instPiObj, CategoryTheory.EnoughInjectives, HasFunctorialInjectiveEmbeddings
statement: formalized
proof: formalized
---

# 12.27 Injectives

Section 12.27 of the Stacks Project, [Tag 0134](https://stacks.math.columbia.edu/tag/0134). 5 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0135, a definition

[Tag 0135](https://stacks.math.columbia.edu/tag/0135) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Injective#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean#L19) (StacksFrontier). References: SGA 4 I (7.11).

## Tag 0136, a lemma

[Tag 0136](https://stacks.math.columbia.edu/tag/0136) in the Stacks Project.

**`injective_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/Characterization.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Injective/Characterization.lean#L115). The attribute's comment: “Condition (2) appears twice: as `HomToIsExact` (`preadditiveYoneda.obj I` sends short exact sequences to short exact sequences, Stacks 010N (4)) and, as the fifth entry, as `preadditiveYoneda.obj I` commuting with finite limits and colimits (Definition 0034); these agree by Mathlib's `Functor.exact_tfae`. Condition (4) is `Subsingleton (Abelian.Ext B I 1)` for Mathlib's `HasExt.standard`; (1)⇒(4) is Mathlib's `Abelian.Ext.subsingleton_of_injective`, (4)⇒(1) uses `Abelian.Ext.contravariant_sequence_exact₁`, (1)⇒(3) is `ShortComplex.ShortExact.splittingOfInjective`.”.

> **Characterisation of injective objects.** For an object `I` of an abelian category `𝒜`,
> the following are equivalent:
> 1. `I` is injective;
> 2. the functor `B ↦ Hom_𝒜(B, I)` is exact, in the form "sends short exact sequences to short
>    exact sequences" (`HomToIsExact`), and in the form of Categories, Definition 0034
>    "commutes with finite limits and finite colimits" (the last entry of the list);
> 3. every short exact sequence `0 ⟶ I ⟶ A ⟶ B ⟶ 0` is split (`EverySESStartingAtSplits`);
> 4. `Ext¹_𝒜(B, I) = 0` for every object `B`, for the `Ext` groups of `HasExt.standard 𝒜`.

```lean
theorem injective_tfae (I : 𝒜) :
    letI := HasExt.standard 𝒜
    List.TFAE [Injective I, HomToIsExact I, EverySESStartingAtSplits I,
      ∀ B : 𝒜, Subsingleton (Abelian.Ext B I 1),
      PreservesFiniteLimits (preadditiveYoneda.obj I) ∧
        PreservesFiniteColimits (preadditiveYoneda.obj I)]
```

## Tag 0137, a lemma

[Tag 0137](https://stacks.math.columbia.edu/tag/0137) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Injective.instPiObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Injective.instPiObj#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean#L21) (StacksFrontier).

## Tag 0138, a definition

[Tag 0138](https://stacks.math.columbia.edu/tag/0138) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.EnoughInjectives`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.EnoughInjectives#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean#L22) (StacksFrontier). References: EGA 0 (11.4.3); SGA 3 I (5.3.1.1); SGA 4 I (7.13); SGA 4 II (6.9); SGA 4 V (0.1.1); SGA 6 II (3.1).

## Tag 0139, a definition

[Tag 0139](https://stacks.math.columbia.edu/tag/0139) in the Stacks Project.

**`HasFunctorialInjectiveEmbeddings`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean#L136).

> The notion of *functorial injective embeddings* for an abelian category `𝒜`: there exists a
> functor `J : 𝒜 ⥤ Arrow 𝒜` satisfying the three conditions `IsFunctorialInjectiveEmbeddings₁`,
> `IsFunctorialInjectiveEmbeddings₂`, and `IsFunctorialInjectiveEmbeddings₃`.

```lean
def HasFunctorialInjectiveEmbeddings : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.27, Tag 0134](https://stacks.math.columbia.edu/tag/0134)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
