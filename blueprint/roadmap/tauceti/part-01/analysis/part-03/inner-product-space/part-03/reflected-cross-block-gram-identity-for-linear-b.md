---
declaration: theorem
origin: cited
lean: LinearIsometry.adjoint_comp_self_adjoint_two_smul_comp_adjoint_sub_id_comp_comp_of_adjoint_comp_eq_zero
statement: formalized
proof: formalized
---

# Reflected cross-block Gram identity for linear blocks

If `E₀` is an
isometry and `F₀`, `F₁` are linear maps with complementary final operators
and orthogonal cross block, the reflected cross block has Gram operator
`4 (M - M²)` for `M = T⋆T` and `T = E₀⋆F₁`.
For arbitrary `F₁`, complementarity alone does not imply orthogonality,
so `F₀⋆F₁ = 0` is explicitly assumed; it follows if `F₁` is a partial isometry.

```lean
LinearIsometry.adjoint_comp_self_adjoint_two_smul_comp_adjoint_sub_id_comp_comp_of_adjoint_comp_eq_zero.{u_1,
    u_2, u_3, u_4, u_5}
  {𝕜 : Type u_1} [RCLike 𝕜] {E : Type u_2} [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] {K₀ : Type u_3} {K₁ : Type u_4} {L : Type u_5} [NormedAddCommGroup K₀]
  [InnerProductSpace 𝕜 K₀] [FiniteDimensional 𝕜 K₀] [NormedAddCommGroup K₁] [InnerProductSpace 𝕜 K₁]
  [FiniteDimensional 𝕜 K₁] [NormedAddCommGroup L] [InnerProductSpace 𝕜 L] [FiniteDimensional 𝕜 L]
  (E₀ : K₀ →ₗᵢ[𝕜] E) (F₀ : L →ₗ[𝕜] E) (F₁ : K₁ →ₗ[𝕜] E)
  (hF : F₀ ∘ₗ LinearMap.adjoint F₀ + F₁ ∘ₗ LinearMap.adjoint F₁ = LinearMap.id)
  (horth : LinearMap.adjoint F₀ ∘ₗ F₁ = 0) :
  LinearMap.adjoint
        (LinearMap.adjoint
            ((2 • E₀.toLinearMap ∘ₗ LinearMap.adjoint E₀.toLinearMap - LinearMap.id) ∘ₗ F₀) ∘ₗ
          F₁) ∘ₗ
      LinearMap.adjoint
          ((2 • E₀.toLinearMap ∘ₗ LinearMap.adjoint E₀.toLinearMap - LinearMap.id) ∘ₗ F₀) ∘ₗ
        F₁ =
    4 •
      (LinearMap.adjoint (LinearMap.adjoint E₀.toLinearMap ∘ₗ F₁) ∘ₗ
          LinearMap.adjoint E₀.toLinearMap ∘ₗ F₁ -
        (LinearMap.adjoint (LinearMap.adjoint E₀.toLinearMap ∘ₗ F₁) ∘ₗ
            LinearMap.adjoint E₀.toLinearMap ∘ₗ F₁) ∘ₗ
          LinearMap.adjoint (LinearMap.adjoint E₀.toLinearMap ∘ₗ F₁) ∘ₗ
            LinearMap.adjoint E₀.toLinearMap ∘ₗ F₁)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Pythagorean Gram identity for complementary linear blocks](../part-02/pythagorean-gram-identity-for-complementary-line.md)
- [The rectangular double-angle Gram identity](the-rectangular-double-angle-gram-identity.md)

## Lean

Formalized in Tau Ceti as [`LinearIsometry.adjoint_comp_self_adjoint_two_smul_comp_adjoint_sub_id_comp_comp_of_adjoint_comp_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/DoubleAngle/Gram.html#LinearIsometry.adjoint_comp_self_adjoint_two_smul_comp_adjoint_sub_id_comp_comp_of_adjoint_comp_eq_zero).

## Sources

- [Tau Ceti documentation: `LinearIsometry.adjoint_comp_self_adjoint_two_smul_comp_adjoint_sub_id_comp_comp_of_adjoint_comp_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/DoubleAngle/Gram.html#LinearIsometry.adjoint_comp_self_adjoint_two_smul_comp_adjoint_sub_id_comp_comp_of_adjoint_comp_eq_zero)
- [Source of `LinearIsometry.adjoint_comp_self_adjoint_two_smul_comp_adjoint_sub_id_comp_comp_of_adjoint_comp_eq_zero` in TauCeti/Analysis/InnerProductSpace/DoubleAngle/Gram.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/DoubleAngle/Gram.lean#L176)
