---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.sum_sq_eigenvalues_sub_le_sum_sq_norm_apply
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

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.sum_sq_eigenvalues_sub_le_sum_sq_norm_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Basic.html#LinearMap.IsSymmetric.sum_sq_eigenvalues_sub_le_sum_sq_norm_apply)
- [Source of `LinearMap.IsSymmetric.sum_sq_eigenvalues_sub_le_sum_sq_norm_apply` in TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Basic.lean#L88)
