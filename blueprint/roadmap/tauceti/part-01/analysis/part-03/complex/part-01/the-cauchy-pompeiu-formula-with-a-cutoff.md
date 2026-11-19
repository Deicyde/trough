---
declaration: theorem
origin: cited
lean: HasCompactSupport.cauchyTransform_conjWirtingerDeriv_smul, HasCompactSupport.two_pi_inv_smul_integral_sub_inv_smul_fderiv_apply_one_add_I_smul_apply_I
statement: formalized
proof: formalized
---

# The Cauchy–Pompeiu formula with a cutoff

If `χ` is a compactly supported `C¹` function
whose topological support lies in an open set `V` on which `f : ℂ → F` is holomorphic, then
`χ w • f w` is the Cauchy transform of `\bar∂χ • f`, for every `w ∈ ℂ`.

```lean
HasCompactSupport.cauchyTransform_conjWirtingerDeriv_smul.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F] {χ : ℂ → ℂ} {f : ℂ → F} {V : Set ℂ}
  (hχ : HasCompactSupport χ) (hχd : ContDiff ℝ 1 χ) (hV : IsOpen V) (hχV : tsupport χ ⊆ V)
  (hf : DifferentiableOn ℂ f V) (w : ℂ) :
  TauCeti.cauchyTransform (fun z => (TauCeti.conjWirtingerDeriv χ z) 1 • f z) w = χ w • f w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HasCompactSupport.cauchyTransform_conjWirtingerDeriv_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pompeiu/Basic.html#HasCompactSupport.cauchyTransform_conjWirtingerDeriv_smul).

## Other forms

**The Cauchy–Pompeiu formula for a compactly supported `C¹` map `u : ℂ → F`.** Formalized in Tau Ceti as [`HasCompactSupport.two_pi_inv_smul_integral_sub_inv_smul_fderiv_apply_one_add_I_smul_apply_I`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pompeiu/Basic.html#HasCompactSupport.two_pi_inv_smul_integral_sub_inv_smul_fderiv_apply_one_add_I_smul_apply_I).

```lean
HasCompactSupport.two_pi_inv_smul_integral_sub_inv_smul_fderiv_apply_one_add_I_smul_apply_I.{u_1}
  {F : Type u_1} [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F] {u : ℂ → F}
  (hc : HasCompactSupport u) (hu : ContDiff ℝ 1 u) (w : ℂ) :
  (2 * ↑Real.pi)⁻¹ •
      ∫ (z : ℂ), (w - z)⁻¹ • ((fderiv ℝ u z) 1 + Complex.I • (fderiv ℝ u z) Complex.I) =
    u w
```

## Sources

- [Tau Ceti documentation: `HasCompactSupport.cauchyTransform_conjWirtingerDeriv_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pompeiu/Basic.html#HasCompactSupport.cauchyTransform_conjWirtingerDeriv_smul)
- [Source of `HasCompactSupport.cauchyTransform_conjWirtingerDeriv_smul` in TauCeti/Analysis/Complex/Pompeiu/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Pompeiu/Basic.lean#L569)
