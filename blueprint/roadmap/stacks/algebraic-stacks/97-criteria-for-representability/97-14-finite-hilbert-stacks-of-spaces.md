---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isAlgebraicStack_absoluteHilbertFibered, AlgebraicGeometry.Stack.isAlgebraicStack_finiteHilbertFibered
statement: formalized
proof: formalized
---

# 97.14 Finite Hilbert stacks of spaces

Section 97.14 of the Stacks Project, [Tag 05YR](https://stacks.math.columbia.edu/tag/05YR). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05YS, a lemma

[Tag 05YS](https://stacks.math.columbia.edu/tag/05YS) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_absoluteHilbertFibered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/HilbertCoverAlgebraic.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/HilbertCoverAlgebraic.lean#L96). The attribute's comment: “`NeZero d` restricts nothing: Examples of Stacks, Section 95.18 (Stacks 05WA) introduces `ℋ_d(X)` only `For each integer d ≥ 1`, and the source's proof of this lemma cites Stacks 05YQ, which stands under the `Let d ≥ 1 be an integer` of Section 97.13 (Stacks 05YL)”.

> The finite Hilbert stack `ℋ_d(𝒳)` of an algebraic space `𝒳` over `S` is an algebraic
> stack.

```lean
theorem isAlgebraicStack_absoluteHilbertFibered [NeZero d]
    (𝒳 : StackInGroupoids.{w, u, u, u + 1, u + 1} (BigFppfOver B S hS)
      (BigFppfOver.topology B S hS))
    (h𝒳 : IsRepresentableByAlgebraicSpace B S hS
      (CatFiberedInGroupoids.mk 𝒳.toBasedCategory
        𝒳.isStackInGroupoids.isFiberedInGroupoids)) :
    IsAlgebraicStack.{u, w} B S hS (absoluteHilbertFibered 𝒳 d).val
```

## Tag 06CI, a lemma

[Tag 06CI](https://stacks.math.columbia.edu/tag/06CI) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_finiteHilbertFibered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/RelativeAlgebraicity.lean, line 554](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteHilbert/RelativeAlgebraicity.lean#L554). The attribute's comment: “for positive degree d, the domain on which the source defines the finite Hilbert stack”.

> **Stacks 06CI.** For positive degree `d`, the relative finite Hilbert stack `ℋ_d(𝒳/𝒴)` of a
> 1-morphism `F : 𝒳 ⟶ 𝒴` of stacks in groupoids over the big fppf site of `S` with `𝒳`
> representable by an algebraic space and `F` representable by algebraic spaces, surjective, flat
> and locally of finite presentation is an algebraic stack.
>
> The hypothesis `hd : 0 < d` is the domain of the statement, not a restriction of it: the source
> defines `ℋ_d(𝒳/𝒴)` only for `d ≥ 1` (Examples of Stacks, Section 05WA).
>
> Writing `𝒰` for a scheme atlas of `ℋ_d(𝒳)` and `𝒲 = ℋ_d(𝒳/𝒴) ×_{ℋ_d(𝒳)} 𝒰`, the 1-morphism
> `𝒲 ⟶ ℋ_d(𝒳/𝒴)` is a base change of `𝒰 ⟶ ℋ_d(𝒳)`, hence representable by algebraic spaces,
> surjective and smooth (Stacks 0302 and Stacks 045C), and `𝒲` is representable by an algebraic
> space, so Stacks 05UL applies to it.

```lean
theorem isAlgebraicStack_finiteHilbertFibered (hd : 0 < d)
    (h𝒴 : Functor.IsStack 𝒴.toBasedCategory.p (BigFppfOver.topology B S hS))
    (h𝒳 : IsRepresentableByAlgebraicSpace B S hS (targetCFG (𝒴 := 𝒳)))
    (hF : IsRepresentableByAlgebraicSpaces B S hS F)
    (hFprops : RelativeFlatPresentation (F := F)) :
    IsAlgebraicStack.{u, w} B S hS (finiteHilbertFibered B S hS d 𝒳 𝒴 F).val
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.14, Tag 05YR](https://stacks.math.columbia.edu/tag/05YR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
