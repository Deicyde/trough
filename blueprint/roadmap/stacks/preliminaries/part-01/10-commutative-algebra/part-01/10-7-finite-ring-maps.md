---
declaration: section
origin: cited
lean: Module.Finite.iff_scalarTower, RingHom.Finite.comp, Module.FinitePresentation.of_finite_of_finitePresentation, RingHom.FiniteType.of_finite
statement: formalized
proof: formalized
---

# 10.7 Finite ring maps

Section 10.7 of the Stacks Project, [Tag 0562](https://stacks.math.columbia.edu/tag/0562). 3 tags here are carried by 1 declaration of the repository (in StacksCore) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00GJ, a lemma

[Tag 00GJ](https://stacks.math.columbia.edu/tag/00GJ) in the Stacks Project.

**`Module.Finite.iff_scalarTower`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Finiteness/Basic.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Finiteness/Basic.lean#L15).

```lean
theorem Module.Finite.iff_scalarTower {R S M : Type*} [Semiring R] [Semiring S] [AddCommMonoid M]
    [Module R S] [Module R M] [Module S M] [Module.Finite R S] [IsScalarTower R S M] :
    Module.Finite R M ↔ Module.Finite S M
```

## Tag 00GL, a lemma

[Tag 00GL](https://stacks.math.columbia.edu/tag/00GL) in the Stacks Project.

Declarations registered for the tag:

- [`RingHom.Finite.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.Finite.comp#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Finiteness/Basic.lean, line 12](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Finiteness/Basic.lean#L12) (StacksCore). References: EGA II (6.1.5), “(ii), special case”.

## Tag 0D46, a lemma

[Tag 0D46](https://stacks.math.columbia.edu/tag/0D46) in the Stacks Project.

Declarations registered for the tag:

- [`Module.FinitePresentation.of_finite_of_finitePresentation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.FinitePresentation.of_finite_of_finitePresentation#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Finiteness/ModuleFinitePresentation.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Finiteness/ModuleFinitePresentation.lean#L10) (StacksCore). References: EGA IV (1.4.7), “necessity”.
- [`RingHom.FiniteType.of_finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.FiniteType.of_finite#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/FiniteType.lean, line 18](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/FiniteType.lean#L18) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.7, Tag 0562](https://stacks.math.columbia.edu/tag/0562)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
