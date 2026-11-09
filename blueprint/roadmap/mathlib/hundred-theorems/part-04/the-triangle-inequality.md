# The Triangle Inequality

**Triangle inequality** for the norm.

```lean
norm_add_le.{u_4} {E : Type u_4} [SeminormedAddGroup E] (a b : E) : ‖a + b‖ ≤ ‖a‖ + ‖b‖
```

## Depends on

- [Bornology](../../overview/analysis/topological-vector-spaces/bornology.md)
- [Order](../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Sources

- [Mathlib documentation: `norm_add_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Group/Basic.html#norm_add_le)
- [Source of `norm_add_le` in Mathlib/Analysis/Normed/Group/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Normed/Group/Basic.lean#L101)
- [Freek Wiedijk's 100 theorems, no. 91](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L468)
