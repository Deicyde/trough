---
declaration: module
origin: cited
lean: KleinGordon.dispersion, KleinGordon.dispersion_zero, KleinGordon.multiplier, KleinGordon.norm_multiplier_le, KleinGordon.multiplier_eq, KleinGordon.hasTemperateGrowth_comp_sincSqrt, KleinGordon.hasTemperateGrowth_comp_cosSqrt, KleinGordon.hasTemperateGrowth_multiplier
statement: formalized
proof: formalized
---

# The propagation multiplier

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.Multiplier`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean): 20 declarations, 7 with a docstring.

> The dispersion relation and the sine and cosine multipliers of the Klein–Gordon evolution.

## i. Overview

> The dispersion relation and the sine and cosine multipliers of the Klein–Gordon evolution. They are
> smooth and have temperate growth.

## ii. Key results

> - `dispersion` : The dispersion `√((2π)² ‖ξ‖² + μ)` of the Klein–Gordon equation with mass parameter
>   `μ`.
> - `multiplier` : The Fourier multiplier of the propagation over the time `t`.
> - `cosMultiplier` : The Fourier multiplier `cos (ω t)`.
> - `frequencySq` : The Fourier multiplier `ω² = (2π)² ‖ξ‖² + μ`.

## iv. References

> None.

## A. The Klein–Gordon propagation multiplier

> - `dispersion` : The dispersion `√((2π)² ‖ξ‖² + μ)` of the Klein–Gordon equation with mass parameter
>   `μ`.
> - `multiplier` : The Fourier multiplier of the propagation over the time `t`.
>
> Lemmas: `dispersion_zero`, `norm_multiplier_le`, `multiplier_eq`,
> `hasTemperateGrowth_comp_sincSqrt`, `hasTemperateGrowth_comp_cosSqrt`,
> `hasTemperateGrowth_multiplier`.

## B. The free Klein–Gordon evolution and its group law

> - `cosMultiplier` : The Fourier multiplier `cos (ω t)`.
> - `frequencySq` : The Fourier multiplier `ω² = (2π)² ‖ξ‖² + μ`.
>
> Lemmas: `cosMultiplier_eq`, `hasTemperateGrowth_cosMultiplier`, `hasTemperateGrowth_frequencySq`.

## C. The propagation multiplier

> Lemmas: `continuous_dispersion`, `continuous_multiplier_uncurry`.

## D. The homogeneous Klein–Gordon evolution of Schwartz data

> Lemmas: `continuous_cosMultiplier_uncurry`, `continuous_frequencySq`.

## E. The retarded Klein–Gordon solution of a test-function source

> Lemmas: `dispersion_sq_le`.

## F. Smoothness of the retarded solution

> Lemmas: `contDiff_multiplier_joint`.

## G. The retarded solution as a tempered distribution in space

> Lemmas: `multiplier_neg`.

**`KleinGordon.dispersion`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L97).

> The dispersion `√((2π)² ‖ξ‖² + μ)` of the Klein–Gordon equation with mass parameter `μ`.

```lean
def dispersion (μ : ℝ) (ξ : E) : ℝ
```

**`KleinGordon.dispersion_zero`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L100).

> The massless dispersion is the norm of the frequency.

```lean
lemma dispersion_zero (ξ : E) : dispersion 0 ξ = 2 * Real.pi * ‖ξ‖
```

**`KleinGordon.multiplier`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L106).

> The Fourier multiplier of the propagation over the time `t`.

```lean
def multiplier (t μ : ℝ) (ξ : E) : ℂ
```

**`KleinGordon.norm_multiplier_le`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L108).

```lean
lemma norm_multiplier_le (t μ : ℝ) (ξ : E) : ‖multiplier t μ ξ‖ ≤ |t|
```

**`KleinGordon.multiplier_eq`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L112).

> For `μ ≥ 0` the multiplier is the entire function `t * sincSqrt` of `t² ω²`.

```lean
lemma multiplier_eq (t : ℝ) {μ : ℝ} (hμ : 0 ≤ μ) (ξ : E) :
    multiplier t μ ξ = ((t * sincSqrt (t ^ 2 * ((2 * π) ^ 2 * ‖ξ‖ ^ 2 + μ)) : ℝ) : ℂ)
```

**`KleinGordon.hasTemperateGrowth_comp_sincSqrt`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L121).

```lean
lemma hasTemperateGrowth_comp_sincSqrt (t : ℝ) {q : E → ℝ} (hq : q.HasTemperateGrowth)
    (hq0 : ∀ ξ, 0 ≤ q ξ) : (fun ξ => t * sincSqrt (q ξ)).HasTemperateGrowth
```

**`KleinGordon.hasTemperateGrowth_comp_cosSqrt`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L131).

```lean
lemma hasTemperateGrowth_comp_cosSqrt {q : E → ℝ} (hq : q.HasTemperateGrowth)
    (hq0 : ∀ ξ, 0 ≤ q ξ) : (fun ξ => cosSqrt (q ξ)).HasTemperateGrowth
```

**`KleinGordon.hasTemperateGrowth_multiplier`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L138).

> The propagation multiplier has temperate growth, also for `μ = 0`.

```lean
lemma hasTemperateGrowth_multiplier (t : ℝ) {μ : ℝ} (hμ : 0 ≤ μ) :
    (multiplier t μ : E → ℂ).HasTemperateGrowth
```

**`KleinGordon.cosMultiplier`**, a def, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L155).

> The Fourier multiplier `cos (ω t)`.

```lean
def cosMultiplier (t μ : ℝ) (ξ : E) : ℂ
```

**`KleinGordon.frequencySq`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L158).

> The Fourier multiplier `ω² = (2π)² ‖ξ‖² + μ`.

```lean
def frequencySq (μ : ℝ) (ξ : E) : ℂ
```

**`KleinGordon.cosMultiplier_eq`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L160).

```lean
lemma cosMultiplier_eq (t : ℝ) {μ : ℝ} (hμ : 0 ≤ μ) (ξ : E) :
    cosMultiplier t μ ξ = (cosSqrt (t ^ 2 * ((2 * π) ^ 2 * ‖ξ‖ ^ 2 + μ)) : ℝ)
```

**`KleinGordon.hasTemperateGrowth_cosMultiplier`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L177).

```lean
lemma hasTemperateGrowth_cosMultiplier (t : ℝ) {μ : ℝ} (hμ : 0 ≤ μ) :
    (cosMultiplier t μ : E → ℂ).HasTemperateGrowth
```

**`KleinGordon.hasTemperateGrowth_frequencySq`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L190).

```lean
lemma hasTemperateGrowth_frequencySq (μ : ℝ) :
    (frequencySq μ : E → ℂ).HasTemperateGrowth
```

**`KleinGordon.continuous_dispersion`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L199).

```lean
lemma continuous_dispersion (μ : ℝ) : Continuous fun ξ : E => dispersion μ ξ
```

**`KleinGordon.continuous_multiplier_uncurry`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L204).

```lean
lemma continuous_multiplier_uncurry (μ : ℝ) :
    Continuous fun p : ℝ × E => multiplier p.1 μ p.2
```

**`KleinGordon.continuous_cosMultiplier_uncurry`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L217).

```lean
lemma continuous_cosMultiplier_uncurry (μ : ℝ) :
    Continuous fun p : ℝ × E => cosMultiplier p.1 μ p.2
```

**`KleinGordon.continuous_frequencySq`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L224).

```lean
lemma continuous_frequencySq : Continuous fun ξ : E => frequencySq (E := E) μ ξ
```

**`KleinGordon.dispersion_sq_le`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L228).

```lean
lemma dispersion_sq_le {μ : ℝ} (hμ : 0 ≤ μ) (ξ : E) :
    dispersion μ ξ ^ 2 ≤ ((2 * π) ^ 2 + μ) * (1 + ‖ξ‖) ^ 2
```

**`KleinGordon.contDiff_multiplier_joint`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L240).

```lean
lemma contDiff_multiplier_joint {μ : ℝ} (hμ : 0 ≤ μ) :
    ContDiff ℝ ∞ fun z : ℝ × E => multiplier z.1 μ z.2
```

**`KleinGordon.multiplier_neg`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean#L255).

```lean
lemma multiplier_neg (r μ : ℝ) (ξ : E) : multiplier r μ (-ξ) = multiplier r μ ξ
```

## Depends on

- [The sine propagation function `t ↦ sin (ω t) / ω`](../../../mathematics/part-02/specialfunctions/sincpropagator-basic.md)

## Proof depends on

- [Fourier multipliers on Schwartz functions](../../../mathematics/part-02/distribution/fouriermultiplier.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Multiplier.lean)
