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

- [Almost sure convergence](../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Giry monad](../../overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Integral of positive measurable functions](../../overview/analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Lebesgue measure (Measures and integral calculus)](../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Measurable function](../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Proof depends on

- [Bochner integral](../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Derivative at a point](../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Hausdorff space](../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Order topology](../../overview/topology/topological-algebra/order-topology.md)
- [Topological ring](../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `Theorems100.area_disc`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/AreaOfACircle.html#Theorems100.area_disc)
- [Source of `Theorems100.area_disc` in Archive/Wiedijk100Theorems/AreaOfACircle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/AreaOfACircle.lean#L84)
- [Freek Wiedijk's 100 theorems, no. 9](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L50)
