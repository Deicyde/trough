---
declaration: theorem
origin: cited
lean: TauCeti.tendsto_integral_cpow_mul_I_smul_atTop
statement: formalized
proof: formalized
---

# Riemann--Lebesgue on a vertical line

the integral of `f` against the oscillating factor
`x ^ (i t)` tends to `0` as `x → ∞`.

No hypothesis is needed on `f`. A limit along `atTop` only sees `x > 0`, and there the factor
`x ^ (i t)` has modulus `1`, so the integrand is integrable exactly when `f` is; when `f` is not
integrable both the left-hand side and the limit are `0`. (For `x ≤ 0` the equivalence fails —
at `x = 0` the integrand vanishes almost everywhere, and for `x < 0` the branch of the complex
power contributes a factor of modulus `exp (-π t)` — but those scales are irrelevant here.)

```lean
TauCeti.tendsto_integral_cpow_mul_I_smul_atTop.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] (f : ℝ → E) :
  Filter.Tendsto (fun x => ∫ (t : ℝ), ↑x ^ (↑t * Complex.I) • f t) Filter.atTop (nhds 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.tendsto_integral_cpow_mul_I_smul_atTop`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/RiemannLebesgue.html#TauCeti.tendsto_integral_cpow_mul_I_smul_atTop).

## Sources

- [Tau Ceti documentation: `TauCeti.tendsto_integral_cpow_mul_I_smul_atTop`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/RiemannLebesgue.html#TauCeti.tendsto_integral_cpow_mul_I_smul_atTop)
- [Source of `TauCeti.tendsto_integral_cpow_mul_I_smul_atTop` in TauCeti/Analysis/Fourier/RiemannLebesgue.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Fourier/RiemannLebesgue.lean#L33)
