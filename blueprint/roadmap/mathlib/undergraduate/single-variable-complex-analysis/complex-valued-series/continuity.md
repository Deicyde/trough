---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: HasFPowerSeriesOnBall.continuousOn
mathlib_file: Mathlib/Analysis/Analytic/Basic.lean
---

# Continuity (Complex-valued series)

If a function admits a power series expansion on a ball, then it is continuous there.

```lean
HasFPowerSeriesOnBall.continuousOn.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3}
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] {f : E → F} {p : FormalMultilinearSeries 𝕜 E F} {x : E} {r : ENNReal}
  (hf : HasFPowerSeriesOnBall f p x r) : ContinuousOn f (Metric.eball x r)
```

## Depends on

- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Radius of convergence](radius-of-convergence.md)

## Proof depends on

- [Ball](../../../overview/topology/metric-spaces/ball.md)
- [Field $\R$ of real numbers](../../ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `HasFPowerSeriesOnBall.continuousOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Analytic/Basic.html#HasFPowerSeriesOnBall.continuousOn)
- [Source of `HasFPowerSeriesOnBall.continuousOn` in Mathlib/Analysis/Analytic/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Analytic/Basic.lean#L1005)
- [Mathlib undergraduate list: Single Variable Complex Analysis › Complex-valued series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L371)
