---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.sum_sq_eigenvalues_sub_le_sum_sq_norm_apply, Matrix.IsHermitian.sum_sq_eigenvalues₀_sub_le_frobenius_norm_sub_sq
statement: formalized
proof: formalized
---

# The Hoffman–Wielandt inequality

For symmetric `T` and `S` with eigenvalues listed in
decreasing order and every orthonormal basis `e`, the squared Euclidean distance between the two
spectra is at most the squared Frobenius distance `∑ₖ ‖T eₖ - S eₖ‖²` between the operators.

```lean
LinearMap.IsSymmetric.sum_sq_eigenvalues_sub_le_sum_sq_norm_apply.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {ι : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] [Fintype ι] {T S : E →ₗ[𝕜] E} {n : ℕ} (hT : T.IsSymmetric)
  (hS : S.IsSymmetric) (hn : Module.finrank 𝕜 E = n) (e : OrthonormalBasis ι 𝕜 E) :
  ∑ i, (hT.eigenvalues hn i - hS.eigenvalues hn i) ^ 2 ≤ ∑ k, ‖T (e k) - S (e k)‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.IsSymmetric.sum_sq_eigenvalues_sub_le_sum_sq_norm_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Basic.html#LinearMap.IsSymmetric.sum_sq_eigenvalues_sub_le_sum_sq_norm_apply).

## Other forms

**The Hoffman–Wielandt inequality for Hermitian matrices.** Formalized in Tau Ceti as [`Matrix.IsHermitian.sum_sq_eigenvalues₀_sub_le_frobenius_norm_sub_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/HoffmanWielandt.html#Matrix.IsHermitian.sum_sq_eigenvalues%E2%82%80_sub_le_frobenius_norm_sub_sq).

```lean
Matrix.IsHermitian.sum_sq_eigenvalues₀_sub_le_frobenius_norm_sub_sq.{u_1, u_2} {n : Type u_1}
  {𝕜 : Type u_2} [Fintype n] [DecidableEq n] [RCLike 𝕜] {A B : Matrix n n 𝕜} (hA : A.IsHermitian)
  (hB : B.IsHermitian) : ∑ i, (hA.eigenvalues₀ i - hB.eigenvalues₀ i) ^ 2 ≤ ‖A - B‖ ^ 2
```

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.sum_sq_eigenvalues_sub_le_sum_sq_norm_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Basic.html#LinearMap.IsSymmetric.sum_sq_eigenvalues_sub_le_sum_sq_norm_apply)
- [Source of `LinearMap.IsSymmetric.sum_sq_eigenvalues_sub_le_sum_sq_norm_apply` in TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Basic.lean#L88)
