---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannTransfer.gravity, ClassicalMechanics.HohmannTransfer.norm_position, ClassicalMechanics.HohmannTransfer.position_bounds, ClassicalMechanics.HohmannTransfer.norm_position_pos, ClassicalMechanics.HohmannTransfer.position_ne_zero, ClassicalMechanics.HohmannTransfer.acceleration_coefficient, ClassicalMechanics.HohmannTransfer.hasDerivAt_velocity_newton, ClassicalMechanics.HohmannTransfer.second_deriv_position
statement: formalized
proof: formalized
---

# Newtonian dynamics of the Hohmann ellipse

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Dynamics.Dynamics`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Dynamics.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Dynamics.lean): 10 declarations, 1 with a docstring.

> The transfer coast solves the inverse-square equation.

## i. Overview

> The norm of the position stays positive. Rewriting the radial acceleration with the mean motion
> law gives the Newtonian acceleration at every real time.

## ii. Key results

> - `second_deriv_position` gives the main result of this module.

## iv. References

> - [ref: hohmann\_jpl\_orbital\_mechanics] describes the Hohmann ellipse and its apses.

## A. The Newtonian equation and periodicity

**`ClassicalMechanics.HohmannTransfer.gravity`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Dynamics.lean#L42).

> The inverse-square central acceleration at the given position.

```lean
def gravity (mu : ℝ) (q : ℂ) : ℂ
```

**`ClassicalMechanics.HohmannTransfer.norm_position`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Dynamics.lean#L44).

```lean
lemma norm_position (p : Parameters) (t : ℝ) :
    ‖position p t‖ = radial p (anomaly p t)
```

**`ClassicalMechanics.HohmannTransfer.position_bounds`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Dynamics.lean#L46).

```lean
lemma position_bounds (p : Parameters) (t : ℝ) :
    p.r₁ ≤ ‖position p t‖ ∧ ‖position p t‖ ≤ p.r₂
```

**`ClassicalMechanics.HohmannTransfer.norm_position_pos`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Dynamics.lean#L50).

```lean
lemma norm_position_pos (p : Parameters) (t : ℝ) : 0 < ‖position p t‖
```

**`ClassicalMechanics.HohmannTransfer.position_ne_zero`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Dynamics.lean#L53).

```lean
lemma position_ne_zero (p : Parameters) (t : ℝ) : position p t ≠ 0
```

**`ClassicalMechanics.HohmannTransfer.acceleration_coefficient`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Dynamics.lean#L55).

```lean
lemma acceleration_coefficient (p : Parameters) (u : ℝ) :
    p.n^2/(D p u)^3 = p.mu/(radial p u)^3
```

**`ClassicalMechanics.HohmannTransfer.hasDerivAt_velocity_newton`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Dynamics.lean#L60).

```lean
lemma hasDerivAt_velocity_newton (p : Parameters) (t : ℝ) :
    HasDerivAt (velocity p) (gravity p.mu (position p t)) t
```

**`ClassicalMechanics.HohmannTransfer.second_deriv_position`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Dynamics.lean#L64).

```lean
lemma second_deriv_position (p : Parameters) (t : ℝ) :
    deriv (deriv (position p)) t = -(p.mu/‖position p t‖^3) • position p t
```

**`ClassicalMechanics.HohmannTransfer.position_periodic`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Dynamics.lean#L68).

```lean
lemma position_periodic (p : Parameters) :
    Function.Periodic (position p) (2*p.transferTime)
```

**`ClassicalMechanics.HohmannTransfer.velocity_periodic`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Dynamics.lean#L74).

```lean
lemma velocity_periodic (p : Parameters) :
    Function.Periodic (velocity p) (2*p.transferTime)
```

## Depends on

- [Time derivatives of the Hohmann ellipse](hohmann-dynamics-differentiation.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Dynamics.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Dynamics.lean)
