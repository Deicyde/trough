---
declaration: theorem
origin: cited
lean: TauCeti.exists_nonneg_sum_smul_eq_zero_and_forall_coeff_add_dual_pos, TauCeti.exists_nat_sum_nsmul_eq_zero_and_forall_coeff_add_dual_pos
statement: formalized
proof: formalized
---

# Tucker's theorem

For a finite family of vectors `a j` there are a nonnegative linear
relation `x` among the `a j` and a linear functional `y` that is nonnegative on every `a j`, such
that `x j + y (a j) > 0` for every `j`: each vector either occurs in the relation or is strictly
positive under `y`.

```lean
TauCeti.exists_nonneg_sum_smul_eq_zero_and_forall_coeff_add_dual_pos.{u_1, u_2, u_3} {ι : Type u_1}
  {K : Type u_2} {V : Type u_3} [Field K] [LinearOrder K] [IsStrictOrderedRing K] [AddCommGroup V]
  [_root_.Module K V] [Fintype ι] (a : ι → V) :
  ∃ x y, 0 ≤ x ∧ ∑ j, x j • a j = 0 ∧ (∀ (j : ι), 0 ≤ y (a j)) ∧ ∀ (j : ι), 0 < x j + y (a j)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Tucker's key lemma](tuckers-key-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_nonneg_sum_smul_eq_zero_and_forall_coeff_add_dual_pos`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/Cone/Alternative.html#TauCeti.exists_nonneg_sum_smul_eq_zero_and_forall_coeff_add_dual_pos).

## Other forms

**Tucker's theorem over the integers.** Formalized in Tau Ceti as [`TauCeti.exists_nat_sum_nsmul_eq_zero_and_forall_coeff_add_dual_pos`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/Cone/Alternative.html#TauCeti.exists_nat_sum_nsmul_eq_zero_and_forall_coeff_add_dual_pos).

```lean
TauCeti.exists_nat_sum_nsmul_eq_zero_and_forall_coeff_add_dual_pos.{u_1, u_4} {ι : Type u_1}
  {N : Type u_4} [AddCommGroup N] [Module.Free ℤ N] [Module.Finite ℤ N] [Fintype ι] (a : ι → N) :
  ∃ x m, ∑ j, x j • a j = 0 ∧ (∀ (j : ι), 0 ≤ m (a j)) ∧ ∀ (j : ι), 0 < ↑(x j) + m (a j)
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_nonneg_sum_smul_eq_zero_and_forall_coeff_add_dual_pos`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/Cone/Alternative.html#TauCeti.exists_nonneg_sum_smul_eq_zero_and_forall_coeff_add_dual_pos)
- [Source of `TauCeti.exists_nonneg_sum_smul_eq_zero_and_forall_coeff_add_dual_pos` in TauCeti/Geometry/Convex/Cone/Alternative.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Convex/Cone/Alternative.lean#L145)
