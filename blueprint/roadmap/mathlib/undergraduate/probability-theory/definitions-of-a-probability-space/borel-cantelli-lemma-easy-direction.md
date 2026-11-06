# Borel-Cantelli lemma (easy direction)

One direction of the **Borel-Cantelli lemma**
(sometimes called the "*first* Borel-Cantelli lemma"):
if `(s i)` is a sequence of sets such that `∑' i, μ (s i)` is finite,
then the limit superior of the `s i` along the `atTop` filter is a null set.

Note: for the *second* Borel-Cantelli lemma (applying to independent sets in a probability space),
see `ProbabilityTheory.measure_limsup_eq_one`.

```lean
MeasureTheory.measure_limsup_atTop_eq_zero.{u_1, u_3} {α : Type u_1} {F : Type u_3}
  [FunLike F (Set α) ENNReal] [MeasureTheory.OuterMeasureClass F α] {μ : F} {s : ℕ → Set α}
  (hs : ∑' (i : ℕ), μ (s i) ≠ ⊤) : μ (Filter.limsup s Filter.atTop) = 0
```

## Depends on

- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Real number](../../../overview/general-algebra/numbers/real-number.md)

## Proof depends on

- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)

## Sources

- [Mathlib documentation: `MeasureTheory.measure_limsup_atTop_eq_zero`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/OuterMeasure/BorelCantelli.html#MeasureTheory.measure_limsup_atTop_eq_zero)
- [Source of `MeasureTheory.measure_limsup_atTop_eq_zero` in Mathlib/MeasureTheory/OuterMeasure/BorelCantelli.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/OuterMeasure/BorelCantelli.lean#L55)
- [Mathlib undergraduate list: Probability Theory › Definitions of a probability space](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L552)
