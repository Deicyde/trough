---
declaration: section
origin: cited
lean: AlgebraicGeometry.locallyOfFinitePresentation_isLocalAtSource, AlgebraicGeometry.locallyOfFiniteType_isLocalAtSource, AlgebraicGeometry.isLocalAtSource_fppf_isOpenMap, AlgebraicGeometry.universallyOpen_isLocalAtSource
statement: formalized
proof: formalized
---

# 35.28 Properties of morphisms local in the fppf topology on the source

Section 35.28 of the Stacks Project, [Tag 036M](https://stacks.math.columbia.edu/tag/036M). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 036N, a lemma

[Tag 036N](https://stacks.math.columbia.edu/tag/036N) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFinitePresentation_isLocalAtSource`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Fppf.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Fppf.lean#L57).

> Being locally of finite presentation is local on the source for the fppf topology.

```lean
instance locallyOfFinitePresentation_isLocalAtSource :
    MorphismProperty.IsLocalAtSource (@LocallyOfFinitePresentation.{u})
      Scheme.fppfPrecoverage
```

## Tag 036O, a lemma

[Tag 036O](https://stacks.math.columbia.edu/tag/036O) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFiniteType_isLocalAtSource`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Fppf.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Fppf.lean#L83).

> Being locally of finite type is local on the source for the fppf topology.

```lean
instance locallyOfFiniteType_isLocalAtSource :
    MorphismProperty.IsLocalAtSource (@LocallyOfFiniteType.{u}) Scheme.fppfPrecoverage
```

## Tag 036P, a lemma

[Tag 036P](https://stacks.math.columbia.edu/tag/036P) in the Stacks Project.

**`AlgebraicGeometry.isLocalAtSource_fppf_isOpenMap`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Fppf.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Fppf.lean#L110).

> Being an open morphism is local on the source for the fppf topology.

```lean
instance isLocalAtSource_fppf_isOpenMap :
    (topologically IsOpenMap : MorphismProperty Scheme.{u}).IsLocalAtSource
      Scheme.fppfPrecoverage
```

## Tag 036Q, a lemma

[Tag 036Q](https://stacks.math.columbia.edu/tag/036Q) in the Stacks Project.

**`AlgebraicGeometry.universallyOpen_isLocalAtSource`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Fppf.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/Fppf.lean#L125).

> Being universally open is local on the source for the fppf topology.

```lean
instance universallyOpen_isLocalAtSource :
    MorphismProperty.IsLocalAtSource (@UniversallyOpen.{u}) Scheme.fppfPrecoverage
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.28, Tag 036M](https://stacks.math.columbia.edu/tag/036M)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
