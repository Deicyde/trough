---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.toLinearMap₂, TensorSpecies.Tensor.toLinearMap₂_apply, TensorSpecies.Tensor.toMatrix₂_toLinearMap₂, TensorSpecies.Tensor.contractInnerT, TensorSpecies.Tensor.contractInnerT_apply, TensorSpecies.Tensor.crossToEnd_eq_permT_contractInnerT, TensorSpecies.Tensor.toMatrix_contractInnerT, TensorSpecies.Tensor.contractInnerT_right_injective
statement: formalized
proof: formalized
---

# The bilinear map and the product of rank-two tensors

The module `Physlib.Relativity.Tensors.Contraction.RankTwo`, [Physlib/Relativity/Tensors/Contraction/RankTwo.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/RankTwo.lean): 9 declarations, 9 with a docstring.

> The bilinear map of a rank-two tensor and the product of two rank-two tensors.

## i. Overview

> A rank-two tensor `M` defines a bilinear map on one-slot tensors by contracting one argument into
> each of its slots, `t, s ↦ M_{zw} tᶻ sʷ`. In the bases dual to the slots of `M` the matrix of this
> map is the component matrix `toMatrix M`.
>
> `contractInnerT A B` is the tensor `A_{μν} B^{νρ}`, in which the second index of `A` is contracted
> with the first index of `B`. Its indices are `μ` and `ρ`, with colours `![cs 0, ds 1]`. The general
> contraction `crossToEnd` gives the same tensor, but its colours are a composite of the two colour
> lists. With `contractInnerT`, an identity such as `η_{μν} η^{νρ} = δ_μ^ρ` needs no renaming of the
> colours of the product. For contraction-dual bases, the matrix of `A_{μν} B^{νρ}` is the matrix
> product of `(A_{μν})` and `(B^{νρ})` (`toMatrix_contractInnerT`).

## ii. Key results

> - `TensorSpecies.Tensor.toLinearMap₂` : the bilinear map `t, s ↦ M_{zw} tᶻ sʷ` of a rank-two
>     tensor, with its component formula `toLinearMap₂_apply`.
> - `TensorSpecies.Tensor.toMatrix₂_toLinearMap₂` : its matrix in the dual bases is the component
>     matrix of `M`.
> - `TensorSpecies.Tensor.contractInnerT` : the contraction `A_{μν} B^{νρ}` of two rank-two tensors.
> - `TensorSpecies.Tensor.toMatrix_contractInnerT` : for contraction-dual bases, its matrix is the
>     matrix product.

## iv. References

> * None.

## A. Pairing a rank-two tensor with two vectors

> Contracting a vector into each slot of a rank-two tensor `M` gives a bilinear map. This holds for
> any species: the only colour condition is duality, an argument contracts with a slot when its
> colour is dual to the slot's. For a species without conjugation this map is the metric form
> itself; a species with conjugation composes it with conjugation of one argument to get a
> sesquilinear form (`ConjTensorSpecies.toSesqForm`).

**`TensorSpecies.Tensor.toLinearMap₂`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/RankTwo.lean#L77).

> The bilinear map `t, s ↦ M_{μν} tᵘ sᵛ` of a rank-two tensor: `t` fills the first index of `M`,
> `s` the second. For the Minkowski metric this is the inner product `η_{μν} tᵘ sᵛ`.

```lean
noncomputable def toLinearMap₂ (x y : C) {cM : Fin 2 → C} (M : Tensor S cM)
    (hx : S.τ x = cM 0 := by rfl) (hy : S.τ y = cM 1 := by rfl) :
    Tensor S ![x] →ₗ[k] Tensor S ![y] →ₗ[k] k
```

**`TensorSpecies.Tensor.toLinearMap₂_apply`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/RankTwo.lean#L85).

> In components, the bilinear map is `∑_{μ,ν} M_{μν} tᵘ sᵛ`.

```lean
lemma toLinearMap₂_apply [HasContrDualBases S] {x y : C} {cM : Fin 2 → C} (hx : S.τ x = cM 0)
    (hy : S.τ y = cM 1) (M : Tensor S cM) (t : Tensor S ![x]) (s : Tensor S ![y]) :
    toLinearMap₂ x y M hx hy t s =
      ∑ w : basisIdx y, ∑ z : basisIdx x,
        (basis ![x]).repr t (ComponentIdx.single.symm z) *
          toMatrix M (HasContrDualBases.dualIdxEquiv hx z) (HasContrDualBases.dualIdxEquiv hy w) *
          (basis ![y]).repr s (ComponentIdx.single.symm w)
```

**`TensorSpecies.Tensor.toMatrix₂_toLinearMap₂`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/RankTwo.lean#L109).

> On basis vectors, the bilinear map gives `M(e_μ, e_ν) = M_{μν}`, so its matrix is the component
> matrix `(M_{μν})`.

```lean
lemma toMatrix₂_toLinearMap₂ [HasContrDualBases S] {x y : C} {cM : Fin 2 → C}
    (hx : S.τ x = cM 0) (hy : S.τ y = cM 1) (M : Tensor S cM) :
    LinearMap.toMatrix₂
      ((basis ![x]).reindex (ComponentIdx.single.trans (HasContrDualBases.dualIdxEquiv hx)))
      ((basis ![y]).reindex (ComponentIdx.single.trans (HasContrDualBases.dualIdxEquiv hy)))
      (toLinearMap₂ x y M hx hy) = toMatrix M
```

## B. Contracting two rank-two tensors

**`TensorSpecies.Tensor.contractInnerT`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/RankTwo.lean#L127).

> The contraction `A_{μν} B^{νρ}` of the second index of `A` with the first index of `B`, whose
> colours are dual by `h`. The result has the indices `μ` and `ρ`, in that order.

```lean
noncomputable def contractInnerT {cs ds : Fin 2 → C} (h : S.τ (cs 1) = ds 0) :
    Tensor S cs →ₗ[k] Tensor S ds →ₗ[k] Tensor S ![cs 0, ds 1]
```

**`TensorSpecies.Tensor.contractInnerT_apply`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/RankTwo.lean#L134).

> `contractInnerT` is `crossToEnd` of the last index of `A` with the first index of `B`, with the
> colours of the result renamed to `![cs 0, ds 1]`.

```lean
lemma contractInnerT_apply {cs ds : Fin 2 → C} (h : S.τ (cs 1) = ds 0) (a : Tensor S cs)
    (b : Tensor S ds) :
    contractInnerT h a b = permT id (IsReindexing.on_id.mpr fun j => by fin_cases j <;> rfl)
      (crossToEnd (Fin.last 1) (0 : Fin 2) h a b)
```

**`TensorSpecies.Tensor.crossToEnd_eq_permT_contractInnerT`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/RankTwo.lean#L142).

> `crossToEnd` of the last index of `A` with the first index of `B` is `contractInnerT` with its
> colours renamed. This is `contractInnerT_apply` read from right to left.

```lean
lemma crossToEnd_eq_permT_contractInnerT {cs ds : Fin 2 → C} (h : S.τ (cs 1) = ds 0)
    (a : Tensor S cs) (b : Tensor S ds) :
    crossToEnd (Fin.last 1) (0 : Fin 2) h a b =
      permT id (IsReindexing.on_id.mpr fun j => by fin_cases j <;> rfl) (contractInnerT h a b)
```

**`TensorSpecies.Tensor.toMatrix_contractInnerT`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/RankTwo.lean#L152).

> The matrix of `A_{μν} B^{νρ}` is the matrix product of `(A_{μν})` and `(B^{νρ})`, with the
> labels of `ν` in `B` matched to those in `A` by `dualIdxEquiv`. This is `toMatrix_crossToEnd_pair`
> at general colour lists.

```lean
lemma toMatrix_contractInnerT [HasContrDualBases S] {cs ds : Fin 2 → C} (h : S.τ (cs 1) = ds 0)
    (a : Tensor S cs) (b : Tensor S ds) :
    toMatrix (contractInnerT h a b) =
      toMatrix a * (toMatrix b).submatrix (HasContrDualBases.dualIdxEquiv h) id
```

**`TensorSpecies.Tensor.contractInnerT_right_injective`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/RankTwo.lean#L166).

> If the matrix `(M_{μν})`, made square by the label bijection `e`, is invertible, then
> `t ↦ M_{μν} t^{νρ}` is injective.

```lean
lemma contractInnerT_right_injective [HasContrDualBases S] {cs ds : Fin 2 → C}
    (h : S.τ (cs 1) = ds 0) (e : basisIdx (cs 0) ≃ basisIdx (cs 1)) (M : Tensor S cs)
    (hM : IsUnit ((toMatrix M).submatrix id e).det) :
    Function.Injective (contractInnerT h M)
```

**`TensorSpecies.Tensor.contractInnerT_equivariant`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/RankTwo.lean#L184).

> `contractInnerT` commutes with the action of `G`. For a Lorentz transformation `Λ`,
> `(Λ A)_{μν} (Λ B)^{νρ} = Λ (A_{μν} B^{νρ})`.

```lean
lemma contractInnerT_equivariant {cs ds : Fin 2 → C} (h : S.τ (cs 1) = ds 0) (g : G)
    (a : Tensor S cs) (b : Tensor S ds) :
    contractInnerT h (g • a) (g • b) = g • contractInnerT h a b
```

## Depends on

- [Component indices for one-index tensors](componentidx-single.md)
- [Result-to-slot contraction against a rank-2 tensor](contraction-crosstoslot.md)

## Sources

- [Physlib/Relativity/Tensors/Contraction/RankTwo.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/RankTwo.lean)
