---
declaration: module
origin: cited
lean: LorentzGroup.toComplex_mul_mul_minkowskiMatrix_map_mul_inv, LorentzGroup.inv_toComplex_transpose_mul_minkowskiMatrix_map_mul_mul, Lorentz.ComplexCoVector.invariants_tprod_eq_span_unitVal, Lorentz.ComplexVector.invariants_tprod_eq_span_unitVal
statement: formalized
proof: formalized
---

# The units are the unique invariants (Pre)

The module `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Units.Pre`, [PhyslibAlpha/Relativity/Tensors/ComplexTensor/Units/Pre.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Units/Pre.lean): 4 declarations, 4 with a docstring.

> Up to scale, the unit `δ` is the only invariant of a complex Lorentz vector index and a covector
> index.

## i. Overview

> On `ComplexVector ⊗ ComplexCoVector` the group `SL(2, ℂ)` acts on the matrix of components by
> `X ↦ Λ X Λ⁻¹`, and on `ComplexCoVector ⊗ ComplexVector` by `X ↦ Λ⁻¹ᵀ X Λᵀ`, with `Λ` the
> complexified Lorentz matrix. Since `Λ⁻¹ = η Λᵀ η`, multiplying the matrix of components by the
> complexified Minkowski matrix `η` on the right, respectively on the left, turns either action into
> the action `Y ↦ Λ Y Λᵀ` on two contravariant indices (A). The classification of invariants for that
> action in `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Metrics.Pre` then applies, and `η` goes to
> `η η = 1`, the matrix of components of the unit. For each of the two orderings the invariants of
> the tensor product are the line through the unit (B, C).

## ii. Key results

> - `Lorentz.ComplexCoVector.invariants_tprod_eq_span_unitVal` : the invariants of
>   `ComplexVector ⊗ ComplexCoVector` are the line through the unit.
> - `Lorentz.ComplexVector.invariants_tprod_eq_span_unitVal` : the same for
>   `ComplexCoVector ⊗ ComplexVector`.

## iv. References

> The units are in `Physlib.Relativity.Tensors.ComplexTensor.Units.Pre`, where these results are
> written to move. The analogous results for Weyl fermions are in
> `PhyslibAlpha.Relativity.Fermions.Weyl.Unit`.

## A. Reparametrising the mixed actions by the Minkowski matrix

**`LorentzGroup.toComplex_mul_mul_minkowskiMatrix_map_mul_inv`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L65).

> Multiplying on the right by `η` turns the action `X ↦ Λ X Λ⁻¹` on a contravariant and a
> covariant index into the action `Y ↦ Λ Y Λᵀ` on two contravariant indices.

```lean
lemma toComplex_mul_mul_minkowskiMatrix_map_mul_inv (Λ : LorentzGroup d)
    (Y : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℂ) :
    toComplex Λ * (Y * minkowskiMatrix.map ofRealHom) * (toComplex Λ)⁻¹ =
      toComplex Λ * Y * (toComplex Λ)ᵀ * minkowskiMatrix.map ofRealHom
```

**`LorentzGroup.inv_toComplex_transpose_mul_minkowskiMatrix_map_mul_mul`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L73).

> Multiplying on the left by `η` turns the action `X ↦ Λ⁻¹ᵀ X Λᵀ` on a covariant and a
> contravariant index into the action `Y ↦ Λ Y Λᵀ` on two contravariant indices.

```lean
lemma inv_toComplex_transpose_mul_minkowskiMatrix_map_mul_mul (Λ : LorentzGroup d)
    (Y : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℂ) :
    (toComplex Λ)⁻¹ᵀ * (minkowskiMatrix.map ofRealHom * Y) * (toComplex Λ)ᵀ =
      minkowskiMatrix.map ofRealHom * (toComplex Λ * Y * (toComplex Λ)ᵀ)
```

## B. A contravariant then a covariant index

**`Lorentz.ComplexCoVector.invariants_tprod_eq_span_unitVal`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L91).

> Up to scale, the unit `δⁱᵢ` is the unique invariant of `ComplexVector ⊗ ComplexCoVector`.

```lean
lemma ComplexCoVector.invariants_tprod_eq_span_unitVal :
    (ComplexVector.SL2CRep.tprod ComplexCoVector.SL2CRep).invariants =
      ℂ ∙ ComplexCoVector.unitVal
```

## C. A covariant then a contravariant index

**`Lorentz.ComplexVector.invariants_tprod_eq_span_unitVal`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L112).

> Up to scale, the unit `δᵢⁱ` is the unique invariant of `ComplexCoVector ⊗ ComplexVector`.

```lean
lemma ComplexVector.invariants_tprod_eq_span_unitVal :
    (ComplexCoVector.SL2CRep.tprod ComplexVector.SL2CRep).invariants =
      ℂ ∙ ComplexVector.unitVal
```

## Depends on

- [Unit for complex Lorentz vectors (ComplexTensor/Units/Pre)](../../../physlib/relativity/tensors/part-02/complextensor-units-pre.md)

## Proof depends on

- [The metrics are the unique invariants](complextensor-metrics-pre.md)

## Sources

- [PhyslibAlpha/Relativity/Tensors/ComplexTensor/Units/Pre.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Units/Pre.lean)
