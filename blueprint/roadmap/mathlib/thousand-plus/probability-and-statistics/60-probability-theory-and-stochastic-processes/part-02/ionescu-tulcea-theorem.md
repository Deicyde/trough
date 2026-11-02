---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.Kernel.traj
mathlib_file: Mathlib/Probability/Kernel/IonescuTulcea/Traj.lean
---

# Ionescu-Tulcea theorem

*Ionescu-Tulcea Theorem* : Given a family of kernels `κ n` taking variables in `Iic n` with
value in `X (n + 1)`, the kernel `traj κ a` takes a variable `x` depending on the
variables `i ≤ a` and associates to it a kernel on trajectories depending on all variables,
where the entries with index `≤ a` are those of `x`, and then one follows iteratively the
kernels `κ a`, then `κ (a + 1)`, and so on.

The fact that such a kernel exists on infinite trajectories is not obvious, and is the content of
the Ionescu-Tulcea theorem.

```lean
ProbabilityTheory.Kernel.traj.{u_1} {X : ℕ → Type u_1} [(n : ℕ) → MeasurableSpace (X n)]
  (κ : (n : ℕ) → ProbabilityTheory.Kernel ((i : ↥(Finset.Iic n)) → X ↑i) (X (n + 1)))
  [∀ (n : ℕ), ProbabilityTheory.IsMarkovKernel (κ n)] (a : ℕ) :
  ProbabilityTheory.Kernel ((i : ↥(Finset.Iic a)) → X ↑i) ((n : ℕ) → X n)
```

## Depends on

- [Almost sure convergence](../../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Carathéodory's extension theorem](../../../analysis/28-measure-and-integration/part-01/caratheodorys-extension-theorem.md)
- [Giry monad](../../../../overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Integral of positive measurable functions](../../../../overview/analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Linear map](../../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Measurable function](../../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Probability measure](../../../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Product of sigma-algebras](../../../../undergraduate/measures-and-integral-calculus/measure-theory/product-of-sigma-algebras.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.Kernel.traj`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Kernel/IonescuTulcea/Traj.html#ProbabilityTheory.Kernel.traj)
- [Source of `ProbabilityTheory.Kernel.traj` in Mathlib/Probability/Kernel/IonescuTulcea/Traj.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Kernel/IonescuTulcea/Traj.lean#L511)
- [1000+ theorems list: Q25378690](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L4227)
- [1000+ theorems project: Q25378690](https://1000-plus.github.io/all.html?length=-1#Q25378690)
- [Wikipedia: Ionescu-Tulcea theorem](https://en.wikipedia.org/wiki/Ionescu-Tulcea_theorem)
- [Wikidata: Q25378690](https://www.wikidata.org/wiki/Q25378690)
