---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidInAlgebraicSpaces.isPullback_fst_snd_source_target, AlgebraicGeometry.AlgebraicSpaces.isPullback_fiberProduct, AlgebraicGeometry.Space.isPullback_comp_source, AlgebraicGeometry.Space.isPullback_fst_comp, AlgebraicGeometry.GroupoidInAlgebraicSpaces.commonTargetPairsIso, AlgebraicGeometry.GroupoidInAlgebraicSpaces.comp_source_eq_snd_source, AlgebraicGeometry.GroupoidInAlgebraicSpaces.fst_source_eq_snd_target, AlgebraicGeometry.GroupoidInAlgebraicSpaces.commonTargetPairsComparison
statement: formalized
proof: formalized
---

# 79.3 Useful diagrams

Section 79.3 of the Stacks Project, [Tag 04P8](https://stacks.math.columbia.edu/tag/04P8). 2 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04P9, an equation

[Tag 04P9](https://stacks.math.columbia.edu/tag/04P9) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isPullback_fst_snd_source_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L190). The attribute's comment: “the lower-left square”.

> **Stacks 0450**, the lower-left square for the projections. The two projections out of the
> space of composable pairs of arrows of a groupoid in algebraic spaces form a cartesian square
> with the source and the target morphisms: a composable pair is exactly a pair of arrows whose
> first arrow has as its source the target of the second.

```lean
theorem isPullback_fst_snd_source_target (G : GroupoidInAlgebraicSpaces C S hS B) :
    IsPullback
      (ObjectProperty.homMk (pullback.fst G.source.hom G.target.hom) :
        AlgebraicSpaces.fiberProduct C S hS G.source G.target ⟶ G.arrows)
      (ObjectProperty.homMk (pullback.snd G.source.hom G.target.hom) :
        AlgebraicSpaces.fiberProduct C S hS G.source G.target ⟶ G.arrows)
      G.source G.target
```

Declarations registered for the tag:

- [`AlgebraicGeometry.AlgebraicSpaces.isPullback_fiberProduct`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Category.lean#L403), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Diagrams.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Diagrams.lean#L53) (StacksFrontier): “the lower-left square”.
- [`AlgebraicGeometry.Space.isPullback_comp_source`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpacesOfComposable.lean#L476), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Diagrams.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Diagrams.lean#L56) (StacksFrontier): “the lower-right square”.
- [`AlgebraicGeometry.Space.isPullback_fst_comp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpacesOfComposable.lean#L503), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Diagrams.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Diagrams.lean#L59) (StacksFrontier): “the upper square”.

## Tag 0451, an equation

[Tag 0451](https://stacks.math.columbia.edu/tag/0451) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.commonTargetPairsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L108). The attribute's comment: “the displayed diagram, through its vertical comparison pr_0 × c ∘ (i,1)”.

> **Stacks 0450.** The canonical comparison `(α, β) ↦ (α, α⁻¹ ∘ β)` of the space of pairs of
> arrows of a groupoid in algebraic spaces with a common target with the space of composable pairs
> of arrows.

```lean
noncomputable def commonTargetPairsIso (G : GroupoidInAlgebraicSpaces C S hS B) :
    AlgebraicSpaces.fiberProduct C S hS G.target G.target ≅
      AlgebraicSpaces.fiberProduct C S hS G.source G.target
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.comp_source_eq_snd_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L165). The attribute's comment: “commutativity of the upper of the two lower left squares”.

> **Stacks 0450**, the commutativity of the lower square for composition: `c ≫ s = pr₁ ≫ s`.
> The composite of a composable pair of arrows of a groupoid in algebraic spaces has the same
> source as the second arrow of the pair.

```lean
theorem comp_source_eq_snd_source (G : GroupoidInAlgebraicSpaces C S hS B) :
    G.comp ≫ G.source =
      (ObjectProperty.homMk (pullback.snd G.source.hom G.target.hom) :
        AlgebraicSpaces.fiberProduct C S hS G.source G.target ⟶ G.arrows) ≫ G.source
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.fst_source_eq_snd_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L176). The attribute's comment: “commutativity of the lower of the two lower left squares”.

> **Stacks 0450**, the commutativity of the lower square for the projections:
> `pr₀ ≫ s = pr₁ ≫ t`. The first arrow of a composable pair of arrows of a groupoid in algebraic
> spaces has as its source the target of the second arrow of the pair.

```lean
theorem fst_source_eq_snd_target (G : GroupoidInAlgebraicSpaces C S hS B) :
    (ObjectProperty.homMk (pullback.fst G.source.hom G.target.hom) :
        AlgebraicSpaces.fiberProduct C S hS G.source G.target ⟶ G.arrows) ≫ G.source =
      (ObjectProperty.homMk (pullback.snd G.source.hom G.target.hom) :
        AlgebraicSpaces.fiberProduct C S hS G.source G.target ⟶ G.arrows) ≫ G.target
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isPullback_fst_snd_source_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L190). The attribute's comment: “the lower of the two lower left squares is cartesian”.

> **Stacks 0450**, the lower-left square for the projections. The two projections out of the
> space of composable pairs of arrows of a groupoid in algebraic spaces form a cartesian square
> with the source and the target morphisms: a composable pair is exactly a pair of arrows whose
> first arrow has as its source the target of the second.

```lean
theorem isPullback_fst_snd_source_target (G : GroupoidInAlgebraicSpaces C S hS B) :
    IsPullback
      (ObjectProperty.homMk (pullback.fst G.source.hom G.target.hom) :
        AlgebraicSpaces.fiberProduct C S hS G.source G.target ⟶ G.arrows)
      (ObjectProperty.homMk (pullback.snd G.source.hom G.target.hom) :
        AlgebraicSpaces.fiberProduct C S hS G.source G.target ⟶ G.arrows)
      G.source G.target
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.commonTargetPairsComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L243). The attribute's comment: “the vertical comparison pr_0 × c ∘ (i, 1)”.

> **Stacks 0451.** The vertical comparison `pr_0 × c ∘ (i, 1)` of the diagram: it sends a pair
> `(α, β)` of arrows with a common target to the composable pair `(α, α⁻¹ ∘ β)`.

```lean
noncomputable def commonTargetPairsComparison (G : GroupoidInAlgebraicSpaces C S hS B) :
    AlgebraicSpaces.fiberProduct C S hS G.target G.target ⟶
      AlgebraicSpaces.fiberProduct C S hS G.source G.target
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.commonTargetPairsComparison_comp_firstArrow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L259). The attribute's comment: “the lower square on the left of the top two rows”.

> **Stacks 0451**, the lower of the two squares on the left of the top two rows: the vertical
> comparison preserves the first arrow.

```lean
theorem commonTargetPairsComparison_comp_firstArrow
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    commonTargetPairsComparison G ≫ firstArrow G = commonTargetFirstArrow G
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.commonTargetPairsComparison_comp_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L314). The attribute's comment: “the upper square on the left of the top two rows”.

> **Stacks 0451**, the upper of the two squares on the left of the top two rows: composing the
> vertical comparison with the composition of the groupoid recovers the second arrow, because
> `α ∘ (α⁻¹ ∘ β) = β`.

```lean
theorem commonTargetPairsComparison_comp_comp (G : GroupoidInAlgebraicSpaces C S hS B) :
    commonTargetPairsComparison G ≫ G.comp = commonTargetSecondArrow G
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.commonTargetPairsIso_hom_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L347). The attribute's comment: “the two top rows are isomorphic via the vertical maps given”.

> **Stacks 0451.** The vertical comparison drawn in the diagram, `pr_0 × c ∘ (i, 1)`, is the
> canonical comparison of the two fibre products, hence an isomorphism: this is the assertion that
> the two top rows of the diagram are isomorphic via the vertical maps given, the other two
> vertical maps being the identities.

```lean
theorem commonTargetPairsIso_hom_eq (G : GroupoidInAlgebraicSpaces C S hS B) :
    (commonTargetPairsIso G).hom = commonTargetPairsComparison G
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.id_comp_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L365). The attribute's comment: “the square on the right of the top two rows”.

> **Stacks 0451**, the square on the right of the top two rows: both of its vertical maps are
> identities, of the arrow space and of the object space, and its two horizontal maps are the
> target.

```lean
theorem id_comp_target (G : GroupoidInAlgebraicSpaces C S hS B) :
    𝟙 G.arrows ≫ G.target = G.target ≫ 𝟙 G.objects
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isPullback_comp_source`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpacesOfComposable.lean#L476), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L381) (StacksFrontier): “the upper of the two lower left squares is cartesian”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 79.3, Tag 04P8](https://stacks.math.columbia.edu/tag/04P8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
