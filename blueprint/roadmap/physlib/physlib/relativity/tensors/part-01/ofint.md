---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.TensorInt, TensorSpecies.Tensor.TensorInt.toTensor, TensorSpecies.Tensor.TensorInt.basis_repr_apply, TensorSpecies.Tensor.basis_eq_tensorInt
statement: formalized
proof: formalized
---

# Basis for tensors in a tensor species

The module `Physlib.Relativity.Tensors.OfInt`, [Physlib/Relativity/Tensors/OfInt.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/OfInt.lean): 4 declarations, 2 with a docstring.

**`TensorSpecies.Tensor.TensorInt`**, an abbrev, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/OfInt.lean#L30).

> A tensor with integer components with respect to the basis.

```lean
abbrev TensorInt {n : ℕ} (c : Fin n → C)
```

**`TensorSpecies.Tensor.TensorInt.toTensor`**, a def, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/OfInt.lean#L37).

> The element of `S.Tensor c` created from a tensor `TensorInt S c`.

```lean
noncomputable def toTensor {n : ℕ} {c : Fin n → C} (f : TensorInt S c) :
    S.Tensor c
```

**`TensorSpecies.Tensor.TensorInt.basis_repr_apply`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/OfInt.lean#L42).

```lean
lemma basis_repr_apply {n : ℕ} {c : Fin n → C}
    (f : TensorInt S c) (b : ComponentIdx c) :
    (Tensor.basis c).repr (toTensor f) b = Int.cast (f b)
```

**`TensorSpecies.Tensor.basis_eq_tensorInt`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/OfInt.lean#L50).

```lean
lemma basis_eq_tensorInt {n : ℕ} {c : Fin n → C}
    (b : ComponentIdx c) :
    Tensor.basis c b = TensorInt.toTensor (S := S) (fun b' => if b = b' then 1 else 0)
```

## Depends on

- [Tensors](basic.md)

## Sources

- [Physlib/Relativity/Tensors/OfInt.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/OfInt.lean)
