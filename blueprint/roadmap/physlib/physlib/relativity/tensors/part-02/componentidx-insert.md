---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.ComponentIdx.insert, TensorSpecies.Tensor.ComponentIdx.insert_apply_self, TensorSpecies.Tensor.ComponentIdx.insert_apply_succAbove
statement: formalized
proof: formalized
---

# Component indices split at a single slot

The module `Physlib.Relativity.Tensors.ComponentIdx.Insert`, [Physlib/Relativity/Tensors/ComponentIdx/Insert.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Insert.lean): 3 declarations, 1 with a docstring.

> Component-index insertion and evaluation at a distinguished slot.

## i. Overview

> `ComponentIdx c` is `∀ j, basisIdx (c j)`, so singling out one slot `i` splits a component index
> into the label there and a component index for the remaining colours `c ∘ i.succAbove`. That is
> mathlib's `Fin.insertNthEquiv` read at the family `fun j => basisIdx (c j)`, and it carries no
> transports of its own.
>
> This is the one-slot counterpart of the two-slot `DropPairSection.ofFinEquiv`, which singles out
> the pair a contraction consumes, and of `ComponentIdx.prod`, which splits a concatenated colour
> list into its two halves. Where those two are shaped by the operation that produced the colour
> list, this one is shaped by a slot the caller names, which is what a general-rank component formula
> needs: an operation acting at slot `i` leaves the other slots alone, and the formula should say so
> at every rank rather than at the rank where the colour list happens to be a literal.

## ii. Key results

> - `TensorSpecies.Tensor.ComponentIdx.insert` : the equivalence splitting a component index at a
>     named slot.
> - `TensorSpecies.Tensor.ComponentIdx.insert_apply_self` and
>     `TensorSpecies.Tensor.ComponentIdx.insert_apply_succAbove` : the two directions, slotwise.

## iv. References

> There are no known references for the material in this module.

## A. The single-slot equivalence

**`TensorSpecies.Tensor.ComponentIdx.insert`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Insert.lean#L70).

> Splitting a component index at a named slot: the label at slot `i`, together with a component
> index for the colours of the remaining slots. The dependent counterpart of `Fin.cons`, and the
> single-slot analogue of the two-slot `DropPairSection.ofFinEquiv`.

```lean
def insert {n : ℕ} {c : Fin (n + 1) → C} (i : Fin (n + 1)) :
    basisIdx (c i) × ComponentIdx (S := S) (c ∘ i.succAbove) ≃ ComponentIdx (S := S) c
```

**`TensorSpecies.Tensor.ComponentIdx.insert_apply_self`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Insert.lean#L75).

```lean
lemma insert_apply_self {n : ℕ} {c : Fin (n + 1) → C} (i : Fin (n + 1))
    (x : basisIdx (c i) × ComponentIdx (S := S) (c ∘ i.succAbove)) :
    insert (S := S) i x i = x.1
```

**`TensorSpecies.Tensor.ComponentIdx.insert_apply_succAbove`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Insert.lean#L81).

```lean
lemma insert_apply_succAbove {n : ℕ} {c : Fin (n + 1) → C} (i : Fin (n + 1))
    (x : basisIdx (c i) × ComponentIdx (S := S) (c ∘ i.succAbove)) (m : Fin n) :
    insert (S := S) i x (i.succAbove m) = x.2 m
```

## Depends on

- [Component indices](componentidx-basic.md)

## Sources

- [Physlib/Relativity/Tensors/ComponentIdx/Insert.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Insert.lean)
