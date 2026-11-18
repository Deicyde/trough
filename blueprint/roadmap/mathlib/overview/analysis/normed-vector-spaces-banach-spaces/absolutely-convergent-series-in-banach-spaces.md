# Absolutely convergent series in Banach spaces

Mathlib states this as `Summable.of_norm`.

```lean
Summable.of_norm.{u_1, u_3} {ι : Type u_1} {E : Type u_3} [SeminormedAddCommGroup E]
  [CompleteSpace E] {f : ι → E} (hf : Summable fun a => ‖f a‖) : Summable f
```

## Depends on

- [Bornology](../topological-vector-spaces/bornology.md)
- [Completeness](../../topology/uniform-notions/completeness.md)
- [Infinite sum](../../topology/topological-algebra/infinite-sum.md)
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Proof depends on

- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Metric space](../../topology/metric-spaces/metric-space.md)
- [The Triangle Inequality](../../../hundred-theorems/part-04/the-triangle-inequality.md)

## Sources

- [Mathlib documentation: `Summable.of_norm`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Group/InfiniteSum.html#Summable.of_norm)
- [Source of `Summable.of_norm` in Mathlib/Analysis/Normed/Group/InfiniteSum.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Analysis/Normed/Group/InfiniteSum.lean#L215)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L287)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L428)
