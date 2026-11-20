---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsGeometricallyIrreducible
statement: formalized
proof: formalized
---

# 72.13 Geometrically irreducible algebraic spaces

Section 72.13 of the Stacks Project, [Tag 0DMT](https://stacks.math.columbia.edu/tag/0DMT). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 0DMU, a definition

[Tag 0DMU](https://stacks.math.columbia.edu/tag/0DMU) in the Stacks Project.

**`AlgebraicGeometry.Space.IsGeometricallyIrreducible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyIntegral.lean, line 94](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/AlgebraicGeometry/Spaces/GeometricallyIntegral.lean#L94).

> **Stacks 0DMU.** An algebraic space over a field `k` is *geometrically irreducible* when
> the space of points of its base change to every field extension of `k` is irreducible — in
> particular nonempty.

```lean
def IsGeometricallyIrreducible (X : (BigFppfOver B (Spec (.of k)) hk)ᵒᵖ ⥤ Type u) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.13, Tag 0DMT](https://stacks.math.columbia.edu/tag/0DMT)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
