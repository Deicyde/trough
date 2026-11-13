---
declaration: section
origin: cited
lean: LinearMap.exact_iff_homLeft, LinearMap.exact_iff_homRight, instIsLocalizedModuleLinearMapIdLocalizationLocalizedModuleMapOfFinitePresentation, Module.FinitePresentation.isLocalizedModule_mapExtendScalars, Module.FinitePresentation.isLocalizedModule_map
statement: formalized
proof: formalized
---

# 10.10 Internal Hom

Section 10.10 of the Stacks Project, [Tag 0581](https://stacks.math.columbia.edu/tag/0581). 2 tags here are carried by 2 declarations of the repository (all in StacksCore) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0582, a lemma

[Tag 0582](https://stacks.math.columbia.edu/tag/0582) in the Stacks Project.

**`LinearMap.exact_iff_homLeft`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Exact.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Exact.lean#L59). The attribute's comment: “part 2”.

```lean
theorem exact_iff_homLeft : (Function.Injective f ∧ Function.Exact f g) ↔
    ∀ (N : Type v) [AddCommGroup N] [Module R N],
      Function.Injective (compRight (M := N) ℕ f) ∧
      Function.Exact (compRight (M := N) ℕ f) (compRight (M := N) ℕ g)
```

**`LinearMap.exact_iff_homRight`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Exact.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Exact.lean#L81). The attribute's comment: “part 1”.

```lean
theorem exact_iff_homRight : (Function.Exact f g ∧ Function.Surjective g) ↔ ∀ (N : Type v)
    [AddCommGroup N] [Module R N], Function.Injective (lcomp ℕ N g) ∧
    Function.Exact (lcomp ℕ N g) (lcomp ℕ N f)
```

## Tag 0583, a lemma

[Tag 0583](https://stacks.math.columbia.edu/tag/0583) in the Stacks Project.

Declarations registered for the tag:

- [`instIsLocalizedModuleLinearMapIdLocalizationLocalizedModuleMapOfFinitePresentation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=instIsLocalizedModuleLinearMapIdLocalizationLocalizedModuleMapOfFinitePresentation#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Module/FinitePresentation.lean, line 11](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Module/FinitePresentation.lean#L11) (StacksCore): “part 1”. References: EGA 0 (1.3.5); EGA 0 (1.5.3), “special case”; EGA 0 (1.5.5), “special case”.
- [`Module.FinitePresentation.isLocalizedModule_mapExtendScalars`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.FinitePresentation.isLocalizedModule_mapExtendScalars#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Module/FinitePresentation.lean, line 13](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Module/FinitePresentation.lean#L13) (StacksCore): “part 1”. References: EGA 0 (1.3.5), “more general”.
- [`Module.FinitePresentation.isLocalizedModule_map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.FinitePresentation.isLocalizedModule_map#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Module/FinitePresentation.lean, line 14](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Module/FinitePresentation.lean#L14) (StacksCore): “part 2”. References: EGA 0 (1.3.5), “more general”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.10, Tag 0581](https://stacks.math.columbia.edu/tag/0581)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
