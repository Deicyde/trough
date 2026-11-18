# Cantor's isomorphism theorem

Any two countable dense, nonempty linear orders without endpoints are order isomorphic. This is
also known as **Cantor's isomorphism theorem**.

```lean
Order.iso_of_countable_dense.{u_1, u_2} (α : Type u_1) (β : Type u_2) [LinearOrder α]
  [LinearOrder β] [Countable α] [DenselyOrdered α] [NoMinOrder α] [NoMaxOrder α] [Nonempty α]
  [Countable β] [DenselyOrdered β] [NoMinOrder β] [NoMaxOrder β] [Nonempty β] : Nonempty (α ≃o β)
```

## Depends on

- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)

## Proof depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)

## Sources

- [Mathlib documentation: `Order.iso_of_countable_dense`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/CountableDenseLinearOrder.html#Order.iso_of_countable_dense)
- [Source of `Order.iso_of_countable_dense` in Mathlib/Order/CountableDenseLinearOrder.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Order/CountableDenseLinearOrder.lean#L244)
- [1000+ theorems list: Q107710112](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/1000.yaml#L4295)
- [1000+ theorems project: Q107710112](https://1000-plus.github.io/all.html?length=-1#Q107710112)
- [Wikipedia: Cantor's isomorphism theorem](https://en.wikipedia.org/wiki/Cantor's_isomorphism_theorem)
- [Wikidata: Q107710112](https://www.wikidata.org/wiki/Q107710112)
