---
declaration: module
origin: cited
lean: WaveEquation.Kirchhoff.wavePropagator_fourier_of_pos, WaveEquation.Kirchhoff.sphericalIntegral_eq_zero_of_forall, WaveEquation.Kirchhoff.wavePropagator_eq_zero_of_far_of_pos, WaveEquation.Kirchhoff.wavePropagator_eq_zero_of_near_of_pos, WaveEquation.Kirchhoff.sphericalIntegral_neg, WaveEquation.Kirchhoff.wavePropagator_zero, WaveEquation.Kirchhoff.wavePropagator_neg, WaveEquation.Kirchhoff.wavePropagator_eq_of_eq_on_sphere
statement: formalized
proof: formalized
---

# Properties of the wave propagator

The module `PhyslibAlpha.ClassicalFieldTheory.WaveEquation.Kirchhoff.Propagator`, [PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean): 13 declarations, 12 with a docstring.

> The wave propagator has the Fourier multiplier `sin(ω t) / ω`, finite propagation speed and the
> Huygens property.

## i. Overview

> The multiplier is `sin(ω t) / ω` with `ω = 2π c |ξ|`. A function supported in a ball is carried by
> the
> propagator to the shell around the ball. Points inside the light cone of the support see nothing.
> The propagator is odd in time. The statements are first proved for positive time. The oddness of the
> spherical integral extends them to negative time.

## ii. Key results

> * `wavePropagator_fourier`: the Fourier multiplier.
> * `wavePropagator_eq_zero_of_far`: finite propagation speed.
> * `wavePropagator_eq_zero_of_near`: Huygens' principle.
> * `wavePropagator_neg`: oddness in time.
> * `wavePropagator_eq_of_eq_on_sphere`: the field depends on the data only on a sphere.
> * `wavePropagator_isWavePropagator`: the three properties together.

## iv. References

> * None.

## A. The Fourier multiplier for positive time

**`WaveEquation.Kirchhoff.wavePropagator_fourier_of_pos`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean#L55).

> **Kirchhoff's formula in Fourier space.** For `c > 0`, `t > 0` and `ξ ≠ 0` the mean has the
> Fourier multiplier `sin(ω t) / ω` with `ω = 2π c |ξ|`, the wave propagator multiplier.

```lean
lemma wavePropagator_fourier_of_pos (f : 𝓢(Space 3, ℂ)) {c t : ℝ} (hc : 0 < c) (ht : 0 < t)
    {ξ : Space 3} (hξ : ξ ≠ 0) :
    ∫ x : Space 3, phase (inner ℝ x ξ) * wavePropagator c t f x =
      ((Real.sin (2 * Real.pi * c * ‖ξ‖ * t) / (2 * Real.pi * c * ‖ξ‖) : ℝ) : ℂ) *
        ∫ x : Space 3, phase (inner ℝ x ξ) * f x
```

## B. Light-cone support for positive time

**`WaveEquation.Kirchhoff.sphericalIntegral_eq_zero_of_forall`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean#L87).

```lean
lemma sphericalIntegral_eq_zero_of_forall {r : ℝ} {f : Space 3 → ℂ} {x : Space 3}
    (h : ∀ n : Sph, f (x + r • n.1) = 0) : sphericalIntegral r f x = 0
```

**`WaveEquation.Kirchhoff.wavePropagator_eq_zero_of_far_of_pos`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean#L95).

> **Finite propagation speed.** If `f` vanishes outside the ball of radius `ρ` about `x₀`, then
> `S_t f` vanishes at every point farther than `ρ + c t` from `x₀`.

```lean
lemma wavePropagator_eq_zero_of_far_of_pos {c t ρ : ℝ} (hc : 0 < c) (ht : 0 < t) {f : Space 3 → ℂ}
    {x₀ : Space 3} (hf : ∀ y, ρ < ‖y - x₀‖ → f y = 0) {x : Space 3}
    (hx : ρ + c * t < ‖x - x₀‖) : wavePropagator c t f x = 0
```

**`WaveEquation.Kirchhoff.wavePropagator_eq_zero_of_near_of_pos`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean#L114).

> **Strong Huygens principle.** If `f` vanishes outside the ball of radius `ρ` about `x₀`, then
> `S_t f` vanishes at every point `x` with `‖x - x₀‖ + ρ < c t`.

```lean
lemma wavePropagator_eq_zero_of_near_of_pos {c t ρ : ℝ} (hc : 0 < c) (ht : 0 < t) {f : Space 3 → ℂ}
    {x₀ : Space 3} (hf : ∀ y, ρ < ‖y - x₀‖ → f y = 0) {x : Space 3}
    (hx : ‖x - x₀‖ + ρ < c * t) : wavePropagator c t f x = 0
```

## C. Two-sided time

**`WaveEquation.Kirchhoff.sphericalIntegral_neg`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean#L134).

> The spherical integral over the sphere of radius `-r` equals the one over radius `r`.

```lean
lemma sphericalIntegral_neg (r : ℝ) (f : Space 3 → ℂ) (x : Space 3) :
    sphericalIntegral (-r) f x = sphericalIntegral r f x
```

**`WaveEquation.Kirchhoff.wavePropagator_zero`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean#L146).

> The wave propagator vanishes at time zero.

```lean
lemma wavePropagator_zero (c : ℝ) (f : Space 3 → ℂ) (x : Space 3) : wavePropagator c 0 f x = 0
```

**`WaveEquation.Kirchhoff.wavePropagator_neg`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean#L150).

> The wave propagator is odd in time.

```lean
lemma wavePropagator_neg (c t : ℝ) (f : Space 3 → ℂ) (x : Space 3) :
    wavePropagator c (-t) f x = -wavePropagator c t f x
```

**`WaveEquation.Kirchhoff.wavePropagator_eq_of_eq_on_sphere`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean#L160).

> The wave propagator at `(t, x)` reads the data only on the sphere `‖y - x‖ = c |t|`, where the
> light cone of `(t, x)` meets the initial time. Data that agree there give the same field.

```lean
lemma wavePropagator_eq_of_eq_on_sphere {c t : ℝ} (hc : 0 < c) {f g : Space 3 → ℂ}
    {x : Space 3} (h : ∀ y, ‖y - x‖ = c * |t| → f y = g y) :
    wavePropagator c t f x = wavePropagator c t g x
```

**`WaveEquation.Kirchhoff.wavePropagator_eq_zero_of_far`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean#L171).

> **Finite propagation speed** for both signs of time.

```lean
lemma wavePropagator_eq_zero_of_far {c t ρ : ℝ} (hc : 0 < c) {f : Space 3 → ℂ}
    {x₀ : Space 3} (hf : ∀ y, ρ < ‖y - x₀‖ → f y = 0) {x : Space 3}
    (hx : ρ + c * |t| < ‖x - x₀‖) : wavePropagator c t f x = 0
```

**`WaveEquation.Kirchhoff.wavePropagator_eq_zero_of_near`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean#L183).

> **Strong Huygens principle** for both signs of time.

```lean
lemma wavePropagator_eq_zero_of_near {c t ρ : ℝ} (hc : 0 < c) {f : Space 3 → ℂ}
    {x₀ : Space 3} (hf : ∀ y, ρ < ‖y - x₀‖ → f y = 0) {x : Space 3}
    (hx : ‖x - x₀‖ + ρ < c * |t|) : wavePropagator c t f x = 0
```

**`WaveEquation.Kirchhoff.wavePropagator_fourier`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean#L195).

> The Fourier multiplier of the wave propagator for both signs of time.

```lean
lemma wavePropagator_fourier (f : 𝓢(Space 3, ℂ)) {c t : ℝ} (hc : 0 < c) {ξ : Space 3}
    (hξ : ξ ≠ 0) :
    ∫ x : Space 3, phase (inner ℝ x ξ) * wavePropagator c t f x =
      ((Real.sin (2 * Real.pi * c * ‖ξ‖ * t) / (2 * Real.pi * c * ‖ξ‖) : ℝ) : ℂ) *
        ∫ x : Space 3, phase (inner ℝ x ξ) * f x
```

## D. The free three-dimensional propagator

**`WaveEquation.Kirchhoff.wavePropagator_isWavePropagator`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean#L219).

> **Kirchhoff's formula.** For `c > 0` and every real `t` the wave propagator has the Fourier
> multiplier `sin(ω t) / ω`, propagates at speed at most `c` and satisfies the strong Huygens
> principle.

```lean
lemma wavePropagator_isWavePropagator {c : ℝ} (hc : 0 < c) (t : ℝ) :
    IsWavePropagator c t (wavePropagator c t)
```

**`WaveEquation.Kirchhoff.wavePropagator_eq_time_sphericalMean`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean#L226).

> The wave propagator is `t M_{ct}` with the normalized sphere mean.

```lean
lemma wavePropagator_eq_time_sphericalMean (c t : ℝ) (f : Space 3 → ℂ) (x : Space 3) :
    wavePropagator c t f x = (t : ℂ) * sphericalMean (c * t) f x
```

## Depends on

- [Fourier properties of wave propagation](kirchhoff-phase.md)
- [Waves propagating along spheres](kirchhoff-setting.md)

## Proof depends on

- [Fourier transform and integrability of spherical means](kirchhoff-sphericalmean.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/Propagator.lean)
