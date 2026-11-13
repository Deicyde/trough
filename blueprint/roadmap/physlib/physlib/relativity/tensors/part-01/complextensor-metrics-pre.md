---
declaration: module
origin: cited
lean: Lorentz.ComplexVector.metricVal, Lorentz.ComplexVector.metricVal_expand_tmul, Lorentz.ComplexVector.metric, Lorentz.ComplexVector.metric_apply_one, Lorentz.ComplexCoVector.metricVal, Lorentz.ComplexCoVector.metricVal_expand_tmul, Lorentz.ComplexCoVector.metric, Lorentz.ComplexCoVector.metric_apply_one
statement: formalized
proof: formalized
---

# Metric for complex Lorentz vectors

The module `Physlib.Relativity.Tensors.ComplexTensor.Metrics.Pre`, [Physlib/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean): 10 declarations, 6 with a docstring.

**`Lorentz.ComplexVector.metricVal`**, a def, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L27).

> The metric `ηᵃᵃ` as an element of `(complexContr ⊗ complexContr).V`.

```lean
def ComplexVector.metricVal : (ComplexVector ⊗[ℂ] ComplexVector)
```

**`Lorentz.ComplexVector.metricVal_expand_tmul`**, a lemma, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L31).

> The expansion of `ComplexVector.metricVal` into basis vectors.

```lean
lemma ComplexVector.metricVal_expand_tmul : ComplexVector.metricVal =
    ComplexVector.basis (Sum.inl 0) ⊗ₜ[ℂ] ComplexVector.basis (Sum.inl 0)
    - ComplexVector.basis (Sum.inr 0) ⊗ₜ[ℂ] ComplexVector.basis (Sum.inr 0)
    - ComplexVector.basis (Sum.inr 1) ⊗ₜ[ℂ] ComplexVector.basis (Sum.inr 1)
    - ComplexVector.basis (Sum.inr 2) ⊗ₜ[ℂ] ComplexVector.basis (Sum.inr 2)
```

**`Lorentz.ComplexVector.metric`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L50).

> The metric `ηᵃᵃ` as a morphism `𝟙_ (Rep ℂ SL(2,ℂ)) ⟶ complexContr ⊗ complexContr`,
> making its invariance under the action of `SL(2,ℂ)`.

```lean
def ComplexVector.metric : (Representation.trivial ℂ SL(2,ℂ) ℂ).IntertwiningMap
    (ComplexVector.SL2CRep.tprod ComplexVector.SL2CRep)
```

**`Lorentz.ComplexVector.metric_apply_one`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L72).

```lean
lemma ComplexVector.metric_apply_one : ComplexVector.metric (1 : ℂ) = ComplexVector.metricVal
```

**`Lorentz.ComplexCoVector.metricVal`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L77).

> The metric `ηᵢᵢ` as an element of `(complexCo ⊗ complexCo).V`.

```lean
def ComplexCoVector.metricVal : (ComplexCoVector ⊗[ℂ] ComplexCoVector)
```

**`Lorentz.ComplexCoVector.metricVal_expand_tmul`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L81).

> The expansion of `ComplexCoVector.metricVal` into basis vectors.

```lean
lemma ComplexCoVector.metricVal_expand_tmul : ComplexCoVector.metricVal =
    ComplexCoVector.basis (Sum.inl 0) ⊗ₜ[ℂ] ComplexCoVector.basis (Sum.inl 0)
    - ComplexCoVector.basis (Sum.inr 0) ⊗ₜ[ℂ] ComplexCoVector.basis (Sum.inr 0)
    - ComplexCoVector.basis (Sum.inr 1) ⊗ₜ[ℂ] ComplexCoVector.basis (Sum.inr 1)
    - ComplexCoVector.basis (Sum.inr 2) ⊗ₜ[ℂ] ComplexCoVector.basis (Sum.inr 2)
```

**`Lorentz.ComplexCoVector.metric`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L100).

> The metric `ηᵢᵢ` as a morphism `𝟙_ (Rep ℂ SL(2,ℂ)) ⟶ complexCo ⊗ complexCo`,
> making its invariance under the action of `SL(2,ℂ)`.

```lean
def ComplexCoVector.metric : (Representation.trivial ℂ SL(2,ℂ) ℂ).IntertwiningMap
    (ComplexCoVector.SL2CRep.tprod ComplexCoVector.SL2CRep)
```

**`Lorentz.ComplexCoVector.metric_apply_one`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L124).

```lean
lemma ComplexCoVector.metric_apply_one :
    ComplexCoVector.metric (1 : ℂ) = ComplexCoVector.metricVal
```

## Contraction of metrics

**`Lorentz.ComplexVector.contr_metric`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L141).

```lean
lemma ComplexVector.contr_metric :
    (TensorProduct.comm ℂ _ _ <|
      (TensorProduct.lid ℂ _).lTensor _ <|
      (ComplexVector.contr.toLinearMap.rTensor _).lTensor _ <|
      (TensorProduct.assoc ℂ _ _ _).symm.toLinearMap.lTensor _<|
      TensorProduct.assoc ℂ _ _ (_ ⊗[ℂ] _) <|
      (ComplexVector.metric 1) ⊗ₜ[ℂ] (ComplexCoVector.metric 1)) = ComplexVector.unit (1 : ℝ)
```

**`Lorentz.ComplexCoVector.contr_metric`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean#L156).

```lean
lemma ComplexCoVector.contr_metric :
    (TensorProduct.comm ℂ _ _ <|
      (TensorProduct.lid ℂ _).lTensor _ <|
      (ComplexCoVector.contr.toLinearMap.rTensor _).lTensor _ <|
      (TensorProduct.assoc ℂ _ _ _).symm.toLinearMap.lTensor _<|
      TensorProduct.assoc ℂ _ _ (_ ⊗[ℂ] _) <|
      (ComplexCoVector.metric 1) ⊗ₜ[ℂ] (ComplexVector.metric 1)) =
      ComplexCoVector.unit (1 : ℝ)
```

## Depends on

- [Unit for complex Lorentz vectors (ComplexTensor/Units/Pre)](../part-02/complextensor-units-pre.md)

## Sources

- [Physlib/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Pre.lean)
