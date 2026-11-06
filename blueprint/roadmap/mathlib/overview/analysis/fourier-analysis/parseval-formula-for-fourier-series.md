# Parseval formula for Fourier series

Mathlib states this as `tsum_sq_fourierCoeff`.

```lean
tsum_sq_fourierCoeff {T : ℝ} [hT : Fact (0 < T)]
  (f : ↥(MeasureTheory.Lp ℂ 2 AddCircle.haarAddCircle)) :
  ∑' (i : ℤ), ‖fourierCoeff (↑↑f) i‖ ^ 2 = ∫ (t : AddCircle T), ‖↑↑f t‖ ^ 2 ∂AddCircle.haarAddCircle
```

## Depends on

- [Fourier Series](../../../hundred-theorems/part-03/fourier-series.md)

## Sources

- [Mathlib documentation: `tsum_sq_fourierCoeff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/AddCircle.html#tsum_sq_fourierCoeff)
- [Source of `tsum_sq_fourierCoeff` in Mathlib/Analysis/Fourier/AddCircle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/AddCircle.lean#L452)
- [Mathlib overview: Analysis › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L388)
- [Mathlib undergraduate list: Measures and integral calculus › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L537)
- [1000+ theorems list: Q1443036](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1694)
- [1000+ theorems project: Q1443036](https://1000-plus.github.io/all.html?length=-1#Q1443036)
- [Wikipedia: Parseval's theorem](https://en.wikipedia.org/wiki/Parseval's_theorem)
- [Wikidata: Q1443036](https://www.wikidata.org/wiki/Q1443036)
