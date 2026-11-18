---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.ComponentIdx.pair, TensorSpecies.Tensor.ComponentIdx.pair_apply, TensorSpecies.Tensor.ComponentIdx.pair_symm_apply_zero, TensorSpecies.Tensor.ComponentIdx.pair_symm_apply_one
statement: formalized
proof: formalized
---

# Component indices for two-index tensors

The module `Physlib.Relativity.Tensors.ComponentIdx.Pair`, [Physlib/Relativity/Tensors/ComponentIdx/Pair.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Pair.lean): 4 declarations, 1 with a docstring.

> Component indices of two-index tensors as pairs of basis indices.

## i. Overview

> This file defines the equivalence between component indices for two colors and pairs of basis
> indices of those colors.

## ii. Key results

> - `TensorSpecies.Tensor.ComponentIdx.pair` is the equivalence between `ComponentIdx cs` and
>   `basisIdx (cs 0) × basisIdx (cs 1)`.

## iv. References

> There are no known references for the material in this module.

## A. The two-index equivalence

**`TensorSpecies.Tensor.ComponentIdx.pair`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Pair.lean#L56).

> The equivalence between component indices for two colors and pairs of basis indices of
> those colors.

```lean
def ComponentIdx.pair {cs : Fin 2 → C} :
    ComponentIdx (S := S) cs ≃ basisIdx (cs 0) × basisIdx (cs 1)
```

**`TensorSpecies.Tensor.ComponentIdx.pair_apply`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Pair.lean#L60).

```lean
lemma ComponentIdx.pair_apply {cs : Fin 2 → C} (b : ComponentIdx (S := S) cs) :
    ComponentIdx.pair (S := S) b = (b 0, b 1)
```

**`TensorSpecies.Tensor.ComponentIdx.pair_symm_apply_zero`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Pair.lean#L64).

```lean
lemma ComponentIdx.pair_symm_apply_zero {cs : Fin 2 → C}
    (x : basisIdx (cs 0) × basisIdx (cs 1)) :
    (ComponentIdx.pair (S := S) (cs := cs)).symm x 0 = x.1
```

**`TensorSpecies.Tensor.ComponentIdx.pair_symm_apply_one`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Pair.lean#L69).

```lean
lemma ComponentIdx.pair_symm_apply_one {cs : Fin 2 → C}
    (x : basisIdx (cs 0) × basisIdx (cs 1)) :
    (ComponentIdx.pair (S := S) (cs := cs)).symm x 1 = x.2
```

## Depends on

- [Component indices](componentidx-basic.md)

## Sources

- [Physlib/Relativity/Tensors/ComponentIdx/Pair.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Pair.lean)
