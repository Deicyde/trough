---
declaration: theorem
origin: cited
lean: LinearMap.sq_mul_sum_sum_norm_inner_self_comp_adjoint_eigenvectorBasis_sq_le_four_mul_card_mul_sq, LinearMap.sq_mul_sum_sum_norm_inner_rightSingularBasis_sq_le_four_mul_card_mul_sq
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

- [The Yu–Wang–Samworth overlap bound, Frobenius form](the-yu-wang-samworth-overlap-bound-frobenius-for.md)

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

## Sources

- [Tau Ceti documentation: `LinearMap.sq_mul_sum_sum_norm_inner_self_comp_adjoint_eigenvectorBasis_sq_le_four_mul_card_mul_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SingularVectors.html#LinearMap.sq_mul_sum_sum_norm_inner_self_comp_adjoint_eigenvectorBasis_sq_le_four_mul_card_mul_sq)
- [Source of `LinearMap.sq_mul_sum_sum_norm_inner_self_comp_adjoint_eigenvectorBasis_sq_le_four_mul_card_mul_sq` in TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SingularVectors.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/YuWangSamworth/SingularVectors.lean#L87)
