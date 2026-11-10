---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.exists_isFlatAt_iff_forall_isFlatAt, AlgebraicGeometry.Stack.AlgebraicStacks.IsFlatAt
statement: formalized
proof: formalized
---

# 101.26 Flat at a point

Section 101.26 of the Stacks Project, [Tag 0CIB](https://stacks.math.columbia.edu/tag/0CIB). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CIC, a lemma

[Tag 0CIC](https://stacks.math.columbia.edu/tag/0CIC) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_isFlatAt_iff_forall_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatAtAPoint/IndependenceOfDiagram.lean, line 802](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatAtAPoint/IndependenceOfDiagram.lean#L802).

> **Stacks 0CIC.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` and let `x` be
> a point of `|𝒳|`. The top horizontal morphism of *some* diagram of
> `AlgebraicGeometry.Stack.AlgebraicStacks.PointedFlatDiagram` is flat at its marked point if and
> only if the top horizontal morphism of *every* such diagram is.
>
> The forward implication is the iterated-2-fibre-product chase of the source; the backward one
> holds because such a diagram exists through every point of `|𝒳|`.

```lean
theorem exists_isFlatAt_iff_forall_isFlatAt {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (x : points B S hS 𝒳) :
    (∃ d : PointedFlatDiagram B S hS f x, Space.IsFlatAt B S hS d.h d.u) ↔
      ∀ d : PointedFlatDiagram B S hS f x, Space.IsFlatAt B S hS d.h d.u
```

## Tag 0CID, a definition

[Tag 0CID](https://stacks.math.columbia.edu/tag/0CID) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsFlatAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatAtAPoint/PointedFlatDiagram.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatAtAPoint/PointedFlatDiagram.lean#L475).

> **Stacks 0CID.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` is *flat at* a point
> `x` of `|𝒳|` when the top horizontal morphism of some diagram of
> `AlgebraicGeometry.Stack.AlgebraicStacks.PointedFlatDiagram` is flat at its marked point.
>
> **Stacks 0CIC** identifies this with the corresponding condition on every such diagram, so the
> choice of the existential formulation is immaterial.

```lean
abbrev IsFlatAt {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (x : points B S hS 𝒳) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.26, Tag 0CIB](https://stacks.math.columbia.edu/tag/0CIB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
