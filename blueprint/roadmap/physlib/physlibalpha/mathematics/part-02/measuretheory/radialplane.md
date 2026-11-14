---
declaration: module
origin: cited
lean: RadialPlane.RadialDecay, RadialPlane.radial_bound, RadialPlane.integral_plane_radial, RadialPlane.integrableOn_radial, RadialPlane.hasDerivAt_tail, RadialPlane.radialDecay_of_vanishing, RadialPlane.integral_plane_radial_zero
statement: formalized
proof: formalized
---

# The integral of a radial function over the plane

The module `PhyslibAlpha.Mathematics.MeasureTheory.RadialPlane`, [PhyslibAlpha/Mathematics/MeasureTheory/RadialPlane.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RadialPlane.lean): 7 declarations, 7 with a docstring.

> Integrating a radial function over two extra variables gives the tail integral of its profile.

## i. Overview

> For a radial function with profile `Φ` the integral over the plane at distance `ρ` is
> `∫ Φ (√(ρ² + |y|²)) dy`. In polar coordinates this is `2π ∫ s Φ (√(ρ² + s²)) ds`. The substitution
> `u = √(ρ² + s²)` turns it into `2π ∫_{u > ρ} u Φ (u) du`. The tail integral has the derivative
> `-ρ Φ (ρ)`.

## ii. Key results

> - `RadialPlane.integral_plane_radial` : the integral of a radial function over the plane.
> - `RadialPlane.hasDerivAt_tail` : the derivative of the tail integral.

## iv. References

> None.

## A. The plane integral

> - `RadialPlane.integral_plane_radial` : the integral of a radial function over the plane.

## B. The tail integral

> - `RadialPlane.hasDerivAt_tail` : the derivative of the tail integral.

**`RadialPlane.RadialDecay`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RadialPlane.lean#L57).

> The decay of the profile used in the radial estimates.

```lean
def RadialDecay (Φ : ℝ → ℂ) : Prop
```

**`RadialPlane.radial_bound`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RadialPlane.lean#L61).

> A bound for the profile times the radius.

```lean
lemma radial_bound {Φ : ℝ → ℂ} {C : ℝ} (hC : ∀ u : ℝ, 0 ≤ u → ‖Φ u‖ ≤ C * (1 + u) ^ (-(3 : ℝ)))
    {x u : ℝ} (hx : 0 ≤ x) (hxu : x ≤ u) : ‖x • Φ u‖ ≤ |C| * (1 + ‖x‖) ^ (-(2 : ℝ))
```

**`RadialPlane.integral_plane_radial`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RadialPlane.lean#L85).

> **The integral of a radial function over the plane.**

```lean
lemma integral_plane_radial {Φ : ℝ → ℂ} (hΦ : RadialDecay Φ) {ρ : ℝ} (hρ : 0 < ρ) :
    ∫ y : EuclideanSpace ℝ (Fin 2), Φ (Real.sqrt (ρ ^ 2 + ‖y‖ ^ 2)) =
      (2 * Real.pi : ℝ) • ∫ u in Ioi ρ, u • Φ u
```

**`RadialPlane.integrableOn_radial`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RadialPlane.lean#L169).

> The profile times the radius is integrable on a half line.

```lean
lemma integrableOn_radial {Φ : ℝ → ℂ} (hΦ : RadialDecay Φ) {a : ℝ} (ha : 0 ≤ a) :
    IntegrableOn (fun u : ℝ => u • Φ u) (Ioi a)
```

**`RadialPlane.hasDerivAt_tail`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RadialPlane.lean#L181).

> **The derivative of the tail integral.**

```lean
lemma hasDerivAt_tail {Φ : ℝ → ℂ} (hΦ : RadialDecay Φ) {ρ : ℝ} (hρ : 0 < ρ) :
    HasDerivAt (fun r : ℝ => ∫ u in Ioi r, u • Φ u) (-(ρ • Φ ρ)) ρ
```

**`RadialPlane.radialDecay_of_vanishing`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RadialPlane.lean#L195).

> A continuous profile that vanishes beyond some radius has the radial decay.

```lean
lemma radialDecay_of_vanishing {Φ : ℝ → ℂ} (hc : Continuous Φ) {S : ℝ}
    (h : ∀ u, S < u → Φ u = 0) : RadialDecay Φ
```

**`RadialPlane.integral_plane_radial_zero`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RadialPlane.lean#L220).

> **The integral of a radial function over the plane at the origin.**

```lean
lemma integral_plane_radial_zero (Φ : ℝ → ℂ) :
    ∫ y : EuclideanSpace ℝ (Fin 2), Φ ‖y‖ = (2 * Real.pi : ℝ) • ∫ u in Ioi (0 : ℝ), u • Φ u
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/MeasureTheory/RadialPlane.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/RadialPlane.lean)
