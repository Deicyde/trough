---
declaration: module
origin: cited
lean: WaveEquation.Kirchhoff.translate_complex, WaveEquation.Kirchhoff.sphericalIntegral_fourier_integral, WaveEquation.Kirchhoff.sphericalIntegral_fourier, WaveEquation.Kirchhoff.integrable_translate_prod, WaveEquation.Kirchhoff.integrable_sphericalIntegral, WaveEquation.Kirchhoff.sphericalIntegral_bound, WaveEquation.Kirchhoff.memLp_two_sphericalIntegral
statement: formalized
proof: formalized
---

# Fourier transform and integrability of spherical means

The module `PhyslibAlpha.ClassicalFieldTheory.WaveEquation.Kirchhoff.SphericalMean`, [PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/SphericalMean.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/SphericalMean.lean): 7 declarations, 3 with a docstring.

> The spherical mean of a Schwartz function has the transform of the sphere measure times that of
> the function.

## i. Overview

> The Fourier integral of a spherical mean is the transform of the sphere measure times that of
> the function. Spherical means are integrable and square integrable.

## ii. Key results

> * `sphericalIntegral_fourier`: the Fourier integral of a spherical mean.
> * `integrable_sphericalIntegral`, `memLp_two_sphericalIntegral`: integrability of spherical means.

## iv. References

> * None.

## A. The Fourier transform of a spherical mean

**`WaveEquation.Kirchhoff.translate_complex`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/SphericalMean.lean#L45).

```lean
lemma translate_complex (f : Space 3 → ℂ) (v ξ : Space 3) :
    ∫ x : Space 3, phase (inner ℝ x ξ) * f (x + v) =
      (phase (inner ℝ v ξ))⁻¹ * ∫ x : Space 3, phase (inner ℝ x ξ) * f x
```

**`WaveEquation.Kirchhoff.sphericalIntegral_fourier_integral`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/SphericalMean.lean#L62).

```lean
lemma sphericalIntegral_fourier_integral (f : 𝓢(Space 3, ℂ)) (r : ℝ) (ξ : Space 3) :
    ∫ x : Space 3, phase (inner ℝ x ξ) * sphericalIntegral r f x =
      (∫ n : Sph, (phase (inner ℝ (r • n.1) ξ))⁻¹ ∂sphereMeasure) *
        ∫ x : Space 3, phase (inner ℝ x ξ) * f x
```

**`WaveEquation.Kirchhoff.sphericalIntegral_fourier`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/SphericalMean.lean#L106).

> **Fourier multiplier of the spherical mean.** For `ξ ≠ 0` and `r > 0`, the Fourier integral of
> the unnormalized spherical mean is `4π sin(2π r |ξ|) / (2π r |ξ|)` times that of `f`.

```lean
lemma sphericalIntegral_fourier (f : 𝓢(Space 3, ℂ)) {r : ℝ} (hr : 0 < r)
    {ξ : Space 3} (hξ : ξ ≠ 0) :
    ∫ x : Space 3, phase (inner ℝ x ξ) * sphericalIntegral r f x =
      ((4 * Real.pi * Real.sin (2 * Real.pi * r * ‖ξ‖) / (2 * Real.pi * r * ‖ξ‖) : ℝ) : ℂ) *
        ∫ x : Space 3, phase (inner ℝ x ξ) * f x
```

## B. Integrability of the spherical mean

**`WaveEquation.Kirchhoff.integrable_translate_prod`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/SphericalMean.lean#L129).

```lean
lemma integrable_translate_prod (f : 𝓢(Space 3, ℂ)) (r : ℝ) :
    Integrable (Function.uncurry fun (x : Space 3) (n : Sph) => f (x + r • n.1))
      (volume.prod sphereMeasure)
```

**`WaveEquation.Kirchhoff.integrable_sphericalIntegral`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/SphericalMean.lean#L147).

> The spherical mean of a Schwartz function is integrable.

```lean
lemma integrable_sphericalIntegral (f : 𝓢(Space 3, ℂ)) (r : ℝ) :
    Integrable (sphericalIntegral r f) volume
```

**`WaveEquation.Kirchhoff.sphericalIntegral_bound`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/SphericalMean.lean#L151).

```lean
lemma sphericalIntegral_bound (f : 𝓢(Space 3, ℂ)) (r : ℝ) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ x, ‖sphericalIntegral r f x‖ ≤ C
```

**`WaveEquation.Kirchhoff.memLp_two_sphericalIntegral`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/SphericalMean.lean#L163).

> The spherical mean of a Schwartz function is square integrable.

```lean
lemma memLp_two_sphericalIntegral (f : 𝓢(Space 3, ℂ)) (r : ℝ) :
    MemLp (sphericalIntegral r f) 2 volume
```

## Depends on

- [Fourier properties of wave propagation](kirchhoff-phase.md)
- [Waves propagating along spheres](kirchhoff-setting.md)

## Proof depends on

- [Fourier transform of the sphere measure](../../mathematics/part-02/geometry/sphere-fourier.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/SphericalMean.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/WaveEquation/Kirchhoff/SphericalMean.lean)
