# Extension by continuity

If `i : α → β` is a dense inducing, then any function `f : α → γ` "extends" to a function `g =
IsDenseInducing.extend di f : β → γ`. If `γ` is Hausdorff and `f` has a continuous extension, then
`g` is the unique such extension. In general, `g` might not be continuous or even extend `f`.

```lean
IsDenseInducing.extend.{u_1, u_2, u_3} {α : Type u_1} {β : Type u_2} {γ : Type u_3}
  [TopologicalSpace α] [TopologicalSpace β] {i : α → β} [TopologicalSpace γ]
  (di : IsDenseInducing i) (f : α → γ) (b : β) : γ
```

## Depends on

- [Closure](closure.md)
- [Filter](filter.md)
- [Induced topology](induced-topology.md)

## Sources

- [Mathlib documentation: `IsDenseInducing.extend`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/DenseEmbedding.html#IsDenseInducing.extend)
- [Source of `IsDenseInducing.extend` in Mathlib/Topology/DenseEmbedding.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/DenseEmbedding.lean#L136)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L227)
