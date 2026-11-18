---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.contrT_decide, TensorSpecies.Tensor.contrT, TensorSpecies.Tensor.contrT_congr, TensorSpecies.Tensor.contrT_pure, TensorSpecies.Tensor.contrT_equivariant, TensorSpecies.Tensor.contrT_permT, TensorSpecies.Tensor.contrT_symm, TensorSpecies.Tensor.contrT_comm
statement: formalized
proof: formalized
---

# Contractions on tensors

The module `Physlib.Relativity.Tensors.Contraction.Basic`, [Physlib/Relativity/Tensors/Contraction/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basic.lean): 8 declarations, 1 with a docstring.

## i. Overview

> This file defines tensor contraction for an arbitrary `TensorSpecies`.
>
> The colors of a tensor record the type of each index. A pair of positions can be
> contracted when their colors are dual, expressed by a proof
> `S.τ (c i) = c j`, where `S.τ` is the color involution in the tensor species.
> For a tensor with colors `c : Fin (n + 1 + 1) → C`, contraction at positions
> `i` and `j` produces a tensor with two fewer indices and colors
> `c ∘ Fin.succSuccAbove i j`.
>
> The construction is first made on pure tensors in
> `Physlib.Relativity.Tensors.Contraction.Pure`. There, `Pure.dropPair` removes the
> two contracted factors from the remaining pure tensor, `Pure.contrPCoeff`
> computes the scalar contraction of the two removed factors using `S.contr`, and
> `Pure.contrP` multiplies that scalar by the dropped tensor. This file extends the
> operation linearly to arbitrary tensors via `contrT`.

## ii. Key results

> - `TensorSpecies.Tensor.contrT` is the linear contraction map on tensors.
> - `TensorSpecies.Tensor.contrT_pure` identifies `contrT` on pure tensors with
>   `Pure.contrP`.
> - `TensorSpecies.Tensor.contrT_equivariant` says contraction commutes with the
>   symmetry-group action.
> - `TensorSpecies.Tensor.contrT_permT`, `TensorSpecies.Tensor.contrT_symm`, and
>   `TensorSpecies.Tensor.contrT_comm` describe the interaction of contraction with
>   reindexing, swapping the contracted pair, and performing two contractions.

## iii. Related files

> - `Physlib.Relativity.Tensors.Contraction.SuccSuccAbove` contains the finite-index
>   maps used to drop two positions.
> - `Physlib.Relativity.Tensors.Contraction.Pure` defines `Pure.dropPair`,
>   `Pure.contrPCoeff`, `Pure.contrP`, and the multilinear map used to define
>   `contrT`.
> - `Physlib.Relativity.Tensors.Contraction.Products` proves compatibility between
>   contractions and tensor products.

## v. References

> There are no known references for the material in this module.

## A. Tensor contraction

**`TensorSpecies.Tensor.contrT_decide`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basic.lean#L83).

```lean
lemma contrT_decide {n : ℕ} {c : Fin (n + 1 + 1) → C} {i j : Fin (n + 1 + 1)}
    (hx : S.τ (c i) = c j) (hij : i ≠ j := by decide) :
    i ≠ j ∧ S.τ (c i) = c j
```

**`TensorSpecies.Tensor.contrT`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basic.lean#L92).

> For `c : Fin (n + 1 + 1) → C`, `i j : Fin (n + 1 + 1)` with dual color, and a tensor
> `t : Tensor S c`, `contrT i j _ t` is the tensor
> formed by contracting the `i`th index of `t`
> with the `j`th index.

```lean
noncomputable def contrT (n : ℕ) {c : Fin (n + 1 + 1) → C} (i j : Fin (n + 1 + 1))
      (hij : i ≠ j ∧ S.τ (c i) = c j) :
    Tensor S c →ₗ[k] Tensor S (c ∘ succSuccAbove i j)
```

**`TensorSpecies.Tensor.contrT_congr`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basic.lean#L97).

```lean
lemma contrT_congr {n : ℕ} {c : Fin (n + 1 + 1) → C}
    {i j : Fin (n + 1 + 1)} {hij : i ≠ j ∧ S.τ (c i) = c j}
    (i' j' : Fin (n + 1 + 1)) (t : S.Tensor c)
    (hii' : i = i' := by decide)
    (hjj' : j = j' := by decide) :
    contrT n i j hij t = permT id (And.intro (Function.bijective_id) (by subst hii' hjj'; simp))
      (contrT n i' j' (by subst hii' hjj'; exact hij) t)
```

**`TensorSpecies.Tensor.contrT_pure`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basic.lean#L108).

```lean
lemma contrT_pure {n : ℕ} {c : Fin (n + 1 + 1) → C} (i j : Fin (n + 1 + 1))
    (hij : i ≠ j ∧ S.τ (c i) = c j) (p : Pure S c) :
    contrT n i j hij p.toTensor = p.contrP i j hij
```

**`TensorSpecies.Tensor.contrT_equivariant`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basic.lean#L116).

```lean
lemma contrT_equivariant {n : ℕ} {c : Fin (n + 1 + 1) → C}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j ∧ S.τ (c i) = c j) (g : G)
    (t : Tensor S c) :
    contrT n i j hij (g • t) = g • contrT n i j hij t
```

**`TensorSpecies.Tensor.contrT_permT`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basic.lean#L134).

```lean
lemma contrT_permT {n n1 : ℕ} {c : Fin (n + 1 + 1) → C}
    {c1 : Fin (n1 + 1 + 1) → C}
    (i j : Fin (n1 + 1 + 1)) (hij : i ≠ j ∧ S.τ (c1 i) = (c1 j))
    (σ : Fin (n1 + 1 + 1) → Fin (n + 1 + 1))
    (hσ : IsReindexing c c1 σ) (t : Tensor S c) :
    contrT n1 i j hij (permT σ hσ t) = permT _ (hσ.succSuccAbove i j hij.1)
      (contrT n (σ i) (σ j) (by simp [hσ.2, hij, hσ.1.injective.eq_iff]) t)
```

**`TensorSpecies.Tensor.contrT_symm`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basic.lean#L157).

```lean
lemma contrT_symm {n : ℕ} {c : Fin (n + 1 + 1) → C}
    {i j : Fin (n + 1 + 1)} {hij : i ≠ j ∧ S.τ (c i) = c j} (t : Tensor S c) :
    contrT n i j hij t = permT id (by simp)
      (contrT n j i ⟨hij.1.symm, by simp [← hij.2]⟩ t)
```

**`TensorSpecies.Tensor.contrT_comm`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basic.lean#L173).

```lean
lemma contrT_comm {n : ℕ} {c : Fin (n + 1 + 1 + 1 + 1) → C}
    (i1 j1 : Fin (n + 1 + 1 + 1 + 1)) (i2 j2 : Fin (n + 1 + 1))
    (hij1 : i1 ≠ j1 ∧ S.τ (c i1) = (c j1))
    (hij2 : i2 ≠ j2 ∧ S.τ (c (succSuccAbove i1 j1 i2)) = (c (succSuccAbove i1 j1 j2)))
    (t : Tensor S c) :
    let i2' := (succSuccAbove i1 j1 i2);
    let j2' := (succSuccAbove i1 j1 j2);
    have hi2j2' : i2' ≠ j2' := by simp [i2', j2', hij2];
    let i1' := (predPredAbove i2' j2' hi2j2' i1 (by simp [i2', j2']));
    let j1' := (predPredAbove i2' j2' hi2j2' j1 (by simp [i2', j2']));
    contrT n i2 j2 hij2 (contrT (n + 1 + 1) i1 j1 hij1 t) =
    permT id (IsReindexing.succSuccAbove_comm i1 j1 i2 j2 hij1.left hij2.left)
      (contrT n i1' j1' (by simp [i1', j1', i2', j2', hij1])
      (contrT (n + 1 + 1) i2' j2' (by simp [i2', j2', hij2]) t))
```

## Depends on

- [Contractions on pure tensors](contraction-pure.md)

## Sources

- [Physlib/Relativity/Tensors/Contraction/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Basic.lean)
