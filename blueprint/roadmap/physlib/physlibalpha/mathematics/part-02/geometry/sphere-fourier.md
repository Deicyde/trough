---
declaration: module
origin: cited
lean: Sphere3.integral_exp_symm, Sphere3.sphere_fourier_axis, Sphere3.sphere_fourier
statement: formalized
proof: formalized
---

# Fourier transform of the sphere measure

The module `PhyslibAlpha.Mathematics.Geometry.Sphere.Fourier`, [PhyslibAlpha/Mathematics/Geometry/Sphere/Fourier.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Fourier.lean): 3 declarations, 1 with a docstring.

> Archimedes' formula computes the exact sine multiplier of the sphere measure.

## i. Overview

> Archimedes' formula computes the exact sine multiplier of the sphere measure.

## ii. Key results

> * `integral_exp_symm`.
> * `sphere_fourier_axis`: The Fourier transform of the sphere measure along an axis.
> * `sphere_fourier`.

## iv. References

> * Bär, [Green-hyperbolic operators on globally hyperbolic
>   spacetimes](https://arxiv.org/abs/1310.0738).

## A. Fourier transform of the sphere measure

**`Sphere3.integral_exp_symm`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Fourier.lean#L46).

```lean
lemma integral_exp_symm (a R : ℝ) (ha : a ≠ 0) :
    ∫ z in (-R)..R, Complex.exp (Complex.I * (a * z)) = 2 * Real.sin (a * R) / a
```

**`Sphere3.sphere_fourier_axis`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Fourier.lean#L73).

> The Fourier transform of the sphere measure along an axis.

```lean
lemma sphere_fourier_axis (i : Fin 3) {a R : ℝ} (ha : a ≠ 0) (hR : 0 < R) :
    ∫ n : Sph, Complex.exp (Complex.I * (a * (R * n.1 i))) ∂sphereMeasure =
      (4 * Real.pi * Real.sin (a * R) / (a * R) : ℝ)
```

**`Sphere3.sphere_fourier`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Fourier.lean#L91).

```lean
lemma sphere_fourier (k : Space 3) (hk : k ≠ 0) {R : ℝ} (hR : 0 < R) :
    ∫ n : Sph, Complex.exp (Complex.I * ((R * inner ℝ k n.1 : ℝ) : ℂ)) ∂sphereMeasure =
      (4 * Real.pi * Real.sin (R * ‖k‖) / (R * ‖k‖) : ℝ)
```

## Depends on

- [Polar coordinates on balls of space](sphere-polar.md)

## Proof depends on

- [Spherical profiles and invariant sphere integrals](sphere-profile.md)

## Sources

- [PhyslibAlpha/Mathematics/Geometry/Sphere/Fourier.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Fourier.lean)
