---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: norm_add_le
mathlib_file: Mathlib/Analysis/Normed/Group/Basic.lean
---

# The Triangle Inequality

**Triangle inequality** for the norm.

```lean
norm_add_le.{u_4} {E : Type u_4} [SeminormedAddGroup E] (a b : E) : ‖a + b‖ ≤ ‖a‖ + ‖b‖
```

## Depends on

- [Bornology](../../overview/analysis/topological-vector-spaces/bornology.md)
- [Order (Real numbers)](../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Uniform space](../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)
- [Permutation group of a type](../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Product of rings](../../undergraduate/ring-theory/fundamentals/product-of-rings.md)
- [Ring structure $\Z$](../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `norm_add_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Group/Basic.html#norm_add_le)
- [Source of `norm_add_le` in Mathlib/Analysis/Normed/Group/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Group/Basic.lean#L101)
- [Freek Wiedijk's 100 theorems, no. 91](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L468)
