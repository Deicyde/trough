---
declaration: module
origin: cited
lean: ClassicalMechanics.SimplePendulum.spaceTrajectory, ClassicalMechanics.SimplePendulum.spaceTrajectory_eq, ClassicalMechanics.SimplePendulum.spaceTrajectory_apply_zero, ClassicalMechanics.SimplePendulum.spaceTrajectory_apply_one, ClassicalMechanics.SimplePendulum.norm_spaceTrajectory, ClassicalMechanics.SimplePendulum.deriv_sin_coord, ClassicalMechanics.SimplePendulum.deriv_cos_coord, ClassicalMechanics.SimplePendulum.differentiable_spaceTrajectory
statement: formalized
proof: formalized
---

# The simple pendulum in physical space

The module `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.Geometric.PhysicalSpace`, [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean): 14 declarations, 14 with a docstring.

## i. Overview

> The trajectory module places the bob in the plane along a lifted trajectory; this module fixes a
> simple pendulum `S` and identifies the dynamics of `SimplePendulum.Basic`, written on the
> Euclidean lift of the angle, with the dynamics of the bob moving in physical space. Along a lift
> `θ` the bob is at `S.spaceTrajectory θ`, at the fixed distance `ℓ` from the pivot; its velocity
> is obtained by differentiating the position componentwise, and the square of its speed is
> `ℓ² θ̇²`. The chart kinetic energy `½ I θ̇²` is then exactly the kinetic energy `½ m ‖v‖²` of
> the bob, the chart potential energy `m g ℓ (1 - cos θ)` is exactly the gravitational potential
> `m g h` of the bob with the height `h` measured from the bottom of the swing, and the chart
> Lagrangian is the constrained Lagrangian `T - V` of a point mass moving on the circle of radius
> `ℓ` about the pivot. Velocities in this module are physical-space time derivatives; the
> geometric velocity as a tangent vector to the configuration circle is deferred, as discussed in
> the trajectory module.

## ii. Key results

> - `SimplePendulum.spaceTrajectory` : the bob's position in the plane along a lifted trajectory,
>   with the rod-length constraint `SimplePendulum.norm_spaceTrajectory`.
> - `SimplePendulum.deriv_spaceTrajectory` : the bob's velocity along a lifted trajectory, with
>   the square of its speed `SimplePendulum.norm_sq_deriv_spaceTrajectory`.
> - `SimplePendulum.kineticEnergy_eq_space`, `SimplePendulum.potentialEnergy_eq_height` and
>   `SimplePendulum.lagrangian_eq_space` : the chart kinetic energy, potential energy and
>   Lagrangian are those of the bob in physical space; `SimplePendulum.energy_eq_space` is the
>   corresponding statement for the total energy.

## iv. References

> * `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.Basic` (the lifted dynamics: the energies and
>   the Lagrangian on the Euclidean lift of the angle).
> * `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.Geometric.Trajectory` (trajectories on the
>   configuration circle and the position of the bob along them).
> * Landau & Lifshitz, Mechanics, 3rd ed., §5, Problems 1–3 (pendulum configurations).
>   [ref: landau\_mechanics]

## A. The bob's position along a lifted trajectory

> Fixing a pendulum `S`, the position of the bob in the plane along the trajectory described by a
> lift `θ` of the angle is obtained by composing the lifted trajectory with the map to physical
> space for a rod of length `S.ℓ`. Along it the bob is at `(ℓ sin θ, -ℓ cos θ)`, and since the
> length of the rod is positive the bob stays at distance `ℓ` from the pivot at all times.

**`ClassicalMechanics.SimplePendulum.spaceTrajectory`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean#L77).

> The position of the bob in the plane along the trajectory described by a lift `θ` of the
> angle, for the pendulum `S`.

```lean
noncomputable def spaceTrajectory (θ : Time → EuclideanSpace ℝ (Fin 1)) : Time → Space 2
```

**`ClassicalMechanics.SimplePendulum.spaceTrajectory_eq`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean#L82).

> Along the trajectory described by a lift `θ` of the angle the bob of the pendulum `S` is at
> `(ℓ sin (θ t 0), -ℓ cos (θ t 0))`.

```lean
lemma spaceTrajectory_eq (θ : Time → EuclideanSpace ℝ (Fin 1)) :
    S.spaceTrajectory θ = fun t => ⟨![S.ℓ * Real.sin (θ t 0), -S.ℓ * Real.cos (θ t 0)]⟩
```

**`ClassicalMechanics.SimplePendulum.spaceTrajectory_apply_zero`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean#L87).

> The horizontal position of the bob along a lifted trajectory is `ℓ sin (θ t 0)`.

```lean
lemma spaceTrajectory_apply_zero (θ : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    S.spaceTrajectory θ t 0 = S.ℓ * Real.sin (θ t 0)
```

**`ClassicalMechanics.SimplePendulum.spaceTrajectory_apply_one`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean#L93).

> The vertical position of the bob along a lifted trajectory is `-ℓ cos (θ t 0)`, the pivot
> being the origin and the second axis pointing upwards.

```lean
lemma spaceTrajectory_apply_one (θ : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    S.spaceTrajectory θ t 1 = -S.ℓ * Real.cos (θ t 0)
```

**`ClassicalMechanics.SimplePendulum.norm_spaceTrajectory`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean#L99).

> The rod-length constraint along a lifted trajectory: the bob of the pendulum `S` stays at
> distance `ℓ` from the pivot, the length of the rod being positive.

```lean
lemma norm_spaceTrajectory (θ : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    ‖S.spaceTrajectory θ t‖ = S.ℓ
```

## B. The bob's velocity and speed

> Differentiating the position of the bob componentwise gives its velocity in the plane: along a
> differentiable lift the bob's position is differentiable in time, and its velocity is
> `(ℓ cos θ, ℓ sin θ)` times the angular velocity — the vector tangent to the circle of radius
> `ℓ`, of length `ℓ |θ̇|`. The square of the speed is therefore `ℓ² θ̇²`, which is the identity
> behind the identification of the kinetic energies in the next section. The two chain-rule
> computations for the sine and the cosine of the angle read from a lift are recorded as
> stand-alone lemmas.

**`ClassicalMechanics.SimplePendulum.deriv_sin_coord`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean#L119).

> The time derivative of the sine of the angle read from a lift is the cosine of the angle
> times the angular velocity.

```lean
lemma deriv_sin_coord (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : Differentiable ℝ θ)
    (t : Time) : ∂ₜ (fun s => Real.sin (θ s 0)) t = Real.cos (θ t 0) * (∂ₜ θ t) 0
```

**`ClassicalMechanics.SimplePendulum.deriv_cos_coord`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean#L126).

> The time derivative of the cosine of the angle read from a lift is minus the sine of the
> angle times the angular velocity.

```lean
lemma deriv_cos_coord (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : Differentiable ℝ θ)
    (t : Time) : ∂ₜ (fun s => Real.cos (θ s 0)) t = -Real.sin (θ t 0) * (∂ₜ θ t) 0
```

**`ClassicalMechanics.SimplePendulum.differentiable_spaceTrajectory`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean#L134).

> Along a differentiable lift of the angle the position of the bob is differentiable in
> time.

```lean
lemma differentiable_spaceTrajectory (θ : Time → EuclideanSpace ℝ (Fin 1))
    (hθ : Differentiable ℝ θ) : Differentiable ℝ (S.spaceTrajectory θ)
```

**`ClassicalMechanics.SimplePendulum.deriv_spaceTrajectory`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean#L145).

> The velocity of the bob along a differentiable lift `θ` of the angle is
> `(ℓ cos (θ t 0), ℓ sin (θ t 0))` times the angular velocity: the vector tangent to the circle
> of radius `ℓ` at the position of the bob.

```lean
lemma deriv_spaceTrajectory (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : Differentiable ℝ θ)
    (t : Time) :
    ∂ₜᵥ (S.spaceTrajectory θ) t =
      !₂[S.ℓ * Real.cos (θ t 0) * (∂ₜ θ t) 0, S.ℓ * Real.sin (θ t 0) * (∂ₜ θ t) 0]
```

**`ClassicalMechanics.SimplePendulum.norm_sq_deriv_spaceTrajectory`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean#L161).

> The square of the speed of the bob along a differentiable lift of the angle is `ℓ² θ̇²`.

```lean
lemma norm_sq_deriv_spaceTrajectory (θ : Time → EuclideanSpace ℝ (Fin 1))
    (hθ : Differentiable ℝ θ) (t : Time) :
    ‖∂ₜᵥ (S.spaceTrajectory θ) t‖ ^ 2 = S.ℓ ^ 2 * ((∂ₜ θ t) 0) ^ 2
```

## C. The energies and the Lagrangian in physical space

> The identities of the previous section identify the energies of `SimplePendulum.Basic`, written
> on the lift of the angle, with the energies of the bob in the plane. The chart kinetic energy
> `½ I θ̇²` is the kinetic energy `½ m ‖v‖²` of the bob, since `I = m ℓ²` and the square of the
> speed is `ℓ² θ̇²`; the chart potential energy `m g ℓ (1 - cos θ)` is the gravitational
> potential `m g h` of the bob, the height `h` above the bottom of the swing being the vertical
> position of the bob plus `ℓ`. Consequently the chart Lagrangian is the constrained Lagrangian
> `T - V` of a point mass moving on the circle of radius `ℓ`, and the chart energy is its total
> energy `T + V`.

**`ClassicalMechanics.SimplePendulum.kineticEnergy_eq_space`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean#L186).

> The chart kinetic energy of the pendulum along a differentiable lift of the angle is the
> kinetic energy of the bob in physical space.

```lean
lemma kineticEnergy_eq_space (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : Differentiable ℝ θ)
    (t : Time) :
    S.kineticEnergy θ t = (1 / (2 : ℝ)) * S.m * ‖∂ₜᵥ (S.spaceTrajectory θ) t‖ ^ 2
```

**`ClassicalMechanics.SimplePendulum.potentialEnergy_eq_height`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean#L197).

> The chart potential energy of the pendulum is the gravitational potential of the bob in
> physical space, normalized to vanish at the bottom of the swing: the height of the bob above
> the bottom is its vertical position plus `ℓ`.

```lean
lemma potentialEnergy_eq_height (θ : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    S.potentialEnergy (θ t) = S.m * S.g * (S.spaceTrajectory θ t 1 + S.ℓ)
```

**`ClassicalMechanics.SimplePendulum.lagrangian_eq_space`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean#L205).

> The chart Lagrangian of the pendulum along a differentiable lift of the angle is the
> constrained Lagrangian of the bob in physical space: the kinetic energy of the point mass
> minus its gravitational potential.

```lean
lemma lagrangian_eq_space (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : Differentiable ℝ θ)
    (t : Time) :
    S.lagrangian t (θ t) (∂ₜ θ t) =
      (1 / (2 : ℝ)) * S.m * ‖∂ₜᵥ (S.spaceTrajectory θ) t‖ ^ 2
        - S.m * S.g * (S.spaceTrajectory θ t 1 + S.ℓ)
```

**`ClassicalMechanics.SimplePendulum.energy_eq_space`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean#L216).

> The chart energy of the pendulum along a differentiable lift of the angle is the total
> energy of the bob in physical space: the kinetic energy of the point mass plus its
> gravitational potential.

```lean
lemma energy_eq_space (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : Differentiable ℝ θ)
    (t : Time) :
    S.energy θ t =
      (1 / (2 : ℝ)) * S.m * ‖∂ₜᵥ (S.spaceTrajectory θ) t‖ ^ 2
        + S.m * S.g * (S.spaceTrajectory θ t 1 + S.ℓ)
```

## Depends on

- [The simple gravity pendulum](basic.md)
- [Geometric trajectories of the simple pendulum](geometric-trajectory.md)

## Sources

- [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/PhysicalSpace.lean)
