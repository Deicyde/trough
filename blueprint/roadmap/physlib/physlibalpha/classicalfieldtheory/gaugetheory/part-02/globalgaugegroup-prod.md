---
declaration: module
origin: cited
lean: GlobalGaugeGroup.prod, GlobalGaugeGroup.mem_prod_iff, GlobalGaugeGroup.prodGroupHom, GlobalGaugeGroup.prodGroupHom_val, GlobalGaugeGroup.prodGroupHom_surjective, GlobalGaugeGroup.prodGroupHom_injective, GlobalGaugeGroup.prodGroupEquiv, GlobalGaugeGroup.prodGroupEquiv_apply
statement: formalized
proof: formalized
---

# The product of global gauge groups

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.Prod`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean): 13 declarations, 11 with a docstring.

> The product `G₁ × G₂` of two global gauge groups, acting block-diagonally.

## i. Overview

> The gauge group of a theory with several independent gauge interactions is a product of
> groups, such as `SU(3) × SU(2) × U(1)` for the Standard Model. For global gauge groups
> `G₁ ⊆ GL(κ₁, ℂ)` and `G₂ ⊆ GL(κ₂, ℂ)` the product sits inside `GL(κ₁ ⊕ κ₂, ℂ)` as the
> block-diagonal matrices `diag(g₁, g₂)` with `g₁ ∈ G₁` and `g₂ ∈ G₂`. Taking the two diagonal
> blocks is a continuous left inverse of `(A₁, A₂) ↦ diag(A₁, A₂)`, so this embedding is
> closed, and so is the induced embedding of pairs of invertible matrices. The product group is
> the image of the closed set `G₁ × G₂` under it, and so it is closed.
>
> The Lie algebra of the product is the direct sum of the Lie algebras. A block-diagonal
> matrix `diag(X₁, X₂)` of generators is a generator of the product, since the exponential of
> a block-diagonal matrix is taken blockwise. Conversely, the one-parameter subgroup of a
> generator of the product lies in the closed subspace of block-diagonal matrices, so the
> generator, its derivative at `t = 0`, does too, and its diagonal blocks are generators.

## ii. Key results

> - `GlobalGaugeGroup.prod` : the product of two global gauge groups.
> - `GlobalGaugeGroup.mem_prod_iff` : the elements of the product are the block-diagonal
>   matrices `diag(g₁, g₂)` with `g₁ ∈ G₁` and `g₂ ∈ G₂`.
> - `GlobalGaugeGroup.prodGroupEquiv` : the elements of the product are the pairs of elements of
>   the factors.
> - `GlobalGaugeGroup.exp_smul_eq_fromBlocks_of_mem_lieAlgebra_prod` : the exponential of a
>   generator of the product is taken blockwise.
> - `GlobalGaugeGroup.mem_lieAlgebra_prod_iff` : the generators of the product are the
>   block-diagonal matrices of generators.

## iv. References

> * None.

## A. The product of global gauge groups

**`GlobalGaugeGroup.prod`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean#L76).

> The product of two global gauge groups `G₁` and `G₂`, made of the block-diagonal matrices
> `diag(g₁, g₂)` with `g₁ ∈ G₁` and `g₂ ∈ G₂`. It is the image of `G₁ × G₂` under the
> block-diagonal embedding of pairs of invertible matrices, which is closed since taking the
> two diagonal blocks is a continuous left inverse.

```lean
def prod : GlobalGaugeGroup (κ₁ ⊕ κ₂)
```

**`GlobalGaugeGroup.mem_prod_iff`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean#L97).

> The elements of the product are the block-diagonal matrices `diag(g₁, g₂)` with
> `g₁ ∈ G₁` and `g₂ ∈ G₂`.

```lean
lemma mem_prod_iff {g : GeneralLinearGroup (κ₁ ⊕ κ₂) ℂ} :
    g ∈ (G₁.prod G₂).group ↔ ∃ g₁ ∈ G₁.group, ∃ g₂ ∈ G₂.group,
      fromBlocks (g₁ : Matrix κ₁ κ₁ ℂ) 0 0 (g₂ : Matrix κ₂ κ₂ ℂ) = g
```

### A.1. Pairs of elements

**`GlobalGaugeGroup.prodGroupHom`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean#L113).

> The pair `(g₁, g₂)` as the element `diag(g₁, g₂)` of the product.

```lean
noncomputable def prodGroupHom : G₁.group × G₂.group →* (G₁.prod G₂).group
```

**`GlobalGaugeGroup.prodGroupHom_val`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean#L123).

```lean
lemma prodGroupHom_val (g : G₁.group × G₂.group) :
    (((prodGroupHom G₁ G₂ g : (G₁.prod G₂).group) : GeneralLinearGroup (κ₁ ⊕ κ₂) ℂ) :
      Matrix (κ₁ ⊕ κ₂) (κ₁ ⊕ κ₂) ℂ) = fromBlocks ((g.1 : GeneralLinearGroup κ₁ ℂ) :
        Matrix κ₁ κ₁ ℂ) 0 0 ((g.2 : GeneralLinearGroup κ₂ ℂ) : Matrix κ₂ κ₂ ℂ)
```

**`GlobalGaugeGroup.prodGroupHom_surjective`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean#L129).

> Every element of the product is a block-diagonal matrix `diag(g₁, g₂)`.

```lean
lemma prodGroupHom_surjective : Function.Surjective (prodGroupHom G₁ G₂)
```

**`GlobalGaugeGroup.prodGroupHom_injective`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean#L135).

> A block-diagonal matrix determines its two blocks.

```lean
lemma prodGroupHom_injective : Function.Injective (prodGroupHom G₁ G₂)
```

**`GlobalGaugeGroup.prodGroupEquiv`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean#L142).

> The elements of the product of two global gauge groups are the pairs of their elements, as
> block-diagonal matrices.

```lean
noncomputable def prodGroupEquiv : G₁.group × G₂.group ≃* (G₁.prod G₂).group
```

**`GlobalGaugeGroup.prodGroupEquiv_apply`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean#L147).

```lean
lemma prodGroupEquiv_apply (g : G₁.group × G₂.group) :
    prodGroupEquiv G₁ G₂ g = prodGroupHom G₁ G₂ g
```

## B. The Lie algebra of the product

### B.1. The generators of the product

**`GlobalGaugeGroup.fromBlocks_mem_lieAlgebra_prod`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean#L160).

> A block-diagonal matrix `diag(X₁, X₂)` of generators of `G₁` and `G₂` is a generator of
> the product, since its exponential is taken blockwise.

```lean
lemma fromBlocks_mem_lieAlgebra_prod {X₁ : Matrix κ₁ κ₁ ℂ} {X₂ : Matrix κ₂ κ₂ ℂ}
    (hX₁ : X₁ ∈ G₁.lieAlgebra) (hX₂ : X₂ ∈ G₂.lieAlgebra) :
    fromBlocks X₁ 0 0 X₂ ∈ (G₁.prod G₂).lieAlgebra
```

**`GlobalGaugeGroup.eq_fromBlocks_of_mem_lieAlgebra_prod`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean#L174).

> A generator of the product is block-diagonal. Its one-parameter subgroup lies in the
> closed subspace of block-diagonal matrices, and so does its derivative at `t = 0`.

```lean
lemma eq_fromBlocks_of_mem_lieAlgebra_prod {X : Matrix (κ₁ ⊕ κ₂) (κ₁ ⊕ κ₂) ℂ}
    (hX : X ∈ (G₁.prod G₂).lieAlgebra) : X = fromBlocks X.toBlocks₁₁ 0 0 X.toBlocks₂₂
```

**`GlobalGaugeGroup.toBlocks_mem_lieAlgebra_of_mem_lieAlgebra_prod`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean#L203).

> The diagonal blocks of a generator of the product are generators of `G₁` and `G₂`.

```lean
lemma toBlocks_mem_lieAlgebra_of_mem_lieAlgebra_prod {X : Matrix (κ₁ ⊕ κ₂) (κ₁ ⊕ κ₂) ℂ}
    (hX : X ∈ (G₁.prod G₂).lieAlgebra) :
    X.toBlocks₁₁ ∈ G₁.lieAlgebra ∧ X.toBlocks₂₂ ∈ G₂.lieAlgebra
```

**`GlobalGaugeGroup.exp_smul_eq_fromBlocks_of_mem_lieAlgebra_prod`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean#L229).

> The exponential of a generator of the product is the block-diagonal matrix of the
> exponentials of its diagonal blocks.

```lean
lemma exp_smul_eq_fromBlocks_of_mem_lieAlgebra_prod {X : Matrix (κ₁ ⊕ κ₂) (κ₁ ⊕ κ₂) ℂ}
    (hX : X ∈ (G₁.prod G₂).lieAlgebra) (t : ℝ) :
    exp (t • X) = fromBlocks (exp (t • X.toBlocks₁₁)) 0 0 (exp (t • X.toBlocks₂₂))
```

**`GlobalGaugeGroup.mem_lieAlgebra_prod_iff`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean#L237).

> The generators of the product of global gauge groups are the block-diagonal matrices
> `diag(X₁, X₂)` with `X₁` a generator of `G₁` and `X₂` a generator of `G₂`.

```lean
lemma mem_lieAlgebra_prod_iff {X : Matrix (κ₁ ⊕ κ₂) (κ₁ ⊕ κ₂) ℂ} :
    X ∈ (G₁.prod G₂).lieAlgebra ↔
      ∃ X₁ ∈ G₁.lieAlgebra, ∃ X₂ ∈ G₂.lieAlgebra, X = fromBlocks X₁ 0 0 X₂
```

## Depends on

- [The Lie algebra of a global gauge group](globalgaugegroup-liealgebra-basic.md)

## Proof depends on

- [Exponentials of block-diagonal, Kronecker and scalar matrices](../../../mathematics/part-02/formathlib/analysis-normed-algebra-matrixexponential.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Prod.lean)
