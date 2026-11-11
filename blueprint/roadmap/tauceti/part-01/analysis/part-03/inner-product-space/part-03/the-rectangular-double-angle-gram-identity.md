---
declaration: theorem
origin: cited
lean: LinearMap.adjoint_comp_self_comp_eq_sub_of_adjoint_comp_self_eq_id_sub
statement: formalized
proof: formalized
---

# The rectangular double-angle Gram identity

If `C⋆C = 1 - T T⋆` then
the Gram operator of the composite `C ∘ T` is `M - M²` for `M = T⋆T`.

The three spaces are independent: `T : K₁ →ₗ K₀` and `C : K₀ →ₗ L` need not have
equal-dimensional domains and codomains, and no direct rotation between them is
assumed.  This is what makes the `sin 2θ` estimate survive the dimension
mismatch `dim 𝔛(E₀) < dim 𝔛(F₀)` of Davis--Kahan 1970.

```lean
LinearMap.adjoint_comp_self_comp_eq_sub_of_adjoint_comp_self_eq_id_sub.{u_1, u_2, u_3, u_4}
  {𝕜 : Type u_1} [RCLike 𝕜] {K₀ : Type u_2} {K₁ : Type u_3} {L : Type u_4} [NormedAddCommGroup K₀]
  [InnerProductSpace 𝕜 K₀] [FiniteDimensional 𝕜 K₀] [NormedAddCommGroup K₁] [InnerProductSpace 𝕜 K₁]
  [FiniteDimensional 𝕜 K₁] [NormedAddCommGroup L] [InnerProductSpace 𝕜 L] [FiniteDimensional 𝕜 L]
  {C : K₀ →ₗ[𝕜] L} {T : K₁ →ₗ[𝕜] K₀}
  (hC : LinearMap.adjoint C ∘ₗ C = LinearMap.id - T ∘ₗ LinearMap.adjoint T) :
  LinearMap.adjoint (C ∘ₗ T) ∘ₗ C ∘ₗ T =
    LinearMap.adjoint T ∘ₗ T - (LinearMap.adjoint T ∘ₗ T) ∘ₗ LinearMap.adjoint T ∘ₗ T
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.adjoint_comp_self_comp_eq_sub_of_adjoint_comp_self_eq_id_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/DoubleAngle/Gram.html#LinearMap.adjoint_comp_self_comp_eq_sub_of_adjoint_comp_self_eq_id_sub).

## Sources

- [Tau Ceti documentation: `LinearMap.adjoint_comp_self_comp_eq_sub_of_adjoint_comp_self_eq_id_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/DoubleAngle/Gram.html#LinearMap.adjoint_comp_self_comp_eq_sub_of_adjoint_comp_self_eq_id_sub)
- [Source of `LinearMap.adjoint_comp_self_comp_eq_sub_of_adjoint_comp_self_eq_id_sub` in TauCeti/Analysis/InnerProductSpace/DoubleAngle/Gram.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/DoubleAngle/Gram.lean#L57)
