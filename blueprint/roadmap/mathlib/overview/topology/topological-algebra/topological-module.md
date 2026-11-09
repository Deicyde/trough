# Topological module

Class `ContinuousSMul M X` says that the scalar multiplication `(•) : M → X → X`
is continuous in both arguments. We use the same class for all kinds of multiplicative actions,
including (semi)modules and algebras.

```lean
ContinuousSMul.{u_1, u_2} (M : Type u_1) (X : Type u_2) [SMul M X] [TopologicalSpace M]
  [TopologicalSpace X] : Prop
```

## Depends on

- [Continuous function](../general-topology/part-01/continuous-function.md)

## Sources

- [Mathlib documentation: `ContinuousSMul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/MulAction.html#ContinuousSMul)
- [Source of `ContinuousSMul` in Mathlib/Topology/Algebra/MulAction.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Algebra/MulAction.lean#L40)
- [Mathlib overview: Topology › Topological algebra](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L256)
