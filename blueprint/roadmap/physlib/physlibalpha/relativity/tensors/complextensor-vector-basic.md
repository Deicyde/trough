---
declaration: module
origin: cited
lean: Lorentz.ComplexCoVector.SL2CRep_dual_dualBasis
statement: formalized
proof: formalized
---

# The dual of the complex covector representation

The module `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Vector.Basic`, [PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/Basic.lean): 1 declaration, 1 with a docstring.

> How dual complex covectors transform, on the dual basis.

## i. Overview

> A covector representation induces one on the dual space, and a classification of invariant
> tensors has to know how the dual basis transforms. For the complex covectors
> `Lorentz.ComplexCoVector` the answer is that dual covectors transform contravariantly: the dual
> basis vector `e^μ` goes to the combination of dual basis vectors given by the column `μ` of the
> complexified Lorentz matrix. This is the complex analogue of
> `Lorentz.CoVector.sl2Rep_dual_dualBasis`, and is obtained from
> `Representation.dual_apply_dualBasis` with the transposed inverse matrix read off from
> `Lorentz.ComplexCoVector.basis_ρ_apply`.

## ii. Key results

> - `Lorentz.ComplexCoVector.SL2CRep_dual_dualBasis` : dual complex covectors transform by the columns
>   of the complexified Lorentz matrix.

## iv. References

> The complex covector representation is in
> `Physlib.Relativity.Tensors.ComplexTensor.Vector.Basic`.

## A. The dual representation on the dual basis

**`Lorentz.ComplexCoVector.SL2CRep_dual_dualBasis`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L60).

> The dual of the complex covector representation on the dual basis: dual covectors
> transform contravariantly, by the columns of the (complexified) Lorentz matrix. The
> complex analogue of `Lorentz.CoVector.sl2Rep_dual_dualBasis`.

```lean
lemma ComplexCoVector.SL2CRep_dual_dualBasis (Λ : SL(2,ℂ))
    (μ : Fin 1 ⊕ Fin 3) :
    Lorentz.ComplexCoVector.SL2CRep.dual Λ (Lorentz.ComplexCoVector.basis.dualBasis μ) =
      ∑ j, (((Lorentz.SL2C.toLorentzGroup Λ).1 j μ : ℝ) : ℂ) •
        Lorentz.ComplexCoVector.basis.dualBasis j
```

## Depends on

- [Complex Lorentz vectors](../../../physlib/relativity/tensors/part-02/complextensor-vector-basic.md)

## Proof depends on

- [Dual representations on a dual basis](../../mathematics/part-01/representationdual.md)

## Sources

- [PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Vector/Basic.lean)
