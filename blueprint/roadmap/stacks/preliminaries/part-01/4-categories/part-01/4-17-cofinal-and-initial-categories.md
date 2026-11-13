---
declaration: section
origin: cited
lean: Final.isColimitWhiskerEquiv, Initial, CategoryTheory.Functor.Initial, Initial.limitIso, Initial.isLimitWhiskerEquiv, CategoryTheory.Functor.final_of_isConnected_fiber, CategoryTheory.final_fst, CategoryTheory.final_snd
statement: formalized
proof: formalized
---

# 4.17 Cofinal and initial categories

Section 4.17 of the Stacks Project, [Tag 09WN](https://stacks.math.columbia.edu/tag/09WN). 5 tags here are carried by 1 declaration of the repository (in StacksCore) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04E7, a lemma

[Tag 04E7](https://stacks.math.columbia.edu/tag/04E7) in the Stacks Project.

Declarations registered for the tag:

- [`Final.isColimitWhiskerEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Final.isColimitWhiskerEquiv#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/FinalFunctors.lean, line 13](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/FinalFunctors.lean#L13) (StacksCore): “either colimit exists iff the other does”.

## Tag 09WP, a definition

[Tag 09WP](https://stacks.math.columbia.edu/tag/09WP) in the Stacks Project.

Declarations registered for the tag:

- [`Initial`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Initial#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/FinalFunctors.lean, line 15](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/FinalFunctors.lean#L15) (StacksCore).
- [`CategoryTheory.Functor.Initial`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.Initial#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/SingletonCoveringsNotInitial.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/SingletonCoveringsNotInitial.lean#L256) (StacksFrontier): “the definition of an initial functor, and so of an initial subcategory”. References: SGA 4 V (8.1.4), “special case”.

## Tag 002R, a lemma

[Tag 002R](https://stacks.math.columbia.edu/tag/002R) in the Stacks Project.

Declarations registered for the tag:

- [`Initial.limitIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Initial.limitIso#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/FinalFunctors.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/FinalFunctors.lean#L17) (StacksCore).
- [`Initial.isLimitWhiskerEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Initial.isLimitWhiskerEquiv#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/FinalFunctors.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/FinalFunctors.lean#L18) (StacksCore): “either limit exists iff the other does”.

## Tag 05US, a lemma

[Tag 05US](https://stacks.math.columbia.edu/tag/05US) in the Stacks Project.

**`CategoryTheory.Functor.final_of_isConnected_fiber`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/FinalFunctors.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/FinalFunctors.lean#L48). The attribute's comment: “implies the lemma via `04E7`”.

> Any functor `F : I ⥤ I'` whose fibre categories are all connected and which is surjective on
> arrows is final.

```lean
lemma CategoryTheory.Functor.final_of_isConnected_fiber {I I' : Type*} [Category* I] [Category* I']
    (F : I ⥤ I') [∀ i, IsConnected (F.Fiber i)] [F.SurjectiveOnArrows] :
    F.Final
```

## Tag 0A2B, a lemma

[Tag 0A2B](https://stacks.math.columbia.edu/tag/0A2B) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.final_fst`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.final_fst#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/FinalFunctors.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/FinalFunctors.lean#L73) (StacksCore): “variant for the first projection; implies the lemma via `04E7`”.
- [`CategoryTheory.final_snd`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.final_snd#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/FinalFunctors.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/FinalFunctors.lean#L75) (StacksCore): “variant for the second projection; implies the lemma via `04E7`”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.17, Tag 09WN](https://stacks.math.columbia.edu/tag/09WN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
