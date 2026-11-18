---
declaration: module
origin: cited
lean: TimeSlice.hasDerivAt_fourier_slice, TimeSlice.deriv_fourier_slice, TimeSlice.iteratedDeriv_fourier_slice, TimeSlice.contDiff_fourier_slice, TimeSlice.exists_iteratedDeriv_fourier_slice_bound, TimeSlice.fourierIntegrand, TimeSlice.contDiff_fourierIntegrand, TimeSlice.fourierIntegrand_eq_zero
statement: formalized
proof: formalized
---

# Smoothness and bounds of time slices

The module `PhyslibAlpha.Mathematics.Distribution.TimeSliceSmooth`, [PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean): 19 declarations, 11 with a docstring.

> The Fourier transform of the slices depends smoothly on time and space.

## i. Overview

> The Fourier transform of the slices depends smoothly on time and space. The seminorms of the slices
> are bounded by seminorms of the source.

## ii. Key results

> - `fourierIntegrand` : The integrand of the partial Fourier transform, as a function of the
>   parameter `(s, ξ)` and the position `y`.
> - `supportedSource` : The native continuous inclusion of fixed-support sources into all compact test
>   sources.
> - `supportedDt` : Time differentiation is a continuous endomorphism of every fixed-support source
>   space.
> - `hasDerivAt_fourier_slice` : The time derivative of the Fourier transformed slice is the Fourier
>   transformed slice of the time derivative.

## iv. References

> None.

## A. The time dependence of the Fourier transformed slices

> Lemmas: `hasDerivAt_fourier_slice`, `deriv_fourier_slice`, `iteratedDeriv_fourier_slice`,
> `contDiff_fourier_slice`, `exists_iteratedDeriv_fourier_slice_bound`.

## B. Joint smoothness of the Fourier transformed slices

> - `fourierIntegrand` : The integrand of the partial Fourier transform, as a function of the
>   parameter `(s, ξ)` and the position `y`.
>
> Lemmas: `contDiff_fourierIntegrand`, `fourierIntegrand_eq_zero`, `contDiff_fourier_slice_joint`.

## C. Smoothness of the retarded solution

> Lemmas: `contDiff_fourier_slice_joint_infty`.

## D. Continuous seminorm bounds for Fourier sources

> - `supportedSource` : The native continuous inclusion of fixed-support sources into all compact test
>   sources.
>
> Lemmas: `seminorm_slice_supported_le`, `exists_fourier_supported_seminorm`,
> `exists_fourier_decay_supported_seminorm`.

## E. Continuous source bounds for parameter derivatives

> - `supportedDt` : Time differentiation is a continuous endomorphism of every fixed-support source
>   space.
>
> Lemmas: `supportedSource_dt`, `supportedSource_iterate_dt`,
> `exists_timeDeriv_fourier_supported_seminorm`, `exists_char_timeDeriv_supported_seminorm`.

**`TimeSlice.hasDerivAt_fourier_slice`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L98).

> The time derivative of the Fourier transformed slice is the Fourier transformed slice of the
> time derivative.

```lean
lemma hasDerivAt_fourier_slice (ξ : E) (s : ℝ) :
    HasDerivAt (fun r => 𝓕 (slice F f r) ξ) (𝓕 (slice F (dt F f) s) ξ) s
```

**`TimeSlice.deriv_fourier_slice`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L139).

```lean
lemma deriv_fourier_slice (ξ : E) :
    deriv (fun r => 𝓕 (slice F f r) ξ) = fun s => 𝓕 (slice F (dt F f) s) ξ
```

**`TimeSlice.iteratedDeriv_fourier_slice`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L145).

> The `k`-th time derivative of the Fourier transformed slice.

```lean
lemma iteratedDeriv_fourier_slice (ξ : E) (k : ℕ) :
    ∀ f : 𝓓((⊤ : Opens (ℝ × E)), F), iteratedDeriv k (fun r => 𝓕 (slice F f r) ξ) =
      fun s => 𝓕 (slice F ((dt F)^[k] f) s) ξ
```

**`TimeSlice.contDiff_fourier_slice`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L155).

```lean
lemma contDiff_fourier_slice (ξ : E) (n : ℕ) :
    ∀ f : 𝓓((⊤ : Opens (ℝ × E)), F), ContDiff ℝ n (fun r => 𝓕 (slice F f r) ξ)
```

**`TimeSlice.exists_iteratedDeriv_fourier_slice_bound`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L172).

> All time derivatives of the Fourier transformed slice decay rapidly, uniformly in time.

```lean
lemma exists_iteratedDeriv_fourier_slice_bound (k N : ℕ) :
    ∃ K : ℝ, ∀ (ξ : E) (s : ℝ), ‖iteratedDeriv k (fun r => 𝓕 (slice F f r) ξ) s‖ ≤
      K * (1 + ‖ξ‖) ^ (-(N : ℝ))
```

**`TimeSlice.fourierIntegrand`**, a def, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L186).

> The integrand of the partial Fourier transform, as a function of the parameter `(s, ξ)` and the
> position `y`.

```lean
def fourierIntegrand (z : (ℝ × E) × E) : F
```

**`TimeSlice.contDiff_fourierIntegrand`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L189).

```lean
lemma contDiff_fourierIntegrand : ContDiff ℝ ∞ (fourierIntegrand F f)
```

**`TimeSlice.fourierIntegrand_eq_zero`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L210).

```lean
lemma fourierIntegrand_eq_zero {R : ℝ} (hR : ∀ y ∈ tsupport f, ‖y‖ ≤ R) {y : E} (hy : R < ‖y‖)
    (q : ℝ × E) : fourierIntegrand F f ((q), y) = 0
```

**`TimeSlice.contDiff_fourier_slice_joint`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L220).

> The partial Fourier transform of a spacetime test function is jointly smooth in the time and
> the frequency.

```lean
lemma contDiff_fourier_slice_joint (n : ℕ) :
    ContDiff ℝ n (fun p : ℝ × E => 𝓕 (slice F f p.1) p.2)
```

**`TimeSlice.contDiff_fourier_slice_joint_infty`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L259).

```lean
lemma contDiff_fourier_slice_joint_infty :
    ContDiff ℝ ∞ (fun p : ℝ × E => 𝓕 (slice F f p.1) p.2)
```

**`TimeSlice.supportedSource`**, a def, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L270).

> The native continuous inclusion of fixed-support sources into all compact test sources.

```lean
def supportedSource (K : Compacts (ℝ × E)) :
    ContDiffMapSupportedIn (ℝ × E) F ⊤ K →L[ℝ] 𝓓((⊤ : Opens (ℝ × E)), F)
```

**`TimeSlice.seminorm_slice_supported_le`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L276).

> Every slice seminorm is controlled by a native spacetime source seminorm.

```lean
lemma seminorm_slice_supported_le (K : Compacts (ℝ × E)) {R : ℝ} (hR0 : 0 ≤ R)
    (hR : ∀ p ∈ K, ‖p‖ ≤ R) (f : ContDiffMapSupportedIn (ℝ × E) F ⊤ K)
    (k j : ℕ) (s : ℝ) :
    SchwartzMap.seminorm ℂ k j (slice F (supportedSource F K f) s) ≤
      R ^ k * ContDiffMapSupportedIn.seminorm ℝ (ℝ × E) F ⊤ K j f
```

**`TimeSlice.exists_fourier_supported_seminorm`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L298).

> Fourier moments of all fixed-support sources are controlled by one continuous seminorm.

```lean
lemma exists_fourier_supported_seminorm (K : Compacts (ℝ × E)) (N : ℕ) :
    ∃ q : Seminorm ℝ (ContDiffMapSupportedIn (ℝ × E) F ⊤ K), Continuous q ∧
      ∀ (f : ContDiffMapSupportedIn (ℝ × E) F ⊤ K) (s : ℝ) (ξ : E),
        ‖ξ‖ ^ N * ‖𝓕 (slice F (supportedSource F K f) s) ξ‖ ≤ q f
```

**`TimeSlice.exists_fourier_decay_supported_seminorm`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L337).

> A continuous source seminorm controls arbitrary polynomial Fourier decay uniformly in time.

```lean
lemma exists_fourier_decay_supported_seminorm (K : Compacts (ℝ × E)) (N : ℕ) :
    ∃ q : Seminorm ℝ (ContDiffMapSupportedIn (ℝ × E) F ⊤ K), Continuous q ∧
      ∀ (f : ContDiffMapSupportedIn (ℝ × E) F ⊤ K) (s : ℝ) (ξ : E),
        ‖𝓕 (slice F (supportedSource F K f) s) ξ‖ ≤ q f * (1 + ‖ξ‖) ^ (-(N : ℝ))
```

**`TimeSlice.supportedDt`**, a def, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L359).

> Time differentiation is a continuous endomorphism of every fixed-support source space.

```lean
def supportedDt (K : Compacts (ℝ × E)) :
    ContDiffMapSupportedIn (ℝ × E) F ⊤ K →L[ℝ] ContDiffMapSupportedIn (ℝ × E) F ⊤ K
```

**`TimeSlice.supportedSource_dt`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L365).

```lean
lemma supportedSource_dt (K : Compacts (ℝ × E)) (f : ContDiffMapSupportedIn (ℝ × E) F ⊤ K) :
    supportedSource F K (supportedDt F K f) = dt F (supportedSource F K f)
```

**`TimeSlice.supportedSource_iterate_dt`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L374).

```lean
lemma supportedSource_iterate_dt (K : Compacts (ℝ × E)) (j : ℕ)
    (f : ContDiffMapSupportedIn (ℝ × E) F ⊤ K) :
    supportedSource F K ((supportedDt F K)^[j] f) = (dt F)^[j] (supportedSource F K f)
```

**`TimeSlice.exists_timeDeriv_fourier_supported_seminorm`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L384).

> Time derivatives of Fourier slices are bounded by continuous source seminorms.

```lean
lemma exists_timeDeriv_fourier_supported_seminorm (K : Compacts (ℝ × E)) (j N : ℕ) :
    ∃ q : Seminorm ℝ (ContDiffMapSupportedIn (ℝ × E) F ⊤ K), Continuous q ∧
      ∀ (f : ContDiffMapSupportedIn (ℝ × E) F ⊤ K) (s : ℝ) (ξ : E),
        ‖iteratedDeriv j (fun r => 𝓕 (slice F (supportedSource F K f) r) ξ) s‖ ≤
          q f * (1 + ‖ξ‖) ^ (-(N : ℝ))
```

**`TimeSlice.exists_char_timeDeriv_supported_seminorm`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean#L398).

```lean
lemma exists_char_timeDeriv_supported_seminorm (K : Compacts (ℝ × E)) (i j N : ℕ) :
    ∃ q : Seminorm ℝ (ContDiffMapSupportedIn (ℝ × E) F ⊤ K), Continuous q ∧
      ∀ (f : ContDiffMapSupportedIn (ℝ × E) F ⊤ K) (s : ℝ) (ξ : E),
        (2 * π * ‖ξ‖) ^ i *
          ‖iteratedDeriv j (fun r => 𝓕 (slice F (supportedSource F K f) r) ξ) s‖ ≤
            q f * (1 + ‖ξ‖) ^ (-(N : ℝ))
```

## Depends on

- [Time slices of test functions](timeslice.md)

## Proof depends on

- [Smoothness of parametric integrals](../../part-01/calculus/parametricintegral.md)
- [Fourier integrals and their derivatives](../fourier/integral.md)

## Sources

- [PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceSmooth.lean)
