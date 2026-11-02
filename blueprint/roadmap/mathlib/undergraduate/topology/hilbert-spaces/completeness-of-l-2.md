---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: lp.completeSpace
mathlib_file: Mathlib/Analysis/Normed/Lp/lpSpace.lean
---

# Completeness of $l^2$

Mathlib states this as `lp.completeSpace`.

```lean
lp.completeSpace.{u_3, u_4} {α : Type u_3} {E : α → Type u_4} {p : ENNReal}
  [(i : α) → NormedAddCommGroup (E i)] [_i : Fact (1 ≤ p)] [∀ (a : α), CompleteSpace (E a)] :
  CompleteSpace ↥(lp E p)
```

## Depends on

- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Induced topology](../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Metric structure](../../single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Module](../../../overview/linear-algebra/fundamentals/module.md)
- [Power functions](../../single-variable-real-analysis/elementary-functions-trigonometric-rational-etc/power-functions.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure.md)

## Proof depends on

- [Arithmetic Mean/Geometric Mean](../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Continuity of monotone functions](../../single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of/continuity-of-monotone-functions.md)
- [Pointwise convergence](../../single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)

## Sources

- [Mathlib documentation: `lp.completeSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Lp/lpSpace.html#lp.completeSpace)
- [Source of `lp.completeSpace` in Mathlib/Analysis/Normed/Lp/lpSpace.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Lp/lpSpace.lean#L1357)
- [Mathlib undergraduate list: Topology › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L443)
