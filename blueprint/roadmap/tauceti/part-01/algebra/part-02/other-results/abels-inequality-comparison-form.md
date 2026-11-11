---
declaration: theorem
origin: cited
lean: TauCeti.sum_range_smul_le_sum_range_smul
statement: formalized
proof: formalized
---

# Abel's inequality, comparison form

If the partial sums of `f` are dominated by those of
`g` up to `N`, and `w` is nonnegative and antitone on the first `N` indices, then
`∑_{i < N} w i • f i ≤ ∑_{i < N} w i • g i`. Only the last weight is required
to be nonnegative explicitly; the other signs follow from the successive comparisons
when `N > 0`.

```lean
TauCeti.sum_range_smul_le_sum_range_smul.{u_1, u_2} {R : Type u_1} {M : Type u_2} [Ring R]
  [Preorder R] [IsOrderedAddMonoid R] [AddCommGroup M] [Preorder M] [IsOrderedAddMonoid M]
  [_root_.Module R M] [PosSMulMono R M] {f g : ℕ → M} {w : ℕ → R} {N : ℕ}
  (hfg : ∀ k ≤ N, ∑ i ∈ Finset.range k, f i ≤ ∑ i ∈ Finset.range k, g i)
  (hw : ∀ (i : ℕ), i + 1 < N → w (i + 1) ≤ w i) (hw0 : 0 ≤ w (N - 1)) :
  ∑ i ∈ Finset.range N, w i • f i ≤ ∑ i ∈ Finset.range N, w i • g i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_range_smul_le_sum_range_smul`](https://taucetiproject.org/docs/TauCeti/Algebra/Order/BigOperators/Sum/ByParts.html#TauCeti.sum_range_smul_le_sum_range_smul).

## Sources

- [Tau Ceti documentation: `TauCeti.sum_range_smul_le_sum_range_smul`](https://taucetiproject.org/docs/TauCeti/Algebra/Order/BigOperators/Sum/ByParts.html#TauCeti.sum_range_smul_le_sum_range_smul)
- [Source of `TauCeti.sum_range_smul_le_sum_range_smul` in TauCeti/Algebra/Order/BigOperators/Sum/ByParts.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Order/BigOperators/Sum/ByParts.lean#L66)
