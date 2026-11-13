---
declaration: module
origin: cited
lean: KleinGordon.fourier_solutionSlice_of_le, KleinGordon.fourier_solutionSlice, KleinGordon.freqSolution_cauchy
statement: formalized
proof: formalized
---

# The spatial Fourier transform of the retarded solution

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.FourierRepresentation`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FourierRepresentation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FourierRepresentation.lean): 3 declarations, 3 with a docstring.

> The retarded solution at time `t` has the spatial Fourier transform given by the Duhamel integral
> of the sine multiplier.

## i. Overview

> For a source `f` of compact support the slice of the retarded solution at time `t` is a Schwartz
> function in space. Its spatial Fourier transform at the frequency `ξ` is the integral over
> earlier times `s` of the sine multiplier `sin(ω (t - s)) / ω` times the Fourier transform of the
> source slice at time `s`. Outside the time support of the source the transform obeys the free
> oscillator evolution of its value and velocity at the last time of the support.

## ii. Key results

> - `fourier_solutionSlice` : the Fourier transform of the retarded slice.

## iv. References

> None.

## A. The Fourier transform of the retarded slice

> - `fourier_solutionSlice` : the Fourier transform of the retarded slice.

**`KleinGordon.fourier_solutionSlice_of_le`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FourierRepresentation.lean#L60).

> The Fourier transform of the retarded slice, when the source vanishes before the time `a`.

```lean
lemma fourier_solutionSlice_of_le {μ : ℝ} (hμ : 0 ≤ μ) {a : ℝ}
    (ha : ∀ s ≤ a, s ∉ Prod.fst '' tsupport f) {t : ℝ} (hat : a ≤ t) (ξ : E) :
    𝓕 (solutionSlice F f hμ t) ξ = freqSolution F f μ a ξ t
```

**`KleinGordon.fourier_solutionSlice`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FourierRepresentation.lean#L83).

> The Fourier transform of the retarded slice at time `t` is the integral over earlier times of
> the sine multiplier times the Fourier transform of the source slice.

```lean
lemma fourier_solutionSlice {μ : ℝ} (hμ : 0 ≤ μ) (t : ℝ) (ξ : E) :
    𝓕 (solutionSlice F f hμ t) ξ =
      ∫ s in Set.Iic t, multiplier (t - s) μ ξ • 𝓕 (slice F f s) ξ
```

**`KleinGordon.freqSolution_cauchy`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FourierRepresentation.lean#L103).

> After the last time of the source the Fourier mode of the retarded solution is the free
> oscillator evolution of its value and velocity at that time.

```lean
lemma freqSolution_cauchy {μ : ℝ} {a T t : ℝ} (hT : ∀ s ≥ T, s ∉ Prod.fst '' tsupport f)
    (hTt : T ≤ t) (ξ : E) :
    freqSolution F f μ a ξ t =
      (Real.cos (dispersion μ ξ * (t - T)) : ℂ) • freqSolution F f μ a ξ T +
        (Real.sincPropagator (t - T) (dispersion μ ξ) : ℂ) • freqSolution1 F f μ a ξ T
```

## Depends on

- [The solution as a tempered distribution in space](temperedslice.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FourierRepresentation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FourierRepresentation.lean)
