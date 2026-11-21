---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannTransfer.position, ClassicalMechanics.HohmannTransfer.velocity, ClassicalMechanics.HohmannTransfer.hasDerivAt_D, ClassicalMechanics.HohmannTransfer.hasDerivAt_position, ClassicalMechanics.HohmannTransfer.hasDerivAt_velocityAtAnomaly_x, ClassicalMechanics.HohmannTransfer.hasDerivAt_velocityAtAnomaly_y, ClassicalMechanics.HohmannTransfer.hasDerivAt_velocity, ClassicalMechanics.HohmannTransfer.deriv_position
statement: formalized
proof: formalized
---

# Time derivatives of the Hohmann ellipse

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Dynamics.Differentiation`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Differentiation.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Differentiation.lean): 10 declarations, 2 with a docstring.

> Kepler time determines the velocity and acceleration.

## i. Overview

> The inverse Kepler clock supplies the anomaly rate. Differentiating the Cartesian coordinates
> yields the velocity and then an acceleration parallel to the displacement.

## ii. Key results

> - `hasDerivAt_velocity` gives the main result of this module.

## iv. References

> - [ref: hohmann\_jpl\_orbital\_mechanics] describes the Hohmann ellipse and its apses.

## A. Differentiation along the ellipse

**`ClassicalMechanics.HohmannTransfer.position`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Differentiation.lean#L42).

> The position on the transfer ellipse at the given physical time.

```lean
def position (p : Parameters) (t : ℝ) : ℂ
```

**`ClassicalMechanics.HohmannTransfer.velocity`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Differentiation.lean#L44).

> The velocity on the transfer ellipse at a given physical time.

```lean
def velocity (p : Parameters) (t : ℝ) : ℂ
```

**`ClassicalMechanics.HohmannTransfer.hasDerivAt_D`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Differentiation.lean#L46).

```lean
lemma hasDerivAt_D (p : Parameters) (u : ℝ) :
    HasDerivAt (D p) (p.e*Real.sin u) u
```

**`ClassicalMechanics.HohmannTransfer.hasDerivAt_position`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Differentiation.lean#L50).

```lean
lemma hasDerivAt_position (p : Parameters) (t : ℝ) :
    HasDerivAt (position p) (velocity p t) t
```

**`ClassicalMechanics.HohmannTransfer.hasDerivAt_velocityAtAnomaly_x`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Differentiation.lean#L59).

```lean
lemma hasDerivAt_velocityAtAnomaly_x (p : Parameters) (u : ℝ) :
    HasDerivAt (fun s => (velocityAtAnomaly p s).re)
      (-p.a*p.n*(Real.cos u-p.e)/(D p u)^2) u
```

**`ClassicalMechanics.HohmannTransfer.hasDerivAt_velocityAtAnomaly_y`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Differentiation.lean#L70).

```lean
lemma hasDerivAt_velocityAtAnomaly_y (p : Parameters) (u : ℝ) :
    HasDerivAt (fun s => (velocityAtAnomaly p s).im)
      (-p.b*p.n*Real.sin u/(D p u)^2) u
```

**`ClassicalMechanics.HohmannTransfer.hasDerivAt_velocity`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Differentiation.lean#L80).

```lean
lemma hasDerivAt_velocity (p : Parameters) (t : ℝ) :
    HasDerivAt (velocity p)
      (-(p.n^2/(D p (anomaly p t))^3) • position p t) t
```

**`ClassicalMechanics.HohmannTransfer.deriv_position`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Differentiation.lean#L93).

```lean
lemma deriv_position (p : Parameters) : deriv (position p) = velocity p
```

**`ClassicalMechanics.HohmannTransfer.position_continuous`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Differentiation.lean#L96).

```lean
lemma position_continuous (p : Parameters) : Continuous (position p)
```

**`ClassicalMechanics.HohmannTransfer.velocity_continuous`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Differentiation.lean#L98).

```lean
lemma velocity_continuous (p : Parameters) : Continuous (velocity p)
```

## Depends on

- [Kepler time for the Hohmann ellipse](hohmann-dynamics-keplerclock.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Differentiation.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Differentiation.lean)
