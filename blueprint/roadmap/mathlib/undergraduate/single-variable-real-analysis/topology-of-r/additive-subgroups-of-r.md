---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: AddSubgroup.dense_or_isCyclic
mathlib_file: Mathlib/Topology/Algebra/Order/ArchimedeanDiscrete.lean
---

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

## Proof depends on

- [Filter](../../../overview/topology/general-topology/part-01/filter.md)
- [List](../../../overview/data-structures/list-like-structures/list.md)
- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `AddSubgroup.dense_or_isCyclic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/Order/ArchimedeanDiscrete.html#AddSubgroup.dense_or_isCyclic)
- [Source of `AddSubgroup.dense_or_isCyclic` in Mathlib/Topology/Algebra/Order/ArchimedeanDiscrete.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Algebra/Order/ArchimedeanDiscrete.lean#L64)
- [Mathlib undergraduate list: Single Variable Real Analysis › Topology of R](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L295)
