---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Summable.of_norm
mathlib_file: Mathlib/Analysis/Normed/Group/InfiniteSum.lean
---

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
- [Order (Real numbers)](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Proof depends on

- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Metric space](../../topology/metric-spaces/metric-space.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)

## Sources

- [Mathlib documentation: `Summable.of_norm`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Group/InfiniteSum.html#Summable.of_norm)
- [Source of `Summable.of_norm` in Mathlib/Analysis/Normed/Group/InfiniteSum.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Group/InfiniteSum.lean#L194)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L287)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L428)
