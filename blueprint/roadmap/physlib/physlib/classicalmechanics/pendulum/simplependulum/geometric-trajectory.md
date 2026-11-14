---
declaration: module
origin: cited
lean: ClassicalMechanics.SimplePendulum.Trajectory, ClassicalMechanics.SimplePendulum.Trajectory.ofLift, ClassicalMechanics.SimplePendulum.Trajectory.ofLift_apply, ClassicalMechanics.SimplePendulum.Trajectory.ofLift_eq_iff, ClassicalMechanics.SimplePendulum.Trajectory.ofLift_add_int_mul_two_pi, ClassicalMechanics.SimplePendulum.Trajectory.continuous_ofLift, ClassicalMechanics.SimplePendulum.Trajectory.contMDiff_ofLift, ClassicalMechanics.SimplePendulum.Trajectory.toSpace
statement: formalized
proof: formalized
---

# Geometric trajectories of the simple pendulum

The module `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.Geometric.Trajectory`, [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Trajectory.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Trajectory.lean): 11 declarations, 11 with a docstring.

## i. Overview

> A trajectory of the simple pendulum is a time-parametrized curve in the configuration circle.
> The dynamics of the pendulum is written for a real-valued lift of the angle;
> `Trajectory.ofLift` sends such a lift to the trajectory it describes on the circle, by applying
> the angular lift `ConfigurationSpace.ofAngle` at each time. Two lifts describe the same
> trajectory exactly when at each time they differ by a whole number of turns, a smooth lift
> describes a smooth curve in the circle, and composing with `ConfigurationSpace.toSpace` places
> the bob in the plane along the trajectory, at distance `|ℓ|` from the pivot at all times.
>
> The geometric velocity — the `mfderiv` of a trajectory as a tangent vector to the circle, read
> in its stereographic charts — is left for a later module, as is the smooth identification of
> the configuration space with `Circle`; in this module and the next, velocities are computed in
> physical space, on the position of the bob in the plane.

## ii. Key results

> - `Trajectory` : a trajectory of the pendulum, a curve in the configuration circle.
> - `Trajectory.ofLift` : the trajectory described by a lift of the angle, with
>   `Trajectory.ofLift_add_int_mul_two_pi` and `Trajectory.ofLift_eq_iff` making precise that two
>   lifts describe the same trajectory exactly when they differ by whole turns at each time.
> - `Trajectory.contMDiff_ofLift` : the trajectory described by a `C^n` lift is a `C^n` curve in
>   the configuration circle; `Trajectory.continuous_ofLift` is the topological counterpart.
> - `Trajectory.toSpace` : the physical position of the bob along a trajectory, with the
>   rod-length constraint `Trajectory.norm_toSpace`.

## iv. References

> * `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.Geometric.Basic` (the configuration circle,
>   the angular lift `ofAngle` and the map to physical space).
> * `Physlib.ClassicalMechanics.HarmonicOscillator.Geometric.Trajectory` (the corresponding trajectory
>   module of the harmonic oscillator, whose structure this module follows).

## A. The trajectory type and the lift

> A trajectory is a curve in the configuration circle, parametrized by `Time`. The dynamics is
> written for the Euclidean lift `Time → EuclideanSpace ℝ (Fin 1)` of the angle; `ofLift` sends a
> lift to the trajectory it describes, and the lift is faithful up to a whole number of turns at
> each time: shifting a lift by `2π n` gives the same trajectory, and two lifts give the same
> trajectory exactly when at each time they differ by some whole number of turns (possibly a
> different number at different times).

**`ClassicalMechanics.SimplePendulum.Trajectory`**, an abbrev, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Trajectory.lean#L76).

> A trajectory of the pendulum: a curve in the configuration space.

```lean
abbrev Trajectory
```

**`ClassicalMechanics.SimplePendulum.Trajectory.ofLift`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Trajectory.lean#L81).

> The trajectory on the circle described by a lift `θ` of the angle.

```lean
def ofLift (θ : Time → EuclideanSpace ℝ (Fin 1)) : Trajectory
```

**`ClassicalMechanics.SimplePendulum.Trajectory.ofLift_apply`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Trajectory.lean#L86).

> At time `t` the trajectory described by a lift `θ` of the angle is the configuration at
> angle `θ t 0`.

```lean
lemma ofLift_apply (θ : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    ofLift θ t = ConfigurationSpace.ofAngle (θ t 0)
```

**`ClassicalMechanics.SimplePendulum.Trajectory.ofLift_eq_iff`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Trajectory.lean#L91).

> Two lifts of the angle describe the same trajectory exactly when at each time they differ by
> a whole number of turns.

```lean
lemma ofLift_eq_iff (θ₁ θ₂ : Time → EuclideanSpace ℝ (Fin 1)) :
    ofLift θ₁ = ofLift θ₂ ↔ ∀ t, ∃ n : ℤ, θ₂ t 0 = θ₁ t 0 + n * (2 * Real.pi)
```

**`ClassicalMechanics.SimplePendulum.Trajectory.ofLift_add_int_mul_two_pi`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Trajectory.lean#L97).

> Shifting a lift of the angle by a whole number of turns leaves the described trajectory
> unchanged.

```lean
lemma ofLift_add_int_mul_two_pi (θ : Time → EuclideanSpace ℝ (Fin 1)) (n : ℤ) :
    ofLift (fun t => θ t + (n * (2 * Real.pi)) • EuclideanSpace.single 0 1) = ofLift θ
```

## B. Smoothness of lifted trajectories

> The angular lift `ConfigurationSpace.ofAngle` is analytic, so the trajectory described by a lift
> inherits the regularity of the lift: a continuous lift describes a continuous trajectory, and a
> `C^n` lift describes a `C^n` curve in the configuration circle. Since `Time` is a normed space,
> smoothness of the lift is ordinary `ContDiff` smoothness, while smoothness of the trajectory is
> manifold smoothness into the circle.

**`ClassicalMechanics.SimplePendulum.Trajectory.continuous_ofLift`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Trajectory.lean#L116).

> The trajectory described by a continuous lift of the angle is continuous.

```lean
lemma continuous_ofLift {θ : Time → EuclideanSpace ℝ (Fin 1)} (hθ : Continuous θ) :
    Continuous (ofLift θ)
```

**`ClassicalMechanics.SimplePendulum.Trajectory.contMDiff_ofLift`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Trajectory.lean#L123).

> The trajectory described by a `C^n` lift of the angle is a `C^n` curve in the configuration
> circle.

```lean
lemma contMDiff_ofLift {n : WithTop ℕ∞} {θ : Time → EuclideanSpace ℝ (Fin 1)}
    (hθ : ContDiff ℝ n θ) : ContMDiff 𝓘(ℝ, Time) (𝓡 1) n (ofLift θ)
```

## C. Physical position along a trajectory

> Composing a trajectory with the map to physical space places the bob in the plane at each time.
> Along the trajectory described by a lift the bob is at `(ℓ sin θ, -ℓ cos θ)`, and the rod-length
> constraint holds at all times: the bob stays on the circle of radius `|ℓ|` about the pivot.

**`ClassicalMechanics.SimplePendulum.Trajectory.toSpace`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Trajectory.lean#L139).

> The physical position of the bob along a trajectory, over time, for a rod of length `ℓ`.

```lean
def toSpace (ℓ : ℝ) (γ : Trajectory) (t : Time) : Space 2
```

**`ClassicalMechanics.SimplePendulum.Trajectory.toSpace_ofLift`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Trajectory.lean#L143).

> Along the trajectory described by a lift `θ` of the angle the bob is at
> `(ℓ sin (θ t 0), -ℓ cos (θ t 0))`.

```lean
lemma toSpace_ofLift (ℓ : ℝ) (θ : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    toSpace ℓ (ofLift θ) t = ⟨![ℓ * Real.sin (θ t 0), -ℓ * Real.cos (θ t 0)]⟩
```

**`ClassicalMechanics.SimplePendulum.Trajectory.norm_toSpace`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Trajectory.lean#L149).

> The rod-length constraint along a trajectory: the bob stays at distance `|ℓ|` from the
> pivot.

```lean
lemma norm_toSpace (ℓ : ℝ) (γ : Trajectory) (t : Time) : ‖toSpace ℓ γ t‖ = |ℓ|
```

**`ClassicalMechanics.SimplePendulum.Trajectory.continuous_toSpace`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Trajectory.lean#L154).

> The physical position of the bob along a continuous trajectory depends continuously on the
> time.

```lean
lemma continuous_toSpace (ℓ : ℝ) {γ : Trajectory} (hγ : Continuous γ) :
    Continuous (toSpace ℓ γ)
```

## Depends on

- [Configuration space of the simple pendulum](geometric-basic.md)
- [Time as an inner product space](../../../spaceandtime/time/innerproductspace.md)

## Sources

- [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Trajectory.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Trajectory.lean)
