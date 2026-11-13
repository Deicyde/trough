---
declaration: module
origin: cited
lean: IsPeano
statement: formalized
proof: formalized
---

# Peano's existence theorem (statements)

The module `PhyslibAlpha.ClassicalMechanics.NortonDome.PeanoExistence`, [PhyslibAlpha/ClassicalMechanics/NortonDome/PeanoExistence.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PeanoExistence.lean): 1 declaration, 1 with a docstring.

> Statements of Peano's existence theorem for ODEs, pending its proof in Mathlib.

## i. Overview

> Peano's existence theorem: the initial value problem `x' = f (t, x)`, `x t₀ = x₀` has a
> solution on a closed time interval whenever `f` is continuous on the product of that interval
> with a closed ball about `x₀` and the interval is short enough for the solution to stay in the
> ball. No Lipschitz condition is asked, and only existence is guaranteed.
>
> The theorem is not yet in Mathlib. This file records the hypotheses and the two forms of the
> conclusion as stated in the Mathlib pull request
> [#42148](https://github.com/leanprover-community/mathlib4/pull/42148), by Julian Rolfes,
> Luke Schleef, Philipp Svinger, Paul Niessner and Florian Grube, as
> informal lemmas. Names and namespace are those of the pull
> request, so that once it is merged this file can be deleted and its uses redirected to
> Mathlib's `IsPeano` by a change of imports. `NortonDome.NewtonianSystem` uses the theorem to
> show that a Newtonian system with a continuous force has local solutions.

## ii. Key results

> - `IsPeano` collects the hypotheses: the initial time lies in the interval, the vector field is
>   continuous on the cylinder, bounded by `L` there, and `L` times the length of the interval on
>   either side of `t₀` is at most the radius `r` of the ball.
> - `IsPeano.exists_eq_forall_mem_Icc_eq_integral` is the theorem in integral form.
> - `IsPeano.exists_eq_forall_mem_Icc_hasDerivWithinAt₀` is the theorem in differential form.

## iv. References

> - Mathlib pull request [#42148](https://github.com/leanprover-community/mathlib4/pull/42148),
>   `Mathlib/Analysis/ODE/Peano.lean`.
> - Hartman, P., *Ordinary Differential Equations*, 2nd ed., SIAM (2002), Theorem II.2.1.

## A. The hypotheses

**`IsPeano`**, a structure, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PeanoExistence.lean#L65).

> The hypotheses for Peano's existence theorem on a closed time interval and a closed ball.

```lean
structure IsPeano {E : Type*} [NormedAddCommGroup E]
    (f : ℝ × E → E) (tmin tmax t₀ : ℝ) (x₀ : E) (r L : ℝ≥0) : Prop where
  /-- The initial time belongs to the time interval. -/
  t₀_mem : t₀ ∈ Icc tmin tmax
  /-- The vector field is continuous on the set product of a time interval and a closed ball. -/
  continuousOn : ContinuousOn f (Icc tmin tmax ×ˢ closedBall x₀ r)
  /-- `L` is an upper bound of the norm of the vector field. -/
  norm_le : ∀ t ∈ Icc tmin tmax, ∀ x ∈ closedBall x₀ r, ‖f (t, x)‖ ≤ L
  /-- The time interval of validity. -/
  mul_max_le : L * max (tmax - t₀) (t₀ - tmin) ≤ r
```

## B. The theorem

## Depends on

- [Physlib.Meta.Informal.Basic](../../../physlib/meta/informal/basic.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/NortonDome/PeanoExistence.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/PeanoExistence.lean)
