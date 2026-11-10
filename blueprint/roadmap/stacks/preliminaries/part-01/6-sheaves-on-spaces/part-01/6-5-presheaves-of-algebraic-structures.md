---
declaration: section
origin: cited
lean: TopCat.Presheaf, TopCat.instCategoryPresheaf, underlyingPresheafSets
statement: formalized
proof: formalized
---

# 6.5 Presheaves of algebraic structures

Section 6.5 of the Stacks Project, [Tag 006M](https://stacks.math.columbia.edu/tag/006M). 2 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 006N, a definition

[Tag 006N](https://stacks.math.columbia.edu/tag/006N) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.Presheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/ValuedInCategory.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/ValuedInCategory.lean#L33) (StacksFrontier): “(1), presheaves valued in a category”. References: SGA 3 IV (4.3.1), “special case”; SGA 3 IV (4.3.17), “special case”; SGA 4 I (1.2), “special case”; SGA 4 II (6.0), “special case”; SGA 4½ Arcata (1.6.3), “special case”.
- [`TopCat.instCategoryPresheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.instCategoryPresheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/ValuedInCategory.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/ValuedInCategory.lean#L34) (StacksFrontier): “(2), their morphisms”. References: SGA 3 IV (4.3.1), “special case”; SGA 4 I (1.2), “special case”.

## Tag 006O, a definition

[Tag 006O](https://stacks.math.columbia.edu/tag/006O) in the Stacks Project.

**`underlyingPresheafSets`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/Forget.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/Forget.lean#L58). References: SGA 4 II (6.3.0), “object assignment of ε^”.

> The underlying presheaf of sets of a presheaf `𝓕` with values in a category `C`,
> obtained by post-composing with a faithful functor `F : C ⥤ Type`. Its value on an
> open `U` is `F (𝓕 U)`.

```lean
def underlyingPresheafSets
    {X : TopCat.{u}} {C : Type u} [Category.{v} C]
    (F : C ⥤ Type u) [F.Faithful] (𝓕 : TopCat.Presheaf C X) :
    TopCat.Presheaf (Type u) X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.5, Tag 006M](https://stacks.math.columbia.edu/tag/006M)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
