---
declaration: section
origin: cited
lean: AlgebraicGeometry.ModuliEllipticCurves.PointedFamily, AlgebraicGeometry.ModuliEllipticCurves.PointedFamily.IsElliptic
statement: formalized
proof: formalized
---

# 105.2 Preliminary

Section 105.2 of the Stacks Project, [Tag 072J](https://stacks.math.columbia.edu/tag/072J). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 072J, the section

[Tag 072J](https://stacks.math.columbia.edu/tag/072J) in the Stacks Project.

**`AlgebraicGeometry.ModuliEllipticCurves.PointedFamily`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ModuliEllipticCurves.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ModuliEllipticCurves.lean#L74). The attribute's comment: “the triple (E, f, 0)”.

> A family of schemes over `S` together with a section of its structure morphism, that is, a
> triple `(E, f, 0)`.

```lean
structure PointedFamily (S : Scheme.{u})
```

**`AlgebraicGeometry.ModuliEllipticCurves.PointedFamily.IsElliptic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ModuliEllipticCurves.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ModuliEllipticCurves.lean#L90). The attribute's comment: “an elliptic curve over S”.

> A pointed family is an elliptic curve when its structure morphism is proper and smooth of
> relative dimension one and each of its fibres is a connected curve of genus one, that is, has
> one-dimensional `H⁰` and `H¹`.

```lean
def IsElliptic {S : Scheme.{u}} (E : PointedFamily S) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 105.2, Tag 072J](https://stacks.math.columbia.edu/tag/072J)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
