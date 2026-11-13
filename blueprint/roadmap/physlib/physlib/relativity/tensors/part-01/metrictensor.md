---
declaration: module
origin: cited
lean: TensorSpecies.metricTensor, TensorSpecies.metricTensor_basis_repr, TensorSpecies.metricTensor_congr, TensorSpecies.metricTensor_invariant, TensorSpecies.permT_fromPairTContr_metric_metric, TensorSpecies.fromPairTContr_metric_metric_eq_permT_unit, TensorSpecies.contrT_metricTensor_metricTensor, TensorSpecies.contrT_metricTensor_metricTensor_eq_dual_unit
statement: formalized
proof: formalized
---

# The metric tensors

The module `Physlib.Relativity.Tensors.MetricTensor`, [Physlib/Relativity/Tensors/MetricTensor.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/MetricTensor.lean): 9 declarations, 3 with a docstring.

**`TensorSpecies.metricTensor`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/MetricTensor.lean#L29).

> The metric tensor associated with a color `c`.

```lean
noncomputable def metricTensor (c : C) : S.Tensor ![c, c]
```

**`TensorSpecies.metricTensor_basis_repr`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/MetricTensor.lean#L34).

> A component of the metric tensor is the corresponding component of the metric intertwiner
> in the tensor-product basis.

```lean
lemma metricTensor_basis_repr (c : C) (φ : ComponentIdx (S := S) ![c, c]) :
    (Tensor.basis _).repr (metricTensor (S := S) c) φ =
      (Module.Basis.tensorProduct (b c) (b c)).repr ((S.metric c) (1 : k)) (φ 0, φ 1)
```

**`TensorSpecies.metricTensor_congr`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/MetricTensor.lean#L39).

```lean
lemma metricTensor_congr {c c1 : C} (h : c = c1) :
    S.metricTensor c = permT id (by simp [h]) (metricTensor c1)
```

**`TensorSpecies.metricTensor_invariant`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/MetricTensor.lean#L45).

```lean
lemma metricTensor_invariant {c : C} (g : G) :
    g • S.metricTensor c = metricTensor c
```

**`TensorSpecies.permT_fromPairTContr_metric_metric`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/MetricTensor.lean#L49).

```lean
lemma permT_fromPairTContr_metric_metric {c : C} :
    permT ![1, 0] (And.intro (by decide) (fun i => by fin_cases i <;> rfl))
    (fromPairTContr ((S.metric c) (1 : k))
    ((S.metric ((S.τ c))) (1 : k))) = (unitTensor c)
```

**`TensorSpecies.fromPairTContr_metric_metric_eq_permT_unit`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/MetricTensor.lean#L59).

```lean
lemma fromPairTContr_metric_metric_eq_permT_unit {c : C} :
    fromPairTContr ((S.metric c) (1 : k))
    ((S.metric (S.τ c)) (1 : k)) =
    permT ![1, 0] (And.intro (by decide) (fun i => by fin_cases i <;> rfl))
    (unitTensor c)
```

**`TensorSpecies.contrT_metricTensor_metricTensor`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/MetricTensor.lean#L74).

> The contraction of the metric tensor with its dual gives the unit tensor.
> This is the de-categorification of `S.contr_metric`.

```lean
lemma contrT_metricTensor_metricTensor {c : C} :
    contrT 2 1 2 (by simp; rfl) (prodT (metricTensor c) (metricTensor (S.τ c))) =
      permT ![1, 0] (And.intro (by decide) (fun i => by fin_cases i <;> rfl))
      (unitTensor (S := S) c)
```

**`TensorSpecies.contrT_metricTensor_metricTensor_eq_dual_unit`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/MetricTensor.lean#L85).

```lean
lemma contrT_metricTensor_metricTensor_eq_dual_unit {c : C} :
    contrT 2 1 2 (by simp; rfl) (prodT (metricTensor c) (metricTensor (S.τ c))) =
      permT ![0, 1] (And.intro (by decide) (fun i => by
        fin_cases i
        · change S.τ (S.τ c) = c
          simp
        · rfl))
      (unitTensor (S := S) (S.τ c))
```

**`TensorSpecies.contrT_dual_metricTensor_metricTensor`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/MetricTensor.lean#L102).

```lean
lemma contrT_dual_metricTensor_metricTensor {c : C} :
    contrT 2 1 2 (by change _ ∧ S.τ (S.τ c) = c; simp)
      (prodT (metricTensor (S.τ c)) (metricTensor c)) =
      permT id (by simp; exact ⟨rfl,rfl⟩) (unitTensor (S := S) c)
```

## Depends on

- [The unit tensors](unittensor.md)

## Sources

- [Physlib/Relativity/Tensors/MetricTensor.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/MetricTensor.lean)
