---
declaration: module
origin: cited
lean: KleinGordon.hasCompactSupport_solution_slice, KleinGordon.solutionSlice, KleinGordon.solutionSlice_apply, KleinGordon.integrable_pairing_integrand, KleinGordon.solutionSlice_pairing, KleinGordon.sineEvolution_apply_eq_delta, KleinGordon.advancedSolution_eq_integral, KleinGordon.advancedSolution_eq_dirac
statement: formalized
proof: formalized
---

# The solution as a tempered distribution in space

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.TemperedSlice`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/TemperedSlice.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/TemperedSlice.lean): 8 declarations, 7 with a docstring.

## i. Overview

> At each time the retarded solution pairs with Schwartz functions through the sine evolution of the
> source slices.

## ii. Key results

> - `solutionSlice` : The spatial slice of the retarded solution as a Schwartz function.
> - `solutionSlice_pairing` : **The retarded solution as a tempered distribution.** Tested against a
>   Schwartz function `g` the spatial slice of the retarded solution at the time `t` is the integral
>   over the source time `s ≤ t` of the Fourier multiplier `sincPropagator (t - s)` applied to the
>   tempered slice of the source.
> - `advancedSolution_eq_dirac` : **Advanced response at a point.** The advanced solution at the point
>   `(t, y)` is the integral over the later source times of the pairing of the propagated Dirac
>   distribution at `y` with the slice of the source.
> - `sineEvolution_apply_eq_delta` : The propagation of a Schwartz function at a point is the pairing
>   of the propagated Dirac distribution with it.

## iv. References

> None.

## A. The retarded solution as a tempered distribution in space

> - `solutionSlice` : The spatial slice of the retarded solution as a Schwartz function.
>
> Lemmas: `hasCompactSupport_solution_slice`, `solutionSlice_apply`, `integrable_pairing_integrand`,
> `solutionSlice_pairing`, `sineEvolution_apply_eq_delta`, `advancedSolution_eq_integral`,
> `advancedSolution_eq_dirac`.

**`KleinGordon.hasCompactSupport_solution_slice`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/TemperedSlice.lean#L67).

> The spatial slice of the retarded solution has compact support.

```lean
lemma hasCompactSupport_solution_slice {μ : ℝ} (hμ : 0 ≤ μ) (t : ℝ) :
    HasCompactSupport fun x : E => solution F f μ t x
```

**`KleinGordon.solutionSlice`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/TemperedSlice.lean#L87).

> The spatial slice of the retarded solution as a Schwartz function.

```lean
def solutionSlice {μ : ℝ} (hμ : 0 ≤ μ) (t : ℝ) : 𝓢(E, F)
```

**`KleinGordon.solutionSlice_apply`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/TemperedSlice.lean#L92).

```lean
lemma solutionSlice_apply {μ : ℝ} (hμ : 0 ≤ μ) (t : ℝ) (x : E) :
    solutionSlice F f hμ t x = solution F f μ t x
```

**`KleinGordon.integrable_pairing_integrand`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/TemperedSlice.lean#L96).

> The integrand of the Duhamel pairing is integrable on the product of space and past times.

```lean
lemma integrable_pairing_integrand {μ : ℝ} (hμ : 0 ≤ μ) (t : ℝ) (g : 𝓢(E, ℂ)) :
    Integrable (fun q : E × ℝ => g q.1 • sineEvolution F (t - q.2) μ (slice F f q.2) q.1)
      ((volume : Measure E).prod (volume.restrict (Set.Iic t)))
```

**`KleinGordon.solutionSlice_pairing`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/TemperedSlice.lean#L146).

> **The retarded solution as a tempered distribution.** Tested against a Schwartz function `g`
> the spatial slice of the retarded solution at the time `t` is the integral over the source time
> `s ≤ t` of the Fourier multiplier `sincPropagator (t - s)` applied to the tempered slice of the
> source.

```lean
lemma solutionSlice_pairing {μ : ℝ} (hμ : 0 ≤ μ) (t : ℝ) (g : 𝓢(E, ℂ)) :
    (solutionSlice F f hμ t : 𝓢'(E, F)) g =
      ∫ s in Set.Iic t, sineEvolutionTempered F (t - s) μ (slice F f s : 𝓢'(E, F)) g
```

**`KleinGordon.sineEvolution_apply_eq_delta`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/TemperedSlice.lean#L160).

> The propagation of a Schwartz function at a point is the pairing of the propagated Dirac
> distribution with it.

```lean
lemma sineEvolution_apply_eq_delta {μ : ℝ} (hμ : 0 ≤ μ) (r : ℝ) (g : 𝓢(E, ℂ)) (y : E) :
    sineEvolution ℂ r μ g y =
      sineEvolutionTempered ℂ r μ (TemperedDistribution.delta y) g
```

**`KleinGordon.advancedSolution_eq_integral`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/TemperedSlice.lean#L174).

> The advanced solution is the integral over the later source times.

```lean
lemma advancedSolution_eq_integral {μ : ℝ} (hμ : 0 ≤ μ) (t : ℝ) (y : E) :
    advancedSolution F f μ t y =
      ∫ s in Set.Ioi t, sineEvolution F (s - t) μ (slice F f s) y
```

**`KleinGordon.advancedSolution_eq_dirac`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/TemperedSlice.lean#L194).

> **Advanced response at a point.** The advanced solution at the point `(t, y)` is the integral
> over the later source times of the pairing of the propagated Dirac distribution at `y` with the
> slice of the source. By transposition this is the retarded response of a point source.

```lean
lemma advancedSolution_eq_dirac {μ : ℝ} (hμ : 0 ≤ μ) (f : 𝓓((⊤ : Opens (ℝ × D)), ℂ))
    (t : ℝ) (y : D) :
    advancedSolution ℂ f μ t y =
      ∫ s in Set.Ioi t, sineEvolutionTempered ℂ (s - t) μ (TemperedDistribution.delta y)
        (slice ℂ f s)
```

## Depends on

- [The retarded and advanced solution](retardedsolution.md)

## Proof depends on

- [Finite propagation speed](finitepropagation.md)
- [Smoothness of the retarded solution](smoothness.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/TemperedSlice.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/TemperedSlice.lean)
