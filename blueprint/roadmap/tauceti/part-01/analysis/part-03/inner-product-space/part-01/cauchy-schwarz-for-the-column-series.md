---
declaration: theorem
origin: cited
lean: HilbertBasis.tsum_norm_inner_mul_norm_le, TauCeti.norm_prod_inner_le, ContinuousLinearMap.sq_mul_re_inner_sub_re_inner_sq_le_of_opNorm_le
statement: formalized
proof: formalized
---

# Cauchy–Schwarz for the column series

`∑' i, ‖⟪bᵢ, x⟫‖ ‖fᵢ‖ ≤ ‖x‖ ‖f‖`.

```lean
HilbertBasis.tsum_norm_inner_mul_norm_le.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} {ι : Type u_4} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [NormedAddCommGroup F] (b : HilbertBasis ι 𝕜 E) (f : ↥(lp (fun x => F) 2)) (x : E) :
  ∑' (i : ι), ‖inner 𝕜 (b i) x‖ * ‖↑f i‖ ≤ ‖x‖ * ‖f‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HilbertBasis.tsum_norm_inner_mul_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HilbertSchmidt/Columns.html#HilbertBasis.tsum_norm_inner_mul_norm_le).

## Other forms

**Cauchy–Schwarz for a product of inner products.** Formalized in Tau Ceti as [`TauCeti.norm_prod_inner_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/ProdInner.html#TauCeti.norm_prod_inner_le).

```lean
TauCeti.norm_prod_inner_le.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {ι : Type u_3} [RCLike 𝕜]
  [SeminormedAddCommGroup E] [InnerProductSpace 𝕜 E] (s : Finset ι) (m : ι → E) (η : E) :
  ‖∏ i ∈ s, inner 𝕜 (m i) η‖ ≤ (∏ i ∈ s, ‖m i‖) * ‖η‖ ^ s.card
```

**Cauchy–Schwarz for the defect form of an operator.** Formalized in Tau Ceti as [`ContinuousLinearMap.sq_mul_re_inner_sub_re_inner_sq_le_of_opNorm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/OpNormDefect.html#ContinuousLinearMap.sq_mul_re_inner_sub_re_inner_sq_le_of_opNorm_le).

```lean
ContinuousLinearMap.sq_mul_re_inner_sub_re_inner_sq_le_of_opNorm_le.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [SeminormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [SeminormedAddCommGroup F] [InnerProductSpace 𝕜 F] (X : F →L[𝕜] E) {c : ℝ} (hc : ‖X‖ ≤ c)
  (v w : F) :
  (c ^ 2 * RCLike.re (inner 𝕜 v w) - RCLike.re (inner 𝕜 (X v) (X w))) ^ 2 ≤
    (c ^ 2 * ‖v‖ ^ 2 - ‖X v‖ ^ 2) * (c ^ 2 * ‖w‖ ^ 2 - ‖X w‖ ^ 2)
```

## Sources

- [Tau Ceti documentation: `HilbertBasis.tsum_norm_inner_mul_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HilbertSchmidt/Columns.html#HilbertBasis.tsum_norm_inner_mul_norm_le)
- [Source of `HilbertBasis.tsum_norm_inner_mul_norm_le` in TauCeti/Analysis/InnerProductSpace/HilbertSchmidt/Columns.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/HilbertSchmidt/Columns.lean#L80)
