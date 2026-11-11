---
declaration: theorem
origin: cited
lean: TauCeti.HaagerupZsido.integral_exp_mul_I_mul_reciprocalKernel
statement: formalized
proof: formalized
---

# The exterior reciprocal Fourier identity

For `|x| ≥ 1`, the Fourier integral of the
Haagerup–Zsidó kernel is `∫ e^{itx} k(t) dt = 1 / x`.

```lean
TauCeti.HaagerupZsido.integral_exp_mul_I_mul_reciprocalKernel {x : ℝ} (hx : 1 ≤ |x|) :
  ∫ (t : ℝ), Complex.exp (↑x * ↑t * Complex.I) * TauCeti.HaagerupZsido.reciprocalKernel t = (↑x)⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HaagerupZsido.integral_exp_mul_I_mul_reciprocalKernel`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/HaagerupZsido/Fourier.html#TauCeti.HaagerupZsido.integral_exp_mul_I_mul_reciprocalKernel).

## Sources

- [Tau Ceti documentation: `TauCeti.HaagerupZsido.integral_exp_mul_I_mul_reciprocalKernel`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/HaagerupZsido/Fourier.html#TauCeti.HaagerupZsido.integral_exp_mul_I_mul_reciprocalKernel)
- [Source of `TauCeti.HaagerupZsido.integral_exp_mul_I_mul_reciprocalKernel` in TauCeti/Analysis/Fourier/HaagerupZsido/Fourier.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fourier/HaagerupZsido/Fourier.lean#L139)
