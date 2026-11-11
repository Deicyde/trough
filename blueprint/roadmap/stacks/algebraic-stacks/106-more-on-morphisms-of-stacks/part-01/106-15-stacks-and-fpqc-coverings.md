---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isStack_fpqc_of_isQuasiAffineHom_diagonal, AlgebraicGeometry.Stack.isMorSheaf_fpqc_of_isAlgebraicStack
statement: formalized
proof: formalized
---

# 106.15 Stacks and fpqc coverings

Section 106.15 of the Stacks Project, [Tag 0GRG](https://stacks.math.columbia.edu/tag/0GRG). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GRH, a proposition

[Tag 0GRH](https://stacks.math.columbia.edu/tag/0GRH) in the Stacks Project.

**`AlgebraicGeometry.Stack.isStack_fpqc_of_isQuasiAffineHom_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FpqcDescent/Stack.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FpqcDescent/Stack.lean#L159).

> **Stacks 0GRH.** An algebraic stack `𝒳` over `S` with quasi-affine diagonal satisfies descent
> for fpqc coverings: it is a stack for the fpqc topology of the big fppf site over `S`.

```lean
theorem isStack_fpqc_of_isQuasiAffineHom_diagonal
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (hΔ : IsQuasiAffineHom B S hS (diagonal.{u, u, u} B S hS 𝒳)) :
    𝒳.val.p.IsStack
      ((Scheme.fpqcPrecoverage.comap (BigFppfOver.toScheme B S hS)).toGrothendieck)
```

**`AlgebraicGeometry.Stack.isMorSheaf_fpqc_of_isAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceFpqcSheaf.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/IsomSpaceFpqcSheaf.lean#L131). The attribute's comment: “the full-faithfulness half of the proof: condition (2) of the fpqc stack condition, that the presheaves Mor(x, y) = Isom(x, y) of an algebraic stack are sheaves for the fpqc topology. No hypothesis on the diagonal is carried: representability of the diagonal by algebraic spaces, which every algebraic stack has, already suffices for this half, so the quasi-affine diagonal of the source and the ind-quasi-affine diagonal of its footnote are both dropped. The essential-surjectivity half, effectivity of fpqc descent data, is not formalized.”.

> **The full-faithfulness half of Stacks 0GRH**: condition (2) of the fpqc stack condition for
> an algebraic stack. For every scheme `U` over `S` and all objects `x`, `y` of the fibre of an
> algebraic stack `𝒳` over `U`, the presheaf `Mor(x, y)` of Stacks 02ZB is a sheaf for the fpqc
> topology on the localization at `U`.

```lean
theorem isMorSheaf_fpqc_of_isAlgebraicStack
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (U : BigFppfOver B S hS) (x y : 𝒳.val.p.Fiber U) :
    haveI : 𝒳.val.p.IsFibered := 𝒳.isFiberedInGroupoids.isFibered
    𝒳.val.p.IsMorSheaf
      ((Scheme.fpqcPrecoverage.comap (BigFppfOver.toScheme B S hS)).toGrothendieck) U x y
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 106.15, Tag 0GRG](https://stacks.math.columbia.edu/tag/0GRG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
