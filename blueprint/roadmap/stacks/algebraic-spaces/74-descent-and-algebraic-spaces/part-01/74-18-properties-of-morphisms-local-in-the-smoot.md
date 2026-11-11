---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isSmooth_isLocalAtSource_smooth
statement: formalized
proof: formalized
---

# 74.18 Properties of morphisms local in the smooth topology on the source

Section 74.18 of the Stacks Project, [Tag 06F1](https://stacks.math.columbia.edu/tag/06F1). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06F2, a lemma

[Tag 06F2](https://stacks.math.columbia.edu/tag/06F2) in the Stacks Project.

**`AlgebraicGeometry.Space.isSmooth_isLocalAtSource_smooth`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothSourceLocalityTransfer.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothSourceLocalityTransfer.lean#L432).

> **Stacks 06F2.** Smoothness of morphisms of algebraic spaces over `S` is local on the source
> for the smooth topology.
>
> One application of the smooth case of Stacks 06ER to smoothness of morphisms of schemes, which
> is étale local on the source and target (Stacks 04R3, smooth case) and smooth local on the
> source (Stacks 036U). Registered as an instance, which is the form the criterion of Stacks 06FB
> takes it in.

```lean
instance isSmooth_isLocalAtSource_smooth :
    MorphismProperty.IsLocalAtSource
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) => IsSmooth B S hS f.hom)
      (Topology.precoverage.{u, v} .smooth B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.18, Tag 06F1](https://stacks.math.columbia.edu/tag/06F1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
