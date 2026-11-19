---
declaration: theorem
origin: cited
lean: HasFPowerSeriesAt.mvCoeff_eq_zero_of_eventuallyEq_zero
statement: formalized
proof: formalized
---

# The identity theorem in coefficient form

if `f` has the power series `p` at `x` and
vanishes near `x`, then every multi-index coefficient of `p` is zero.

```lean
HasFPowerSeriesAt.mvCoeff_eq_zero_of_eventuallyEq_zero.{u_1, u_2, u_3} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {ι : Type u_2} [Fintype ι] {F : Type u_3} [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] {f : (ι → 𝕜) → F} {p : FormalMultilinearSeries 𝕜 (ι → 𝕜) F} {x : ι → 𝕜}
  (hf : HasFPowerSeriesAt f p x) (h0 : f =ᶠ[nhds x] 0) (α : ι → ℕ) : p.mvCoeff α = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HasFPowerSeriesAt.mvCoeff_eq_zero_of_eventuallyEq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/MultiIndex/Coeff.html#HasFPowerSeriesAt.mvCoeff_eq_zero_of_eventuallyEq_zero).

## Sources

- [Tau Ceti documentation: `HasFPowerSeriesAt.mvCoeff_eq_zero_of_eventuallyEq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/MultiIndex/Coeff.html#HasFPowerSeriesAt.mvCoeff_eq_zero_of_eventuallyEq_zero)
- [Source of `HasFPowerSeriesAt.mvCoeff_eq_zero_of_eventuallyEq_zero` in TauCeti/Analysis/Analytic/MultiIndex/Coeff.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Analytic/MultiIndex/Coeff.lean#L249)
