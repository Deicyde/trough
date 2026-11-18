---
declaration: module
origin: cited
lean: TimeSlice.isClosedEmbedding_prodMk, TimeSlice.hasCompactSupport_slice, TimeSlice.contDiff_slice, TimeSlice.slice, TimeSlice.slice_apply, TimeSlice.norm_iteratedFDeriv_slice_le, TimeSlice.exists_bound_iteratedFDeriv, TimeSlice.exists_radius
statement: formalized
proof: formalized
---

# Time slices of test functions

The module `PhyslibAlpha.Mathematics.Distribution.TimeSlice`, [PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean): 41 declarations, 14 with a docstring.

> A test function on time and space has a Schwartz function as its slice at a fixed time.

## i. Overview

> A test function on time and space has a Schwartz function as its slice at a fixed time. Time and
> space derivatives and the time reflection commute with slicing.

## ii. Key results

> - `slice` : The slice `f(s, ·)` of a spacetime test function at the time `s` is a Schwartz function.
> - `timeReflect` : Reflection in time.
> - `reflect` : The time-reflected test function.
> - `dt` : The time derivative of a spacetime test function.
> - `reflectSourceCLM` : Time reflection acts continuously on the native compact source space.
> - `timeReflectionCLE` : Time reflection on time-space coordinates.
> - `dx` : Spatial differentiation of a spacetime test field in the direction `m`.
> - `spatialLaplacian` : The spatial Laplacian on compact spacetime test fields.

## iv. References

> None.

## A. Time slices of test functions

> - `slice` : The slice `f(s, ·)` of a spacetime test function at the time `s` is a Schwartz function.
>
> Lemmas: `isClosedEmbedding_prodMk`, `hasCompactSupport_slice`, `contDiff_slice`, `slice_apply`,
> `norm_iteratedFDeriv_slice_le`, `exists_bound_iteratedFDeriv`, `exists_radius`,
> `exists_seminorm_slice_le`, `exists_fourier_bound`, `exists_fourier_decay_pow` and more.

## B. Causal support of the retarded solution

> - `timeReflect` : Reflection in time.
> - `reflect` : The time-reflected test function.
>
> Lemmas: `timeReflect_apply`, `reflect_apply`, `tsupport_reflect`, `slice_add`, `slice_smul`.

## C. The time dependence of the Fourier transformed slices

> - `dt` : The time derivative of a spacetime test function.
>
> Lemmas: `dt_apply`, `hasDerivAt_time`.

## D. Continuous seminorm bounds for Fourier sources

> - `reflectSourceCLM` : Time reflection acts continuously on the native compact source space.
>
> Lemmas: `reflectSourceCLM_eq`.

## E. Continuous compactly cut off advanced response

> - `timeReflectionCLE` : Time reflection on time-space coordinates.
>
> Lemmas: `timeReflectionCLE_apply`.

## F. The two-sided Klein–Gordon inverse on compact test fields

> - `dx` : Spatial differentiation of a spacetime test field in the direction `m`.
> - `spatialLaplacian` : The spatial Laplacian on compact spacetime test fields.
>
> Lemmas: `slice_dx`, `slice_spatialLaplacian`, `dt_reflect`, `dt_neg`, `dt_dt_reflect`,
> `slice_reflect`, `dx_reflect`, `spatialLaplacian_reflect`.

**`TimeSlice.isClosedEmbedding_prodMk`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L106).

```lean
lemma isClosedEmbedding_prodMk (s : ℝ) : IsClosedEmbedding fun x : E => (s, x)
```

**`TimeSlice.hasCompactSupport_slice`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L114).

```lean
lemma hasCompactSupport_slice (s : ℝ) : HasCompactSupport fun x : E => f (s, x)
```

**`TimeSlice.contDiff_slice`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L118).

```lean
lemma contDiff_slice (s : ℝ) : ContDiff ℝ ∞ fun x : E => f (s, x)
```

**`TimeSlice.slice`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L122).

> The slice `f(s, ·)` of a spacetime test function at the time `s` is a Schwartz function.

```lean
def slice (s : ℝ) : 𝓢(E, F)
```

**`TimeSlice.slice_apply`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L127).

```lean
lemma slice_apply (s : ℝ) (x : E) : slice F f s x = f (s, x)
```

**`TimeSlice.norm_iteratedFDeriv_slice_le`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L131).

> The derivatives of a slice are bounded by the derivatives of the spacetime function.

```lean
lemma norm_iteratedFDeriv_slice_le (p : ℕ) (s : ℝ) (x : E) :
    ‖iteratedFDeriv ℝ p (fun x : E => f (s, x)) x‖ ≤ ‖iteratedFDeriv ℝ p f (s, x)‖
```

**`TimeSlice.exists_bound_iteratedFDeriv`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L150).

```lean
lemma exists_bound_iteratedFDeriv (p : ℕ) :
    ∃ M : ℝ, ∀ y : ℝ × E, ‖iteratedFDeriv ℝ p f y‖ ≤ M
```

**`TimeSlice.exists_radius`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L160).

```lean
lemma exists_radius : ∃ R : ℝ, 0 ≤ R ∧ ∀ y ∈ tsupport f, ‖y‖ ≤ R
```

**`TimeSlice.exists_seminorm_slice_le`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L166).

> The Schwartz seminorms of the slices are bounded uniformly in the time.

```lean
lemma exists_seminorm_slice_le (k p : ℕ) :
    ∃ C : ℝ, ∀ s, SchwartzMap.seminorm ℂ k p (slice F f s) ≤ C
```

**`TimeSlice.exists_fourier_bound`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L190).

> The Fourier transforms of the slices decay uniformly in the time.

```lean
lemma exists_fourier_bound (N : ℕ) :
    ∃ C : ℝ, ∀ s (ξ : E), ‖ξ‖ ^ N * ‖𝓕 (slice F f s) ξ‖ ≤ C
```

**`TimeSlice.exists_fourier_decay_pow`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L219).

> Polynomial decay of any order of the Fourier transforms of the slices, uniformly in the
> time.

```lean
lemma exists_fourier_decay_pow (N : ℕ) :
    ∃ K : ℝ, ∀ s (ξ : E), ‖𝓕 (slice F f s) ξ‖ ≤ K * (1 + ‖ξ‖) ^ (-(N : ℝ))
```

**`TimeSlice.exists_fourier_decay`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L238).

```lean
lemma exists_fourier_decay :
    ∃ K : ℝ, ∀ s (ξ : E), ‖𝓕 (slice F f s) ξ‖ ≤ K * (1 + ‖ξ‖) ^ (-((Module.finrank ℝ E + 1 : ℕ) :
      ℝ))
```

**`TimeSlice.fourier_slice_apply`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L244).

```lean
lemma fourier_slice_apply (s : ℝ) (ξ : E) :
    𝓕 (slice F f s) ξ = ∫ x : E, 𝐞 (-inner ℝ x ξ) • f (s, x)
```

**`TimeSlice.continuous_fourier_slice`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L250).

```lean
lemma continuous_fourier_slice :
    Continuous fun p : ℝ × E => 𝓕 (slice F f p.1) p.2
```

**`TimeSlice.slice_eq_zero_of_notMem`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L281).

```lean
lemma slice_eq_zero_of_notMem {s : ℝ} (hs : s ∉ Prod.fst '' tsupport f) : slice F f s = 0
```

**`TimeSlice.isCompact_timeSupport`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L288).

> The time support of a spacetime test function is compact.

```lean
lemma isCompact_timeSupport : IsCompact (Prod.fst '' tsupport f)
```

**`TimeSlice.timeReflect`**, a def, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L298).

> Reflection in time.

```lean
def timeReflect : ℝ × E ≃ₜ ℝ × E
```

**`TimeSlice.timeReflect_apply`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L302).

```lean
lemma timeReflect_apply (p : ℝ × E) : timeReflect p = (-p.1, p.2)
```

**`TimeSlice.reflect`**, a def, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L305).

> The time-reflected test function.

```lean
def reflect : 𝓓((⊤ : Opens (ℝ × E)), F)
```

**`TimeSlice.reflect_apply`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L312).

```lean
lemma reflect_apply (p : ℝ × E) : reflect F f p = f (-p.1, p.2)
```

**`TimeSlice.reflect_reflect`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L316).

> Time reflection is an involution.

```lean
lemma reflect_reflect : reflect F (reflect F f) = f
```

**`TimeSlice.tsupport_reflect`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L321).

```lean
lemma tsupport_reflect : tsupport (reflect F f) = timeReflect ⁻¹' tsupport f
```

**`TimeSlice.slice_add`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L326).

```lean
lemma slice_add (g : 𝓓((⊤ : Opens (ℝ × E)), F)) (s : ℝ) :
    slice F (f + g) s = slice F f s + slice F g s
```

**`TimeSlice.slice_smul`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L331).

```lean
lemma slice_smul (c : ℝ) (s : ℝ) : slice F (c • f) s = c • slice F f s
```

**`TimeSlice.dt`**, a def, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L335).

> The time derivative of a spacetime test function.

```lean
def dt : 𝓓((⊤ : Opens (ℝ × E)), F)
```

**`TimeSlice.dt_apply`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L339).

```lean
lemma dt_apply (p : ℝ × E) : dt F f p = lineDeriv ℝ f p ((1 : ℝ), (0 : E))
```

**`TimeSlice.hasDerivAt_time`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L344).

```lean
lemma hasDerivAt_time (s : ℝ) (y : E) : HasDerivAt (fun r : ℝ => f (r, y)) (dt F f (s, y)) s
```

**`TimeSlice.reflectSourceCLM`**, a def, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L361).

> Time reflection acts continuously on the native compact source space.

```lean
def reflectSourceCLM :
    𝓓((⊤ : Opens (ℝ × E)), F) →L[ℝ] 𝓓((⊤ : Opens (ℝ × E)), F)
```

**`TimeSlice.reflectSourceCLM_eq`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L367).

```lean
lemma reflectSourceCLM_eq (f : 𝓓((⊤ : Opens (ℝ × E)), F)) :
    reflectSourceCLM F f = reflect F f
```

**`TimeSlice.timeReflectionCLE`**, a def, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L373).

> Time reflection on time-space coordinates.

```lean
def timeReflectionCLE (E : Type u) [NormedAddCommGroup E] [NormedSpace ℝ E] :
    (ℝ × E) ≃L[ℝ] (ℝ × E)
```

**`TimeSlice.timeReflectionCLE_apply`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L378).

```lean
lemma timeReflectionCLE_apply (p : ℝ × E) : timeReflectionCLE E p = (-p.1, p.2)
```

**`TimeSlice.dx`**, a def, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L387).

> Spatial differentiation of a spacetime test field in the direction `m`.

```lean
def dx (m : E) : 𝓓((⊤ : Opens (ℝ × E)), F)
```

**`TimeSlice.slice_dx`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L391).

```lean
lemma slice_dx (m : E) (s : ℝ) : slice F (dx F f m) s = ∂_{m} (slice F f s)
```

**`TimeSlice.spatialLaplacian`**, a def, [line 403](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L403).

> The spatial Laplacian on compact spacetime test fields.

```lean
def spatialLaplacian : 𝓓((⊤ : Opens (ℝ × E)), F)
```

**`TimeSlice.slice_spatialLaplacian`**, a lemma, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L407).

```lean
lemma slice_spatialLaplacian (s : ℝ) :
    slice F (spatialLaplacian F f) s = Δ (slice F f s)
```

**`TimeSlice.dt_reflect`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L417).

```lean
lemma dt_reflect : dt F (reflect F f) = -reflect F (dt F f)
```

**`TimeSlice.dt_neg`**, a lemma, [line 424](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L424).

```lean
lemma dt_neg : dt F (-f) = -dt F f
```

**`TimeSlice.dt_dt_reflect`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L427).

```lean
lemma dt_dt_reflect : dt F (dt F (reflect F f)) = reflect F (dt F (dt F f))
```

**`TimeSlice.slice_reflect`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L433).

```lean
lemma slice_reflect (s : ℝ) : slice F (reflect F f) s = slice F f (-s)
```

**`TimeSlice.dx_reflect`**, a lemma, [line 437](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L437).

```lean
lemma dx_reflect (m : E) : dx F (reflect F f) m = reflect F (dx F f m)
```

**`TimeSlice.spatialLaplacian_reflect`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean#L443).

```lean
lemma spatialLaplacian_reflect :
    spatialLaplacian F (reflect F f) = reflect F (spatialLaplacian F f)
```

## Depends on

- [Operations on test functions](testfunction.md)

## Sources

- [PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/TimeSlice.lean)
