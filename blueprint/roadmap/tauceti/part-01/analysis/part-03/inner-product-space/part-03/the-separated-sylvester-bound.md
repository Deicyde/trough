---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.mul_norm_le_norm_sylvester_apply_of_le_re_inner_of_re_inner_le
statement: formalized
proof: formalized
---

# The separated Sylvester bound

If the real part of the quadratic form of `A` is at least
`c + g` and that of `B` is at most `c`, then `g ‖X‖ ≤ ‖A X - X B‖` for every bounded operator `X`.
For `g > 0`, every solution of `A X - X B = Y` therefore satisfies `‖X‖ ≤ ‖Y‖ / g`.

```lean
ContinuousLinearMap.mul_norm_le_norm_sylvester_apply_of_le_re_inner_of_re_inner_le.{u_1, u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [SeminormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] {A : E →L[𝕜] E}
  {B : F →L[𝕜] F} {c g : ℝ} (hA : ∀ (x : E), (c + g) * ‖x‖ ^ 2 ≤ RCLike.re (inner 𝕜 (A x) x))
  (hB : ∀ (y : F), RCLike.re (inner 𝕜 (B y) y) ≤ c * ‖y‖ ^ 2) (X : F →L[𝕜] E) :
  g * ‖X‖ ≤ ‖(A.sylvester B) X‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy–Schwarz for the column series](../part-01/cauchy-schwarz-for-the-column-series.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.mul_norm_le_norm_sylvester_apply_of_le_re_inner_of_re_inner_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Sylvester.html#ContinuousLinearMap.mul_norm_le_norm_sylvester_apply_of_le_re_inner_of_re_inner_le).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.mul_norm_le_norm_sylvester_apply_of_le_re_inner_of_re_inner_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Sylvester.html#ContinuousLinearMap.mul_norm_le_norm_sylvester_apply_of_le_re_inner_of_re_inner_le)
- [Source of `ContinuousLinearMap.mul_norm_le_norm_sylvester_apply_of_le_re_inner_of_re_inner_le` in TauCeti/Analysis/InnerProductSpace/Sylvester.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Sylvester.lean#L177)
