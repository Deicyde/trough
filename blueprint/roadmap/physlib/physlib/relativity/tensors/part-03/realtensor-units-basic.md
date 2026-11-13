---
declaration: module
origin: cited
lean: realLorentzTensor.unitTensor_repr_apply
statement: formalized
proof: formalized
---

# Unit tensors for real Lorentz tensors

The module `Physlib.Relativity.Tensors.RealTensor.Units.Basic`, [Physlib/Relativity/Tensors/RealTensor/Units/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Basic.lean): 1 declaration, 1 with a docstring.

## i. Overview

> This file computes the unit tensors of `realLorentzTensor` in the standard covariant and
> contravariant bases.

## ii. Key results

> - `realLorentzTensor.unitTensor_repr_apply` identifies the standard-basis components of either
>   real Lorentz unit tensor with the Kronecker delta.

## iv. References

> * None.

## A. Basis components

**`realLorentzTensor.unitTensor_repr_apply`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Basic.lean#L51).

> In the standard contravariant and covariant bases, either real Lorentz unit tensor has
> Kronecker-delta components.

```lean
lemma unitTensor_repr_apply {d : ℕ} (c : Color)
    (φ : ComponentIdx (S := realLorentzTensor d) ![(realLorentzTensor d).τ c, c]) :
    (Tensor.basis _).repr (unitTensor (S := realLorentzTensor d) c) φ =
      if φ 0 = φ 1 then 1 else 0
```

## Depends on

- [Physlib.Relativity.Tensors.RealTensor.Basic](realtensor-basic.md)
- [The unit tensors](../part-01/unittensor.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Units/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Units/Basic.lean)
