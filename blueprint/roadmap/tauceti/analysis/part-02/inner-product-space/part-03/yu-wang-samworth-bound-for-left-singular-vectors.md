---
declaration: theorem
origin: cited
lean: LinearMap.sq_mul_sum_sum_norm_inner_self_comp_adjoint_eigenvectorBasis_sq_le_four_mul_card_mul_sq, LinearMap.sq_mul_sum_sum_norm_inner_rightSingularBasis_sq_le_four_mul_card_mul_sq, LinearMap.IsSymmetric.sq_mul_sum_sum_norm_inner_sq_le_four_mul_frobenius_sq, LinearMap.IsSymmetric.sq_mul_sum_sum_norm_inner_sq_le_four_mul_card_mul_sq
statement: formalized
proof: formalized
---

# Yu–Wang–Samworth bound for left singular vectors

A population gap in the
eigenvalues of the target Gram operator gives the same cross-block
bound as for right singular vectors. The eigenbases of `A A†` and `Â Â†` include
complete bases of the kernels, so no positive-rank assumption is needed.

Adapted by target-Gram duality from the left-singular population bound in
`YuWangSamworth2015/YuWangSamworth2015/Rectangular/Theorem4.lean` in the Kitware
DKPS formalization (Jon Crall and GPT 5.6 High; Apache-2.0).

```lean
LinearMap.sq_mul_sum_sum_norm_inner_self_comp_adjoint_eigenvectorBasis_sq_le_four_mul_card_mul_sq.{u_1,
    u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
  [FiniteDimensional 𝕜 F] (A Â : E →ₗ[𝕜] F) {Γ a â ε : ℝ} (hΓ : 0 ≤ Γ)
  (hA : ∀ (x : E), ‖A x‖ ≤ a * ‖x‖) (hÂ : ∀ (x : E), ‖Â x‖ ≤ â * ‖x‖)
  (hE : ∀ (x : E), ‖(Â - A) x‖ ≤ ε * ‖x‖) (s : Finset (Fin (Module.finrank 𝕜 F)))
  (hgap : ∀ j ∈ s, ∀ k ∉ s, Γ ≤ |⋯.eigenvalues ⋯ j - ⋯.eigenvalues ⋯ k|) :
  Γ ^ 2 * ∑ j ∈ s, ∑ k ∈ sᶜ, ‖inner 𝕜 ((⋯.eigenvectorBasis ⋯) k) ((⋯.eigenvectorBasis ⋯) j)‖ ^ 2 ≤
    4 * ↑s.card * ((a + â) * ε) ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Frobenius upper residual bound](../part-01/the-frobenius-upper-residual-bound.md)
- [Weyl's inequality](weyls-inequality.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.sq_mul_sum_sum_norm_inner_self_comp_adjoint_eigenvectorBasis_sq_le_four_mul_card_mul_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SingularVectors.html#LinearMap.sq_mul_sum_sum_norm_inner_self_comp_adjoint_eigenvectorBasis_sq_le_four_mul_card_mul_sq).

## Other forms

**Yu–Wang–Samworth bound for right singular vectors.** Formalized in Tau Ceti as [`LinearMap.sq_mul_sum_sum_norm_inner_rightSingularBasis_sq_le_four_mul_card_mul_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SingularVectors.html#LinearMap.sq_mul_sum_sum_norm_inner_rightSingularBasis_sq_le_four_mul_card_mul_sq).

```lean
LinearMap.sq_mul_sum_sum_norm_inner_rightSingularBasis_sq_le_four_mul_card_mul_sq.{u_1, u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
  [FiniteDimensional 𝕜 F] (A Â : E →ₗ[𝕜] F) {Γ a â ε : ℝ} (hΓ : 0 ≤ Γ)
  (hA : ∀ (x : E), ‖A x‖ ≤ a * ‖x‖) (hÂ : ∀ (x : E), ‖Â x‖ ≤ â * ‖x‖)
  (hE : ∀ (x : E), ‖(Â - A) x‖ ≤ ε * ‖x‖) (s : Finset (Fin (Module.finrank 𝕜 E)))
  (hgap : ∀ j ∈ s, ∀ k ∉ s, Γ ≤ |A.singularValues ↑j ^ 2 - A.singularValues ↑k ^ 2|) :
  Γ ^ 2 * ∑ j ∈ s, ∑ k ∈ sᶜ, ‖inner 𝕜 (A.rightSingularBasis k) (Â.rightSingularBasis j)‖ ^ 2 ≤
    4 * ↑s.card * ((a + â) * ε) ^ 2
```

**The Yu–Wang–Samworth overlap bound, Frobenius form.** Formalized in Tau Ceti as [`LinearMap.IsSymmetric.sq_mul_sum_sum_norm_inner_sq_le_four_mul_frobenius_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/Basic.html#LinearMap.IsSymmetric.sq_mul_sum_sum_norm_inner_sq_le_four_mul_frobenius_sq).

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

- [Tau Ceti documentation: `LinearMap.sq_mul_sum_sum_norm_inner_self_comp_adjoint_eigenvectorBasis_sq_le_four_mul_card_mul_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SingularVectors.html#LinearMap.sq_mul_sum_sum_norm_inner_self_comp_adjoint_eigenvectorBasis_sq_le_four_mul_card_mul_sq)
- [Source of `LinearMap.sq_mul_sum_sum_norm_inner_self_comp_adjoint_eigenvectorBasis_sq_le_four_mul_card_mul_sq` in TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SingularVectors.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SingularVectors.lean#L87)
