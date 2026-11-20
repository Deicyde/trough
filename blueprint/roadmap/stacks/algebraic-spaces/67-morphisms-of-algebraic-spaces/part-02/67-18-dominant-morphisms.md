---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsDominant
statement: formalized
proof: formalized
---

# 67.18 Dominant morphisms

Section 67.18 of the Stacks Project, [Tag 0ABK](https://stacks.math.columbia.edu/tag/0ABK). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 0ABL, a definition

[Tag 0ABL](https://stacks.math.columbia.edu/tag/0ABL) in the Stacks Project.

**`AlgebraicGeometry.Space.IsDominant`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RationalMaps.lean, line 85](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RationalMaps.lean#L85). References: EGA I (2.2.6), “dominant”.

> A morphism of algebraic spaces over `S` is *dominant* when the image of its map on points is
> dense in the point space of the target.

```lean
abbrev IsDominant (f : F ⟶ G) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.18, Tag 0ABK](https://stacks.math.columbia.edu/tag/0ABK)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
