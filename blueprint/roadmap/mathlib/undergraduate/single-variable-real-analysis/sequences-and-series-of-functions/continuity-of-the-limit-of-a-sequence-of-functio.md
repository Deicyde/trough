---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: continuous_of_uniform_approx_of_continuous
mathlib_file: Mathlib/Topology/UniformSpace/UniformApproximation.lean
---

# Continuity of the limit of a sequence of functions

A function which can be uniformly approximated by continuous functions is continuous.

```lean
continuous_of_uniform_approx_of_continuous.{u_1, u_2} {α : Type u_1} {β : Type u_2}
  [TopologicalSpace α] [UniformSpace β] {f : α → β}
  (L : ∀ u ∈ uniformity β, ∃ F, Continuous F ∧ ∀ (y : α), (f y, F y) ∈ u) : Continuous f
```

## Depends on

- [Continuous function](../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Uniform space](../../../overview/topology/uniform-notions/uniform-space.md)

## Sources

- [Mathlib documentation: `continuous_of_uniform_approx_of_continuous`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/UniformSpace/UniformApproximation.html#continuous_of_uniform_approx_of_continuous)
- [Source of `continuous_of_uniform_approx_of_continuous` in Mathlib/Topology/UniformSpace/UniformApproximation.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/UniformSpace/UniformApproximation.lean#L88)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences and series of functions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L352)
