---
declaration: module
origin: cited
lean: complexLorentzTensor.invariants_pair_eq_span_metricTensor, Lorentz.invariantReductionToMetricTensor, Lorentz.RankTwo.isReindexing_up_up, Lorentz.RankTwo.metric, Lorentz.RankTwo.metric_invariant, Lorentz.RankTwo.coeffEquiv_symm_minkowskiMatrixZ, Lorentz.RankTwo.liftComponents_metric, complexLorentzTensor.invariants_up_pow_two_eq_span_metric
statement: formalized
proof: formalized
---

# The metrics are the unique invariant tensors with two indices of one colour

The module `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Metrics.Basic`, [PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean): 9 declarations, 9 with a docstring.

> Up to scale, the metric of a colour is the only invariant tensor with two indices of that colour.

## i. Overview

> A tensor with two indices of colour `k` is `fromPairT` of an element of the tensor square of the
> representation of that colour. The invariants of that tensor square are the line through the
> metric, for the four-vectors, the covectors and each of the four Weyl representations, so the
> invariant tensors of `ℂT[k, k]` are the line through `metricTensor k` (A). For an equivariant map
> `f` out of `ℂT[k, k]`, every Lorentz invariant of the range of `f` is a multiple of
> `f (metricTensor k)`, modulo a Lorentz-stable submodule, the shape of a mass term (B).
>
> The colours `fun _ : Fin 2 => .up` of two four-vector indices are a reindexing of `![.up, .up]`,
> so the invariant tensors with these colours are the line through the reindexed metric
> `RankTwo.metric`, whose components are the Minkowski metric (C).

## ii. Key results

> - `complexLorentzTensor.invariants_pair_eq_span_metricTensor` : the invariant tensors with two
>   indices of one colour are the line through the metric.
> - `Lorentz.invariantReductionToMetricTensor` : the invariants of the range of an equivariant map
>   reduce to the image of the metric.
> - `complexLorentzTensor.invariants_up_pow_two_eq_span_metric` : the same for the colours
>   `fun _ : Fin 2 => .up`.
> - `Lorentz.ComplexVector.reducesInvariantsTo_span_metric` : the invariants of an equivariant map
>   out of these tensors reduce to the image of the metric.

## iv. References

> The uniqueness of the metric of each representation is in
> `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Metrics.Pre` and
> `PhyslibAlpha.Relativity.Fermions.Weyl.Metric`.

## A. The invariant tensors with two indices of one colour

**`complexLorentzTensor.invariants_pair_eq_span_metricTensor`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L74).

> The invariant tensors with two indices of one colour are the line through the metric of that
> colour. A tensor with two indices comes from the tensor square of the representation of the
> colour, whose invariants are the line through the metric.

```lean
lemma _root_.complexLorentzTensor.invariants_pair_eq_span_metricTensor
    (k : complexLorentzTensor.Color) :
    (complexLorentzTensor.tensorRep ![k, k]).invariants = ℂ ∙ metricTensor k
```

## B. The reduction to the metric

**`Lorentz.invariantReductionToMetricTensor`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L105).

> For an equivariant map `f` out of `ℂT[k, k]`, the Lorentz invariants of the range of `f`
> reduce to the span of the image `f (metricTensor k)` of the metric.

```lean
noncomputable def invariantReductionToMetricTensor {k : complexLorentzTensor.Color} {B : Type*}
    [AddCommGroup B] [Module ℂ B] {repLorentz : Representation ℂ SL(2,ℂ) B}
    {f : ℂT[k, k] →ₗ[ℂ] B} (hf : complexLorentzTensor.IsEquivariant ![k, k] repLorentz f) :
    InvariantReductionToSpan (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f)
```

## C. Two four-vector indices with constant colours

### C.1. The metric with constant colours

**`Lorentz.RankTwo.isReindexing_up_up`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L130).

> Relabelling the colours `![.up, .up]` of two indices as `fun _ => .up`.

```lean
lemma isReindexing_up_up :
    IsReindexing ![Color.up, Color.up] (fun _ : Fin 2 => Color.up) id
```

**`Lorentz.RankTwo.metric`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L136).

> The metric `η` on two contravariant indices, with its colours relabelled from
> `![.up, .up]` to `fun _ => .up`.

```lean
noncomputable def metric : ℂT(fun _ : Fin 2 => Color.up)
```

**`Lorentz.RankTwo.metric_invariant`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L140).

> The metric is Lorentz invariant.

```lean
lemma metric_invariant (g : SL(2,ℂ)) : g • metric = metric
```

**`Lorentz.RankTwo.coeffEquiv_symm_minkowskiMatrixZ`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L144).

> The coefficient tensor of the metric is the Minkowski metric.

```lean
lemma coeffEquiv_symm_minkowskiMatrixZ :
    (coeffEquiv 2).symm (fun d => ((minkowskiMatrixZ (d 0) (d 1) : ℤ) : ℂ)) = metric
```

**`Lorentz.RankTwo.liftComponents_metric`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L156).

> `liftComponents T` sends the metric to the contraction `η_{μν} T^{μν}`.

```lean
lemma liftComponents_metric (T : (Fin 2 → Fin 1 ⊕ Fin 3) → B) :
    liftComponents T metric
      = ∑ d : Fin 2 → Fin 1 ⊕ Fin 3, ((minkowskiMatrixZ (d 0) (d 1) : ℤ) : ℂ) • T d
```

### C.2. The invariant tensors

**`complexLorentzTensor.invariants_up_pow_two_eq_span_metric`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L169).

> The invariant tensors with two four-vector indices of constant colours are the line through
> the metric, the reindexing of the line through `η`.

```lean
lemma _root_.complexLorentzTensor.invariants_up_pow_two_eq_span_metric :
    (complexLorentzTensor.tensorRep (fun _ : Fin 2 => Color.up)).invariants = ℂ ∙ metric
```

### C.3. The invariants of an equivariant map

**`Lorentz.ComplexVector.reducesInvariantsTo_span_metric`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean#L186).

> The invariants of the range of `f` reduce to the line through the image `f metric` of the
> metric. A Lorentz invariant of `LinearMap.range f ⊔ S`, for `S` a Lorentz-stable submodule, is
> a multiple of `f metric` plus an element of `S`.

```lean
lemma _root_.Lorentz.ComplexVector.reducesInvariantsTo_span_metric
    (hf : complexLorentzTensor.IsEquivariant (fun _ : Fin 2 => .up) repLorentz f) :
    ReducesInvariantsTo (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f)
      (ℂ ∙ f metric)
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Metrics.Basic](../../../physlib/relativity/tensors/part-01/complextensor-metrics-basic.md)
- [The Minkowski matrix over the integers](../minkowskimatrix.md)
- [Invariant coefficient tensors of the complex vector representation](complextensor-vector-invariantcoeff.md)

## Proof depends on

- [Invariants of two Weyl indices](../fermions/weyl-metric.md)
- [The metrics are the unique invariants](complextensor-metrics-pre.md)

## Sources

- [PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Tensors/ComplexTensor/Metrics/Basic.lean)
