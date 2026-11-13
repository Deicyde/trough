---
declaration: section
origin: cited
lean: Adjunction.mkOfHomEquiv, isLeftAdjoint_of_rightAdjointObjIsDefined_eq_top, CategoryTheory.Adjunction.fullyFaithfulLeftOfComp, CategoryTheory.Adjunction.fullyFaithfulRightOfComp, Adjunction.fullyFaithfulLOfCompIsoId, Adjunction.unit_isIso_of_L_fully_faithful, Adjunction.fullyFaithfulLOfIsIsoUnit, Adjunction.fullyFaithfulROfCompIsoId
statement: formalized
proof: formalized
---

# 4.24 Adjoint functors

Section 4.24 of the Stacks Project, [Tag 0036](https://stacks.math.columbia.edu/tag/0036). 9 tags here are carried by 2 declarations of the repository (all in StacksCore) and 16 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0037, a definition

[Tag 0037](https://stacks.math.columbia.edu/tag/0037) in the Stacks Project.

Declarations registered for the tag:

- [`Adjunction.mkOfHomEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Adjunction.mkOfHomEquiv#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 16](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L16) (StacksCore): “constructor using the hom-isomorphism definition”.

## Tag 0A8B, a lemma

[Tag 0A8B](https://stacks.math.columbia.edu/tag/0A8B) in the Stacks Project.

Declarations registered for the tag:

- [`isLeftAdjoint_of_rightAdjointObjIsDefined_eq_top`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isLeftAdjoint_of_rightAdjointObjIsDefined_eq_top#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L18) (StacksCore).

## Tag 0FWV, a lemma

[Tag 0FWV](https://stacks.math.columbia.edu/tag/0FWV) in the Stacks Project.

**`CategoryTheory.Adjunction.fullyFaithfulLeftOfComp`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L22). The attribute's comment: “Case 1”.

> Given an adjunction `L ⊣ R`, if `L ⋙ R` is fully faithful `L` is too.

```lean
def Adjunction.fullyFaithfulLeftOfComp {C D : Type*} [Category C] [Category D]
    {L : C ⥤ D} {R : D ⥤ C} (adj : L ⊣ R) (h : (L ⋙ R).FullyFaithful) : L.FullyFaithful
```

**`CategoryTheory.Adjunction.fullyFaithfulRightOfComp`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L32). The attribute's comment: “Case 2”.

> Given an adjunction `L ⊣ R`, if `R ⋙ L` is fully faithful `R` is too.

```lean
def Adjunction.fullyFaithfulRightOfComp {C D : Type*} [Category C] [Category D]
    {L : C ⥤ D} {R : D ⥤ C} (adj : L ⊣ R) (h : (R ⋙ L).FullyFaithful) : R.FullyFaithful
```

## Tag 07RB, a lemma

[Tag 07RB](https://stacks.math.columbia.edu/tag/07RB) in the Stacks Project.

Declarations registered for the tag:

- [`Adjunction.fullyFaithfulLOfCompIsoId`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Adjunction.fullyFaithfulLOfCompIsoId#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L40) (StacksCore): “Part 1, (2) => (1)”.
- [`Adjunction.unit_isIso_of_L_fully_faithful`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Adjunction.unit_isIso_of_L_fully_faithful#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L41) (StacksCore): “Part 1, (1) => (3)”.
- [`Adjunction.fullyFaithfulLOfIsIsoUnit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Adjunction.fullyFaithfulLOfIsIsoUnit#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L42) (StacksCore): “Part 1, (3) => (1)”.
- [`Adjunction.fullyFaithfulROfCompIsoId`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Adjunction.fullyFaithfulROfCompIsoId#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L43) (StacksCore): “Part 2, (2) => (1)”.
- [`Adjunction.counit_isIso_of_R_fully_faithful`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Adjunction.counit_isIso_of_R_fully_faithful#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L44) (StacksCore): “Part 2, (1) => (3)”.
- [`Adjunction.fullyFaithfulROfIsIsoCounit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Adjunction.fullyFaithfulROfIsIsoCounit#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L45) (StacksCore): “Part 2, (3) => (1)”.

## Tag 0038, a lemma

[Tag 0038](https://stacks.math.columbia.edu/tag/0038) in the Stacks Project.

Declarations registered for the tag:

- [`instPreservesColimitsOfSizeOfIsLeftAdjoint`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=instPreservesColimitsOfSizeOfIsLeftAdjoint#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L47) (StacksCore).
- [`instPreservesLimitsOfSizeOfIsRightAdjoint`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=instPreservesLimitsOfSizeOfIsRightAdjoint#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L48) (StacksCore).

## Tag 0039, a lemma

[Tag 0039](https://stacks.math.columbia.edu/tag/0039) in the Stacks Project.

Declarations registered for the tag:

- [`Adjunction.leftAdjoint_preservesColimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Adjunction.leftAdjoint_preservesColimits#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L50) (StacksCore): “implies 0039 for left adjoints with `PreservesColimits.preservesFiniteColimits`”.
- [`Adjunction.rightAdjoint_preservesLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Adjunction.rightAdjoint_preservesLimits#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L52) (StacksCore): “implies 0039 for right adjoints with `PreservesLimits.preservesFiniteLimits`”.

## Tag 0GLL, a lemma

[Tag 0GLL](https://stacks.math.columbia.edu/tag/0GLL) in the Stacks Project.

Declarations registered for the tag:

- [`Adjunction.left_triangle_components`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Adjunction.left_triangle_components#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L55) (StacksCore): “first equation”.
- [`Adjunction.right_triangle_components`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Adjunction.right_triangle_components#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L56) (StacksCore): “second equation”.

## Tag 0B65, a lemma

[Tag 0B65](https://stacks.math.columbia.edu/tag/0B65) in the Stacks Project.

Declarations registered for the tag:

- [`conjugateEquiv_counit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=conjugateEquiv_counit#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L58) (StacksCore): “in components”.

## Tag 0DV0, a lemma

[Tag 0DV0](https://stacks.math.columbia.edu/tag/0DV0) in the Stacks Project.

Declarations registered for the tag:

- [`Adjunction.comp_counit_app`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Adjunction.comp_counit_app#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/AdjointFunctors.lean#L60) (StacksCore): “counit equation”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.24, Tag 0036](https://stacks.math.columbia.edu/tag/0036)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
