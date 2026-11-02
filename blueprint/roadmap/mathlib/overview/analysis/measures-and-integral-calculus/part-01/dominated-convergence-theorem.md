---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.tendsto_integral_of_dominated_convergence
mathlib_file: Mathlib/MeasureTheory/Integral/DominatedConvergence.lean
---

# Dominated convergence theorem

**Lebesgue dominated convergence theorem** provides sufficient conditions under which almost
everywhere convergence of a sequence of functions implies the convergence of their integrals.
We could weaken the condition `bound_integrable` to require `HasFiniteIntegral bound μ` instead
(i.e. not requiring that `bound` is measurable), but in all applications proving integrability
is easier.

```lean
MeasureTheory.tendsto_integral_of_dominated_convergence.{u_1, u_3} {α : Type u_1} {G : Type u_3}
  [NormedAddCommGroup G] [NormedSpace ℝ G] {m : MeasurableSpace α} {μ : MeasureTheory.Measure α}
  {F : ℕ → α → G} {f : α → G} (bound : α → ℝ)
  (F_measurable : ∀ (n : ℕ), MeasureTheory.AEStronglyMeasurable (F n) μ)
  (bound_integrable : MeasureTheory.Integrable bound μ)
  (h_bound : ∀ (n : ℕ), ∀ᵐ (a : α) ∂μ, ‖F n a‖ ≤ bound a)
  (h_lim : ∀ᵐ (a : α) ∂μ, Filter.Tendsto (fun n => F n a) Filter.atTop (nhds (f a))) :
  Filter.Tendsto (fun n => ∫ (a : α), F n a ∂μ) Filter.atTop (nhds (∫ (a : α), f a ∂μ))
```

## Depends on

- [Bochner integral](bochner-integral.md)

## Proof depends on

- [Ring structure $\Z$](../../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `MeasureTheory.tendsto_integral_of_dominated_convergence`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/DominatedConvergence.html#MeasureTheory.tendsto_integral_of_dominated_convergence)
- [Source of `MeasureTheory.tendsto_integral_of_dominated_convergence` in Mathlib/MeasureTheory/Integral/DominatedConvergence.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/DominatedConvergence.lean#L53)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L354)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L517)
- [1000+ theorems list: Q1067156](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1299)
- [1000+ theorems project: Q1067156](https://1000-plus.github.io/all.html?length=-1#Q1067156)
- [Wikipedia: Dominated convergence theorem](https://en.wikipedia.org/wiki/Dominated_convergence_theorem)
- [Wikidata: Q1067156](https://www.wikidata.org/wiki/Q1067156)
