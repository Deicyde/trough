---
declaration: section
origin: cited
lean: Fork, Fork.IsLimit.mk, HasEqualizer, equalizer
statement: formalized
proof: formalized
---

# 4.10 Equalizers

Section 4.10 of the Stacks Project, [Tag 0027](https://stacks.math.columbia.edu/tag/0027). 1 tag here is carried by 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0028, a definition

[Tag 0028](https://stacks.math.columbia.edu/tag/0028) in the Stacks Project.

Declarations registered for the tag:

- [`Fork`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Fork#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/SpecificLimits.lean#L37) (StacksCore): “An equalizer is a limiting fork, so this in combination with `IsLimit` covers equalizers. API specific to equalizers is provided in the namespace `Fork.IsLimit`, while API that holds more generally (like uniqueness up to isomorphism) is provided in the namespace `IsLimit`.”.
- [`Fork.IsLimit.mk`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Fork.IsLimit.mk#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/SpecificLimits.lean#L41) (StacksCore): “A constructor for `IsLimit` using the usual data of an equalizer”.
- [`HasEqualizer`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HasEqualizer#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/SpecificLimits.lean#L43) (StacksCore): “Prop-valued typeclass stating that two morphisms have an equalizer”.
- [`equalizer`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=equalizer#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/SpecificLimits.lean#L44) (StacksCore): “A choice of equalizer, when one exists”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.10, Tag 0027](https://stacks.math.columbia.edu/tag/0027)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
