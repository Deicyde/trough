---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: TopologicalSpace.metrizableSpace_of_t3_secondCountable
mathlib_file: Mathlib/Topology/Metrizable/Urysohn.lean
---

# Metrization theorems

*Urysohn's metrization theorem* (Tychonoff's version): a T₃ topological space with second
countable topology `X` is metrizable, i.e., there exists a metric space structure that generates the
same topology.

```lean
TopologicalSpace.metrizableSpace_of_t3_secondCountable.{u_1} (X : Type u_1) [TopologicalSpace X]
  [T3Space X] [SecondCountableTopology X] : TopologicalSpace.MetrizableSpace X
```

Urysohn's metrization theorem (only).

## Depends on

- [Natural number](../../../../overview/general-algebra/numbers/natural-number.md)
- [Uniform space](../../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Ball](../../../../overview/topology/metric-spaces/ball.md)
- [Infinite sum](../../../../overview/topology/topological-algebra/infinite-sum.md)
- [Urysohn's lemma](../../../../overview/topology/general-topology/part-02/urysohns-lemma.md)

## Sources

- [Mathlib documentation: `TopologicalSpace.metrizableSpace_of_t3_secondCountable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Metrizable/Urysohn.html#TopologicalSpace.metrizableSpace_of_t3_secondCountable)
- [Source of `TopologicalSpace.metrizableSpace_of_t3_secondCountable` in Mathlib/Topology/Metrizable/Urysohn.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Metrizable/Urysohn.lean#L125)
- [1000+ theorems list: Q1194053](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1518)
- [1000+ theorems project: Q1194053](https://1000-plus.github.io/all.html?length=-1#Q1194053)
- [Wikipedia: Metrization theorems](https://en.wikipedia.org/wiki/Metrization_theorems)
- [Wikidata: Q1194053](https://www.wikidata.org/wiki/Q1194053)
