---
declaration: section
origin: cited
lean: Stacks.Examples.exists_abelian_not_hasExt
statement: formalized
proof: formalized
---

# 110.63 A big abelian category

Section 110.63 of the Stacks Project, [Tag 07JS](https://stacks.math.columbia.edu/tag/07JS). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 07JT, a lemma

[Tag 07JT](https://stacks.math.columbia.edu/tag/07JT) in the Stacks Project.

**`Stacks.Examples.exists_abelian_not_hasExt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/CategoryTheory/AbelianCategoryWithLargeExt.lean, line 270](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/Examples/CategoryTheory/AbelianCategoryWithLargeExt.lean#L270).

> **Stacks 07JT.** There exists a large abelian category whose `Ext`-groups are not small
> in the next lower universe.

```lean
theorem exists_abelian_not_hasExt :
    ∃ (C : Type (u + 1)) (_ : Category.{u} C) (_ : Abelian C),
      ¬ HasExt.{u} C
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.63, Tag 07JS](https://stacks.math.columbia.edu/tag/07JS)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
