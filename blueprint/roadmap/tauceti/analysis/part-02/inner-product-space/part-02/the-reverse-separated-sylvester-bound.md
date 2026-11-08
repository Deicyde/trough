---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.mul_norm_le_norm_sylvester_apply_of_re_inner_le_of_le_re_inner
statement: formalized
proof: formalized
---

# The reverse separated Sylvester bound

If the real part of the quadratic form of `A` is at
most `c` and that of `B` is at least `c + g`, then `g ‖X‖ ≤ ‖A X - X B‖` for every bounded operator
`X`. For `g > 0`, every solution of `A X - X B = Y` therefore satisfies `‖X‖ ≤ ‖Y‖ / g`.

```lean
ContinuousLinearMap.mul_norm_le_norm_sylvester_apply_of_re_inner_le_of_le_re_inner.{u_1, u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [SeminormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] {A : E →L[𝕜] E}
  {B : F →L[𝕜] F} {c g : ℝ} (hA : ∀ (x : E), RCLike.re (inner 𝕜 (A x) x) ≤ c * ‖x‖ ^ 2)
  (hB : ∀ (y : F), (c + g) * ‖y‖ ^ 2 ≤ RCLike.re (inner 𝕜 (B y) y)) (X : F →L[𝕜] E) :
  g * ‖X‖ ≤ ‖(A.sylvester B) X‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy–Schwarz for the column series](../part-01/cauchy-schwarz-for-the-column-series.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.mul_norm_le_norm_sylvester_apply_of_re_inner_le_of_le_re_inner`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Sylvester.html#ContinuousLinearMap.mul_norm_le_norm_sylvester_apply_of_re_inner_le_of_le_re_inner).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.mul_norm_le_norm_sylvester_apply_of_re_inner_le_of_le_re_inner`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Sylvester.html#ContinuousLinearMap.mul_norm_le_norm_sylvester_apply_of_re_inner_le_of_le_re_inner)
- [Source of `ContinuousLinearMap.mul_norm_le_norm_sylvester_apply_of_re_inner_le_of_le_re_inner` in TauCeti/Analysis/InnerProductSpace/Sylvester.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/Sylvester.lean#L188)
