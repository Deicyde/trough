---
declaration: section
origin: cited
lean: Stacks.Groupoids.GroupoidScheme.comp_source_isPullback, Stacks.Groupoids.GroupoidScheme.target_comp_isPullback, AlgebraicGeometry.GroupoidScheme.targetPullbackToComposable, AlgebraicGeometry.GroupoidScheme.fst_source_isPullback, AlgebraicGeometry.GroupoidScheme.id_target_comm, AlgebraicGeometry.GroupoidScheme.targetPullbackToComposable_fst, AlgebraicGeometry.GroupoidScheme.targetPullbackToComposable_comp, AlgebraicGeometry.GroupoidScheme.targetPullbackToComposable_isIso
statement: formalized
proof: formalized
---

# 40.3 Useful diagrams

Section 40.3 of the Stacks Project, [Tag 04LE](https://stacks.math.columbia.edu/tag/04LE). 2 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04LF, an equation

[Tag 04LF](https://stacks.math.columbia.edu/tag/04LF) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.comp_source_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FieldExtensionEvaluation.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FieldExtensionEvaluation.lean#L148). The attribute's comment: “diagram (04LF): the lower-right square is cartesian”.

> The square formed by composition, the second projection, and two copies of the source map
> is a pullback square: a composable pair of arrows is determined by its first member together
> with its composite.

```lean
theorem comp_source_isPullback {S : Scheme.{u}} (G : GroupoidScheme S) :
    IsPullback G.comp (pullback.snd G.source G.target) G.source G.source
```

**`Stacks.Groupoids.GroupoidScheme.target_comp_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FieldExtensionEvaluation.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FieldExtensionEvaluation.lean#L197). The attribute's comment: “diagram (04LF): the lower-right square is cartesian”.

> The upper triangle in the composition diagram, viewed as a square with two copies of its
> apex, is a pullback square: a pair of arrows with the same target is the same thing as a
> composable pair together with its composite.

```lean
theorem target_comp_isPullback {S : Scheme.{u}} (G : GroupoidScheme S) :
    IsPullback (pullback.fst G.source G.target) G.comp G.target G.target
```

## Tag 04LG, an equation

[Tag 04LG](https://stacks.math.columbia.edu/tag/04LG) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.targetPullbackToComposable`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean#L81). The attribute's comment: “the vertical map `(pr₀, c ∘ (i, 1))` of the displayed diagram”.

> The vertical map in the top left of the diagram: it sends a pair `(α, β)` with equal
> targets to the composable pair `(α, α⁻¹ ∘ β)`.

```lean
noncomputable def targetPullbackToComposable {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S) :
    pullback G.target G.target ⟶ pullback G.source G.target
```

**`AlgebraicGeometry.GroupoidScheme.fst_source_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean#L103). The attribute's comment: “cartesianness: the lower of the two lower left squares, the one taken with the first projection on top and the target along the bottom”.

> The square formed by the two projections of the scheme of composable pairs together with
> the source and the target maps is a pullback square.  This is the lower-left square of the
> diagram taken with the lower horizontal maps, and it is cartesian because the scheme of
> composable pairs is by definition the fibre product of the source and the target.

```lean
theorem fst_source_isPullback {S : Scheme.{u}} (G : Stacks.Groupoids.GroupoidScheme S) :
    IsPullback (pullback.fst G.source G.target) (pullback.snd G.source G.target)
      G.source G.target
```

**`AlgebraicGeometry.GroupoidScheme.id_target_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean#L114). The attribute's comment: “commutativity: the right-hand square between the two top rows, whose vertical maps are the identities”.

> The upper-right square of the diagram commutes.  Both of its vertical maps are
> identities, of the arrow scheme and of the object scheme respectively, and both of its
> horizontal maps are the target map.

```lean
theorem id_target_comm {S : Scheme.{u}} (G : Stacks.Groupoids.GroupoidScheme S) :
    𝟙 G.arrows ≫ G.target = G.target ≫ 𝟙 G.objects
```

**`AlgebraicGeometry.GroupoidScheme.targetPullbackToComposable_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean#L123). The attribute's comment: “commutativity: the left square between the two top rows taken with the first projections”.

> The comparison map preserves the first projection.  This is the lower of the two
> commutative triangles in the top left of the diagram.

```lean
theorem targetPullbackToComposable_fst {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S) :
    targetPullbackToComposable G ≫ pullback.fst G.source G.target =
      pullback.fst G.target G.target
```

**`AlgebraicGeometry.GroupoidScheme.targetPullbackToComposable_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean#L142). The attribute's comment: “commutativity: the left square between the two top rows taken with the second projection on top and the composition along the bottom”.

> Composing a pair after the change of coordinates recovers its second member.  This is
> the upper of the two commutative triangles in the top left of the diagram.

```lean
theorem targetPullbackToComposable_comp {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S) :
    targetPullbackToComposable G ≫ G.comp = pullback.snd G.target G.target
```

**`AlgebraicGeometry.GroupoidScheme.targetPullbackToComposable_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean#L213). The attribute's comment: “the two top rows are isomorphic via the vertical maps given”.

> The vertical comparison between pairs with the same target and composable pairs is an
> isomorphism.

```lean
theorem targetPullbackToComposable_isIso {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S) :
    IsIso (targetPullbackToComposable G)
```

**`AlgebraicGeometry.GroupoidScheme.diagram_pull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean#L250). The attribute's comment: “the whole diagram: it is commutative, its two top rows are isomorphic via the vertical maps given, and its two lower left squares are cartesian”.

> Every assertion made about the displayed diagram, in one statement.
>
> Each square is written as `left ≫ bottom = top ≫ right`, so that the vertical maps which are
> identities are displayed rather than suppressed.  The first three conjuncts are the
> commutativity of the three squares between the two top rows: the two on the left, one for each
> of the two parallel arrows, and the right-hand one whose vertical maps are the identity of the
> arrow scheme and the identity of the object scheme.  Together with the fourth conjunct, which
> says that the remaining vertical map is an isomorphism, they say that the two top rows are
> isomorphic through the vertical maps given.  The last two conjuncts say that the two lower left
> squares, again one for each of the two parallel arrows, are cartesian; the commutativity of
> those two squares is part of the same assertions.

```lean
theorem diagram_pull {S : Scheme.{u}} (G : Stacks.Groupoids.GroupoidScheme S) :
    targetPullbackToComposable G ≫ G.comp =
          pullback.snd G.target G.target ≫ 𝟙 G.arrows ∧
      targetPullbackToComposable G ≫ pullback.fst G.source G.target =
          pullback.fst G.target G.target ≫ 𝟙 G.arrows ∧
      𝟙 G.arrows ≫ G.target = G.target ≫ 𝟙 G.objects ∧
      IsIso (targetPullbackToComposable G) ∧
      IsPullback G.comp (pullback.snd G.source G.target) G.source G.source ∧
      IsPullback (pullback.fst G.source G.target) (pullback.snd G.source G.target)
        G.source G.target
```

Declarations registered for the tag:

- [`Stacks.Groupoids.GroupoidScheme.comp_source_isPullback`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FieldExtensionEvaluation.lean#L148), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean#L92) (StacksFrontier): “cartesianness: the upper of the two lower left squares, the one taken with the composition on top and the source along the bottom”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 40.3, Tag 04LE](https://stacks.math.columbia.edu/tag/04LE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
