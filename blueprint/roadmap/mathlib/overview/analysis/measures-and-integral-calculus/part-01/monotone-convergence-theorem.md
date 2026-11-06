# Monotone convergence theorem (Measures and integral calculus)

**Monotone convergence theorem** for nonincreasing sequences of functions.

```lean
MeasureTheory.lintegral_iInf_ae.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} {f : ℕ → α → ENNReal} (h_meas : ∀ (n : ℕ), Measurable (f n))
  (h_mono : ∀ (n : ℕ), f n.succ ≤ᵐ[μ] f n) (h_fin : ∫⁻ (a : α), f 0 a ∂μ ≠ ⊤) :
  ∫⁻ (a : α), ⨅ n, f n a ∂μ = ⨅ n, ∫⁻ (a : α), f n a ∂μ
```

## Depends on

- [Almost sure convergence](../../../probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Integral of positive measurable functions](integral-of-positive-measurable-functions.md)
- [Measurable function](measurable-function.md)

## Proof depends on

- [Borel sigma-algebra](borel-sigma-algebra.md)
- [Order topology](../../../topology/topological-algebra/order-topology.md)

## Sources

- [Mathlib documentation: `MeasureTheory.lintegral_iInf_ae`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Lebesgue/Sub.html#MeasureTheory.lintegral_iInf_ae)
- [Source of `MeasureTheory.lintegral_iInf_ae` in Mathlib/MeasureTheory/Integral/Lebesgue/Sub.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/Lebesgue/Sub.lean#L55)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L348)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L514)
