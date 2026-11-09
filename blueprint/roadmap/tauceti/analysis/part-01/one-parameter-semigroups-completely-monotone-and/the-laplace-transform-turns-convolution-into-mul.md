---
declaration: theorem
origin: cited
lean: TauCeti.laplaceTransform_conv
statement: formalized
proof: formalized
---

# The Laplace transform turns convolution into multiplication

The identity needs no
finiteness or integrability hypothesis: under the junk-value convention for non-integrable
Bochner integrals it holds for all s-finite measures and every real parameter `t`.

```lean
TauCeti.laplaceTransform_conv (μ ν : MeasureTheory.Measure NNReal) [MeasureTheory.SFinite μ]
  [MeasureTheory.SFinite ν] (t : ℝ) :
  TauCeti.laplaceTransform (μ.conv ν) t =
    TauCeti.laplaceTransform μ t * TauCeti.laplaceTransform ν t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.laplaceTransform_conv`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/Laplace/Convolution.html#TauCeti.laplaceTransform_conv).

## Sources

- [Tau Ceti documentation: `TauCeti.laplaceTransform_conv`](https://taucetiproject.org/docs/TauCeti/Analysis/CompletelyMonotone/Laplace/Convolution.html#TauCeti.laplaceTransform_conv)
- [Source of `TauCeti.laplaceTransform_conv` in TauCeti/Analysis/CompletelyMonotone/Laplace/Convolution.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CompletelyMonotone/Laplace/Convolution.lean#L54)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OneParameterSemigroups/STATUS.md)
