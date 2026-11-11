---
declaration: theorem
origin: cited
lean: LinearIsometry.adjoint_comp_self_adjoint_comp_eq_id_sub_comp_adjoint
statement: formalized
proof: formalized
---

# Pythagorean Gram identity for complementary linear blocks

If the ranges
of linear maps `F₀` and `F₁` satisfy `F₀F₀⋆ + F₁F₁⋆ = 1` and `E₀` is an
isometry, then `(F₀⋆E₀)⋆(F₀⋆E₀) = 1 - (E₀⋆F₁)(E₀⋆F₁)⋆`.
No isometry hypothesis on `F₀` or `F₁` is needed.

```lean
LinearIsometry.adjoint_comp_self_adjoint_comp_eq_id_sub_comp_adjoint.{u_1, u_2, u_3, u_4, u_5}
  {𝕜 : Type u_1} [RCLike 𝕜] {E : Type u_2} [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] {K₀ : Type u_3} {K₁ : Type u_4} {L : Type u_5} [NormedAddCommGroup K₀]
  [InnerProductSpace 𝕜 K₀] [FiniteDimensional 𝕜 K₀] [NormedAddCommGroup K₁] [InnerProductSpace 𝕜 K₁]
  [FiniteDimensional 𝕜 K₁] [NormedAddCommGroup L] [InnerProductSpace 𝕜 L] [FiniteDimensional 𝕜 L]
  (E₀ : K₀ →ₗᵢ[𝕜] E) (F₀ : L →ₗ[𝕜] E) (F₁ : K₁ →ₗ[𝕜] E)
  (hF : F₀ ∘ₗ LinearMap.adjoint F₀ + F₁ ∘ₗ LinearMap.adjoint F₁ = LinearMap.id) :
  LinearMap.adjoint (LinearMap.adjoint F₀ ∘ₗ E₀.toLinearMap) ∘ₗ
      LinearMap.adjoint F₀ ∘ₗ E₀.toLinearMap =
    LinearMap.id -
      (LinearMap.adjoint E₀.toLinearMap ∘ₗ F₁) ∘ₗ
        LinearMap.adjoint (LinearMap.adjoint E₀.toLinearMap ∘ₗ F₁)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearIsometry.adjoint_comp_self_adjoint_comp_eq_id_sub_comp_adjoint`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/DoubleAngle/Gram.html#LinearIsometry.adjoint_comp_self_adjoint_comp_eq_id_sub_comp_adjoint).

## Sources

- [Tau Ceti documentation: `LinearIsometry.adjoint_comp_self_adjoint_comp_eq_id_sub_comp_adjoint`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/DoubleAngle/Gram.html#LinearIsometry.adjoint_comp_self_adjoint_comp_eq_id_sub_comp_adjoint)
- [Source of `LinearIsometry.adjoint_comp_self_adjoint_comp_eq_id_sub_comp_adjoint` in TauCeti/Analysis/InnerProductSpace/DoubleAngle/Gram.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/DoubleAngle/Gram.lean#L152)
