---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsQuasiCompactStack, AlgebraicGeometry.Stack.isQuasiCompactStack_iff_hasAffineSmoothPresentation, AlgebraicGeometry.Stack.hasAffineSmoothPresentation_iff_hasQuasiCompactSchemeSmoothPresentation, AlgebraicGeometry.Stack.hasQuasiCompactSchemeSmoothPresentation_iff_hasQuasiCompactSpaceSmoothPresentation, AlgebraicGeometry.Stack.hasQuasiCompactSpaceSmoothPresentation_iff_hasQuasiCompactStackSurjection, AlgebraicGeometry.Stack.isQuasiCompactStack_of_isOpenSubstackCover
statement: formalized
proof: formalized
---

# 100.6 Quasi-compact algebraic stacks

Section 100.6 of the Stacks Project, [Tag 04YA](https://stacks.math.columbia.edu/tag/04YA). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04YB, a definition

[Tag 04YB](https://stacks.math.columbia.edu/tag/04YB) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsQuasiCompactStack`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactStack.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactStack.lean#L50).

> An algebraic stack over `S` is *quasi-compact* when its space of points, with the topology
> `pointTopology`, is a compact space.

```lean
abbrev IsQuasiCompactStack
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (_h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val) : Prop
```

## Tag 04YC, a lemma

[Tag 04YC](https://stacks.math.columbia.edu/tag/04YC) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasiCompactStack_iff_hasAffineSmoothPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationQuasiCompact.lean, line 433](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationQuasiCompact.lean#L433). The attribute's comment: “parts (1) and (2)”.

> An algebraic stack is quasi-compact if and only if it has a surjective smooth presentation by
> an affine scheme.

```lean
theorem isQuasiCompactStack_iff_hasAffineSmoothPresentation :
    IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property ↔
      HasAffineSmoothPresentation.{u, w} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.hasAffineSmoothPresentation_iff_hasQuasiCompactSchemeSmoothPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationQuasiCompact.lean, line 450](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationQuasiCompact.lean#L450). The attribute's comment: “parts (2) and (3)”.

> An algebraic stack has a surjective smooth presentation by an affine scheme if and only if it
> has one by a quasi-compact scheme.

```lean
theorem hasAffineSmoothPresentation_iff_hasQuasiCompactSchemeSmoothPresentation :
    HasAffineSmoothPresentation.{u, w} B S hS 𝒳 ↔
      HasQuasiCompactSchemeSmoothPresentation.{u, w} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.hasQuasiCompactSchemeSmoothPresentation_iff_hasQuasiCompactSpaceSmoothPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationQuasiCompact.lean, line 462](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationQuasiCompact.lean#L462). The attribute's comment: “parts (3) and (4)”.

> An algebraic stack has a surjective smooth presentation by a quasi-compact scheme if and only
> if it has one by a quasi-compact algebraic space.

```lean
theorem hasQuasiCompactSchemeSmoothPresentation_iff_hasQuasiCompactSpaceSmoothPresentation :
    HasQuasiCompactSchemeSmoothPresentation.{u, w} B S hS 𝒳 ↔
      HasQuasiCompactSpaceSmoothPresentation.{u, w} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.hasQuasiCompactSpaceSmoothPresentation_iff_hasQuasiCompactStackSurjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationQuasiCompact.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationQuasiCompact.lean#L476). The attribute's comment: “parts (4) and (5)”.

> An algebraic stack has a surjective smooth presentation by a quasi-compact algebraic space if
> and only if there is a surjection onto it from a quasi-compact algebraic stack.

```lean
theorem hasQuasiCompactSpaceSmoothPresentation_iff_hasQuasiCompactStackSurjection :
    HasQuasiCompactSpaceSmoothPresentation.{u, w} B S hS 𝒳 ↔
      HasQuasiCompactStackSurjection.{u, w} B S hS 𝒳
```

## Tag 04YD, a lemma

[Tag 04YD](https://stacks.math.columbia.edu/tag/04YD) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasiCompactStack_of_isOpenSubstackCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactStackCover.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactStackCover.lean#L119). The attribute's comment: “the union is quasi-compact”.

> **Stacks 04YD**, quasi-compactness. An algebraic stack covered by finitely many
> quasi-compact open substacks is quasi-compact; in particular a finite disjoint union of
> quasi-compact algebraic stacks is quasi-compact, disjointness of the members playing no role.
> The points of the substacks cover the points of `𝒳`, so this is the topological fact that a
> finite union of quasi-compact subsets is quasi-compact.

```lean
theorem isQuasiCompactStack_of_isOpenSubstackCover
    {ι : Type*} [Finite ι] (𝒳 : AlgebraicStacks.{u, w} B S hS) (𝒰 : ι → OpenSubstack 𝒳)
    (hcover : IsOpenSubstackCover 𝒳 𝒰)
    (h𝒰 : ∀ i, IsQuasiCompactStack.{u, w} B S hS
      (fullSubcategoryAlgebraicStack 𝒳 (𝒰 i).property (𝒰 i).isAlgebraic).val
      (fullSubcategoryAlgebraicStack 𝒳 (𝒰 i).property (𝒰 i).isAlgebraic).property) :
    IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 100.6, Tag 04YA](https://stacks.math.columbia.edu/tag/04YA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
