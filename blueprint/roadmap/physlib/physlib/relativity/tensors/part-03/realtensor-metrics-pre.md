---
declaration: module
origin: cited
lean: Lorentz.ContrMod.metricVal, Lorentz.ContrMod.metricVal_expand_tmul_minkowskiMatrix, Lorentz.ContrMod.metricVal_expand_tmul, Lorentz.ContrMod.metric, Lorentz.ContrMod.metric_apply_one, Lorentz.CoMod.metricVal, Lorentz.CoMod.metricVal_expand_tmul_minkowskiMatrix, Lorentz.CoMod.metricVal_expand_tmul
statement: formalized
proof: formalized
---

# Metric for real Lorentz vectors

The module `Physlib.Relativity.Tensors.RealTensor.Metrics.Pre`, [Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean): 12 declarations, 6 with a docstring.

**`Lorentz.ContrMod.metricVal`**, a def, [line 24](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean#L24).

> The metric `ηᵃᵃ` as an element of `(ContrMod d ⊗[ℝ] ContrMod d)`.

```lean
def ContrMod.metricVal (d : ℕ := 3) : ContrMod d ⊗[ℝ] ContrMod d
```

**`Lorentz.ContrMod.metricVal_expand_tmul_minkowskiMatrix`**, a lemma, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean#L27).

```lean
lemma ContrMod.metricVal_expand_tmul_minkowskiMatrix {d : ℕ} : ContrMod.metricVal d =
    ∑ i, (minkowskiMatrix i i) • (contrBasis d i ⊗ₜ[ℝ] contrBasis d i)
```

**`Lorentz.ContrMod.metricVal_expand_tmul`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean#L34).

> Expansion of `ContrMod.metricVal` into basis.

```lean
lemma ContrMod.metricVal_expand_tmul {d : ℕ} : ContrMod.metricVal d =
    contrBasis d (Sum.inl 0) ⊗ₜ[ℝ] contrBasis d (Sum.inl 0) -
    ∑ i, contrBasis d (Sum.inr i) ⊗ₜ[ℝ] contrBasis d (Sum.inr i)
```

**`Lorentz.ContrMod.metric`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean#L43).

> The metric `ηᵃᵃ` as a morphism `𝟙_ (Rep ℝ (LorentzGroup d)) ⟶ ContrMod.rep ⊗ ContrMod.rep`,
> making its invariance under the action of `LorentzGroup d`.

```lean
def ContrMod.metric (d : ℕ := 3) :
    (Representation.trivial ℝ (LorentzGroup d) ℝ).IntertwiningMap
    ((ContrMod.rep).tprod (ContrMod.rep))
```

**`Lorentz.ContrMod.metric_apply_one`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean#L62).

```lean
lemma ContrMod.metric_apply_one {d : ℕ} : (ContrMod.metric d) (1 : ℝ) = ContrMod.metricVal d
```

**`Lorentz.CoMod.metricVal`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean#L66).

> The metric `ηᵢᵢ` as an element of `(CoMod d ⊗[ℝ] CoMod d)`.

```lean
def CoMod.metricVal (d : ℕ := 3) : CoMod d ⊗[ℝ] CoMod d
```

**`Lorentz.CoMod.metricVal_expand_tmul_minkowskiMatrix`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean#L69).

```lean
lemma CoMod.metricVal_expand_tmul_minkowskiMatrix {d : ℕ} : CoMod.metricVal d =
    ∑ i, (minkowskiMatrix i i) • (coBasis d i ⊗ₜ[ℝ] coBasis d i)
```

**`Lorentz.CoMod.metricVal_expand_tmul`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean#L76).

> Expansion of `ContrMod.metricVal` into basis.

```lean
lemma CoMod.metricVal_expand_tmul {d : ℕ} : CoMod.metricVal d =
    coBasis d (Sum.inl 0) ⊗ₜ[ℝ] coBasis d (Sum.inl 0) -
    ∑ i, coBasis d (Sum.inr i) ⊗ₜ[ℝ] coBasis d (Sum.inr i)
```

**`Lorentz.CoMod.metric`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean#L85).

> The metric `ηᵢᵢ` as a morphism `𝟙_ (Rep ℂ (LorentzGroup d))) ⟶ CoMod.rep ⊗ CoMod.rep`,
> making its invariance under the action of `LorentzGroup d`.

```lean
def CoMod.metric (d : ℕ := 3) : (Representation.trivial ℝ (LorentzGroup d) ℝ).IntertwiningMap
    ((CoMod.rep).tprod (CoMod.rep))
```

**`Lorentz.CoMod.metric_apply_one`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean#L102).

```lean
lemma CoMod.metric_apply_one {d : ℕ} : (CoMod.metric d) (1 : ℝ) = CoMod.metricVal d
```

## Contraction of metrics

**`Lorentz.ContrMod.contr_metric`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean#L112).

```lean
lemma ContrMod.contr_metric {d : ℕ} :
    (TensorProduct.comm ℝ _ _ <|
      (TensorProduct.lid ℝ _).lTensor _ <|
      (ContrMod.contr.toLinearMap.rTensor (CoMod d)).lTensor (ContrMod d) <|
      (TensorProduct.assoc ℝ (ContrMod d) (CoMod d) (CoMod d)).symm.toLinearMap.lTensor
        (ContrMod d) <|
      TensorProduct.assoc ℝ (ContrMod d) (ContrMod d) ((CoMod d) ⊗[ℝ] (CoMod d)) <|
      (ContrMod.metric d 1) ⊗ₜ[ℝ] (CoMod.metric d 1)) = ContrMod.unit d (1 : ℝ)
```

**`Lorentz.CoMod.contr_metric`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean#L152).

```lean
lemma CoMod.contr_metric {d : ℕ} :
    (TensorProduct.comm ℝ _ _ <|
    (TensorProduct.lid ℝ _).lTensor _ <|
    (CoMod.contr.toLinearMap.rTensor (ContrMod d)).lTensor (CoMod d) <|
    (TensorProduct.assoc ℝ (CoMod d) (ContrMod d) (ContrMod d)).symm.toLinearMap.lTensor
      (CoMod d) <|
    TensorProduct.assoc ℝ (CoMod d) (CoMod d) ((ContrMod d) ⊗[ℝ] (ContrMod d)) <|
    (CoMod.metric d 1) ⊗ₜ[ℝ] (ContrMod.metric d 1)) = CoMod.unit d (1 : ℝ)
```

## Depends on

- [Unit for complex Lorentz vectors (RealTensor/Units/Pre)](realtensor-units-pre.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Pre.lean)
