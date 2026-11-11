---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.tendsto_integral_newmanDetour_mul_kernel
statement: formalized
proof: formalized
---

# The detour contribution in Newman's argument vanishes in the limit

If `G` is continuous
on the detour `newmanDetour R δ` with `R, δ > 0`, then the detour integral of `G` against Newman's
kernel `exp (T z) (1 + z² / R²) / z` tends to `0` as `T → ∞`.

```lean
TauCeti.LSeries.tendsto_integral_newmanDetour_mul_kernel {R δ : ℝ} {G : ℂ → ℂ} (hR : 0 < R)
  (hδ : 0 < δ) (hG : ContinuousOn G (TauCeti.LSeries.newmanDetour R δ '' Set.Icc (-1) 1)) :
  Filter.Tendsto
    (fun T =>
      ∫ (s : ℝ) in -1..1,
        deriv (TauCeti.LSeries.newmanDetour R δ) s *
          (G (TauCeti.LSeries.newmanDetour R δ s) *
                Complex.exp (↑T * TauCeti.LSeries.newmanDetour R δ s) *
              (1 + TauCeti.LSeries.newmanDetour R δ s ^ 2 / ↑R ^ 2) /
            TauCeti.LSeries.newmanDetour R δ s))
    Filter.atTop (nhds 0)
```

## Depends on

- [Newman's left detour](newmans-left-detour.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.tendsto_integral_newmanDetour_mul_kernel`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Detour.html#TauCeti.LSeries.tendsto_integral_newmanDetour_mul_kernel).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.tendsto_integral_newmanDetour_mul_kernel`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Detour.html#TauCeti.LSeries.tendsto_integral_newmanDetour_mul_kernel)
- [Source of `TauCeti.LSeries.tendsto_integral_newmanDetour_mul_kernel` in TauCeti/NumberTheory/LSeries/Newman/Detour.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LSeries/Newman/Detour.lean#L344)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
