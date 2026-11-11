---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.ThickeningPushout.fiberSquareComparison_isEquivalence
statement: formalized
proof: formalized
---

# 98.4 Pushouts and stacks

Section 98.4 of the Stacks Project, [Tag 07WM](https://stacks.math.columbia.edu/tag/07WM). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07WN, a lemma

[Tag 07WN](https://stacks.math.columbia.edu/tag/07WN) in the Stacks Project.

**`AlgebraicGeometry.Stack.ThickeningPushout.fiberSquareComparison_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ThickeningPushoutEquivalence.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ThickeningPushoutEquivalence.lean#L66).

> Let `Y' = Y ⨿_X X'` be the pushout of a thickening `i : X ⟶ X'` and an affine morphism
> `f : X ⟶ Y` of schemes over `S`, and let `𝒵` be an algebraic stack over `S`. The functor of fibre
> categories `𝒵_{Y'} ⟶ 𝒵_Y ×_{𝒵_X} 𝒵_{X'}` is an equivalence.

```lean
theorem fiberSquareComparison_isEquivalence.{w'}
    (𝒵 : BasedCategory.{u, u + 1} (BigFppfOver B S hS))
    (h𝒵 : IsAlgebraicStack.{u, w'} B S hS 𝒵)
    {X X' Y Y' : BigFppfOver B S hS} (i : X ⟶ X') (f : X ⟶ Y) (a : X' ⟶ Y') (b : Y ⟶ Y')
    (w : i ≫ a = f ≫ b)
    (hi : Stacks.Thickenings.IsThickening ((BigFppfOver.toScheme B S hS).map i))
    [IsAffineHom ((BigFppfOver.toScheme B S hS).map f)]
    (hsq : IsPushout ((BigFppfOver.toScheme B S hS).map i)
      ((BigFppfOver.toScheme B S hS).map f) ((BigFppfOver.toScheme B S hS).map a)
      ((BigFppfOver.toScheme B S hS).map b)) :
    letI : 𝒵.p.IsFibered := (Classical.choose h𝒵).isFibered
    (Deformation.Artin.fiberSquareComparison 𝒵.p 𝒵.p.chosenPullbacks f i b a
      w.symm).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.4, Tag 07WM](https://stacks.math.columbia.edu/tag/07WM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
