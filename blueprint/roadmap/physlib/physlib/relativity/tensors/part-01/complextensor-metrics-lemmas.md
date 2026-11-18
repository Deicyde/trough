---
declaration: module
origin: cited
lean: complexLorentzTensor.coMetric_symm, complexLorentzTensor.contrMetric_symm, complexLorentzTensor.leftMetric_antisymm, complexLorentzTensor.rightMetric_antisymm, complexLorentzTensor.dualLeftMetric_antisymm, complexLorentzTensor.dualRightMetric_antisymm, complexLorentzTensor.coMetric_contr_contrMetric, complexLorentzTensor.contrMetric_contr_coMetric
statement: formalized
proof: formalized
---

# Physlib.Relativity.Tensors.ComplexTensor.Metrics.Lemmas

The module `Physlib.Relativity.Tensors.ComplexTensor.Metrics.Lemmas`, [Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean): 12 declarations, 12 with a docstring.

## Basic lemmas regarding metrics

## Symmetry properties

**`complexLorentzTensor.coMetric_symm`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean#L34).

> The covariant metric is symmetric `{η' | μ ν = η' | ν μ}ᵀ`.

```lean
lemma coMetric_symm : {η' | μ ν = η' | ν μ}ᵀ
```

**`complexLorentzTensor.contrMetric_symm`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean#L44).

> The contravariant metric is symmetric `{η | μ ν = η | ν μ}ᵀ`.

```lean
lemma contrMetric_symm : {η | μ ν = η | ν μ}ᵀ
```

**`complexLorentzTensor.leftMetric_antisymm`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean#L54).

> The left metric is antisymmetric `{εL | α α' = - εL | α' α}ᵀ`.

```lean
lemma leftMetric_antisymm : {εL | α α' = - (εL| α' α)}ᵀ
```

**`complexLorentzTensor.rightMetric_antisymm`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean#L65).

> The right metric is antisymmetric `{εR | β β' = - εR | β' β}ᵀ`.

```lean
lemma rightMetric_antisymm : {εR | β β' = - (εR| β' β)}ᵀ
```

**`complexLorentzTensor.dualLeftMetric_antisymm`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean#L76).

> The dual-left metric is antisymmetric `{εL' | α α' = - εL' | α' α}ᵀ`.

```lean
lemma dualLeftMetric_antisymm : {εL' | α α' = - (εL' | α' α)}ᵀ
```

**`complexLorentzTensor.dualRightMetric_antisymm`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean#L87).

> The dual-right metric is antisymmetric `{εR' | β β' = - εR' | β' β}ᵀ`.

```lean
lemma dualRightMetric_antisymm : {εR' | α α' = - (εR' | α' α)}ᵀ
```

## Contractions with each other

**`complexLorentzTensor.coMetric_contr_contrMetric`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean#L106).

> The contraction of the covariant metric with the contravariant metric is the unit
> `{η' | μ ρ ⊗ η | ρ ν = δ' | μ ν}ᵀ`.

```lean
lemma coMetric_contr_contrMetric : {η' | μ ρ ⊗ η | ρ ν = δ' | μ ν}ᵀ
```

**`complexLorentzTensor.contrMetric_contr_coMetric`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean#L112).

> The contraction of the contravariant metric with the covariant metric is the unit
> `{η | μ ρ ⊗ η' | ρ ν = δ | μ ν}ᵀ`.

```lean
lemma contrMetric_contr_coMetric : {η | μ ρ ⊗ η' | ρ ν = δ | μ ν}ᵀ
```

**`complexLorentzTensor.leftMetric_contr_dualLeftMetric`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean#L118).

> The contraction of the left metric with the dual-left metric is the unit
> `{εL | α β ⊗ εL' | β γ = δL | α γ}ᵀ`.

```lean
lemma leftMetric_contr_dualLeftMetric : {εL | α β ⊗ εL' | β γ = δL | α γ}ᵀ
```

**`complexLorentzTensor.rightMetric_contr_dualRightMetric`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean#L124).

> The contraction of the right metric with the dual-right metric is the unit
> `{εR | α β ⊗ εR' | β γ = δR | α γ}ᵀ`.

```lean
lemma rightMetric_contr_dualRightMetric : {εR | α β ⊗ εR' | β γ = δR | α γ}ᵀ
```

**`complexLorentzTensor.dualLeftMetric_contr_leftMetric`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean#L130).

> The contraction of the dual-left metric with the left metric is the unit
> `{εL' | α β ⊗ εL | β γ = δL' | α γ}ᵀ`.

```lean
lemma dualLeftMetric_contr_leftMetric : {εL' | α β ⊗ εL | β γ = δL' | α γ}ᵀ
```

**`complexLorentzTensor.dualRightMetric_contr_rightMetric`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean#L136).

> The contraction of the dual-right metric with the right metric is the unit
> `{εR' | α β ⊗ εR | β γ = δR' | α γ}ᵀ`.

```lean
lemma dualRightMetric_contr_rightMetric : {εR' | α β ⊗ εR | β γ = δR' | α γ}ᵀ
```

## Other relations

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Metrics.Basic](complextensor-metrics-basic.md)
- [Physlib.Relativity.Tensors.ComplexTensor.Units.Basic](complextensor-units-basic.md)

## Sources

- [Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Metrics/Lemmas.lean)
