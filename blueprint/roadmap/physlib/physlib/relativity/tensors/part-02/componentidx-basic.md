---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.ComponentIdx, TensorSpecies.Tensor.ComponentIdx.congr_right, TensorSpecies.Tensor.ComponentIdx.cast
statement: formalized
proof: formalized
---

# Component indices

The module `Physlib.Relativity.Tensors.ComponentIdx.Basic`, [Physlib/Relativity/Tensors/ComponentIdx/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Basic.lean): 3 declarations, 2 with a docstring.

## i. Overview

> For a tensor species `S` and a list of colors `c : Fin n → C`, `ComponentIdx S c`
> is the type of choices of a basis index for every color in `c`. For example, for a
> tensor with colors `![.up, .down]`, an element of `ComponentIdx ![.up, .down]`
> records one contravariant component index and one covariant component index.
>
> This file contains the basic definition and congruence/cast API. Operations on
> component indices induced by tensor products and contractions live in sibling files.

## ii. Key results

> - `TensorSpecies.Tensor.ComponentIdx` is the type of component indices for a tensor
>   with a given list of colors.
> - `TensorSpecies.Tensor.ComponentIdx.congr_right` relates entries whose positions are equal.
> - `TensorSpecies.Tensor.ComponentIdx.cast` casts component indices along equivalent color maps.

## iv. References

> * None.

## A. Basic definitions

**`TensorSpecies.Tensor.ComponentIdx`**, an abbrev, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Basic.lean#L64).

> Given a list of indices `c : Fin n → C`, the type `ComponentIdx c` is the type of
> component indices of a tensor with those colors. For instance, if `c = ![.up, .down]`,
> then an element of `ComponentIdx c` specifies one basis index for `.up` and one for
> `.down`.

```lean
abbrev ComponentIdx {n : ℕ} {S : TensorSpecies k C G V basisIdx rep b}
    (c : Fin n → C) : Type
```

**`TensorSpecies.Tensor.ComponentIdx.congr_right`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Basic.lean#L68).

```lean
lemma ComponentIdx.congr_right {n : ℕ} {c : Fin n → C} (b : ComponentIdx (S := S) c)
    (i j : Fin n) (h : i = j) : b i = basisIdxCongr (by simp [h]) (b j)
```

**`TensorSpecies.Tensor.ComponentIdx.cast`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Basic.lean#L74).

> Casting of a `ComponentIdx` through equivalent color maps.

```lean
def ComponentIdx.cast {n m : ℕ} {c : Fin n → C} {cm : Fin m → C}
    (h : n = m) (hc : c = cm ∘ Fin.cast h) (b : ComponentIdx (S := S) c) :
    ComponentIdx (S := S) cm
```

## Depends on

- [Tensor species](../part-04/tensorspecies-basic.md)

## Sources

- [Physlib/Relativity/Tensors/ComponentIdx/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Basic.lean)
