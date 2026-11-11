---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsInvertible.norm_inverse_le_of_mul_norm_sub_lt
statement: formalized
proof: formalized
---

# The Neumann bound for the inverse of a perturbation

If `‖A⁻¹‖ ≤ M` for an invertible
`A` and `M * ‖B - A‖ < 1`, then `B` is invertible
(`ContinuousLinearMap.IsInvertible.of_mul_norm_sub_lt`) and
`‖B⁻¹‖ ≤ M / (1 - M * ‖B - A‖)`.

```lean
ContinuousLinearMap.IsInvertible.norm_inverse_le_of_mul_norm_sub_lt.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] [CompleteSpace E] {A B : E →L[𝕜] F} (hA : A.IsInvertible)
  {M : ℝ} (hM : ‖A.inverse‖ ≤ M) (h : M * ‖B - A‖ < 1) : ‖B.inverse‖ ≤ M / (1 - M * ‖B - A‖)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsInvertible.norm_inverse_le_of_mul_norm_sub_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/ContinuousLinearMapInverse.html#ContinuousLinearMap.IsInvertible.norm_inverse_le_of_mul_norm_sub_lt).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsInvertible.norm_inverse_le_of_mul_norm_sub_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/ContinuousLinearMapInverse.html#ContinuousLinearMap.IsInvertible.norm_inverse_le_of_mul_norm_sub_lt)
- [Source of `ContinuousLinearMap.IsInvertible.norm_inverse_le_of_mul_norm_sub_lt` in TauCeti/Analysis/Calculus/ContinuousLinearMapInverse.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/ContinuousLinearMapInverse.lean#L155)
