---
declaration: theorem
origin: cited
lean: Nat.sum_range_sub_ceilDiv
statement: formalized
proof: formalized
---

# Hermite's identity in truncated ceiling-division form

for `0 < n`, the ceilings of
`(r - i) / n` over a complete block `0 ≤ i < n` of shifts add up to `r`. The subtraction is
truncated, so the terms with `r ≤ i` vanish. Compare the floor form `Int.sum_range_add_ediv`.

```lean
Nat.sum_range_sub_ceilDiv (r : ℕ) {n : ℕ} (hn : 0 < n) : ∑ i ∈ Finset.range n, (r - i) ⌈/⌉ n = r
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Nat.sum_range_sub_ceilDiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Order/Floor/Div.html#Nat.sum_range_sub_ceilDiv).

## Sources

- [Tau Ceti documentation: `Nat.sum_range_sub_ceilDiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Order/Floor/Div.html#Nat.sum_range_sub_ceilDiv)
- [Source of `Nat.sum_range_sub_ceilDiv` in TauCeti/Algebra/Order/Floor/Div.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Order/Floor/Div.lean#L55)
