---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsRowCompact.mem_spectrum_iff_evalAt_inv_eq_zero
statement: formalized
proof: formalized
---

# The nonzero spectrum of a row-compact operator

For a row-compact endomorphism `u` of
`C₀(I, K)` over a complete ultrametric field and `μ ≠ 0`, `μ` lies in the spectrum of `u` if and
only if `μ⁻¹` is a zero of the Fredholm series `det (1 - T u)`.

```lean
ContinuousLinearMap.IsRowCompact.mem_spectrum_iff_evalAt_inv_eq_zero.{u_1, u_2} {I : Type u_1}
  [TopologicalSpace I] [DiscreteTopology I] [DecidableEq I] {K : Type u_2}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K]
  {u : ZeroAtInftyContinuousMap I K →L[K] ZeroAtInftyContinuousMap I K} (hu : u.IsRowCompact)
  {μ : K} (hμ : μ ≠ 0) : μ ∈ spectrum K u ↔ u.matrixCoeff.charPowerSeries.evalAt μ⁻¹ = 0
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Proof depends on

- [ContinuousLinearMap.charPowerSeries](continuouslinearmap-charpowerseries.md)
- [The Fredholm determinant is entire](the-fredholm-determinant-is-entire.md)
- [Independence of the presentation](independence-of-the-presentation.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsRowCompact.mem_spectrum_iff_evalAt_inv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Spectrum.html#ContinuousLinearMap.IsRowCompact.mem_spectrum_iff_evalAt_inv_eq_zero).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsRowCompact.mem_spectrum_iff_evalAt_inv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Spectrum.html#ContinuousLinearMap.IsRowCompact.mem_spectrum_iff_evalAt_inv_eq_zero)
- [Source of `ContinuousLinearMap.IsRowCompact.mem_spectrum_iff_evalAt_inv_eq_zero` in TauCeti/Analysis/Normed/Operator/Nonarchimedean/Spectrum.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Spectrum.lean#L123)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CompactOperators/STATUS.md)
