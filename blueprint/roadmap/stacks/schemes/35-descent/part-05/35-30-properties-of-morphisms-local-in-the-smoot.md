---
declaration: section
origin: cited
lean: AlgebraicGeometry.smooth_isLocalAtSource, AlgebraicGeometry.Smooth.isLocalAtSource_smoothPrecoverage
statement: formalized
proof: formalized
---

# 35.30 Properties of morphisms local in the smooth topology on the source

Section 35.30 of the Stacks Project, [Tag 036T](https://stacks.math.columbia.edu/tag/036T). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 036U, a lemma

[Tag 036U](https://stacks.math.columbia.edu/tag/036U) in the Stacks Project.

**`AlgebraicGeometry.smooth_isLocalAtSource`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Smooth.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Smooth.lean#L52).

> **Stacks Project, Tag 036U.** Being a smooth morphism of schemes is local on the source for
> the smooth topology.

```lean
instance smooth_isLocalAtSource :
    MorphismProperty.IsLocalAtSource (@Smooth.{u}) (Scheme.precoverage (@Smooth.{u}))
```

**`AlgebraicGeometry.Smooth.isLocalAtSource_smoothPrecoverage`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/SmoothSourceLocality.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/SmoothSourceLocality.lean#L108). References: SGA 4 IV (8.5.5), “special case”.

> **Stacks 036U.** Smoothness of morphisms of schemes is local on the source for the smooth
> topology: a morphism is smooth exactly when its composites with the members of a smooth covering
> of its source are smooth.
>
> The affine descent hypothesis of the smooth case of Stacks 036H is the smooth case of
> Stacks 02KM, which holds without any affineness assumption.

```lean
instance Smooth.isLocalAtSource_smoothPrecoverage :
    MorphismProperty.IsLocalAtSource (@Smooth : MorphismProperty Scheme.{u})
      (Scheme.precoverage (@Smooth : MorphismProperty Scheme.{u}))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.30, Tag 036T](https://stacks.math.columbia.edu/tag/036T)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
