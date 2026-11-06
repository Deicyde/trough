# Stieltjes measure

The measure associated to a Stieltjes function, giving mass `f b - f a` to the
interval `(a, b]`. If there is a bot element, it gives zero mass to it.

```lean
StieltjesFunction.measure.{u_1} {R : Type u_1} [LinearOrder R] [TopologicalSpace R]
  (f : StieltjesFunction R) [OrderTopology R] [CompactIccSpace R] [MeasurableSpace R] [BorelSpace R]
  [SecondCountableTopology R] [DenselyOrdered R] : MeasureTheory.Measure R
```

## Depends on

- [Borel sigma-algebra](borel-sigma-algebra.md)
- [Bornology](../../topological-vector-spaces/bornology.md)
- [Compactness in terms of filters](../../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Order](../../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Order topology](../../../topology/topological-algebra/order-topology.md)
- [Positive measure](positive-measure.md)

## Sources

- [Mathlib documentation: `StieltjesFunction.measure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Stieltjes.html#StieltjesFunction.measure)
- [Source of `StieltjesFunction.measure` in Mathlib/MeasureTheory/Measure/Stieltjes.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/Stieltjes.lean#L518)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L342)
