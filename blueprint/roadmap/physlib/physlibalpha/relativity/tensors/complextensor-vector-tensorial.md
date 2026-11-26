---
declaration: module
origin: cited
lean: Lorentz.ComplexVector.tensorial, Lorentz.ComplexVector.toTensor_eq_fromSingleT, Lorentz.ComplexVector.toTensor_SL2CRep, Lorentz.ComplexVector.toTensor_basis
statement: formalized
proof: formalized
---

# Complex four-vectors as tensors

The module `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Vector.Tensorial`, [PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/Tensorial.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/Tensorial.lean): 4 declarations, 3 with a docstring.

> Complex four-vectors are the complex Lorentz tensors with one contravariant index.

## i. Overview

> A complex four-vector is a complex Lorentz tensor with a single index of colour `.up`, and
> `fromSingleT` is the linear equivalence between the two. It makes `Lorentz.ComplexVector` a
> tensorial type, so that tensor products of it with other tensorial types are tensorial through
> `TensorSpecies.Tensorial.prod`. The equivalence carries the action of `SL(2, ℂ)` on four-vectors to
> the action on tensors, and the basis vector `e_μ` to the basis tensor with the single component
> `μ` (A).

## ii. Key results

> - `Lorentz.ComplexVector.tensorial` : complex four-vectors are the tensors with one index `.up`.
> - `Lorentz.ComplexVector.toTensor_SL2CRep` : the equivalence intertwines the two actions.
> - `Lorentz.ComplexVector.toTensor_basis` : the basis vector `e_μ` is the basis tensor with
>   component `μ`.

## iv. References

> The tensorial class is in `Physlib.Relativity.Tensors.Tensorial`. The instance for real
> four-vectors is in `Physlib.Relativity.Tensors.RealTensor.Vector.Tensorial`.

## A. The tensorial instance

**`Lorentz.ComplexVector.tensorial`**, an instance, [line 56](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/Tensorial.lean#L56).

> Complex four-vectors are the complex Lorentz tensors with one index `.up`, through
> `fromSingleT`.

```lean
noncomputable instance tensorial : Tensorial complexLorentzTensor ![.up] ComplexVector
```

**`Lorentz.ComplexVector.toTensor_eq_fromSingleT`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/Tensorial.lean#L59).

```lean
lemma toTensor_eq_fromSingleT (v : ComplexVector) :
    toTensor v = fromSingleT (S := complexLorentzTensor) (c := .up) v
```

**`Lorentz.ComplexVector.toTensor_SL2CRep`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/Tensorial.lean#L64).

> The equivalence with the one-index tensors carries the action of `SL(2, ℂ)` on four-vectors to
> the action on tensors.

```lean
lemma toTensor_SL2CRep (g : SL(2,ℂ)) (v : ComplexVector) :
    toTensor (SL2CRep g v) = g • toTensor v
```

**`Lorentz.ComplexVector.toTensor_basis`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/Tensorial.lean#L69).

> The basis vector `e_μ` is the basis tensor with the single component `μ`.

```lean
lemma toTensor_basis (μ : Fin 1 ⊕ Fin 3) :
    toTensor (basis μ) = Tensor.basis (S := complexLorentzTensor) ![.up]
      (ComponentIdx.single.symm μ)
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](../../../physlib/relativity/tensors/part-01/complextensor-basic.md)

## Sources

- [PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/Tensorial.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/Tensorial.lean)
