---
declaration: theorem
origin: cited
lean: Chebyshev.abs_sum_primesLE_filter_gt_log_div_sub_log_div_le
statement: formalized
proof: formalized
---

# Interval form of Mertens' first theorem

For `1 ≤ y ≤ x`,
`|∑_{y < p ≤ x} log p / p - log (x / y)| ≤ 2 (log 4 + 4)`.

```lean
Chebyshev.abs_sum_primesLE_filter_gt_log_div_sub_log_div_le {y x : ℝ} (hy : 1 ≤ y) (hyx : y ≤ x) :
  |∑ p ∈ ⌊x⌋₊.primesLE with y < ↑p, Real.log ↑p / ↑p - Real.log (x / y)| ≤ 2 * (Real.log 4 + 4)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Mertens' first theorem](mertens-first-theorem.md)

## Lean

Formalized in Tau Ceti as [`Chebyshev.abs_sum_primesLE_filter_gt_log_div_sub_log_div_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/Mertens.html#Chebyshev.abs_sum_primesLE_filter_gt_log_div_sub_log_div_le).

## Sources

- [Tau Ceti documentation: `Chebyshev.abs_sum_primesLE_filter_gt_log_div_sub_log_div_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/Mertens.html#Chebyshev.abs_sum_primesLE_filter_gt_log_div_sub_log_div_le)
- [Source of `Chebyshev.abs_sum_primesLE_filter_gt_log_div_sub_log_div_le` in TauCeti/NumberTheory/Chebyshev/Mertens.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Chebyshev/Mertens.lean#L327)
