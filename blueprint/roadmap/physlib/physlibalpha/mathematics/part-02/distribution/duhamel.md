---
declaration: module
origin: cited
lean: Duhamel.propagatedSlice, Duhamel.continuous_propagatedSlice, Duhamel.propagatedSlice_eq_zero_of_notMem, Duhamel.duhamel, Duhamel.integrable_duhamel, Duhamel.exists_timeBound, Duhamel.duhamel_eq_intervalIntegral, Duhamel.duhamel_eq_integral_fourier
statement: formalized
proof: formalized
---

# The Duhamel integral of Fourier multiplied slices

The module `PhyslibAlpha.Mathematics.Distribution.Duhamel`, [PhyslibAlpha/Mathematics/Distribution/Duhamel.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/Duhamel.lean): 8 declarations, 7 with a docstring.

> The slice of a source at each time is propagated by a Fourier multiplier.

## i. Overview

> The slice of a source at each time is propagated by a Fourier multiplier. The Duhamel integral adds
> the contributions of all earlier times.

## ii. Key results

> - `propagatedSlice` : The spatial Fourier propagation of the slice `f(s, ·)` by a multiplier family
>   `m` over the time `r`, evaluated at the position `x`.
> - `duhamel` : The retarded Duhamel integral of the sources `f` for a multiplier family `m`: the
>   source at the time `s` is propagated over the time `t - s` and summed over `s ≤ t`.
> - `continuous_propagatedSlice` : The propagated slices are jointly continuous in the propagation
>   time, the source time and the position, for every multiplier family that is jointly continuous and
>   locally bounded in time.
> - `duhamel_eq_integral_fourier` : The Duhamel integral is the inverse Fourier integral of the
>   per-frequency Duhamel integral of the Fourier transformed slices.

## iv. References

> None.

## A. The Duhamel integral of Fourier multiplied slices

> - `propagatedSlice` : The spatial Fourier propagation of the slice `f(s, ·)` by a multiplier family
>   `m` over the time `r`, evaluated at the position `x`.
> - `duhamel` : The retarded Duhamel integral of the sources `f` for a multiplier family `m`: the
>   source at the time `s` is propagated over the time `t - s` and summed over `s ≤ t`.
>
> Lemmas: `continuous_propagatedSlice`, `propagatedSlice_eq_zero_of_notMem`, `integrable_duhamel`,
> `exists_timeBound`, `duhamel_eq_intervalIntegral`, `duhamel_eq_integral_fourier`.

**`Duhamel.propagatedSlice`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/Duhamel.lean#L71).

> The spatial Fourier propagation of the slice `f(s, ·)` by a multiplier family `m` over the
> time `r`, evaluated at the position `x`. It is independent of the equation: the equation only
> enters through the multiplier family.

```lean
def propagatedSlice (m : ℝ → E → ℂ) (r s : ℝ) (x : E) : F
```

**`Duhamel.continuous_propagatedSlice`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/Duhamel.lean#L77).

> The propagated slices are jointly continuous in the propagation time, the source time and the
> position, for every multiplier family that is jointly continuous and locally bounded in time.

```lean
lemma continuous_propagatedSlice (m : ℝ → E → ℂ)
    (hm : Continuous fun p : ℝ × E => m p.1 p.2)
    (hb : ∀ R : ℝ, ∃ B : ℝ, ∀ r ξ, |r| ≤ R → ‖m r ξ‖ ≤ B) :
    Continuous fun q : ℝ × ℝ × E => propagatedSlice F f m q.1 q.2.1 q.2.2
```

**`Duhamel.propagatedSlice_eq_zero_of_notMem`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/Duhamel.lean#L117).

```lean
lemma propagatedSlice_eq_zero_of_notMem (m : ℝ → E → ℂ) (r : ℝ) {s : ℝ}
    (hs : s ∉ Prod.fst '' tsupport f) (x : E) : propagatedSlice F f m r s x = 0
```

**`Duhamel.duhamel`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/Duhamel.lean#L123).

> The retarded Duhamel integral of the sources `f` for a multiplier family `m`:
> the source at the time `s` is propagated over the time `t - s` and summed over `s ≤ t`.

```lean
def duhamel (m : ℝ → E → ℂ) (t : ℝ) (x : E) : F
```

**`Duhamel.integrable_duhamel`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/Duhamel.lean#L128).

> The integrand of the Duhamel integral is integrable.

```lean
lemma integrable_duhamel (m : ℝ → E → ℂ)
    (hm : Continuous fun p : ℝ × E => m p.1 p.2)
    (hb : ∀ R : ℝ, ∃ B : ℝ, ∀ r ξ, |r| ≤ R → ‖m r ξ‖ ≤ B) (t : ℝ) (x : E) :
    MeasureTheory.Integrable fun s : ℝ => propagatedSlice F f m (t - s) s x
```

**`Duhamel.exists_timeBound`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/Duhamel.lean#L141).

> A time strictly before the support of the source.

```lean
lemma exists_timeBound : ∃ a : ℝ, ∀ s ≤ a, s ∉ Prod.fst '' tsupport f
```

**`Duhamel.duhamel_eq_intervalIntegral`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/Duhamel.lean#L147).

> The Duhamel integral starts at any time before the support of the source.

```lean
lemma duhamel_eq_intervalIntegral (m : ℝ → E → ℂ) {a : ℝ}
    (ha : ∀ s ≤ a, s ∉ Prod.fst '' tsupport f) {t : ℝ} (hat : a ≤ t) (x : E) :
    duhamel F f m t x = ∫ s in a..t, propagatedSlice F f m (t - s) s x
```

**`Duhamel.duhamel_eq_integral_fourier`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/Duhamel.lean#L161).

> The Duhamel integral is the inverse Fourier integral of the per-frequency Duhamel integral
> of the Fourier transformed slices.

```lean
lemma duhamel_eq_integral_fourier (m : ℝ → E → ℂ)
    (hm : Continuous fun p : ℝ × E => m p.1 p.2)
    (hb : ∀ R : ℝ, ∃ B : ℝ, ∀ r ξ, |r| ≤ R → ‖m r ξ‖ ≤ B) {a : ℝ}
    (ha : ∀ s ≤ a, s ∉ Prod.fst '' tsupport f) {t : ℝ} (hat : a ≤ t) (x : E) :
    duhamel F f m t x =
      ∫ ξ : E, 𝐞 (inner ℝ ξ x) • ∫ s in a..t, m (t - s) ξ • 𝓕 (slice F f s) ξ
```

## Depends on

- [Time slices of test functions](timeslice.md)

## Sources

- [PhyslibAlpha/Mathematics/Distribution/Duhamel.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/Duhamel.lean)
