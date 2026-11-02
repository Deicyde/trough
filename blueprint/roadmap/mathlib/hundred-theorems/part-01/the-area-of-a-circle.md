---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Theorems100.area_disc
mathlib_file: Archive/Wiedijk100Theorems/AreaOfACircle.lean
---

# The Area of a Circle

**Area of a Circle**: The area of a disc with radius `r` is `π * r ^ 2`.

```lean
Theorems100.area_disc (r : NNReal) :
  MeasureTheory.volume (Theorems100.disc ↑r) = ↑NNReal.pi * ↑r ^ 2
```

## Depends on

- [Cos (extension of trigonometric functions to the complex plane)](../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Lebesgue measure (Measures and integral calculus)](../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Continuity of monotone functions](../../undergraduate/single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of-r/continuity-of-monotone-functions.md)
- [Derivative at a point](../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Fundamental theorem of calculus, part 2](../../overview/analysis/measures-and-integral-calculus/part-01/fundamental-theorem-of-calculus-part-2.md)
- [Giry monad](../../overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Hausdorff space](../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Inverse trigonometric functions](../../overview/analysis/special-functions/inverse-trigonometric-functions.md)

## Sources

- [Mathlib documentation: `Theorems100.area_disc`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/AreaOfACircle.html#Theorems100.area_disc)
- [Source of `Theorems100.area_disc` in Archive/Wiedijk100Theorems/AreaOfACircle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/AreaOfACircle.lean#L84)
- [Freek Wiedijk's 100 theorems, no. 9](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L50)
