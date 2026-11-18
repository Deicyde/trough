---
declaration: module
origin: cited
lean: ClassicalMechanics.VisViva, ClassicalMechanics.VisViva.ConfigurationSpace, ClassicalMechanics.VisViva.speedCircular, ClassicalMechanics.VisViva.speedCircular_sq
statement: formalized
proof: formalized
---

# Circular Orbit Vis Viva

The module `Physlib.ClassicalMechanics.OrbitalMechanics.VisViva`, [Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean): 4 declarations, 4 with a docstring.

> The vis-viva equation relates the speed of an orbiting body to its position
> and the mass of the central body. This module defines a simplified version of the
> vis-viva equation that is restricted to circular orbits (v^2 = G M / r).

**`ClassicalMechanics.VisViva`**, a structure, [line 23](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L23).

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

**`ClassicalMechanics.VisViva.ConfigurationSpace`**, a structure, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L34).

> Configuration space for orbital mechanics, defining the orbital radius.

```lean
structure ConfigurationSpace where
  /-- Orbital radius. -/
  r : ℝ
```

**`ClassicalMechanics.VisViva.speedCircular`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L39).

> The orbital speed required for a circular orbit at radius `r`.

```lean
noncomputable def speedCircular (sys : VisViva) (cfg : ConfigurationSpace) : ℝ
```

**`ClassicalMechanics.VisViva.speedCircular_sq`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean#L43).

> Lemma: the square of the circular orbit speed equals G M / r.

```lean
lemma speedCircular_sq (sys : VisViva) (cfg : ConfigurationSpace) (hr : 0 < cfg.r) (hG : 0 < sys.G)
    (hM : 0 < sys.M) :
    (speedCircular sys cfg)^2 = sys.G * sys.M / cfg.r
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/OrbitalMechanics/VisViva.lean)
