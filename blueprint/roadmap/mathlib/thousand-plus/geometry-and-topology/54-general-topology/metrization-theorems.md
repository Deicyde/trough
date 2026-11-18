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

- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)
- [Uniform space](../../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Induced topology](../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Urysohn's lemma](../../../overview/topology/general-topology/part-02/urysohns-lemma.md)

## Sources

- [Mathlib documentation: `TopologicalSpace.metrizableSpace_of_t3_secondCountable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Metrizable/Urysohn.html#TopologicalSpace.metrizableSpace_of_t3_secondCountable)
- [Source of `TopologicalSpace.metrizableSpace_of_t3_secondCountable` in Mathlib/Topology/Metrizable/Urysohn.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Topology/Metrizable/Urysohn.lean#L125)
- [1000+ theorems list: Q1194053](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/1000.yaml#L1521)
- [1000+ theorems project: Q1194053](https://1000-plus.github.io/all.html?length=-1#Q1194053)
- [Wikipedia: Metrization theorems](https://en.wikipedia.org/wiki/Metrization_theorems)
- [Wikidata: Q1194053](https://www.wikidata.org/wiki/Q1194053)
