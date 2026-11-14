---
declaration: module
origin: cited
lean: Fermion.metricRaw, Fermion.comm_metricRaw, Fermion.metricRaw_comm, Fermion.star_comm_metricRaw, Fermion.metricRaw_comm_star, Fermion.LeftHandedWeyl.metricVal, Fermion.LeftHandedWeyl.metricVal_expand_tmul, Fermion.LeftHandedWeyl.metricVal_expand_tmul'
statement: formalized
proof: formalized
---

# Metrics of Weyl fermions

The module `Physlib.Relativity.Fermions.Weyl.Metric`, [Physlib/Relativity/Fermions/Weyl/Metric.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean): 27 declarations, 14 with a docstring.

> We define the metrics for Weyl fermions, often denoted `ε` in the literature.
> These allow us to go from left-handed to dual-left-handed Weyl fermions and back,
> and from right-handed to dual-right-handed Weyl fermions and back.

## A. The underlying matrix

**`Fermion.metricRaw`**, a def, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L37).

> The raw `2x2` matrix corresponding to the metric for fermions.

```lean
def metricRaw : Matrix (Fin 2) (Fin 2) ℂ
```

**`Fermion.comm_metricRaw`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L41).

> Multiplying an element of `SL(2, ℂ)` on the left with the metric `𝓔` is equivalent
> to multiplying the inverse-transpose of that element on the right with the metric.

```lean
lemma comm_metricRaw (M : SL(2,ℂ)) : M.1 * metricRaw = metricRaw * (M.1⁻¹)ᵀ
```

**`Fermion.metricRaw_comm`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L51).

```lean
lemma metricRaw_comm (M : SL(2,ℂ)) : metricRaw * M.1 = (M.1⁻¹)ᵀ * metricRaw
```

**`Fermion.star_comm_metricRaw`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L62).

```lean
lemma star_comm_metricRaw (M : SL(2,ℂ)) : M.1.map star * metricRaw = metricRaw * ((M.1)⁻¹)ᴴ
```

**`Fermion.metricRaw_comm_star`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L70).

```lean
lemma metricRaw_comm_star (M : SL(2,ℂ)) : metricRaw * M.1.map star = ((M.1)⁻¹)ᴴ * metricRaw
```

## B. The metric for left-handed Weyl fermions

**`Fermion.LeftHandedWeyl.metricVal`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L85).

> The metric `εᵃᵃ` as an element of `(leftHanded ⊗ leftHanded).V`.

```lean
def LeftHandedWeyl.metricVal : LeftHandedWeyl ⊗[ℂ] LeftHandedWeyl
```

**`Fermion.LeftHandedWeyl.metricVal_expand_tmul`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L89).

> Expansion of `LeftHandedWeyl.metricVal` into the left basis.

```lean
lemma LeftHandedWeyl.metricVal_expand_tmul : LeftHandedWeyl.metricVal =
    - LeftHandedWeyl.basis 0 ⊗ₜ[ℂ] LeftHandedWeyl.basis 1 +
      LeftHandedWeyl.basis 1 ⊗ₜ[ℂ] LeftHandedWeyl.basis 0
```

**`Fermion.LeftHandedWeyl.metricVal_expand_tmul'`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L99).

```lean
lemma LeftHandedWeyl.metricVal_expand_tmul' : LeftHandedWeyl.metricVal =
    LeftHandedWeyl.basis 1 ⊗ₜ[ℂ] LeftHandedWeyl.basis 0
    - LeftHandedWeyl.basis 0 ⊗ₜ[ℂ] LeftHandedWeyl.basis 1
```

**`Fermion.LeftHandedWeyl.metric`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L106).

> The metric `εᵃᵃ` as a morphism `𝟙_ (Rep ℂ SL(2,ℂ)) ⟶ leftHanded ⊗ leftHanded`,
> making manifest its invariance under the action of `SL(2,ℂ)`.

```lean
def LeftHandedWeyl.metric : (Representation.trivial ℂ SL(2,ℂ) ℂ).IntertwiningMap
    (LeftHandedWeyl.rep.tprod LeftHandedWeyl.rep)
```

**`Fermion.LeftHandedWeyl.metric_apply_one`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L130).

```lean
lemma LeftHandedWeyl.metric_apply_one :
    LeftHandedWeyl.metric (1 : ℂ) = LeftHandedWeyl.metricVal
```

## C. The metric for dual left-handed Weyl fermions

**`Fermion.DualLeftHandedWeyl.metricVal`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L142).

> The metric `εₐₐ` as an element of `(dualLeftHanded ⊗ dualLeftHanded).V`.

```lean
def DualLeftHandedWeyl.metricVal : (DualLeftHandedWeyl ⊗[ℂ] DualLeftHandedWeyl)
```

**`Fermion.DualLeftHandedWeyl.metricVal_expand_tmul`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L146).

> Expansion of `DualLeftHandedWeyl.metricVal` into the left basis.

```lean
lemma DualLeftHandedWeyl.metricVal_expand_tmul : DualLeftHandedWeyl.metricVal =
    DualLeftHandedWeyl.basis 0 ⊗ₜ[ℂ] DualLeftHandedWeyl.basis 1 -
      DualLeftHandedWeyl.basis 1 ⊗ₜ[ℂ] DualLeftHandedWeyl.basis 0
```

**`Fermion.DualLeftHandedWeyl.metric`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L157).

> The metric `εₐₐ` as a morphism `𝟙_ (Rep ℂ SL(2,ℂ)) ⟶ dualLeftHanded ⊗ dualLeftHanded`,
> making manifest its invariance under the action of `SL(2,ℂ)`.

```lean
def DualLeftHandedWeyl.metric : (Representation.trivial ℂ SL(2,ℂ) ℂ).IntertwiningMap
    (DualLeftHandedWeyl.rep.tprod DualLeftHandedWeyl.rep)
```

**`Fermion.DualLeftHandedWeyl.metric_apply_one`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L181).

```lean
lemma DualLeftHandedWeyl.metric_apply_one :
    DualLeftHandedWeyl.metric (1 : ℂ) = DualLeftHandedWeyl.metricVal
```

## D. The metric for right-handed Weyl fermions

**`Fermion.RightHandedWeyl.metricVal`**, a def, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L193).

> The metric `ε^{dot a}^{dot a}` as an element of `(rightHanded ⊗ rightHanded).V`.

```lean
def RightHandedWeyl.metricVal : (RightHandedWeyl ⊗[ℂ] RightHandedWeyl)
```

**`Fermion.RightHandedWeyl.metricVal_expand_tmul`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L197).

> Expansion of `RightHandedWeyl.metricVal` into the left basis.

```lean
lemma RightHandedWeyl.metricVal_expand_tmul : RightHandedWeyl.metricVal =
    - RightHandedWeyl.basis 0 ⊗ₜ[ℂ] RightHandedWeyl.basis 1 +
      RightHandedWeyl.basis 1 ⊗ₜ[ℂ] RightHandedWeyl.basis 0
```

**`Fermion.RightHandedWeyl.metricVal_expand_tmul'`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L207).

```lean
lemma RightHandedWeyl.metricVal_expand_tmul' : RightHandedWeyl.metricVal =
    RightHandedWeyl.basis 1 ⊗ₜ[ℂ] RightHandedWeyl.basis 0
    - RightHandedWeyl.basis 0 ⊗ₜ[ℂ] RightHandedWeyl.basis 1
```

**`Fermion.RightHandedWeyl.metric`**, a def, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L215).

> The metric `ε^{dot a}^{dot a}` as a morphism `𝟙_ (Rep ℂ SL(2,ℂ)) ⟶ rightHanded ⊗ rightHanded`,
> making manifest its invariance under the action of `SL(2,ℂ)`.

```lean
def RightHandedWeyl.metric : (Representation.trivial ℂ SL(2,ℂ) ℂ).IntertwiningMap
    (RightHandedWeyl.rep.tprod RightHandedWeyl.rep)
```

**`Fermion.RightHandedWeyl.metric_apply_one`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L246).

```lean
lemma RightHandedWeyl.metric_apply_one :
    RightHandedWeyl.metric (1 : ℂ) = RightHandedWeyl.metricVal
```

## E. The metric for dual right-handed Weyl fermions

**`Fermion.DualRightHandedWeyl.metricVal`**, a def, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L258).

> The metric `ε_{dot a}_{dot a}` as an element of `(dualRightHanded ⊗ dualRightHanded).V`.

```lean
def DualRightHandedWeyl.metricVal : DualRightHandedWeyl ⊗[ℂ] DualRightHandedWeyl
```

**`Fermion.DualRightHandedWeyl.metricVal_expand_tmul`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L262).

> Expansion of `RightHandedWeyl.metricVal` into the left basis.

```lean
lemma DualRightHandedWeyl.metricVal_expand_tmul : DualRightHandedWeyl.metricVal =
    DualRightHandedWeyl.basis 0 ⊗ₜ[ℂ] DualRightHandedWeyl.basis 1 -
      DualRightHandedWeyl.basis 1 ⊗ₜ[ℂ] DualRightHandedWeyl.basis 0
```

**`Fermion.DualRightHandedWeyl.metric`**, a def, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L274).

> The metric `ε_{dot a}_{dot a}` as a morphism
> `𝟙_ (Rep ℂ SL(2,ℂ)) ⟶ dualRightHanded ⊗ dualRightHanded`,
> making manifest its invariance under the action of `SL(2,ℂ)`.

```lean
def DualRightHandedWeyl.metric : (Representation.trivial ℂ SL(2,ℂ) ℂ).IntertwiningMap
    (DualRightHandedWeyl.rep.tprod DualRightHandedWeyl.rep)
```

**`Fermion.DualRightHandedWeyl.metric_apply_one`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L307).

```lean
lemma DualRightHandedWeyl.metric_apply_one :
    DualRightHandedWeyl.metric (1 : ℂ) = DualRightHandedWeyl.metricVal
```

## Contraction of metrics

**`Fermion.LeftHandedWeyl.contr_metric`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L324).

```lean
lemma LeftHandedWeyl.contr_metric :
    (TensorProduct.comm ℂ _ _ <|
      (TensorProduct.lid ℂ _).lTensor _ <|
      (LeftHandedWeyl.contr.toLinearMap.rTensor _).lTensor _ <|
      (TensorProduct.assoc ℂ _ _ _).symm.toLinearMap.lTensor _<|
      TensorProduct.assoc ℂ _ _ (_ ⊗[ℂ] _) <|
      (LeftHandedWeyl.metric 1) ⊗ₜ[ℂ] (DualLeftHandedWeyl.metric 1)) =
      LeftHandedWeyl.unit (1 : ℂ)
```

**`Fermion.DualLeftHandedWeyl.contr_metric`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L344).

```lean
lemma DualLeftHandedWeyl.contr_metric :
    (TensorProduct.comm ℂ _ _ <|
    (TensorProduct.lid ℂ _).lTensor _ <|
    (DualLeftHandedWeyl.contr.toLinearMap.rTensor _).lTensor _ <|
    (TensorProduct.assoc ℂ _ _ _).symm.toLinearMap.lTensor _<|
    TensorProduct.assoc ℂ _ _ (_ ⊗[ℂ] _) <|
    (DualLeftHandedWeyl.metric 1) ⊗ₜ[ℂ] (LeftHandedWeyl.metric 1)) =
    DualLeftHandedWeyl.unit (1 : ℂ)
```

**`Fermion.RightHandedWeyl.contr_metric`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L363).

```lean
lemma RightHandedWeyl.contr_metric :
    (TensorProduct.comm ℂ _ _ <|
    (TensorProduct.lid ℂ _).lTensor _ <|
    (RightHandedWeyl.contr.toLinearMap.rTensor _).lTensor _ <|
    (TensorProduct.assoc ℂ _ _ _).symm.toLinearMap.lTensor _<|
    TensorProduct.assoc ℂ _ _ (_ ⊗[ℂ] _) <|
    (RightHandedWeyl.metric 1) ⊗ₜ[ℂ] (DualRightHandedWeyl.metric 1)) =
    RightHandedWeyl.unit (1 : ℂ)
```

**`Fermion.DualRightHandedWeyl.contr_metric`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean#L384).

```lean
lemma DualRightHandedWeyl.contr_metric :
    (TensorProduct.comm ℂ _ _ <|
      (TensorProduct.lid ℂ _).lTensor _ <|
      (DualRightHandedWeyl.contr.toLinearMap.rTensor _).lTensor _ <|
      (TensorProduct.assoc ℂ _ _ _).symm.toLinearMap.lTensor _<|
      TensorProduct.assoc ℂ _ _ (_ ⊗[ℂ] _) <|
      (DualRightHandedWeyl.metric 1) ⊗ₜ[ℂ] (RightHandedWeyl.metric 1)) =
      DualRightHandedWeyl.unit (1 : ℂ)
```

## Depends on

- [Units of Weyl fermions](unit.md)

## Sources

- [Physlib/Relativity/Fermions/Weyl/Metric.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Metric.lean)
