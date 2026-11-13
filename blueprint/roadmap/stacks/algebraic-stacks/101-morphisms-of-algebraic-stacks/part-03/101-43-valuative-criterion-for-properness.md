---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.isProper_iff_valuativeCriterion
statement: formalized
proof: formalized
---

# 101.43 Valuative criterion for properness

Section 101.43 of the Stacks Project, [Tag 0CLY](https://stacks.math.columbia.edu/tag/0CLY). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CLZ, a lemma

[Tag 0CLZ](https://stacks.math.columbia.edu/tag/0CLZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isProper_iff_valuativeCriterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionProperness.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionProperness.lean#L159).

> **Stacks 0CLZ.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` which is of
> finite type (**Stacks 06FS**, part (2)) and quasi-separated (**Stacks 04YW**). Then `f` is proper
> (**Stacks 0CL5**) if and only if it satisfies both the uniqueness part (**Stacks 0CLG**) and the
> existence part (**Stacks 0CLK**) of the valuative criterion.
>
> Properness is separatedness, finite type and universal closedness, and under the standing
> hypotheses the equivalence is the conjunction of two equivalences: separatedness is the
> uniqueness part, by **Stacks 0CLU** forwards and **Stacks 0CLT** backwards, and universal
> closedness is the existence part, by **Stacks 0CLX** forwards and **Stacks 0CLW** backwards.

```lean
theorem isProper_iff_valuativeCriterion (f : 𝒳 ⟶ 𝒴)
    (hft : IsFiniteType B S hS f)
    (hqs : IsQuasiSeparated B S hS f) :
    IsProper B S hS f ↔
      ValuativeCriterion.Uniqueness B S hS f ∧ ValuativeCriterion.Existence B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.43, Tag 0CLY](https://stacks.math.columbia.edu/tag/0CLY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
