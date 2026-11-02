---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Theorems100.birthday, Theorems100.birthday_measure
mathlib_file: Archive/Wiedijk100Theorems/BirthdayProblem.lean
---

# The Birthday Problem

Mathlib records this with 2 declarations.

`Theorems100.birthday`: **Birthday Problem**: set cardinality interpretation.

```lean
Theorems100.birthday :
  2 * Fintype.card (Fin 23 ↪ Fin 365) < Fintype.card (Fin 23 → Fin 365) ∧
    2 * Fintype.card (Fin 22 ↪ Fin 365) > Fintype.card (Fin 22 → Fin 365)
```

`Theorems100.birthday_measure`: **Birthday Problem**: first probabilistic interpretation.

```lean
Theorems100.birthday_measure : MeasureTheory.volume {f | Function.Injective f} < 1 / 2
```

## Depends on

- [Conditional probability](../../overview/probability-theory/definitions-in-probability-theory/conditional-probability.md)
- [Counting measure](../../undergraduate/measures-and-integral-calculus/measure-theory/counting-measure.md)
- [Lebesgue measure](../../undergraduate/measures-and-integral-calculus/measure-theory/lebesgue-measure.md)
- [Product of sigma-algebras](../../undergraduate/measures-and-integral-calculus/measure-theory/product-of-sigma-algebras.md)

## Proof depends on

- [Almost sure convergence](../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Cantor’s Theorem](../part-04/cantors-theorem.md)
- [Cardinal](../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Closure](../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../overview/topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Continuity of monotone functions](../../undergraduate/single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of/continuity-of-monotone-functions.md)
- [Hausdorff space](../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Measurable function](../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Open map](../../overview/topology/general-topology/part-01/open-map.md)
- [Schroeder-Bernstein Theorem](../part-02/schroeder-bernstein-theorem.md)
- [Topological module](../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../overview/topology/topological-algebra/topological-ring.md)
- [Uniformly continuous function](../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `Theorems100.birthday`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/BirthdayProblem.html#Theorems100.birthday)
- [Source of `Theorems100.birthday` in Archive/Wiedijk100Theorems/BirthdayProblem.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/BirthdayProblem.lean#L29)
- [Mathlib documentation: `Theorems100.birthday_measure`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/BirthdayProblem.html#Theorems100.birthday_measure)
- [Source of `Theorems100.birthday_measure` in Archive/Wiedijk100Theorems/BirthdayProblem.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/BirthdayProblem.lean#L48)
- [Freek Wiedijk's 100 theorems, no. 93](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L478)
