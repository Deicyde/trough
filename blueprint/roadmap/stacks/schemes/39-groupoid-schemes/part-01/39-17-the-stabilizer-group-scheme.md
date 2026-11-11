---
declaration: section
origin: cited
lean: AlgebraicGeometry.stabilizerGroupStructure, AlgebraicGeometry.stabilizerAction, AlgebraicGeometry.stabilizerActionOverPairs, AlgebraicGeometry.stabilizerActionOverPairs_pseudoTorsor, AlgebraicGeometry.stabilizerActionOnFiber, AlgebraicGeometry.fiber_isFpqcTorsor
statement: formalized
proof: formalized
---

# 39.17 The stabilizer group scheme

Section 39.17 of the Stacks Project, [Tag 03LM](https://stacks.math.columbia.edu/tag/03LM). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0235, a lemma

[Tag 0235](https://stacks.math.columbia.edu/tag/0235) in the Stacks Project.

**`AlgebraicGeometry.stabilizerGroupStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Basic.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Basic.lean#L412). References: SGA 3 V (10.2.1), “X-group scheme”.

> **Stacks Project, Tag 0235.** The stabilizer of a groupoid scheme is canonically a group
> scheme over its object scheme, with multiplication induced by groupoid composition.

```lean
noncomputable def stabilizerGroupStructure {S : Scheme.{u}} (G : GroupoidScheme S) :
    { h : GrpObj (stabilizer G) // IsStabilizerGroupStructure G h }
```

## Tag 0236, a definition

[Tag 0236](https://stacks.math.columbia.edu/tag/0236) in the Stacks Project.

**`AlgebraicGeometry.stabilizerGroupStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Basic.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Basic.lean#L412). The attribute's comment: “the stabilizer group scheme of a groupoid scheme”. References: SGA 3 V (10.2.1), “X-group scheme”.

> **Stacks Project, Tag 0235.** The stabilizer of a groupoid scheme is canonically a group
> scheme over its object scheme, with multiplication induced by groupoid composition.

```lean
noncomputable def stabilizerGroupStructure {S : Scheme.{u}} (G : GroupoidScheme S) :
    { h : GrpObj (stabilizer G) // IsStabilizerGroupStructure G h }
```

## Tag 0237, a lemma

[Tag 0237](https://stacks.math.columbia.edu/tag/0237) in the Stacks Project.

**`AlgebraicGeometry.stabilizerAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Action.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Action.lean#L223).

> The stabilizer group scheme acts canonically on the arrow scheme over the object scheme via
> the target map; the action is induced by composition in the groupoid.

```lean
noncomputable def stabilizerAction {S : Scheme.{u}} (G : GroupoidScheme S) :
    { h : ModObj (stabilizer G) (arrowsOverTarget G) // IsStabilizerAction G h }
```

## Tag 04Q2, a lemma

[Tag 04Q2](https://stacks.math.columbia.edu/tag/04Q2) in the Stacks Project.

**`AlgebraicGeometry.stabilizerActionOverPairs`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/PairPseudotorsor.lean, line 691](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/PairPseudotorsor.lean#L691). The attribute's comment: “induced action”.

> The stabilizer action on arrows induces the canonical action of the base-changed stabilizer
> on arrows over the pair scheme.

```lean
def stabilizerActionOverPairs {S : Scheme.{u}} (G : GroupoidScheme S) :
    { h : ModObj (stabilizerOverPairs G) (arrowsOverPairs G) // IsInducedAction G h }
```

**`AlgebraicGeometry.stabilizerActionOverPairs_pseudoTorsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/PairPseudotorsor.lean, line 718](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/PairPseudotorsor.lean#L718). The attribute's comment: “pseudo-torsor”.

> The arrow scheme is a pseudo-torsor under the stabilizer over the pair scheme.

```lean
theorem stabilizerActionOverPairs_pseudoTorsor {S : Scheme.{u}}
    (G : GroupoidScheme S) :
    IsPseudoTorsor (stabilizerOverPairs G) (arrowsOverPairs G)
```

## Tag 04Q3, a lemma

[Tag 04Q3](https://stacks.math.columbia.edu/tag/04Q3) in the Stacks Project.

**`AlgebraicGeometry.stabilizerActionOnFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Fiber.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Fiber.lean#L78). The attribute's comment: “action on the fibre”.

> The canonical action on the fibre, induced from the action over pairs.

```lean
def stabilizerActionOnFiber {S : Scheme.{u}} (G : GroupoidScheme S)
    (p : (G.objects ⊗ G.objects).left) :
    { h : ModObj (fiberGroup G p) (fiberArrows G p) // IsFiberAction G p h }
```

**`AlgebraicGeometry.fiber_isFpqcTorsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Fiber.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/Fiber.lean#L103). The attribute's comment: “torsor property”.

> A nonempty fibre of the arrows over a pair is a torsor under the corresponding
> stabilizer group over the residue field.

```lean
theorem fiber_isFpqcTorsor {S : Scheme.{u}} (G : GroupoidScheme S)
    (p : (G.objects ⊗ G.objects).left) (h : Nonempty (fiberArrows G p).left) :
    IsFpqcTorsor
      (Scheme.Spec.obj (.op ((G.objects ⊗ G.objects).left.residueField p)))
      (fiberGroup G p) (fiberArrows G p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.17, Tag 03LM](https://stacks.math.columbia.edu/tag/03LM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
