---
declaration: module
origin: cited
lean: TimeSlice.spaceFourier, TimeSlice.hasCompactSupport_spaceFourier, TimeSlice.contDiff_spaceFourier, TimeSlice.spaceFourierSchwartz, TimeSlice.timeFourier, TimeSlice.spaceFourier_eq_integral, TimeSlice.timeFourier_eq_integral, TimeSlice.continuous_timeFourier
statement: formalized
proof: formalized
---

# The space and time Fourier transform of a test function

The module `PhyslibAlpha.Mathematics.Distribution.TimeSliceFourier`, [PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean): 12 declarations, 9 with a docstring.

> A test function on time and space is transformed in the space variable and then in the time
> variable.

## i. Overview

> The spatial transform of the slices of a test function is a smooth function of the time with
> compact support. It is therefore a Schwartz function of the time. Its transform in the time is the
> spacetime transform in the split variables. Fourier inversion in the time recovers the spatial
> transform. The Schwartz seminorms and the integral over the frequency decay faster than every
> power of the wave vector.

## ii. Key results

> - `TimeSlice.spaceFourier` : the spatial transform of the slices.
> - `TimeSlice.timeFourier` : the transform in the time of the spatial transform.
> - `TimeSlice.spaceFourier_eq_integral` : Fourier inversion in the time.
> - `TimeSlice.exists_integral_norm_timeFourier_le` : decay of the integral over the frequency.

## iv. References

> None.

## A. The transforms

> - `TimeSlice.spaceFourier` : the spatial transform of the slices.
> - `TimeSlice.spaceFourierSchwartz` : the spatial transform as a Schwartz function of the time.
> - `TimeSlice.timeFourier` : the transform in the time of the spatial transform.
> - `TimeSlice.spaceFourier_eq_integral` : Fourier inversion in the time.
> - `TimeSlice.timeFourier_eq_integral` : the time transform as an integral.

## B. Properties of the time transform

> - `TimeSlice.continuous_timeFourier` : joint continuity.
> - `TimeSlice.timeFourier_reflect` : reflecting the source reflects the frequency.
> - `TimeSlice.integrable_timeFourier` : integrability in the frequency.

## C. Decay in the wave vector

> - `TimeSlice.exists_seminorm_spaceFourier_le` : decay of the Schwartz seminorms.
> - `TimeSlice.exists_integral_norm_timeFourier_le` : decay of the integral over the frequency.

**`TimeSlice.spaceFourier`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean#L77).

> The spatial transform of the slices of `ψ` at the frequency `ξ` as a function of the time.

```lean
def spaceFourier (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (ξ : E) (s : ℝ) : ℂ
```

**`TimeSlice.hasCompactSupport_spaceFourier`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean#L79).

```lean
lemma hasCompactSupport_spaceFourier (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (ξ : E) :
    HasCompactSupport (spaceFourier ψ ξ)
```

**`TimeSlice.contDiff_spaceFourier`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean#L84).

```lean
lemma contDiff_spaceFourier (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (ξ : E) :
    ContDiff ℝ ∞ (spaceFourier ψ ξ)
```

**`TimeSlice.spaceFourierSchwartz`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean#L89).

> The spatial transform of a test function is a Schwartz function of the time.

```lean
def spaceFourierSchwartz (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (ξ : E) : 𝓢(ℝ, ℂ)
```

**`TimeSlice.timeFourier`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean#L93).

> The transform in the time of the spatial transform.

```lean
def timeFourier (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (w : ℝ) (ξ : E) : ℂ
```

**`TimeSlice.spaceFourier_eq_integral`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean#L98).

> **Fourier inversion in the time.** The spatial transform of a slice is the inverse transform
> in the time of `timeFourier`.

```lean
lemma spaceFourier_eq_integral (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (ξ : E) (s : ℝ) :
    spaceFourier ψ ξ s = ∫ w : ℝ, (𝐞 (s * w) : ℂ) • timeFourier ψ w ξ
```

**`TimeSlice.timeFourier_eq_integral`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean#L104).

> The transform in the time as an integral.

```lean
lemma timeFourier_eq_integral (χ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (v : ℝ) (ξ : E) :
    timeFourier χ v ξ = ∫ s : ℝ, (𝐞 (-(s * v)) : ℂ) • spaceFourier χ ξ s
```

**`TimeSlice.continuous_timeFourier`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean#L111).

> The transformed test function is jointly continuous in the frequency and the wave vector.

```lean
lemma continuous_timeFourier (χ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) :
    Continuous fun p : ℝ × E => timeFourier χ p.1 p.2
```

**`TimeSlice.timeFourier_reflect`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean#L132).

> Reflecting the source in the time reflects the frequency.

```lean
lemma timeFourier_reflect (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (w : ℝ) (ξ : E) :
    timeFourier (reflect ℂ ψ) w ξ = timeFourier ψ (-w) ξ
```

**`TimeSlice.integrable_timeFourier`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean#L141).

```lean
lemma integrable_timeFourier (χ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (ξ : E) :
    Integrable fun w : ℝ => timeFourier χ w ξ
```

**`TimeSlice.exists_seminorm_spaceFourier_le`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean#L146).

> The Schwartz seminorms of the spatial transform of a test function decay in the frequency.

```lean
lemma exists_seminorm_spaceFourier_le (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (N k p : ℕ) :
    ∃ B : ℝ, ∀ ξ : E, SchwartzMap.seminorm ℂ k p (spaceFourierSchwartz ψ ξ) ≤
      B * (1 + ‖ξ‖) ^ (-(N : ℝ))
```

**`TimeSlice.exists_integral_norm_timeFourier_le`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean#L182).

> The integral over the frequency of the transformed test function decays in `ξ`.

```lean
lemma exists_integral_norm_timeFourier_le (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (N : ℕ) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ ξ : E, ∫ w : ℝ, ‖timeFourier ψ w ξ‖ ≤ C * (1 + ‖ξ‖) ^ (-(N : ℝ))
```

## Depends on

- [Time slices of test functions](timeslice.md)

## Proof depends on

- [Smoothness and bounds of time slices](timeslicesmooth.md)
- [Fourier inversion for Schwartz functions on the line](../fourier/inversion.md)
- [The integral of a Fourier transform is bounded by Schwartz seminorms](../fourier/schwartzdecay.md)

## Sources

- [PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSliceFourier.lean)
