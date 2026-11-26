---
declaration: module
origin: cited
lean: ClassicalMechanics.VisViva, ClassicalMechanics.VisViva.ConfigurationSpace, ClassicalMechanics.VisViva.speedCircular, ClassicalMechanics.VisViva.speedCircular_sq, ClassicalMechanics.VisViva.speedCircular_eq_radius_mul_angularRate, ClassicalMechanics.VisViva.periodTwoBody, ClassicalMechanics.VisViva.periodTwoBody_sq, ClassicalMechanics.VisViva.reflexRadius
statement: formalized
proof: formalized
---

# Vis viva for circular orbits and the escape speed

The module `Physlib.ClassicalMechanics.OrbitalMechanics.VisViva`, [Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean): 19 declarations, 19 with a docstring.

> The vis-viva equation relates the speed of an orbiting body to its position
> and the mass of the central body.

## i. Overview

> The circular-orbit case of the vis-viva equation gives the speed from the radius and the
> gravitational parameter. It also relates the speed to the positive angular rate.
>
> Two mass conventions appear. The circular speed, the specific orbital energy and the escape speed
> use the gravitational parameter `G M` of the central body alone, the limit of a test body with
> `m ≪ M`. The period of the two-body orbit and the reflex motion use the total mass `M + m`.
>
> For two bodies of masses `M` and `m` on a circular orbit of separation `r`, the central body also
> moves, on a circle about the barycentre. Its reflex speed, written with the orbital period from
> Kepler's third law, is the radial-velocity semi-amplitude of a star with a planet on an edge-on
> circular orbit.
>
> The specific orbital energy `v² / 2 - G M / r` is negative on a circular orbit, where it equals
> half the potential energy per unit mass, and vanishes at the escape speed `√(2 G M / r)`, which
> is `√2` times the circular speed at the same radius.

## ii. Key results

> - `VisViva.speedCircular_sq` gives the squared speed of a circular orbit.
> - `VisViva.speedCircular_eq_radius_mul_angularRate` expresses the speed using the angular rate.
> - `VisViva.periodTwoBody_sq` is Kepler's third law for a circular two-body orbit.
> - `VisViva.reflexSpeed_pow_three` gives the cube of the reflex speed of the central body in terms of
>   the period, `K³ = 2π G m³ / (P (M + m)²)`.
> - `VisViva.specificOrbitalEnergy_speedCircular` and `VisViva.specificOrbitalEnergy_speedEscape`
>   evaluate the specific orbital energy on a circular orbit and at the escape speed.
> - `VisViva.speedEscape_eq_sqrt_two_mul_speedCircular` and `VisViva.speedCircular_lt_speedEscape`
>   relate the escape speed to the circular speed.

## iv. References

> * Landau & Lifshitz, Mechanics, 3rd ed., sections 13 and 15. [ref: landau\_mechanics]
> * Perryman, The Exoplanet Handbook, 2nd ed., chapter 2. [ref: perryman\_exoplanet\_handbook]

## A. System parameters and orbital radius

### A.1. System parameters

**`ClassicalMechanics.VisViva`**, a structure, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L79).

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

**`ClassicalMechanics.VisViva.ConfigurationSpace`**, a structure, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L94).

> Configuration space for orbital mechanics, defining the orbital radius.

```lean
structure ConfigurationSpace where
  /-- Orbital radius. -/
  r : ℝ
```

## B. Circular orbit speed

### B.1. Speed from the vis-viva equation

**`ClassicalMechanics.VisViva.speedCircular`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L105).

> The orbital speed required for a circular orbit at radius `r`.

```lean
noncomputable def speedCircular (sys : VisViva) (cfg : ConfigurationSpace) : ℝ
```

**`ClassicalMechanics.VisViva.speedCircular_sq`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L109).

> Lemma: the square of the circular orbit speed equals G M / r.

```lean
lemma speedCircular_sq (sys : VisViva) (cfg : ConfigurationSpace) (hr : 0 < cfg.r) (hG : 0 < sys.G)
    (hM : 0 < sys.M) :
    (speedCircular sys cfg)^2 = sys.G * sys.M / cfg.r
```

### B.2. Relation to the angular rate

**`ClassicalMechanics.VisViva.speedCircular_eq_radius_mul_angularRate`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L119).

> The circular speed equals the orbital radius times the positive circular angular rate.

```lean
lemma speedCircular_eq_radius_mul_angularRate (sys : VisViva) (cfg : ConfigurationSpace)
    (hr : 0 < cfg.r) (hG : 0 < sys.G) (hM : 0 < sys.M) :
    sys.speedCircular cfg = cfg.r * Real.sqrt (sys.G * sys.M / cfg.r ^ 3)
```

## C. Reflex motion of the central body

### C.1. The period of a two-body orbit

**`ClassicalMechanics.VisViva.periodTwoBody`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L136).

> The period of a circular orbit of two bodies of masses `M` and `m` at separation `r`, from
> Kepler's third law with the total mass `M + m`.

```lean
noncomputable def periodTwoBody (sys : VisViva) (cfg : ConfigurationSpace) : ℝ
```

**`ClassicalMechanics.VisViva.periodTwoBody_sq`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L140).

> Kepler's third law for a circular two-body orbit, `P² G (M + m) = 4π² r³`.

```lean
lemma periodTwoBody_sq (sys : VisViva) (cfg : ConfigurationSpace) (hr : 0 < cfg.r)
    (hG : 0 < sys.G) (hM : 0 < sys.M) (hm : 0 < sys.m) :
    sys.periodTwoBody cfg ^ 2 * (sys.G * (sys.M + sys.m)) = 4 * Real.pi ^ 2 * cfg.r ^ 3
```

### C.2. The reflex speed

**`ClassicalMechanics.VisViva.reflexRadius`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L153).

> The distance of the central body from the barycentre, `m r / (M + m)`.

```lean
noncomputable def reflexRadius (sys : VisViva) (cfg : ConfigurationSpace) : ℝ
```

**`ClassicalMechanics.VisViva.reflexSpeed`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L159).

> The reflex speed of the central body, which goes once round a circle of radius
> `reflexRadius` per orbital period. For a star with a planet on an edge-on circular orbit, this is
> the radial-velocity semi-amplitude `K`.

```lean
noncomputable def reflexSpeed (sys : VisViva) (cfg : ConfigurationSpace) : ℝ
```

**`ClassicalMechanics.VisViva.reflexSpeed_pow_three`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L164).

> The reflex speed in terms of the period, `K³ = 2π G m³ / (P (M + m)²)`. Taking the cube root
> gives the radial-velocity semi-amplitude `K = (2π G / P)^{1/3} m / (M + m)^{2/3}`.

```lean
lemma reflexSpeed_pow_three (sys : VisViva) (cfg : ConfigurationSpace) (hr : 0 < cfg.r)
    (hG : 0 < sys.G) (hM : 0 < sys.M) (hm : 0 < sys.m) :
    sys.reflexSpeed cfg ^ 3 =
      2 * Real.pi * sys.G * sys.m ^ 3 / (sys.periodTwoBody cfg * (sys.M + sys.m) ^ 2)
```

## D. Escape speed

### D.1. The specific orbital energy

**`ClassicalMechanics.VisViva.specificOrbitalEnergy`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L185).

> The specific orbital energy of the orbiting body moving at speed `v` at radius `r`: the
> kinetic energy per unit mass `v² / 2` plus the gravitational potential energy per unit mass
> `-G M / r`.

```lean
noncomputable def specificOrbitalEnergy (sys : VisViva) (cfg : ConfigurationSpace) (v : ℝ) : ℝ
```

**`ClassicalMechanics.VisViva.specificOrbitalEnergy_speedCircular`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L190).

> On a circular orbit the specific orbital energy is `-(G M / r) / 2`, half the potential
> energy per unit mass.

```lean
lemma specificOrbitalEnergy_speedCircular (sys : VisViva) (cfg : ConfigurationSpace)
    (hr : 0 < cfg.r) (hG : 0 < sys.G) (hM : 0 < sys.M) :
    sys.specificOrbitalEnergy cfg (sys.speedCircular cfg) = -(sys.G * sys.M / cfg.r) / 2
```

### D.2. The escape speed

**`ClassicalMechanics.VisViva.speedEscape`**, a def, [line 202](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L202).

> The escape speed from radius `r`, `√(2 G M / r)`: the speed at which the specific orbital
> energy vanishes, so that the body can just reach infinite separation.

```lean
noncomputable def speedEscape (sys : VisViva) (cfg : ConfigurationSpace) : ℝ
```

**`ClassicalMechanics.VisViva.speedEscape_sq`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L206).

> The square of the escape speed equals `2 G M / r`.

```lean
lemma speedEscape_sq (sys : VisViva) (cfg : ConfigurationSpace) (hr : 0 < cfg.r)
    (hG : 0 < sys.G) (hM : 0 < sys.M) :
    sys.speedEscape cfg ^ 2 = 2 * sys.G * sys.M / cfg.r
```

**`ClassicalMechanics.VisViva.speedEscape_pos`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L212).

> The escape speed is positive.

```lean
lemma speedEscape_pos (sys : VisViva) (cfg : ConfigurationSpace) (hr : 0 < cfg.r)
    (hG : 0 < sys.G) (hM : 0 < sys.M) :
    0 < sys.speedEscape cfg
```

**`ClassicalMechanics.VisViva.specificOrbitalEnergy_speedEscape`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L218).

> At the escape speed the specific orbital energy vanishes.

```lean
lemma specificOrbitalEnergy_speedEscape (sys : VisViva) (cfg : ConfigurationSpace)
    (hr : 0 < cfg.r) (hG : 0 < sys.G) (hM : 0 < sys.M) :
    sys.specificOrbitalEnergy cfg (sys.speedEscape cfg) = 0
```

### D.3. Relation to the circular speed

**`ClassicalMechanics.VisViva.speedEscape_eq_sqrt_two_mul_speedCircular`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L229).

> The escape speed is `√2` times the circular speed at the same radius.

```lean
lemma speedEscape_eq_sqrt_two_mul_speedCircular (sys : VisViva) (cfg : ConfigurationSpace) :
    sys.speedEscape cfg = Real.sqrt 2 * sys.speedCircular cfg
```

**`ClassicalMechanics.VisViva.speedEscape_sq_eq_two_mul_speedCircular_sq`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L236).

> The square of the escape speed is twice the square of the circular speed.

```lean
lemma speedEscape_sq_eq_two_mul_speedCircular_sq (sys : VisViva) (cfg : ConfigurationSpace) :
    sys.speedEscape cfg ^ 2 = 2 * sys.speedCircular cfg ^ 2
```

**`ClassicalMechanics.VisViva.speedCircular_lt_speedEscape`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L242).

> A body on a circular orbit moves more slowly than the escape speed: it is bound.

```lean
lemma speedCircular_lt_speedEscape (sys : VisViva) (cfg : ConfigurationSpace) (hr : 0 < cfg.r)
    (hG : 0 < sys.G) (hM : 0 < sys.M) :
    sys.speedCircular cfg < sys.speedEscape cfg
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean)
