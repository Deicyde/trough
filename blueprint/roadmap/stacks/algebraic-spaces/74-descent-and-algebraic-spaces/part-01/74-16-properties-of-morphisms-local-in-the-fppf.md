---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isLocallyOfFinitePresentation_isLocalAtSource_fppf, AlgebraicGeometry.Space.isLocallyOfFiniteType_isLocalAtSource_fppf, AlgebraicGeometry.Space.isOpenMorphism_isLocalAtSource_fppf, AlgebraicGeometry.Space.universallyOpen_isLocalAtSource_fppf
statement: formalized
proof: formalized
---

# 74.16 Properties of morphisms local in the fppf topology on the source

Section 74.16 of the Stacks Project, [Tag 06EU](https://stacks.math.columbia.edu/tag/06EU). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06EV, a lemma

[Tag 06EV](https://stacks.math.columbia.edu/tag/06EV) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_isLocalAtSource_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Fppf.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSource/Fppf.lean#L63).

> **Stacks 06EV.** Being locally of finite presentation, for a morphism of algebraic spaces
> over `S`, is local on the source for the fppf topology.

```lean
instance isLocallyOfFinitePresentation_isLocalAtSource_fppf :
    MorphismProperty.IsLocalAtSource
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) =>
        IsLocallyOfFinitePresentation B S hS f.hom)
      (Topology.fppf.precoverage.{u, v} B S hS)
```

## Tag 06EW, a lemma

[Tag 06EW](https://stacks.math.columbia.edu/tag/06EW) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_isLocalAtSource_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FppfSourceLocalityFiniteType.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FppfSourceLocalityFiniteType.lean#L58).

> **Stacks 06EW.** Being locally of finite type, as a property of morphisms of algebraic spaces
> over `S`, is local on the source for the fppf topology.

```lean
instance isLocallyOfFiniteType_isLocalAtSource_fppf :
    MorphismProperty.IsLocalAtSource
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) =>
        IsLocallyOfFiniteType B S hS f.hom)
      (Topology.precoverage.{u, v} .fppf B S hS)
```

## Tag 06EX, a lemma

[Tag 06EX](https://stacks.math.columbia.edu/tag/06EX) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpenMorphism_isLocalAtSource_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OpenSourceLocality.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/OpenSourceLocality.lean#L113).

> **Stacks 06EX.** Being open, for a morphism of algebraic spaces over `S`, is local on the
> source for the fppf topology.

```lean
instance isOpenMorphism_isLocalAtSource_fppf :
    MorphismProperty.IsLocalAtSource
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (f : X ⟶ Y) ↦ IsOpenMorphism B S hS f.hom)
      (Topology.fppf.precoverage.{u, v} B S hS)
```

## Tag 06EY, a lemma

[Tag 06EY](https://stacks.math.columbia.edu/tag/06EY) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyOpen_isLocalAtSource_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OpenSourceLocality.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/OpenSourceLocality.lean#L135).

> **Stacks 06EY.** Being universally open, for a morphism of algebraic spaces over `S`, is
> local on the source for the fppf topology.

```lean
instance universallyOpen_isLocalAtSource_fppf :
    MorphismProperty.IsLocalAtSource
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (f : X ⟶ Y) ↦ UniversallyOpen B S hS f.hom)
      (Topology.fppf.precoverage.{u, v} B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.16, Tag 06EU](https://stacks.math.columbia.edu/tag/06EU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
