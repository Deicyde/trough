---
declaration: section
origin: cited
lean: SimplexCategory.δ, SimplexCategory.σ, SimplexCategory.morphismProperty_eq_top, SimplexCategory.δ_comp_δ, SimplexCategory.δ_comp_σ_of_le, SimplexCategory.δ_comp_σ_self, SimplexCategory.δ_comp_σ_succ, SimplexCategory.δ_comp_σ_of_gt
statement: formalized
proof: formalized
---

# 14.2 The category of finite ordered sets

Section 14.2 of the Stacks Project, [Tag 0164](https://stacks.math.columbia.edu/tag/0164). 4 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0165, a definition

[Tag 0165](https://stacks.math.columbia.edu/tag/0165) in the Stacks Project.

Declarations registered for the tag:

- [`SimplexCategory.δ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplexCategory.δ#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L33) (StacksFrontier): “δⁿⱼ : [n-1] → [n], the injection skipping j”. References: SGA 4 V (1.10); SGA 4 Vbis (5.1.0).
- [`SimplexCategory.σ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplexCategory.σ#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L34) (StacksFrontier): “σⁿⱼ : [n+1] → [n], the surjection hitting j twice”.

## Tag 0166, a lemma

[Tag 0166](https://stacks.math.columbia.edu/tag/0166) in the Stacks Project.

Declarations registered for the tag:

- [`SimplexCategory.morphismProperty_eq_top`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplexCategory.morphismProperty_eq_top#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L36) (StacksFrontier).

## Tag 0167, a lemma

[Tag 0167](https://stacks.math.columbia.edu/tag/0167) in the Stacks Project.

Declarations registered for the tag:

- [`SimplexCategory.δ_comp_δ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplexCategory.δ_comp_δ#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L38) (StacksFrontier): “(1)”.
- [`SimplexCategory.δ_comp_σ_of_le`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplexCategory.δ_comp_σ_of_le#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L39) (StacksFrontier): “(2)”.
- [`SimplexCategory.δ_comp_σ_self`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplexCategory.δ_comp_σ_self#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L40) (StacksFrontier): “(3), σⱼ ∘ δⱼ = id”.
- [`SimplexCategory.δ_comp_σ_succ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplexCategory.δ_comp_σ_succ#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L41) (StacksFrontier): “(3), σⱼ ∘ δⱼ₊₁ = id”.
- [`SimplexCategory.δ_comp_σ_of_gt`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplexCategory.δ_comp_σ_of_gt#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L42) (StacksFrontier): “(4)”.
- [`SimplexCategory.σ_comp_σ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplexCategory.σ_comp_σ#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L43) (StacksFrontier): “(5)”.

## Tag 0168, a lemma

[Tag 0168](https://stacks.math.columbia.edu/tag/0168) in the Stacks Project.

**`SimplexCategoryGenRel.toSimplexCategory_full_faithful_bijective_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplexCategory/GeneratorsRelations/ToSimplexCategory.lean, line 492](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplexCategory/GeneratorsRelations/ToSimplexCategory.lean#L492).

> **Stacks 0168**.
> The category `Δ` is presented by the face and degeneracy generators and the simplicial
> relations: the canonical functor from the category defined by those generators and relations is
> full and faithful and is bijective on objects. Thus every morphism is generated by faces and
> degeneracies, and every equality between such composites follows from the defining relations.

```lean
public theorem toSimplexCategory_full_faithful_bijective_obj :
    toSimplexCategory.Full ∧ toSimplexCategory.Faithful ∧
      Function.Bijective toSimplexCategory.obj
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.2, Tag 0164](https://stacks.math.columbia.edu/tag/0164)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
