---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: DifferentiableOn
mathlib_file: Mathlib/Analysis/Calculus/FDeriv/Defs.lean
---

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
- [Source of `DifferentiableOn` in Mathlib/Analysis/Calculus/FDeriv/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/FDeriv/Defs.lean#L165)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Functions on one complex variable](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L383)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L455)
