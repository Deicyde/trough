---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidInAlgebraicSpaces.stabilizerGroupStructure, AlgebraicGeometry.GroupoidInAlgebraicSpaces.stabilizerGroup, AlgebraicGeometry.GroupoidInAlgebraicSpaces.stabilizerAction
statement: formalized
proof: formalized
---

# 78.16 The stabilizer group algebraic space

Section 78.16 of the Stacks Project, [Tag 0446](https://stacks.math.columbia.edu/tag/0446). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0447, a lemma

[Tag 0447](https://stacks.math.columbia.edu/tag/0447) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.stabilizerGroupStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/GroupStructure.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/GroupStructure.lean#L224).

> **Stacks 0447.** The stabilizer of a groupoid in algebraic spaces is a group object in the
> slice over the object space, with groupoid composition as multiplication.

```lean
noncomputable def stabilizerGroupStructure (G : GroupoidInAlgebraicSpaces C S hS B) :
    { h : GrpObj (stabilizer G) // IsStabilizerGroupStructure G h }
```

## Tag 0448, a definition

[Tag 0448](https://stacks.math.columbia.edu/tag/0448) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.stabilizerGroup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/GroupStructure.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/GroupStructure.lean#L367). The attribute's comment: “the stabilizer as a group algebraic space over the object space”.

> The stabilizer group algebraic space over the object space of a groupoid in algebraic
> spaces.

```lean
noncomputable def stabilizerGroup (G : GroupoidInAlgebraicSpaces C S hS B) :
    Space.GroupAlgebraicSpace C S hS G.objects.obj G.objects.property
```

## Tag 0449, a lemma

[Tag 0449](https://stacks.math.columbia.edu/tag/0449) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.stabilizerAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/Action.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/Action.lean#L172).

> The stabilizer of a groupoid in algebraic spaces acts on its arrow space over the object space,
> and the action is groupoid composition on generalized points.

```lean
noncomputable def stabilizerAction (G : GroupoidInAlgebraicSpaces C S hS B) :
    { h : ModObj (stabilizer G) (arrowsOverTarget G) // IsStabilizerAction G h }
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.16, Tag 0446](https://stacks.math.columbia.edu/tag/0446)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
