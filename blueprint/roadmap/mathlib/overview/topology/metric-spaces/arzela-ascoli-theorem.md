# Arzela-Ascoli theorem

Third \(main\) version, with pointwise equicontinuity and range in a compact subset, but
without closedness. The closure is then compact.

```lean
BoundedContinuousFunction.arzela_ascoli.{u, v} {α : Type u} {β : Type v} [TopologicalSpace α]
  [CompactSpace α] [PseudoMetricSpace β] [T2Space β] (s : Set β) (hs : IsCompact s)
  (A : Set (BoundedContinuousFunction α β))
  (in_s : ∀ (f : BoundedContinuousFunction α β) (x : α), f ∈ A → f x ∈ s)
  (H : Equicontinuous fun x => ⇑↑x) : IsCompact (closure A)
```

## Depends on

- [Bornology](../../analysis/topological-vector-spaces/bornology.md)
- [Closure](../general-topology/part-01/closure.md)
- [Compactness in terms of filters](../general-topology/part-01/compactness-in-terms-of-filters.md)
- [Continuous function](../general-topology/part-01/continuous-function.md)
- [Hausdorff space](../general-topology/part-01/hausdorff-space.md)
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Proof depends on

- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Completeness of spaces of bounded continuous functions](../../analysis/normed-vector-spaces-banach-spaces/completeness-of-spaces-of-bounded-continuous-fun.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Lipschitz continuity](lipschitz-continuity.md)

## Sources

- [Mathlib documentation: `BoundedContinuousFunction.arzela_ascoli`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/ContinuousMap/Bounded/ArzelaAscoli.html#BoundedContinuousFunction.arzela_ascoli)
- [Source of `BoundedContinuousFunction.arzela_ascoli` in Mathlib/Topology/ContinuousMap/Bounded/ArzelaAscoli.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/ContinuousMap/Bounded/ArzelaAscoli.lean#L111)
- [Mathlib overview: Topology › Metric spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L268)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L436)
- [1000+ theorems list: Q1477053](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1722)
- [1000+ theorems project: Q1477053](https://1000-plus.github.io/all.html?length=-1#Q1477053)
- [Wikipedia: Arzelà–Ascoli theorem](https://en.wikipedia.org/wiki/Arzel%C3%A0%E2%80%93Ascoli_theorem)
- [Wikidata: Q1477053](https://www.wikidata.org/wiki/Q1477053)
