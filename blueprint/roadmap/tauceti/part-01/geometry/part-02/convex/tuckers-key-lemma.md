---
declaration: theorem
origin: cited
lean: TauCeti.exists_nonneg_sum_smul_eq_zero_and_coeff_add_dual_pos_at
statement: formalized
proof: formalized
---

# Tucker's key lemma

For a finite family of vectors `a j` and an index `k`, there are a
nonnegative linear relation `x` among the `a j` and a linear functional `y` that is nonnegative on
every `a j`, such that `x k + y (a k) > 0`: either `a k` occurs in a nonnegative relation, or some
functional nonnegative on the family is strictly positive on `a k`.

```lean
TauCeti.exists_nonneg_sum_smul_eq_zero_and_coeff_add_dual_pos_at.{u_1, u_2, u_3} {ι : Type u_1}
  {K : Type u_2} {V : Type u_3} [Field K] [LinearOrder K] [IsStrictOrderedRing K] [AddCommGroup V]
  [_root_.Module K V] [Fintype ι] (a : ι → V) (k : ι) :
  ∃ x y, 0 ≤ x ∧ ∑ j, x j • a j = 0 ∧ (∀ (j : ι), 0 ≤ y (a j)) ∧ 0 < x k + y (a k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_nonneg_sum_smul_eq_zero_and_coeff_add_dual_pos_at`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/Cone/Alternative.html#TauCeti.exists_nonneg_sum_smul_eq_zero_and_coeff_add_dual_pos_at).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_nonneg_sum_smul_eq_zero_and_coeff_add_dual_pos_at`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/Cone/Alternative.html#TauCeti.exists_nonneg_sum_smul_eq_zero_and_coeff_add_dual_pos_at)
- [Source of `TauCeti.exists_nonneg_sum_smul_eq_zero_and_coeff_add_dual_pos_at` in TauCeti/Geometry/Convex/Cone/Alternative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Convex/Cone/Alternative.lean#L130)
