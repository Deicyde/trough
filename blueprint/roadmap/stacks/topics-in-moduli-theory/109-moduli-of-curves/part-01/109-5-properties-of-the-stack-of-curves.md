---
declaration: section
origin: cited
lean: AlgebraicGeometry.isSeparated_and_isRelativelyFinitePresentation_diagonal_curves, AlgebraicGeometry.isQuasiSeparated_and_isLocallyOfFinitePresentation_curvesAlgebraicStack
statement: formalized
proof: formalized
---

# 109.5 Properties of the stack of curves

Section 109.5 of the Stacks Project, [Tag 0DSP](https://stacks.math.columbia.edu/tag/0DSP). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DSQ, a lemma

[Tag 0DSQ](https://stacks.math.columbia.edu/tag/0DSQ) in the Stacks Project.

**`AlgebraicGeometry.isSeparated_and_isRelativelyFinitePresentation_diagonal_curves`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesDiagonalUnconditional.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesDiagonalUnconditional.lean#L58).

> **Stacks 0DSQ.** The diagonal of the algebraic stack `Curves` over `Spec ℤ` is separated and
> of finite presentation.

```lean
theorem isSeparated_and_isRelativelyFinitePresentation_diagonal_curves :
    Stack.IsSeparated B integerBase hZ
        (Stack.relativeDiagonal.{u, u, u + 1} B integerBase hZ
          (curvesAlgebraicStack B hZ
            (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)).val
          (Stack.schemeStack.{u, w} B integerBase hZ (Over.mk (𝟙 (B.obj hZ)))).val
          (Stack.structureMorphism B integerBase hZ (curvesAlgebraicStack B hZ
            (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ))).hom) ∧
      Stack.AlgebraicStacks.IsRelativelyFinitePresentation B integerBase hZ
        (Stack.AlgebraicStacks.relativeDiagonal B integerBase hZ
          (Stack.structureMorphism B integerBase hZ (curvesAlgebraicStack B hZ
            (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ))))
```

## Tag 0DSS, a lemma

[Tag 0DSS](https://stacks.math.columbia.edu/tag/0DSS) in the Stacks Project.

**`AlgebraicGeometry.isQuasiSeparated_and_isLocallyOfFinitePresentation_curvesAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesQuasiSeparatedLocallyFinitePresentation.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesQuasiSeparatedLocallyFinitePresentation.lean#L53).

> **Stacks 0DSS.** The morphism `Curves → Spec(ℤ)` of the algebraic stack of curves is
> quasi-separated and locally of finite presentation.
>
> Quasi-separatedness is the quasi-compactness and quasi-separatedness of the diagonal, given by
> the finite presentation of the diagonal in Stacks 0DSQ
> (`AlgebraicGeometry.isSeparated_and_isRelativelyFinitePresentation_diagonal_curves`); local
> finite presentation is Stacks 0CMY applied to Stacks 0D55
> (`AlgebraicGeometry.isLimitPreserving_curvesFiberedCategory_unconditional`).

```lean
theorem isQuasiSeparated_and_isLocallyOfFinitePresentation_curvesAlgebraicStack :
    Stack.AlgebraicStacks.IsQuasiSeparated B integerBase hZ
        (Stack.structureMorphism B integerBase hZ (curvesAlgebraicStack B hZ
          (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ))) ∧
      Stack.AlgebraicStacks.IsLocallyOfFinitePresentation B integerBase hZ
        (Stack.structureMorphism B integerBase hZ (curvesAlgebraicStack B hZ
          (C1590Private.isAlgebraicStack_curvesFiberedCategory.{u, w} B hZ)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.5, Tag 0DSP](https://stacks.math.columbia.edu/tag/0DSP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
