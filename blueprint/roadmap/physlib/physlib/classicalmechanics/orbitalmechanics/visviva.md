---
declaration: module
origin: cited
lean: ClassicalMechanics.VisViva, ClassicalMechanics.VisViva.ConfigurationSpace, ClassicalMechanics.VisViva.speedCircular, ClassicalMechanics.VisViva.speedCircular_sq, ClassicalMechanics.VisViva.speedCircular_eq_radius_mul_angularRate
statement: formalized
proof: formalized
---

# Circular Orbit Vis Viva

The module `Physlib.ClassicalMechanics.OrbitalMechanics.VisViva`, [Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean): 5 declarations, 5 with a docstring.

> The vis-viva equation relates the speed of an orbiting body to its position
> and the mass of the central body.

## i. Overview

> The circular-orbit case of the vis-viva equation gives the speed from the radius and the
> gravitational parameter. It also relates the speed to the positive angular rate.

## ii. Key results

> - `VisViva.speedCircular_sq` gives the squared speed of a circular orbit.
> - `VisViva.speedCircular_eq_radius_mul_angularRate` expresses the speed using the angular rate.

## iv. References

> * None.

## A. System parameters and orbital radius

### A.1. System parameters

**`ClassicalMechanics.VisViva`**, a structure, [line 51](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L51).

> System parameters for the vis-viva equation in circular orbital mechanics.

```lean
structure VisViva where
  /-- Gravitational constant. -/
  G : ℝ
  /-- Central mass body. -/
  M : ℝ
  /-- Orbiting mass body. -/
  m : ℝ
```

### A.2. Orbital radius

**`ClassicalMechanics.VisViva.ConfigurationSpace`**, a structure, [line 66](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L66).

> Configuration space for orbital mechanics, defining the orbital radius.

```lean
structure ConfigurationSpace where
  /-- Orbital radius. -/
  r : ℝ
```

## B. Circular orbit speed

### B.1. Speed from the vis-viva equation

**`ClassicalMechanics.VisViva.speedCircular`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L77).

> The orbital speed required for a circular orbit at radius `r`.

```lean
noncomputable def speedCircular (sys : VisViva) (cfg : ConfigurationSpace) : ℝ
```

**`ClassicalMechanics.VisViva.speedCircular_sq`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L81).

> Lemma: the square of the circular orbit speed equals G M / r.

```lean
lemma speedCircular_sq (sys : VisViva) (cfg : ConfigurationSpace) (hr : 0 < cfg.r) (hG : 0 < sys.G)
    (hM : 0 < sys.M) :
    (speedCircular sys cfg)^2 = sys.G * sys.M / cfg.r
```

### B.2. Relation to the angular rate

**`ClassicalMechanics.VisViva.speedCircular_eq_radius_mul_angularRate`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L91).

> The circular speed equals the orbital radius times the positive circular angular rate.

```lean
lemma speedCircular_eq_radius_mul_angularRate (sys : VisViva) (cfg : ConfigurationSpace)
    (hr : 0 < cfg.r) (hG : 0 < sys.G) (hM : 0 < sys.M) :
    sys.speedCircular cfg = cfg.r * Real.sqrt (sys.G * sys.M / cfg.r ^ 3)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean)
