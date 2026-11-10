---
declaration: section
origin: cited
lean: AlgebraicGeometry.FourierMukaiKernelObj.category, AlgebraicGeometry.FourierMukaiKernelObj.baseChangeFunctor
statement: formalized
proof: formalized
---

# 57.14 A category of Fourier-Mukai kernels

Section 57.14 of the Stacks Project, [Tag 0G0F](https://stacks.math.columbia.edu/tag/0G0F). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G0F, the section

[Tag 0G0F](https://stacks.math.columbia.edu/tag/0G0F) in the Stacks Project.

**`AlgebraicGeometry.FourierMukaiKernelObj.category`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/KernelCategoryInstance.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/KernelCategoryInstance.lean#L72). The attribute's comment: “the category, with all four clauses of the source: objects the proper smooth schemes over S; morphisms X to Y the isomorphism classes of objects of D_perf(O_{X x_S Y}); composition the class of R pr_13,*(L pr_12^*K tensor^L L pr_23^*K'), perfect by Tag 0B91 (isPerfect_convolution); identity the class of Delta_{X/S,*}O_X; associativity and the unit laws are the category axioms, proved. Clauses (3) and (4) are mk_comp_mk and id_eq”.

> **[Stacks, Tag 0G0F]: the category of Fourier-Mukai kernels over `S`.** Its objects are the
> proper smooth schemes over `S` (`AlgebraicGeometry.FourierMukaiKernelObj`), its morphisms from `X`
> to `Y` the isomorphism classes of objects of `D_perf(𝒪_{X ×_S Y})`
> (`AlgebraicGeometry.FourierMukaiKernelObj.Hom`), composition of the classes of `K` and `K'` the
> class of `R pr_{13,*}(L pr_{12}^*K ⊗^𝐋 L pr_{23}^*K')`, which is perfect by [Stacks, Tag 0B91]
> (`AlgebraicGeometry.FourierMukaiKernelObj.isPerfect_convolution`), and identity of `X` the class of
> `Δ_{X/S,*}𝒪_X`. The unit laws and associativity are proved
> (`AlgebraicGeometry.diagonalKernelConvolutionIso`,
> `AlgebraicGeometry.convolutionDiagonalKernelIso`,
> `AlgebraicGeometry.fourierMukaiConvolutionAssocIso`).

```lean
instance category : Category (FourierMukaiKernelObj S)
```

## Tag 0G0G, a lemma

[Tag 0G0G](https://stacks.math.columbia.edu/tag/0G0G) in the Stacks Project.

**`AlgebraicGeometry.FourierMukaiKernelObj.baseChangeFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/KernelCategoryInstance.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/KernelCategoryInstance.lean#L97). The attribute's comment: “the functor between the categories of Tag 0G0F over S and over S1, both built with the perfectness of convolution proved (Tag 0B91): objects X go to the base change, written X x_S S1 (the source's S1 x_S X up to the symmetry of the fibre product), morphisms the class of K to the class of L(X1 x_{S1} Y1 --> X x_S Y)^*K; preservation of identities and of composition are the functor axioms, proved. The two rules are baseChangeFunctor_obj and baseChangeFunctor_map_mk”.

> **[Stacks, Tag 0G0G]: base change along `s : S₁ ⟶ S` is a functor** from the category of
> Fourier-Mukai kernels over `S` to the one over `S₁`. On objects it sends `X` to its base change
> `X ×_S S₁ ⟶ S₁` and on morphisms the class of `K` on `X ×_S Y` to the class of
> `L(X₁ ×_{S₁} Y₁ ⟶ X ×_S Y)^*K`.

```lean
def baseChangeFunctor (s : S₁ ⟶ S) : FourierMukaiKernelObj S ⥤ FourierMukaiKernelObj S₁
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.14, Tag 0G0F](https://stacks.math.columbia.edu/tag/0G0F)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
