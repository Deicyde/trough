---
declaration: section
origin: cited
lean: PreservesFiniteLimits, PreservesFiniteColimits, leftExactFunctor, rightExactFunctor, exactFunctor, exactFunctor_iff, CategoryTheory.Limits.preservesFiniteLimits_tfae_of_hasFiniteLimits, preservesFiniteLimits_of_preservesEqualizers_and_finiteProducts
statement: formalized
proof: formalized
---

# 4.23 Exact functors

Section 4.23 of the Stacks Project, [Tag 0033](https://stacks.math.columbia.edu/tag/0033). 3 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 10 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0034, a definition

[Tag 0034](https://stacks.math.columbia.edu/tag/0034) in the Stacks Project.

Declarations registered for the tag:

- [`PreservesFiniteLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PreservesFiniteLimits#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L59) (StacksCore): “Prop-valued typeclass for left exact functors”.
- [`PreservesFiniteColimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PreservesFiniteColimits#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L60) (StacksCore): “Prop-valued typeclass for right exact functors”.
- [`leftExactFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=leftExactFunctor#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Limits/ExactFunctor.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/ExactFunctor.lean#L22) (StacksFrontier): “Part (1), left exact functors: the property `leftExactFunctor C D` of a functor `F : C ⥤ D`, which is `PreservesFiniteLimits F` (`leftExactFunctor_iff`); left exact functors form the full subcategory `C ⥤ₗ D`.”.
- [`rightExactFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=rightExactFunctor#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Limits/ExactFunctor.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/ExactFunctor.lean#L26) (StacksFrontier): “Part (2), right exact functors: the property `rightExactFunctor C D` of a functor `F : C ⥤ D`, which is `PreservesFiniteColimits F` (`rightExactFunctor_iff`); right exact functors form the full subcategory `C ⥤ᵣ D`.”.
- [`exactFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=exactFunctor#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Limits/ExactFunctor.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/ExactFunctor.lean#L30) (StacksFrontier): “Part (3), exact functors: the property `exactFunctor C D` of a functor `F : C ⥤ D`, which is `PreservesFiniteLimits F ∧ PreservesFiniteColimits F`, i.e. both left and right exact (`exactFunctor_iff`, `exactFunctor_le_leftExactFunctor`, `exactFunctor_le_rightExactFunctor`); exact functors form the full subcategory `C ⥤ₑ D`.”.
- [`exactFunctor_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=exactFunctor_iff#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Limits/ExactFunctor.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/ExactFunctor.lean#L36) (StacksFrontier): “Part (3): a functor is exact iff it preserves finite limits and finite colimits.”.

## Tag 0035, a lemma

[Tag 0035](https://stacks.math.columbia.edu/tag/0035) in the Stacks Project.

**`CategoryTheory.Limits.preservesFiniteLimits_tfae_of_hasFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Constructions/LimitsOfProductsAndEqualizers.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Constructions/LimitsOfProductsAndEqualizers.lean#L32). The attribute's comment: “Left exactness is `PreservesFiniteLimits`; `(2) → (1)` is Mathlib's `preservesFiniteLimits_of_preservesEqualizers_and_finiteProducts` and `(3) → (1)` is `preservesFiniteLimits_of_preservesTerminal_and_pullbacks`, while `(1) → (2)` and `(1) → (3)` hold because finite products, equalizers, the empty limit and pullbacks are finite limits.”.

> A functor out of a category with finite limits is left exact if and only if it preserves
> finite products and equalizers, if and only if it preserves the terminal object and pullbacks.

```lean
theorem preservesFiniteLimits_tfae_of_hasFiniteLimits [HasFiniteLimits C] (F : C ⥤ D) :
    List.TFAE [PreservesFiniteLimits F,
      PreservesFiniteProducts F ∧ PreservesLimitsOfShape WalkingParallelPair F,
      PreservesLimitsOfShape (Discrete.{0} PEmpty) F ∧ PreservesLimitsOfShape WalkingCospan F]
```

Declarations registered for the tag:

- [`preservesFiniteLimits_of_preservesEqualizers_and_finiteProducts`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=preservesFiniteLimits_of_preservesEqualizers_and_finiteProducts#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L62) (StacksCore): “2. => 1.”.
- [`preservesFiniteLimits_of_preservesTerminal_and_pullbacks`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=preservesFiniteLimits_of_preservesTerminal_and_pullbacks#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L63) (StacksCore): “3. => 1.”.

## Tag 0GMN, a lemma

[Tag 0GMN](https://stacks.math.columbia.edu/tag/0GMN) in the Stacks Project.

**`CategoryTheory.Limits.preservesFiniteColimits_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/RightExactFunctorCharacterization.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/RightExactFunctorCharacterization.lean#L54). The attribute's comment: “The complete statement: the equivalence of (1), (2) and (3) for a functor out of a category with all finite colimits.”.

> Let `F : C ⥤ D` be a functor and suppose all finite colimits exist in `C`. The following
> are equivalent:
> 1. `F` is right exact (preserves finite colimits);
> 2. `F` commutes with finite coproducts and coequalizers;
> 3. `F` transforms initial objects of `C` into initial objects of `D`, and commutes with pushouts.
>
> The implications `2 → 1` and `3 → 1` are Mathlib's
> `preservesFiniteColimits_of_preservesCoequalizers_and_finiteCoproducts` and
> `preservesFiniteColimits_of_preservesInitial_and_pushouts`; the implications out of `1` hold since
> the walking parallel pair, the finite discrete categories, the empty category and the walking span
> are finite categories.

```lean
theorem preservesFiniteColimits_tfae [HasFiniteColimits C] (F : C ⥤ D) :
    List.TFAE
      [PreservesFiniteColimits F,
        PreservesFiniteCoproducts F ∧ PreservesColimitsOfShape WalkingParallelPair F,
        (∀ X : C, IsInitial X → Nonempty (IsInitial (F.obj X))) ∧
          PreservesColimitsOfShape WalkingSpan F]
```

Declarations registered for the tag:

- [`preservesFiniteColimits_of_preservesCoequalizers_and_finiteCoproducts`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=preservesFiniteColimits_of_preservesCoequalizers_and_finiteCoproducts#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L65) (StacksCore): “2. => 1.”.
- [`preservesFiniteColimits_of_preservesInitial_and_pushouts`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=preservesFiniteColimits_of_preservesInitial_and_pushouts#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L66) (StacksCore): “3. => 1.”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.23, Tag 0033](https://stacks.math.columbia.edu/tag/0033)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
