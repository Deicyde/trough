---
declaration: section
origin: cited
lean: Cofork, Cofork.IsColimit.mk, HasCoequalizer, coequalizer
statement: formalized
proof: formalized
---

# 4.11 Coequalizers

Section 4.11 of the Stacks Project, [Tag 0029](https://stacks.math.columbia.edu/tag/0029). 1 tag here is carried by 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 002A, a definition

[Tag 002A](https://stacks.math.columbia.edu/tag/002A) in the Stacks Project.

Declarations registered for the tag:

- [`Cofork`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Cofork#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L46) (StacksCore): “A coequalizer is a limiting cofork, so this in combination with `IsColimit` covers coequalizers. API specific to coequalizers is provided in the namespace `Cofork.IsColimit`, while API that holds more generally (like uniqueness up to isomorphism) is provided in the namespace `IsColimit`.”.
- [`Cofork.IsColimit.mk`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Cofork.IsColimit.mk#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L50) (StacksCore): “A constructor for `IsColimit` using the usual data of a coequalizer”.
- [`HasCoequalizer`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HasCoequalizer#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L52) (StacksCore): “Prop-valued typeclass stating that two morphisms have a coequalizer”.
- [`coequalizer`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=coequalizer#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L54) (StacksCore): “A choice of coequalizer, when one exists”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.11, Tag 0029](https://stacks.math.columbia.edu/tag/0029)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
