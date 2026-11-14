---
declaration: module
origin: cited
lean: Lorentz.ComplexCoVector.unitVal, Lorentz.ComplexCoVector.unitVal_expand_tmul, Lorentz.ComplexCoVector.unitVal_eq_sum_tmul, Lorentz.ComplexCoVector.unit, Lorentz.ComplexCoVector.unit_apply_one, Lorentz.ComplexVector.unitVal, Lorentz.ComplexVector.unitVal_expand_tmul, Lorentz.ComplexVector.unitVal_eq_sum_tmul
statement: formalized
proof: formalized
---

# Unit for complex Lorentz vectors (ComplexTensor/Units/Pre)

The module `Physlib.Relativity.Tensors.ComplexTensor.Units.Pre`, [Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean): 14 declarations, 8 with a docstring.

**`Lorentz.ComplexCoVector.unitVal`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L28).

> The contra-co unit for complex lorentz vectors. Usually denoted `δⁱᵢ`.

```lean
def ComplexCoVector.unitVal : ComplexVector ⊗[ℂ] ComplexCoVector
```

**`Lorentz.ComplexCoVector.unitVal_expand_tmul`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L32).

> Expansion of `ComplexCoVector.unitVal` into basis.

```lean
lemma ComplexCoVector.unitVal_expand_tmul : ComplexCoVector.unitVal =
    ComplexVector.basis (Sum.inl 0) ⊗ₜ[ℂ] ComplexCoVector.basis (Sum.inl 0)
    + ComplexVector.basis (Sum.inr 0) ⊗ₜ[ℂ] ComplexCoVector.basis (Sum.inr 0)
    + ComplexVector.basis (Sum.inr 1) ⊗ₜ[ℂ] ComplexCoVector.basis (Sum.inr 1)
    + ComplexVector.basis (Sum.inr 2) ⊗ₜ[ℂ] ComplexCoVector.basis (Sum.inr 2)
```

**`Lorentz.ComplexCoVector.unitVal_eq_sum_tmul`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L45).

```lean
lemma ComplexCoVector.unitVal_eq_sum_tmul : ComplexCoVector.unitVal =
    ∑ i, ComplexVector.basis i ⊗ₜ[ℂ] ComplexCoVector.basis i
```

**`Lorentz.ComplexCoVector.unit`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L53).

> The contra-co unit for complex lorentz vectors as a morphism
> `𝟙_ (Rep ℂ SL(2,ℂ)) ⟶ complexContr ⊗ complexCo`, manifesting the invariance under
> the `SL(2, ℂ)` action.

```lean
def ComplexCoVector.unit : (Representation.trivial ℂ SL(2,ℂ) ℂ).IntertwiningMap
    (ComplexVector.SL2CRep.tprod ComplexCoVector.SL2CRep)
```

**`Lorentz.ComplexCoVector.unit_apply_one`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L75).

```lean
lemma ComplexCoVector.unit_apply_one : ComplexCoVector.unit (1 : ℂ) = ComplexCoVector.unitVal
```

**`Lorentz.ComplexVector.unitVal`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L80).

> The co-contra unit for complex lorentz vectors. Usually denoted `δᵢⁱ`.

```lean
def ComplexVector.unitVal : ComplexCoVector ⊗[ℂ] ComplexVector
```

**`Lorentz.ComplexVector.unitVal_expand_tmul`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L84).

> Expansion of `ComplexVector.unitVal` into basis.

```lean
lemma ComplexVector.unitVal_expand_tmul : ComplexVector.unitVal =
    ComplexCoVector.basis (Sum.inl 0) ⊗ₜ[ℂ] ComplexVector.basis (Sum.inl 0)
    + ComplexCoVector.basis (Sum.inr 0) ⊗ₜ[ℂ] ComplexVector.basis (Sum.inr 0)
    + ComplexCoVector.basis (Sum.inr 1) ⊗ₜ[ℂ] ComplexVector.basis (Sum.inr 1)
    + ComplexCoVector.basis (Sum.inr 2) ⊗ₜ[ℂ] ComplexVector.basis (Sum.inr 2)
```

**`Lorentz.ComplexVector.unitVal_eq_sum_tmul`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L97).

```lean
lemma ComplexVector.unitVal_eq_sum_tmul : ComplexVector.unitVal =
    ∑ i, ComplexCoVector.basis i ⊗ₜ[ℂ] ComplexVector.basis i
```

**`Lorentz.ComplexVector.unit`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L105).

> The co-contra unit for complex lorentz vectors as a morphism
> `𝟙_ (Rep ℂ SL(2,ℂ)) ⟶ complexCo ⊗ complexContr`, manifesting the invariance under
> the `SL(2, ℂ)` action.

```lean
def ComplexVector.unit : (Representation.trivial ℂ SL(2,ℂ) ℂ).IntertwiningMap
    (ComplexCoVector.SL2CRep.tprod ComplexVector.SL2CRep)
```

**`Lorentz.ComplexVector.unit_apply_one`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L129).

```lean
lemma ComplexVector.unit_apply_one : ComplexVector.unit (1 : ℂ) = ComplexVector.unitVal
```

## Contraction of the units

**`Lorentz.ComplexCoVector.contr_unit`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L140).

> Contraction on the right with `ComplexCoVector.unit` does nothing.

```lean
lemma ComplexCoVector.contr_unit (x : ComplexCoVector) :
    (TensorProduct.lid ℂ _ <|
    ComplexCoVector.contr.toLinearMap.rTensor _ <|
    (TensorProduct.assoc ℂ _ _ _).symm <|
    x ⊗ₜ[ℂ] (ComplexCoVector.unit (1 : ℂ))) = x
```

**`Lorentz.ComplexVector.contr_unit`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L152).

> Contraction on the right with `ComplexVector.unit`.

```lean
lemma ComplexVector.contr_unit (x : ComplexVector) :
    (TensorProduct.lid ℂ _ <|
    ComplexVector.contr.toLinearMap.rTensor _ <|
    (TensorProduct.assoc ℂ _ _ _).symm <|
    x ⊗ₜ[ℂ] (ComplexVector.unit (1 : ℂ))) = x
```

## Symmetry properties of the units

**`Lorentz.ComplexCoVector.unit_symm`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L171).

```lean
lemma ComplexCoVector.unit_symm :
    ComplexCoVector.unit (1 : ℂ) = LinearMap.lTensor _ (LinearEquiv.refl _ _).toLinearMap
      (TensorProduct.comm ℂ _ _ (ComplexVector.unit (1 : ℂ)))
```

**`Lorentz.ComplexVector.unit_symm`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean#L178).

```lean
lemma ComplexVector.unit_symm :
    (ComplexVector.unit (1 : ℂ)) = LinearMap.lTensor _ (LinearEquiv.refl _ _).toLinearMap
      (TensorProduct.comm ℂ _ _ (ComplexCoVector.unit (1 : ℂ)))
```

## Depends on

- [Tensor products of two complex Lorentz vectors](../part-01/complextensor-matrix-pre.md)
- [Contraction of Lorentz vectors](complextensor-vector-contraction.md)

## Sources

- [Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Units/Pre.lean)
