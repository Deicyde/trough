---
declaration: section
origin: cited
lean: Stacks.Sheaf.canonicalComplementSequence_shortExact
statement: formalized
proof: formalized
---

# 17.7 A canonical exact sequence

Section 17.7 of the Stacks Project, [Tag 02US](https://stacks.math.columbia.edu/tag/02US). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 02UT, a lemma

[Tag 02UT](https://stacks.math.columbia.edu/tag/02UT) in the Stacks Project.

**`Stacks.Sheaf.canonicalComplementSequence_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Generators/ComplementExactSequence.lean, line 238](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/Topology/Sheaves/Modules/Generators/ComplementExactSequence.lean#L238). References: SGA 4 IV (14.6), “(14.6.1)”.

> **Stacks Project, Tag 02UT.** The canonical sequence associated to an open subset and its
> closed complement is short exact for every sheaf of abelian groups.

```lean
theorem canonicalComplementSequence_shortExact
    (F : TopCat.Sheaf AddCommGrpCat.{u} X) :
    ((canonicalComplementSequence U).obj F).ShortExact
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.7, Tag 02US](https://stacks.math.columbia.edu/tag/02US)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
