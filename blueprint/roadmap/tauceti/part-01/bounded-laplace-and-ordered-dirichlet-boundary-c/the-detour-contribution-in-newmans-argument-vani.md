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
- [Source of `TauCeti.LSeries.tendsto_integral_newmanDetour_mul_kernel` in TauCeti/NumberTheory/LSeries/Newman/Detour.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LSeries/Newman/Detour.lean#L344)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
