---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.ComponentIdx.single, TensorSpecies.Tensor.ComponentIdx.single_apply, TensorSpecies.Tensor.ComponentIdx.single_symm_apply
statement: formalized
proof: formalized
---

# Component indices for one-index tensors

The module `Physlib.Relativity.Tensors.ComponentIdx.Single`, [Physlib/Relativity/Tensors/ComponentIdx/Single.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Single.lean): 3 declarations, 1 with a docstring.

## i. Overview

> This file defines the canonical equivalence between component indices for a single
> color and the basis indices of that color.

## ii. Key results

> - `TensorSpecies.Tensor.ComponentIdx.single` is the equivalence between
>   `ComponentIdx ![c]` and `basisIdx c`.
> - `TensorSpecies.Tensor.ComponentIdx.single_apply` and
>   `TensorSpecies.Tensor.ComponentIdx.single_symm_apply` are simp lemmas for the two
>   directions of this equivalence.

## iv. References

> * None.

## A. Single-index equivalence

**`TensorSpecies.Tensor.ComponentIdx.single`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Single.lean#L56).

> The equivalence between component indices for a single color and the basis indices
> of that color.

```lean
def ComponentIdx.single {c : C} :
    ComponentIdx (S := S) ![c] ≃ basisIdx c
```

**`TensorSpecies.Tensor.ComponentIdx.single_apply`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Single.lean#L70).

```lean
lemma ComponentIdx.single_apply {c : C} (b : ComponentIdx (S := S) ![c]) :
    ComponentIdx.single (S := S) b = basisIdxCongr (by simp) (b 0)
```

**`TensorSpecies.Tensor.ComponentIdx.single_symm_apply`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Single.lean#L74).

```lean
lemma ComponentIdx.single_symm_apply {c : C} (b : basisIdx c) (i : Fin 1) :
    (ComponentIdx.single (S := S) (c := c)).symm b i = basisIdxCongr (by simp) b
```

## Depends on

- [Component indices](componentidx-basic.md)

## Sources

- [Physlib/Relativity/Tensors/ComponentIdx/Single.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Single.lean)
