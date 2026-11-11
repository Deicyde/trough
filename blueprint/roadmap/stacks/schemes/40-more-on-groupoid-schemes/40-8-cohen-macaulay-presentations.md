---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_open_source_cohenMacaulay_locus, AlgebraicGeometry.target_cohenMacaulay_locus, AlgebraicGeometry.target_from_source_surjective, AlgebraicGeometry.source_from_target_surjective, AlgebraicGeometry.restricted_source_cohenMacaulay, AlgebraicGeometry.restricted_target_cohenMacaulay, AlgebraicGeometry.restricted_source_locallyOfFinitePresentation, AlgebraicGeometry.restricted_target_locallyOfFinitePresentation
statement: formalized
proof: formalized
---

# 40.8 Cohen-Macaulay presentations

Section 40.8 of the Stacks Project, [Tag 04LK](https://stacks.math.columbia.edu/tag/04LK). 1 tag here is carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0460, a lemma

[Tag 0460](https://stacks.math.columbia.edu/tag/0460) in the Stacks Project.

**`AlgebraicGeometry.exists_open_source_cohenMacaulay_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean#L324). The attribute's comment: “part (1)”.

> There is an open of objects whose inverse image under the target is the
> greatest open on which the source map is Cohen–Macaulay.

```lean
public theorem exists_open_source_cohenMacaulay_locus {S : Scheme.{u}}
    (G : GroupoidScheme S)
    [Flat G.source.left] [Flat G.target.left]
    [LocallyOfFinitePresentation G.source.left]
    [LocallyOfFinitePresentation G.target.left] :
    ∃ W : G.objects.left.Opens,
      IsGreatest
        {V : G.arrows.left.Opens |
          ∃ hf : ∀ y : G.objects.left,
            IsLocallyNoetherian ((V.ι ≫ G.source.left).fiber y),
            Scheme.Hom.IsCohenMacaulay (V.ι ≫ G.source.left) hf}
        (G.target.left ⁻¹ᵁ W)
```

**`AlgebraicGeometry.target_cohenMacaulay_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean#L382). The attribute's comment: “part (2)”.

> The inverse image of the object open under the source is the greatest
> open on which the target map is Cohen–Macaulay.

```lean
public theorem target_cohenMacaulay_locus {S : Scheme.{u}} (G : GroupoidScheme S)
    [Flat G.source.left] [Flat G.target.left]
    [LocallyOfFinitePresentation G.source.left]
    [LocallyOfFinitePresentation G.target.left] :
    IsGreatest
      {V : G.arrows.left.Opens |
        ∃ hf : ∀ y : G.objects.left,
          IsLocallyNoetherian ((V.ι ≫ G.target.left).fiber y),
          Scheme.Hom.IsCohenMacaulay (V.ι ≫ G.target.left) hf}
      (G.source.left ⁻¹ᵁ cohenMacaulayOpen G)
```

**`AlgebraicGeometry.target_from_source_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean, line 477](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean#L477). The attribute's comment: “part (3)”.

> The target remains surjective on the inverse image of the open under the source.

```lean
public theorem target_from_source_surjective {S : Scheme.{u}} (G : GroupoidScheme S)
    [Flat G.source.left] [Flat G.target.left]
    [LocallyOfFinitePresentation G.source.left]
    [LocallyOfFinitePresentation G.target.left] :
    Surjective ((G.source.left ⁻¹ᵁ cohenMacaulayOpen G).ι ≫ G.target.left)
```

**`AlgebraicGeometry.source_from_target_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean, line 487](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean#L487). The attribute's comment: “part (4)”.

> The source remains surjective on the inverse image of the open under the target.

```lean
public theorem source_from_target_surjective {S : Scheme.{u}} (G : GroupoidScheme S)
    [Flat G.source.left] [Flat G.target.left]
    [LocallyOfFinitePresentation G.source.left]
    [LocallyOfFinitePresentation G.target.left] :
    Surjective ((G.target.left ⁻¹ᵁ cohenMacaulayOpen G).ι ≫ G.source.left)
```

**`AlgebraicGeometry.restricted_source_cohenMacaulay`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean, line 588](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean#L588). The attribute's comment: “part (5): source Cohen–Macaulay”.

> The source map of the restricted groupoid is Cohen–Macaulay.

```lean
public theorem restricted_source_cohenMacaulay {S : Scheme.{u}} (G : GroupoidScheme S)
    [Flat G.source.left] [Flat G.target.left]
    [LocallyOfFinitePresentation G.source.left]
    [LocallyOfFinitePresentation G.target.left] :
    let U' := cohenMacaulayOpen G
    let g : Over.mk (U'.ι ≫ G.objects.hom) ⟶ G.objects := Over.homMk U'.ι
    let f := (GroupoidScheme.restrict G g).groupoid.source.left
    ∃ hf : ∀ y, IsLocallyNoetherian (f.fiber y),
      Scheme.Hom.IsCohenMacaulay f hf
```

**`AlgebraicGeometry.restricted_target_cohenMacaulay`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean, line 631](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean#L631). The attribute's comment: “part (5): target Cohen–Macaulay”.

> The target map of the restricted groupoid is Cohen–Macaulay.

```lean
public theorem restricted_target_cohenMacaulay {S : Scheme.{u}} (G : GroupoidScheme S)
    [Flat G.source.left] [Flat G.target.left]
    [LocallyOfFinitePresentation G.source.left]
    [LocallyOfFinitePresentation G.target.left] :
    let U' := cohenMacaulayOpen G
    let g : Over.mk (U'.ι ≫ G.objects.hom) ⟶ G.objects := Over.homMk U'.ι
    let f := (GroupoidScheme.restrict G g).groupoid.target.left
    ∃ hf : ∀ y, IsLocallyNoetherian (f.fiber y),
      Scheme.Hom.IsCohenMacaulay f hf
```

**`AlgebraicGeometry.restricted_source_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean, line 655](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean#L655). The attribute's comment: “part (5): source locally of finite presentation”.

> The source map of the restricted groupoid is locally of finite presentation.

```lean
public theorem restricted_source_locallyOfFinitePresentation {S : Scheme.{u}}
    (G : GroupoidScheme S) [Flat G.source.left] [Flat G.target.left]
    [LocallyOfFinitePresentation G.source.left]
    [LocallyOfFinitePresentation G.target.left] :
    let U' := cohenMacaulayOpen G
    let g : Over.mk (U'.ι ≫ G.objects.hom) ⟶ G.objects := Over.homMk U'.ι
    LocallyOfFinitePresentation (GroupoidScheme.restrict G g).groupoid.source.left
```

**`AlgebraicGeometry.restricted_target_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean, line 666](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayRestriction.lean#L666). The attribute's comment: “part (5): target locally of finite presentation”.

> The target map of the restricted groupoid is locally of finite presentation.

```lean
public theorem restricted_target_locallyOfFinitePresentation {S : Scheme.{u}}
    (G : GroupoidScheme S) [Flat G.source.left] [Flat G.target.left]
    [LocallyOfFinitePresentation G.source.left]
    [LocallyOfFinitePresentation G.target.left] :
    let U' := cohenMacaulayOpen G
    let g : Over.mk (U'.ι ≫ G.objects.hom) ⟶ G.objects := Over.homMk U'.ι
    LocallyOfFinitePresentation (GroupoidScheme.restrict G g).groupoid.target.left
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 40.8, Tag 04LK](https://stacks.math.columbia.edu/tag/04LK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
