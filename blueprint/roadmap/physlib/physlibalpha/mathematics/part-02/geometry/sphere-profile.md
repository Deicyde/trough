---
declaration: module
origin: cited
lean: Sphere3.sphereProfile, Sphere3.ball_integral_profile, Sphere3.continuous_sphereProfile, Sphere3.discProfile, Sphere3.hasDerivAt_discProfile, Sphere3.sphereProfile_eq, Sphere3.sphereEquiv, Sphere3.sphereEquiv_coe
statement: formalized
proof: formalized
---

# Spherical profiles and invariant sphere integrals

The module `PhyslibAlpha.Mathematics.Geometry.Sphere.Profile`, [PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean): 12 declarations, 6 with a docstring.

> The invariant sphere measure has mass `4 π` and admits directional integration formulas.

## i. Overview

> Differentiating the ball integral in the radius gives Archimedes' projection of the sphere onto an
> axis. This is the sphere transform for axis directions. Rotation invariance of the sphere measure
> extends it to every direction.

## ii. Key results

> * `sphereProfile_eq`: Archimedes' projection of the sphere onto an axis.
> * `sphereEquiv_measurePreserving`: the sphere measure is invariant under linear isometries.
> * `sphereMeasure_univ`: the total mass is `4 π`.
> * `sphereIntegral_dir`: Archimedes' formula for a function of one direction.
> * `integral_sphere_neg`: invariance of the sphere measure under the antipodal map.

## iv. References

> * None.

## A. The radial profile of the sphere average

**`Sphere3.sphereProfile`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean#L50).

> The average of `h (r n_i)` over the unit sphere, as a function of the radius.

```lean
noncomputable def sphereProfile {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    (i : Fin 3) (h : ℝ → F) (r : ℝ) : F
```

**`Sphere3.ball_integral_profile`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean#L54).

```lean
lemma ball_integral_profile {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    (i : Fin 3) {h : ℝ → F} (hh : Continuous h) {R : ℝ} (hR : 0 < R) :
    ∫ x in Metric.ball (0 : Space 3) R, h (x i) =
      ∫ r in Set.Ioo 0 R, r ^ 2 • sphereProfile i h r
```

**`Sphere3.continuous_sphereProfile`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean#L90).

```lean
lemma continuous_sphereProfile {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    (i : Fin 3) {h : ℝ → F} (hh : Continuous h) :
    Continuous (sphereProfile i h)
```

## B. Archimedes' projection

**`Sphere3.discProfile`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean#L107).

> The closed-form side: the integral of `π (R² - z²) h(z)`, as a function of `R`.

```lean
noncomputable def discProfile {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    (h : ℝ → F) (R : ℝ) : F
```

**`Sphere3.hasDerivAt_discProfile`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean#L111).

```lean
lemma hasDerivAt_discProfile {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    [CompleteSpace F] {h : ℝ → F} (hh : Continuous h) (R : ℝ) :
    HasDerivAt (discProfile h) ((2 * Real.pi * R) • ∫ z in (-R)..R, h z) R
```

**`Sphere3.sphereProfile_eq`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean#L146).

```lean
lemma sphereProfile_eq {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
    (i : Fin 3) {h : ℝ → F} (hh : Continuous h) {R : ℝ} (hR : 0 < R) :
    sphereProfile i h R = (2 * Real.pi / R) • ∫ z in (-R)..R, h z
```

## C. Rotation invariance and general directions

**`Sphere3.sphereEquiv`**, a def, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean#L198).

> The restriction of a linear isometry of `Space 3` to the unit sphere.

```lean
noncomputable def sphereEquiv (U : Space 3 ≃ₗᵢ[ℝ] Space 3) : Sph ≃ₜ Sph
```

**`Sphere3.sphereEquiv_coe`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean#L208).

```lean
lemma sphereEquiv_coe (U : Space 3 ≃ₗᵢ[ℝ] Space 3) (n : Sph) :
    ((sphereEquiv U n : Sph) : Space 3) = U n.1
```

**`Sphere3.sphereEquiv_measurePreserving`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean#L211).

```lean
lemma sphereEquiv_measurePreserving (U : Space 3 ≃ₗᵢ[ℝ] Space 3) :
    MeasurePreserving (sphereEquiv U) sphereMeasure sphereMeasure
```

**`Sphere3.sphereMeasure_univ`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean#L252).

> The total mass of the sphere measure is the area `4 π`.

```lean
lemma sphereMeasure_univ : sphereMeasure Set.univ = ENNReal.ofReal (4 * Real.pi)
```

## D. Functions of one direction

**`Sphere3.sphereIntegral_dir`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean#L262).

> **Archimedes in an arbitrary direction.** The sphere integral of a function of the inner product
> with a fixed vector `z ≠ 0` is a one-dimensional integral over `[-‖z‖, ‖z‖]`.

```lean
lemma sphereIntegral_dir {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
    {h : ℝ → F} (hh : Continuous h) {z : Space 3} (hz : z ≠ 0) :
    ∫ n : Sph, h (inner ℝ z n.1) ∂sphereMeasure =
      (2 * Real.pi / ‖z‖) • ∫ s in (-‖z‖)..‖z‖, h s
```

**`Sphere3.integral_sphere_neg`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean#L292).

> The sphere measure is invariant under the antipodal map.

```lean
lemma integral_sphere_neg {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    (f : Space 3 → F) : ∫ n : Sph, f (-n.1) ∂sphereMeasure = ∫ n : Sph, f n.1 ∂sphereMeasure
```

## Depends on

- [Polar coordinates on balls of space](sphere-polar.md)

## Sources

- [PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Profile.lean)
