---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: ContinuousSMul
mathlib_file: Mathlib/Topology/Algebra/MulAction.lean
---

# Topological module

Class `ContinuousSMul M X` says that the scalar multiplication `(•) : M → X → X`
is continuous in both arguments. We use the same class for all kinds of multiplicative actions,
including (semi)modules and algebras.

```lean
ContinuousSMul.{u_1, u_2} (M : Type u_1) (X : Type u_2) [SMul M X] [TopologicalSpace M]
  [TopologicalSpace X] : Prop
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Continuous function](../general-topology/part-01/continuous-function.md)
- [Induced topology](../general-topology/part-01/induced-topology.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `ContinuousSMul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/MulAction.html#ContinuousSMul)
- [Source of `ContinuousSMul` in Mathlib/Topology/Algebra/MulAction.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Algebra/MulAction.lean#L40)
- [Mathlib overview: Topology › Topological algebra](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L256)
