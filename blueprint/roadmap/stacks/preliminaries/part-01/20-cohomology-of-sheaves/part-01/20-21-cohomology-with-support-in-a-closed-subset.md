---
declaration: section
origin: cited
lean: ClosedImmersionSheaves.supportedSectionsOnClosed_injective
statement: formalized
proof: formalized
---

# 20.21 Cohomology with support in a closed subset

Section 20.21 of the Stacks Project, [Tag 0A39](https://stacks.math.columbia.edu/tag/0A39). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 0A3A, a lemma

[Tag 0A3A](https://stacks.math.columbia.edu/tag/0A3A) in the Stacks Project.

**`ClosedImmersionSheaves.supportedSectionsOnClosed_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/InjectiveSupportedSections.lean, line 56](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/Topology/Sheaves/Cohomology/Vanishing/InjectiveSupportedSections.lean#L56).

> **Stacks Project, Tag 0A3A.** Sections of an injective abelian sheaf supported on a closed
> subset form an injective abelian sheaf on that subset.

```lean
theorem supportedSectionsOnClosed_injective {X : TopCat.{u}}
    (Z : Set X) (hZ : IsClosed Z) (I : X.Sheaf AddCommGrpCat.{u})
    [Injective I] :
    Injective ((supportedSectionsOnClosedFunctor Z hZ).obj I)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.21, Tag 0A39](https://stacks.math.columbia.edu/tag/0A39)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
