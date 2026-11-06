---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: integral_comp_polarCoord_symm
mathlib_file: Mathlib/Analysis/SpecialFunctions/PolarCoord.lean
---

# Change of variables to polar co-ordinates

Mathlib states this as `integral_comp_polarCoord_symm`.

```lean
integral_comp_polarCoord_symm.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  (f : ℝ × ℝ → E) :
  ∫ (p : ℝ × ℝ) in polarCoord.target, p.1 • f (↑polarCoord.symm p) = ∫ (p : ℝ × ℝ), f p
```

## Depends on

- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Inverse trigonometric functions](../../../overview/analysis/special-functions/inverse-trigonometric-functions.md)
- [Lebesgue measure (Measures and integral calculus)](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Proof depends on

- [Change of variables formula](../../../overview/analysis/measures-and-integral-calculus/part-02/change-of-variables-formula.md)
- [Derivative at a point](../../single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Derivative of a composition of functions (Analysis)](../../../overview/analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Giry monad](../../../overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Kernel of a linear map](../../linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Noetherian module](../../../overview/linear-algebra/fundamentals/noetherian-module.md)
- [Product of vector spaces](../../linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Sum of subspaces](../../linear-algebra/fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `integral_comp_polarCoord_symm`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/PolarCoord.html#integral_comp_polarCoord_symm)
- [Source of `integral_comp_polarCoord_symm` in Mathlib/Analysis/SpecialFunctions/PolarCoord.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/SpecialFunctions/PolarCoord.lean#L139)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L526)
