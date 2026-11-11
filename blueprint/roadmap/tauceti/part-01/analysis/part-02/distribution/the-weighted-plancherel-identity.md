---
declaration: theorem
origin: cited
lean: SchwartzMap.integral_inner_pow_mul_norm_fourierInv_sq
statement: formalized
proof: formalized
---

# The weighted Plancherel identity

for a Schwartz function `σ`,

`(2π) ^ (2N) ∫ ⟪x, m⟫ ^ (2N) ‖𝓕⁻ σ x‖² dx = ‖∂_m^N σ‖²_{L²}`.

```lean
SchwartzMap.integral_inner_pow_mul_norm_fourierInv_sq.{u_1, u_2} {V : Type u_1} {H : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [MeasurableSpace V]
  [BorelSpace V] [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
  (σ : SchwartzMap V H) (m : V) (N : ℕ) :
  (2 * Real.pi) ^ (2 * N) *
      ∫ (x : V), inner ℝ x m ^ (2 * N) * ‖(FourierTransformInv.fourierInv σ) x‖ ^ 2 =
    ‖((LineDeriv.lineDerivOp m)^[N] σ).toLp 2 MeasureTheory.volume‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Plancherel's theorem for the inverse Fourier transform of Schwartz functions](plancherels-theorem-for-the-inverse-fourier-tran.md)

## Lean

Formalized in Tau Ceti as [`SchwartzMap.integral_inner_pow_mul_norm_fourierInv_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/SchwartzSpace/WeightedPlancherel.html#SchwartzMap.integral_inner_pow_mul_norm_fourierInv_sq).

## Sources

- [Tau Ceti documentation: `SchwartzMap.integral_inner_pow_mul_norm_fourierInv_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/SchwartzSpace/WeightedPlancherel.html#SchwartzMap.integral_inner_pow_mul_norm_fourierInv_sq)
- [Source of `SchwartzMap.integral_inner_pow_mul_norm_fourierInv_sq` in TauCeti/Analysis/Distribution/SchwartzSpace/WeightedPlancherel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/SchwartzSpace/WeightedPlancherel.lean#L137)
