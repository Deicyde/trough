---
declaration: module
origin: cited
lean: ClassicalMechanics.HarmonicOscillator.Trajectory, ClassicalMechanics.HarmonicOscillator.Trajectory.coord, ClassicalMechanics.HarmonicOscillator.Trajectory.toSpace, ClassicalMechanics.HarmonicOscillator.Trajectory.coord_apply, ClassicalMechanics.HarmonicOscillator.Trajectory.contMDiff_iff_contDiff_coord, ClassicalMechanics.HarmonicOscillator.Trajectory.velocity, ClassicalMechanics.HarmonicOscillator.Trajectory.mdifferentiableAt_iff_differentiableAt_coord, ClassicalMechanics.HarmonicOscillator.Trajectory.velocity_eq_deriv_coord
statement: formalized
proof: formalized
---

# Geometric trajectories of the harmonic oscillator

The module `Physlib.ClassicalMechanics.HarmonicOscillator.Geometric.Trajectory`, [Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Trajectory.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Trajectory.lean): 8 declarations, 7 with a docstring; 1 private, not shown.

## i. Overview

> A trajectory of the harmonic oscillator is a time-parametrized curve in the configuration
> manifold `Q`. Since this model of `Q` has a single global coordinate valued in
> `EuclideanSpace ℝ (Fin 1)`, every geometric trajectory has an associated coordinate curve.
>
> The coordinate diffeomorphism from `Q` to its model space lets smoothness of a geometric
> trajectory be tested as ordinary smoothness of its coordinate curve.

## ii. Key results

> - `Trajectory` : a curve from `Time` into the configuration manifold.
> - `Trajectory.coord` : the global Euclidean coordinate curve of a trajectory.
> - `Trajectory.toSpace` : the physical-space position along a trajectory.
> - `Trajectory.contMDiff_iff_contDiff_coord` : geometric smoothness of a trajectory is
>   equivalent to ordinary smoothness of its coordinate curve.
> - `Trajectory.velocity` : the geometric velocity of a trajectory as a tangent vector.
> - `Trajectory.velocity_eq_deriv_coord` : in the global coordinate, geometric velocity is
>   represented by the time derivative of the coordinate curve.

## iv. References

> * Ivo Terek, Introductory Variational Calculus on Manifolds, pages 1-2 (Section 1, Basic definitions
>   and examples). [ref: terek\_variational\_manifolds]

## A. The trajectory type and coordinate projection

> A trajectory is a curve in the configuration manifold `Q`, parametrized by `Time`. The
> coordinate projection reads the same curve in the chosen global coordinate, while `toSpace`
> forgets the manifold structure and returns the corresponding physical-space position.

**`ClassicalMechanics.HarmonicOscillator.Trajectory`**, an abbrev, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Trajectory.lean#L63).

> A trajectory of the oscillator: a curve in the configuration manifold `Q`.

```lean
abbrev Trajectory
```

**`ClassicalMechanics.HarmonicOscillator.Trajectory.coord`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Trajectory.lean#L68).

> The coordinate curve of a trajectory: its reading in the global Euclidean coordinate.

```lean
def coord (γ : Trajectory) : Time → EuclideanSpace ℝ (Fin 1)
```

**`ClassicalMechanics.HarmonicOscillator.Trajectory.toSpace`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Trajectory.lean#L72).

> The physical position of the oscillator along a trajectory, over time.

```lean
def toSpace (γ : Trajectory) : Time → Space 1
```

**`ClassicalMechanics.HarmonicOscillator.Trajectory.coord_apply`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Trajectory.lean#L74).

```lean
lemma coord_apply (γ : Trajectory) (t : Time) : coord γ t = (γ t).val
```

## B. Smoothness of trajectories

> Because the global coordinate is a diffeomorphism, composing a trajectory with it preserves
> and reflects manifold smoothness. Since both `Time` and the coordinate model are normed
> spaces, this manifold-smoothness statement then becomes ordinary `ContDiff` smoothness.

**`ClassicalMechanics.HarmonicOscillator.Trajectory.contMDiff_iff_contDiff_coord`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Trajectory.lean#L85).

> A trajectory is smooth as a curve in `Q` iff its coordinate curve is ordinarily smooth.

```lean
lemma contMDiff_iff_contDiff_coord {n : WithTop ℕ∞} (γ : Trajectory) :
    ContMDiff 𝓘(ℝ, Time) 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) n γ ↔
      ContDiff ℝ n (coord γ)
```

## C. Velocity in the tangent bundle

> The velocity of a trajectory at time `t` is the tangent vector obtained by differentiating
> the curve in the direction of the unit time vector. In this one-chart model, the tangent
> space at each configuration is represented by the same Euclidean model space, so the
> geometric velocity can be compared with the derivative of the coordinate curve.

**`ClassicalMechanics.HarmonicOscillator.Trajectory.velocity`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Trajectory.lean#L103).

> The geometric velocity of a trajectory at time `t`: a tangent vector at `γ t`.

```lean
noncomputable def velocity (γ : Trajectory) (t : Time) :
    TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) (γ t)
```

**`ClassicalMechanics.HarmonicOscillator.Trajectory.mdifferentiableAt_iff_differentiableAt_coord`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Trajectory.lean#L110).

> A trajectory is `MDifferentiableAt` a time iff its coordinate curve is ordinarily
> differentiable there, since the two differ by the coordinate diffeomorphism.

```lean
lemma mdifferentiableAt_iff_differentiableAt_coord (γ : Trajectory) (t : Time) :
    MDifferentiableAt 𝓘(ℝ, Time) 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) γ t ↔
      DifferentiableAt ℝ (coord γ) t
```

**`ClassicalMechanics.HarmonicOscillator.Trajectory.velocity_eq_deriv_coord`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Trajectory.lean#L151).

> In the global coordinate, geometric velocity is represented by the time derivative of the
> coordinate curve.

```lean
lemma velocity_eq_deriv_coord (γ : Trajectory) (t : Time) :
    velocity γ t = ∂ₜ (coord γ) t
```

## Depends on

- [Configuration space of the harmonic oscillator](basic.md)
- [Time Derivatives](../../../spaceandtime/time/derivatives.md)

## Sources

- [Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Trajectory.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/Trajectory.lean)
