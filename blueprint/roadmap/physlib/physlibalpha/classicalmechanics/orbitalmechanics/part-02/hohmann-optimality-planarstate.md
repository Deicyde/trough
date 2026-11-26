---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannOptimality.PlanarState, ClassicalMechanics.HohmannOptimality.PlanarState.radius, ClassicalMechanics.HohmannOptimality.PlanarState.angular, ClassicalMechanics.HohmannOptimality.PlanarState.radial, ClassicalMechanics.HohmannOptimality.PlanarState.tangent, ClassicalMechanics.HohmannOptimality.PlanarState.energy, ClassicalMechanics.HohmannOptimality.PlanarState.impulse, ClassicalMechanics.HohmannOptimality.PlanarState.radius_sq
statement: formalized
proof: formalized
---

# Planar states for the Hohmann comparison

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Optimality.PlanarState`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PlanarState.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PlanarState.lean): 11 declarations, 7 with a docstring.

> Cartesian velocity jumps can be evaluated in polar components.

## i. Overview

> The endpoint velocity is compared with the prograde circular velocity at the same position. The
> squared Euclidean norm decomposes into a radial square and a tangential difference squared.

## ii. Key results

> - `PlanarState.impulse_polar` gives the main result of this module.

## iv. References

> - [ref: hohmann\_prussing\_1992]. Prussing studies the two-impulse global comparison.

## A. Cartesian and polar endpoint data

**`ClassicalMechanics.HohmannOptimality.PlanarState`**, a structure, [line 42](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PlanarState.lean#L42).

> The Cartesian position and velocity of a particle in the orbital plane.

```lean
structure PlanarState where
  /-- The first Cartesian position coordinate. -/
  x : ℝ
  /-- The second Cartesian position coordinate. -/
  y : ℝ
  /-- The first Cartesian velocity coordinate. -/
  vx : ℝ
  /-- The second Cartesian velocity coordinate. -/
  vy : ℝ
```

**`ClassicalMechanics.HohmannOptimality.PlanarState.radius`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PlanarState.lean#L55).

> The Euclidean distance from the attracting centre.

```lean
def radius (z : PlanarState) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.PlanarState.angular`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PlanarState.lean#L57).

> The signed angular momentum per unit mass.

```lean
def angular (z : PlanarState) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.PlanarState.radial`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PlanarState.lean#L59).

> The component of the velocity along the outward radial direction.

```lean
def radial (z : PlanarState) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.PlanarState.tangent`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PlanarState.lean#L61).

> The velocity component in the prograde tangential direction.

```lean
def tangent (z : PlanarState) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.PlanarState.energy`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PlanarState.lean#L63).

> Twice the sum of kinetic and gravitational potential energy per unit mass.

```lean
def energy (z : PlanarState) (mu : ℝ) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.PlanarState.impulse`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PlanarState.lean#L65).

> Actual Cartesian speed change to/from the same prograde circular velocity.

```lean
def impulse (z : PlanarState) (c : ℝ) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.PlanarState.radius_sq`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PlanarState.lean#L68).

```lean
lemma radius_sq (z : PlanarState) : z.radius^2=z.x^2+z.y^2
```

**`ClassicalMechanics.HohmannOptimality.PlanarState.radius_mul_tangent`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PlanarState.lean#L70).

```lean
lemma radius_mul_tangent (z : PlanarState) (hr : 0 < z.radius) :
    z.radius*z.tangent = z.angular
```

**`ClassicalMechanics.HohmannOptimality.PlanarState.polar_speed_sq`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PlanarState.lean#L74).

```lean
lemma polar_speed_sq (z : PlanarState) (hr : 0 < z.radius) :
    z.radial^2+z.tangent^2=z.vx^2+z.vy^2
```

**`ClassicalMechanics.HohmannOptimality.PlanarState.impulse_polar`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PlanarState.lean#L81).

```lean
lemma impulse_polar (z : PlanarState) (c : ℝ) (hr : 0 < z.radius) :
    z.impulse c = Real.sqrt (z.radial^2+(z.tangent-c)^2)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PlanarState.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/PlanarState.lean)
