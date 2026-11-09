---
declaration: theorem
origin: cited
lean: TauCeti.norm_deriv_div_one_sub_norm_sq_le
statement: formalized
proof: formalized
---

# The infinitesimal Schwarz--Pick inequality

A holomorphic self-map `f` of the open
unit disc contracts the Poincaré metric: at every point `z` of the disc,
`‖deriv f z‖ / (1 - ‖f z‖ ^ 2) ≤ 1 / (1 - ‖z‖ ^ 2)`.

```lean
TauCeti.norm_deriv_div_one_sub_norm_sq_le {f : ℂ → ℂ} (hf : DifferentiableOn ℂ f (Metric.ball 0 1))
  (hmaps : Set.MapsTo f (Metric.ball 0 1) (Metric.ball 0 1)) {z : ℂ} (hz : z ∈ Metric.ball 0 1) :
  ‖deriv f z‖ / (1 - ‖f z‖ ^ 2) ≤ 1 / (1 - ‖z‖ ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_deriv_div_one_sub_norm_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzPick/Derivative.html#TauCeti.norm_deriv_div_one_sub_norm_sq_le).

## Sources

- [Tau Ceti documentation: `TauCeti.norm_deriv_div_one_sub_norm_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzPick/Derivative.html#TauCeti.norm_deriv_div_one_sub_norm_sq_le)
- [Source of `TauCeti.norm_deriv_div_one_sub_norm_sq_le` in TauCeti/Analysis/Complex/Conformal/SchwarzPick/Derivative.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/SchwarzPick/Derivative.lean#L97)
