---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsAlgebraicMorphism, AlgebraicGeometry.Stack.isAlgebraicStack_of_isAlgebraicMorphism, AlgebraicGeometry.Stack.isAlgebraicMorphism_of_isAlgebraicStack, AlgebraicGeometry.Stack.hasRepresentableDiagonal_of_isAlgebraicMorphism
statement: formalized
proof: formalized
---

# 97.8 Algebraic morphisms

Section 97.8 of the Stacks Project, [Tag 05XX](https://stacks.math.columbia.edu/tag/05XX). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06CF, a definition

[Tag 06CF](https://stacks.math.columbia.edu/tag/06CF) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsAlgebraicMorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicMorphism.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicMorphism.lean#L44).

> A morphism of stacks is algebraic if every base change along a
> scheme-valued point of its target is an algebraic stack.

```lean
abbrev IsAlgebraicMorphism.{u, wX, wY, w, vX, uX, vY, uY}
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 : StackInGroupoids.{wX, u, vX, u + 1, uX}
      (BigFppfOver B S hS)
      (BigFppfOver.topology B S hS)}
    {𝒴 : StackInGroupoids.{wY, u, vY, u + 1, uY}
      (BigFppfOver B S hS)
      (BigFppfOver.topology B S hS)}
    (f : 𝒳.toBasedCategory ⥤ᵇ 𝒴.toBasedCategory) : Prop
```

## Tag 05XY, a lemma

[Tag 05XY](https://stacks.math.columbia.edu/tag/05XY) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_of_isAlgebraicMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicMorphismSourceAlgebraic.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicMorphismSourceAlgebraic.lean#L88).

> Let `F : 𝒳 ⟶ 𝒴` be a 1-morphism of stacks in groupoids over the big fppf site of `S`. If `𝒴`
> is an algebraic stack and `F` is algebraic in the sense of Stacks 06CF, then `𝒳` is an algebraic
> stack.

```lean
theorem isAlgebraicStack_of_isAlgebraicMorphism
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : StackInGroupoids.{w, u, u, u + 1, u + 1}
      (BigFppfOver B S hS) (BigFppfOver.topology B S hS)}
    (f : 𝒳 ⟶ 𝒴)
    (h𝒳 : 𝒳.toBasedCategory.p.IsStack (BigFppfOver.topology B S hS))
    (h𝒴 : IsAlgebraicStack.{u, w} B S hS 𝒴.toBasedCategory)
    (hf : IsAlgebraicMorphism.{u, w, w, w} B S hS (𝒳 := 𝒳) (𝒴 := 𝒴) f.hom) :
    IsAlgebraicStack.{u, w} B S hS 𝒳.toBasedCategory
```

## Tag 06CG, a lemma

[Tag 06CG](https://stacks.math.columbia.edu/tag/06CG) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicMorphism_of_isAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicMorphismFromAlgebraicStack.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicMorphismFromAlgebraicStack.lean#L82).

> **Stacks 06CG.** Let `F : 𝒳 ⟶ 𝒴` be a 1-morphism of stacks in groupoids over the big fppf
> site of `S`. If `𝒳` is an algebraic stack and the diagonal of `𝒴` is representable by algebraic
> spaces, then `F` is algebraic in the sense of Stacks 06CF.

```lean
theorem isAlgebraicMorphism_of_isAlgebraicStack
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : StackInGroupoids.{w, u, u, u + 1, u + 1}
      (BigFppfOver B S hS) (BigFppfOver.topology B S hS)}
    (f : 𝒳 ⟶ 𝒴)
    (h𝒴 : 𝒴.toBasedCategory.p.IsStack (BigFppfOver.topology B S hS))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.toBasedCategory)
    (hΔ : HasRepresentableDiagonal B S hS
      (CatFiberedInGroupoids.mk 𝒴.toBasedCategory
        𝒴.isStackInGroupoids.isFiberedInGroupoids)) :
    IsAlgebraicMorphism.{u, w, w, w} B S hS (𝒳 := 𝒳) (𝒴 := 𝒴) f.hom
```

## Tag 0D3R, a lemma

[Tag 0D3R](https://stacks.math.columbia.edu/tag/0D3R) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasRepresentableDiagonal_of_isAlgebraicMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicMorphismRepresentableDiagonal.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicMorphismRepresentableDiagonal.lean#L111).

> **Stacks 0D3R.** An algebraic 1-morphism of stacks in groupoids over the big fppf site of
> `S` inherits a diagonal representable by algebraic spaces from its target.

```lean
theorem hasRepresentableDiagonal_of_isAlgebraicMorphism
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : StackInGroupoids.{w, u, u, u + 1, u + 1}
      (BigFppfOver B S hS) (BigFppfOver.topology B S hS)}
    (f : 𝒳 ⟶ 𝒴)
    (hf : IsAlgebraicMorphism.{u, w, w, w'} B S hS (𝒳 := 𝒳) (𝒴 := 𝒴) f.hom)
    (h𝒴 : HasRepresentableDiagonal B S hS
      (CatFiberedInGroupoids.mk 𝒴.toBasedCategory
        𝒴.isStackInGroupoids.isFiberedInGroupoids)) :
    HasRepresentableDiagonal B S hS
      (CatFiberedInGroupoids.mk 𝒳.toBasedCategory
        𝒳.isStackInGroupoids.isFiberedInGroupoids)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.8, Tag 05XX](https://stacks.math.columbia.edu/tag/05XX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
