# Sum of an arithmetic series

Gauss' summation formula

```lean
Finset.sum_range_id (n : ℕ) : ∑ i ∈ Finset.range n, i = n * (n - 1) / 2
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Natural number](../../overview/general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Finset.sum_range_id`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/BigOperators/Intervals.html#Finset.sum_range_id)
- [Source of `Finset.sum_range_id` in Mathlib/Algebra/BigOperators/Intervals.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/BigOperators/Intervals.lean#L184)
- [Freek Wiedijk's 100 theorems, no. 68](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L343)
