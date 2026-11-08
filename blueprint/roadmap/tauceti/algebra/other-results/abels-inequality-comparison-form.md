---
declaration: theorem
origin: cited
lean: TauCeti.sum_range_mul_le_sum_range_mul
statement: formalized
proof: formalized
---

# Abel's inequality, comparison form

If the partial sums of `f` are dominated by those of
`g` up to `N`, and `w` is nonnegative and antitone on the first `N` indices, then
`∑_{i < N} w i * f i ≤ ∑_{i < N} w i * g i`. Only the last weight is required
to be nonnegative explicitly; the other signs follow from the successive comparisons
when `N > 0`.

```lean
TauCeti.sum_range_mul_le_sum_range_mul.{u_1} {R : Type u_1} [Ring R] [Preorder R]
  [IsOrderedAddMonoid R] [PosMulMono R] {f g w : ℕ → R} {N : ℕ}
  (hfg : ∀ k ≤ N, ∑ i ∈ Finset.range k, f i ≤ ∑ i ∈ Finset.range k, g i)
  (hw : ∀ (i : ℕ), i + 1 < N → w (i + 1) ≤ w i) (hw0 : 0 ≤ w (N - 1)) :
  ∑ i ∈ Finset.range N, w i * f i ≤ ∑ i ∈ Finset.range N, w i * g i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_range_mul_le_sum_range_mul`](https://taucetiproject.org/docs/TauCeti/Algebra/Order/BigOperators/Sum/ByParts.html#TauCeti.sum_range_mul_le_sum_range_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.sum_range_mul_le_sum_range_mul`](https://taucetiproject.org/docs/TauCeti/Algebra/Order/BigOperators/Sum/ByParts.html#TauCeti.sum_range_mul_le_sum_range_mul)
- [Source of `TauCeti.sum_range_mul_le_sum_range_mul` in TauCeti/Algebra/Order/BigOperators/Sum/ByParts.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Order/BigOperators/Sum/ByParts.lean#L51)
