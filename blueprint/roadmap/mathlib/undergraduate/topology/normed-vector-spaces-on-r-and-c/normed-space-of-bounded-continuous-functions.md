# Normed space of bounded continuous functions

Mathlib states this as `BoundedContinuousFunction.instNormedSpace`.

```lean
BoundedContinuousFunction.instNormedSpace.{u, v, u_1} {α : Type u} {β : Type v} {𝕜 : Type u_1}
  [TopologicalSpace α] [SeminormedAddCommGroup β] [NormedField 𝕜] [NormedSpace 𝕜 β] :
  NormedSpace 𝕜 (BoundedContinuousFunction α β)
```

## Depends on

- [Continuous function](../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Sources

- [Mathlib documentation: `BoundedContinuousFunction.instNormedSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/ContinuousMap/Bounded/Normed.html#BoundedContinuousFunction.instNormedSpace)
- [Source of `BoundedContinuousFunction.instNormedSpace` in Mathlib/Topology/ContinuousMap/Bounded/Normed.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/ContinuousMap/Bounded/Normed.lean#L272)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L432)
