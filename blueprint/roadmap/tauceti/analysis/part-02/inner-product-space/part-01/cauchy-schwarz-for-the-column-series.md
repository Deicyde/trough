---
declaration: theorem
origin: cited
lean: HilbertBasis.tsum_norm_inner_mul_norm_le, ContinuousLinearMap.sq_opNorm_sq_mul_re_inner_sub_re_inner_le
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

**Cauchy–Schwarz for the defect form of an operator.** Formalized in Tau Ceti as [`ContinuousLinearMap.sq_opNorm_sq_mul_re_inner_sub_re_inner_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/OpNormDefect.html#ContinuousLinearMap.sq_opNorm_sq_mul_re_inner_sub_re_inner_le).

```lean
ContinuousLinearMap.sq_opNorm_sq_mul_re_inner_sub_re_inner_le.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [SeminormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [SeminormedAddCommGroup F] [InnerProductSpace 𝕜 F] (X : F →L[𝕜] E) (v w : F) :
  (‖X‖ ^ 2 * RCLike.re (inner 𝕜 v w) - RCLike.re (inner 𝕜 (X v) (X w))) ^ 2 ≤
    (‖X‖ ^ 2 * ‖v‖ ^ 2 - ‖X v‖ ^ 2) * (‖X‖ ^ 2 * ‖w‖ ^ 2 - ‖X w‖ ^ 2)
```

## Sources

- [Tau Ceti documentation: `HilbertBasis.tsum_norm_inner_mul_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HilbertSchmidt/Columns.html#HilbertBasis.tsum_norm_inner_mul_norm_le)
- [Source of `HilbertBasis.tsum_norm_inner_mul_norm_le` in TauCeti/Analysis/InnerProductSpace/HilbertSchmidt/Columns.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/HilbertSchmidt/Columns.lean#L80)
