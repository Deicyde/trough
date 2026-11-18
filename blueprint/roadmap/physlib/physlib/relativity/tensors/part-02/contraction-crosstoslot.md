---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.IsReindexing.crossToSlot_cycle, TensorSpecies.Tensor.crossToSlot, TensorSpecies.Tensor.crossToSlot_eq_crossToEnd, TensorSpecies.Tensor.crossToSlot_basis_repr_apply, TensorSpecies.Tensor.crossToSlotInv, TensorSpecies.Tensor.crossToSlot_permT_right_id, TensorSpecies.Tensor.crossToSlot_basis_repr_eq_sum_fin, TensorSpecies.Tensor.crossToSlot_basis_repr_eq_sum_dual
statement: formalized
proof: formalized
---

# Result-to-slot contraction against a rank-2 tensor

The module `Physlib.Relativity.Tensors.Contraction.CrossToSlot`, [Physlib/Relativity/Tensors/Contraction/CrossToSlot.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToSlot.lean): 9 declarations, 9 with a docstring.

## i. Overview

> `crossToEnd` deposits the surviving index of a slot contraction at the end of the survivor list.
> Raising and lowering a named index instead wants the replacement to stay *in place*: contracting
> slot `i` of `t` against a rank-2 tensor `M` (a metric, the unit tensor) should return `t` with only
> slot `i`'s color changed, `T^{μ}{}_{νρ} ↦ T_{μνρ}`. `crossToSlot i j hc M` is that operation, and
> `crossToSlot_eq_crossToEnd` is the one place the two conventions meet.
>
> This module stays at the `CommRing` altitude of `crossToEnd`; the `RCLike` round trips built on the
> operation live with the unit-tensor collapse theory in
> `Physlib.Relativity.Tensors.Contraction.UnitTensorContraction`.

## ii. Key results

> - `TensorSpecies.Tensor.crossToSlot` : contract slot `i` against slot `j` of a rank-2 tensor and
>     rotate the survivor back into position `i`; raising and lowering a named index.
> - `TensorSpecies.Tensor.crossToSlot_eq_crossToEnd` : the bridge to the result-to-end convention.
> - `TensorSpecies.Tensor.crossToSlot_basis_repr_apply` : the component bridge from result-to-slot
>     to result-to-end contraction.
> - `TensorSpecies.Tensor.crossToSlotInv` : the returning half of a round trip, the contraction
>     against the second factor with the round trip's color cast absorbed.
> - `TensorSpecies.Tensor.crossToSlot_basis_repr_eq_sum_fin` : the component formula at arbitrary
>     rank and slot for any species, the contraction of the two contracted basis vectors left as an
>     opaque coefficient.
> - `TensorSpecies.Tensor.crossToSlot_basis_repr_eq_sum_dual` : the same formula for a species with
>     contraction-dual bases, the δ collapsing the two sums into one.
> - `TensorSpecies.Tensor.crossToSlot_permT_right_id` : an identity reindexing of the rank-2 tensor
>     passes through the contraction.
> - `TensorSpecies.Tensor.crossToSlot_equivariant` : the contraction commutes with the `G`-action.

## iv. References

> * None.

## A. The result-to-slot contraction

**`TensorSpecies.Tensor.IsReindexing.crossToSlot_cycle`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToSlot.lean#L73).

> The survivor color of `crossToEnd i j` against a rank-2 tensor of color `cM` is `c` with
> slot `i` replaced by the surviving color `cM (j.succAbove 0)`, once the survivors are rotated
> back by the inverse of the cycle `[i, last]`.

```lean
lemma IsReindexing.crossToSlot_cycle {nA : ℕ} {c : Fin (nA + 1) → C} {cM : Fin 2 → C}
    (i : Fin (nA + 1)) (j : Fin 2) :
    IsReindexing
      (Fin.append (c ∘ i.succAbove) (cM ∘ j.succAbove))
      (Function.update c i (cM (j.succAbove 0)))
      ⇑(Fin.cycleIcc i (Fin.last nA)).symm
```

**`TensorSpecies.Tensor.crossToSlot`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToSlot.lean#L97).

> Contract slot `i` of `t` against slot `j` of the rank-2 tensor `M`, whose `j`-slot color must
> equal the dual color `τ (c i)` (propositionally, via `hc`), and rotate `M`'s surviving slot back
> into position `i`. The result is `t` with slot `i` relabelled to `M`'s surviving color.
>
> This is raising and lowering a named index; the metric case is `j = 0`,
> `M = metricTensor (τ (c i))`. Because `hc` is propositional, a rank-2 tensor whose slot color
> matches only up to an equality enters directly, with no transport.

```lean
noncomputable def crossToSlot {nA : ℕ} {c : Fin (nA + 1) → C} {cM : Fin 2 → C}
    (i : Fin (nA + 1)) (j : Fin 2) (hc : S.τ (c i) = cM j) (M : S.Tensor cM) :
    S.Tensor c →ₗ[k] S.Tensor (Function.update c i (cM (j.succAbove 0)))
```

**`TensorSpecies.Tensor.crossToSlot_eq_crossToEnd`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToSlot.lean#L105).

> The bridge between the two conventions: `crossToSlot i j hc M t` is `crossToEnd i j hc t M`
> with the survivor rotated from the last slot back to slot `i` by the inverse cycle.

```lean
lemma crossToSlot_eq_crossToEnd {nA : ℕ} {c : Fin (nA + 1) → C} {cM : Fin 2 → C}
    (i : Fin (nA + 1)) (j : Fin 2) (hc : S.τ (c i) = cM j) (M : S.Tensor cM) (t : S.Tensor c) :
    crossToSlot i j hc M t =
      permT ⇑(Fin.cycleIcc i (Fin.last nA)).symm (IsReindexing.crossToSlot_cycle i j)
        (crossToEnd i j hc t M)
```

**`TensorSpecies.Tensor.crossToSlot_basis_repr_apply`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToSlot.lean#L113).

> A component of `crossToSlot` is the corresponding component of `crossToEnd`, with the
> surviving indices rotated back into the contracted slot.

```lean
lemma crossToSlot_basis_repr_apply {nA : ℕ} {c : Fin (nA + 1) → C} {cM : Fin 2 → C}
    (i : Fin (nA + 1)) (j : Fin 2) (hc : S.τ (c i) = cM j) (M : Tensor S cM)
    (t : Tensor S c)
    (φ : ComponentIdx (S := S) (Function.update c i (cM (j.succAbove 0)))) :
    (basis _).repr (crossToSlot i j hc M t) φ =
      (basis _).repr (crossToEnd i j hc t M) (fun m =>
        basisIdxCongr ((IsReindexing.crossToSlot_cycle i j).inv_perserve_color m)
          (φ ((IsReindexing.crossToSlot_cycle i j).inv
            ⇑(Fin.cycleIcc i (Fin.last nA)).symm m)))
```

**`TensorSpecies.Tensor.crossToSlotInv`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToSlot.lean#L126).

> `crossToSlot` of slot `i` with the first index of `M'`, followed by renaming slot `i` back to
> its original colour `c i` (`he`).

```lean
noncomputable def crossToSlotInv {nA : ℕ} {c : Fin (nA + 1) → C} {d : C} {ds : Fin 2 → C}
    (i : Fin (nA + 1)) (he : c i = ds 1) (hb : S.τ d = ds 0) (M' : S.Tensor ds) :
    S.Tensor (Function.update c i d) →ₗ[k] S.Tensor c
```

**`TensorSpecies.Tensor.crossToSlot_permT_right_id`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToSlot.lean#L137).

> An identity reindexing of the rank-2 tensor becomes the corresponding identity reindexing of
> the contracted output: the `crossToSlot`-level case of `crossToEnd_permT_right` where the rank-2
> tensor's colors are only propositionally recast.

```lean
lemma crossToSlot_permT_right_id {nA : ℕ} {c : Fin (nA + 1) → C} {cM cM' : Fin 2 → C}
    (i : Fin (nA + 1)) (j : Fin 2) (hc : S.τ (c i) = cM' j)
    (M : Tensor S cM) (hM : IsReindexing cM cM' (id : Fin 2 → Fin 2)) (t : Tensor S c) :
    crossToSlot i j hc (permT (id : Fin 2 → Fin 2) hM M) t =
      permT (id : Fin (nA + 1) → Fin (nA + 1))
        (IsReindexing.on_id.mpr (fun a => by
          by_cases ha : a = i
          · subst ha
            simpa using hM.2 (j.succAbove 0)
          · simp [Function.update_of_ne ha]))
        (crossToSlot i j (hc.trans (hM.2 j).symm) M t)
```

**`TensorSpecies.Tensor.crossToSlot_basis_repr_eq_sum_fin`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToSlot.lean#L163).

> The component formula for a cross contraction into an arbitrary slot, for a species whose bases
> are not assumed adapted to the contraction: each contracted label is summed over its own slot and
> the contraction of the two basis vectors remains an opaque coefficient. Rotating the survivor back
> to its slot only transports the surviving labels, so this is `crossToEnd_basis_repr_eq_sum_fin` read
> through the cycle.

```lean
lemma crossToSlot_basis_repr_eq_sum_fin {nA : ℕ} {c : Fin (nA + 1) → C}
    {cM : Fin 2 → C} (i : Fin (nA + 1)) (j : Fin 2) (hc : S.τ (c i) = cM j)
    (M : S.Tensor cM) (t : S.Tensor c)
    (φ : ComponentIdx (S := S) (Function.update c i (cM (j.succAbove 0)))) :
    (basis (Function.update c i (cM (j.succAbove 0)))).repr
        (crossToSlot i j hc M t) φ =
      ∑ x₁ : basisIdx (c i), ∑ x₂ : basisIdx (cM j),
        ((basis c).repr t (ComponentIdx.insert i
            (x₁, fun m => basisIdxCongr (by simp [Function.update_of_ne]) (φ (i.succAbove m)))) *
          (basis cM).repr M (ComponentIdx.insert j
            (x₂, fun m => basisIdxCongr (by fin_cases m; simp) (φ i)))) *
        S.contr (c i) (b (c i) x₁ ⊗ₜ[k]
          b (S.τ (c i)) (basisIdxCongr (by rw [hc]) x₂))
```

**`TensorSpecies.Tensor.crossToSlot_basis_repr_eq_sum_dual`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToSlot.lean#L208).

> The component formula for a cross contraction into an arbitrary slot, for a species with
> contraction-dual bases: the contraction coefficient is `δ` and one sum remains, the contracted label
> of `M` matched to that of `t` by `contrDualIdxEquiv`.

```lean
lemma crossToSlot_basis_repr_eq_sum_dual [HasContrDualBases S] {nA : ℕ} {c : Fin (nA + 1) → C}
    {cM : Fin 2 → C} (i : Fin (nA + 1)) (j : Fin 2) (hc : S.τ (c i) = cM j)
    (M : S.Tensor cM) (t : S.Tensor c)
    (φ : ComponentIdx (S := S) (Function.update c i (cM (j.succAbove 0)))) :
    (basis (Function.update c i (cM (j.succAbove 0)))).repr
        (crossToSlot i j hc M t) φ =
      ∑ x : basisIdx (c i),
        (basis c).repr t (ComponentIdx.insert i
          (x, fun m => basisIdxCongr (by simp [Function.update_of_ne]) (φ (i.succAbove m)))) *
        (basis cM).repr M (ComponentIdx.insert j
          (basisIdxCongr hc ((HasContrDualBases.contrDualIdxEquiv S (c i)).symm x),
            fun m => basisIdxCongr (by fin_cases m; simp) (φ i)))
```

**`TensorSpecies.Tensor.crossToSlot_equivariant`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToSlot.lean#L227).

> Cross contraction into a slot is `G`-equivariant, both constituents (`crossToEnd`, `permT`)
> being so.

```lean
lemma crossToSlot_equivariant {nA : ℕ} {c : Fin (nA + 1) → C} {cM : Fin 2 → C}
    (i : Fin (nA + 1)) (j : Fin 2) (hc : S.τ (c i) = cM j) (g : G)
    (M : Tensor S cM) (t : Tensor S c) :
    crossToSlot i j hc (g • M) (g • t) = g • crossToSlot i j hc M t
```

## Depends on

- [Cross contraction at named slots](contraction-crosstoend.md)

## Sources

- [Physlib/Relativity/Tensors/Contraction/CrossToSlot.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToSlot.lean)
