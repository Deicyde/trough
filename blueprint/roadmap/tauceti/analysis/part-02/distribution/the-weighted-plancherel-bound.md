---
declaration: theorem
origin: cited
lean: SchwartzMap.integral_norm_pow_mul_norm_fourierInv_sq_le
statement: formalized
proof: formalized
---

# The weighted Plancherel bound

for a Schwartz function `σ`, an orthonormal basis `b` of
`V` indexed by `ι`, and `N ≠ 0`,

`(2π) ^ (2N) ∫ ‖x‖ ^ (2N) ‖𝓕⁻ σ x‖² dx ≤ (#ι) ^ (N - 1) ∑ᵢ ‖∂_{bᵢ}^N σ‖²_{L²}`.

```lean
SchwartzMap.integral_norm_pow_mul_norm_fourierInv_sq_le.{u_1, u_2, u_3} {V : Type u_1}
  {H : Type u_2} [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V]
  [MeasurableSpace V] [BorelSpace V] [NormedAddCommGroup H] [InnerProductSpace ℂ H]
  [CompleteSpace H] {ι : Type u_3} [Fintype ι] (σ : SchwartzMap V H) (b : OrthonormalBasis ι ℝ V)
  {N : ℕ} (hN : N ≠ 0) :
  (2 * Real.pi) ^ (2 * N) * ∫ (x : V), ‖x‖ ^ (2 * N) * ‖(FourierTransformInv.fourierInv σ) x‖ ^ 2 ≤
    ↑(Fintype.card ι) ^ (N - 1) *
      ∑ i, ‖((LineDeriv.lineDerivOp (b i))^[N] σ).toLp 2 MeasureTheory.volume‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The weighted Plancherel identity](the-weighted-plancherel-identity.md)

## Lean

Formalized in Tau Ceti as [`SchwartzMap.integral_norm_pow_mul_norm_fourierInv_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/SchwartzSpace/WeightedPlancherel.html#SchwartzMap.integral_norm_pow_mul_norm_fourierInv_sq_le).

## Sources

- [Tau Ceti documentation: `SchwartzMap.integral_norm_pow_mul_norm_fourierInv_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/SchwartzSpace/WeightedPlancherel.html#SchwartzMap.integral_norm_pow_mul_norm_fourierInv_sq_le)
- [Source of `SchwartzMap.integral_norm_pow_mul_norm_fourierInv_sq_le` in TauCeti/Analysis/Distribution/SchwartzSpace/WeightedPlancherel.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Distribution/SchwartzSpace/WeightedPlancherel.lean#L148)
