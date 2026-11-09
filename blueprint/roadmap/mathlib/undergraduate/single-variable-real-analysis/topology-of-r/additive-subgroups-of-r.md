# Additive subgroups of $\R$

An additive subgroup of an archimedean linear ordered additive commutative group `G`
with order topology either is dense in `G` or is a cyclic subgroup.

```lean
AddSubgroup.dense_or_isCyclic.{u_1} {G : Type u_1} [AddCommGroup G] [LinearOrder G]
  [IsOrderedAddMonoid G] [TopologicalSpace G] [OrderTopology G] [Archimedean G]
  (H : AddSubgroup G) : Dense ↑H ∨ IsAddCyclic ↥H
```

## Depends on

- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Integer](../../../overview/general-algebra/numbers/integer.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)

## Sources

- [Mathlib documentation: `AddSubgroup.dense_or_isCyclic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/Order/ArchimedeanDiscrete.html#AddSubgroup.dense_or_isCyclic)
- [Source of `AddSubgroup.dense_or_isCyclic` in Mathlib/Topology/Algebra/Order/ArchimedeanDiscrete.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Algebra/Order/ArchimedeanDiscrete.lean#L64)
- [Mathlib undergraduate list: Single Variable Real Analysis › Topology of R](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L295)
