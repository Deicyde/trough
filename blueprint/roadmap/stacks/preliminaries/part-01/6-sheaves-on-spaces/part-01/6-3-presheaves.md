---
declaration: section
origin: cited
lean: TopCat.Presheaf, TopCat.instCategoryPresheaf, constantPresheaf
statement: formalized
proof: formalized
---

# 6.3 Presheaves

Section 6.3 of the Stacks Project, [Tag 006D](https://stacks.math.columbia.edu/tag/006D). 2 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 006E, a definition

[Tag 006E](https://stacks.math.columbia.edu/tag/006E) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.Presheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Basic.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/Basic.lean#L28) (StacksFrontier): “a presheaf of sets on `X` is a functor `(Opens X)ᵒᵖ ⥤ Type u`, whose `map_id` and `map_comp` are the axioms `ρ^U_U = id` and `ρ^U_W = ρ^V_W ∘ ρ^U_V`; the objects of `PSh(X)`”. References: SGA 3 IV (4.3.1), “special case”; SGA 3 IV (4.3.17), “special case”; SGA 4 I (1.2), “special case”; SGA 4 II (6.0), “special case”; SGA 4½ Arcata (1.6.3), “special case”.
- [`TopCat.instCategoryPresheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.instCategoryPresheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Basic.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/Basic.lean#L31) (StacksFrontier): “morphisms of presheaves of sets are natural transformations, naturality being compatibility with the restriction maps; the category `PSh(X)`”. References: SGA 3 IV (4.3.1), “special case”; SGA 4 I (1.2), “special case”.

## Tag 006F, a definition

[Tag 006F](https://stacks.math.columbia.edu/tag/006F) in the Stacks Project.

**`constantPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/Constant.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/Constant.lean#L57). References: EGA 0 (3.6.1); SGA 4 IV (2.7.5), “special case”; SGA 4 IV (4.3.4), “special case”; SGA 4 IX (2.0), “partial”.

> The constant presheaf on a topological space `X` with value the set `A`: the constant
> functor `(Opens X)ᵒᵖ ⥤ Type` at `A`.

```lean
def constantPresheaf (X : TopCat) (A : Type) : TopCat.Presheaf Type X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.3, Tag 006D](https://stacks.math.columbia.edu/tag/006D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
