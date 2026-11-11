---
declaration: theorem
origin: cited
lean: HasCompactSupport.two_pi_inv_smul_integral_sub_inv_smul_fderiv_apply_one_add_I_smul_apply_I
statement: formalized
proof: formalized
---

# The Cauchy–Pompeiu formula for a compactly supported `C¹` map `u : ℂ → F`

`u` is the
Cauchy transform of `∂ₓ u + i ∂ᵧ u = 2 \bar∂ u`,
`u w = (2π)⁻¹ ∫ (w - z)⁻¹ • (∂ₓ u z + i ∂ᵧ u z)`, the integral being over the whole plane.

```lean
HasCompactSupport.two_pi_inv_smul_integral_sub_inv_smul_fderiv_apply_one_add_I_smul_apply_I.{u_1}
  {F : Type u_1} [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F] {u : ℂ → F}
  (hc : HasCompactSupport u) (hu : ContDiff ℝ 1 u) (w : ℂ) :
  (2 * ↑Real.pi)⁻¹ •
      ∫ (z : ℂ), (w - z)⁻¹ • ((fderiv ℝ u z) 1 + Complex.I • (fderiv ℝ u z) Complex.I) =
    u w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HasCompactSupport.two_pi_inv_smul_integral_sub_inv_smul_fderiv_apply_one_add_I_smul_apply_I`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pompeiu/Basic.html#HasCompactSupport.two_pi_inv_smul_integral_sub_inv_smul_fderiv_apply_one_add_I_smul_apply_I).

## Sources

- [Tau Ceti documentation: `HasCompactSupport.two_pi_inv_smul_integral_sub_inv_smul_fderiv_apply_one_add_I_smul_apply_I`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pompeiu/Basic.html#HasCompactSupport.two_pi_inv_smul_integral_sub_inv_smul_fderiv_apply_one_add_I_smul_apply_I)
- [Source of `HasCompactSupport.two_pi_inv_smul_integral_sub_inv_smul_fderiv_apply_one_add_I_smul_apply_I` in TauCeti/Analysis/Complex/Pompeiu/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Pompeiu/Basic.lean#L298)
