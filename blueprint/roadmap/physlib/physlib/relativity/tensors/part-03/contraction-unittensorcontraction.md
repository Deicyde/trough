---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.crossToEnd_unitTensor, TensorSpecies.Tensor.crossToEnd_round_trip_of_unit_slot, TensorSpecies.Tensor.crossToSlot_raise_lower_round_trip, TensorSpecies.Tensor.crossToSlotInv_crossToSlot, TensorSpecies.Tensor.crossToSlot_crossToSlotInv, TensorSpecies.Tensor.crossToSlotEquiv, TensorSpecies.Tensor.contractInnerT_eq_unitTensor_comm
statement: formalized
proof: formalized
---

# Contraction against the unit tensor

The module `Physlib.Relativity.Tensors.Contraction.UnitTensorContraction`, [Physlib/Relativity/Tensors/Contraction/UnitTensorContraction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/UnitTensorContraction.lean): 7 declarations, 7 with a docstring; 3 private, not shown.

## i. Overview

> The unit tensor is the identity for slot contraction: contracting any slot of `t` against
> `unitTensor` for that slot's color returns `t`, the slot relabelled to the survivor tail. That is
> what collapses "raise then lower" to the identity, a metric contracted against its dual becoming
> the unit tensor and then contracting away.
>
> `crossToEnd_unitTensor` is proved by decomposing `t` along its last slot (`eq_sum_evalT`) and
> transporting to an arbitrary slot with the transposition `swap i (last)`. On it the round trip
> against a matched pair is assembled in both conventions, and a pair collapsing in *both* orders
> makes the two contractions mutually inverse, which `crossToSlotEquiv` bundles as a linear
> equivalence between the two color assignments.
>
> Since `unitTensor` is `RCLike`-valued, this material sits over an `[RCLike k]` variable block, apart
> from the `CommRing` `crossToEnd`/`crossToSlot` algebra.

## ii. Key results

> - `TensorSpecies.Tensor.crossToEnd_unitTensor` : the unit tensor is an identity for `crossToEnd`
>     at any named slot.
> - `TensorSpecies.Tensor.crossToEnd_round_trip_of_unit_slot` : two contractions against a pair that
>     collapses to the unit tensor return the original tensor, in result-to-end form.
> - `TensorSpecies.Tensor.crossToSlot_raise_lower_round_trip` : the round trip in result-to-slot
>     form, every color propositional.
> - `TensorSpecies.Tensor.crossToSlotEquiv` : raising and lowering a named index against a pair that
>     collapses in both orders, as a linear equivalence.
> - `TensorSpecies.Tensor.contractInnerT_eq_unitTensor_comm` : if the label sets of the two indices
>     of `M` are in bijection, `M_{μν} M'^{νρ} = δ_μ^ρ` implies `M'^{νρ} M_{ρσ} = δ^ν_σ`.

## iv. References

> * None.

## A. The unit tensor as a slot-contraction identity

> Contracting a named slot against `unitTensor` returns the tensor unchanged, the slot carried to the
> survivor tail by `move_last`.

**`TensorSpecies.Tensor.crossToEnd_unitTensor`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/UnitTensorContraction.lean#L163).

> Contracting slot `i` of `t1` against the unit tensor for that slot's color returns `t1`, the
> contracted slot relabelled by `move_last i`. The unit tensor acts as an identity for `crossToEnd`
> at any named slot.

```lean
lemma crossToEnd_unitTensor {nA : ℕ} {cA : Fin (nA + 1) → C} {c : C}
    (i : Fin (nA + 1)) (hc : cA i = c) (t1 : Tensor S cA) :
    crossToEnd i (0 : Fin 2) (by simp [hc] : S.τ (cA i) = ![S.τ c, c] 0) t1 (unitTensor c) =
      permT (Fin.append i.succAbove (fun _ : Fin 1 => i)) (IsReindexing.move_last i hc) t1
```

## B. Round trips against a matched pair

> If `M_{μν} M'^{νρ} = δ_μ^ρ`, contracting an index of a tensor `t` with `M` and then with `M'` gives
> back `t`. The metric and its inverse are such a pair.

**`TensorSpecies.Tensor.crossToEnd_round_trip_of_unit_slot`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/UnitTensorContraction.lean#L205).

> If `M₁_{μν} M₂^{νρ} = δ_μ^ρ`, contracting slot `i` of `t` with `M₁` and then with `M₂` gives
> back `t` with that slot moved to the end, because `crossToEnd` places the surviving index last.
> The last slot is a variable `j` with `hj : j = last nA`, so the lemma also applies where `j` is
> last only up to an equality.

```lean
lemma crossToEnd_round_trip_of_unit_slot {nA : ℕ} {c : Fin (nA + 1) → C} {d : C}
    (i j : Fin (nA + 1)) (hj : j = Fin.last nA)
    (M₁ : Tensor S ![S.τ (c i), d]) (M₂ : Tensor S ![S.τ d, c i])
    (hM : contractInnerT rfl M₁ M₂ =
      permT (id : Fin 2 → Fin 2) (IsReindexing.unitTensor_of_tau_eq rfl)
        (unitTensor (S := S) (c i)))
    (t : Tensor S c) :
    crossToEnd j (0 : Fin 2)
        (by subst hj
            rw [show (Fin.last nA : Fin (nA + 1)) = Fin.natAdd nA (0 : Fin 1) from
                  Fin.ext (by simp), Fin.append_right]; rfl)
        (crossToEnd i (0 : Fin 2) rfl t M₁) M₂ =
      permT (Fin.append i.succAbove (fun _ : Fin 1 => i))
        (by
          subst hj
          exact ⟨by
            rw [Fin.append_succAbove_const_eq_cycleIcc i]
            exact (Fin.cycleIcc i (Fin.last nA)).bijective,
          fun x => by
            refine Fin.addCases (fun a => ?_) (fun a => ?_) x
            · simp only [Function.comp_apply, Fin.append_left, Fin.succAbove_last,
                show (Fin.castSucc a : Fin (nA + 1)) = Fin.castAdd 1 a from rfl]
            · fin_cases a
              simp [Fin.append_right, Fin.succAbove_zero]⟩)
        t
```

**`TensorSpecies.Tensor.crossToSlot_raise_lower_round_trip`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/UnitTensorContraction.lean#L302).

> If `M_{μν} M'^{νρ} = δ_μ^ρ`, contracting slot `i` of `t` with `M` and then with `M'` gives back
> `t` in place, up to renaming the colour of slot `i`. The equalities `ha`, `hb` and `he` match
> slot `i` with the indices of `M` and `M'`, so `M` and `M'` can have any colour lists.

```lean
lemma crossToSlot_raise_lower_round_trip {nA : ℕ} {c : Fin (nA + 1) → C} {cs ds : Fin 2 → C}
    (i : Fin (nA + 1)) (he : c i = ds 1) (ha : S.τ (c i) = cs 0) (hb : S.τ (cs 1) = ds 0)
    (M : Tensor S cs) (M' : Tensor S ds)
    (hM : contractInnerT hb M M' =
      permT (id : Fin 2 → Fin 2)
        (IsReindexing.unitTensor_of_tau_eq ((congrArg S.τ he.symm).trans ha))
        (unitTensor (S := S) (ds 1)))
    (t : Tensor S c) :
    crossToSlot (S := S) i (0 : Fin 2)
        (by rw [Function.update_self]; exact hb : S.τ (Function.update c i (cs 1) i) = ds 0) M'
        (crossToSlot (S := S) i (0 : Fin 2) ha M t) =
      permT (id : Fin (nA + 1) → Fin (nA + 1)) (IsReindexing.update_update_of_eq i he) t
```

## C. Raising and lowering as an equivalence

> Both collapse orders are hypotheses here and each is used once: `M · M' = δ` gives one round trip
> by section B, `M' · M = δ` the other through injectivity of the lowering half. If the label sets of
> the two indices of `M` are in bijection, as for a metric, the second law follows from the first
> (section D).

**`TensorSpecies.Tensor.crossToSlotInv_crossToSlot`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/UnitTensorContraction.lean#L351).

> If `M_{μν} M'^{νρ} = δ_μ^ρ`, `crossToSlotInv` with `M'` undoes `crossToSlot` with `M`.

```lean
lemma crossToSlotInv_crossToSlot (t : Tensor S c) :
    crossToSlotInv i he hb M' (crossToSlot i (0 : Fin 2) ha M t) = t
```

**`TensorSpecies.Tensor.crossToSlot_crossToSlotInv`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/UnitTensorContraction.lean#L362).

> If also `M'^{νρ} M_{ρσ} = δ^ν_σ`, `crossToSlot` with `M` undoes `crossToSlotInv` with `M'`. The
> second law makes `crossToSlotInv` injective, so its left inverse is also a right inverse.

```lean
lemma crossToSlot_crossToSlotInv (t : Tensor S (Function.update c i (cs 1))) :
    crossToSlot i (0 : Fin 2) ha M (crossToSlotInv i he hb M' t) = t
```

**`TensorSpecies.Tensor.crossToSlotEquiv`**, a def, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/UnitTensorContraction.lean#L383).

> The linear equivalence `crossToSlot` with `M`, with inverse `crossToSlotInv` with `M'`, when
> `M_{μν} M'^{νρ} = δ_μ^ρ` and `M'^{νρ} M_{ρσ} = δ^ν_σ`. Slot `i` has colour `c i` on one side and
> the colour `cs 1` of the second index of `M` on the other. For the metric this lowers and raises
> an index with `η_{μν}` and `η^{νρ}`.

```lean
noncomputable def crossToSlotEquiv : Tensor S c ≃ₗ[k] Tensor S (Function.update c i (cs 1))
```

## D. One contraction law from the other

**`TensorSpecies.Tensor.contractInnerT_eq_unitTensor_comm`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/UnitTensorContraction.lean#L400).

> If the label sets of the two indices of `M` are in bijection, `M_{μν} M'^{νρ} = δ_μ^ρ` implies
> `M'^{νρ} M_{ρσ} = δ^ν_σ`. Without the bijection `e` this fails, since `A B = 1` does not imply
> `B A = 1` for rectangular matrices.

```lean
lemma contractInnerT_eq_unitTensor_comm [HasContrDualBases S] {cs ds : Fin 2 → C}
    (hb : S.τ (cs 1) = ds 0) (ha : S.τ (ds 1) = cs 0) (e : basisIdx (cs 0) ≃ basisIdx (cs 1))
    (M : Tensor S cs) (M' : Tensor S ds)
    (h : contractInnerT hb M M' =
      permT id (IsReindexing.unitTensor_of_tau_eq ha) (unitTensor (S := S) (ds 1))) :
    contractInnerT ha M' M =
      permT id (IsReindexing.unitTensor_of_tau_eq hb) (unitTensor (S := S) (cs 1))
```

## Depends on

- [The bilinear map and the product of rank-two tensors](../part-02/contraction-ranktwo.md)
- [The unit tensors](../part-01/unittensor.md)

## Proof depends on

- [Evaluation of tensor indices](../part-01/evaluation.md)

## Sources

- [Physlib/Relativity/Tensors/Contraction/UnitTensorContraction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/UnitTensorContraction.lean)
