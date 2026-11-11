---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.sum_norm_smul_sub_apply_eigenvectorBasis_sq_le_four_mul_frobenius_sq
statement: formalized
proof: formalized
---

# The Frobenius upper residual bound

The residuals `Rⱼ = λⱼ(T) uⱼ - T uⱼ` of the
eigenvectors `uⱼ` of `S` satisfy `∑_{j ∈ s} ‖Rⱼ‖² ≤ 4 ‖S - T‖_F²` for every index block `s`.

```lean
LinearMap.IsSymmetric.sum_norm_smul_sub_apply_eigenvectorBasis_sq_le_four_mul_frobenius_sq.{u_1,
    u_2}
  {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] {T S : E →ₗ[𝕜] E} {n : ℕ} (hT : T.IsSymmetric) (hS : S.IsSymmetric)
  (hn : Module.finrank 𝕜 E = n) (s : Finset (Fin n)) :
  ∑ j ∈ s,
      ‖↑(hT.eigenvalues hn j) • (hS.eigenvectorBasis hn) j - T ((hS.eigenvectorBasis hn) j)‖ ^ 2 ≤
    4 * (TauCeti.UnitarilyInvariantSeminorm.frobenius 𝕜 E E) (S - T) ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hoffman–Wielandt inequality](the-hoffman-wielandt-inequality.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.IsSymmetric.sum_norm_smul_sub_apply_eigenvectorBasis_sq_le_four_mul_frobenius_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/Basic.html#LinearMap.IsSymmetric.sum_norm_smul_sub_apply_eigenvectorBasis_sq_le_four_mul_frobenius_sq).

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.sum_norm_smul_sub_apply_eigenvectorBasis_sq_le_four_mul_frobenius_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/Basic.html#LinearMap.IsSymmetric.sum_norm_smul_sub_apply_eigenvectorBasis_sq_le_four_mul_frobenius_sq)
- [Source of `LinearMap.IsSymmetric.sum_norm_smul_sub_apply_eigenvectorBasis_sq_le_four_mul_frobenius_sq` in TauCeti/Analysis/InnerProductSpace/YuWangSamworth/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/Basic.lean#L137)
