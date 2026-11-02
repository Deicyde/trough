---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: fderiv
mathlib_file: Mathlib/Analysis/Calculus/FDeriv/Defs.lean
---

# Differentials (linear tangent functions)

If `f` has a derivative at `x`, then `fderiv 𝕜 f x` is such a derivative. Otherwise, it is
set to `0`.

```lean
fderiv.{u_1, u_2, u_3} (𝕜 : Type u_1) [NontriviallyNormedField 𝕜] {E : Type u_2} [AddCommGroup E]
  [_root_.Module 𝕜 E] [TopologicalSpace E] {F : Type u_3} [AddCommGroup F] [_root_.Module 𝕜 F]
  [TopologicalSpace F] (f : E → F) (x : E) : E →L[𝕜] F
```

## Depends on

- [Continuous linear map](../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `fderiv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/FDeriv/Defs.html#fderiv)
- [Source of `fderiv` in Mathlib/Analysis/Calculus/FDeriv/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/FDeriv/Defs.lean#L160)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L456)
