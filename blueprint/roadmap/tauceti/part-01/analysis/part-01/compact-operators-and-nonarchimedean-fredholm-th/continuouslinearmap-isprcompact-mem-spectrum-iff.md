---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsPrCompact.mem_spectrum_iff_evalAt_inv_eq_zero
statement: formalized
proof: formalized
---

# ContinuousLinearMap.IsPrCompact.mem_spectrum_iff_evalAt_inv_eq_zero

The nonzero spectrum of a row-compact endomorphism of a (Pr) module over a complete
ultrametric field is detected by the zeros of its Fredholm series.

```lean
ContinuousLinearMap.IsPrCompact.mem_spectrum_iff_evalAt_inv_eq_zero.{u_1, u_2} {K : Type u_1}
  {M : Type u_2} [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K]
  [SeminormedAddCommGroup M] [_root_.Module K M] [ContinuousConstSMul K M] {u : M →L[K] M}
  (hu : u.IsPrCompact) {μ : K} (hμ : μ ≠ 0) : μ ∈ spectrum K u ↔ u.charPowerSeries.evalAt μ⁻¹ = 0
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsPrCompact.mem_spectrum_iff_evalAt_inv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/PrModule/Spectrum.html#ContinuousLinearMap.IsPrCompact.mem_spectrum_iff_evalAt_inv_eq_zero).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsPrCompact.mem_spectrum_iff_evalAt_inv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/PrModule/Spectrum.html#ContinuousLinearMap.IsPrCompact.mem_spectrum_iff_evalAt_inv_eq_zero)
- [Source of `ContinuousLinearMap.IsPrCompact.mem_spectrum_iff_evalAt_inv_eq_zero` in TauCeti/Analysis/Normed/Operator/Nonarchimedean/PrModule/Spectrum.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/Nonarchimedean/PrModule/Spectrum.lean#L78)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CompactOperators/STATUS.md)
