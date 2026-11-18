---
declaration: module
origin: cited
lean: Sphere3.equivPi_measurePreserving, Sphere3.slice_measurePreserving, Sphere3.volume_ball_two, Sphere3.integral_ball_coord_aux, Sphere3.indicator_slice_apply, Sphere3.slab_section_volume, Sphere3.integral_ball_coord, Sphere3.Sph
statement: formalized
proof: formalized
---

# Polar coordinates on balls of space

The module `PhyslibAlpha.Mathematics.Geometry.Sphere.Polar`, [PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean): 15 declarations, 7 with a docstring.

> Integrals over balls of `Space 3` reduce to integrals over the unit sphere and the radius.

## i. Overview

> The coordinate slice `Space 3 ≃ ℝ × Space 2` preserves volume. This gives integrals over a ball of
> functions of one coordinate as one-dimensional integrals against the disc area `π (R² - z²)`.
> Polar coordinates write the ball integral as an integral over the unit sphere and over the radius.
> The unit sphere carries the surface measure of total mass `4 π`. The same holds for general
> integrands. Integrability of `1 / |x|` times a continuous function and of radial exponentials is
> included.

## ii. Key results

> * `slice_measurePreserving`: the slice map preserves volume.
> * `integral_ball_coord`: a ball integral of a function of one coordinate.
> * `ball_integral_polar`, `ball_integral_polar_general`: polar coordinates on a ball.
> * `integrable_inv_norm_mul`: integrability of the singular Green density.

## iv. References

> * None.

## A. Volume preservation of coordinate maps

**`Sphere3.equivPi_measurePreserving`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean#L53).

```lean
lemma equivPi_measurePreserving (d : ℕ) :
    MeasurePreserving (Space.equivPi d) (volume : Measure (Space d))
      (volume : Measure (Fin d → ℝ))
```

**`Sphere3.slice_measurePreserving`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean#L63).

```lean
lemma slice_measurePreserving {d : ℕ} (i : Fin d.succ) :
    MeasurePreserving (Space.slice i) (volume : Measure (Space d.succ))
      (volume : Measure (ℝ × Space d))
```

## B. Integrals over a ball of a function of one coordinate

**`Sphere3.volume_ball_two`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean#L81).

```lean
lemma volume_ball_two (ρ : ℝ) (hρ : 0 ≤ ρ) :
    volume (Metric.ball (0 : Space 2) ρ) = ENNReal.ofReal (Real.pi * ρ ^ 2)
```

**`Sphere3.integral_ball_coord_aux`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean#L89).

```lean
lemma integral_ball_coord_aux {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    (i : Fin 3) (h : ℝ → F) {R : ℝ} :
    ∫ x in Metric.ball (0 : Space 3) R, h (x i) =
      ∫ p : ℝ × Space 2, (Metric.ball (0 : Space 3) R).indicator (fun x => h (x i))
        ((Space.slice i).symm p)
```

**`Sphere3.indicator_slice_apply`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean#L102).

```lean
lemma indicator_slice_apply {F : Type*} [NormedAddCommGroup F]
    (i : Fin 3) (h : ℝ → F) {R : ℝ} (hR : 0 < R) (z : ℝ) (y : Space 2) :
    (Metric.ball (0 : Space 3) R).indicator (fun x => h (x i)) ((Space.slice i).symm (z, y)) =
      {y' : Space 2 | z ^ 2 + ‖y'‖ ^ 2 < R ^ 2}.indicator (fun _ => h z) y
```

**`Sphere3.slab_section_volume`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean#L117).

```lean
lemma slab_section_volume (R z : ℝ) :
    volume {y : Space 2 | z ^ 2 + ‖y‖ ^ 2 < R ^ 2} =
      ENNReal.ofReal (Real.pi * (R ^ 2 - z ^ 2))
```

**`Sphere3.integral_ball_coord`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean#L141).

> A ball integral of a function of one coordinate reduces to a one-dimensional integral against
> the disc area.

```lean
lemma integral_ball_coord {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
    (i : Fin 3) {h : ℝ → F} (hh : Continuous h) {R : ℝ} (hR : 0 < R) :
    ∫ x in Metric.ball (0 : Space 3) R, h (x i) =
      ∫ z in Set.Ioo (-R) R, (Real.pi * (R ^ 2 - z ^ 2)) • h z
```

## C. Polar coordinates on the ball

**`Sphere3.Sph`**, an abbrev, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean#L214).

> The unit sphere of `Space 3` with its surface measure.

```lean
abbrev Sph
```

**`Sphere3.sphereMeasure`**, an abbrev, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean#L217).

> The surface measure on the unit sphere, normalized so that the total mass is `4 π`.

```lean
noncomputable abbrev sphereMeasure : Measure Sph
```

**`Sphere3.integrable_ball_indicator_coord`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean#L219).

```lean
lemma integrable_ball_indicator_coord {F : Type*} [NormedAddCommGroup F]
    (i : Fin 3) {h : ℝ → F} (hh : Continuous h) (R : ℝ) :
    Integrable ((Metric.ball (0 : Space 3) R).indicator (fun x => h (x i))) volume
```

**`Sphere3.ball_integral_polar`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean#L227).

```lean
lemma ball_integral_polar {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    (i : Fin 3) {h : ℝ → F} (hh : Continuous h) {R : ℝ} :
    ∫ x in Metric.ball (0 : Space 3) R, h (x i) =
      ∫ n : Sph, ∫ r in Set.Ioo 0 R, r ^ 2 • h (r * (n.1 i)) ∂volume ∂sphereMeasure
```

## D. Polar coordinates for general integrands

**`Sphere3.integrable_ball_indicator`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean#L260).

> A continuous function has an integrable restriction to a ball.

```lean
lemma integrable_ball_indicator {F : Type*} [NormedAddCommGroup F]
    {g : Space 3 → F} (hg : Continuous g) (R : ℝ) :
    Integrable ((Metric.ball (0 : Space 3) R).indicator g) volume
```

**`Sphere3.integrable_inv_norm_mul`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean#L268).

> `‖z‖⁻¹` times a continuous function is integrable on a ball of `Space 3`.

```lean
lemma integrable_inv_norm_mul {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    {k : Space 3 → F} (hk : Continuous k) (R : ℝ) :
    Integrable ((Metric.ball (0 : Space 3) R).indicator (fun z => (‖z‖⁻¹ : ℝ) • k z)) volume
```

**`Sphere3.ball_integral_polar_general`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean#L286).

> Polar coordinates on a ball for a general continuous integrand.

```lean
lemma ball_integral_polar_general {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    {g : Space 3 → F} {R : ℝ}
    (hg : Integrable ((Metric.ball (0 : Space 3) R).indicator g) volume) :
    ∫ y in Metric.ball (0 : Space 3) R, g y =
      ∫ n : Sph, ∫ r in Set.Ioo 0 R, r ^ 2 • g (r • n.1) ∂volume ∂sphereMeasure
```

**`Sphere3.setIntegral_ball_translate`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean#L316).

> Translation of a ball integral to the origin.

```lean
lemma setIntegral_ball_translate {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    (G : Space 3 → F) (x : Space 3) (R : ℝ) :
    ∫ y in Metric.ball x R, G y = ∫ z in Metric.ball (0 : Space 3) R, G (x + z)
```

## Depends on

- [Slices of space](../../../../physlib/spaceandtime/space/part-01/slice.md)

## Proof depends on

- [Integrals in Space](../../../../physlib/spaceandtime/space/part-02/integrals-basic.md)

## Sources

- [PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Geometry/Sphere/Polar.lean)
