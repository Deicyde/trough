---
declaration: section
origin: cited
lean: BinaryCofan, BinaryCofan.IsColimit.mk, HasBinaryCoproduct, coprod
statement: formalized
proof: formalized
---

# 4.5 Coproducts of pairs

Section 4.5 of the Stacks Project, [Tag 04AN](https://stacks.math.columbia.edu/tag/04AN). 1 tag here is carried by 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04AO, a definition

[Tag 04AO](https://stacks.math.columbia.edu/tag/04AO) in the Stacks Project.

Declarations registered for the tag:

- [`BinaryCofan`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=BinaryCofan#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L24) (StacksCore): “A coproduct is a limiting binary cofan, so this in combination with `IsColimit` covers binary coproducts. API specific to binary coproducts is provided in the namespace `BinaryCofan.IsColimit`, while API that holds more generally (like uniqueness up to isomorphism) is provided in the namespace `IsColimit`.”.
- [`BinaryCofan.IsColimit.mk`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=BinaryCofan.IsColimit.mk#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L28) (StacksCore): “A constructor for `IsColimit` using the usual data of a binary coproduct”.
- [`HasBinaryCoproduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HasBinaryCoproduct#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L30) (StacksCore): “Prop-valued typeclass stating that two objects have a product”.
- [`coprod`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=coprod#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L32) (StacksCore): “A choice of coproduct, when one exists”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.5, Tag 04AN](https://stacks.math.columbia.edu/tag/04AN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
