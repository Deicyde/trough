---
declaration: section
origin: cited
lean: AlgebraicGeometry.Syntomic.isLocalAtSource_syntomicPrecoverage
statement: formalized
proof: formalized
---

# 35.29 Properties of morphisms local in the syntomic topology on the source

Section 35.29 of the Stacks Project, [Tag 036R](https://stacks.math.columbia.edu/tag/036R). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 036S, a lemma

[Tag 036S](https://stacks.math.columbia.edu/tag/036S) in the Stacks Project.

**`AlgebraicGeometry.Syntomic.isLocalAtSource_syntomicPrecoverage`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Syntomic.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Syntomic.lean#L42).

> Being syntomic is local on the source for the syntomic topology: a morphism of schemes is
> syntomic exactly when its composites with the members of a syntomic covering of its source are.

```lean
instance Syntomic.isLocalAtSource_syntomicPrecoverage :
    MorphismProperty.IsLocalAtSource (@Syntomic.{u} : MorphismProperty Scheme.{u})
      (Scheme.precoverage (@Syntomic.{u}))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.29, Tag 036R](https://stacks.math.columbia.edu/tag/036R)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
