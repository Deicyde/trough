---
declaration: theorem
origin: cited
lean: Matrix.IsHermitian.sum_sq_eigenvalues₀_sub_le_frobenius_norm_sub_sq
statement: formalized
proof: formalized
---

# The Hoffman–Wielandt inequality for Hermitian matrices

the squared Euclidean distance
between the decreasingly sorted spectra is at most the squared Frobenius norm `‖A - B‖_F²`.

```lean
Matrix.IsHermitian.sum_sq_eigenvalues₀_sub_le_frobenius_norm_sub_sq.{u_1, u_2} {n : Type u_1}
  {𝕜 : Type u_2} [Fintype n] [DecidableEq n] [RCLike 𝕜] {A B : Matrix n n 𝕜} (hA : A.IsHermitian)
  (hB : B.IsHermitian) : ∑ i, (hA.eigenvalues₀ i - hB.eigenvalues₀ i) ^ 2 ≤ ‖A - B‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hoffman–Wielandt inequality](../inner-product-space/part-01/the-hoffman-wielandt-inequality.md)

## Lean

Formalized in Tau Ceti as [`Matrix.IsHermitian.sum_sq_eigenvalues₀_sub_le_frobenius_norm_sub_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/HoffmanWielandt.html#Matrix.IsHermitian.sum_sq_eigenvalues%E2%82%80_sub_le_frobenius_norm_sub_sq).

## Sources

- [Tau Ceti documentation: `Matrix.IsHermitian.sum_sq_eigenvalues₀_sub_le_frobenius_norm_sub_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/HoffmanWielandt.html#Matrix.IsHermitian.sum_sq_eigenvalues%E2%82%80_sub_le_frobenius_norm_sub_sq)
- [Source of `Matrix.IsHermitian.sum_sq_eigenvalues₀_sub_le_frobenius_norm_sub_sq` in TauCeti/Analysis/Matrix/HoffmanWielandt.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Matrix/HoffmanWielandt.lean#L91)
