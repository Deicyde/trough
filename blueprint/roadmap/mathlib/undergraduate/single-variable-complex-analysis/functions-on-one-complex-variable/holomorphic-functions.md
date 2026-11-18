# Holomorphic functions

`DifferentiableOn 𝕜 f s` means that `f` is differentiable within `s` at any point of `s`.

```lean
DifferentiableOn.{u_1, u_2, u_3} (𝕜 : Type u_1) [NontriviallyNormedField 𝕜] {E : Type u_2}
  [AddCommGroup E] [_root_.Module 𝕜 E] [TopologicalSpace E] {F : Type u_3} [AddCommGroup F]
  [_root_.Module 𝕜 F] [TopologicalSpace F] (f : E → F) (s : Set E) : Prop
```

## Depends on

- [Continuous linear map](../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)

## Sources

- [Mathlib documentation: `DifferentiableOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/FDeriv/Defs.html#DifferentiableOn)
- [Source of `DifferentiableOn` in Mathlib/Analysis/Calculus/FDeriv/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Analysis/Calculus/FDeriv/Defs.lean#L164)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Functions on one complex variable](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L383)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L455)
