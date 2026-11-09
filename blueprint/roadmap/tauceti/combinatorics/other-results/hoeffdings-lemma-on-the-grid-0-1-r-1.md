---
declaration: theorem
origin: cited
lean: TauCeti.sum_range_exp_mul_div_sub_half_le
statement: formalized
proof: formalized
---

# Hoeffding's lemma on the grid `{0, 1 / r, …, 1}`

For `r ≠ 0` and every real `t`, the
exponential moment of the uniformly distributed centred point `k / r - 1 / 2` satisfies
`∑ k ∈ range (r + 1), exp (t (k / r - 1 / 2)) ≤ (r + 1) exp (t² / 8)`.

```lean
TauCeti.sum_range_exp_mul_div_sub_half_le {r : ℕ} (hr : r ≠ 0) (t : ℝ) :
  ∑ k ∈ Finset.range (r + 1), Real.exp (t * (↑k / ↑r - 1 / 2)) ≤ (↑r + 1) * Real.exp (t ^ 2 / 8)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_range_exp_mul_div_sub_half_le`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Enumerative/BoxLargeDeviation.html#TauCeti.sum_range_exp_mul_div_sub_half_le).

## Sources

- [Tau Ceti documentation: `TauCeti.sum_range_exp_mul_div_sub_half_le`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Enumerative/BoxLargeDeviation.html#TauCeti.sum_range_exp_mul_div_sub_half_le)
- [Source of `TauCeti.sum_range_exp_mul_div_sub_half_le` in TauCeti/Combinatorics/Enumerative/BoxLargeDeviation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Enumerative/BoxLargeDeviation.lean#L77)
