---
declaration: module
origin: cited
lean: ClassicalMechanics.NortonDome.horizontal, ClassicalMechanics.NortonDome.horizontal_eq, ClassicalMechanics.NortonDome.horizontal_zero, ClassicalMechanics.NortonDome.hasDerivAt_horizontal, ClassicalMechanics.NortonDome.horizontal_differentiable, ClassicalMechanics.NortonDome.unit_speed, ClassicalMechanics.NortonDome.profile, ClassicalMechanics.NortonDome.profile_apply_zero
statement: formalized
proof: formalized
---

# The Norton dome in physical space

The module `PhyslibAlpha.ClassicalMechanics.NortonDome.PhysicalSpace`, [PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean): 23 declarations, 23 with a docstring.

> The Norton dome chart dynamics as a point mass constrained to the dome surface.

## i. Overview

> `NortonDome.Basic` writes the dynamics on the arc length `r`, with kinetic energy `½ m ṙ²` and
> potential energy `-m g h(r)`. This module identifies that chart dynamics with a point mass
> constrained to the surface of the dome, as `SimplePendulum.Geometric.PhysicalSpace` does for
> the pendulum.
>
> The motion is radial, so it suffices to work in the vertical plane through the apex, with the
> apex at the origin and the vertical coordinate measured upwards. The profile is the arc-length
> parametrised curve `s ↦ (x(s), -h(s))`, where `x'(s)² + h'(s)² = 1` and `h'(s) = √s / g` give
> `x'(s) = √(1 - s/g²)` and `x(s) = (2g²/3) (1 - (1 - s/g²)^{3/2})`. The profile exists for
> `0 ≤ s ≤ g²`; at `s = g²` it is vertical and Norton's model stops. While the arc length is in
> that range the chart kinetic energy is `½ m ‖v‖²` by unit speed, and the chart potential energy
> is the gravitational potential `m g y` at height `y`, so the chart Lagrangian is the
> constrained Lagrangian.

## ii. Key results

> - `NortonDome.horizontal` is the horizontal distance `x(s)` of the profile from the apex, with
>   its derivative `hasDerivAt_horizontal`; `NortonDome.unit_speed` is the identity
>   `x'(s)² + h'(s)² = 1`.
> - `NortonDome.profile` is the profile curve `s ↦ (x(s), -h(s))` in the vertical plane, and
>   `NortonDome.dome` its image on `0 ≤ s ≤ g²`.
> - `NortonDome.spaceTrajectory` is the position of the particle in the plane along a chart
>   trajectory; it lies on the dome, `spaceTrajectory_mem_dome`, while the arc length is in range.
> - `NortonDome.deriv_spaceTrajectory` is the velocity of the particle in the plane, with the
>   square of its speed `norm_sq_deriv_spaceTrajectory`.
> - `NortonDome.kineticEnergy_eq_space`, `NortonDome.potentialEnergy_eq_height`,
>   `NortonDome.lagrangian_eq_space` and `NortonDome.energy_eq_space` identify the chart
>   energies and Lagrangian with those of the point mass in physical space.

## iv. References

> - Norton, J. D., *The dome: an unexpectedly simple failure of determinism*, Philosophy of
>   Science 75 (2008), 786–798.
> - `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.Geometric.PhysicalSpace` (the same
>   identification for the pendulum).

## A. The profile of the dome in the plane

### A.1. The horizontal coordinate and the unit-speed property

> The horizontal distance from the apex has derivative `√(1 - s/g²)`; with the slope `√s / g` of
> the depth this gives unit speed.

**`ClassicalMechanics.NortonDome.horizontal`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L88).

> The horizontal distance `x(s) = (2g²/3) (1 - (1 - s/g²)^{3/2})` of the profile of the dome
> from the apex at arc length `s`.

```lean
noncomputable def horizontal (s : ℝ) : ℝ
```

**`ClassicalMechanics.NortonDome.horizontal_eq`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L91).

> The horizontal distance of the profile from the apex, written out.

```lean
lemma horizontal_eq (s : ℝ) :
    S.horizontal s = 2 * S.g ^ 2 / 3 * (1 - √(1 - s / S.g ^ 2) ^ 3)
```

**`ClassicalMechanics.NortonDome.horizontal_zero`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L95).

> The profile of the dome starts at the apex.

```lean
lemma horizontal_zero : S.horizontal 0 = 0
```

**`ClassicalMechanics.NortonDome.hasDerivAt_horizontal`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L100).

> The derivative of the horizontal distance with respect to the arc length is `√(1 - s/g²)`,
> at every `s`.

```lean
lemma hasDerivAt_horizontal (s : ℝ) : HasDerivAt S.horizontal (√(1 - s / S.g ^ 2)) s
```

**`ClassicalMechanics.NortonDome.horizontal_differentiable`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L110).

> The horizontal distance of the profile from the apex is a differentiable function of the
> arc length.

```lean
lemma horizontal_differentiable : Differentiable ℝ S.horizontal
```

**`ClassicalMechanics.NortonDome.unit_speed`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L116).

> Unit speed: for arc length `0 ≤ s ≤ g²` the derivatives of the horizontal distance and
> of the depth satisfy `x'(s)² + h'(s)² = 1`, so that `s` is indeed the arc length along the
> profile.

```lean
lemma unit_speed {s : ℝ} (h0 : 0 ≤ s) (h1 : s ≤ S.g ^ 2) :
    √(1 - s / S.g ^ 2) ^ 2 + (√s / S.g) ^ 2 = 1
```

### A.2. The profile curve and the dome

**`ClassicalMechanics.NortonDome.profile`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L132).

> The profile of the dome in the vertical plane through the apex: the point at arc length
> `s` is at horizontal distance `x(s)` from the apex and at height `-h(s)`.

```lean
noncomputable def profile (s : ℝ) : Space 2
```

**`ClassicalMechanics.NortonDome.profile_apply_zero`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L135).

> The horizontal coordinate of the profile of the dome.

```lean
lemma profile_apply_zero (s : ℝ) : S.profile s 0 = S.horizontal s
```

**`ClassicalMechanics.NortonDome.profile_apply_one`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L139).

> The vertical coordinate of the profile of the dome is minus its depth below the apex.

```lean
lemma profile_apply_one (s : ℝ) : S.profile s 1 = -S.height s
```

**`ClassicalMechanics.NortonDome.profile_zero`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L143).

> The apex of the dome is the origin.

```lean
lemma profile_zero : S.profile 0 = 0
```

**`ClassicalMechanics.NortonDome.dome`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L149).

> The dome, in the vertical plane through its apex: the image of the profile on the range
> `0 ≤ s ≤ g²` of arc lengths on which the profile exists.

```lean
noncomputable def dome : Set (Space 2)
```

**`ClassicalMechanics.NortonDome.profile_mem_dome`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L152).

> The point of the profile at arc length `0 ≤ s ≤ g²` lies on the dome.

```lean
lemma profile_mem_dome {s : ℝ} (h0 : 0 ≤ s) (h1 : s ≤ S.g ^ 2) : S.profile s ∈ S.dome
```

## B. The particle's position along a trajectory

> Along a chart trajectory `r` the particle is at the point of the profile at arc length
> `r t 0`, on the dome while that is in range.

**`ClassicalMechanics.NortonDome.spaceTrajectory`**, a def, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L166).

> The position of the particle in the plane along the chart trajectory `r` of the arc
> length.

```lean
noncomputable def spaceTrajectory (r : Time → EuclideanSpace ℝ (Fin 1)) : Time → Space 2
```

**`ClassicalMechanics.NortonDome.spaceTrajectory_apply_zero`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L170).

> The horizontal position of the particle along a chart trajectory.

```lean
lemma spaceTrajectory_apply_zero (r : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    S.spaceTrajectory r t 0 = S.horizontal (r t 0)
```

**`ClassicalMechanics.NortonDome.spaceTrajectory_apply_one`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L176).

> The height of the particle along a chart trajectory is minus the depth of the dome at its
> arc length.

```lean
lemma spaceTrajectory_apply_one (r : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    S.spaceTrajectory r t 1 = -S.height (r t 0)
```

**`ClassicalMechanics.NortonDome.spaceTrajectory_mem_dome`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L181).

> While its arc length is in the range `0 ≤ r ≤ g²` the particle is on the dome.

```lean
lemma spaceTrajectory_mem_dome (r : Time → EuclideanSpace ℝ (Fin 1)) {t : Time}
    (h0 : 0 ≤ r t 0) (h1 : r t 0 ≤ S.g ^ 2) : S.spaceTrajectory r t ∈ S.dome
```

## C. The particle's velocity and speed

> The velocity in the plane is the unit tangent `(x'(r), -h'(r))` times `ṙ`, so by unit speed the
> square of the speed is `ṙ²` while the arc length is in range.

**`ClassicalMechanics.NortonDome.differentiable_spaceTrajectory`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L197).

> Along a differentiable chart trajectory the position of the particle is differentiable in
> time.

```lean
lemma differentiable_spaceTrajectory (r : Time → EuclideanSpace ℝ (Fin 1))
    (hr : Differentiable ℝ r) : Differentiable ℝ (S.spaceTrajectory r)
```

**`ClassicalMechanics.NortonDome.deriv_spaceTrajectory`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L208).

> The velocity of the particle in the plane along a differentiable chart trajectory `r` is
> `(√(1 - r/g²), -√r / g)` times the rate of change `ṙ` of the arc length: the unit tangent
> vector to the profile times `ṙ`.

```lean
lemma deriv_spaceTrajectory (r : Time → EuclideanSpace ℝ (Fin 1)) (hr : Differentiable ℝ r)
    (t : Time) :
    ∂ₜᵥ (S.spaceTrajectory r) t =
      !₂[√(1 - r t 0 / S.g ^ 2) * (∂ₜ r t) 0, -(√(r t 0) / S.g) * (∂ₜ r t) 0]
```

**`ClassicalMechanics.NortonDome.norm_sq_deriv_spaceTrajectory`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L222).

> While the arc length is in range, the square of the speed of the particle along a
> differentiable chart trajectory is `ṙ²`.

```lean
lemma norm_sq_deriv_spaceTrajectory (r : Time → EuclideanSpace ℝ (Fin 1))
    (hr : Differentiable ℝ r) {t : Time} (h0 : 0 ≤ r t 0) (h1 : r t 0 ≤ S.g ^ 2) :
    ‖∂ₜᵥ (S.spaceTrajectory r) t‖ ^ 2 = ((∂ₜ r t) 0) ^ 2
```

## D. The energies and the Lagrangian in physical space

> The chart kinetic energy is that of the particle in the plane while the arc length is in range,
> and the chart potential energy is `m g y` at its height `y` at all times; the chart Lagrangian
> is the constrained Lagrangian `T - V`.

**`ClassicalMechanics.NortonDome.kineticEnergy_eq_space`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L241).

> The chart kinetic energy of the dome along a differentiable chart trajectory is the kinetic
> energy of the particle in physical space, while the arc length is in range.

```lean
lemma kineticEnergy_eq_space (r : Time → EuclideanSpace ℝ (Fin 1)) (hr : Differentiable ℝ r)
    {t : Time} (h0 : 0 ≤ r t 0) (h1 : r t 0 ≤ S.g ^ 2) :
    S.kineticEnergy r t = (1 / (2 : ℝ)) * S.m * ‖∂ₜᵥ (S.spaceTrajectory r) t‖ ^ 2
```

**`ClassicalMechanics.NortonDome.potentialEnergy_eq_height`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L250).

> The chart potential energy of the dome is the gravitational potential `m g y` of the
> particle at its height `y` in physical space.

```lean
lemma potentialEnergy_eq_height (r : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    S.potentialEnergy (r t) = S.m * S.g * S.spaceTrajectory r t 1
```

**`ClassicalMechanics.NortonDome.lagrangian_eq_space`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L257).

> The chart Lagrangian of the dome along a differentiable chart trajectory is the constrained
> Lagrangian of the particle in physical space, while the arc length is in range.

```lean
lemma lagrangian_eq_space (r : Time → EuclideanSpace ℝ (Fin 1)) (hr : Differentiable ℝ r)
    {t : Time} (h0 : 0 ≤ r t 0) (h1 : r t 0 ≤ S.g ^ 2) :
    S.lagrangian t (r t) (∂ₜ r t) =
      (1 / (2 : ℝ)) * S.m * ‖∂ₜᵥ (S.spaceTrajectory r) t‖ ^ 2
        - S.m * S.g * S.spaceTrajectory r t 1
```

**`ClassicalMechanics.NortonDome.energy_eq_space`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean#L267).

> The chart energy of the dome along a differentiable chart trajectory is the total energy of
> the particle in physical space, while the arc length is in range.

```lean
lemma energy_eq_space (r : Time → EuclideanSpace ℝ (Fin 1)) (hr : Differentiable ℝ r)
    {t : Time} (h0 : 0 ≤ r t 0) (h1 : r t 0 ≤ S.g ^ 2) :
    S.energy r t =
      (1 / (2 : ℝ)) * S.m * ‖∂ₜᵥ (S.spaceTrajectory r) t‖ ^ 2
        + S.m * S.g * S.spaceTrajectory r t 1
```

## Depends on

- [The Norton dome](basic.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PhysicalSpace.lean)
