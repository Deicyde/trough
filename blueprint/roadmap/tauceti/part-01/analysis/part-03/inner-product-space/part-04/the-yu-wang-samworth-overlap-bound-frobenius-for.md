---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.sq_mul_sum_sum_norm_inner_sq_le_four_mul_frobenius_sq, LinearMap.IsSymmetric.sq_mul_sum_sum_norm_inner_sq_le_four_mul_card_mul_sq
statement: formalized
proof: formalized
---

# The Yu–Wang–Samworth overlap bound, Frobenius form

If `Δ ≥ 0` separates the eigenvalues of
the population operator `T` indexed by `s` from the remaining ones, then the eigenvectors `uⱼ` of
the perturbation `S` satisfy `Δ² ∑_{j ∈ s} ∑_{k ∉ s} |⟪vₖ, uⱼ⟫|² ≤ 4 ‖S - T‖_F²`. No gap is
assumed in the spectrum of `S`.

```lean
LinearMap.IsSymmetric.sq_mul_sum_sum_norm_inner_sq_le_four_mul_frobenius_sq.{u_1, u_2}
  {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] {T S : E →ₗ[𝕜] E} {n : ℕ} (hT : T.IsSymmetric) (hS : S.IsSymmetric)
  (hn : Module.finrank 𝕜 E = n) {Δ : ℝ} (hΔ : 0 ≤ Δ) {s : Finset (Fin n)}
  (hgap : ∀ j ∈ s, ∀ k ∉ s, Δ ≤ |hT.eigenvalues hn j - hT.eigenvalues hn k|) :
  Δ ^ 2 *
      ∑ j ∈ s, ∑ k ∈ sᶜ, ‖inner 𝕜 ((hT.eigenvectorBasis hn) k) ((hS.eigenvectorBasis hn) j)‖ ^ 2 ≤
    4 * (TauCeti.UnitarilyInvariantSeminorm.frobenius 𝕜 E E) (S - T) ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Frobenius upper residual bound](../part-01/the-frobenius-upper-residual-bound.md)
- [Weyl's inequality](../part-03/weyls-inequality.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.IsSymmetric.sq_mul_sum_sum_norm_inner_sq_le_four_mul_frobenius_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/Basic.html#LinearMap.IsSymmetric.sq_mul_sum_sum_norm_inner_sq_le_four_mul_frobenius_sq).

## Other forms

**The Yu–Wang–Samworth overlap bound, operator-norm form.** Formalized in Tau Ceti as [`LinearMap.IsSymmetric.sq_mul_sum_sum_norm_inner_sq_le_four_mul_card_mul_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/Basic.html#LinearMap.IsSymmetric.sq_mul_sum_sum_norm_inner_sq_le_four_mul_card_mul_sq).

```lean
LinearMap.IsSymmetric.sq_mul_sum_sum_norm_inner_sq_le_four_mul_card_mul_sq.{u_1, u_2} {𝕜 : Type u_1}
  {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E]
  {T S : E →ₗ[𝕜] E} {n : ℕ} (hT : T.IsSymmetric) (hS : S.IsSymmetric) (hn : Module.finrank 𝕜 E = n)
  {Δ : ℝ} (hΔ : 0 ≤ Δ) {s : Finset (Fin n)}
  (hgap : ∀ j ∈ s, ∀ k ∉ s, Δ ≤ |hT.eigenvalues hn j - hT.eigenvalues hn k|) {ε : ℝ}
  (hε : ∀ (x : E), ‖(S - T) x‖ ≤ ε * ‖x‖) :
  Δ ^ 2 *
      ∑ j ∈ s, ∑ k ∈ sᶜ, ‖inner 𝕜 ((hT.eigenvectorBasis hn) k) ((hS.eigenvectorBasis hn) j)‖ ^ 2 ≤
    4 * ↑s.card * ε ^ 2
```

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.sq_mul_sum_sum_norm_inner_sq_le_four_mul_frobenius_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/Basic.html#LinearMap.IsSymmetric.sq_mul_sum_sum_norm_inner_sq_le_four_mul_frobenius_sq)
- [Source of `LinearMap.IsSymmetric.sq_mul_sum_sum_norm_inner_sq_le_four_mul_frobenius_sq` in TauCeti/Analysis/InnerProductSpace/YuWangSamworth/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/Basic.lean#L189)
