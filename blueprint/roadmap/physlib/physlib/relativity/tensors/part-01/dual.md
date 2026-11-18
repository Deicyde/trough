---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.toDualMapAtIndex, TensorSpecies.Tensor.contractInnerT_dual_metricTensor_metricTensor, TensorSpecies.Tensor.contractInnerT_metricTensor_metricTensor_eq_dual_unit, TensorSpecies.Tensor.toDualMapAtIndex_toDualMapAtIndex, TensorSpecies.Tensor.fromDualMapAtIndex, TensorSpecies.Tensor.fromDualMapAtIndex_toDualMapAtIndex, TensorSpecies.Tensor.toDualMapAtIndex_fromDualMapAtIndex, TensorSpecies.Tensor.toDualMapAtIndex_equivariant
statement: formalized
proof: formalized
---

# Dual tensors

The module `Physlib.Relativity.Tensors.Dual`, [Physlib/Relativity/Tensors/Dual.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Dual.lean): 11 declarations, 7 with a docstring.

## i. Overview

> The metric tensor identifies a tensor with the one obtained by dualising the color of a single
> index: contracting slot `i` of `t` against `metricTensor (S.τ (c i))` returns a tensor of color
> `Function.update c i (S.τ (c i))`, leaving every other slot alone. This is the raising and lowering
> of a named index, `T^{μν} ↦ T_{μ}{}^{ν}`. `toDualMapAtIndex i` is that contraction, `crossToSlot`
> against the metric, at every rank and every named slot.
>
> A metric contracted against the metric at the dual color collapses to the unit tensor, in both
> orders. So the contraction back against `metricTensor (c i)`, `fromDualMapAtIndex i`, inverts it,
> and the two assemble into the linear equivalence `toDualAtIndex i`: the two color assignments
> carry the same information. Dualising the same index twice returns the original tensor, up to the
> reindexing of the colors.

## ii. Key results

> - `TensorSpecies.Tensor.toDualMapAtIndex` : dualise the color of the index `i` by contracting with
>     the metric tensor.
> - `TensorSpecies.Tensor.fromDualMapAtIndex` : the returning contraction, against the metric tensor
>     at `c i`.
> - `TensorSpecies.Tensor.toDualMapAtIndex_toDualMapAtIndex` : dualising the index `i` twice returns
>     the original tensor.
> - `TensorSpecies.Tensor.toDualMapAtIndex_equivariant` : dualising an index commutes with the
>     `G`-action.
> - `TensorSpecies.Tensor.toDualAtIndex` : raising and lowering the index `i` as a linear
>     equivalence.

## iv. References

> * None.

## A. Dualising a named index

**`TensorSpecies.Tensor.toDualMapAtIndex`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Dual.lean#L75).

> The linear map between `S.Tensor c` and `S.Tensor (Function.update c i (S.τ (c i)))`
> formed by contracting the index `i` with the metric tensor.

```lean
noncomputable def toDualMapAtIndex : {n : ℕ} → {c : Fin n → C} → (i : Fin n) →
    S.Tensor c →ₗ[k] S.Tensor (Function.update c i (S.τ (c i)))
```

## B. Contracting a metric against its dual

**`TensorSpecies.Tensor.contractInnerT_dual_metricTensor_metricTensor`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Dual.lean#L89).

> The metric at `τ c` contracted with the metric at `c` is the unit tensor at `c`,
> `η^{μν} η_{νρ} = δ^μ_ρ`.

```lean
lemma contractInnerT_dual_metricTensor_metricTensor {c : C} :
    contractInnerT (S.τ_τ_apply c) (metricTensor (S := S) (S.τ c)) (metricTensor (S := S) c) =
      permT (id : Fin 2 → Fin 2) (IsReindexing.unitTensor_of_tau_eq rfl)
        (unitTensor (S := S) c)
```

**`TensorSpecies.Tensor.contractInnerT_metricTensor_metricTensor_eq_dual_unit`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Dual.lean#L100).

> The metric at `c` contracted with the metric at `τ c` is the unit tensor at `τ c`,
> `η_{μν} η^{νρ} = δ_μ^ρ`.

```lean
lemma contractInnerT_metricTensor_metricTensor_eq_dual_unit {c : C} :
    contractInnerT rfl (metricTensor (S := S) c) (metricTensor (S := S) (S.τ c)) =
      permT (id : Fin 2 → Fin 2) (IsReindexing.unitTensor_of_tau_eq (S.τ_τ_apply c))
        (unitTensor (S := S) (S.τ c))
```

## C. Dualising twice

**`TensorSpecies.Tensor.toDualMapAtIndex_toDualMapAtIndex`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Dual.lean#L116).

> Dualising the index `i` twice returns the original tensor, up to the reindexing of the
> colors.

```lean
lemma toDualMapAtIndex_toDualMapAtIndex {n : ℕ} {c : Fin n → C}
    (i : Fin n) (t : S.Tensor c) :
    toDualMapAtIndex (S := S) i (toDualMapAtIndex (S := S) i t) =
      permT (id : Fin n → Fin n)
        (IsReindexing.update_update_of_eq i (by simp [τ_τ_apply])) t
```

## D. The returning contraction

**`TensorSpecies.Tensor.fromDualMapAtIndex`**, a def, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Dual.lean#L148).

> The linear map between `S.Tensor (Function.update c i (S.τ (c i)))` and `S.Tensor c`
> formed by contracting the index `i` with the metric tensor. It is the inverse of
> `toDualMapAtIndex`.

```lean
noncomputable def fromDualMapAtIndex : {n : ℕ} → {c : Fin n → C} → (i : Fin n) →
    S.Tensor (Function.update c i (S.τ (c i))) →ₗ[k] S.Tensor c
```

**`TensorSpecies.Tensor.fromDualMapAtIndex_toDualMapAtIndex`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Dual.lean#L154).

```lean
lemma fromDualMapAtIndex_toDualMapAtIndex {n : ℕ} {c : Fin n → C} (i : Fin n) (t : S.Tensor c) :
    fromDualMapAtIndex (S := S) i (toDualMapAtIndex (S := S) i t) = t
```

**`TensorSpecies.Tensor.toDualMapAtIndex_fromDualMapAtIndex`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Dual.lean#L164).

```lean
lemma toDualMapAtIndex_fromDualMapAtIndex {n : ℕ} {c : Fin n → C} (i : Fin n)
    (t : S.Tensor (Function.update c i (S.τ (c i)))) :
    toDualMapAtIndex (S := S) i (fromDualMapAtIndex (S := S) i t) = t
```

## E. Equivariance

**`TensorSpecies.Tensor.toDualMapAtIndex_equivariant`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Dual.lean#L183).

> Dualising the index `i` commutes with the action of `G`.

```lean
lemma toDualMapAtIndex_equivariant {n : ℕ} {c : Fin n → C} (i : Fin n) (g : G) (t : S.Tensor c) :
    toDualMapAtIndex (S := S) i (g • t) = g • toDualMapAtIndex (S := S) i t
```

## F. Raising and lowering as an equivalence

**`TensorSpecies.Tensor.toDualAtIndex`**, a def, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Dual.lean#L200).

> The linear equivalence between `S.Tensor c` and `S.Tensor (Function.update c i (S.τ (c i)))`
> formed by contracting the index `i` with the metric tensor.

```lean
noncomputable def toDualAtIndex : {n : ℕ} → {c : Fin n → C} → (i : Fin n) →
    S.Tensor c ≃ₗ[k] S.Tensor (Function.update c i (S.τ (c i)))
```

**`TensorSpecies.Tensor.toDualAtIndex_apply`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Dual.lean#L209).

```lean
lemma toDualAtIndex_apply {n : ℕ} {c : Fin n → C} (i : Fin n) (t : S.Tensor c) :
    toDualAtIndex (S := S) i t = toDualMapAtIndex (S := S) i t
```

**`TensorSpecies.Tensor.toDualAtIndex_symm_apply`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Dual.lean#L216).

```lean
lemma toDualAtIndex_symm_apply {n : ℕ} {c : Fin n → C} (i : Fin n)
    (t : S.Tensor (Function.update c i (S.τ (c i)))) :
    (toDualAtIndex (S := S) i).symm t = fromDualMapAtIndex (S := S) i t
```

## Depends on

- [Contraction against the unit tensor](../part-03/contraction-unittensorcontraction.md)
- [The metric tensors](metrictensor.md)

## Sources

- [Physlib/Relativity/Tensors/Dual.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Dual.lean)
