# Szpilrajn extension theorem

**Szpilrajn extension theorem**: any partial order can be extended to a linear order.

```lean
extend_partialOrder.{u} {α : Type u} (r : α → α → Prop) [IsPartialOrder α r] :
  ∃ s, IsLinearOrder α s ∧ r ≤ s
```

## Depends on

Its statement uses no other concept on these lists.

## Proof depends on

- [Set](../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `extend_partialOrder`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/Extension/Linear.html#extend_partialOrder)
- [Source of `extend_partialOrder` in Mathlib/Order/Extension/Linear.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Order/Extension/Linear.lean#L27)
- [1000+ theorems list: Q869647](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1019)
- [1000+ theorems project: Q869647](https://1000-plus.github.io/all.html?length=-1#Q869647)
- [Wikipedia: Szpilrajn extension theorem](https://en.wikipedia.org/wiki/Szpilrajn_extension_theorem)
- [Wikidata: Q869647](https://www.wikidata.org/wiki/Q869647)
