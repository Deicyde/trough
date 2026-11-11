---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidInAlgebraicSpaces.isInvariantOpen_largestOpenSubspace_source, AlgebraicGeometry.GroupoidInAlgebraicSpaces.stabilizerProjectionOverOpen, AlgebraicGeometry.GroupoidInAlgebraicSpaces.isInvariantOpen_of_isGreatest_stabilizer
statement: formalized
proof: formalized
---

# 79.6 Properties of groupoids

Section 79.6 of the Stacks Project, [Tag 044Y](https://stacks.math.columbia.edu/tag/044Y). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 044Z, a lemma

[Tag 044Z](https://stacks.math.columbia.edu/tag/044Z) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isInvariantOpen_largestOpenSubspace_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/InvariantSourceLocus.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/InvariantSourceLocus.lean#L108).

> **Stacks 044Z.** Let `G` be a groupoid in algebraic spaces whose source and target
> morphisms are both coverings for a topology `τ` other than the fpqc topology, and let `P` be a
> property of morphisms of algebraic spaces local on the target for `τ`. The largest open
> subspace of the object space over which the restriction of the source morphism has `P` is
> invariant under `G`.

```lean
theorem isInvariantOpen_largestOpenSubspace_source (G : GroupoidInAlgebraicSpaces C S hS B)
    (τ : Space.Topology) (hτ : τ ≠ .fpqc) (P : MorphismProperty (AlgebraicSpaces C S hS))
    [P.IsLocalAtTarget (Space.Topology.precoverage.{u, u + 1} τ C S hS)]
    (hs : τ.IsCovering C S hS (fun _ : Unit => G.arrows.obj) (fun _ => G.source.hom))
    (ht : τ.IsCovering C S hS (fun _ : Unit => G.arrows.obj) (fun _ => G.target.hom)) :
    IsInvariantOpen G (Space.largestOpenSubspace C S hS τ hτ P G.source).1.1
```

## Tag 06R4, a lemma

[Tag 06R4](https://stacks.math.columbia.edu/tag/06R4) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.stabilizerProjectionOverOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/InvariantStabilizerLocus.lean, line 691](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/InvariantStabilizerLocus.lean#L691). The attribute's comment: “the stabilizer restricted over an open subspace of the object space”.

> **Stacks 06R4.** The restriction of the stabilizer of a groupoid in algebraic spaces over
> an open subspace of the object space.

```lean
noncomputable def stabilizerProjectionOverOpen
    (W : {W : Subfunctor G.objects.obj // Space.IsOpenSubspace C S hS W}) :
    AlgebraicSpaces.fiberProduct C S hS (stabilizerToObjects G)
        (Space.openInclusion C S hS W) ⟶ Space.openObject C S hS W
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isInvariantOpen_of_isGreatest_stabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/InvariantStabilizerLocus.lean, line 721](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/InvariantStabilizerLocus.lean#L721). The attribute's comment: “invariance of the maximal open stabilizer-property locus”.

> **Stacks 06R4.** Let `G` be a groupoid in algebraic spaces whose source and target
> morphisms are both coverings for a topology `τ` other than the fpqc topology, and let `P` be a
> property of morphisms of algebraic spaces local on the target for `τ`. A greatest open
> subspace of the object space over which the restriction of the stabilizer has `P` is invariant
> under `G`.

```lean
theorem isInvariantOpen_of_isGreatest_stabilizer (τ : Space.Topology) (hτ : τ ≠ .fpqc)
    (P : MorphismProperty (AlgebraicSpaces C S hS))
    [P.IsLocalAtTarget (Space.Topology.precoverage.{u, u + 1} τ C S hS)]
    (hs : τ.IsCovering C S hS (fun _ : Unit => G.arrows.obj) (fun _ => G.source.hom))
    (ht : τ.IsCovering C S hS (fun _ : Unit => G.arrows.obj) (fun _ => G.target.hom))
    (W : {W : Subfunctor G.objects.obj // Space.IsOpenSubspace C S hS W})
    (hW : IsGreatest {V : {V : Subfunctor G.objects.obj // Space.IsOpenSubspace C S hS V} |
      P (stabilizerProjectionOverOpen G V)} W) :
    IsInvariantOpen G W.1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 79.6, Tag 044Y](https://stacks.math.columbia.edu/tag/044Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
